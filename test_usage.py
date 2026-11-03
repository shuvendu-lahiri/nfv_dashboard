import copy
from decimal import Decimal
import io
import json
import unittest
import zipfile

import collect_usage
import refresh
from test_refresh import pr, run


def archive(**roles):
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as output:
        for role, amounts in roles.items():
            lines = [
                json.dumps({"event": "token_usage", "request_id": f"{role}-{index}",
                            "ai_credits_this_response": amount, "ai_credits_total": 9999})
                for index, amount in enumerate(amounts)]
            output.writestr(f"{role}/token_usage.jsonl", "\n".join(lines))
    return buffer.getvalue()


def evidence(data, values):
    records = []
    for entry, attempts in zip(data["prs"], values):
        records.append({
            "number": entry["number"], "scope_sha256": refresh.usage_scope(entry),
            "scope_matches": True, "workflow_attempts": entry["attempts"],
            "runs": [{"run_id": 100 + entry["number"], "attempt": index + 1,
                      "aic": amount, "ai_jobs": jobs}
                     for index, (amount, jobs) in enumerate(attempts)],
        })
    return {"schema": 1, "repository": data["repository"], "prs": records}


class UsageTests(unittest.TestCase):
    def test_per_response_billing_includes_detection_not_cumulative_totals(self):
        content = archive(agent=["1.25", "2.5"], detection=["0.125"])
        self.assertEqual(Decimal("3.875"),
                         collect_usage.artifact_credits(content, ["agent", "detection"]))
        self.assertIsNone(collect_usage.artifact_credits(archive(agent=["1"]), ["agent", "detection"]))

    def test_duplicate_requests_are_not_double_charged_and_conflicts_fail(self):
        row = {"event": "token_usage", "request_id": "request", "ai_credits_this_response": "2"}
        def duplicate(other):
            buffer = io.BytesIO()
            with zipfile.ZipFile(buffer, "w") as output:
                output.writestr("agent/token_usage.jsonl",
                                json.dumps(row) + "\n" + json.dumps({**row, **other}))
            return buffer.getvalue()
        self.assertEqual(Decimal(2), collect_usage.artifact_credits(duplicate({}), ["agent"]))
        with self.assertRaisesRegex(ValueError, "Conflicting"):
            collect_usage.artifact_credits(duplicate({"ai_credits_this_response": "3"}), ["agent"])
        self.assertIsNone(collect_usage.artifact_credits(
            duplicate({"ai_credits_this_response": None}), ["agent"]))
        self.assertIsNone(collect_usage.artifact_credits(
            duplicate({"ai_credits_fallback_pricing_used": True}), ["agent"]))
        self.assertIsNone(collect_usage.artifact_credits(archive(agent=[]), ["agent"]))

    def test_artifacts_are_bound_to_each_jobs_upload_not_names_or_cache(self):
        jobs, artifacts, content = [], [], {}
        for index, prefix in enumerate(("", "repository_context / ")):
            for role in ("agent", "detection"):
                jobs.append({"name": prefix + role, "conclusion": "success", "status": "completed"})
            start = f"2026-11-01T00:0{index}:00Z"
            end = f"2026-11-01T00:0{index}:10Z"
            jobs.append({"name": prefix + "conclusion", "status": "completed", "conclusion": "success",
                         "steps": [{"name": "Upload usage artifact", "conclusion": "success",
                                    "started_at": start, "completed_at": end}]})
            artifacts.append({"id": index, "name": "usage" if not prefix else "abc-usage",
                              "expired": False, "created_at": start})
            content[index] = archive(agent=["10"], detection=["1"])
        artifacts.append({"id": 99, "name": "usage", "expired": False,
                          "created_at": "2026-10-31T00:00:00Z"})
        result = collect_usage.measure_attempt(jobs, artifacts, content.__getitem__)
        self.assertEqual("22", result["aic"])
        self.assertEqual(4, result["ai_jobs"])
        self.assertEqual(2, len(result["artifacts"]))
        artifacts[1]["expired"] = True
        self.assertIsNone(collect_usage.measure_attempt(jobs, artifacts, content.__getitem__)["aic"])

    def test_all_skipped_jobs_have_known_zero_but_missing_jobs_are_unknown(self):
        jobs = [{"name": "agent", "status": "completed", "conclusion": "skipped"}]
        result = collect_usage.measure_attempt(jobs, [], lambda _: self.fail("No download expected"))
        self.assertEqual("0", result["aic"])
        self.assertEqual(0, result["ai_jobs"])
        self.assertIsNone(collect_usage.measure_attempt([], [], None)["aic"])
        jobs[0].update(conclusion="success", steps=[
            {"name": "Execute GitHub Copilot CLI", "conclusion": "skipped"}])
        self.assertEqual("0", collect_usage.measure_attempt(jobs, [], None)["aic"])
        jobs[0]["steps"][0]["conclusion"] = "failure"
        self.assertIsNone(collect_usage.measure_attempt(jobs, [], None)["aic"])

    def test_log_fallback_uses_only_trusted_parser_step_and_rejects_ambiguity(self):
        job = {"steps": [{
            "name": "Parse token usage for step summary", "conclusion": "success",
            "started_at": "2026-11-01T00:01:00Z", "completed_at": "2026-11-01T00:01:05Z",
        }]}
        log = (b"2026-11-01T00:00:59.999Z AI Credits: 9999\n"
               b"2026-11-01T00:01:02.123Z AI Credits: 12.5\n"
               b"2026-11-01T00:01:02.456Z AI Credits: 12.5\n"
               b"2026-11-01T00:01:06.000Z AI Credits: 9999\n")
        self.assertEqual(Decimal("12.5"), collect_usage.job_credits(job, log))
        self.assertIsNone(collect_usage.job_credits(
            job, log + b"2026-11-01T00:01:03Z AI Credits: 13\n"))
        self.assertIsNone(collect_usage.job_credits(
            job, b"2026-11-01T00:00:59Z AI Credits: 12.5\n"))
        job["steps"][0]["conclusion"] = "failure"
        self.assertIsNone(collect_usage.job_credits(job, log))

    def test_pr_total_includes_all_retries_and_failures(self):
        data = refresh.build([pr()], [], [run(), {**run(run_id=101, conclusion="failure"),
                                                "run_attempt": 2}], "snapshot")
        proof = evidence(data, [[("10", 2), ("3", 2), ("2", 2)]])
        refresh.apply_usage_evidence(data, proof)
        self.assertEqual("15", data["prs"][0]["usage"]["aic"])
        self.assertEqual("15", data["summary"]["usage"]["average_aic_per_pr"])
        self.assertIn("Average review AIC: 15.00 per PR", refresh.render_html(data))
        self.assertIn("Review AIC (all attempts)", refresh.render_markdown(data))

    def test_incomplete_and_quota_only_prs_do_not_lower_the_average(self):
        data = refresh.build([pr(2), pr(3), pr(4)], [], [run(2), run(3, 101), run(4, 102)], "snapshot")
        proof = evidence(data, [[("12", 2)], [(None, 2)], [("0", 0)]])
        refresh.apply_usage_evidence(data, proof)
        self.assertEqual({"total_aic": "12", "average_aic_per_pr": "12", "measured_prs": 1,
                          "incomplete_prs": 1, "no_ai_prs": 1}, data["summary"]["usage"])
        self.assertIn("Coverage: 1 / 3 attempted PRs fully measured; 1 with incomplete usage; 1 with no AI execution.",
                      refresh.render_html(data))

    def test_new_scope_or_incomplete_attempt_list_invalidates_old_usage(self):
        data = refresh.build([pr()], [], [run()], "snapshot")
        proof = evidence(data, [[("10", 2)]])
        for mutate in (lambda d: d["prs"][0].update(head_sha="f" * 40),
                       lambda d: d["prs"][0].update(attempts=2)):
            changed = copy.deepcopy(data)
            mutate(changed)
            refresh.apply_usage_evidence(changed, proof)
            self.assertIsNone(changed["summary"]["usage"]["average_aic_per_pr"])
            self.assertEqual("incomplete", changed["prs"][0]["usage"]["status"])
        proof["prs"][0]["runs"] = []
        refresh.apply_usage_evidence(data, proof)
        self.assertEqual(1, data["summary"]["usage"]["incomplete_prs"])

    def test_overall_average_is_weighted_by_fully_measured_prs(self):
        first = refresh.build([pr()], [], [run()], "snapshot")
        second = refresh.build([pr(3), pr(4)], [], [run(3, 101), run(4, 102)], "snapshot")
        refresh.apply_usage_evidence(first, evidence(first, [[("100", 2)]]))
        refresh.apply_usage_evidence(second, evidence(second, [[("10", 2)], [("10", 2)]]))
        combined = refresh.hub([first, second])
        self.assertEqual("40", combined["summary"]["usage"]["average_aic_per_pr"])
        self.assertIn("Average review AIC: 40.00 per PR", refresh.render_html(combined, "hub.html"))

    def test_zero_cost_executed_review_is_measured_and_invalid_costs_fail(self):
        data = refresh.build([pr()], [], [run()], "snapshot")
        proof = evidence(data, [[("0", 2)]])
        refresh.apply_usage_evidence(data, proof)
        self.assertEqual(1, data["summary"]["usage"]["measured_prs"])
        for invalid in ("-1", "NaN", "Infinity", True):
            with self.subTest(invalid=invalid):
                proof["prs"][0]["runs"][0]["aic"] = invalid
                with self.assertRaises(ValueError):
                    refresh.apply_usage_evidence(data, proof)
        proof = evidence(data, [[("1", 2)]])
        proof["prs"][0]["runs"] *= 2
        with self.assertRaisesRegex(ValueError, "duplicate workflow"):
            refresh.apply_usage_evidence(data, proof)

    def test_usage_summary_is_visible_even_without_published_properties(self):
        data = refresh.build([pr()], [], [run()], "snapshot")
        refresh.apply_usage_evidence(data, evidence(data, [[("12", 2)]]))
        rendered = refresh.render_outcome_tracker(data["summary"])
        self.assertIn("Average review AIC: 12.00", rendered)
        self.assertNotIn('class="outcome-bar"', rendered)
        self.assertLess(rendered.index("</dl>"), rendered.index('<aside class="usage-summary"'))


if __name__ == "__main__":
    unittest.main()
