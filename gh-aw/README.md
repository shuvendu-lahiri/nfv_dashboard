# gh-aw NFV audit dashboard

Published results from the prototype [Neuro-Formal Verification](https://arxiv.org/abs/2608.21516) reviewer.
**Refutations are conditional MODEL refutations, not confirmed source bugs. Verification concerns translated models under stated assumptions; failure to refute is not evidence of correctness.**

**[Live interactive dashboard](https://shuvendu-lahiri.github.io/nfv_dashboard/gh-aw/)** / [all repositories](https://shuvendu-lahiri.github.io/nfv_dashboard/) or [download the standalone HTML](index.html) (no server or external dependencies).

Snapshot: 2026-11-01T18:59:10.745194+00:00. Latest published report per PR supplies the counts; all report links are retained in [data.json](data.json). Workflow attempts without a published report are not counted as zero findings.

**1 PRs attempted; 1 workflow attempts; 1 published reports; 0 PRs with 0 conditional refutations; 4 model verifications; 0 PRs without a published report.**

## Campaign paused

100 source PRs selected; 1 attempted; 99 not attempted\.

The pilot workflow completed and its report is published, but the campaign controller has not accepted the pilot: gh\-aw transport formatting differs from the native report bytes\. Supervision is stopped; no additional audits or retries have run\. The plan contains 50 eligible source PRs each from pelikhan and dsyme\. Results below are published model\-conditional outcomes, not campaign acceptance or source\-correctness claims\.

249\.88 / 20,000 AIC spent; 0 checked patches\.

## All attempted PRs (refutations first)

| PR | Change | Latest report | Properties | Refuted | Verified | Exhausted | Audit failure | Evidence |
|---|---|---|---:|---:|---:|---:|---:|---|
| [shuvendu-lahiri/gh-aw#3](https://github.com/shuvendu-lahiri/gh-aw/pull/3) | [Source change 73588](https://redirect.github.com/github/gh-aw/pull/73588) / fix: check recorded attempt bounds before integer conversion | Published | 4 | 0 | 4 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/gh-aw/pull/3#issuecomment-6555126609) / [run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41284849816) |

## Conditional model refutations

The following property texts are extracted from the published reports, without new adjudication or inference. The original report contains assumptions, source overlays and native evidence.

## Refresh and validate

Requires Python 3.10+ and authenticated GitHub CLI read access. From the repository root:

```text
python refresh.py
python -m unittest discover
python refresh.py --check
```

Refresh reads PR metadata, issue comments and reviewer workflow runs. It never checks out PR heads, executes PR code, launches audits or changes proof acceptance. Malformed report counts fail refresh explicitly. Code blocks are excluded when reading outcome labels; Markdown and HTML output treat PR content as data.

Only non-skipped reviewer attempts and published reports are included. Skipped-only setup PRs are excluded. Workflow attempts include reruns without counting PRs or property outcomes twice. A report for an older head is labeled. Counts are published outcomes, not new proof validation; comment hashes are snapshot provenance, not authentication or semantic proof.

Where a fixed campaign cohort is supplied, its selected PRs and source-change links are preserved. This is a snapshot, not a scheduled audit or an automatically refreshing site.

Visual layout reference: [CoZ3 NFV dashboard](https://github.com/Z3Prover/coz3/blob/main/nfv_dashboard.html). No CoZ3 audit data or adjudication results are used here.
