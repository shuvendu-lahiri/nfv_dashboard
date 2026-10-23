"""Refresh the public NFV dashboard hub from published GitHub evidence."""

import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import html
import json
from pathlib import Path
import re
import subprocess


REPOSITORY = "shuvendu-lahiri/litebox"
WEB = f"https://github.com/{REPOSITORY}"
DIRECTORY = Path(__file__).resolve().parent
REPOSITORIES = {"z3": "Z3", "litebox": "LiteBox", "nvx": "NVX"}
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


def build(pulls, comments, runs, generated_at, repository=REPOSITORY, cohort=None):
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
    totals = Counter({status: 0 for status in STATUSES})
    for entry in entries:
        if entry["latest_report"]:
            totals.update(entry["latest_report"]["counts"])
    return {
        "schema": 1, "repository": repository, "generated_at": generated_at,
        "name": repository.rsplit("/", 1)[1], "label": REPOSITORIES[repository.rsplit("/", 1)[1]],
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
        "## All attempted PRs (refutations first)", "",
        "| PR | Change | Latest report | Properties | Refuted | Verified | Exhausted | Audit failure | Evidence |",
        "|---|---|---|---:|---:|---:|---:|---:|---|",
    ]
    for entry in ordered(data):
        report = entry["latest_report"]
        label = f"{repository}#{entry['number']}"
        title = markdown(entry["title"])
        if "source_number" in entry:
            title = f"[Source change {entry['source_number']}]({entry['source_url']}) / {title}"
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
            evidence = f"[Report]({report['url']}) / [run]({report['run_url']})"
            if newer_attempt:
                evidence += f" / [latest attempt]({run['url']})"
            lines.append(f"| [{label}]({entry['url']}) | {title} | {result} | "
                         f"{report['properties']} | {' | '.join(values)} | {evidence} |")
        else:
            run = entry["latest_run"]
            status = (run["conclusion"] or run["status"]) if run else "not attempted"
            evidence = f"[Run]({run['url']})" if run else "-"
            lines.append(f"| [{label}]({entry['url']}) | {title} | "
                         f"No published report ({markdown(status)}) | - | - | - | - | - | {evidence} |")
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


def render_html(data, template_name="dashboard.html"):
    template = (DIRECTORY / template_name).read_text(encoding="utf-8")
    if template.count("__NFV_DATA__") != 1 or template.count("__NFV_CANONICAL__") != 1:
        raise ValueError("Invalid dashboard template")
    encoded = json.dumps(data, ensure_ascii=True).replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
    canonical = SITE if "repositories" in data else f"{SITE}{data['name']}/"
    return template.replace("__NFV_CANONICAL__", html.escape(canonical, quote=True)).replace("__NFV_DATA__", encoded)


def fetch(repository, endpoint, key=None):
    pages = json.loads(subprocess.check_output(
        ["gh", "api", "--paginate", "--slurp", f"repos/{repository}/{endpoint}"],
        text=True, encoding="utf-8"))
    return [item for page in pages for item in (page[key] if key else page)]


def hub(snapshots):
    fields = ("attempted_prs", "published_reports", "workflow_attempts", "without_report", "refuted_prs", "properties")
    summary = {field: sum(data["summary"][field] for data in snapshots) for field in fields}
    summary["outcomes"] = {status: sum(data["summary"]["outcomes"][status] for data in snapshots) for status in STATUSES}
    return {
        "schema": 1, "generated_at": max(data["generated_at"] for data in snapshots), "summary": summary,
        "repositories": [{key: data[key] for key in ("name", "label", "repository", "generated_at", "summary")}
                         for data in snapshots],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--input-dir", type=Path, help="Read pulls/comments/review-runs JSON in each repository subdirectory")
    mode.add_argument("--check", action="store_true", help="Check generated files offline without changing them")
    args = parser.parse_args()
    generated_at = datetime.now(timezone.utc).isoformat()

    def collect(name):
        if args.check:
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
        return build(pulls, comments, runs, generated_at, repository, cohort)

    with ThreadPoolExecutor(max_workers=len(REPOSITORIES)) as executor:
        snapshots = list(executor.map(collect, REPOSITORIES))
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
