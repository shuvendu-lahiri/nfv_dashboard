# NVX NFV formal audit dashboard

**Main source languages:** Rust, Python.

Published results from the prototype [Neuro-Formal Verification](https://arxiv.org/abs/2608.21516) reviewer.
Both verification and refutation are based on **machine-checked proofs** over translated models under their stated assumptions. Agents act as **translators, not proof reasoners**: they translate source and intent into formal models; formal verifiers establish the outcomes. Refutations are model results, not confirmed source bugs. Failure to refute is not evidence of correctness.

**[Live interactive dashboard](https://shuvendu-lahiri.github.io/nfv_dashboard/nvx/)** / [all repositories](https://shuvendu-lahiri.github.io/nfv_dashboard/) or [download the standalone HTML](index.html) (no server or external dependencies).

Snapshot: 2026-10-30T04:24:40.608973+00:00. Latest published report per PR supplies the counts; all report links are retained in [data.json](data.json). Workflow attempts without a published report are not counted as zero findings.

**50 PRs attempted; 124 workflow attempts; 45 published reports; 10 PRs with 14 refutations; 201 model verifications; 5 PRs without a published report.**

**6 / 14 refutations with a verified fix across 6 PRs; 0 refutations with unknown fix evidence.** A verified fix means native checked repair of the complete translated property plus a hash-bound candidate source patch, not proof of source correctness. Simplifications do not count.

**Average workflow time: 41m 19s (45 / 45 latest-report runs timed; 100.0% coverage; 0 missing).** First job start to last job completion, excluding the initial queue. Missing timings are excluded. Metadata is retained in [timings.json](timings.json).

Average review AIC: 777\.23 per PR

Coverage: 41 / 50 attempted PRs fully measured \(82\.0%\); 9 with incomplete usage; 0 with no AI execution\.

31,866\.35 AIC across fully measured PRs\. Includes retries, failed attempts, source\-context and detection sessions\. Incomplete measurements are excluded, not counted as zero\. Quota\-only PRs with no AI execution are excluded from the average\.

Billing evidence collected: 2026\-11\-03T23:11:53\.118856\+00:00\. Review scope follows the saved project snapshots; campaign\-controller spend and reservations are separate\.

[Billing evidence and missing-data reasons](usage.json).

## All attempted PRs (refutations first)

Original PR links use GitHub's no-backlink redirect; Replay PR links open the fork's audited copy.

| Replay PR | Original PR | Change | Latest report | Properties | Refuted | Verified fixes | Verified | Exhausted | Audit failure | Review AIC (all attempts) | Evidence |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| [shuvendu-lahiri/nvx#20](https://github.com/shuvendu-lahiri/nvx/pull/20) | [Original PR 657](https://redirect.github.com/microsoft/nvx/pull/657) | adversarial: keep executor close bounded when a child holds stdout | **REFUTED (model)** | 10 | **2** | 1 | 8 | 0 | 0 | 1,335.23 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/20#issuecomment-6514538938) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39898919181) |
| [shuvendu-lahiri/nvx#13](https://github.com/shuvendu-lahiri/nvx/pull/13) | [Original PR 681](https://redirect.github.com/microsoft/nvx/pull/681) | nvx\-rs: report the time probe's invalid options with one method | **REFUTED (model)** | 10 | **1** | 0 | 5 | 4 | 0 | 2,224.06 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/13#issuecomment-6514438588) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39893507724) |
| [shuvendu-lahiri/nvx#17](https://github.com/shuvendu-lahiri/nvx/pull/17) | [Original PR 678](https://redirect.github.com/microsoft/nvx/pull/678) | nvx\-rs: build the NVXS unit tests' epoch identities with one function | **REFUTED (model)** | 7 | **1** | 0 | 6 | 0 | 0 | 1,276.80 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/17#issuecomment-6514396713) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39896853340) |
| [shuvendu-lahiri/nvx#45](https://github.com/shuvendu-lahiri/nvx/pull/45) | [Original PR 823](https://redirect.github.com/microsoft/nvx/pull/823) | Specify sandbox launch and option contracts before fixture retirement | **REFUTED (model)** | 9 | **3** | 0 | 3 | 0 | 3 | 778.22 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/45#issuecomment-6512446360) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/40955054329) |
| [shuvendu-lahiri/nvx#47](https://github.com/shuvendu-lahiri/nvx/pull/47) | [Original PR 814](https://redirect.github.com/microsoft/nvx/pull/814) | nvx\-rs: reset an entered program's signals and let a command search PATH | **REFUTED (model)** | 9 | **1** | 1 | 7 | 0 | 1 | Unknown | [Report](https://github.com/shuvendu-lahiri/nvx/pull/47#issuecomment-6512259817) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/40955092049) |
| [shuvendu-lahiri/nvx#43](https://github.com/shuvendu-lahiri/nvx/pull/43) | [Original PR 827](https://redirect.github.com/microsoft/nvx/pull/827) | nvx\-rs: split the credit module into one submodule per structure | **REFUTED (model)** | 8 | **1** | 0 | 6 | 0 | 1 | 420.20 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/43#issuecomment-6512116709) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/40955012283) |
| [shuvendu-lahiri/nvx#36](https://github.com/shuvendu-lahiri/nvx/pull/36) | [Original PR 873](https://redirect.github.com/microsoft/nvx/pull/873) | nvx\-rs: encode activation records canonically | **REFUTED (model)** | 10 | **2** | 1 | 6 | 0 | 2 | 625.39 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/36#issuecomment-6511471874) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/40835290323) |
| [shuvendu-lahiri/nvx#39](https://github.com/shuvendu-lahiri/nvx/pull/39) | [Original PR 831](https://redirect.github.com/microsoft/nvx/pull/831) | nvx\-rs: let an execution drive a program that its caller started | **REFUTED (model)** | 10 | **1** | 1 | 5 | 1 | 3 | 1,014.03 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/39#issuecomment-6511347815) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/40835334327) |
| [shuvendu-lahiri/nvx#40](https://github.com/shuvendu-lahiri/nvx/pull/40) | [Original PR 830](https://redirect.github.com/microsoft/nvx/pull/830) | nvx\-rs: retire the golden CLI scenarios | **REFUTED (model)** | 6 | **1** | 1 | 5 | 0 | 0 | 906.62 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/40#issuecomment-6511347416) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/40835350142) |
| [shuvendu-lahiri/nvx#35](https://github.com/shuvendu-lahiri/nvx/pull/35) | [Original PR 874](https://redirect.github.com/microsoft/nvx/pull/874) | nvx\-rs: encode what Ready reports about an activation, with conformance vectors | **REFUTED (model)** | 3 | **1** | 1 | 0 | 0 | 2 | 202.70 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/35#issuecomment-6510867527) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/40835273267) |
| [shuvendu-lahiri/nvx#19](https://github.com/shuvendu-lahiri/nvx/pull/19) | [Original PR 658](https://redirect.github.com/microsoft/nvx/pull/658) | performance: keep results measured before a history reset out of the series | Published | 10 | 0 | 0 | 7 | 0 | 3 | 1,582.95 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/19#issuecomment-6514510507) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39898539854) |
| [shuvendu-lahiri/nvx#14](https://github.com/shuvendu-lahiri/nvx/pull/14) | [Original PR 680](https://redirect.github.com/microsoft/nvx/pull/680) | nvx\-rs: check the CLI session's replies through shared methods | Published | 7 | 0 | 0 | 6 | 0 | 1 | 1,476.80 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/14#issuecomment-6514444195) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39893712214) |
| [shuvendu-lahiri/nvx#16](https://github.com/shuvendu-lahiri/nvx/pull/16) | [Original PR 659](https://redirect.github.com/microsoft/nvx/pull/659) | microvm tests: stream OpenVMM transcripts to disk as they are read | Published | 10 | 0 | 0 | 8 | 0 | 2 | 1,378.44 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/16#issuecomment-6514363939) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39896467670) |
| [shuvendu-lahiri/nvx#11](https://github.com/shuvendu-lahiri/nvx/pull/11) | [Original PR 682](https://redirect.github.com/microsoft/nvx/pull/682) | nvx\-rs: parse legacy egress rules with the MXC form's helpers | Published | 7 | 0 | 0 | 5 | 0 | 2 | 1,024.73 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/11#issuecomment-6514092087) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39893495398) |
| [shuvendu-lahiri/nvx#18](https://github.com/shuvendu-lahiri/nvx/pull/18) | [Original PR 664](https://redirect.github.com/microsoft/nvx/pull/664) | release: name the mismatched fields in Ubuntu artifact manifest errors | Published | 4 | 0 | 0 | 2 | 0 | 2 | 909.26 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/18#issuecomment-6514089919) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39896859074) |
| [shuvendu-lahiri/nvx#15](https://github.com/shuvendu-lahiri/nvx/pull/15) | [Original PR 679](https://redirect.github.com/microsoft/nvx/pull/679) | nvx\-rs: run the guest programs' main through one shared function | Published | 1 | 0 | 0 | 1 | 0 | 0 | 290.26 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/15#issuecomment-6514030118) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39895920868) |
| [shuvendu-lahiri/nvx#10](https://github.com/shuvendu-lahiri/nvx/pull/10) | [Original PR 683](https://redirect.github.com/microsoft/nvx/pull/683) | nvx\-rs: check the golden tests' fixture sections with one function | Published | 1 | 0 | 0 | 1 | 0 | 0 | 393.57 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/10#issuecomment-6513912115) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39892893751) |
| [shuvendu-lahiri/nvx#12](https://github.com/shuvendu-lahiri/nvx/pull/12) | [Original PR 714](https://redirect.github.com/microsoft/nvx/pull/714) | ci: link the Windows OpenVMM test builds with /Brepro for sccache | Published | 8 | 0 | 0 | 5 | 0 | 3 | 1,456.56 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/12#issuecomment-6513605486) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39893502095) |
| [shuvendu-lahiri/nvx#6](https://github.com/shuvendu-lahiri/nvx/pull/6) | [Original PR 705](https://redirect.github.com/microsoft/nvx/pull/705) | nvx\-rs: write the NVXS record header with one function | Published | 5 | 0 | 0 | 5 | 0 | 0 | Unknown | [Report](https://github.com/shuvendu-lahiri/nvx/pull/6#issuecomment-6513419923) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39891550289) |
| [shuvendu-lahiri/nvx#9](https://github.com/shuvendu-lahiri/nvx/pull/9) | [Original PR 684](https://redirect.github.com/microsoft/nvx/pull/684) | nvx\-rs: send the guest's attachment, ACK, and CREDIT with one method | Published | 1 | 0 | 0 | 1 | 0 | 0 | 304.31 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/9#issuecomment-6513306763) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39892693600) |
| [shuvendu-lahiri/nvx#7](https://github.com/shuvendu-lahiri/nvx/pull/7) | [Original PR 689](https://redirect.github.com/microsoft/nvx/pull/689) | nvx\-rs: lay out execution\-helper configurations with one function | Published | 3 | 0 | 0 | 3 | 0 | 0 | 555.42 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/7#issuecomment-6513286729) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39891744153) |
| [shuvendu-lahiri/nvx#5](https://github.com/shuvendu-lahiri/nvx/pull/5) | [Original PR 742](https://redirect.github.com/microsoft/nvx/pull/742) | nvx\-rs: read the time checks' kernel files with one function | Published | 5 | 0 | 0 | 4 | 0 | 1 | 711.33 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/5#issuecomment-6513232485) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39890427567) |
| [shuvendu-lahiri/nvx#4](https://github.com/shuvendu-lahiri/nvx/pull/4) | [Original PR 750](https://redirect.github.com/microsoft/nvx/pull/750) | nvx\-rs: share the guest tests' /bin/sh \-c command helper | Published | 1 | 0 | 0 | 1 | 0 | 0 | 222.00 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/4#issuecomment-6513130206) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39890421003) |
| [shuvendu-lahiri/nvx#3](https://github.com/shuvendu-lahiri/nvx/pull/3) | [Original PR 755](https://redirect.github.com/microsoft/nvx/pull/755) | nvx\-rs: share the sandbox tests' policy and native helpers | Published | 1 | 0 | 0 | 1 | 0 | 0 | 254.45 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/3#issuecomment-6513108632) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39890415139) |
| [shuvendu-lahiri/nvx#2](https://github.com/shuvendu-lahiri/nvx/pull/2) | [Original PR 758](https://redirect.github.com/microsoft/nvx/pull/758) | nvx\-rs: build the guest programs' test command lines with one helper | Published | 1 | 0 | 0 | 1 | 0 | 0 | 318.96 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/2#issuecomment-6513024485) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39890408953) |
| [shuvendu-lahiri/nvx#44](https://github.com/shuvendu-lahiri/nvx/pull/44) | [Original PR 824](https://redirect.github.com/microsoft/nvx/pull/824) | nvx\-rs: check egress policies against a reference model and property tests | Published | 10 | 0 | 0 | 4 | 2 | 4 | Unknown | [Report](https://github.com/shuvendu-lahiri/nvx/pull/44#issuecomment-6512537229) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/40955033538) |
| [shuvendu-lahiri/nvx#46](https://github.com/shuvendu-lahiri/nvx/pull/46) | [Original PR 815](https://redirect.github.com/microsoft/nvx/pull/815) | nvx\-rs: sleep a Linux wait's last millisecond instead of polling a whole one | Published | 4 | 0 | 0 | 4 | 0 | 0 | Unknown | [Report](https://github.com/shuvendu-lahiri/nvx/pull/46#issuecomment-6512209119) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/40955075088) |
| [shuvendu-lahiri/nvx#48](https://github.com/shuvendu-lahiri/nvx/pull/48) | [Original PR 813](https://redirect.github.com/microsoft/nvx/pull/813) | sandbox: bind GPT disks, plan adapter launches, and stage registered images | Published | 10 | 0 | 0 | 8 | 0 | 2 | Unknown | [Report](https://github.com/shuvendu-lahiri/nvx/pull/48#issuecomment-6512090573) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/40955111250) |
| [shuvendu-lahiri/nvx#49](https://github.com/shuvendu-lahiri/nvx/pull/49) | [Original PR 807](https://redirect.github.com/microsoft/nvx/pull/807) | nvx\-rs: skip journal loading for GPT lower layers | Published | 4 | 0 | 0 | 1 | 3 | 0 | Unknown | [Report](https://github.com/shuvendu-lahiri/nvx/pull/49#issuecomment-6511934056) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/40955134520) |
| [shuvendu-lahiri/nvx#41](https://github.com/shuvendu-lahiri/nvx/pull/41) | [Original PR 829](https://redirect.github.com/microsoft/nvx/pull/829) | sandbox: refuse the \(uid\_t\)\-1 sentinel in \-\-workload\-user | Published | 2 | 0 | 0 | 0 | 0 | 2 | 330.39 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/41#issuecomment-6511868068) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/40954969307) |
| [shuvendu-lahiri/nvx#33](https://github.com/shuvendu-lahiri/nvx/pull/33) | [Original PR 877](https://redirect.github.com/microsoft/nvx/pull/877) | nvx\-rs: prepare a template's guest for a capture before root assembly | Published | 10 | 0 | 0 | 6 | 1 | 3 | 1,693.98 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/33#issuecomment-6511402632) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/40835242182) |
| [shuvendu-lahiri/nvx#38](https://github.com/shuvendu-lahiri/nvx/pull/38) | [Original PR 864](https://redirect.github.com/microsoft/nvx/pull/864) | nvx\-rs: mount the host export as a source of a root's mappings | Published | 8 | 0 | 0 | 5 | 1 | 2 | 523.68 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/38#issuecomment-6511382280) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/40835322389) |
| [shuvendu-lahiri/nvx#34](https://github.com/shuvendu-lahiri/nvx/pull/34) | [Original PR 876](https://redirect.github.com/microsoft/nvx/pull/876) | nvx\-rs: bind a resolver file into entries, and return removable runtime binds | Published | 10 | 0 | 0 | 8 | 0 | 2 | 1,123.68 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/34#issuecomment-6511179031) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/40835258683) |
| [shuvendu-lahiri/nvx#37](https://github.com/shuvendu-lahiri/nvx/pull/37) | [Original PR 871](https://redirect.github.com/microsoft/nvx/pull/871) | nvx\-rs: define the activation record of a layered root and its limits | Published | 7 | 0 | 0 | 5 | 0 | 2 | 632.17 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/37#issuecomment-6511138775) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/40835305967) |
| [shuvendu-lahiri/nvx#32](https://github.com/shuvendu-lahiri/nvx/pull/32) | [Original PR 880](https://redirect.github.com/microsoft/nvx/pull/880) | nvx\-rs: return a restore's seed in memory and zero it on drop | Published | 10 | 0 | 0 | 6 | 0 | 4 | 808.49 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/32#issuecomment-6511107158) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/40835224989) |
| [shuvendu-lahiri/nvx#29](https://github.com/shuvendu-lahiri/nvx/pull/29) | [Original PR 886](https://redirect.github.com/microsoft/nvx/pull/886) | nvx\-rs: reserve the launch of a leased clone, and document the lock order | Published | 10 | 0 | 0 | 9 | 1 | 0 | 1,404.44 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/29#issuecomment-6509965386) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/40591813556) |
| [shuvendu-lahiri/nvx#22](https://github.com/shuvendu-lahiri/nvx/pull/22) | [Original PR 936](https://redirect.github.com/microsoft/nvx/pull/936) | nvx\-rs: repair a clone's restore in the guest | Published | 10 | 0 | 0 | 5 | 1 | 4 | 1,101.99 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/22#issuecomment-6509646462) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/40591675811) |
| [shuvendu-lahiri/nvx#26](https://github.com/shuvendu-lahiri/nvx/pull/26) | [Original PR 900](https://redirect.github.com/microsoft/nvx/pull/900) | nvx\-rs: fail a provision at once for a lock file that Windows refuses for good | Published | 4 | 0 | 0 | 3 | 0 | 1 | 687.37 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/26#issuecomment-6509503805) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/40591761649) |
| [shuvendu-lahiri/nvx#21](https://github.com/shuvendu-lahiri/nvx/pull/21) | [Original PR 937](https://redirect.github.com/microsoft/nvx/pull/937) | nvx\-rs: give a clone's failures documented statuses | Published | 10 | 0 | 0 | 6 | 2 | 2 | 957.09 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/21#issuecomment-6509431041) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/40591658053) |
| [shuvendu-lahiri/nvx#27](https://github.com/shuvendu-lahiri/nvx/pull/27) | [Original PR 894](https://redirect.github.com/microsoft/nvx/pull/894) | nvx\-rs: read a process's stat line as bytes on Linux | Published | 7 | 0 | 0 | 7 | 0 | 0 | 351.58 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/27#issuecomment-6509417974) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/40591780072) |
| [shuvendu-lahiri/nvx#28](https://github.com/shuvendu-lahiri/nvx/pull/28) | [Original PR 893](https://redirect.github.com/microsoft/nvx/pull/893) | nvx\-rs: conservatively mark output without a terminal outcome | Published | 3 | 0 | 0 | 3 | 0 | 0 | 527.49 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/28#issuecomment-6509388118) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/40591795846) |
| [shuvendu-lahiri/nvx#24](https://github.com/shuvendu-lahiri/nvx/pull/24) | [Original PR 916](https://redirect.github.com/microsoft/nvx/pull/916) | nvx\-rs: finish the \-\-memory\-mib checks of sandbox provision and start | Published | 2 | 0 | 0 | 2 | 0 | 0 | 265.78 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/24#issuecomment-6508969605) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/40591715292) |
| [shuvendu-lahiri/nvx#31](https://github.com/shuvendu-lahiri/nvx/pull/31) | [Original PR 881](https://redirect.github.com/microsoft/nvx/pull/881) | nvx\-rs: add the template store | Published / latest attempt: failure | 10 | 0 | 0 | 7 | 2 | 1 | 628.51 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/31#issuecomment-6491239578) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/40835208517) / [latest attempt](https://github.com/shuvendu-lahiri/nvx/actions/runs/40835208517) |
| [shuvendu-lahiri/nvx#8](https://github.com/shuvendu-lahiri/nvx/pull/8) | [Original PR 685](https://redirect.github.com/microsoft/nvx/pull/685) | nvx\-rs: parse the mount mode, owner, and kind names with one function | Published / latest attempt: failure | 2 | 0 | 0 | 2 | 0 | 0 | 222.31 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/8#issuecomment-6383811291) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39892492366) / [latest attempt](https://github.com/shuvendu-lahiri/nvx/actions/runs/39892492366) |
| [shuvendu-lahiri/nvx#1](https://github.com/shuvendu-lahiri/nvx/pull/1) | [Original PR 747](https://redirect.github.com/microsoft/nvx/pull/747) | nvx\-rs: encode the NVXS roles' DATA and CREDIT with one function | Published / latest attempt: failure | 8 | 0 | 0 | 8 | 0 | 0 | 758.76 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/1#issuecomment-6382219305) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39888393336) / [latest attempt](https://github.com/shuvendu-lahiri/nvx/actions/runs/39888393336) |
| [shuvendu-lahiri/nvx#50](https://github.com/shuvendu-lahiri/nvx/pull/50) | [Original PR 801](https://redirect.github.com/microsoft/nvx/pull/801) | openvmm: let platform snapshots activate vCPUs at restore | No published report (failure) | - | - | - | - | - | - | Unknown | [Run](https://github.com/shuvendu-lahiri/nvx/actions/runs/40955154888) |
| [shuvendu-lahiri/nvx#42](https://github.com/shuvendu-lahiri/nvx/pull/42) | [Original PR 828](https://redirect.github.com/microsoft/nvx/pull/828) | nvx\-rs: retire the egress policy fixture and read policies as strict JSON | No published report (failure) | - | - | - | - | - | - | Unknown | [Run](https://github.com/shuvendu-lahiri/nvx/actions/runs/40954992358) |
| [shuvendu-lahiri/nvx#30](https://github.com/shuvendu-lahiri/nvx/pull/30) | [Original PR 885](https://redirect.github.com/microsoft/nvx/pull/885) | nvx\-rs: lease eligible templates to clones, and retire them | No published report (failure) | - | - | - | - | - | - | Unknown | [Run](https://github.com/shuvendu-lahiri/nvx/actions/runs/40591830617) |
| [shuvendu-lahiri/nvx#25](https://github.com/shuvendu-lahiri/nvx/pull/25) | [Original PR 908](https://redirect.github.com/microsoft/nvx/pull/908) | sandbox: reserve the double quote in live share targets | No published report (failure) | - | - | - | - | - | - | 96.41 | [Run](https://github.com/shuvendu-lahiri/nvx/actions/runs/40591736049) |
| [shuvendu-lahiri/nvx#23](https://github.com/shuvendu-lahiri/nvx/pull/23) | [Original PR 935](https://redirect.github.com/microsoft/nvx/pull/935) | openvmm: pin amd\.genoa\.v2 for Genoa hosts without the TSA immunities | No published report (failure) | - | - | - | - | - | - | 89.92 | [Run](https://github.com/shuvendu-lahiri/nvx/actions/runs/40591695929) |

## Conditional model refutations

The following property texts are extracted from the published reports, without new adjudication or inference. The original report contains assumptions, source overlays and native evidence.

### shuvendu-lahiri/nvx#20 / P6

A Popen OSError still leaves the stderr log closed\.

[Original report](https://github.com/shuvendu-lahiri/nvx/pull/20#issuecomment-6514538938)

### shuvendu-lahiri/nvx#20 / P10

Without a polling exception, close attempts the process wait\.

[Original report](https://github.com/shuvendu-lahiri/nvx/pull/20#issuecomment-6514538938)

### shuvendu-lahiri/nvx#13 / P2

A positive selected measurement duration causes one measured\-line write attempt\.

[Original report](https://github.com/shuvendu-lahiri/nvx/pull/13#issuecomment-6514438588)

### shuvendu-lahiri/nvx#17 / P4

The unsplit run produces five events\.

[Original report](https://github.com/shuvendu-lahiri/nvx/pull/17#issuecomment-6514396713)

### shuvendu-lahiri/nvx#45 / P6

All eight malformed mount values are rejected as unsupported\.

[Original report](https://github.com/shuvendu-lahiri/nvx/pull/45#issuecomment-6512446360)

### shuvendu-lahiri/nvx#45 / P8

The EROFS launch for identity \(1, 2\) produces the expected kernel command line\.

[Original report](https://github.com/shuvendu-lahiri/nvx/pull/45#issuecomment-6512446360)

### shuvendu-lahiri/nvx#45 / P9

The read\-only directory arguments equal the expected mount pair\.

[Original report](https://github.com/shuvendu-lahiri/nvx/pull/45#issuecomment-6512446360)

### shuvendu-lahiri/nvx#47 / P6

The child terminates with launch\-failure status 125\.

[Original report](https://github.com/shuvendu-lahiri/nvx/pull/47#issuecomment-6512259817)

### shuvendu-lahiri/nvx#43 / P7

The credit spend completes without panicking\.

[Original report](https://github.com/shuvendu-lahiri/nvx/pull/43#issuecomment-6512116709)

### shuvendu-lahiri/nvx#36 / P6

from\_tag\(0x01\) returns Restore\.

[Original report](https://github.com/shuvendu-lahiri/nvx/pull/36#issuecomment-6511471874)

### shuvendu-lahiri/nvx#36 / P10

Every matching declared code returns that declaration's choice\.

[Original report](https://github.com/shuvendu-lahiri/nvx/pull/36#issuecomment-6511471874)

### shuvendu-lahiri/nvx#39 / P10

A configured cgroup receives a kill attempt\.

[Original report](https://github.com/shuvendu-lahiri/nvx/pull/39#issuecomment-6511347815)

### shuvendu-lahiri/nvx#40 / P4

A non\-list \`layers\` value produces the malformed\-configuration failure\.

[Original report](https://github.com/shuvendu-lahiri/nvx/pull/40#issuecomment-6511347416)

### shuvendu-lahiri/nvx#35 / P3

Encoding a clone produces exactly 17 bytes\.

[Original report](https://github.com/shuvendu-lahiri/nvx/pull/35#issuecomment-6510867527)

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
