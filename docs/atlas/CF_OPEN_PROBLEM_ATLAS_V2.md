# C/F Open Problem Atlas V2

**Date:** 2026-05-06
**Roadmap:** `ROADMAP_V4.md`, Phase 8 + RY-31 sync
**Status:** V2 package/readout synchronization with RY Level 2b blocker recorded
**Claim level:** open problems and proof obligations, not theorem proofs

This V2 atlas is the Phase 8 status layer over
`CF_OPEN_PROBLEM_ATLAS_V1.md`. It records the V4 closures and leaves only
genuine blockers as active problems.

## Summary

```yaml
base_problem_count: 8
v2_added_problem_count: 1
closed_or_metadata_reconciled_in_v4:
  - OP-CF-005
  - OP-CF-006
  - OP-CF-007
partially_closed_with_open_subproblem:
  - OP-CF-004
active_or_blocked_problem_count_at_v2_freeze: 6
post_sun_3_5_active_or_blocked_problem_count: 4
phase7_watch_rows_remaining: 0
```

## Active / Blocked Problems And Post-Freeze Updates

| problem | status | blocking issue | next action |
| --- | --- | --- | --- |
| `OP-CF-001` Sun 3.5 raw-C to RV-108 bridge | addressed in companion Sun 3.5 paper after V2 freeze | Franel--Domb raw-C/RV bridge outside the C/F atlas | cite the separate Sun 3.5 paper; do not reclassify as a C/F consequence |
| `OP-CF-002` A2b global BM-core glue | addressed in companion Sun 3.5 paper after V2 freeze | Domb branch-multiplier identity outside the C/F atlas | cite the separate Sun 3.5 paper; retain V2 row as provenance |
| `OP-CF-003` BTY weight-1 `chi(w_d)` rows | open | missing row-specific Atkin-Lehner multipliers | extract/evaluate `chi(w_d)` table |
| `OP-CF-004b` Dwork complement vs Gorodetsky `Q_F` equivalence | open | no controlled mutation/birational equivalence yet | invariant audit before any search |
| `OP-CF-008` Straub derivative transport | blocked proof obligation | `HYP-LOW-CARRY-ID` | only reopen under bounded WZ/adjoint proof plan |
| `OP-CF-009` Rowland-Yassawi Level 2b all-good-primes/all-alpha import | open infrastructure theorem-certificate target | no all-good-primes filter/spec yet | RY-32 Level 2b spec, then RY-33 direct R/Q filter |

## Closed / Reconciled Problems

| problem | V2 status | evidence |
| --- | --- | --- |
| `OP-CF-004a` CT-operation realization of C/F | closed metadata | `Lambda_C1 -> 9-Lambda_C1` and rational diagonal contracts |
| `OP-CF-005` Rowland-Yassawi automaton pilot | closed as explicit automaton metadata | Cooper, Franel, C/F mod 2/mod 3, C/F mod 4/mod 9 bounded targets, and source-Cartier alpha=2 fixed-modulus metadata |
| `OP-CF-006` new C/F-like Mobius-binomial edges | closed for V1 watch set | Phase 7 triaged all 8 watch rows as known metadata |
| `OP-CF-007` Liu table-convention resolution | closed as convention-mapped metadata | eta/s18 source-normalization audit and repaired profile |

## OP-CF-006 Phase 7 Closeout

```yaml
input_watch_rows: 8
closed_known_metadata_rows: 8
still_watch_rows: 0
new_proof_obligations: 0
new_theorem_edges: 0
```

The V1 watch set does not require registry promotion. Six rows are the
`apery_zeta3`/`az_gamma` catalog alias identity under the inert transform
`a=0, s=1`. Two rows are inverse Franel transforms already recorded in the
Franel transform trace.

## Guardrails

- Future C/F-like scans require explicit authorization and bounded parameters.
- Coefficient matches alone remain non-promotional.
- Closed metadata rows are not internal proofs unless separately marked.
- The Rowland-Yassawi fixed-modulus Level 2a layer is active for selected
  Cooper and C/F rows.
- The Rowland-Yassawi all-good-primes/all-alpha Level 2b layer remains open.
- Source-Cartier alpha=2 public product exposure remains deferred.
- The Sun 3.5 rows are retained as V2 provenance but are addressed in the\n  companion Franel-Domb Sun 3.5 paper, not by this C/F atlas.

## Next Action

Use this V2 atlas for Paper B and package readouts. The next Rowland-Yassawi
work should be theorem-certificate infrastructure, not discovery: Level 2b
specification, then direct `R/Q` all-good-primes filter.
