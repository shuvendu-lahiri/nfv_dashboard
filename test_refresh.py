import json
import re
import unittest
from datetime import timedelta
from unittest.mock import patch

import refresh


BODY = """# NFV: 1 refuted, 0 verified in PR #2

refuted: 1 \u00b7 verified: 0 \u00b7 resources exhausted: 0 \u00b7 type-check/audit failure: 0

PR head `abcdef123456`, base `012345678901` \u00b7 [run and evidence](https://github.com/shuvendu-lahiri/litebox/actions/runs/100)

### P1
**Intended property:** Every x &lt; limit is retained.

**Outcome: refuted**

**Input on which it fails:** x = 0.

**Sketch of the failure:** The translated condition excludes zero.
"""


def comment(body=BODY, comment_id=200, date="2026-10-20T00:00:00Z"):
    return {"id": comment_id, "body": body, "issue_url": "https://api.github.com/repos/shuvendu-lahiri/litebox/issues/2",
            "created_at": date, "updated_at": date, "user": {"login": "github-actions[bot]"}}


def pr(number=2):
    return {"number": number, "title": "Example", "state": "open", "merged_at": None,
            "head": {"ref": f"branch-{number}", "sha": "abcdef123456" + "0" * 28}}


def run(number=2, run_id=100, conclusion="success"):
    return {"id": run_id, "pull_requests": [{"number": number,
             "url": f"https://api.github.com/repos/shuvendu-lahiri/litebox/pulls/{number}"}],
            "head_branch": f"branch-{number}", "head_repository": {"full_name": refresh.REPOSITORY},
            "created_at": "2026-10-20T00:00:00Z", "status": "completed", "conclusion": conclusion, "run_attempt": 1,
            "html_url": f"{refresh.WEB}/actions/runs/{run_id}"}


class RefreshTests(unittest.TestCase):
    def test_replay_headers_map_original_pr_without_backlinks(self):
        headers = (
            "Historical source replay of change 99 from microsoft/litebox.\n",
            "Historical source replay of change 99 from microsoft/litebox, selected for a trial.",
            "Read-only source replay of microsoft/litebox#99 at `abc`.",
            "Replay of microsoft/litebox#99 (upstream head `abc`).",
            "Historical replay of change 99, opened in an approved batch.",
            "**Parser-fix rerun:** Recorded configuration.\n\n---\n\n"
            "Replay of historical change 99 for an approved NFV pilot.",
        )
        for header in headers:
            with self.subTest(header=header):
                data = refresh.build([{**pr(), "body": header}], [comment()], [run()], "snapshot")
                entry = data["prs"][0]
                self.assertEqual(99, entry["source_number"])
                self.assertEqual("https://redirect.github.com/microsoft/litebox/pull/99",
                                 entry["source_url"])
                self.assertIn("[Original PR 99](https://redirect.github.com/", refresh.render_markdown(data))
                self.assertIn("<th>Original PR</th>", refresh.render_html(data))

    def test_unrelated_or_embedded_source_references_are_not_guessed(self):
        for body in ("Replay of other/repo#99", "User prose\nReplay of microsoft/litebox#99",
                     "Fix issue #99", None):
            with self.subTest(body=body):
                data = refresh.build([{**pr(), "body": body}], [], [run()], "snapshot")
                self.assertNotIn("source_url", data["prs"][0])
                self.assertIn("| Not mapped |", refresh.render_markdown(data))

    def test_source_languages_survive_hub_and_project_rendering(self):
        data = refresh.build([pr()], [comment()], [run()], "snapshot")
        self.assertEqual(["Rust", "C"], data["languages"])
        self.assertIn("Main source languages:** Rust, C.", refresh.render_markdown(data))
        combined = refresh.hub([data])
        self.assertEqual(data["languages"], combined["repositories"][0]["languages"])
        self.assertIn('<td class="languages">Rust, C</td>', refresh.render_html(combined, "hub.html"))
        self.assertIn("data.languages.join", refresh.render_html(data))

    def fix_evidence(self, report, checked=True):
        return {
            "schema": 1, "repository": refresh.REPOSITORY, "reports": [{
                "run_id": report["run_id"], "comment_id": report["comment_id"],
                "body_sha256": report["body_sha256"], "status": "complete", "refutations": 1,
                "checked": [{"finding_id": "finding", "patch_sha256": "a" * 64,
                             "patch": "followups/finding/1/fix/candidate.patch"}] if checked else [],
            }],
        }

    def test_checked_fix_counts_are_bound_to_latest_published_report(self):
        data = refresh.build([pr()], [comment()], [run()], "snapshot")
        evidence = self.fix_evidence(data["prs"][0]["latest_report"])
        refresh.apply_fix_evidence(data, evidence)
        self.assertEqual(1, data["summary"]["checked_fixes"])
        self.assertEqual(0, data["summary"]["fix_unknown"])
        self.assertEqual(1, data["summary"]["checked_fix_prs"])
        self.assertIn("1 / 1 refutations with a verified fix", refresh.render_html(data))
        self.assertIn("| Verified fixes |", refresh.render_markdown(data))
        combined = refresh.hub([data])
        self.assertEqual(1, combined["summary"]["checked_fixes"])
        self.assertIn("1 / 1 refutations with a verified fix", refresh.render_html(combined, "hub.html"))
        newer = refresh.build([pr()], [comment(), comment(comment_id=201)], [run()], "snapshot",
                              fixes=evidence)
        self.assertEqual(0, newer["summary"]["checked_fixes"])
        self.assertEqual(1, newer["summary"]["fix_unknown"])

    def test_missing_fix_evidence_is_unknown_not_zero(self):
        data = refresh.build([pr()], [comment()], [run()], "snapshot")
        self.assertEqual(1, data["summary"]["fix_unknown"])
        evidence = self.fix_evidence(data["prs"][0]["latest_report"], checked=False)
        refresh.apply_fix_evidence(data, evidence)
        self.assertEqual(0, data["summary"]["checked_fixes"])
        self.assertEqual(0, data["summary"]["fix_unknown"])
        evidence["reports"][0]["body_sha256"] = "b" * 64
        refresh.apply_fix_evidence(data, evidence)
        self.assertEqual(1, data["summary"]["fix_unknown"])

    def test_invalid_checked_fix_evidence_fails_explicitly(self):
        data = refresh.build([pr()], [comment()], [run()], "snapshot")
        evidence = self.fix_evidence(data["prs"][0]["latest_report"])
        evidence["reports"][0]["checked"] *= 2
        with self.assertRaisesRegex(ValueError, "checked-fix"):
            refresh.apply_fix_evidence(data, evidence)
        evidence = self.fix_evidence(data["prs"][0]["latest_report"])
        evidence["reports"][0]["checked"][0]["patch_sha256"] = "wrong"
        with self.assertRaisesRegex(ValueError, "checked-fix"):
            refresh.apply_fix_evidence(data, evidence)

    def campaign(self):
        return {
            "repository": refresh.REPOSITORY, "status": "paused", "planned_prs": 100,
            "attempted_prs": 1, "workflow_attempts": 1, "spent_aic": "249.87792",
            "budget_aic": "20000", "checked_patches": 0,
            "note": "Report is published; campaign acceptance remains blocked.",
        }

    def test_paused_plan_does_not_inflate_published_outcomes(self):
        data = refresh.build([pr()], [comment()], [run()], "snapshot", campaign=self.campaign())
        self.assertEqual(1, data["summary"]["attempted_prs"])
        self.assertEqual(1, data["summary"]["properties"])
        self.assertEqual(0, data["summary"]["without_report"])
        rendered = refresh.render_html(data)
        self.assertIn("Campaign paused", rendered)
        self.assertIn("100 source PRs selected; 1 attempted; 99 not attempted.", rendered)
        self.assertIn("249.88 / 20,000 AIC spent; 0 checked patches.", rendered)
        combined = refresh.hub([data])
        self.assertEqual(self.campaign(), combined["repositories"][0]["campaign"])
        self.assertNotIn('<aside class="campaign"', refresh.render_html(combined, "hub.html"))
        self.assertIn('<aside class="campaign"', rendered)
        self.assertIn("## Campaign paused", refresh.render_markdown(data))

    def test_campaign_metadata_is_bound_and_escaped(self):
        campaign = self.campaign()
        campaign["note"] = "<script>alert(1)</script> @user"
        data = refresh.build([pr()], [comment()], [run()], "snapshot", campaign=campaign)
        self.assertNotIn("<script>alert", refresh.render_html(data))
        self.assertNotIn("<script>alert", refresh.render_markdown(data))
        self.assertIn("&lt;script&gt;", refresh.render_campaign(data))
        for key, value in (("repository", "example/other"), ("planned_prs", 0),
                           ("workflow_attempts", 2), ("spent_aic", "NaN")):
            with self.subTest(key=key), self.assertRaises(ValueError):
                refresh.build([pr()], [comment()], [run()], "snapshot",
                              campaign={**self.campaign(), key: value})

    def test_ghaw_published_pilot_counts_four_properties_not_the_plan(self):
        repository = "shuvendu-lahiri/gh-aw"
        header = BODY[:BODY.index("### P1")].replace("1 refuted, 0 verified", "0 refuted, 4 verified")
        header = header.replace("refuted: 1", "refuted: 0").replace("verified: 0", "verified: 4")
        body = header.replace(refresh.REPOSITORY, repository) + "\n".join(
            f"### P{number}\n**Outcome: verified**\n" for number in range(1, 5))
        value = comment(body)
        value["issue_url"] = f"https://api.github.com/repos/{repository}/issues/2"
        workflow = run()
        workflow["pull_requests"][0]["url"] = f"https://api.github.com/repos/{repository}/pulls/2"
        data = refresh.build([pr()], [value], [workflow], "snapshot", repository,
                             campaign={**self.campaign(), "repository": repository})
        self.assertEqual(4, data["summary"]["properties"])
        self.assertEqual(4, data["summary"]["outcomes"]["verified"])
        self.assertEqual(0, data["summary"]["outcomes"]["refuted"])
        self.assertIn("<strong>100.0%</strong>", refresh.render_html(data))

    def test_reruns_do_not_duplicate_prs_or_properties(self):
        data = refresh.build([pr()], [comment()], [{**run(), "run_attempt": 2}], "snapshot")
        self.assertEqual(1, data["summary"]["attempted_prs"])
        self.assertEqual(2, data["summary"]["workflow_attempts"])
        self.assertEqual(1, data["summary"]["properties"])
        self.assertEqual(2, data["prs"][0]["latest_run"]["attempt"])

    def test_invalid_attempts_fail_closed(self):
        for attempt in (None, 0, -1, True, "2"):
            with self.subTest(attempt=attempt), self.assertRaisesRegex(ValueError, "invalid workflow attempt"):
                refresh.build([pr()], [], [{**run(), "run_attempt": attempt}], "snapshot")

    def test_live_dashboard_and_github_readme_navigation(self):
        data = refresh.build([pr()], [comment()], [run()], "snapshot")
        self.assertIn(refresh.SITE + "litebox/", refresh.render_markdown(data))
        self.assertIn(refresh.GITHUB + "/", refresh.render_html(data))

    def test_legacy_numbered_report_preserves_identifiers(self):
        body = BODY.replace("### P1\n**Intended property:**", "## 1.")
        report = refresh.parse_report(comment(body))
        self.assertEqual(1, report["counts"]["refuted"])
        self.assertEqual("1", report["refutations"][0]["property_id"])
        self.assertEqual("Every x < limit is retained.", report["refutations"][0]["property"])

    def test_legacy_numbered_code_blocks_are_not_properties(self):
        body = BODY + "\n```text\n## 999. Not a property\n**Outcome: refuted**\n```\n"
        self.assertEqual(1, refresh.parse_report(comment(body))["properties"])

    def test_repository_links_do_not_leak_between_collectors(self):
        for name in refresh.REPOSITORIES:
            repository = f"shuvendu-lahiri/{name}"
            with self.subTest(repository=repository):
                value = comment(BODY.replace(refresh.REPOSITORY, repository))
                value["issue_url"] = f"https://api.github.com/repos/{repository}/issues/2"
                workflow = run()
                workflow["pull_requests"][0]["url"] = f"https://api.github.com/repos/{repository}/pulls/2"
                workflow["head_repository"]["full_name"] = repository
                data = refresh.build([pr()], [value], [workflow], "snapshot", repository)
                report = data["prs"][0]["latest_report"]
                self.assertEqual(f"https://github.com/{repository}/pull/2#issuecomment-200", report["url"])
                self.assertEqual(f"https://github.com/{repository}/actions/runs/100", report["run_url"])
                self.assertEqual(repository, data["repository"])

    def test_cross_repository_comment_identity_rejected(self):
        with self.assertRaisesRegex(ValueError, "repository identity"):
            refresh.parse_report(comment(), repository="shuvendu-lahiri/z3")

    def test_reused_branch_resolves_by_immutable_head(self):
        first, second = pr(), pr(3)
        second["head"]["ref"] = first["head"]["ref"]
        second["head"]["sha"] = "f" * 40
        value = {**run(), "pull_requests": [], "head_sha": first["head"]["sha"]}
        self.assertEqual([2], refresh.run_numbers(value, {"branch-2": [2, 3]}, prs={2: first, 3: second}))

    def test_reused_head_resolves_by_original_run_lifetime_not_retry_date(self):
        first, second = pr(), pr(3)
        second["head"]["ref"] = first["head"]["ref"]
        first.update(created_at="2026-10-19T00:00:00Z", closed_at="2026-10-20T01:00:00Z")
        second.update(created_at="2026-10-21T00:00:00Z", closed_at=None)
        value = {**run(), "pull_requests": [], "head_sha": first["head"]["sha"],
                 "run_started_at": "2026-10-22T00:00:00Z", "run_attempt": 2}
        self.assertEqual([2], refresh.run_numbers(value, {"branch-2": [2, 3]}, prs={2: first, 3: second}))
        second["created_at"] = first["created_at"]
        with self.assertRaisesRegex(ValueError, "ambiguous historical"):
            refresh.run_numbers(value, {"branch-2": [2, 3]}, prs={2: first, 3: second})

    def test_cohort_preserves_waiting_and_source_mapping(self):
        cohort = {"repository": refresh.REPOSITORY, "source_repository": "example/source",
                  "prs": [{"number": 2, "source_number": 99, "source_title": "Original title",
                           "source_head_sha": "a" * 40}]}
        data = refresh.build([pr(), pr(3)], [], [run(3)], "snapshot", cohort=cohort)
        self.assertEqual(1, data["summary"]["selected_prs"])
        self.assertEqual(0, data["summary"]["attempted_prs"])
        self.assertEqual(1, data["summary"]["without_report"])
        self.assertEqual("https://redirect.github.com/example/source/pull/99", data["prs"][0]["source_url"])
        self.assertIn("No published report (not attempted)", refresh.render_markdown(data))
        cohort["repository"] = "example/other"
        with self.assertRaisesRegex(ValueError, "different repository"):
            refresh.build([pr()], [], [], "snapshot", cohort=cohort)

    def test_hub_totals_do_not_count_report_history_twice(self):
        data = refresh.build([pr()], [comment(), comment(comment_id=201)], [run()], "snapshot")
        combined = refresh.hub([data])
        self.assertEqual(1, combined["summary"]["published_reports"])
        self.assertEqual(1, combined["summary"]["outcomes"]["refuted"])
        rendered = refresh.render_html(combined, "hub.html")
        self.assertNotIn("innerHTML", rendered)
        self.assertIn("Refutations are model results, not confirmed source bugs.", rendered)
        self.assertEqual(1, rendered.count("<strong>100.0%</strong>"))
        self.assertIn('<tr data-repository="litebox">', rendered)
        self.assertNotIn('<template id="outcome-tracker-', rendered)
        self.assertEqual(1, refresh.render_html(data).count("100.0%"))

    def test_hub_has_one_static_metric_row_per_repository_and_total_row(self):
        first = refresh.build([pr()], [comment()], [run()], "snapshot")
        second = refresh.build([pr()], [], [run()], "snapshot")
        second.update(name="next", label="Next <project>", languages=["C++", "<test>"])
        rendered = refresh.render_html(refresh.hub([first, second]), "hub.html")
        rows = re.findall(r'<tr data-repository="([^"]+)">(.*?)</tr>', rendered, re.S)
        self.assertEqual(["litebox", "next"], [name for name, _ in rows])
        for _, row in rows:
            self.assertEqual(9, len(re.findall(r"<t[dh](?:\s|>)", row)))
        self.assertIn('<a href="litebox/"', rows[0][1])
        self.assertIn('<a href="next/"', rows[1][1])
        self.assertIn("Next &lt;project&gt;", rows[1][1])
        self.assertIn("C++, &lt;test&gt;", rows[1][1])
        self.assertNotIn("Next <project>", rows[1][1])
        self.assertIn('<th scope="row" colspan="2">All projects</th>'
                      '<td>1 / 2<span class="cell-note">50.0% published</span></td>', rendered)
        self.assertNotIn('class="card"', rendered)
        self.assertNotIn("cloneNode", rendered)
        self.assertNotIn("__NFV_", rendered)
        self.assertNotIn('<details class="totals">', rendered)
        self.assertLess(rendered.index('<section class="totals"'), rendered.index('<section class="repositories"'))
        self.assertIn("Latest snapshot: snapshot.", rendered)

    def test_repository_table_distinguishes_unknown_measurements_from_known_zero(self):
        data = refresh.build([pr()], [comment()], [run()], "snapshot")
        unknown = refresh.render_repository_rows(refresh.hub([data]))
        self.assertIn('N/A<span class="cell-note">0 / 1 runs (0.0%)</span>', unknown)
        self.assertIn('N/A<span class="cell-note">0 / 1 PRs (0.0%)</span>', unknown)
        data["summary"]["timing"] = refresh.timing_summary(1, 0, 1)
        data["summary"]["usage"] = refresh.usage_summary(refresh.Decimal(0), 1, 0, 0)
        measured = refresh.render_repository_rows(refresh.hub([data]))
        self.assertIn('0m 00s<span class="cell-note">1 / 1 runs (100.0%)</span>', measured)
        self.assertIn('0.00<span class="cell-note">1 / 1 PRs (100.0%)</span>', measured)

    def test_table_percentages_use_metric_denominators_and_pooled_totals(self):
        first = refresh.build([pr()], [comment()], [run()], "snapshot")
        first["summary"].update(
            attempted_prs=4, published_reports=3, properties=10, checked_fixes=1, fix_unknown=1,
            outcomes={"refuted": 2, "verified": 6, "resources exhausted": 2, "type-check/audit failure": 0},
            timing=refresh.timing_summary(2, 120, 3),
            usage=refresh.usage_summary(refresh.Decimal(40), 2, 2, 0))
        second = refresh.build([pr()], [comment()], [run()], "snapshot")
        rendered = refresh.render_repository_rows(refresh.hub([first, second]))
        for value in ("75.0% published", "<td>2 (20.0%)", "<td>1 (50.0%)", "<td>6 (60.0%)",
                      "2 / 4 PRs (50.0%)", "2 / 3 runs (66.7%)"):
            self.assertIn(value, rendered)
        total = rendered.split("<tfoot>")[1]
        self.assertIn("<td>3 (27.3%)", total)
        self.assertIn("<td>1 (33.3%)", total)
        self.assertIn("<td>6 (54.5%)", total)
        self.assertIn("(50.0%)", refresh.render_usage(first["summary"]))
        self.assertIn("66.7% coverage", refresh.render_timing(first["summary"]))
        self.assertIn("1 / 2 refutations with a verified fix (50.0%)",
                      refresh.render_outcome_tracker(first["summary"]))

    def test_table_zero_denominators_show_unavailable_percentages(self):
        data = refresh.build([], [], [], "snapshot")
        rendered = refresh.render_repository_rows(refresh.hub([data]))
        self.assertIn("N/A published", rendered)
        self.assertIn("<td>0 (N/A)", rendered)
        self.assertIn("0 / 0 PRs (N/A)", rendered)
        self.assertIn("0 / 0 runs (N/A)", rendered)
        self.assertNotIn("0.0%", rendered)

    def test_outcome_percentages_use_properties_not_prs_or_attempts(self):
        summary = {
            "properties": 10, "attempted_prs": 100, "workflow_attempts": 200,
            "outcomes": {"verified": 6, "refuted": 1,
                         "type-check/audit failure": 2, "resources exhausted": 1},
        }
        rendered = refresh.render_outcome_tracker(summary)
        for percentage, count in (("60.0%", 6), ("20.0%", 2), ("10.0%", 1)):
            self.assertIn(
                f'<strong>{percentage}</strong><span class="muted">{count} / 10 properties</span>',
                rendered)
        self.assertIn('style="flex-grow:6"', rendered)

    def test_no_published_properties_have_unavailable_percentages(self):
        data = refresh.build([pr()], [], [run(conclusion="failure")], "snapshot")
        rendered = refresh.render_outcome_tracker(data["summary"])
        self.assertIn("No published property outcomes yet", rendered)
        self.assertEqual(4, rendered.count("<strong>N/A</strong>"))
        self.assertNotIn("%", rendered)
        self.assertNotIn('class="outcome-bar"', rendered)

    def test_invalid_percentage_totals_fail_explicitly(self):
        for total, count in ((2, 1), (1, -1), (1, True), (1, "1")):
            with self.subTest(total=total, count=count):
                summary = {"properties": total, "outcomes": dict.fromkeys(refresh.STATUSES, 0)}
                summary["outcomes"]["verified"] = count
                with self.assertRaisesRegex(ValueError, "property outcome totals"):
                    refresh.render_outcome_tracker(summary)

    def test_report_without_legacy_marker(self):
        report = refresh.parse_report(comment())
        self.assertEqual(report["counts"]["refuted"], 1)
        self.assertEqual(report["refutations"][0]["property"], "Every x < limit is retained.")
        self.assertEqual(report["refutations"][0]["input"], "x = 0.")
        self.assertEqual(report["properties"], 1)

    def test_counts_fail_closed(self):
        with self.assertRaisesRegex(ValueError, "disagree with summary"):
            refresh.parse_report(comment(BODY.replace("**Outcome: refuted**", "**Outcome: verified**")))

    def test_identity_and_heading_must_match(self):
        with self.assertRaisesRegex(ValueError, "PR identity"):
            refresh.parse_report(comment(BODY.replace("in PR #2", "in PR #3")))
        with self.assertRaisesRegex(ValueError, "inconsistent heading"):
            refresh.parse_report(comment(BODY.replace("# NFV: 1", "# NFV: 2")))

    def test_duplicate_properties_rejected(self):
        body = BODY.replace("1 refuted", "2 refuted").replace("refuted: 1", "refuted: 2")
        body += BODY[BODY.index("### P1"):]
        with self.assertRaisesRegex(ValueError, "duplicate property"):
            refresh.parse_report(comment(body))

    def test_code_blocks_do_not_forge_outcomes(self):
        body = BODY + "\n`````rust\n### P999\n**Outcome: refuted**\n```\n`````\n"
        self.assertEqual(refresh.parse_report(comment(body))["properties"], 1)

    def test_setup_and_bot_notes_are_not_reports(self):
        self.assertIsNone(refresh.parse_report(comment("Setup complete. NFV replay will follow.")))
        self.assertIsNone(refresh.parse_report(comment("```text\n" + BODY + "\n```")))

    def test_report_requires_matching_workflow(self):
        with self.assertRaisesRegex(ValueError, "does not match"):
            refresh.build([pr(), pr(3)], [comment()], [run(3)], "snapshot")

    def test_unrecognized_publisher_rejected(self):
        value = comment()
        value["user"]["login"] = "untrusted-contributor"
        with self.assertRaisesRegex(ValueError, "unrecognized NFV publisher"):
            refresh.parse_report(value)

    def test_latest_report_not_double_counted(self):
        first = comment()
        first["updated_at"] = "2026-10-22T00:00:00Z"
        second = comment(comment_id=201, date="2026-10-21T00:00:00Z")
        data = refresh.build([pr()], [first, second], [run()], "snapshot")
        self.assertEqual(data["summary"]["outcomes"]["refuted"], 1)
        self.assertEqual(data["prs"][0]["latest_report"]["comment_id"], 201)
        self.assertEqual(len(data["prs"][0]["report_history"]), 2)

    def test_failed_attempt_is_unknown_not_zero_and_skipped_excluded(self):
        data = refresh.build([pr(3), pr(4)], [], [run(3, 101, "failure"), run(4, 102, "skipped")], "snapshot")
        self.assertEqual(data["summary"]["attempted_prs"], 1)
        self.assertIsNone(data["prs"][0]["latest_report"])
        self.assertEqual(data["summary"]["without_report"], 1)
        self.assertIn("No published report (failure)", refresh.render_markdown(data))
        self.assertIn("| - | - | - | - | - |", refresh.render_markdown(data))

    def test_older_report_is_marked(self):
        value = pr()
        value["head"]["sha"] = "f" * 40
        data = refresh.build([value], [comment()], [run()], "snapshot")
        self.assertFalse(data["prs"][0]["report_matches_current_head"])
        self.assertIn("(older head)", refresh.render_markdown(data))

    def test_latest_failed_attempt_does_not_erase_published_report(self):
        last = run(2, 101, "failure")
        last["created_at"] = "2026-10-21T00:00:00Z"
        data = refresh.build([pr()], [comment()], [run(), last], "snapshot")
        self.assertEqual(data["summary"]["outcomes"]["refuted"], 1)
        self.assertIn("latest attempt: failure", refresh.render_markdown(data))

    def test_markdown_entities_and_identifiers_remain_readable(self):
        self.assertEqual(refresh.plain(r"VAULT\_STACK"), "VAULT_STACK")
        self.assertEqual(refresh.markdown("caller's <limit>"), "caller's &lt;limit&gt;")

    def test_branch_fallback_must_be_unique(self):
        value = run()
        value["pull_requests"] = []
        self.assertEqual(refresh.run_numbers(value, {"branch-2": [2]}), [2])
        with self.assertRaisesRegex(ValueError, "ambiguous"):
            refresh.run_numbers(value, {"branch-2": [2, 3]})
        value["head_repository"] = None
        self.assertEqual(refresh.run_numbers(value, {"branch-2": [2]}), [])

    def test_untrusted_text_cannot_break_script_or_markdown(self):
        data = refresh.build([pr()], [comment()], [run()], "snapshot")
        payload = '</script><img src=x onerror="alert(1)"> | [trap](javascript:alert(1))'
        data["prs"][0]["title"] = payload
        rendered = refresh.render_html(data)
        self.assertNotIn(payload, rendered)
        embedded = re.search(r'<script type="application/json" id="data">(.*?)</script>', rendered, re.S)[1]
        self.assertEqual(json.loads(embedded)["prs"][0]["title"], payload)
        self.assertNotIn("<img", refresh.render_markdown(data))
        self.assertIn(r"\|", refresh.render_markdown(data))
        self.assertNotIn("innerHTML", rendered)

    def test_snapshot_totals_and_refutation_order(self):
        paths = [refresh.DIRECTORY / name / "data.json" for name in refresh.REPOSITORIES]
        if not all(path.exists() for path in paths):
            self.skipTest("Dashboard has not been generated")
        snapshots = [json.loads(path.read_text(encoding="utf-8")) for path in paths]
        for data in snapshots:
            with self.subTest(repository=data["repository"]):
                published = [entry["latest_report"] for entry in data["prs"] if entry["latest_report"]]
                self.assertEqual(data["summary"]["published_reports"], len(published))
                self.assertEqual(data["summary"]["properties"], sum(r["properties"] for r in published))
                self.assertEqual(data["summary"]["workflow_attempts"], sum(e["attempts"] for e in data["prs"]))
                for status in refresh.STATUSES:
                    self.assertEqual(data["summary"]["outcomes"][status], sum(r["counts"][status] for r in published))
                self.assertEqual(data["summary"]["outcomes"]["refuted"], sum(len(r["refutations"]) for r in published))
                ordered = refresh.ordered(data)
                flags = [bool(e["latest_report"] and e["latest_report"]["counts"]["refuted"]) for e in ordered]
                self.assertEqual(flags, sorted(flags, reverse=True))
        combined = json.loads((refresh.DIRECTORY / "data.json").read_text(encoding="utf-8"))
        self.assertEqual(combined, refresh.hub(snapshots))


class TimingTests(unittest.TestCase):
    def data(self, count=1):
        pulls, comments, runs = [], [], []
        for number in range(2, 2 + count):
            pulls.append(pr(number))
            body = BODY.replace("in PR #2", f"in PR #{number}").replace("/runs/100", f"/runs/{100 + number}")
            item = comment(body, comment_id=200 + number)
            item["issue_url"] = item["issue_url"].rsplit("/", 1)[0] + f"/{number}"
            comments.append(item)
            runs.append(run(number, 100 + number))
        return refresh.build(pulls, comments, runs, "snapshot")

    def evidence(self, data, durations):
        records = []
        for entry, seconds in zip(data["prs"], durations):
            report = entry["latest_report"]
            start = refresh.timestamp(report["published_at"]) - timedelta(seconds=1)
            records.append({
                **{key: report[key] for key in ("run_id", "comment_id", "body_sha256")},
                "status": "complete", "attempt": 1, "started_at": start.isoformat(),
                "completed_at": (start + timedelta(seconds=seconds)).isoformat(),
            })
        return {"schema": 1, "repository": data["repository"], "reports": records}

    def test_overall_average_is_weighted_by_timed_runs_and_excludes_missing(self):
        first, second = self.data(), self.data(4)
        refresh.apply_timing_evidence(first, self.evidence(first, [60]))
        refresh.apply_timing_evidence(second, self.evidence(second, [180, 180, 180]))
        timing = refresh.hub([first, second])["summary"]["timing"]
        self.assertEqual(4, timing["samples"])
        self.assertEqual(1, timing["missing"])
        self.assertEqual(150, timing["average_seconds"])
        self.assertIn("2m 30s", refresh.render_html(refresh.hub([first, second]), "hub.html"))
        self.assertIn("3 / 4 latest-report runs timed", refresh.render_html(second))
        self.assertIn("3 / 4 latest-report runs timed", refresh.render_markdown(second))

    def test_missing_or_mismatched_timing_is_unavailable_not_zero(self):
        data = self.data()
        evidence = self.evidence(data, [60])
        evidence["reports"][0]["body_sha256"] = "b" * 64
        refresh.apply_timing_evidence(data, evidence)
        self.assertIsNone(data["summary"]["timing"]["average_seconds"])
        self.assertEqual(1, data["summary"]["timing"]["missing"])
        self.assertIn("Average workflow time: N/A", refresh.render_html(data))
        self.assertNotIn("workflow_timing", data["prs"][0]["latest_report"])

    def test_historical_reports_do_not_add_timing_samples(self):
        data = self.data()
        evidence = self.evidence(data, [60])
        old = data["prs"][0]["latest_report"]
        data["prs"][0]["report_history"].append(dict(old))
        data["prs"][0]["latest_report"] = {**old, "comment_id": 999}
        refresh.apply_timing_evidence(data, evidence)
        self.assertEqual(0, data["summary"]["timing"]["samples"])
        evidence["reports"].extend(self.evidence(data, [120])["reports"])
        refresh.apply_timing_evidence(data, evidence)
        self.assertEqual(1, data["summary"]["timing"]["samples"])
        self.assertEqual(120, data["summary"]["timing"]["average_seconds"])

    def test_jobs_use_wall_clock_span_and_the_attempt_covering_publication(self):
        report = self.data()["prs"][0]["latest_report"]

        def job(start, end, attempt=1, conclusion="success"):
            return {"run_id": report["run_id"], "run_attempt": attempt, "status": "completed",
                    "conclusion": conclusion, "started_at": start, "completed_at": end}

        jobs = [
            job("2026-10-19T23:59:00Z", "2026-10-20T00:00:10Z"),
            job("2026-10-20T00:00:05Z", "2026-10-20T00:01:00Z"),
            job("2026-10-19T19:00:00Z", "2026-10-19T19:00:00Z", conclusion="skipped"),
            job("2026-10-21T00:00:00Z", "2026-10-21T01:00:00Z", attempt=2),
        ]
        record = refresh.timing_record(report, jobs)
        self.assertEqual("complete", record["status"])
        self.assertEqual(1, record["attempt"])
        seconds = (refresh.timestamp(record["completed_at"]) - refresh.timestamp(record["started_at"])).total_seconds()
        self.assertEqual(120, seconds)
        jobs[0]["status"] = "in_progress"
        self.assertEqual("unavailable", refresh.timing_record(report, jobs)["status"])
        jobs[0]["status"] = "completed"
        jobs[0]["completed_at"] = "2026-10-19T23:58:00Z"
        unavailable = refresh.timing_record(report, jobs)
        self.assertEqual("unavailable", unavailable["status"])
        self.assertIn("ends before it starts", unavailable["reason"])

    def test_invalid_timing_and_ambiguous_attempts_fail_or_remain_unknown(self):
        data = self.data()
        evidence = self.evidence(data, [60])
        evidence["reports"][0]["completed_at"] = "2026-10-19T00:00:00Z"
        with self.assertRaisesRegex(ValueError, "does not cover"):
            refresh.apply_timing_evidence(data, evidence)
        report = data["prs"][0]["latest_report"]
        jobs = [{"run_id": report["run_id"], "run_attempt": attempt, "status": "completed",
                 "conclusion": "success", "started_at": "2026-10-19T23:59:00Z",
                 "completed_at": "2026-10-20T00:01:00Z"} for attempt in (1, 2)]
        self.assertEqual("unavailable", refresh.timing_record(report, jobs)["status"])

    def test_api_errors_are_not_hidden_as_missing_timings(self):
        report = self.data()["prs"][0]["latest_report"]
        result = type("Result", (), {"returncode": 1, "stderr": "HTTP 403: rate limit", "stdout": ""})()
        with patch.object(refresh.subprocess, "run", return_value=result):
            with self.assertRaisesRegex(RuntimeError, "HTTP 403"):
                refresh.fetch_timing_record(refresh.REPOSITORY, report)
        result.stderr = "HTTP 404: Not Found"
        with patch.object(refresh.subprocess, "run", return_value=result):
            self.assertEqual("unavailable", refresh.fetch_timing_record(refresh.REPOSITORY, report)["status"])


if __name__ == "__main__":
    unittest.main()
