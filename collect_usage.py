"""Collect compact, read-only workflow billing evidence for saved dashboard PRs."""

import argparse
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from decimal import Decimal
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess
import time
import zipfile

import refresh


def artifact_credits(content, roles):
    """Sum per-response charges, never cumulative counters or cached run totals."""
    with zipfile.ZipFile(io.BytesIO(content)) as archive:
        names = archive.namelist()
        total = Decimal(0)
        requests = {}
        for role in roles:
            paths = [name for name in names if name == f"{role}/token_usage.jsonl"]
            if len(paths) != 1:
                return None
            lines = archive.read(paths[0]).decode("utf-8").splitlines()
            if not lines:
                return None
            for line in lines:
                row = json.loads(line, parse_float=Decimal)
                if row.get("event") != "token_usage":
                    raise ValueError("Unexpected token usage event")
                if (row.get("ai_credits_this_response") is None
                        or row.get("ai_credits_fallback_pricing_used") is True):
                    return None
                amount = refresh.aic_amount(row["ai_credits_this_response"])
                request = row.get("request_id")
                if not isinstance(request, str) or not request:
                    raise ValueError("Missing billing request identity")
                if request in requests:
                    if requests[request] != amount:
                        raise ValueError("Conflicting duplicate billing request")
                    continue
                requests[request] = amount
                total += amount
        return total


def runs_ai(job):
    if job["name"].split(" / ")[-1] not in ("agent", "detection") or job["conclusion"] == "skipped":
        return False
    execution = [step for step in job.get("steps", []) if step["name"] in (
        "Execute GitHub Copilot CLI", "Execute threat detection with AWF")]
    return not execution or any(step["conclusion"] != "skipped" for step in execution)


def measure_attempt(jobs, artifacts, download):
    groups = defaultdict(list)
    for job in jobs:
        prefix, _, role = job["name"].rpartition(" / ")
        if runs_ai(job):
            groups[prefix].append(role)
    result = {"aic": None, "ai_jobs": sum(map(len, groups.values())), "artifacts": []}
    if any(job["status"] != "completed" for job in jobs):
        return {**result, "reason": "workflow still active"}
    if not any(job["name"].split(" / ")[-1] == "agent" for job in jobs):
        return {**result, "reason": "agent job metadata unavailable"}
    total = Decimal(0)
    for prefix, roles in groups.items():
        name = f"{prefix} / conclusion" if prefix else "conclusion"
        conclusions = [job for job in jobs if job["name"] == name]
        if len(conclusions) != 1:
            return {**result, "reason": "usage upload job unavailable"}
        uploads = [step for step in conclusions[0]["steps"]
                   if step["name"] == "Upload usage artifact" and step["conclusion"] == "success"]
        if len(uploads) != 1:
            return {**result, "reason": "usage upload incomplete"}
        step = uploads[0]
        matches = [artifact for artifact in artifacts
                   if (artifact["name"] == "usage" or artifact["name"].endswith("-usage"))
                   and step["started_at"] <= artifact["created_at"] <= step["completed_at"]]
        if len(matches) != 1 or matches[0]["expired"]:
            return {**result, "reason": "usage artifact missing, expired or ambiguous"}
        artifact = matches[0]
        content = download(artifact["id"])
        if content is None:
            return {**result, "reason": "usage artifact no longer available"}
        result["artifacts"].append({
            "id": artifact["id"], "name": artifact["name"],
            "sha256": hashlib.sha256(content).hexdigest(),
        })
        amount = artifact_credits(content, roles)
        if amount is None:
            return {**result, "reason": "per-response billing incomplete"}
        total += amount
    return {**result, "aic": str(total), "reason": None}


def job_credits(job, content):
    parsers = [step for step in job["steps"] if step["name"] in (
        "Parse token usage for step summary", "Parse threat detection token usage for step summary")
        and step["conclusion"] == "success"]
    if len(parsers) != 1:
        return None
    step = parsers[0]
    amounts = set()
    for line in content.decode("utf-8").splitlines():
        match = re.fullmatch(r"(\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d)(?:\.\d+)?Z AI Credits: (\d+(?:\.\d+)?)", line)
        if match and step["started_at"] <= match[1] + "Z" <= step["completed_at"]:
            amounts.add(refresh.aic_amount(match[2]))
    return amounts.pop() if len(amounts) == 1 else None


class GitHub:
    def __init__(self, repository, cache):
        self.repository = repository
        self.cache = cache / repository.replace("/", "_")
        self.cache.mkdir(parents=True, exist_ok=True)

    def read(self, endpoint, binary=False, allow_missing=False):
        key = hashlib.sha256(endpoint.encode()).hexdigest()
        suffix = ".log" if endpoint.endswith("/logs") else ".zip" if binary else ".json"
        path = self.cache / (key + suffix)
        if not path.exists():
            arguments = ["gh", "api"]
            if not binary:
                arguments += ["--paginate", "--slurp"]
            if endpoint.endswith("/logs"):
                arguments += ["--allow-escape-sequences"]
            for attempt in range(3):
                result = subprocess.run(arguments + [f"repos/{self.repository}/{endpoint}"],
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                if result.returncode == 0:
                    path.write_bytes(result.stdout)
                    break
                error = result.stderr.decode("utf-8", errors="replace")
                if allow_missing and re.search(r"HTTP (404|410)", error):
                    return None
                if attempt < 2 and re.search(
                        r"HTTP (429|500|502|503|504)|connection reset|unexpected EOF|TLS handshake|timed out",
                        error, re.I):
                    print(f"Retrying transient GitHub error for {self.repository}/{endpoint}", flush=True)
                    time.sleep(2 ** (attempt + 1))
                    continue
                raise RuntimeError(f"GitHub read failed for {self.repository}/{endpoint}: {error.strip()}")
        content = path.read_bytes()
        return content if binary else json.loads(content)

    def attempt(self, run_id, attempt, artifacts):
        pages = self.read(f"actions/runs/{run_id}/attempts/{attempt}/jobs?per_page=100")
        jobs = [job for page in pages for job in page["jobs"]]
        result = {
            "run_id": run_id, "attempt": attempt,
            **measure_attempt(jobs, artifacts, lambda identifier:
                              self.read(f"actions/artifacts/{identifier}/zip", binary=True, allow_missing=True)),
        }
        if result["aic"] is not None:
            return result
        ai_jobs = [job for job in jobs if runs_ai(job)]
        if not ai_jobs or any(job["status"] != "completed" for job in jobs):
            return result
        summaries = []
        for job in ai_jobs:
            content = self.read(f"actions/jobs/{job['id']}/logs", binary=True, allow_missing=True)
            amount = job_credits(job, content) if content is not None else None
            summaries.append({"job_id": job["id"], "name": job["name"],
                              "sha256": hashlib.sha256(content).hexdigest() if content is not None else None,
                              "aic": str(amount) if amount is not None else None})
        result["job_summaries"] = summaries
        if all(summary["aic"] is not None for summary in summaries):
            result.update(aic=str(sum((refresh.aic_amount(summary["aic"]) for summary in summaries),
                                     Decimal(0))), reason=None)
        return result


def collect(name, cache):
    directory = refresh.DIRECTORY / name
    snapshot = json.loads((directory / "data.json").read_text(encoding="utf-8"))
    repository = snapshot["repository"]
    pulls = refresh.fetch(repository, "pulls?state=all&per_page=100")
    runs = refresh.fetch(repository, "actions/workflows/nfv-pr-review.lock.yml/runs?per_page=100",
                         "workflow_runs")
    prs = {pr["number"]: pr for pr in pulls}
    heads = defaultdict(list)
    for pr in pulls:
        heads[pr["head"]["ref"]].append(pr["number"])
    selected = {entry["number"]: entry for entry in snapshot["prs"]}
    associated = defaultdict(list)
    for run in runs:
        if run["created_at"] > snapshot["generated_at"] or run["conclusion"] == "skipped":
            continue
        numbers = refresh.run_numbers(run, heads, repository, prs)
        if len(numbers) > 1:
            raise ValueError(f"Run {run['id']}: ambiguous review billing PR association")
        for number in numbers:
            if number in selected:
                associated[number].append(run)
    github = GitHub(repository, cache)
    records = []
    for number, entry in selected.items():
        recent = associated[number]
        expected = entry["attempts"]
        matched = sum(run["run_attempt"] for run in recent) == expected
        record = {"number": number, "workflow_attempts": expected,
                  "scope_matches": matched, "scope_sha256": refresh.usage_scope(entry), "runs": []}
        if matched:
            for run in recent:
                if run["status"] != "completed":
                    record["runs"].append({
                        "run_id": run["id"], "attempt": run["run_attempt"], "aic": None,
                        "ai_jobs": 0, "artifacts": [], "reason": "workflow still active",
                    })
                    continue
                artifacts = [artifact for page in github.read(
                    f"actions/runs/{run['id']}/artifacts?per_page=100")
                    for artifact in page["artifacts"]]
                for attempt in range(1, run["run_attempt"] + 1):
                    record["runs"].append(github.attempt(run["id"], attempt, artifacts))
        records.append(record)
    evidence = {"schema": 1, "repository": repository,
                "collected_at": datetime.now(timezone.utc).isoformat(), "prs": records}
    path = directory / "usage.json"
    temporary = path.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8", newline="\n")
    temporary.replace(path)
    complete = sum(record["scope_matches"] and bool(record["runs"])
                   and all(run["aic"] is not None for run in record["runs"]) for record in records)
    print(f"{repository}: {complete}/{sum(bool(entry['attempts']) for entry in selected.values())} "
          "PRs have complete workflow usage", flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache-dir", type=Path, required=True,
                        help="External directory for immutable terminal-run metadata and compact artifacts")
    parser.add_argument("--project", choices=refresh.REPOSITORIES)
    args = parser.parse_args()
    if args.cache_dir.resolve().is_relative_to(refresh.DIRECTORY):
        parser.error("--cache-dir must be outside the published dashboard repository")
    names = [args.project] if args.project else list(refresh.REPOSITORIES)
    with ThreadPoolExecutor(max_workers=3) as executor:
        list(executor.map(lambda name: collect(name, args.cache_dir), names))


if __name__ == "__main__":
    main()
