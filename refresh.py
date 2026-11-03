"""Refresh the public NFV dashboard hub from published GitHub evidence."""

import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from decimal import Decimal
import hashlib
import html
import json
from pathlib import Path
import re
import subprocess


REPOSITORY = "shuvendu-lahiri/litebox"
WEB = f"https://github.com/{REPOSITORY}"
DIRECTORY = Path(__file__).resolve().parent
REPOSITORIES = {"z3": "Z3", "litebox": "LiteBox", "nvx": "NVX", "gh-aw": "gh-aw",
                "garnet": "Garnet"}
LANGUAGES = {"z3": ["C++"], "litebox": ["Rust", "C"], "nvx": ["Rust", "Python"],
             "gh-aw": ["Go", "JavaScript"], "garnet": ["C#"]}
SOURCE_REPOSITORIES = {"z3": "Z3Prover/z3", "litebox": "microsoft/litebox",
                       "nvx": "microsoft/nvx", "gh-aw": "github/gh-aw",
                       "garnet": "microsoft/garnet"}
SITE = "https://shuvendu-lahiri.github.io/nfv_dashboard/"
GITHUB = "https://github.com/shuvendu-lahiri/nfv_dashboard/blob/nfv-reports"
STATUSES = ("refuted", "verified", "resources exhausted", "type-check/audit failure")
COUNTS = re.compile(
    r"^refuted: (\d+) \u00b7 verified: (\d+) \u00b7 "
    r"resources exhausted: (\d+) \u00b7 type-check/audit failure: (\d+)$", re.M)


def prose(body):
    result, fence = [], None
    for line in body.splitlines():
        match = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
        if match:
            marker, suffix = match.groups()
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence) and not suffix.strip():
                fence = None
            continue
        if fence is None:
            result.append(line)
    return "\n".join(result)


def plain(value):
    return re.sub(r"\\([^\w\s]|_)", r"\1", html.unescape(value))


def paragraph(block, label):
    match = re.search(rf"^\*\*{label}:\*\* (.*)$", block, re.M)
    return plain(match[1]) if match else None


def parse_report(comment, repository=REPOSITORY):
    body = prose(comment["body"])
    heading = re.search(r"^# NFV: (\d+) refuted, (\d+) verified in PR #(\d+)$", body, re.M)
    if not heading:
        return None
    if not comment["issue_url"].startswith(f"https://api.github.com/repos/{repository}/issues/"):
        raise ValueError(f"Comment {comment['id']}: repository identity mismatch")
    number = int(comment["issue_url"].rsplit("/", 1)[1])
    if int(heading[3]) != number:
        raise ValueError(f"Comment {comment['id']}: PR identity mismatch")
    if comment["user"]["login"] not in (repository.split("/")[0], "github-actions[bot]"):
        raise ValueError(f"Comment {comment['id']}: unrecognized NFV publisher")
    summaries = COUNTS.findall(body)
    if len(summaries) != 1:
        raise ValueError(f"Comment {comment['id']}: missing or ambiguous outcome summary")
    counts = dict(zip(STATUSES, map(int, summaries[0])))
    if (counts["refuted"], counts["verified"]) != (int(heading[1]), int(heading[2])):
        raise ValueError(f"Comment {comment['id']}: inconsistent heading")
    snapshot = re.search(r"^PR head `([0-9a-f]{12,40})`, base `([0-9a-f]{12,40})`", body, re.M)
    web = f"https://github.com/{repository}"
    run = re.search(re.escape(web) + r"/actions/runs/(\d+)", body)
    if not snapshot or not run:
        raise ValueError(f"Comment {comment['id']}: missing source snapshot or workflow link")
    outcomes = Counter()
    refutations = []
    headings = list(re.finditer(r"^(?:### (P\d+)\s*|## ([1-9]\d*)\. (.+))$", body, re.M))
    identifiers = [match[1] or match[2] for match in headings]
    if len(set(identifiers)) != len(identifiers):
        raise ValueError(f"Comment {comment['id']}: duplicate property identifiers")
    for index, match in enumerate(headings):
        property_id = identifiers[index]
        end = headings[index + 1].start() if index + 1 < len(headings) else len(body)
        block = body[match.end():end]
        statuses = re.findall(r"^\*\*Outcome: (.*?)\*\*$", block, re.M)
        if len(statuses) != 1 or statuses[0] not in STATUSES:
            raise ValueError(f"Comment {comment['id']}: invalid outcome for {property_id}")
        status = statuses[0]
        outcomes[status] += 1
        if status == "refuted":
            intended = re.search(r"^\*\*(?:Intended|Inferred) property:\*\* (.*?)\n\n",
                                 block, re.M | re.S)
            if not intended and not match[3]:
                raise ValueError(f"Comment {comment['id']}: missing refuted property")
            refutations.append({
                "property_id": property_id, "property": plain(intended[1] if intended else match[3]),
                "input": paragraph(block, "Input on which it fails"),
                "sketch": paragraph(block, "Sketch of the failure"),
            })
    if any(outcomes[status] != count for status, count in counts.items()):
        raise ValueError(f"Comment {comment['id']}: property outcomes disagree with summary")
    return {
        "comment_id": comment["id"], "url": f"{web}/pull/{number}#issuecomment-{comment['id']}",
        "published_at": comment["created_at"], "updated_at": comment["updated_at"],
        "body_sha256": hashlib.sha256(comment["body"].encode("utf-8")).hexdigest(),
        "source_sha_prefix": snapshot[1], "base_sha_prefix": snapshot[2],
        "run_id": int(run[1]), "run_url": f"{web}/actions/runs/{run[1]}",
        "counts": counts, "properties": sum(counts.values()), "refutations": refutations,
    }


def run_numbers(run, heads, repository=REPOSITORY, prs=None):
    numbers = [pr["number"] for pr in run["pull_requests"]
               if pr["url"].startswith(f"https://api.github.com/repos/{repository}/pulls/")]
    if not numbers and (run.get("head_repository") or {}).get("full_name") == repository:
        numbers = heads.get(run["head_branch"], [])
        if len(numbers) > 1 and prs is not None:
            matching = [number for number in numbers if prs[number]["head"]["sha"] == run["head_sha"]]
            if matching:
                numbers = matching
            if len(numbers) > 1:
                numbers = [number for number in numbers
                           if prs[number]["created_at"] <= run["created_at"]
                           and (prs[number]["closed_at"] is None or run["created_at"] <= prs[number]["closed_at"])]
            if len(numbers) != 1:
                raise ValueError(f"Run {run['id']}: ambiguous historical PR branch association")
        if len(numbers) > 1:
            raise ValueError(f"Run {run['id']}: ambiguous PR branch association")
    return numbers


def replay_source(pr, repository):
    source = SOURCE_REPOSITORIES[repository.rsplit("/", 1)[1]]
    body = pr.get("body") or ""
    if body.startswith("**Parser-fix rerun:**") and "\n---\n" in body:
        body = body.split("\n---\n", 1)[1].lstrip()
    patterns = (
        rf"Historical source replay of change ([1-9]\d*) from {re.escape(source)}[.,]",
        rf"(?:Read-only source replay|Replay) of {re.escape(source)}#([1-9]\d*)\b",
    )
    if repository == "shuvendu-lahiri/litebox":
        patterns += (r"(?:Historical replay of change|Replay of historical change) ([1-9]\d*)\b",)
    for pattern in patterns:
        match = re.match(pattern, body)
        if match:
            number = int(match[1])
            return {"source_number": number,
                    "source_url": f"https://redirect.github.com/{source}/pull/{number}"}
    return {}


def build(pulls, comments, runs, generated_at, repository=REPOSITORY, cohort=None, campaign=None, fixes=None):
    web = f"https://github.com/{repository}"
    prs = {pr["number"]: pr for pr in pulls}
    if len(prs) != len(pulls):
        raise ValueError("Duplicate PR metadata")
    selected = {}
    if cohort is not None:
        if cohort["repository"] != repository:
            raise ValueError("Cohort belongs to a different repository")
        if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", cohort["source_repository"]):
            raise ValueError("Invalid cohort source repository")
        selected = {entry["number"]: entry for entry in cohort["prs"]}
        if len(selected) != len(cohort["prs"]):
            raise ValueError("Duplicate cohort PRs")
        if not selected.keys() <= prs.keys():
            raise ValueError("Missing metadata for a selected PR")
    heads = {}
    for pr in pulls:
        heads.setdefault(pr["head"]["ref"], []).append(pr["number"])
    attempts, reports = {}, {}
    run_index = {run["id"]: run for run in runs}
    for run in runs:
        if run.get("conclusion") == "skipped":
            continue
        if type(run.get("run_attempt")) is not int or run["run_attempt"] < 1:
            raise ValueError(f"Run {run['id']}: missing or invalid workflow attempt")
        for number in run_numbers(run, heads, repository, prs):
            if cohort is not None and number not in selected:
                continue
            if number not in prs:
                raise ValueError(f"Missing metadata for attempted PR {number}")
            attempts.setdefault(number, []).append(run)
    for comment in comments:
        if cohort is not None and int(comment["issue_url"].rsplit("/", 1)[1]) not in selected:
            continue
        report = parse_report(comment, repository)
        if report is None:
            continue
        number = int(comment["issue_url"].rsplit("/", 1)[1])
        run = run_index.get(report["run_id"])
        if run is None or number not in run_numbers(run, heads, repository, prs):
            raise ValueError(f"Comment {comment['id']}: workflow evidence does not match the PR")
        reports.setdefault(number, []).append(report)
    entries = []
    for number in sorted(selected.keys() | attempts.keys() | reports.keys()):
        pr = prs[number]
        history = sorted(reports.get(number, []), key=lambda r: (r["published_at"], r["comment_id"]))
        latest = history[-1] if history else None
        recent = sorted(attempts.get(number, []), key=lambda r: (r.get("run_started_at", r["created_at"]), r["id"]))
        last_run = recent[-1] if recent else None
        entries.append({
            "number": number, "title": pr["title"], "url": f"{web}/pull/{number}",
            "state": "merged" if pr["merged_at"] else pr["state"],
            "head_sha": pr["head"]["sha"], "head_branch": pr["head"]["ref"],
            "latest_report": latest, "report_history": history,
            "report_matches_current_head": pr["head"]["sha"].startswith(latest["source_sha_prefix"]) if latest else None,
            "attempts": sum(run["run_attempt"] for run in recent),
            "latest_run": {"id": last_run["id"], "url": f"{web}/actions/runs/{last_run['id']}", "status": last_run["status"],
                           "conclusion": last_run["conclusion"], "attempt": last_run["run_attempt"]} if last_run else None,
        })
        if number in selected:
            original = selected[number]
            source_number = original["source_number"]
            if type(source_number) is not int or source_number < 1:
                raise ValueError("Invalid cohort source number")
            entries[-1].update({
                "source_number": source_number, "title": original["source_title"],
                "source_url": f"https://redirect.github.com/{cohort['source_repository']}/pull/{source_number}",
                "source_head_sha": original["source_head_sha"],
            })
        else:
            entries[-1].update(replay_source(pr, repository))
    totals = Counter({status: 0 for status in STATUSES})
    for entry in entries:
        if entry["latest_report"]:
            totals.update(entry["latest_report"]["counts"])
    data = {
        "schema": 1, "repository": repository, "generated_at": generated_at,
        "name": repository.rsplit("/", 1)[1], "label": REPOSITORIES[repository.rsplit("/", 1)[1]],
        "languages": LANGUAGES[repository.rsplit("/", 1)[1]],
        "summary": {
            "selected_prs": len(entries),
            "attempted_prs": sum(bool(e["attempts"] or e["latest_report"]) for e in entries),
            "published_reports": sum(bool(e["latest_report"]) for e in entries),
            "workflow_attempts": sum(e["attempts"] for e in entries),
            "without_report": sum(e["latest_report"] is None for e in entries),
            "refuted_prs": sum(bool(e["latest_report"] and e["latest_report"]["counts"]["refuted"]) for e in entries),
            "properties": sum(totals.values()), "outcomes": dict(totals),
        },
        "prs": entries,
    }
    if campaign is not None:
        data["campaign"] = campaign
        campaign_lines(data)
    apply_fix_evidence(data, fixes)
    return data


def apply_fix_evidence(data, evidence=None):
    records = {}
    if evidence is not None:
        if evidence.get("schema") != 1 or evidence.get("repository") != data["repository"]:
            raise ValueError("Invalid fix evidence repository or schema")
        for record in evidence["reports"]:
            key = (record["run_id"], record["comment_id"])
            if key in records or record["status"] not in ("complete", "unavailable"):
                raise ValueError("Duplicate or invalid fix evidence")
            records[key] = record
    checked = unknown = checked_prs = 0
    for entry in data["prs"]:
        report = entry["latest_report"]
        if report is None:
            continue
        refuted = report["counts"]["refuted"]
        record = records.get((report["run_id"], report["comment_id"]))
        findings = []
        missing = refuted
        if record is not None and record["body_sha256"] == report["body_sha256"]:
            if record["refutations"] != refuted:
                raise ValueError("Fix evidence disagrees with published refutations")
            if record["status"] == "complete":
                findings = record["checked"]
                if (len(findings) > refuted
                        or len({finding["finding_id"] for finding in findings}) != len(findings)
                        or any(not re.fullmatch(r"[0-9a-f]{64}", finding["patch_sha256"])
                               or re.fullmatch(
                                   rf"followups/{re.escape(finding['finding_id'])}/[12]/fix/candidate\.patch",
                                   finding["patch"]) is None for finding in findings)):
                    raise ValueError("Invalid checked-fix finding identity or patch")
                missing = 0
        report.update(checked_fixes=len(findings), fix_unknown=missing, checked_fix_findings=findings)
        checked += len(findings)
        unknown += missing
        checked_prs += bool(findings)
    data["summary"].update(checked_fixes=checked, fix_unknown=unknown, checked_fix_prs=checked_prs)


def fix_count(report):
    return (str(report["checked_fixes"])
            + (f" (+{report['fix_unknown']} unknown)" if report["fix_unknown"] else ""))


def aic_amount(value):
    if isinstance(value, bool) or not isinstance(value, (str, int, Decimal)):
        raise ValueError("Invalid AIC measurement")
    amount = Decimal(value)
    if not amount.is_finite() or amount < 0:
        raise ValueError("Invalid AIC measurement")
    return amount


def usage_scope(entry):
    identity = {key: entry[key] for key in ("number", "head_sha", "attempts", "latest_run")}
    return hashlib.sha256(json.dumps(identity, sort_keys=True).encode()).hexdigest()


def usage_summary(total, measured, incomplete, no_ai):
    return {
        "total_aic": str(total),
        "average_aic_per_pr": str(total / measured) if measured else None,
        "measured_prs": measured, "incomplete_prs": incomplete, "no_ai_prs": no_ai,
    }


def apply_usage_evidence(data, evidence=None):
    records = {}
    owners = {}
    if evidence is not None:
        if evidence.get("schema") != 1 or evidence.get("repository") != data["repository"]:
            raise ValueError("Invalid usage evidence repository or schema")
        for record in evidence["prs"]:
            number = record["number"]
            if (type(number) is not int or number < 1 or number in records
                    or type(record["scope_matches"]) is not bool
                    or type(record["workflow_attempts"]) is not int
                    or record["workflow_attempts"] < 0):
                raise ValueError("Invalid or duplicate PR usage evidence")
            identities = set()
            for run in record["runs"]:
                identity = (run["run_id"], run["attempt"])
                if (any(type(value) is not int or value < 1 for value in identity)
                        or identity in identities
                        or type(run["ai_jobs"]) is not int or run["ai_jobs"] < 0):
                    raise ValueError("Invalid or duplicate workflow usage identity")
                identities.add(identity)
                if identity in owners and owners[identity] != number:
                    raise ValueError("Workflow usage assigned to multiple PRs")
                owners[identity] = number
                if run["aic"] is not None:
                    aic_amount(run["aic"])
            records[number] = record
    total = Decimal(0)
    measured = incomplete = no_ai = 0
    for entry in data["prs"]:
        entry["usage"] = {"status": "not_attempted", "aic": None}
        if not (entry["attempts"] or entry["latest_report"]):
            continue
        record = records.get(entry["number"])
        if (record is None or not record["scope_matches"]
                or record["scope_sha256"] != usage_scope(entry)
                or record["workflow_attempts"] != entry["attempts"]
                or len(record["runs"]) != entry["attempts"]
                or not record["runs"]
                or any(run["aic"] is None for run in record["runs"])):
            incomplete += 1
            entry["usage"]["status"] = "incomplete"
            continue
        amount = sum((aic_amount(run["aic"]) for run in record["runs"]), Decimal(0))
        if not any(run["ai_jobs"] for run in record["runs"]):
            if amount:
                raise ValueError("Billing evidence records charges without AI jobs")
            no_ai += 1
            entry["usage"] = {"status": "no_ai_jobs", "aic": "0"}
        else:
            measured += 1
            total += amount
            entry["usage"] = {"status": "measured", "aic": str(amount)}
    data["summary"]["usage"] = usage_summary(total, measured, incomplete, no_ai)
    if evidence is not None and "collected_at" in evidence:
        data["summary"]["usage"]["collected_at"] = evidence["collected_at"]


def usage_lines(summary):
    usage = summary.get("usage")
    if usage is None:
        return []
    average = usage["average_aic_per_pr"]
    value = f"{aic_amount(average):,.2f}" if average is not None else "N/A"
    lines = [
        f"Average review AIC: {value} per PR",
        f"Coverage: {usage['measured_prs']:,} / {summary['attempted_prs']:,} attempted PRs fully measured; "
        f"{usage['incomplete_prs']:,} with incomplete usage; "
        f"{usage['no_ai_prs']:,} with no AI execution.",
        f"{aic_amount(usage['total_aic']):,.2f} AIC across fully measured PRs. "
        "Includes retries, failed attempts, source-context and detection sessions. "
        "Incomplete measurements are excluded, not counted as zero. "
        "Quota-only PRs with no AI execution are excluded from the average.",
    ]
    if "collected_at" in usage:
        lines.append(f"Billing evidence collected: {usage['collected_at']}. "
                     "Review scope follows the saved project snapshots; "
                     "campaign-controller spend and reservations are separate.")
    return lines


def render_usage(summary):
    lines = usage_lines(summary)
    if not lines:
        return ""
    return ('<aside class="usage-summary" aria-label="Review AIC usage">'
            f"<h3>{html.escape(lines[0])}</h3>"
            + "".join(f"<p>{html.escape(line)}</p>" for line in lines[1:]) + "</aside>")


def campaign_lines(data):
    campaign = data.get("campaign")
    if campaign is None:
        return []
    summary = data["summary"]
    if campaign["repository"] != data["repository"]:
        raise ValueError("Campaign belongs to a different repository")
    planned, patches = campaign["planned_prs"], campaign["checked_patches"]
    spent, budget = Decimal(campaign["spent_aic"]), Decimal(campaign["budget_aic"])
    if (type(planned) is not int or planned < summary["attempted_prs"]
            or type(patches) is not int or patches < 0
            or not spent.is_finite() or not budget.is_finite()
            or spent < 0 or budget <= 0 or spent > budget
            or campaign["attempted_prs"] != summary["attempted_prs"]
            or campaign["workflow_attempts"] != summary["workflow_attempts"]):
        raise ValueError("Invalid or stale campaign snapshot")
    return [
        f"Campaign {campaign['status']}",
        f"{planned} source PRs selected; {summary['attempted_prs']} attempted; "
        f"{planned - summary['attempted_prs']} not attempted.",
        campaign["note"],
        f"{spent:,.2f} / {budget:,.0f} AIC spent; {patches} checked patches.",
    ]


def render_campaign(data):
    lines = campaign_lines(data)
    if not lines:
        return ""
    return ('<aside class="campaign" aria-label="Campaign status">'
            f"<h3>{html.escape(lines[0])}</h3>"
            + "".join(f"<p>{html.escape(line)}</p>" for line in lines[1:]) + "</aside>")


def ordered(data):
    return sorted(data["prs"], key=lambda e: (
        bool(e["latest_report"] and e["latest_report"]["counts"]["refuted"]),
        e["latest_report"]["published_at"] if e["latest_report"] else "", e["number"]), reverse=True)


def markdown(value):
    escaped = re.sub(r"([\\`*{}\[\]()#+.!_|~-])", r"\\\1", str(value))
    return html.escape(escaped, quote=False).replace("@", "&#64;").replace("\n", " ")


def render_markdown(data):
    total = data["summary"]
    repository = data["repository"]
    lines = [
        f"# {data['label']} NFV audit dashboard", "",
        f"**Main source languages:** {', '.join(data['languages'])}.", "",
        "Published results from the prototype [Neuro-Formal Verification](https://arxiv.org/abs/2608.21516) reviewer.",
        "**Refutations are conditional MODEL refutations, not confirmed source bugs. Verification concerns "
        "translated models under stated assumptions; failure to refute is not evidence of correctness.**", "",
        f"**[Live interactive dashboard]({SITE}{data['name']}/)** / [all repositories](" + SITE + ") "
        "or [download the standalone HTML](index.html) (no server or external dependencies).", "",
        f"Snapshot: {data['generated_at']}. Latest published report per PR supplies the counts; all report links are retained "
        "in [data.json](data.json). Workflow attempts without a published report are not counted as zero findings.", "",
        f"**{total['attempted_prs']} PRs attempted; {total['workflow_attempts']} workflow attempts; "
        f"{total['published_reports']} published reports; "
        f"{total['refuted_prs']} PRs with {total['outcomes']['refuted']} conditional refutations; "
        f"{total['outcomes']['verified']} model verifications; {total['without_report']} PRs without a published report.**", "",
        f"**{total['checked_fixes']} / {total['outcomes']['refuted']} refutations with a verified fix "
        f"across {total['checked_fix_prs']} PRs; {total['fix_unknown']} refutations with unknown fix evidence.** "
        "A verified fix means native checked repair of the complete translated property plus a hash-bound "
        "candidate source patch, not proof of source correctness. Simplifications do not count.", "",
    ]
    campaign = campaign_lines(data)
    for line in usage_lines(total):
        lines.extend([markdown(line), ""])
    if "usage" in total:
        lines.extend(["[Billing evidence and missing-data reasons](usage.json).", ""])
    if campaign:
        lines.extend([f"## {markdown(campaign[0])}", ""])
        for line in campaign[1:]:
            lines.extend([markdown(line), ""])
    lines.extend([
        "## All attempted PRs (refutations first)", "",
        "Original PR links use GitHub's no-backlink redirect; Replay PR links open the fork's audited copy.", "",
        "| Replay PR | Original PR | Change | Latest report | Properties | Refuted | Verified fixes | Verified | Exhausted | Audit failure | Review AIC (all attempts) | Evidence |",
        "|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|",
    ])
    for entry in ordered(data):
        report = entry["latest_report"]
        label = f"{repository}#{entry['number']}"
        title = markdown(entry["title"])
        source = (f"[Original PR {entry['source_number']}]({entry['source_url']})"
                  if "source_number" in entry else "Not mapped")
        usage = entry.get("usage", {})
        aic = (f"{aic_amount(usage['aic']):,.2f}" if usage.get("status") == "measured"
               else "No AI jobs" if usage.get("status") == "no_ai_jobs"
               else "-" if usage.get("status") == "not_attempted" else "Unknown")
        if report:
            counts = report["counts"]
            result = "**REFUTED (model)**" if counts["refuted"] else "Published"
            if not entry["report_matches_current_head"]:
                result += " (older head)"
            run = entry["latest_run"]
            newer_attempt = run and (run["id"] != report["run_id"] or run["conclusion"] != "success")
            if newer_attempt:
                result += " / latest attempt: " + markdown(run["conclusion"] or run["status"])
            values = [str(counts[status]) for status in STATUSES]
            if counts["refuted"]:
                values[0] = f"**{values[0]}**"
            values.insert(1, fix_count(report))
            evidence = f"[Report]({report['url']}) / [run]({report['run_url']})"
            if newer_attempt:
                evidence += f" / [latest attempt]({run['url']})"
            lines.append(f"| [{label}]({entry['url']}) | {source} | {title} | {result} | "
                         f"{report['properties']} | {' | '.join(values)} | {aic} | {evidence} |")
        else:
            run = entry["latest_run"]
            status = (run["conclusion"] or run["status"]) if run else "not attempted"
            evidence = f"[Run]({run['url']})" if run else "-"
            lines.append(f"| [{label}]({entry['url']}) | {source} | {title} | "
                         f"No published report ({markdown(status)}) | - | - | - | - | - | - | {aic} | {evidence} |")
    lines.extend(["", "## Conditional model refutations", "",
                  "The following property texts are extracted from the published reports, without new adjudication "
                  "or inference. The original report contains assumptions, source overlays and native evidence.", ""])
    for entry in ordered(data):
        report = entry["latest_report"]
        if not report:
            continue
        for finding in report["refutations"]:
            lines.extend([f"### {repository}#{entry['number']} / {finding['property_id']}", "",
                          markdown(finding["property"]), "", f"[Original report]({report['url']})", ""])
    lines.extend([
        "## Refresh and validate", "",
        "Requires Python 3.10+ and authenticated GitHub CLI read access. From the repository root:", "",
        "```text", "python refresh.py",
        "python -m unittest discover",
        "python refresh.py --check", "```", "",
        "Refresh reads PR metadata, issue comments and reviewer workflow runs. It never checks out PR heads, "
        "executes PR code, launches audits or changes proof acceptance. Malformed report counts fail refresh explicitly. "
        "Code blocks are excluded when reading outcome labels; Markdown and HTML output treat PR content as data.", "",
        "Only non-skipped reviewer attempts and published reports are included. Skipped-only setup PRs are excluded. "
        "Workflow attempts include reruns without counting PRs or property outcomes twice. "
        "A report for an older head is labeled. Counts are published outcomes, not new proof validation; "
        "comment hashes are snapshot provenance, not authentication or semantic proof.", "",
        "Where a fixed campaign cohort is supplied, its selected PRs and source-change links are preserved. "
        "This is a snapshot, not a scheduled audit or an automatically refreshing site.", "",
        "Visual layout reference: [CoZ3 NFV dashboard](https://github.com/Z3Prover/coz3/blob/main/nfv_dashboard.html). "
        "No CoZ3 audit data or adjudication results are used here.", "",
    ])
    return "\n".join(lines)


def render_outcome_tracker(summary):
    total = summary["properties"]
    statuses = (
        ("verified", "Verified (model)", "verified"),
        ("refuted", "Refuted (model)", "refuted"),
        ("type-check/audit failure", "Type-check / audit error", "failed"),
        ("resources exhausted", "Exhausted", "exhausted"),
    )
    counts = [summary["outcomes"][status] for status, _, _ in statuses]
    if (type(total) is not int or total < 0
            or any(type(count) is not int or count < 0 for count in counts)
            or sum(counts) != total):
        raise ValueError("Invalid property outcome totals for percentage tracker")
    parts = ['<div class="outcome-tracker">']
    if total:
        parts.append(
            f'<p class="muted">Shares of {total:,} properties in latest published reports. '
            'Percentages are rounded to one decimal place.</p>')
        parts.append('<div class="outcome-bar" aria-hidden="true">')
        for (_, _, class_name), count in zip(statuses, counts):
            parts.append(f'<span class="outcome-{class_name}" style="flex-grow:{count}"></span>')
        parts.append('</div>')
    else:
        parts.append('<p class="muted">No published property outcomes yet; percentages are unavailable.</p>')
    parts.append('<dl class="outcome-shares">')
    for (_, label, class_name), count in zip(statuses, counts):
        percentage = f"{count / total * 100:.1f}%" if total else "N/A"
        parts.append(
            f'<div><dt><span class="outcome-dot outcome-{class_name}" aria-hidden="true"></span>'
            f'{label}</dt><dd><strong>{percentage}</strong>'
            f'<span class="muted">{count:,} / {total:,} properties</span></dd></div>')
    parts.append('</dl>')
    if "checked_fixes" in summary:
        checked, unknown, refuted = summary["checked_fixes"], summary["fix_unknown"], summary["outcomes"]["refuted"]
        if (type(checked) is not int or type(unknown) is not int
                or checked < 0 or unknown < 0 or checked + unknown > refuted):
            raise ValueError("Invalid verified-fix totals")
        parts.append(
            f'<p class="verified-fixes"><strong>{checked:,} / {refuted:,} refutations with a verified fix</strong>'
            f' <span class="muted">({unknown:,} with unknown fix evidence)</span></p>'
            '<p class="muted">Native checked model repairs with hash-bound candidate source patches; '
            'not proof of source correctness. Simplifications do not count.</p>')
    parts.append(render_usage(summary))
    parts.append('</div>')
    return "\n".join(parts)


def render_html(data, template_name="dashboard.html"):
    template = (DIRECTORY / template_name).read_text(encoding="utf-8")
    if (template.count("__NFV_DATA__") != 1 or template.count("__NFV_CANONICAL__") != 1
            or template.count("__NFV_OUTCOME_TRACKER__") != 1
            or template.count("__NFV_REPOSITORY_TRACKERS__") != (1 if "repositories" in data else 0)):
        raise ValueError("Invalid dashboard template")
    encoded = json.dumps(data, ensure_ascii=True).replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
    canonical = SITE if "repositories" in data else f"{SITE}{data['name']}/"
    repository_trackers = "\n".join(
        f'<template id="outcome-tracker-{html.escape(repository["name"], quote=True)}">'
        f'{render_outcome_tracker(repository["summary"])}</template>'
        for repository in data.get("repositories", []))
    return (template.replace("__NFV_CANONICAL__", html.escape(canonical, quote=True))
            .replace("__NFV_OUTCOME_TRACKER__", render_campaign(data) + render_outcome_tracker(data["summary"]))
            .replace("__NFV_REPOSITORY_TRACKERS__", repository_trackers)
            .replace("__NFV_DATA__", encoded))


def fetch(repository, endpoint, key=None):
    pages = json.loads(subprocess.check_output(
        ["gh", "api", "--paginate", "--slurp", f"repos/{repository}/{endpoint}"],
        text=True, encoding="utf-8"))
    return [item for page in pages for item in (page[key] if key else page)]


def hub(snapshots):
    fields = ("attempted_prs", "published_reports", "workflow_attempts", "without_report", "refuted_prs", "properties",
              "checked_fixes", "fix_unknown", "checked_fix_prs")
    summary = {field: sum(data["summary"][field] for data in snapshots) for field in fields}
    summary["outcomes"] = {status: sum(data["summary"]["outcomes"][status] for data in snapshots) for status in STATUSES}
    usages = [data["summary"].get("usage", usage_summary(Decimal(0), 0,
               data["summary"]["attempted_prs"], 0)) for data in snapshots]
    summary["usage"] = usage_summary(
        sum((aic_amount(usage["total_aic"]) for usage in usages), Decimal(0)),
        *(sum(usage[key] for usage in usages)
          for key in ("measured_prs", "incomplete_prs", "no_ai_prs")))
    collected = [usage["collected_at"] for usage in usages if "collected_at" in usage]
    if collected:
        summary["usage"]["collected_at"] = max(collected)
    return {
        "schema": 1, "generated_at": max(data["generated_at"] for data in snapshots), "summary": summary,
        "repositories": [{key: data[key] for key in ("name", "label", "repository", "languages", "generated_at", "summary", "campaign")
                          if key in data}
                         for data in snapshots],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--input-dir", type=Path, help="Read pulls/comments/review-runs JSON in each repository subdirectory")
    mode.add_argument("--check", action="store_true", help="Check generated files offline without changing them")
    mode.add_argument("--render-only", action="store_true",
                      help="Regenerate pages from saved metadata, fix evidence and usage evidence without network access")
    parser.add_argument("--project", choices=REPOSITORIES,
                        help="Refresh only this project; retain other projects' saved evidence")
    args = parser.parse_args()
    generated_at = datetime.now(timezone.utc).isoformat()

    def collect(name):
        if args.check or args.render_only or args.project and name != args.project:
            return json.loads((DIRECTORY / name / "data.json").read_text(encoding="utf-8"))
        repository = f"shuvendu-lahiri/{name}"
        if args.input_dir:
            pulls, comments, runs = [
                json.loads((args.input_dir / name / filename).read_text(encoding="utf-8"))
                for filename in ("pulls.json", "comments.json", "review-runs.json")]
        else:
            pulls = fetch(repository, "pulls?state=all&per_page=100")
            comments = fetch(repository, "issues/comments?per_page=100")
            runs = fetch(repository, "actions/workflows/nfv-pr-review.lock.yml/runs?per_page=100", "workflow_runs")
        cohort_path = DIRECTORY / name / "cohort.json"
        cohort = json.loads(cohort_path.read_text(encoding="utf-8")) if cohort_path.exists() else None
        campaign_path = DIRECTORY / name / "campaign.json"
        campaign = json.loads(campaign_path.read_text(encoding="utf-8")) if campaign_path.exists() else None
        return build(pulls, comments, runs, generated_at, repository, cohort, campaign)

    with ThreadPoolExecutor(max_workers=len(REPOSITORIES)) as executor:
        snapshots = list(executor.map(collect, REPOSITORIES))
    for data in snapshots:
        data["languages"] = LANGUAGES[data["name"]]
        path = DIRECTORY / data["name"] / "fixes.json"
        evidence = json.loads(path.read_text(encoding="utf-8")) if path.exists() else None
        apply_fix_evidence(data, evidence)
        path = DIRECTORY / data["name"] / "usage.json"
        evidence = json.loads(path.read_text(encoding="utf-8")) if path.exists() else None
        apply_usage_evidence(data, evidence)
    outputs = {}
    for data in snapshots:
        base = DIRECTORY / data["name"]
        outputs.update({
            base / "data.json": json.dumps(data, indent=2, ensure_ascii=True) + "\n",
            base / "README.md": render_markdown(data),
            base / "index.html": render_html(data),
        })
    combined = hub(snapshots)
    outputs[DIRECTORY / "data.json"] = json.dumps(combined, indent=2, ensure_ascii=True) + "\n"
    outputs[DIRECTORY / "index.html"] = render_html(combined, "hub.html")
    for path, content in outputs.items():
        if args.check:
            if path.read_text(encoding="utf-8") != content:
                raise ValueError(f"Generated dashboard is stale: {path.relative_to(DIRECTORY)}")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            temporary = path.with_name(path.name + ".tmp")
            temporary.write_text(content, encoding="utf-8", newline="\n")
            temporary.replace(path)
    print(json.dumps({"checked" if args.check else "generated": True, **combined}))


if __name__ == "__main__":
    main()
