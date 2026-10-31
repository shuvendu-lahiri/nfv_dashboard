# LiteBox NFV audit dashboard

Published results from the prototype [Neuro-Formal Verification](https://arxiv.org/abs/2608.21516) reviewer.
**Refutations are conditional MODEL refutations, not confirmed source bugs. Verification concerns translated models under stated assumptions; failure to refute is not evidence of correctness.**

**[Live interactive dashboard](https://shuvendu-lahiri.github.io/nfv_dashboard/litebox/)** / [all repositories](https://shuvendu-lahiri.github.io/nfv_dashboard/) or [download the standalone HTML](index.html) (no server or external dependencies).

Snapshot: 2026-10-31T08:38:07.205113+00:00. Latest published report per PR supplies the counts; all report links are retained in [data.json](data.json). Workflow attempts without a published report are not counted as zero findings.

**84 PRs attempted; 155 workflow attempts; 68 published reports; 17 PRs with 22 conditional refutations; 373 model verifications; 16 PRs without a published report.**

## All attempted PRs (refutations first)

| PR | Change | Latest report | Properties | Refuted | Verified | Exhausted | Audit failure | Evidence |
|---|---|---|---:|---:|---:|---:|---:|---|
| [shuvendu-lahiri/litebox#74](https://github.com/shuvendu-lahiri/litebox/pull/74) | NFV audit \- change 1721: Consolidate Windows virtual\-memory tracking and fix reservation release bookkeeping | **REFUTED (model)** | 10 | **2** | 6 | 1 | 1 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/74#issuecomment-6536937151) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41147635725) |
| [shuvendu-lahiri/litebox#75](https://github.com/shuvendu-lahiri/litebox/pull/75) | NFV audit \- change 1720: Expose symlinks in the 9p backend | **REFUTED (model)** | 9 | **1** | 8 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/75#issuecomment-6536936167) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41147646230) |
| [shuvendu-lahiri/litebox#77](https://github.com/shuvendu-lahiri/litebox/pull/77) | NFV audit \- change 1717: Direct host file I/O in the broker on Windows | **REFUTED (model)** | 10 | **2** | 8 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/77#issuecomment-6536933264) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41147667730) |
| [shuvendu-lahiri/litebox#72](https://github.com/shuvendu-lahiri/litebox/pull/72) | NFV audit \- change 1723: Share broker ring association across platforms | **REFUTED (model)** | 10 | **1** | 9 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/72#issuecomment-6536868150) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41147612949) |
| [shuvendu-lahiri/litebox#73](https://github.com/shuvendu-lahiri/litebox/pull/73) | NFV audit \- change 1722: Add pseudo\-terminal pairs | **REFUTED (model)** | 10 | **1** | 8 | 0 | 1 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/73#issuecomment-6536704761) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41147623141) |
| [shuvendu-lahiri/litebox#65](https://github.com/shuvendu-lahiri/litebox/pull/65) | NFV audit \- change 1734: Support AF\_UNIX SOCK\_SEQPACKET sockets | **REFUTED (model)** | 10 | **1** | 9 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/65#issuecomment-6535926145) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41140753055) |
| [shuvendu-lahiri/litebox#36](https://github.com/shuvendu-lahiri/litebox/pull/36) | Replay change 1040: Migrate Tar\-RO file system to new backend | **REFUTED (model)** | 10 | **1** | 5 | 4 | 0 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/36#issuecomment-6389082690) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39462655079) |
| [shuvendu-lahiri/litebox#42](https://github.com/shuvendu-lahiri/litebox/pull/42) | Staged NFV audit \- change 1637: Cherry\-pick "LVBS: Clean up after a panic inside the vault" | **REFUTED (model)** / latest attempt: failure | 8 | **2** | 4 | 2 | 0 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/42#issuecomment-6388208161) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39532822431) / [latest attempt](https://github.com/shuvendu-lahiri/litebox/actions/runs/39532822431) |
| [shuvendu-lahiri/litebox#39](https://github.com/shuvendu-lahiri/litebox/pull/39) | Staged NFV audit \- change 1665: Zeroize sensitive data in OP\-TEE crypto syscalls | **REFUTED (model)** | 9 | **2** | 6 | 0 | 1 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/39#issuecomment-6388205075) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39532831209) |
| [shuvendu-lahiri/litebox#43](https://github.com/shuvendu-lahiri/litebox/pull/43) | Staged NFV audit \- change 1635: Cherry\-pick "LVBS: Allow concurrent vault entries" | **REFUTED (model)** | 10 | **1** | 4 | 1 | 4 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/43#issuecomment-6388020752) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39532819562) |
| [shuvendu-lahiri/litebox#31](https://github.com/shuvendu-lahiri/litebox/pull/31) | Replay change 1272: Cherry pick change 1110 Fix checking of directory search/read perms | **REFUTED (model)** | 9 | **1** | 6 | 0 | 2 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/31#issuecomment-6387051342) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39447927739) |
| [shuvendu-lahiri/litebox#24](https://github.com/shuvendu-lahiri/litebox/pull/24) | Replay change 1297: Cherry pick change 1231 Switch to explicit file system \`Context\`s | **REFUTED (model)** | 10 | **1** | 8 | 0 | 1 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/24#issuecomment-6386308409) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39424463467) |
| [shuvendu-lahiri/litebox#18](https://github.com/shuvendu-lahiri/litebox/pull/18) | Replay change 1470: Bump SNP and LVBS nightly toolchains | **REFUTED (model)** | 8 | **1** | 6 | 0 | 1 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/18#issuecomment-6385081547) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39415165751) |
| [shuvendu-lahiri/litebox#13](https://github.com/shuvendu-lahiri/litebox/pull/13) | Replay change 1539: Introduce \`LocalFs\` mounting to CLI | **REFUTED (model)** | 5 | **1** | 3 | 0 | 1 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/13#issuecomment-6384318525) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39363406105) |
| [shuvendu-lahiri/litebox#8](https://github.com/shuvendu-lahiri/litebox/pull/8) | Replay change 1648: Cherry pick change 1564 Refactor to remove \`litebox::path::Arg\` | **REFUTED (model)** | 10 | **1** | 6 | 0 | 3 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/8#issuecomment-6383719541) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39357363330) |
| [shuvendu-lahiri/litebox#3](https://github.com/shuvendu-lahiri/litebox/pull/3) | Replay change 1640: replace procfd special cases with filesystem symlinks | **REFUTED (model)** | 10 | **2** | 4 | 0 | 4 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/3#issuecomment-6383064179) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39390206732) |
| [shuvendu-lahiri/litebox#2](https://github.com/shuvendu-lahiri/litebox/pull/2) | Replay change 1656: copy broker pipe and socket reads in bulk | **REFUTED (model)** | 9 | **1** | 8 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/2#issuecomment-6382629152) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39205431424) |
| [shuvendu-lahiri/litebox#76](https://github.com/shuvendu-lahiri/litebox/pull/76) | NFV audit \- change 1719: Expose host symlinks in the userland LocalFs broker | Published | 10 | 0 | 9 | 0 | 1 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/76#issuecomment-6536909267) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41147657427) |
| [shuvendu-lahiri/litebox#71](https://github.com/shuvendu-lahiri/litebox/pull/71) | NFV audit \- change 1724: Harden OP\-TEE TA value/memref writeback | Published | 10 | 0 | 7 | 1 | 2 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/71#issuecomment-6536856272) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41147600287) |
| [shuvendu-lahiri/litebox#70](https://github.com/shuvendu-lahiri/litebox/pull/70) | NFV audit \- change 1725: Support NULL memref in the OP\-TEE shim | Published | 9 | 0 | 6 | 1 | 2 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/70#issuecomment-6536813949) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41147591127) |
| [shuvendu-lahiri/litebox#69](https://github.com/shuvendu-lahiri/litebox/pull/69) | NFV audit \- change 1727: Add per\-session controlling terminals | Published | 10 | 0 | 7 | 1 | 2 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/69#issuecomment-6536720238) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41147579936) |
| [shuvendu-lahiri/litebox#68](https://github.com/shuvendu-lahiri/litebox/pull/68) | NFV audit \- change 1729: Store inert termios settings for guest terminals | Published | 10 | 0 | 8 | 0 | 2 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/68#issuecomment-6536573405) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41147568263) |
| [shuvendu-lahiri/litebox#67](https://github.com/shuvendu-lahiri/litebox/pull/67) | NFV audit \- change 1731: Stacked runners: Cap the CPU time charged per run at one slice | Published | 9 | 0 | 5 | 0 | 4 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/67#issuecomment-6536104263) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41140780172) |
| [shuvendu-lahiri/litebox#64](https://github.com/shuvendu-lahiri/litebox/pull/64) | NFV audit \- change 1737: Change TA verification to take a X\.509 cert | Published | 7 | 0 | 7 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/64#issuecomment-6535837172) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41140738657) |
| [shuvendu-lahiri/litebox#60](https://github.com/shuvendu-lahiri/litebox/pull/60) | NFV audit \- change 1743: Add symlink creation support | Published | 10 | 0 | 8 | 1 | 1 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/60#issuecomment-6535818771) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41140681353) |
| [shuvendu-lahiri/litebox#62](https://github.com/shuvendu-lahiri/litebox/pull/62) | NFV audit \- change 1740: Fix argv/envp order on initial stack | Published | 1 | 0 | 1 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/62#issuecomment-6535571954) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41140710653) |
| [shuvendu-lahiri/litebox#66](https://github.com/shuvendu-lahiri/litebox/pull/66) | NFV audit \- change 1732: Preserve AArch64 code execute permission during cache synchronization | Published | 1 | 0 | 1 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/66#issuecomment-6535540062) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41140765965) |
| [shuvendu-lahiri/litebox#59](https://github.com/shuvendu-lahiri/litebox/pull/59) | NFV audit \- change 1745: Remove the unused copy\-on\-write file mapping path | Published | 1 | 0 | 1 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/59#issuecomment-6535323097) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41140668369) |
| [shuvendu-lahiri/litebox#55](https://github.com/shuvendu-lahiri/litebox/pull/55) | NFV audit \- change 1750: Stacked runners: Take pending interrupts before retrying upcall | Published | 4 | 0 | 1 | 0 | 3 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/55#issuecomment-6534848894) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41130552868) |
| [shuvendu-lahiri/litebox#57](https://github.com/shuvendu-lahiri/litebox/pull/57) | NFV audit \- change 1747: Redirect jumps to unpatchable syscalls | Published | 10 | 0 | 9 | 1 | 0 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/57#issuecomment-6534838741) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41130589390) |
| [shuvendu-lahiri/litebox#53](https://github.com/shuvendu-lahiri/litebox/pull/53) | NFV audit \- change 1753: Stacked runners: Add virtio\-vsock driver | Published | 10 | 0 | 8 | 0 | 2 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/53#issuecomment-6534731140) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41130517106) |
| [shuvendu-lahiri/litebox#49](https://github.com/shuvendu-lahiri/litebox/pull/49) | NFV audit \- change 1762: Add rename support | Published | 10 | 0 | 7 | 1 | 2 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/49#issuecomment-6534695800) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41130444869) |
| [shuvendu-lahiri/litebox#52](https://github.com/shuvendu-lahiri/litebox/pull/52) | NFV audit \- change 1757: Deliver host objects from the broker to runners | Published | 10 | 0 | 9 | 1 | 0 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/52#issuecomment-6534676983) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41130499764) |
| [shuvendu-lahiri/litebox#50](https://github.com/shuvendu-lahiri/litebox/pull/50) | NFV audit \- change 1761: Resume interrupted futex waits, polls, and selects like Linux | Published | 10 | 0 | 6 | 0 | 4 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/50#issuecomment-6534426803) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41130462405) |
| [shuvendu-lahiri/litebox#48](https://github.com/shuvendu-lahiri/litebox/pull/48) | NFV audit \- change 1763: Stacked runners: Wake console writers that found the device full | Published | 5 | 0 | 5 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/48#issuecomment-6534296819) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41130426553) |
| [shuvendu-lahiri/litebox#6](https://github.com/shuvendu-lahiri/litebox/pull/6) | Replay change 1671: Route chown syscalls | Published | 6 | 0 | 4 | 2 | 0 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/6#issuecomment-6389801177) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39397856512) |
| [shuvendu-lahiri/litebox#47](https://github.com/shuvendu-lahiri/litebox/pull/47) | Add LiteBox NFV audit dashboard | Published | 9 | 0 | 5 | 0 | 4 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/47#issuecomment-6389785633) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39871498222) |
| [shuvendu-lahiri/litebox#25](https://github.com/shuvendu-lahiri/litebox/pull/25) | Replay change 1284: Cherry pick change 1226 Retire legacy \`FileSystem\` trait | Published | 10 | 0 | 4 | 6 | 0 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/25#issuecomment-6389163200) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39430657719) |
| [shuvendu-lahiri/litebox#17](https://github.com/shuvendu-lahiri/litebox/pull/17) | Replay change 1672: Route chmod syscalls | Published | 6 | 0 | 5 | 1 | 0 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/17#issuecomment-6389161071) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39415165794) |
| [shuvendu-lahiri/litebox#40](https://github.com/shuvendu-lahiri/litebox/pull/40) | Staged NFV audit \- change 1651: Spin before sleeping and skip needless wakes on the broker control ring | Published | 9 | 0 | 7 | 2 | 0 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/40#issuecomment-6389144883) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39532825730) |
| [shuvendu-lahiri/litebox#37](https://github.com/shuvendu-lahiri/litebox/pull/37) | Staged NFV audit \- change 1676: Plausible results for statfs | Published | 6 | 0 | 2 | 3 | 1 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/37#issuecomment-6389050567) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39532837030) |
| [shuvendu-lahiri/litebox#26](https://github.com/shuvendu-lahiri/litebox/pull/26) | Replay change 1282: Cherry pick change 1195 Switch layered to overlay filesystem | Published | 10 | 0 | 0 | 10 | 0 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/26#issuecomment-6388996226) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39431692418) |
| [shuvendu-lahiri/litebox#4](https://github.com/shuvendu-lahiri/litebox/pull/4) | Replay change 1641: implement partial backend walks | Published | 9 | 0 | 4 | 3 | 2 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/4#issuecomment-6388781477) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39209801291) |
| [shuvendu-lahiri/litebox#44](https://github.com/shuvendu-lahiri/litebox/pull/44) | Staged NFV audit \- change 1633: Cherry\-pick "Fix handle allocator overflows in OP\-TEE shim" | Published | 10 | 0 | 9 | 0 | 1 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/44#issuecomment-6388210553) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39532816407) |
| [shuvendu-lahiri/litebox#34](https://github.com/shuvendu-lahiri/litebox/pull/34) | Replay change 1078: Normalize objdump snapshot output | Published | 7 | 0 | 2 | 4 | 1 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/34#issuecomment-6388203409) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39456543041) |
| [shuvendu-lahiri/litebox#33](https://github.com/shuvendu-lahiri/litebox/pull/33) | Replay change 1254: Cherry pick change 1106 Improve handle management | Published | 10 | 0 | 9 | 0 | 1 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/33#issuecomment-6388201818) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39456104468) |
| [shuvendu-lahiri/litebox#14](https://github.com/shuvendu-lahiri/litebox/pull/14) | Replay change 1538: Implement LocalFs backend | Published | 10 | 0 | 10 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/14#issuecomment-6388190321) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39366637569) |
| [shuvendu-lahiri/litebox#45](https://github.com/shuvendu-lahiri/litebox/pull/45) | Staged NFV audit \- change 1623: Cherry\-pick "Fix the failure handling of non\-page\-sized memory allocation" | Published | 7 | 0 | 5 | 0 | 2 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/45#issuecomment-6388116905) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39532695234) |
| [shuvendu-lahiri/litebox#46](https://github.com/shuvendu-lahiri/litebox/pull/46) | Staged NFV audit \- change 1621: Fix delayed SIGCHLD after wait4 returns ECHILD | Published | 2 | 0 | 1 | 1 | 0 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/46#issuecomment-6387966596) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39532813376) |
| [shuvendu-lahiri/litebox#41](https://github.com/shuvendu-lahiri/litebox/pull/41) | Staged NFV audit \- change 1652: Accept inherited ignored signals in the Linux userland runner | Published | 6 | 0 | 5 | 1 | 0 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/41#issuecomment-6387720259) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39532828639) |
| [shuvendu-lahiri/litebox#38](https://github.com/shuvendu-lahiri/litebox/pull/38) | Staged NFV audit \- change 1668: Stacked runners: Add virtual init | Published | 7 | 0 | 6 | 0 | 1 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/38#issuecomment-6387516345) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39532833594) |
| [shuvendu-lahiri/litebox#35](https://github.com/shuvendu-lahiri/litebox/pull/35) | Replay change 1059: Minor cleanup over change 1056 | Published | 6 | 0 | 3 | 0 | 3 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/35#issuecomment-6387473232) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39460648199) |
| [shuvendu-lahiri/litebox#32](https://github.com/shuvendu-lahiri/litebox/pull/32) | Replay change 1255: Cherry pick change 1107 Migrate in\-memory file system to new backend | Published | 10 | 0 | 8 | 1 | 1 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/32#issuecomment-6387156766) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39449644221) |
| [shuvendu-lahiri/litebox#29](https://github.com/shuvendu-lahiri/litebox/pull/29) | Replay change 1278: Cherry pick change 1113 Migrate 9p file system to new backend | Published | 10 | 0 | 6 | 1 | 3 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/29#issuecomment-6386849622) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39440128194) |
| [shuvendu-lahiri/litebox#30](https://github.com/shuvendu-lahiri/litebox/pull/30) | Replay change 1273: Cherry pick change 1111 Reduce locking contention over fd iterations | Published | 8 | 0 | 5 | 1 | 2 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/30#issuecomment-6386746637) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39440593410) |
| [shuvendu-lahiri/litebox#28](https://github.com/shuvendu-lahiri/litebox/pull/28) | Replay change 1279: Stabilize broker TCP client test | Published | 1 | 0 | 1 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/28#issuecomment-6386380592) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39437995772) |
| [shuvendu-lahiri/litebox#23](https://github.com/shuvendu-lahiri/litebox/pull/23) | Replay change 1301: Sync ulitebox to latest main | Published | 10 | 0 | 2 | 4 | 4 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/23#issuecomment-6386307299) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39422364492) |
| [shuvendu-lahiri/litebox#22](https://github.com/shuvendu-lahiri/litebox/pull/22) | Replay change 1448: Unseal file system \`Backend\` | Published | 4 | 0 | 4 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/22#issuecomment-6385829780) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39421605628) |
| [shuvendu-lahiri/litebox#19](https://github.com/shuvendu-lahiri/litebox/pull/19) | Replay change 1469: Fixups for Rust 1\.99\.0 | Published | 10 | 0 | 7 | 0 | 3 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/19#issuecomment-6385478792) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39416362695) |
| [shuvendu-lahiri/litebox#21](https://github.com/shuvendu-lahiri/litebox/pull/21) | Replay change 1452: Add fallible backend constructors to ComposerBuilder mounts | Published | 2 | 0 | 2 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/21#issuecomment-6385478151) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39419250767) |
| [shuvendu-lahiri/litebox#20](https://github.com/shuvendu-lahiri/litebox/pull/20) | Replay change 1453: Add a ratchet test limiting pub use | Published | 1 | 0 | 1 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/20#issuecomment-6385334341) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39417204232) |
| [shuvendu-lahiri/litebox#15](https://github.com/shuvendu-lahiri/litebox/pull/15) | Replay change 1533: Use try\_update instead of deprecated fetch\_update for atomics | Published | 7 | 0 | 6 | 0 | 1 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/15#issuecomment-6384749133) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39370711394) |
| [shuvendu-lahiri/litebox#12](https://github.com/shuvendu-lahiri/litebox/pull/12) | Replay change 1642: Cherry pick change 1385 Fix O\_PATH branch returns | Published | 10 | 0 | 10 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/12#issuecomment-6384179982) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39411981934) |
| [shuvendu-lahiri/litebox#11](https://github.com/shuvendu-lahiri/litebox/pull/11) | Replay change 1643: Cherry pick change 1386 Directory write check logic sits better in shim | Published | 1 | 0 | 0 | 0 | 1 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/11#issuecomment-6384003763) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39409808199) |
| [shuvendu-lahiri/litebox#10](https://github.com/shuvendu-lahiri/litebox/pull/10) | Replay change 1646: Cherry pick change 1548 Reject O\_CREAT \| O\_EXCL before backend open | Published | 4 | 0 | 1 | 3 | 0 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/10#issuecomment-6383934870) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39358987665) |
| [shuvendu-lahiri/litebox#9](https://github.com/shuvendu-lahiri/litebox/pull/9) | Replay change 1647: Cherry pick change 1558 Minor error cleanup for \`NoSearchPerms\` | Published | 10 | 0 | 10 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/9#issuecomment-6383869303) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39405410051) |
| [shuvendu-lahiri/litebox#7](https://github.com/shuvendu-lahiri/litebox/pull/7) | Replay change 1657: Cherry pick change 1566 Add support for symlink resolution | Published | 10 | 0 | 9 | 1 | 0 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/7#issuecomment-6383605651) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39399231191) |
| [shuvendu-lahiri/litebox#27](https://github.com/shuvendu-lahiri/litebox/pull/27) | Replay change 1281: Cherry pick change 1165 Join the spawned handles in tests | Published | 7 | 0 | 7 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/litebox/pull/27#issuecomment-6382201720) / [run](https://github.com/shuvendu-lahiri/litebox/actions/runs/39432560915) |
| [shuvendu-lahiri/litebox#87](https://github.com/shuvendu-lahiri/litebox/pull/87) | NFV audit \- change 1701: Remove dual\-context \`dyld\` shared cache support | No published report (pending) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41154972324) |
| [shuvendu-lahiri/litebox#86](https://github.com/shuvendu-lahiri/litebox/pull/86) | NFV audit \- change 1702: Prevent host stack exhaustion in native fork chains | No published report (in\_progress) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41154961120) |
| [shuvendu-lahiri/litebox#85](https://github.com/shuvendu-lahiri/litebox/pull/85) | NFV audit \- change 1703: Simplify Windows shim syscall dispatch and object handling | No published report (in\_progress) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41154951212) |
| [shuvendu-lahiri/litebox#84](https://github.com/shuvendu-lahiri/litebox/pull/84) | NFV audit \- change 1706: Bypass the subpage compatibility layer for macOS guests | No published report (in\_progress) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41154940198) |
| [shuvendu-lahiri/litebox#83](https://github.com/shuvendu-lahiri/litebox/pull/83) | NFV audit \- change 1707: Support shared anonymous mappings across native fork | No published report (pending) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41154929189) |
| [shuvendu-lahiri/litebox#82](https://github.com/shuvendu-lahiri/litebox/pull/82) | NFV audit \- change 1708: Keep guest\-to\-guest connections queued after client exits in smoltcp socket provider | No published report (in\_progress) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41154917386) |
| [shuvendu-lahiri/litebox#81](https://github.com/shuvendu-lahiri/litebox/pull/81) | NFV audit \- change 1709: Parse the \`dyld\` shared cache | No published report (in\_progress) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41154906208) |
| [shuvendu-lahiri/litebox#80](https://github.com/shuvendu-lahiri/litebox/pull/80) | NFV audit \- change 1713: litebox\_runner\_linux\_userland: Support \`\-\-insert\-files\` | No published report (in\_progress) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41154894342) |
| [shuvendu-lahiri/litebox#79](https://github.com/shuvendu-lahiri/litebox/pull/79) | NFV audit \- change 1714: Support terminal foreground process groups | No published report (in\_progress) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41154883667) |
| [shuvendu-lahiri/litebox#78](https://github.com/shuvendu-lahiri/litebox/pull/78) | NFV audit \- change 1716: Rename control\-ring epochs to wake counters | No published report (in\_progress) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41154872490) |
| [shuvendu-lahiri/litebox#63](https://github.com/shuvendu-lahiri/litebox/pull/63) | NFV audit \- change 1738: Fix the Linux sysinfo ABI layout | No published report (failure) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41140724678) |
| [shuvendu-lahiri/litebox#61](https://github.com/shuvendu-lahiri/litebox/pull/61) | NFV audit \- change 1742: Name shared anonymous memory lazily | No published report (failure) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41140695554) |
| [shuvendu-lahiri/litebox#58](https://github.com/shuvendu-lahiri/litebox/pull/58) | NFV audit \- change 1746: Resume interrupted relative sleeps through restart\_syscall | No published report (failure) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41140657618) |
| [shuvendu-lahiri/litebox#56](https://github.com/shuvendu-lahiri/litebox/pull/56) | NFV audit \- change 1748: Do socket I/O directly on shared buffers | No published report (failure) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41130574811) |
| [shuvendu-lahiri/litebox#54](https://github.com/shuvendu-lahiri/litebox/pull/54) | NFV audit \- change 1751: Support sched\_getscheduler and sched\_getparam | No published report (failure) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41130532806) |
| [shuvendu-lahiri/litebox#51](https://github.com/shuvendu-lahiri/litebox/pull/51) | NFV audit \- change 1760: Wait for runner helper threads to start before running the guest | No published report (failure) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41130479576) |

## Conditional model refutations

The following property texts are extracted from the published reports, without new adjudication or inference. The original report contains assumptions, source overlays and native evidence.

### shuvendu-lahiri/litebox#74 / P7

An error leaves at least one reservation unattempted\.

[Original report](https://github.com/shuvendu-lahiri/litebox/pull/74#issuecomment-6536937151)

### shuvendu-lahiri/litebox#74 / P8

A failed output write after successful creation removes the new pages\.

[Original report](https://github.com/shuvendu-lahiri/litebox/pull/74#issuecomment-6536937151)

### shuvendu-lahiri/litebox#75 / P4

A selected non\-directory, non\-PATH fid is opened with the claimed translated flags\.

[Original report](https://github.com/shuvendu-lahiri/litebox/pull/75#issuecomment-6536936167)

### shuvendu-lahiri/litebox#77 / P3

A single exposed raw part is written using its full length\.

[Original report](https://github.com/shuvendu-lahiri/litebox/pull/77#issuecomment-6536933264)

### shuvendu-lahiri/litebox#77 / P9

Fallback invokes the staging copy\.

[Original report](https://github.com/shuvendu-lahiri/litebox/pull/77#issuecomment-6536933264)

### shuvendu-lahiri/litebox#72 / P9

An error result leaves the association failed\.

[Original report](https://github.com/shuvendu-lahiri/litebox/pull/72#issuecomment-6536868150)

### shuvendu-lahiri/litebox#73 / P9

An open, nonempty write that is not blocked returns success\.

[Original report](https://github.com/shuvendu-lahiri/litebox/pull/73#issuecomment-6536704761)

### shuvendu-lahiri/litebox#65 / P7

A non\-shut channel with no room returns the blocking\-mode\-appropriate would\-block result\.

[Original report](https://github.com/shuvendu-lahiri/litebox/pull/65#issuecomment-6535926145)

### shuvendu-lahiri/litebox#36 / P7

The reported node information equals the indexed entry's node information\.

[Original report](https://github.com/shuvendu-lahiri/litebox/pull/36#issuecomment-6389082690)

### shuvendu-lahiri/litebox#42 / P3

Exactly one VTL\-switch call is observed\.

[Original report](https://github.com/shuvendu-lahiri/litebox/pull/42#issuecomment-6388208161)

### shuvendu-lahiri/litebox#42 / P6

A non\-null location emits exactly one vault\-panic line\.

[Original report](https://github.com/shuvendu-lahiri/litebox/pull/42#issuecomment-6388208161)

### shuvendu-lahiri/litebox#39 / P2

Successful initialization over existing cipher state zeroizes that state\.

[Original report](https://github.com/shuvendu-lahiri/litebox/pull/39#issuecomment-6388205075)

### shuvendu-lahiri/litebox#39 / P4

With a prior cipher, every released sensitive element is zero\.

[Original report](https://github.com/shuvendu-lahiri/litebox/pull/39#issuecomment-6388205075)

### shuvendu-lahiri/litebox#43 / P9

Speculation remains in the retpoline capture loop\.

[Original report](https://github.com/shuvendu-lahiri/litebox/pull/43#issuecomment-6388020752)

### shuvendu-lahiri/litebox#31 / P2

Allowed creation calls create\_file\_at\.

[Original report](https://github.com/shuvendu-lahiri/litebox/pull/31#issuecomment-6387051342)

### shuvendu-lahiri/litebox#24 / P9

An empty pathname returns ENOENT\.

[Original report](https://github.com/shuvendu-lahiri/litebox/pull/24#issuecomment-6386308409)

### shuvendu-lahiri/litebox#18 / P3

Every BSP invocation constructs a platform\.

[Original report](https://github.com/shuvendu-lahiri/litebox/pull/18#issuecomment-6385081547)

### shuvendu-lahiri/litebox#13 / P4

If pre\-mount setup succeeds and no LocalFs mount fails, the function returns no error\.

[Original report](https://github.com/shuvendu-lahiri/litebox/pull/13#issuecomment-6384318525)

### shuvendu-lahiri/litebox#8 / P2

With no unsupported flags and successful path resolution, sys\_unlinkat returns normally\.

[Original report](https://github.com/shuvendu-lahiri/litebox/pull/8#issuecomment-6383719541)

### shuvendu-lahiri/litebox#3 / P5

An invalid extension returns an error\.

[Original report](https://github.com/shuvendu-lahiri/litebox/pull/3#issuecomment-6383064179)

### shuvendu-lahiri/litebox#3 / P8

A nonempty declared region without a final NUL terminator triggers invalid\-parameter termination\.

[Original report](https://github.com/shuvendu-lahiri/litebox/pull/3#issuecomment-6383064179)

### shuvendu-lahiri/litebox#2 / P4

An invalid queue range must panic\.

[Original report](https://github.com/shuvendu-lahiri/litebox/pull/2#issuecomment-6382629152)

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
