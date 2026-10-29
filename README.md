# NFV audit dashboards

**[Open the dashboard hub](https://shuvendu-lahiri.github.io/nfv_dashboard/)**

| Repository | Live dashboard | GitHub-readable index |
|---|---|---|
| Z3 | [Open](https://shuvendu-lahiri.github.io/nfv_dashboard/z3/) | [Reports](z3/README.md) |
| LiteBox | [Open](https://shuvendu-lahiri.github.io/nfv_dashboard/litebox/) | [Reports](litebox/README.md) |
| NVX | [Open](https://shuvendu-lahiri.github.io/nfv_dashboard/nvx/) | [Reports](nvx/README.md) |

Published results from the prototype [Neuro-Formal Verification
reviewer](https://arxiv.org/abs/2608.21516). Refutations are **conditional MODEL
refutations, not confirmed source bugs**. Verification concerns translated models
under their stated assumptions; failure to refute is not evidence of correctness.

Latest published reports supply the counts. Earlier reports remain in each
repository's `data.json`. Failed or missing publication is shown explicitly, not
as a successful zero-finding analysis. NVX retains its recorded campaign cohorts
and source-change links; Z3 and LiteBox include all non-skipped reviewer attempts.

## Refresh

Requires Python 3.10+ and authenticated GitHub CLI read access:

```text
python refresh.py
python -m unittest discover
python refresh.py --check
```

Refresh reads only PR metadata, published comments and workflow metadata. It never
checks out or executes inspected PR code, starts audits, reruns proofs or changes
proof acceptance. Reused historical branches are disambiguated with captured head
SHAs and PR lifetimes; ambiguous associations and malformed report counts fail
explicitly. Current and legacy numbered property headings are supported without
relabeling their property identifiers.

These are public static snapshots, not private or access-controlled pages. No
automatic refresh or audit schedule is installed. To publish a refreshed snapshot,
commit and push the generated files to the `nfv-reports` branch.

GitHub Pages serves this branch from its root. `.nojekyll` prevents source
processing; the site needs no external scripts, assets or runtime dependencies.
