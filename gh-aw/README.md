# gh-aw NFV audit dashboard

Published results from the prototype [Neuro-Formal Verification](https://arxiv.org/abs/2608.21516) reviewer.
**Refutations are conditional MODEL refutations, not confirmed source bugs. Verification concerns translated models under stated assumptions; failure to refute is not evidence of correctness.**

**[Live interactive dashboard](https://shuvendu-lahiri.github.io/nfv_dashboard/gh-aw/)** / [all repositories](https://shuvendu-lahiri.github.io/nfv_dashboard/) or [download the standalone HTML](index.html) (no server or external dependencies).

Snapshot: 2026-11-02T09:53:51.103336+00:00. Latest published report per PR supplies the counts; all report links are retained in [data.json](data.json). Workflow attempts without a published report are not counted as zero findings.

**31 PRs attempted; 31 workflow attempts; 13 published reports; 2 PRs with 2 conditional refutations; 49 model verifications; 18 PRs without a published report.**

**2 / 2 refutations with a verified fix across 2 PRs; 0 refutations with unknown fix evidence.** A verified fix means native checked repair of the complete translated property plus a hash-bound candidate source patch, not proof of source correctness. Simplifications do not count.

## Campaign running

100 source PRs selected; 31 attempted; 69 not attempted\.

5 attempts remain unresolved in the controller\. Goal: 10 conditional MODEL refutations with native checked fixes; continue within the 50,000\-AIC aggregate cap, without an early target stop\. Recorded spend below includes only fully accounted attempts; 44,800\.00 AIC remains reserved for active or incompletely accounted attempts \(11 finished attempts have incomplete usage\)\. Total spent or reserved: 49,325\.99 / 50,000 AIC\. Missing usage is not zero consumption\. The repository daily guard remains 20,000 AIC\. The plan contains 50 eligible source PRs each from pelikhan and dsyme\. Published outcomes are model\-conditional, not source\-correctness claims\.

4,525\.99 / 50,000 AIC spent; 2 checked patches\.

## All attempted PRs (refutations first)

| PR | Change | Latest report | Properties | Refuted | Verified fixes | Verified | Exhausted | Audit failure | Evidence |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| [shuvendu-lahiri/gh-aw#28](https://github.com/shuvendu-lahiri/gh-aw/pull/28) | [Source change 37313](https://redirect.github.com/github/gh-aw/pull/37313) / feat\(cli\): add \-\-gh\-aw\-ref convenience flag to compile | **REFUTED (model)** | 1 | **1** | 1 | 0 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/gh-aw/pull/28#issuecomment-6574011081) / [run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41419957239) |
| [shuvendu-lahiri/gh-aw#15](https://github.com/shuvendu-lahiri/gh-aw/pull/15) | [Source change 73583](https://redirect.github.com/github/gh-aw/pull/73583) / fix: isolate Syft outputs and update\-check state | **REFUTED (model)** | 9 | **1** | 1 | 7 | 0 | 1 | [Report](https://github.com/shuvendu-lahiri/gh-aw/pull/15#issuecomment-6573420369) / [run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41413333428) |
| [shuvendu-lahiri/gh-aw#21](https://github.com/shuvendu-lahiri/gh-aw/pull/21) | [Source change 72942](https://redirect.github.com/github/gh-aw/pull/72942) / feat\(cli\): diagnose assign\-to\-agent credentials in doctor | Published | 10 | 0 | 0 | 5 | 2 | 3 | [Report](https://github.com/shuvendu-lahiri/gh-aw/pull/21#issuecomment-6573960716) / [run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41416181507) |
| [shuvendu-lahiri/gh-aw#19](https://github.com/shuvendu-lahiri/gh-aw/pull/19) | [Source change 72951](https://redirect.github.com/github/gh-aw/pull/72951) / Deduplicate compiler tips across workflows | Published | 6 | 0 | 0 | 6 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/gh-aw/pull/19#issuecomment-6573536584) / [run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41416117966) |
| [shuvendu-lahiri/gh-aw#14](https://github.com/shuvendu-lahiri/gh-aw/pull/14) | [Source change 39707](https://redirect.github.com/github/gh-aw/pull/39707) / perf\(workflow\): check embedded action pins before gh\-api network call in ActionResolver | Published | 7 | 0 | 0 | 7 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/gh-aw/pull/14#issuecomment-6573080103) / [run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41412609572) |
| [shuvendu-lahiri/gh-aw#17](https://github.com/shuvendu-lahiri/gh-aw/pull/17) | [Source change 73575](https://redirect.github.com/github/gh-aw/pull/73575) / Reuse shared file writer for MCP compile progress | Published | 3 | 0 | 0 | 3 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/gh-aw/pull/17#issuecomment-6573039490) / [run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41414064477) |
| [shuvendu-lahiri/gh-aw#16](https://github.com/shuvendu-lahiri/gh-aw/pull/16) | [Source change 38689](https://redirect.github.com/github/gh-aw/pull/38689) / Resolve \-\-gh\-aw\-ref branch/tag to commit SHA at compile time | Published | 4 | 0 | 0 | 3 | 0 | 1 | [Report](https://github.com/shuvendu-lahiri/gh-aw/pull/16#issuecomment-6572929171) / [run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41413363688) |
| [shuvendu-lahiri/gh-aw#5](https://github.com/shuvendu-lahiri/gh-aw/pull/5) | [Source change 72093](https://redirect.github.com/github/gh-aw/pull/72093) / Soften container pin update failure messages | Published | 10 | 0 | 0 | 5 | 2 | 3 | [Report](https://github.com/shuvendu-lahiri/gh-aw/pull/5#issuecomment-6572884112) / [run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41409150540) |
| [shuvendu-lahiri/gh-aw#6](https://github.com/shuvendu-lahiri/gh-aw/pull/6) | [Source change 73590](https://redirect.github.com/github/gh-aw/pull/73590) / fix: remove overflow\-prone allocation size hints | Published | 10 | 0 | 0 | 5 | 3 | 2 | [Report](https://github.com/shuvendu-lahiri/gh-aw/pull/6#issuecomment-6572867594) / [run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41409176759) |
| [shuvendu-lahiri/gh-aw#12](https://github.com/shuvendu-lahiri/gh-aw/pull/12) | [Source change 39923](https://redirect.github.com/github/gh-aw/pull/39923) / Skip copilot\-requests tip for individual \(non\-org\) repository owners | Published | 5 | 0 | 0 | 4 | 0 | 1 | [Report](https://github.com/shuvendu-lahiri/gh-aw/pull/12#issuecomment-6572854794) / [run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41411189001) |
| [shuvendu-lahiri/gh-aw#9](https://github.com/shuvendu-lahiri/gh-aw/pull/9) | [Source change 73585](https://redirect.github.com/github/gh-aw/pull/73585) / Use standard slash\-path validation for shell graders | Published | 1 | 0 | 0 | 0 | 0 | 1 | [Report](https://github.com/shuvendu-lahiri/gh-aw/pull/9#issuecomment-6572532229) / [run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41409254306) |
| [shuvendu-lahiri/gh-aw#10](https://github.com/shuvendu-lahiri/gh-aw/pull/10) | [Source change 40154](https://redirect.github.com/github/gh-aw/pull/40154) / Fix call\-workflow compiler passing undeclared payload input \(\#40152\) | Published | 1 | 0 | 0 | 0 | 0 | 1 | [Report](https://github.com/shuvendu-lahiri/gh-aw/pull/10#issuecomment-6572378181) / [run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41409279703) |
| [shuvendu-lahiri/gh-aw#3](https://github.com/shuvendu-lahiri/gh-aw/pull/3) | [Source change 73588](https://redirect.github.com/github/gh-aw/pull/73588) / fix: check recorded attempt bounds before integer conversion | Published | 4 | 0 | 0 | 4 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/gh-aw/pull/3#issuecomment-6555126609) / [run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41284849816) |
| [shuvendu-lahiri/gh-aw#33](https://github.com/shuvendu-lahiri/gh-aw/pull/33) | [Source change 72395](https://redirect.github.com/github/gh-aw/pull/72395) / feat: add optional actions\-lock integration to compile | No published report (in\_progress) | - | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41424280837) |
| [shuvendu-lahiri/gh-aw#32](https://github.com/shuvendu-lahiri/gh-aw/pull/32) | [Source change 36657](https://redirect.github.com/github/gh-aw/pull/36657) / feat: support multi\-repo wildcard target\-repo in safe\_outputs job | No published report (queued) | - | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41424247191) |
| [shuvendu-lahiri/gh-aw#31](https://github.com/shuvendu-lahiri/gh-aw/pull/31) | [Source change 72407](https://redirect.github.com/github/gh-aw/pull/72407) / Merge imported job outputs with main workflow precedence | No published report (in\_progress) | - | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41422333871) |
| [shuvendu-lahiri/gh-aw#30](https://github.com/shuvendu-lahiri/gh-aw/pull/30) | [Source change 37225](https://redirect.github.com/github/gh-aw/pull/37225) / fix\(safe\-outputs\): prevent MCP server git hangs; add base\-branch \+ checkout manifest | No published report (failure) | - | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41421555311) |
| [shuvendu-lahiri/gh-aw#29](https://github.com/shuvendu-lahiri/gh-aw/pull/29) | [Source change 72412](https://redirect.github.com/github/gh-aw/pull/72412) / Add guided pull\_request\_target fixes and safe role restriction | No published report (failure) | - | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41420761367) |
| [shuvendu-lahiri/gh-aw#27](https://github.com/shuvendu-lahiri/gh-aw/pull/27) | [Source change 72418](https://redirect.github.com/github/gh-aw/pull/72418) / Add interactive org and enterprise update rollouts | No published report (in\_progress) | - | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41419923921) |
| [shuvendu-lahiri/gh-aw#26](https://github.com/shuvendu-lahiri/gh-aw/pull/26) | [Source change 37359](https://redirect.github.com/github/gh-aw/pull/37359) / feat\(compile\): add hidden \`\-\-use\-samples\` flag for deterministic safe\-outputs replay | No published report (failure) | - | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41419127709) |
| [shuvendu-lahiri/gh-aw#25](https://github.com/shuvendu-lahiri/gh-aw/pull/25) | [Source change 72542](https://redirect.github.com/github/gh-aw/pull/72542) / Add privileged checkout and cross\-run artifact execution diagnostics | No published report (in\_progress) | - | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41418383499) |
| [shuvendu-lahiri/gh-aw#24](https://github.com/shuvendu-lahiri/gh-aw/pull/24) | [Source change 37437](https://redirect.github.com/github/gh-aw/pull/37437) / feat\(max\-ai\-credits\): allow \-1 to disable budget enforcement and steering | No published report (failure) | - | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41418350383) |
| [shuvendu-lahiri/gh-aw#23](https://github.com/shuvendu-lahiri/gh-aw/pull/23) | [Source change 72579](https://redirect.github.com/github/gh-aw/pull/72579) / fix\(workflow\): prevent compiler\-only PR trigger filters from leaking | No published report (failure) | - | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41417616830) |
| [shuvendu-lahiri/gh-aw#22](https://github.com/shuvendu-lahiri/gh-aw/pull/22) | [Source change 37537](https://redirect.github.com/github/gh-aw/pull/37537) / Accept runtime $\{\{ \.\.\. \}\} expressions in safe\-outputs samples | No published report (failure) | - | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41416889883) |
| [shuvendu-lahiri/gh-aw#20](https://github.com/shuvendu-lahiri/gh-aw/pull/20) | [Source change 37539](https://redirect.github.com/github/gh-aw/pull/37539) / Make safe\-outputs sample runtime\-expression substitution schema\-aware | No published report (failure) | - | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41416148059) |
| [shuvendu-lahiri/gh-aw#18](https://github.com/shuvendu-lahiri/gh-aw/pull/18) | [Source change 37567](https://redirect.github.com/github/gh-aw/pull/37567) / Fix golint stringsseq modernize finding in nolint\.go | No published report (failure) | - | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41416091834) |
| [shuvendu-lahiri/gh-aw#13](https://github.com/shuvendu-lahiri/gh-aw/pull/13) | [Source change 73582](https://redirect.github.com/github/gh-aw/pull/73582) / fix\(parser\): confine import cache reads and atomic writes | No published report (failure) | - | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41411895258) |
| [shuvendu-lahiri/gh-aw#11](https://github.com/shuvendu-lahiri/gh-aw/pull/11) | [Source change 73584](https://redirect.github.com/github/gh-aw/pull/73584) / fix\(parser\): confine local include symlink targets and reads | No published report (failure) | - | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41411160183) |
| [shuvendu-lahiri/gh-aw#8](https://github.com/shuvendu-lahiri/gh-aw/pull/8) | [Source change 42250](https://redirect.github.com/github/gh-aw/pull/42250) / fix: support max field on custom safe\-jobs | No published report (failure) | - | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41409227119) |
| [shuvendu-lahiri/gh-aw#7](https://github.com/shuvendu-lahiri/gh-aw/pull/7) | [Source change 61105](https://redirect.github.com/github/gh-aw/pull/61105) / Fix clean\-checkout test and lint failures | No published report (failure) | - | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41409202018) |
| [shuvendu-lahiri/gh-aw#4](https://github.com/shuvendu-lahiri/gh-aw/pull/4) | [Source change 73672](https://redirect.github.com/github/gh-aw/pull/73672) / Fix safe\-output Git remote helper execution | No published report (failure) | - | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/gh-aw/actions/runs/41409131525) |

## Conditional model refutations

The following property texts are extracted from the published reports, without new adjudication or inference. The original report contains assumptions, source overlays and native evidence.

### shuvendu-lahiri/gh-aw#28 / P1

\`\-\-gh\-aw\-ref\` selects release action mode\.

[Original report](https://github.com/shuvendu-lahiri/gh-aw/pull/28#issuecomment-6574011081)

### shuvendu-lahiri/gh-aw#15 / P1

A nonempty result is beneath the per\-user update\-check directory\.

[Original report](https://github.com/shuvendu-lahiri/gh-aw/pull/15#issuecomment-6573420369)

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
