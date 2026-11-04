# NFV audit dashboards

**[Open the dashboard hub](https://shuvendu-lahiri.github.io/nfv_dashboard/)**

The hub has one row per repository, with languages, published/attempted PRs,
properties, conditional model refutations, verified model fixes, model
verifications, average review AIC and average workflow time. Measurement coverage
appears beside the averages, with weighted totals in the final row. Select a
repository name for its detailed PR dashboard, outcomes, campaign state and
evidence. Overall outcome and measurement details are collapsed below the table.
The overview works without JavaScript and scrolls horizontally on narrow screens.

| Repository | Main source languages | Live dashboard | GitHub-readable index |
|---|---|---|---|
| Z3 | C++ | [Open](https://shuvendu-lahiri.github.io/nfv_dashboard/z3/) | [Reports](z3/README.md) |
| LiteBox | Rust, C | [Open](https://shuvendu-lahiri.github.io/nfv_dashboard/litebox/) | [Reports](litebox/README.md) |
| NVX | Rust, Python | [Open](https://shuvendu-lahiri.github.io/nfv_dashboard/nvx/) | [Reports](nvx/README.md) |
| gh-aw | Go, JavaScript | [Open](https://shuvendu-lahiri.github.io/nfv_dashboard/gh-aw/) | [Reports](gh-aw/README.md) |
| Garnet | C# | [Open](https://shuvendu-lahiri.github.io/nfv_dashboard/garnet/) | [Reports](garnet/README.md) |

Language labels describe the repositories' main implementation languages, not
every language in their tests, bindings or tooling, or the languages covered by
each audit.

Each project table separates the fork's **Replay PR** from the **Original PR**.
Original PR links use `redirect.github.com`, GitHub's documented no-backlink
redirect. Mappings come from recorded cohorts or recognized replay provenance
headers, never from incidental references in copied descriptions. Unknown
mappings are labeled rather than guessed. These links do not make public replays
private or remove earlier upstream references.

Published results from the prototype [Neuro-Formal Verification
reviewer](https://arxiv.org/abs/2608.21516). Refutations are **conditional MODEL
refutations, not confirmed source bugs**. Verification concerns translated models
under their stated assumptions; failure to refute is not evidence of correctness.

Latest published reports supply the counts. Earlier reports remain in each
repository's `data.json`. Failed or missing publication is shown explicitly, not
as a successful zero-finding analysis. NVX retains its recorded campaign cohorts
and source-change links; Z3 and LiteBox include all non-skipped reviewer attempts.
Garnet retains its selected replay cohort and immutable source-change links,
including queued replays without reports. Use `python refresh.py --project garnet`
to update Garnet while preserving other projects' snapshots.
gh-aw shows its published pilot even while campaign acceptance is blocked. Its
campaign panel separates the 100-PR plan from actual attempts, explains the paused
state, and records credit usage and checked patches; unattempted PRs contribute
no property outcomes.

The hub and each project dashboard show the percentage and count/total fraction
of properties verified, refuted, rejected by type-check/audit, or exhausted.
Percentages use the latest published property outcomes, exclude unknown
unpublished outcomes, and are unavailable when no properties have been reported.

The hub, each project and each PR also show **refutations with a verified fix**.
Counts use native checked repairs of the whole translated property and its witness
plus SHA-256-bound candidate source patches, not simplifications. They do not prove
source correctness or source/model equivalence. Per-project `fixes.json` records
the native evidence index, bound to the exact published comment and run; missing
or mismatched evidence is shown as unknown, never as an established zero. Totals
use each PR's latest published report, without double-counting historical runs.

## Review AIC averages

The hub, repository cards and project pages show **average AIC per PR**, including
all its reviewer attempts: retries, failures, source-context sessions and detection
sessions. The overall average is total measured AIC divided by the number of fully
measured PRs across repositories, not an unweighted mean of repository averages.
Each PR's total is also shown in its project table.

Only PRs with complete billing evidence for every captured attempt contribute to
the average. Coverage lists fully measured PRs, incomplete measurements and PRs
with no AI execution (for example, quota-only skips). Missing evidence is unknown,
not zero; PRs with no AI execution are excluded from the average. Known zero-cost
executed reviews remain eligible. The measured total is not total campaign spend
when coverage is incomplete.

`collect_usage.py` reads workflow job metadata and compact `usage` artifacts.
It sums per-response `ai_credits_this_response` values for every executed agent
and detection job, including reusable source-context workflows. It does not sum
cumulative token counters, reuse daily guardrail measurements or count the same
request twice. Artifacts are bound to each attempt's usage-upload step; missing,
expired or incomplete artifacts fall back to retained job logs: only the final
`AI Credits` output within the successful, timestamp-bound token-parser step of
each executed AI job is accepted, not arbitrary agent output. If either source
is incomplete, the PR remains unknown. Explicitly skipped AI execution steps
establish zero usage; missing token logs alone do not. `usage.json`
retains run/attempt identities, artifact/job-log hashes and reasons for missing evidence,
bound to the saved PR/head/latest-run scope. Changed review scopes invalidate old
usage measurements until recollected.

Collect usage for the saved snapshots, then regenerate without changing report
or campaign snapshots:

```text
python collect_usage.py --cache-dir <external-cache-directory>
python refresh.py --render-only
python -m unittest discover
python refresh.py --check
```

Both collection and rendering are read-only with respect to reviewed repositories:
they launch no audits, reruns or proofs. `--project garnet` is also supported by
the collector. The external cache keeps terminal-run metadata, compact ZIPs and
raw job logs out of the published site; only billing measurements and provenance
are committed.

## Workflow timing averages

The hub and project pages show **average workflow time** for the runs backing
each PR's latest published report. This is wall-clock time from the first
non-skipped job starting to the last job completing: the initial queue is
excluded, while setup, source-context, auditing, publication and inter-job waits
are included. Parallel jobs are not summed. Overall averages are weighted by
timed runs, not repository averages. Coverage is shown as timed/published runs;
missing timings are excluded, never treated as zero.

Per-project `timings.json` binds GitHub job timestamps and attempt numbers to the
exact published comment and run. A later rerun does not replace an older report's
timing; missing or ambiguous attempt metadata remains unavailable.

## Refresh

Requires Python 3.10+ and authenticated GitHub CLI read access:

```text
python refresh.py
python -m unittest discover
python refresh.py --check
```

Use `python refresh.py --refresh-timings` to fetch job timing metadata for saved
latest reports without refreshing their frozen result counts; add `--project`
to limit it to one repository. Existing complete timing records are reused;
unavailable records are retried. Ordinary refreshes retain matching timing
evidence, and offline `--check` recomputes the aggregates from it.

Use `python refresh.py --project gh-aw` to refresh only gh-aw while retaining the
other projects' saved evidence. `gh-aw/cohort.json` maps attempted replays to
immutable source changes; `gh-aw/campaign.json` is the explicit campaign-status
snapshot, not a workflow-status inference. Update it when the campaign changes;
inconsistent attempt counts fail refresh rather than silently retaining stale
campaign metadata.

Refresh reads only PR metadata, published comments and workflow metadata. It never
checks out or executes inspected PR code, starts audits, reruns proofs or changes
proof acceptance. Reused historical branches are disambiguated with captured head
SHAs and PR lifetimes; ambiguous associations and malformed report counts fail
explicitly. Current and legacy numbered property headings are supported without
relabeling their property identifiers.

These are public static snapshots, not private or access-controlled pages. No
automatic refresh or audit schedule is installed. To publish a refreshed snapshot,
commit and push the generated files to the `nfv-reports` branch.

GitHub Pages serves this branch from its root. `.nojekyll` prevents source
processing; the site needs no external scripts, assets or runtime dependencies.
