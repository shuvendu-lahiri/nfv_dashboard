# NVX NFV audit dashboard

Published results from the prototype [Neuro-Formal Verification](https://arxiv.org/abs/2608.21516) reviewer.
**Refutations are conditional MODEL refutations, not confirmed source bugs. Verification concerns translated models under stated assumptions; failure to refute is not evidence of correctness.**

**[Live interactive dashboard](https://shuvendu-lahiri.github.io/nfv_dashboard/nvx/)** / [all repositories](https://shuvendu-lahiri.github.io/nfv_dashboard/) or [download the standalone HTML](index.html) (no server or external dependencies).

Snapshot: 2026-10-24T18:47:17.208323+00:00. Latest published report per PR supplies the counts; all report links are retained in [data.json](data.json). Workflow attempts without a published report are not counted as zero findings.

**20 PRs attempted; 43 workflow attempts; 20 published reports; 4 PRs with 4 conditional refutations; 74 model verifications; 0 PRs without a published report.**

## All attempted PRs (refutations first)

| PR | Change | Latest report | Properties | Refuted | Verified | Exhausted | Audit failure | Evidence |
|---|---|---|---:|---:|---:|---:|---:|---|
| [shuvendu-lahiri/nvx#20](https://github.com/shuvendu-lahiri/nvx/pull/20) | [Source change 657](https://redirect.github.com/microsoft/nvx/pull/657) / adversarial: keep executor close bounded when a child holds stdout | **REFUTED (model)** | 9 | **1** | 8 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/20#issuecomment-6385797194) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39898919181) |
| [shuvendu-lahiri/nvx#19](https://github.com/shuvendu-lahiri/nvx/pull/19) | [Source change 658](https://redirect.github.com/microsoft/nvx/pull/658) / performance: keep results measured before a history reset out of the series | **REFUTED (model)** | 10 | **1** | 6 | 0 | 3 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/19#issuecomment-6385668120) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39898539854) |
| [shuvendu-lahiri/nvx#11](https://github.com/shuvendu-lahiri/nvx/pull/11) | [Source change 682](https://redirect.github.com/microsoft/nvx/pull/682) / nvx\-rs: parse legacy egress rules with the MXC form's helpers | **REFUTED (model)** | 7 | **1** | 4 | 0 | 2 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/11#issuecomment-6384226118) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39893495398) |
| [shuvendu-lahiri/nvx#16](https://github.com/shuvendu-lahiri/nvx/pull/16) | [Source change 659](https://redirect.github.com/microsoft/nvx/pull/659) / microvm tests: stream OpenVMM transcripts to disk as they are read | **REFUTED (model)** / latest attempt: failure | 9 | **1** | 4 | 0 | 4 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/16#issuecomment-6357198686) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39896467670) / [latest attempt](https://github.com/shuvendu-lahiri/nvx/actions/runs/39896467670) |
| [shuvendu-lahiri/nvx#18](https://github.com/shuvendu-lahiri/nvx/pull/18) | [Source change 664](https://redirect.github.com/microsoft/nvx/pull/664) / release: name the mismatched fields in Ubuntu artifact manifest errors | Published | 5 | 0 | 3 | 0 | 2 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/18#issuecomment-6385338262) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39896859074) |
| [shuvendu-lahiri/nvx#17](https://github.com/shuvendu-lahiri/nvx/pull/17) | [Source change 678](https://redirect.github.com/microsoft/nvx/pull/678) / nvx\-rs: build the NVXS unit tests' epoch identities with one function | Published | 6 | 0 | 5 | 0 | 1 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/17#issuecomment-6385037482) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39896853340) |
| [shuvendu-lahiri/nvx#15](https://github.com/shuvendu-lahiri/nvx/pull/15) | [Source change 679](https://redirect.github.com/microsoft/nvx/pull/679) / nvx\-rs: run the guest programs' main through one shared function | Published | 2 | 0 | 1 | 0 | 1 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/15#issuecomment-6384718515) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39895920868) |
| [shuvendu-lahiri/nvx#14](https://github.com/shuvendu-lahiri/nvx/pull/14) | [Source change 680](https://redirect.github.com/microsoft/nvx/pull/680) / nvx\-rs: check the CLI session's replies through shared methods | Published | 7 | 0 | 6 | 1 | 0 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/14#issuecomment-6384666255) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39893712214) |
| [shuvendu-lahiri/nvx#13](https://github.com/shuvendu-lahiri/nvx/pull/13) | [Source change 681](https://redirect.github.com/microsoft/nvx/pull/681) / nvx\-rs: report the time probe's invalid options with one method | Published | 10 | 0 | 6 | 4 | 0 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/13#issuecomment-6384590061) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39893507724) |
| [shuvendu-lahiri/nvx#10](https://github.com/shuvendu-lahiri/nvx/pull/10) | [Source change 683](https://redirect.github.com/microsoft/nvx/pull/683) / nvx\-rs: check the golden tests' fixture sections with one function | Published | 1 | 0 | 1 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/10#issuecomment-6384026244) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39892893751) |
| [shuvendu-lahiri/nvx#9](https://github.com/shuvendu-lahiri/nvx/pull/9) | [Source change 684](https://redirect.github.com/microsoft/nvx/pull/684) / nvx\-rs: send the guest's attachment, ACK, and CREDIT with one method | Published | 1 | 0 | 1 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/9#issuecomment-6383899877) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39892693600) |
| [shuvendu-lahiri/nvx#8](https://github.com/shuvendu-lahiri/nvx/pull/8) | [Source change 685](https://redirect.github.com/microsoft/nvx/pull/685) / nvx\-rs: parse the mount mode, owner, and kind names with one function | Published | 2 | 0 | 2 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/8#issuecomment-6383811291) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39892492366) |
| [shuvendu-lahiri/nvx#7](https://github.com/shuvendu-lahiri/nvx/pull/7) | [Source change 689](https://redirect.github.com/microsoft/nvx/pull/689) / nvx\-rs: lay out execution\-helper configurations with one function | Published | 3 | 0 | 2 | 0 | 1 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/7#issuecomment-6383542807) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39891744153) |
| [shuvendu-lahiri/nvx#5](https://github.com/shuvendu-lahiri/nvx/pull/5) | [Source change 742](https://redirect.github.com/microsoft/nvx/pull/742) / nvx\-rs: read the time checks' kernel files with one function | Published | 5 | 0 | 4 | 0 | 1 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/5#issuecomment-6383361770) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39890427567) |
| [shuvendu-lahiri/nvx#4](https://github.com/shuvendu-lahiri/nvx/pull/4) | [Source change 750](https://redirect.github.com/microsoft/nvx/pull/750) / nvx\-rs: share the guest tests' /bin/sh \-c command helper | Published | 2 | 0 | 1 | 0 | 1 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/4#issuecomment-6383210022) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39890421003) |
| [shuvendu-lahiri/nvx#3](https://github.com/shuvendu-lahiri/nvx/pull/3) | [Source change 755](https://redirect.github.com/microsoft/nvx/pull/755) / nvx\-rs: share the sandbox tests' policy and native helpers | Published | 1 | 0 | 1 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/3#issuecomment-6382784741) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39890415139) |
| [shuvendu-lahiri/nvx#2](https://github.com/shuvendu-lahiri/nvx/pull/2) | [Source change 758](https://redirect.github.com/microsoft/nvx/pull/758) / nvx\-rs: build the guest programs' test command lines with one helper | Published | 1 | 0 | 1 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/2#issuecomment-6382400640) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39890408953) |
| [shuvendu-lahiri/nvx#1](https://github.com/shuvendu-lahiri/nvx/pull/1) | [Source change 747](https://redirect.github.com/microsoft/nvx/pull/747) / nvx\-rs: encode the NVXS roles' DATA and CREDIT with one function | Published | 8 | 0 | 8 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/1#issuecomment-6382219305) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39888393336) |
| [shuvendu-lahiri/nvx#12](https://github.com/shuvendu-lahiri/nvx/pull/12) | [Source change 714](https://redirect.github.com/microsoft/nvx/pull/714) / ci: link the Windows OpenVMM test builds with /Brepro for sccache | Published | 8 | 0 | 7 | 0 | 1 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/12#issuecomment-6382206968) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39893502095) |
| [shuvendu-lahiri/nvx#6](https://github.com/shuvendu-lahiri/nvx/pull/6) | [Source change 705](https://redirect.github.com/microsoft/nvx/pull/705) / nvx\-rs: write the NVXS record header with one function | Published / latest attempt: failure | 5 | 0 | 3 | 0 | 2 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/6#issuecomment-6358109237) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39891550289) / [latest attempt](https://github.com/shuvendu-lahiri/nvx/actions/runs/39891550289) |

## Conditional model refutations

The following property texts are extracted from the published reports, without new adjudication or inference. The original report contains assumptions, source overlays and native evidence.

### shuvendu-lahiri/nvx#20 / P6

A process\-creation OSError closes the opened stderr log\.

[Original report](https://github.com/shuvendu-lahiri/nvx/pull/20#issuecomment-6385797194)

### shuvendu-lahiri/nvx#19 / P10

A successful git retrieval writes using the relative basename\.

[Original report](https://github.com/shuvendu-lahiri/nvx/pull/19#issuecomment-6385668120)

### shuvendu-lahiri/nvx#11 / P5

A missing cidr produces an Unsupported error\.

[Original report](https://github.com/shuvendu-lahiri/nvx/pull/11#issuecomment-6384226118)

### shuvendu-lahiri/nvx#16 / P8

When close is called, it attempts to stop the interaction before draining queued output; if interaction shutdown raises, it still attempts the drain when the transcript is open; and regardless of shutdown or drain failure, it attempts to close the transcript\. If final transcript closure returns normally, the process is marked finished\.

[Original report](https://github.com/shuvendu-lahiri/nvx/pull/16#issuecomment-6357198686)

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
