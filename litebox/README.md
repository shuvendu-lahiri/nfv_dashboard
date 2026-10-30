# LiteBox NFV audit dashboard

Published results from the prototype [Neuro-Formal Verification](https://arxiv.org/abs/2608.21516) reviewer.
**Refutations are conditional MODEL refutations, not confirmed source bugs. Verification concerns translated models under stated assumptions; failure to refute is not evidence of correctness.**

**[Live interactive dashboard](https://shuvendu-lahiri.github.io/nfv_dashboard/litebox/)** / [all repositories](https://shuvendu-lahiri.github.io/nfv_dashboard/) or [download the standalone HTML](index.html) (no server or external dependencies).

Snapshot: 2026-10-30T22:27:24.916902+00:00. Latest published report per PR supplies the counts; all report links are retained in [data.json](data.json). Workflow attempts without a published report are not counted as zero findings.

**54 PRs attempted; 115 workflow attempts; 49 published reports; 11 PRs with 14 conditional refutations; 255 model verifications; 5 PRs without a published report.**

## All attempted PRs (refutations first)

| PR | Change | Latest report | Properties | Refuted | Verified | Exhausted | Audit failure | Evidence |
|---|---|---|---:|---:|---:|---:|---:|---|
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
| [shuvendu-lahiri/litebox#57](https://github.com/shuvendu-lahiri/litebox/pull/57) | NFV audit \- change 1747: Redirect jumps to unpatchable syscalls | No published report (in\_progress) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41130589390) |
| [shuvendu-lahiri/litebox#56](https://github.com/shuvendu-lahiri/litebox/pull/56) | NFV audit \- change 1748: Do socket I/O directly on shared buffers | No published report (failure) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41130574811) |
| [shuvendu-lahiri/litebox#55](https://github.com/shuvendu-lahiri/litebox/pull/55) | NFV audit \- change 1750: Stacked runners: Take pending interrupts before retrying upcall | No published report (in\_progress) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41130552868) |
| [shuvendu-lahiri/litebox#54](https://github.com/shuvendu-lahiri/litebox/pull/54) | NFV audit \- change 1751: Support sched\_getscheduler and sched\_getparam | No published report (failure) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41130532806) |
| [shuvendu-lahiri/litebox#51](https://github.com/shuvendu-lahiri/litebox/pull/51) | NFV audit \- change 1760: Wait for runner helper threads to start before running the guest | No published report (failure) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/litebox/actions/runs/41130479576) |

## Conditional model refutations

The following property texts are extracted from the published reports, without new adjudication or inference. The original report contains assumptions, source overlays and native evidence.

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
