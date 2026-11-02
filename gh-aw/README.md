# gh-aw NFV audit dashboard

Published results from the prototype [Neuro-Formal Verification](https://arxiv.org/abs/2608.21516) reviewer.
**Refutations are conditional MODEL refutations, not confirmed source bugs. Verification concerns translated models under stated assumptions; failure to refute is not evidence of correctness.**

**[Live interactive dashboard](https://shuvendu-lahiri.github.io/nfv_dashboard/gh-aw/)** / [all repositories](https://shuvendu-lahiri.github.io/nfv_dashboard/) or [download the standalone HTML](index.html) (no server or external dependencies).

Snapshot: 2026-11-02T08:42:58.833557+00:00. Latest published report per PR supplies the counts; all report links are retained in [data.json](data.json). Workflow attempts without a published report are not counted as zero findings.

**15 PRs attempted; 15 workflow attempts; 3 published reports; 0 PRs with 0 conditional refutations; 4 model verifications; 12 PRs without a published report.**

## Campaign running

100 source PRs selected; 15 attempted; 85 not attempted\.

Campaign resumed after accepting the existing pilot with a transport\-aware publication check; native evidence validation is unchanged\. 7 audits remain active\. Target: 10 conditional MODEL refutations with native checked fixes\. Recorded spend below includes only fully accounted attempts; 28,000\.00 AIC remains reserved for active or incompletely accounted attempts \(3 finished attempts have incomplete usage\)\. Total spent or reserved: 28,528\.88 / 50,000 AIC\. The repository daily guard remains 20,000 AIC\. The plan contains 50 eligible source PRs each from pelikhan and dsyme\. Published outcomes are model\-conditional, not source\-correctness claims\.

528\.88 / 50,000 AIC spent; 0 checked patches\.

## All attempted PRs (refutations first)

| PR | Change | Latest report | Properties | Refuted | Verified | Exhausted | Audit failure | Evidence |
|---|---|---|---:|---:|---:|---:|---:|---|
| [shuvendu-lahiri/gh-aw#9](https://github.com/shuvendu-lahiri/gh-aw/pull/9) | [Source change 73585](https://redirect.github.com/github/gh-aw/pull/73585) / Use standard slash\-path validation for shell graders | Published | 1 | 0 | 0 | 0 | 1 | [Report](https://github.com/shuvendu-lahiri/gh-aw/pull/9#issuecomment-6572532229) / [run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41409254306) |
| [shuvendu-lahiri/gh-aw#10](https://github.com/shuvendu-lahiri/gh-aw/pull/10) | [Source change 40154](https://redirect.github.com/github/gh-aw/pull/40154) / Fix call\-workflow compiler passing undeclared payload input \(\#40152\) | Published | 1 | 0 | 0 | 0 | 1 | [Report](https://github.com/shuvendu-lahiri/gh-aw/pull/10#issuecomment-6572378181) / [run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41409279703) |
| [shuvendu-lahiri/gh-aw#3](https://github.com/shuvendu-lahiri/gh-aw/pull/3) | [Source change 73588](https://redirect.github.com/github/gh-aw/pull/73588) / fix: check recorded attempt bounds before integer conversion | Published | 4 | 0 | 4 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/gh-aw/pull/3#issuecomment-6555126609) / [run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41284849816) |
| [shuvendu-lahiri/gh-aw#17](https://github.com/shuvendu-lahiri/gh-aw/pull/17) | [Source change 73575](https://redirect.github.com/github/gh-aw/pull/73575) / Reuse shared file writer for MCP compile progress | No published report (in\_progress) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41414064477) |
| [shuvendu-lahiri/gh-aw#16](https://github.com/shuvendu-lahiri/gh-aw/pull/16) | [Source change 38689](https://redirect.github.com/github/gh-aw/pull/38689) / Resolve \-\-gh\-aw\-ref branch/tag to commit SHA at compile time | No published report (in\_progress) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41413363688) |
| [shuvendu-lahiri/gh-aw#15](https://github.com/shuvendu-lahiri/gh-aw/pull/15) | [Source change 73583](https://redirect.github.com/github/gh-aw/pull/73583) / fix: isolate Syft outputs and update\-check state | No published report (in\_progress) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41413333428) |
| [shuvendu-lahiri/gh-aw#14](https://github.com/shuvendu-lahiri/gh-aw/pull/14) | [Source change 39707](https://redirect.github.com/github/gh-aw/pull/39707) / perf\(workflow\): check embedded action pins before gh\-api network call in ActionResolver | No published report (in\_progress) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41412609572) |
| [shuvendu-lahiri/gh-aw#13](https://github.com/shuvendu-lahiri/gh-aw/pull/13) | [Source change 73582](https://redirect.github.com/github/gh-aw/pull/73582) / fix\(parser\): confine import cache reads and atomic writes | No published report (failure) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41411895258) |
| [shuvendu-lahiri/gh-aw#12](https://github.com/shuvendu-lahiri/gh-aw/pull/12) | [Source change 39923](https://redirect.github.com/github/gh-aw/pull/39923) / Skip copilot\-requests tip for individual \(non\-org\) repository owners | No published report (in\_progress) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41411189001) |
| [shuvendu-lahiri/gh-aw#11](https://github.com/shuvendu-lahiri/gh-aw/pull/11) | [Source change 73584](https://redirect.github.com/github/gh-aw/pull/73584) / fix\(parser\): confine local include symlink targets and reads | No published report (failure) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41411160183) |
| [shuvendu-lahiri/gh-aw#8](https://github.com/shuvendu-lahiri/gh-aw/pull/8) | [Source change 42250](https://redirect.github.com/github/gh-aw/pull/42250) / fix: support max field on custom safe\-jobs | No published report (failure) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41409227119) |
| [shuvendu-lahiri/gh-aw#7](https://github.com/shuvendu-lahiri/gh-aw/pull/7) | [Source change 61105](https://redirect.github.com/github/gh-aw/pull/61105) / Fix clean\-checkout test and lint failures | No published report (failure) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41409202018) |
| [shuvendu-lahiri/gh-aw#6](https://github.com/shuvendu-lahiri/gh-aw/pull/6) | [Source change 73590](https://redirect.github.com/github/gh-aw/pull/73590) / fix: remove overflow\-prone allocation size hints | No published report (in\_progress) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41409176759) |
| [shuvendu-lahiri/gh-aw#5](https://github.com/shuvendu-lahiri/gh-aw/pull/5) | [Source change 72093](https://redirect.github.com/github/gh-aw/pull/72093) / Soften container pin update failure messages | No published report (in\_progress) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41409150540) |
| [shuvendu-lahiri/gh-aw#4](https://github.com/shuvendu-lahiri/gh-aw/pull/4) | [Source change 73672](https://redirect.github.com/github/gh-aw/pull/73672) / Fix safe\-output Git remote helper execution | No published report (failure) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41409131525) |

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
