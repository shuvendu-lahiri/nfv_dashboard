# Z3 NFV audit dashboard

Published results from the prototype [Neuro-Formal Verification](https://arxiv.org/abs/2608.21516) reviewer.
**Refutations are conditional MODEL refutations, not confirmed source bugs. Verification concerns translated models under stated assumptions; failure to refute is not evidence of correctness.**

**[Live interactive dashboard](https://shuvendu-lahiri.github.io/nfv_dashboard/z3/)** / [all repositories](https://shuvendu-lahiri.github.io/nfv_dashboard/) or [download the standalone HTML](index.html) (no server or external dependencies).

Snapshot: 2026-10-26T17:54:10.540224+00:00. Latest published report per PR supplies the counts; all report links are retained in [data.json](data.json). Workflow attempts without a published report are not counted as zero findings.

**41 PRs attempted; 117 workflow attempts; 40 published reports; 5 PRs with 5 conditional refutations; 90 model verifications; 1 PRs without a published report.**

## All attempted PRs (refutations first)

| PR | Change | Latest report | Properties | Refuted | Verified | Exhausted | Audit failure | Evidence |
|---|---|---|---:|---:|---:|---:|---:|---|
| [shuvendu-lahiri/z3#35](https://github.com/shuvendu-lahiri/z3/pull/35) | NFV replay Z3Prover/z3\#11123: fix\(seq\): respect known length lower bounds when minting fresh model values \(\#7664\) | **REFUTED (model)** | 2 | **1** | 1 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/z3/pull/35#issuecomment-6388194175) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39012427142) |
| [shuvendu-lahiri/z3#43](https://github.com/shuvendu-lahiri/z3/pull/43) | Staged NFV audit \- change 11237: Handle constant rows in implied\-equality proof checking | **REFUTED (model)** | 3 | **1** | 2 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/z3/pull/43#issuecomment-6386071462) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39532855682) |
| [shuvendu-lahiri/z3#40](https://github.com/shuvendu-lahiri/z3/pull/40) | Staged NFV audit \- change 11245: Check alldiff gate clauses natively and log root distinct as input | **REFUTED (model)** | 9 | **1** | 5 | 0 | 3 | [Report](https://github.com/shuvendu-lahiri/z3/pull/40#issuecomment-6385766326) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39532863673) |
| [shuvendu-lahiri/z3#41](https://github.com/shuvendu-lahiri/z3/pull/41) | Staged NFV audit \- change 11239: Check xor gate clauses in the native Tseitin proof checker | **REFUTED (model)** | 6 | **1** | 4 | 0 | 1 | [Report](https://github.com/shuvendu-lahiri/z3/pull/41#issuecomment-6385751609) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39532858434) |
| [shuvendu-lahiri/z3#29](https://github.com/shuvendu-lahiri/z3/pull/29) | NFV replay Z3Prover/z3\#11153: Bound finite\-field factor splitting per SMT search | **REFUTED (model)** | 5 | **1** | 2 | 0 | 2 | [Report](https://github.com/shuvendu-lahiri/z3/pull/29#issuecomment-6383789499) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39011193107) |
| [shuvendu-lahiri/z3#53](https://github.com/shuvendu-lahiri/z3/pull/53) | NFV audit \- change 11082: Make heuristic comparator ties deterministic | Published | 10 | 0 | 3 | 7 | 0 | [Report](https://github.com/shuvendu-lahiri/z3/pull/53#issuecomment-6413007979) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/40296592893) |
| [shuvendu-lahiri/z3#59](https://github.com/shuvendu-lahiri/z3/pull/59) | NFV audit \- change 11165: Avoid regex unfolding for provably out\-of\-range substring offsets | Published | 3 | 0 | 2 | 1 | 0 | [Report](https://github.com/shuvendu-lahiri/z3/pull/59#issuecomment-6412947395) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/40296700318) |
| [shuvendu-lahiri/z3#58](https://github.com/shuvendu-lahiri/z3/pull/58) | NFV audit \- change 11105: A few fixes | Published | 9 | 0 | 5 | 4 | 0 | [Report](https://github.com/shuvendu-lahiri/z3/pull/58#issuecomment-6412917346) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/40296683882) |
| [shuvendu-lahiri/z3#54](https://github.com/shuvendu-lahiri/z3/pull/54) | NFV audit \- change 11086: Fix invalid model for to\_fp\-from\-real zero sign \( change 7431\) | Published | 3 | 0 | 1 | 2 | 0 | [Report](https://github.com/shuvendu-lahiri/z3/pull/54#issuecomment-6412870103) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/40296613539) |
| [shuvendu-lahiri/z3#57](https://github.com/shuvendu-lahiri/z3/pull/57) | NFV audit \- change 11099: determinism: Use a fixed null ID in theory traces | Published | 1 | 0 | 0 | 1 | 0 | [Report](https://github.com/shuvendu-lahiri/z3/pull/57#issuecomment-6412850641) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/40296665905) |
| [shuvendu-lahiri/z3#50](https://github.com/shuvendu-lahiri/z3/pull/50) | NFV audit \- change 11051: recfun: require a strictly decreasing recursive call before unfolding a ground constructor argument | Published | 4 | 0 | 4 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/z3/pull/50#issuecomment-6412740549) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/40296533839) |
| [shuvendu-lahiri/z3#52](https://github.com/shuvendu-lahiri/z3/pull/52) | NFV audit \- change 11330: Preserve singleton cardinalities for array fields | Published | 7 | 0 | 5 | 2 | 0 | [Report](https://github.com/shuvendu-lahiri/z3/pull/52#issuecomment-6412569770) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/40296575400) |
| [shuvendu-lahiri/z3#55](https://github.com/shuvendu-lahiri/z3/pull/55) | NFV audit \- change 11087: \[code\-simplifier\] Simplify duplicated delay\-ineq normalization in theory\_lra | Published | 1 | 0 | 1 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/z3/pull/55#issuecomment-6412567597) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/40296631365) |
| [shuvendu-lahiri/z3#56](https://github.com/shuvendu-lahiri/z3/pull/56) | NFV audit \- change 11091: Keep symbolic regex ranges out of ground equivalence checks | Published | 2 | 0 | 1 | 0 | 1 | [Report](https://github.com/shuvendu-lahiri/z3/pull/56#issuecomment-6412499957) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/40296647633) |
| [shuvendu-lahiri/z3#51](https://github.com/shuvendu-lahiri/z3/pull/51) | NFV audit \- change 11079: Preserve normalization bridges for deferred arithmetic inequalities | Published | 1 | 0 | 0 | 1 | 0 | [Report](https://github.com/shuvendu-lahiri/z3/pull/51#issuecomment-6412444161) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/40296556162) |
| [shuvendu-lahiri/z3#30](https://github.com/shuvendu-lahiri/z3/pull/30) | NFV replay Z3Prover/z3\#11148: Document default error handler exit behavior and install non\-exit handler on JNI context creation | Published | 1 | 0 | 1 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/z3/pull/30#issuecomment-6389471193) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39011209640) |
| [shuvendu-lahiri/z3#36](https://github.com/shuvendu-lahiri/z3/pull/36) | NFV replay Z3Prover/z3\#11136: \[code\-simplifier\] Remove redundant match\_iff check in PR\_QUANT\_INTRO proof validation | Published | 4 | 0 | 2 | 2 | 0 | [Report](https://github.com/shuvendu-lahiri/z3/pull/36#issuecomment-6388738350) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39012568191) |
| [shuvendu-lahiri/z3#33](https://github.com/shuvendu-lahiri/z3/pull/33) | NFV replay Z3Prover/z3\#11117: params: parse unsigned API limits without depending on long | Published | 2 | 0 | 1 | 0 | 1 | [Report](https://github.com/shuvendu-lahiri/z3/pull/33#issuecomment-6388569772) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39012005732) |
| [shuvendu-lahiri/z3#31](https://github.com/shuvendu-lahiri/z3/pull/31) | NFV replay Z3Prover/z3\#11146: \[code\-simplifier\] Use existing match\_equiv helper instead of repeating its definition | Published | 3 | 0 | 1 | 2 | 0 | [Report](https://github.com/shuvendu-lahiri/z3/pull/31#issuecomment-6388553794) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39011222164) |
| [shuvendu-lahiri/z3#37](https://github.com/shuvendu-lahiri/z3/pull/37) | NFV replay Z3Prover/z3\#11130: root subst\. in stoi bug \(nseq\) | Published | 9 | 0 | 6 | 2 | 1 | [Report](https://github.com/shuvendu-lahiri/z3/pull/37#issuecomment-6388200584) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39012839420) |
| [shuvendu-lahiri/z3#49](https://github.com/shuvendu-lahiri/z3/pull/49) | Staged NFV audit \- change 11212: \[code\-simplifier\] Simplify CLI argument parsing in shell/main\.cpp | Published | 4 | 0 | 2 | 0 | 2 | [Report](https://github.com/shuvendu-lahiri/z3/pull/49#issuecomment-6386691606) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39532839650) |
| [shuvendu-lahiri/z3#48](https://github.com/shuvendu-lahiri/z3/pull/48) | Staged NFV audit \- change 11221: \[WIP\] Fix Spacer returning unsat on reachable error in Z3 | Published | 2 | 0 | 1 | 0 | 1 | [Report](https://github.com/shuvendu-lahiri/z3/pull/48#issuecomment-6386527964) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39532842941) |
| [shuvendu-lahiri/z3#47](https://github.com/shuvendu-lahiri/z3/pull/47) | Staged NFV audit \- change 11227: Prevent assertion in finite\-set union cardinality bounds | Published | 1 | 0 | 0 | 0 | 1 | [Report](https://github.com/shuvendu-lahiri/z3/pull/47#issuecomment-6386429605) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39532698130) |
| [shuvendu-lahiri/z3#46](https://github.com/shuvendu-lahiri/z3/pull/46) | Staged NFV audit \- change 11235: Fix macro\-induced solve\-eqs performance regression | Published | 1 | 0 | 1 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/z3/pull/46#issuecomment-6386350225) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39532848529) |
| [shuvendu-lahiri/z3#45](https://github.com/shuvendu-lahiri/z3/pull/45) | Staged NFV audit \- change 11233: Prevent variable capture in constant\-array/lambda equality rewriting | Published | 1 | 0 | 1 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/z3/pull/45#issuecomment-6386226460) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39532845507) |
| [shuvendu-lahiri/z3#44](https://github.com/shuvendu-lahiri/z3/pull/44) | Staged NFV audit \- change 11236: Reject malformed implied\-equality proof hints | Published | 3 | 0 | 2 | 0 | 1 | [Report](https://github.com/shuvendu-lahiri/z3/pull/44#issuecomment-6386095395) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39532851433) |
| [shuvendu-lahiri/z3#42](https://github.com/shuvendu-lahiri/z3/pull/42) | Staged NFV audit \- change 11241: Enable model completion during Spacer term\-graph projection | Published | 1 | 0 | 1 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/z3/pull/42#issuecomment-6385926056) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39532861238) |
| [shuvendu-lahiri/z3#39](https://github.com/shuvendu-lahiri/z3/pull/39) | NFV replay Z3Prover/z3\#11111: Fix unit detection in the SAT proof trimmer | Published | 1 | 0 | 0 | 0 | 1 | [Report](https://github.com/shuvendu-lahiri/z3/pull/39#issuecomment-6385232407) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39015881455) |
| [shuvendu-lahiri/z3#38](https://github.com/shuvendu-lahiri/z3/pull/38) | NFV replay Z3Prover/z3\#11114: smt: run MBQI after a theory gives up instead of answering unknown | Published | 3 | 0 | 3 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/z3/pull/38#issuecomment-6385217118) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39012980760) |
| [shuvendu-lahiri/z3#34](https://github.com/shuvendu-lahiri/z3/pull/34) | NFV replay Z3Prover/z3\#11128: wrong length evaluation in seq model \(nseq\) | Published | 1 | 0 | 1 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/z3/pull/34#issuecomment-6384331655) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39012414006) |
| [shuvendu-lahiri/z3#32](https://github.com/shuvendu-lahiri/z3/pull/32) | NFV replay Z3Prover/z3\#11166: Fix thread\-safety defects in parallel SMT reached via the qfbv fallback | Published | 9 | 0 | 9 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/z3/pull/32#issuecomment-6384221871) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39011236095) |
| [shuvendu-lahiri/z3#27](https://github.com/shuvendu-lahiri/z3/pull/27) | NFV replay Z3Prover/z3\#11160: Fix floating\-point rounding for extreme integer exponents | Published | 5 | 0 | 3 | 0 | 2 | [Report](https://github.com/shuvendu-lahiri/z3/pull/27#issuecomment-6383679732) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39011165580) |
| [shuvendu-lahiri/z3#26](https://github.com/shuvendu-lahiri/z3/pull/26) | NFV replay Z3Prover/z3\#11162: Avoid array\-theory give\-up for uninterpreted uses of lambdas | Published | 1 | 0 | 1 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/z3/pull/26#issuecomment-6383360848) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39011150890) |
| [shuvendu-lahiri/z3#25](https://github.com/shuvendu-lahiri/z3/pull/25) | NFV replay Z3Prover/z3\#11159: Correct RTN selection for real\-to\-float conversion | Published | 4 | 0 | 4 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/z3/pull/25#issuecomment-6383313246) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39010871224) |
| [shuvendu-lahiri/z3#24](https://github.com/shuvendu-lahiri/z3/pull/24) | NFV replay Z3Prover/z3\#11164: Fix MBQI returning \`unknown\` on array model values over uninterpreted sorts | Published | 1 | 0 | 1 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/z3/pull/24#issuecomment-6383232899) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39010856073) |
| [shuvendu-lahiri/z3#23](https://github.com/shuvendu-lahiri/z3/pull/23) | NFV replay Z3Prover/z3\#11165: Avoid regex unfolding for provably out\-of\-range substring offsets | Published | 4 | 0 | 2 | 0 | 2 | [Report](https://github.com/shuvendu-lahiri/z3/pull/23#issuecomment-6382921550) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39010841303) |
| [shuvendu-lahiri/z3#28](https://github.com/shuvendu-lahiri/z3/pull/28) | NFV replay Z3Prover/z3\#11161: Honor binary exponents in Z3Py FPVal | Published | 7 | 0 | 7 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/z3/pull/28#issuecomment-6382902190) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/39011178503) |
| [shuvendu-lahiri/z3#20](https://github.com/shuvendu-lahiri/z3/pull/20) | Port recursive\-function MBQI handling to SAT/SMT | Published | 5 | 0 | 3 | 0 | 2 | [Report](https://github.com/shuvendu-lahiri/z3/pull/20#issuecomment-6382555028) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/38965099587) |
| [shuvendu-lahiri/z3#22](https://github.com/shuvendu-lahiri/z3/pull/22) | Add exp/atan2 transcendental support to nla\_core | Published (older head) / latest attempt: cancelled | 10 | 0 | 1 | 0 | 9 | [Report](https://github.com/shuvendu-lahiri/z3/pull/22#issuecomment-6206551734) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/38837955521) / [latest attempt](https://github.com/shuvendu-lahiri/z3/actions/runs/38952644587) |
| [shuvendu-lahiri/z3#21](https://github.com/shuvendu-lahiri/z3/pull/21) | Fix false \`unsat\` for inexact symbolic Real\-to\-FloatingPoint rounding | Published (older head) / latest attempt: cancelled | 10 | 0 | 0 | 10 | 0 | [Report](https://github.com/shuvendu-lahiri/z3/pull/21#issuecomment-6206176939) / [run](https://github.com/shuvendu-lahiri/z3/actions/runs/38835819515) / [latest attempt](https://github.com/shuvendu-lahiri/z3/actions/runs/38952645412) |
| [shuvendu-lahiri/z3#19](https://github.com/shuvendu-lahiri/z3/pull/19) | Fix invalid model for to\_fp\-from\-real zero sign \(\#7431\) | No published report (success) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/z3/actions/runs/38483080218) |

## Conditional model refutations

The following property texts are extracted from the published reports, without new adjudication or inference. The original report contains assumptions, source overlays and native evidence.

### shuvendu-lahiri/z3#35 / P1

Under the complete padding guard, the returned string meets the known length lower bound\.

[Original report](https://github.com/shuvendu-lahiri/z3/pull/35#issuecomment-6388194175)

### shuvendu-lahiri/z3#43 / P3

Every created row uses a nonzero selected\-row pivot coefficient\.

[Original report](https://github.com/shuvendu-lahiri/z3/pull/43#issuecomment-6386071462)

### shuvendu-lahiri/z3#40 / P2

An accepted negated OR gate contains no unsupported disjunct kind\.

[Original report](https://github.com/shuvendu-lahiri/z3/pull/40#issuecomment-6385766326)

### shuvendu-lahiri/z3#41 / P1

Acceptance requires the first xor argument to be fixed when present\.

[Original report](https://github.com/shuvendu-lahiri/z3/pull/41#issuecomment-6385751609)

### shuvendu-lahiri/z3#29 / P1

A normally completed search initialization leaves the factor\-split clause counter at zero\.

[Original report](https://github.com/shuvendu-lahiri/z3/pull/29#issuecomment-6383789499)

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
