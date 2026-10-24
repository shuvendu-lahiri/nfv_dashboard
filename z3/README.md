# Z3 NFV audit dashboard

Published results from the prototype [Neuro-Formal Verification](https://arxiv.org/abs/2608.21516) reviewer.
**Refutations are conditional MODEL refutations, not confirmed source bugs. Verification concerns translated models under stated assumptions; failure to refute is not evidence of correctness.**

**[Live interactive dashboard](https://shuvendu-lahiri.github.io/nfv_dashboard/z3/)** / [all repositories](https://shuvendu-lahiri.github.io/nfv_dashboard/) or [download the standalone HTML](index.html) (no server or external dependencies).

Snapshot: 2026-10-24T12:30:08.851094+00:00. Latest published report per PR supplies the counts; all report links are retained in [data.json](data.json). Workflow attempts without a published report are not counted as zero findings.

**31 PRs attempted; 86 workflow attempts; 26 published reports; 3 PRs with 3 conditional refutations; 43 model verifications; 5 PRs without a published report.**

## All attempted PRs (refutations first)

| PR | Change | Latest report | Properties | Refuted | Verified | Exhausted | Audit failure | Evidence |
|---|---|---|---:|---:|---:|---:|---:|---|
| [shuvendu-lahiri/z3#29](https://github.com/shuvendu-lahiri/z3/pull/29) | NFV replay Z3Prover/z3\#11153: Bound finite\-field factor splitting per SMT search | **REFUTED (model)** | 5 | **1** | 2 | 0 | 2 | [Report](https://github.com/shuvendu-lahiri/z3/pull/29#issuecomment-6383789499) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39011193107) |
| [shuvendu-lahiri/z3#41](https://github.com/shuvendu-lahiri/z3/pull/41) | Staged NFV audit \- change 11239: Check xor gate clauses in the native Tseitin proof checker | **REFUTED (model)** | 6 | **1** | 0 | 1 | 4 | [Report](https://github.com/shuvendu-lahiri/z3/pull/41#issuecomment-6306928614) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39532858434) |
| [shuvendu-lahiri/z3#35](https://github.com/shuvendu-lahiri/z3/pull/35) | NFV replay Z3Prover/z3\#11123: fix\(seq\): respect known length lower bounds when minting fresh model values \(\#7664\) | **REFUTED (model)** | 1 | **1** | 0 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/z3/pull/35#issuecomment-6231227079) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39012427142) |
| [shuvendu-lahiri/z3#32](https://github.com/shuvendu-lahiri/z3/pull/32) | NFV replay Z3Prover/z3\#11166: Fix thread\-safety defects in parallel SMT reached via the qfbv fallback | Published | 9 | 0 | 9 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/z3/pull/32#issuecomment-6384221871) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39011236095) |
| [shuvendu-lahiri/z3#27](https://github.com/shuvendu-lahiri/z3/pull/27) | NFV replay Z3Prover/z3\#11160: Fix floating\-point rounding for extreme integer exponents | Published | 5 | 0 | 3 | 0 | 2 | [Report](https://github.com/shuvendu-lahiri/z3/pull/27#issuecomment-6383679732) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39011165580) |
| [shuvendu-lahiri/z3#26](https://github.com/shuvendu-lahiri/z3/pull/26) | NFV replay Z3Prover/z3\#11162: Avoid array\-theory give\-up for uninterpreted uses of lambdas | Published | 1 | 0 | 1 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/z3/pull/26#issuecomment-6383360848) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39011150890) |
| [shuvendu-lahiri/z3#25](https://github.com/shuvendu-lahiri/z3/pull/25) | NFV replay Z3Prover/z3\#11159: Correct RTN selection for real\-to\-float conversion | Published | 4 | 0 | 4 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/z3/pull/25#issuecomment-6383313246) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39010871224) |
| [shuvendu-lahiri/z3#24](https://github.com/shuvendu-lahiri/z3/pull/24) | NFV replay Z3Prover/z3\#11164: Fix MBQI returning \`unknown\` on array model values over uninterpreted sorts | Published | 1 | 0 | 1 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/z3/pull/24#issuecomment-6383232899) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39010856073) |
| [shuvendu-lahiri/z3#23](https://github.com/shuvendu-lahiri/z3/pull/23) | NFV replay Z3Prover/z3\#11165: Avoid regex unfolding for provably out\-of\-range substring offsets | Published | 4 | 0 | 2 | 0 | 2 | [Report](https://github.com/shuvendu-lahiri/z3/pull/23#issuecomment-6382921550) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39010841303) |
| [shuvendu-lahiri/z3#28](https://github.com/shuvendu-lahiri/z3/pull/28) | NFV replay Z3Prover/z3\#11161: Honor binary exponents in Z3Py FPVal | Published | 7 | 0 | 7 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/z3/pull/28#issuecomment-6382902190) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39011178503) |
| [shuvendu-lahiri/z3#20](https://github.com/shuvendu-lahiri/z3/pull/20) | Port recursive\-function MBQI handling to SAT/SMT | Published | 5 | 0 | 3 | 0 | 2 | [Report](https://github.com/shuvendu-lahiri/z3/pull/20#issuecomment-6382555028) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/38965099587) |
| [shuvendu-lahiri/z3#40](https://github.com/shuvendu-lahiri/z3/pull/40) | Staged NFV audit \- change 11245: Check alldiff gate clauses natively and log root distinct as input | Published | 10 | 0 | 1 | 3 | 6 | [Report](https://github.com/shuvendu-lahiri/z3/pull/40#issuecomment-6307102053) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39532863673) |
| [shuvendu-lahiri/z3#44](https://github.com/shuvendu-lahiri/z3/pull/44) | Staged NFV audit \- change 11236: Reject malformed implied\-equality proof hints | Published | 6 | 0 | 3 | 1 | 2 | [Report](https://github.com/shuvendu-lahiri/z3/pull/44#issuecomment-6307041366) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39532851433) |
| [shuvendu-lahiri/z3#42](https://github.com/shuvendu-lahiri/z3/pull/42) | Staged NFV audit \- change 11241: Enable model completion during Spacer term\-graph projection | Published | 1 | 0 | 0 | 0 | 1 | [Report](https://github.com/shuvendu-lahiri/z3/pull/42#issuecomment-6306904677) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39532861238) |
| [shuvendu-lahiri/z3#46](https://github.com/shuvendu-lahiri/z3/pull/46) | Staged NFV audit \- change 11235: Fix macro\-induced solve\-eqs performance regression | Published | 1 | 0 | 0 | 0 | 1 | [Report](https://github.com/shuvendu-lahiri/z3/pull/46#issuecomment-6306893713) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39532848529) |
| [shuvendu-lahiri/z3#48](https://github.com/shuvendu-lahiri/z3/pull/48) | Staged NFV audit \- change 11221: \[WIP\] Fix Spacer returning unsat on reachable error in Z3 | Published | 4 | 0 | 1 | 2 | 1 | [Report](https://github.com/shuvendu-lahiri/z3/pull/48#issuecomment-6306883806) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39532842941) |
| [shuvendu-lahiri/z3#43](https://github.com/shuvendu-lahiri/z3/pull/43) | Staged NFV audit \- change 11237: Handle constant rows in implied\-equality proof checking | Published | 4 | 0 | 0 | 1 | 3 | [Report](https://github.com/shuvendu-lahiri/z3/pull/43#issuecomment-6306868942) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39532855682) |
| [shuvendu-lahiri/z3#45](https://github.com/shuvendu-lahiri/z3/pull/45) | Staged NFV audit \- change 11233: Prevent variable capture in constant\-array/lambda equality rewriting | Published | 1 | 0 | 0 | 1 | 0 | [Report](https://github.com/shuvendu-lahiri/z3/pull/45#issuecomment-6306858304) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39532845507) |
| [shuvendu-lahiri/z3#49](https://github.com/shuvendu-lahiri/z3/pull/49) | Staged NFV audit \- change 11212: \[code\-simplifier\] Simplify CLI argument parsing in shell/main\.cpp | Published | 5 | 0 | 0 | 0 | 5 | [Report](https://github.com/shuvendu-lahiri/z3/pull/49#issuecomment-6306757255) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39532839650) |
| [shuvendu-lahiri/z3#47](https://github.com/shuvendu-lahiri/z3/pull/47) | Staged NFV audit \- change 11227: Prevent assertion in finite\-set union cardinality bounds | Published | 2 | 0 | 1 | 0 | 1 | [Report](https://github.com/shuvendu-lahiri/z3/pull/47#issuecomment-6306596567) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39532698130) |
| [shuvendu-lahiri/z3#39](https://github.com/shuvendu-lahiri/z3/pull/39) | NFV replay Z3Prover/z3\#11111: Fix unit detection in the SAT proof trimmer | Published | 2 | 0 | 0 | 0 | 2 | [Report](https://github.com/shuvendu-lahiri/z3/pull/39#issuecomment-6231676360) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39015881455) |
| [shuvendu-lahiri/z3#38](https://github.com/shuvendu-lahiri/z3/pull/38) | NFV replay Z3Prover/z3\#11114: smt: run MBQI after a theory gives up instead of answering unknown | Published | 3 | 0 | 2 | 1 | 0 | [Report](https://github.com/shuvendu-lahiri/z3/pull/38#issuecomment-6231379994) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39012980760) |
| [shuvendu-lahiri/z3#34](https://github.com/shuvendu-lahiri/z3/pull/34) | NFV replay Z3Prover/z3\#11128: wrong length evaluation in seq model \(nseq\) | Published | 1 | 0 | 1 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/z3/pull/34#issuecomment-6231186119) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39012414006) |
| [shuvendu-lahiri/z3#33](https://github.com/shuvendu-lahiri/z3/pull/33) | NFV replay Z3Prover/z3\#11117: params: parse unsigned API limits without depending on long | Published / latest attempt: failure | 1 | 0 | 1 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/z3/pull/33#issuecomment-6231170012) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39012005732) / [latest attempt](https://github.com/shuvendu-lahiri/z3/actions/runs/39012005732) |
| [shuvendu-lahiri/z3#22](https://github.com/shuvendu-lahiri/z3/pull/22) | Add exp/atan2 transcendental support to nla\_core | Published (older head) / latest attempt: cancelled | 10 | 0 | 1 | 0 | 9 | [Report](https://github.com/shuvendu-lahiri/z3/pull/22#issuecomment-6206551734) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/38837955521) / [latest attempt](https://github.com/shuvendu-lahiri/z3/actions/runs/38952644587) |
| [shuvendu-lahiri/z3#21](https://github.com/shuvendu-lahiri/z3/pull/21) | Fix false \`unsat\` for inexact symbolic Real\-to\-FloatingPoint rounding | Published (older head) / latest attempt: cancelled | 10 | 0 | 0 | 10 | 0 | [Report](https://github.com/shuvendu-lahiri/z3/pull/21#issuecomment-6206176939) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/38835819515) / [latest attempt](https://github.com/shuvendu-lahiri/z3/actions/runs/38952645412) |
| [shuvendu-lahiri/z3#37](https://github.com/shuvendu-lahiri/z3/pull/37) | NFV replay Z3Prover/z3\#11130: root subst\. in stoi bug \(nseq\) | No published report (failure) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/z3/actions/runs/39012839420) |
| [shuvendu-lahiri/z3#36](https://github.com/shuvendu-lahiri/z3/pull/36) | NFV replay Z3Prover/z3\#11136: \[code\-simplifier\] Remove redundant match\_iff check in PR\_QUANT\_INTRO proof validation | No published report (failure) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/z3/actions/runs/39012568191) |
| [shuvendu-lahiri/z3#31](https://github.com/shuvendu-lahiri/z3/pull/31) | NFV replay Z3Prover/z3\#11146: \[code\-simplifier\] Use existing match\_equiv helper instead of repeating its definition | No published report (failure) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/z3/actions/runs/39011222164) |
| [shuvendu-lahiri/z3#30](https://github.com/shuvendu-lahiri/z3/pull/30) | NFV replay Z3Prover/z3\#11148: Document default error handler exit behavior and install non\-exit handler on JNI context creation | No published report (failure) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/z3/actions/runs/39011209640) |
| [shuvendu-lahiri/z3#19](https://github.com/shuvendu-lahiri/z3/pull/19) | Fix invalid model for to\_fp\-from\-real zero sign \(\#7431\) | No published report (success) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/z3/actions/runs/38483080218) |

## Conditional model refutations

The following property texts are extracted from the published reports, without new adjudication or inference. The original report contains assumptions, source overlays and native evidence.

### shuvendu-lahiri/z3#29 / P1

A normally completed search initialization leaves the factor\-split clause counter at zero\.

[Original report](https://github.com/shuvendu-lahiri/z3/pull/29#issuecomment-6383789499)

### shuvendu-lahiri/z3#41 / P3

When the process exit handler runs during an active replay, with g\_captured referring to the replay's captured stream, it reports that replay ended prematurely together with the captured output and terminates with failure status 1; when no replay is active, it returns without forcing failure\.

[Original report](https://github.com/shuvendu-lahiri/z3/pull/41#issuecomment-6306928614)

### shuvendu-lahiri/z3#35 / P1

When the unresolved\-sequence fallback obtains a concrete fresh string and the original term has a reported positive unsigned length lower bound no greater than 65,536, a fresh string shorter than that bound is returned with its original content preserved and enough trailing 'a' characters added to reach the bound\. If the bound is absent, nonpositive, non\-unsigned, above 65,536, or already met by the fresh string, this padding step leaves the fresh value unchanged\.

[Original report](https://github.com/shuvendu-lahiri/z3/pull/35#issuecomment-6231227079)

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
