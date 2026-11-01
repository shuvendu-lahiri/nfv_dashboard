# Garnet NFV audit dashboard

Published results from the prototype [Neuro-Formal Verification](https://arxiv.org/abs/2608.21516) reviewer.
**Refutations are conditional MODEL refutations, not confirmed source bugs. Verification concerns translated models under stated assumptions; failure to refute is not evidence of correctness.**

**[Live interactive dashboard](https://shuvendu-lahiri.github.io/nfv_dashboard/garnet/)** / [all repositories](https://shuvendu-lahiri.github.io/nfv_dashboard/) or [download the standalone HTML](index.html) (no server or external dependencies).

Snapshot: 2026-11-01T19:09:51.708032+00:00. Latest published report per PR supplies the counts; all report links are retained in [data.json](data.json). Workflow attempts without a published report are not counted as zero findings.

**48 PRs attempted; 48 workflow attempts; 41 published reports; 5 PRs with 6 conditional refutations; 83 model verifications; 12 PRs without a published report.**

## All attempted PRs (refutations first)

| PR | Change | Latest report | Properties | Refuted | Verified | Exhausted | Audit failure | Evidence |
|---|---|---|---:|---:|---:|---:|---:|---|
| [shuvendu-lahiri/garnet#48](https://github.com/shuvendu-lahiri/garnet/pull/48) | [Source change 1860](https://redirect.github.com/microsoft/garnet/pull/1860) / Simplified latch\-free read cache design with eviction improvements | **REFUTED (model)** | 9 | **2** | 1 | 6 | 0 | [Report](https://github.com/shuvendu-lahiri/garnet/pull/48#issuecomment-6562421139) / [run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41336837326) |
| [shuvendu-lahiri/garnet#42](https://github.com/shuvendu-lahiri/garnet/pull/42) | [Source change 1919](https://redirect.github.com/microsoft/garnet/pull/1919) / Support INFO KEYSPACE command \(\#1668\) | **REFUTED (model)** | 8 | **1** | 3 | 4 | 0 | [Report](https://github.com/shuvendu-lahiri/garnet/pull/42#issuecomment-6561470963) / [run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41329613631) |
| [shuvendu-lahiri/garnet#34](https://github.com/shuvendu-lahiri/garnet/pull/34) | [Source change 2063](https://redirect.github.com/microsoft/garnet/pull/2063) / \[Tsavorite\] Scalable origin\-return buffer pool \+ direct\-VM native allocator | **REFUTED (model)** | 10 | **1** | 0 | 6 | 3 | [Report](https://github.com/shuvendu-lahiri/garnet/pull/34#issuecomment-6560093765) / [run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41319511957) |
| [shuvendu-lahiri/garnet#26](https://github.com/shuvendu-lahiri/garnet/pull/26) | [Source change 2268](https://redirect.github.com/microsoft/garnet/pull/2268) / Improve network connection handling | **REFUTED (model)** | 10 | **1** | 2 | 7 | 0 | [Report](https://github.com/shuvendu-lahiri/garnet/pull/26#issuecomment-6558794782) / [run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41310406324) |
| [shuvendu-lahiri/garnet#22](https://github.com/shuvendu-lahiri/garnet/pull/22) | [Source change 1335](https://redirect.github.com/microsoft/garnet/pull/1335) / Implement several HELP subcommands | **REFUTED (model)** | 10 | **1** | 7 | 2 | 0 | [Report](https://github.com/shuvendu-lahiri/garnet/pull/22#issuecomment-6558284211) / [run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41306762408) |
| [shuvendu-lahiri/garnet#47](https://github.com/shuvendu-lahiri/garnet/pull/47) | [Source change 1867](https://redirect.github.com/microsoft/garnet/pull/1867) / More IO optimizations | Published | 9 | 0 | 2 | 7 | 0 | [Report](https://github.com/shuvendu-lahiri/garnet/pull/47#issuecomment-6562342566) / [run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41336064482) |
| [shuvendu-lahiri/garnet#46](https://github.com/shuvendu-lahiri/garnet/pull/46) | [Source change 1879](https://redirect.github.com/microsoft/garnet/pull/1879) / Small corner case handling in storage | Published | 5 | 0 | 1 | 4 | 0 | [Report](https://github.com/shuvendu-lahiri/garnet/pull/46#issuecomment-6562050175) / [run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41335018223) |
| [shuvendu-lahiri/garnet#45](https://github.com/shuvendu-lahiri/garnet/pull/45) | [Source change 1884](https://redirect.github.com/microsoft/garnet/pull/1884) / Native storage device: improved error handling | Published | 10 | 0 | 2 | 8 | 0 | [Report](https://github.com/shuvendu-lahiri/garnet/pull/45#issuecomment-6561943190) / [run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41333320624) |
| [shuvendu-lahiri/garnet#44](https://github.com/shuvendu-lahiri/garnet/pull/44) | [Source change 1901](https://redirect.github.com/microsoft/garnet/pull/1901) / Improve store info stats, optimize vector IO | Published | 9 | 0 | 4 | 4 | 1 | [Report](https://github.com/shuvendu-lahiri/garnet/pull/44#issuecomment-6561808427) / [run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41332479451) |
| [shuvendu-lahiri/garnet#43](https://github.com/shuvendu-lahiri/garnet/pull/43) | [Source change 1903](https://redirect.github.com/microsoft/garnet/pull/1903) / Make alignment calculation consistent | Published | 10 | 0 | 5 | 5 | 0 | [Report](https://github.com/shuvendu-lahiri/garnet/pull/43#issuecomment-6561576485) / [run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41330420889) |
| [shuvendu-lahiri/garnet#41](https://github.com/shuvendu-lahiri/garnet/pull/41) | [Source change 1924](https://redirect.github.com/microsoft/garnet/pull/1924) / Update native storage device on Azure Linux docker container | Published | 7 | 0 | 4 | 0 | 3 | [Report](https://github.com/shuvendu-lahiri/garnet/pull/41#issuecomment-6561174231) / [run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41327805955) |
| [shuvendu-lahiri/garnet#40](https://github.com/shuvendu-lahiri/garnet/pull/40) | [Source change 1962](https://redirect.github.com/microsoft/garnet/pull/1962) / Fix LoadModuleCS parsing for module paths containing spaces \(\#1951\) | Published | 10 | 0 | 2 | 8 | 0 | [Report](https://github.com/shuvendu-lahiri/garnet/pull/40#issuecomment-6561070755) / [run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41327055085) |
| [shuvendu-lahiri/garnet#38](https://github.com/shuvendu-lahiri/garnet/pull/38) | [Source change 1980](https://redirect.github.com/microsoft/garnet/pull/1980) / Fix misaligned object\-log write of large overflow values | Published | 6 | 0 | 1 | 4 | 1 | [Report](https://github.com/shuvendu-lahiri/garnet/pull/38#issuecomment-6560833115) / [run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41324881276) |
| [shuvendu-lahiri/garnet#37](https://github.com/shuvendu-lahiri/garnet/pull/37) | [Source change 1984](https://redirect.github.com/microsoft/garnet/pull/1984) / Update docs, move purgebp to a debug subcommand | Published | 9 | 0 | 2 | 7 | 0 | [Report](https://github.com/shuvendu-lahiri/garnet/pull/37#issuecomment-6560532078) / [run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41322682763) |
| [shuvendu-lahiri/garnet#36](https://github.com/shuvendu-lahiri/garnet/pull/36) | [Source change 1989](https://redirect.github.com/microsoft/garnet/pull/1989) / Fix CI BDN allocation flakiness | Published | 10 | 0 | 0 | 10 | 0 | [Report](https://github.com/shuvendu-lahiri/garnet/pull/36#issuecomment-6560424840) / [run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41322333482) |
| [shuvendu-lahiri/garnet#33](https://github.com/shuvendu-lahiri/garnet/pull/33) | [Source change 2093](https://redirect.github.com/microsoft/garnet/pull/2093) / Fix silent pre\-listen hang and silent wrong\-recovery on \-\-recover \(\#2076\) | Published | 10 | 0 | 2 | 8 | 0 | [Report](https://github.com/shuvendu-lahiri/garnet/pull/33#issuecomment-6559998470) / [run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41318820506) |
| [shuvendu-lahiri/garnet#32](https://github.com/shuvendu-lahiri/garnet/pull/32) | [Source change 2095](https://redirect.github.com/microsoft/garnet/pull/2095) / Fix live\-object mutation and scan liveness defects \(\#2092\) | Published | 9 | 0 | 1 | 7 | 1 | [Report](https://github.com/shuvendu-lahiri/garnet/pull/32#issuecomment-6559705779) / [run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41317516432) |
| [shuvendu-lahiri/garnet#31](https://github.com/shuvendu-lahiri/garnet/pull/31) | [Source change 2110](https://redirect.github.com/microsoft/garnet/pull/2110) / Fix root causes behind recurring Garnet \.NET CI flakes | Published | 10 | 0 | 1 | 9 | 0 | [Report](https://github.com/shuvendu-lahiri/garnet/pull/31#issuecomment-6559600023) / [run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41316337819) |
| [shuvendu-lahiri/garnet#29](https://github.com/shuvendu-lahiri/garnet/pull/29) | [Source change 2159](https://redirect.github.com/microsoft/garnet/pull/2159) / \[Tsavorite\] Fix silent data loss when the hash index checkpoint exceeds the OS single\-request limit | Published | 10 | 0 | 0 | 9 | 1 | [Report](https://github.com/shuvendu-lahiri/garnet/pull/29#issuecomment-6559423932) / [run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41315164609) |
| [shuvendu-lahiri/garnet#27](https://github.com/shuvendu-lahiri/garnet/pull/27) | [Source change 2229](https://redirect.github.com/microsoft/garnet/pull/2229) / \[Tsavorite\] Account hash index memory in the log budget and bound overflow buckets | Published | 10 | 0 | 1 | 7 | 2 | [Report](https://github.com/shuvendu-lahiri/garnet/pull/27#issuecomment-6559114446) / [run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41312282197) |
| [shuvendu-lahiri/garnet#28](https://github.com/shuvendu-lahiri/garnet/pull/28) | [Source change 2172](https://redirect.github.com/microsoft/garnet/pull/2172) / \[Tsavorite\] Fix checkpoint abort abandoning in\-flight flushes and stale checkpoint selection on recovery | Published | 10 | 0 | 2 | 5 | 3 | [Report](https://github.com/shuvendu-lahiri/garnet/pull/28#issuecomment-6559100068) / [run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41313085388) |
| [shuvendu-lahiri/garnet#25](https://github.com/shuvendu-lahiri/garnet/pull/25) | [Source change 2285](https://redirect.github.com/microsoft/garnet/pull/2285) / Do not block in blocking commands run by EXEC or a script | Published | 10 | 0 | 2 | 8 | 0 | [Report](https://github.com/shuvendu-lahiri/garnet/pull/25#issuecomment-6558687175) / [run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41309586441) |
| [shuvendu-lahiri/garnet#23](https://github.com/shuvendu-lahiri/garnet/pull/23) | [Source change 1278](https://redirect.github.com/microsoft/garnet/pull/1278) / Implement the inline command format | Published | 10 | 0 | 2 | 8 | 0 | [Report](https://github.com/shuvendu-lahiri/garnet/pull/23#issuecomment-6558309245) / [run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41307003552) |
| [shuvendu-lahiri/garnet#20](https://github.com/shuvendu-lahiri/garnet/pull/20) | [Source change 1684](https://redirect.github.com/microsoft/garnet/pull/1684) / Replace PriorityQueue \+ Dictionary with IndexedPriorityQueue in Sorte… | Published | 10 | 0 | 2 | 7 | 1 | [Report](https://github.com/shuvendu-lahiri/garnet/pull/20#issuecomment-6557969568) / [run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41304257822) |
| [shuvendu-lahiri/garnet#21](https://github.com/shuvendu-lahiri/garnet/pull/21) | [Source change 1574](https://redirect.github.com/microsoft/garnet/pull/1574) / Amehlem/opentelemetry | Published | 10 | 0 | 6 | 4 | 0 | [Report](https://github.com/shuvendu-lahiri/garnet/pull/21#issuecomment-6557943522) / [run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41304496466) |
| [shuvendu-lahiri/garnet#19](https://github.com/shuvendu-lahiri/garnet/pull/19) | [Source change 1801](https://redirect.github.com/microsoft/garnet/pull/1801) / Implement CLIENT REPLY ON\|OFF\|SKIP \(\#1626\) | Published | 7 | 0 | 1 | 6 | 0 | [Report](https://github.com/shuvendu-lahiri/garnet/pull/19#issuecomment-6557631987) / [run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41302567248) |
| [shuvendu-lahiri/garnet#18](https://github.com/shuvendu-lahiri/garnet/pull/18) | [Source change 1825](https://redirect.github.com/microsoft/garnet/pull/1825) / Feature: graceful shutdown for v2 \( \#1382 \) | Published | 10 | 0 | 3 | 6 | 1 | [Report](https://github.com/shuvendu-lahiri/garnet/pull/18#issuecomment-6557595703) / [run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41301967979) |
| [shuvendu-lahiri/garnet#16](https://github.com/shuvendu-lahiri/garnet/pull/16) | [Source change 2090](https://redirect.github.com/microsoft/garnet/pull/2090) / Extend DUMP &amp; RESTORE to support object types \(\#1343\) | Published | 5 | 0 | 0 | 5 | 0 | [Report](https://github.com/shuvendu-lahiri/garnet/pull/16#issuecomment-6557372532) / [run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41300990688) |
| [shuvendu-lahiri/garnet#15](https://github.com/shuvendu-lahiri/garnet/pull/15) | [Source change 2168](https://redirect.github.com/microsoft/garnet/pull/2168) / Add COPY command | Published | 3 | 0 | 1 | 2 | 0 | [Report](https://github.com/shuvendu-lahiri/garnet/pull/15#issuecomment-6557189812) / [run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41299926102) |
| [shuvendu-lahiri/garnet#14](https://github.com/shuvendu-lahiri/garnet/pull/14) | [Source change 2226](https://redirect.github.com/microsoft/garnet/pull/2226) / Introduce and use \`UnsafeNullSessionLocker\` for Vector Set operations in a transaction | Published | 10 | 0 | 3 | 7 | 0 | [Report](https://github.com/shuvendu-lahiri/garnet/pull/14#issuecomment-6557166556) / [run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41298930644) |
| [shuvendu-lahiri/garnet#13](https://github.com/shuvendu-lahiri/garnet/pull/13) | [Source change 2236](https://redirect.github.com/microsoft/garnet/pull/2236) / Fix \`DBSIZE\`, \`INFO\`, \`KEYS\`, and \`SCAN\` deadlocks in transactions | Published | 10 | 0 | 5 | 5 | 0 | [Report](https://github.com/shuvendu-lahiri/garnet/pull/13#issuecomment-6557013599) / [run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41297999115) |
| [shuvendu-lahiri/garnet#12](https://github.com/shuvendu-lahiri/garnet/pull/12) | [Source change 2242](https://redirect.github.com/microsoft/garnet/pull/2242) / Fixes for expiration of \`RENAME\(NX\)\`'d keys in cluster | Published | 8 | 0 | 0 | 8 | 0 | [Report](https://github.com/shuvendu-lahiri/garnet/pull/12#issuecomment-6556890688) / [run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41297338522) |
| [shuvendu-lahiri/garnet#10](https://github.com/shuvendu-lahiri/garnet/pull/10) | [Source change 2251](https://redirect.github.com/microsoft/garnet/pull/2251) / Fix object\-log reads across segment boundaries | Published | 6 | 0 | 1 | 5 | 0 | [Report](https://github.com/shuvendu-lahiri/garnet/pull/10#issuecomment-6556757929) / [run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41296351755) |
| [shuvendu-lahiri/garnet#9](https://github.com/shuvendu-lahiri/garnet/pull/9) | [Source change 2278](https://redirect.github.com/microsoft/garnet/pull/2278) / \[Storage\] Preserve imported ETags through migration and replay | Published | 6 | 0 | 3 | 3 | 0 | [Report](https://github.com/shuvendu-lahiri/garnet/pull/9#issuecomment-6556572741) / [run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41294961223) |
| [shuvendu-lahiri/garnet#8](https://github.com/shuvendu-lahiri/garnet/pull/8) | [Source change 2287](https://redirect.github.com/microsoft/garnet/pull/2287) / Repro: replica replay loses AOF records after mid\-chunk commit metadata | Published | 7 | 0 | 2 | 5 | 0 | [Report](https://github.com/shuvendu-lahiri/garnet/pull/8#issuecomment-6556545349) / [run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41294752687) |
| [shuvendu-lahiri/garnet#2](https://github.com/shuvendu-lahiri/garnet/pull/2) | [Source change 2289](https://redirect.github.com/microsoft/garnet/pull/2289) / Fix RMW update parity, blocking\-pop race, log dispose, migration and AAD refresh bugs | Published | 10 | 0 | 4 | 6 | 0 | [Report](https://github.com/shuvendu-lahiri/garnet/pull/2#issuecomment-6555798591) / [run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41287466540) |
| [shuvendu-lahiri/garnet#7](https://github.com/shuvendu-lahiri/garnet/pull/7) | [Source change 2308](https://redirect.github.com/microsoft/garnet/pull/2308) / Return inf and \-inf for infinite scores in ZSCAN | Published | 2 | 0 | 0 | 2 | 0 | [Report](https://github.com/shuvendu-lahiri/garnet/pull/7#issuecomment-6556341462) / [run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41293904915) |
| [shuvendu-lahiri/garnet#6](https://github.com/shuvendu-lahiri/garnet/pull/6) | [Source change 2309](https://redirect.github.com/microsoft/garnet/pull/2309) / Honor exclusive infinite bounds in sorted set score ranges | Published | 1 | 0 | 1 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/garnet/pull/6#issuecomment-6556302519) / [run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41293683784) |
| [shuvendu-lahiri/garnet#5](https://github.com/shuvendu-lahiri/garnet/pull/5) | [Source change 2311](https://redirect.github.com/microsoft/garnet/pull/2311) / Fix DB selection in Lua scripts | Published | 2 | 0 | 0 | 2 | 0 | [Report](https://github.com/shuvendu-lahiri/garnet/pull/5#issuecomment-6556167690) / [run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41292825699) |
| [shuvendu-lahiri/garnet#4](https://github.com/shuvendu-lahiri/garnet/pull/4) | [Source change 2334](https://redirect.github.com/microsoft/garnet/pull/2334) / Configurable chunk size and pipelining for disk\-based replica sync | Published | 10 | 0 | 2 | 8 | 0 | [Report](https://github.com/shuvendu-lahiri/garnet/pull/4#issuecomment-6556144253) / [run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41291155843) |
| [shuvendu-lahiri/garnet#3](https://github.com/shuvendu-lahiri/garnet/pull/3) | [Source change 2262](https://redirect.github.com/microsoft/garnet/pull/2262) / Lua redis\.call fast paths: fix replies, stats and cluster routing; add HGET/HSET/EXPIRE; HashGet returns NOTFOUND \(breaking\) | Published | 10 | 0 | 2 | 4 | 4 | [Report](https://github.com/shuvendu-lahiri/garnet/pull/3#issuecomment-6556035034) / [run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41291155746) |
| [shuvendu-lahiri/garnet#54](https://github.com/shuvendu-lahiri/garnet/pull/54) | [Source change 1823](https://redirect.github.com/microsoft/garnet/pull/1823) / Add KV\.benchmark: lean Tsavorite KV throughput benchmark | No published report (not attempted) | - | - | - | - | - | - |
| [shuvendu-lahiri/garnet#53](https://github.com/shuvendu-lahiri/garnet/pull/53) | [Source change 1831](https://redirect.github.com/microsoft/garnet/pull/1831) / \[Tsavorite\] Add native Linux storage backend, harden NativeStorageDevice, refresh storage benchmarks | No published report (not attempted) | - | - | - | - | - | - |
| [shuvendu-lahiri/garnet#52](https://github.com/shuvendu-lahiri/garnet/pull/52) | [Source change 1834](https://redirect.github.com/microsoft/garnet/pull/1834) / v1 backport pr 1798 v1 | No published report (not attempted) | - | - | - | - | - | - |
| [shuvendu-lahiri/garnet#51](https://github.com/shuvendu-lahiri/garnet/pull/51) | [Source change 1837](https://redirect.github.com/microsoft/garnet/pull/1837) / Optimize IO paths in KV | No published report (not attempted) | - | - | - | - | - | - |
| [shuvendu-lahiri/garnet#50](https://github.com/shuvendu-lahiri/garnet/pull/50) | [Source change 1838](https://redirect.github.com/microsoft/garnet/pull/1838) / Fix AOF page/memory size defaults and validation \(\#1811\) | No published report (not attempted) | - | - | - | - | - | - |
| [shuvendu-lahiri/garnet#49](https://github.com/shuvendu-lahiri/garnet/pull/49) | [Source change 1854](https://redirect.github.com/microsoft/garnet/pull/1854) / More IO optimization | No published report (success) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41338873749) |
| [shuvendu-lahiri/garnet#39](https://github.com/shuvendu-lahiri/garnet/pull/39) | [Source change 1970](https://redirect.github.com/microsoft/garnet/pull/1970) / \[Docs\] Refresh unified\-store, auth/config, and API docs | No published report (failure) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41325764496) |
| [shuvendu-lahiri/garnet#35](https://github.com/shuvendu-lahiri/garnet/pull/35) | [Source change 2007](https://redirect.github.com/microsoft/garnet/pull/2007) / Reduce disk reads on the tiered Vector Set search path | No published report (failure) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41321657529) |
| [shuvendu-lahiri/garnet#30](https://github.com/shuvendu-lahiri/garnet/pull/30) | [Source change 2157](https://redirect.github.com/microsoft/garnet/pull/2157) / Bound per\-connection memory: adaptive network buffer budget, session buffer caps, and connection admission | No published report (failure) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41315247247) |
| [shuvendu-lahiri/garnet#24](https://github.com/shuvendu-lahiri/garnet/pull/24) | [Source change 2331](https://redirect.github.com/microsoft/garnet/pull/2331) / \[RESP\] Fix EXEC aborting when a queued SUBSCRIBE enters subscription mode | No published report (failure) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41309339657) |
| [shuvendu-lahiri/garnet#17](https://github.com/shuvendu-lahiri/garnet/pull/17) | [Source change 1875](https://redirect.github.com/microsoft/garnet/pull/1875) / Add server\-side RESP protocol restrictions | No published report (failure) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41301229318) |
| [shuvendu-lahiri/garnet#11](https://github.com/shuvendu-lahiri/garnet/pull/11) | [Source change 2247](https://redirect.github.com/microsoft/garnet/pull/2247) / Fix INT64\_MIN parsing for INCR and INCRBY | No published report (failure) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/garnet/actions/runs/41296578534) |

## Conditional model refutations

The following property texts are extracted from the published reports, without new adjudication or inference. The original report contains assumptions, source overlays and native evidence.

### shuvendu-lahiri/garnet#48 / P2

The entry returns normally\.

[Original report](https://github.com/shuvendu-lahiri/garnet/pull/48#issuecomment-6562421139)

### shuvendu-lahiri/garnet#48 / P5

For each key passed to ReadValueOrPending, the helper uses the immediate read status and output when the read is not pending; when it is pending, it waits for completion and replaces both with the single completed result\. It then requires the selected status to be Found and returns the corresponding selected output\.

[Original report](https://github.com/shuvendu-lahiri/garnet/pull/48#issuecomment-6562421139)

### shuvendu-lahiri/garnet#42 / P3

Database ID 0 returns normally\.

[Original report](https://github.com/shuvendu-lahiri/garnet/pull/42#issuecomment-6561470963)

### shuvendu-lahiri/garnet#34 / P10

Success exactly indicates that the mathematical reservation fits the budget\.

[Original report](https://github.com/shuvendu-lahiri/garnet/pull/34#issuecomment-6560093765)

### shuvendu-lahiri/garnet#26 / P10

Non\-timeout start failures make one error\-log call\.

[Original report](https://github.com/shuvendu-lahiri/garnet/pull/26#issuecomment-6558794782)

### shuvendu-lahiri/garnet#22 / P1

With remaining arguments, the result is false\.

[Original report](https://github.com/shuvendu-lahiri/garnet/pull/22#issuecomment-6558284211)

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
