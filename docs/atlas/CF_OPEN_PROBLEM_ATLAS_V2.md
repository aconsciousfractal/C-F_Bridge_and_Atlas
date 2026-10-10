# C/F open questions and scope boundaries

Package version: `1.0.1`
Claim level: open questions and proof obligations, not theorem proofs

This record separates unresolved mathematical conditions from results already
proved in the paper or classified as metadata.

## Open or blocked rows

| ID | Public status | Missing mathematical condition |
|---|---|---|
| `OP-CF-003` | open | Row-specific Atkin-Lehner multipliers `chi(w_d)` for the BTY weight-1 rows are not derived. |
| `OP-CF-004b` | open | No controlled mutation or birational equivalence between the Dwork complement and the Gorodetsky `Q_F` model is proved. |
| `OP-CF-008` | blocked proof obligation | The Straub derivative transfer lacks the low-carry identity `HYP-LOW-CARRY-ID`. |
| `OP-CF-009` | open | Complete model/state certificate payloads are not included; Q(0) must be a unit for each explicit rational diagonal. |

## Resolved or separately scoped rows

| ID | Status | Public evidence |
|---|---|---|
| `OP-CF-001`, `OP-CF-002` | addressed outside this paper | The separate Sun supercongruence manuscript reports a proof; its proof is not certified by this Atlas. |
| `OP-CF-004a` | closed metadata | Constant-term complement `Lambda_C1 -> 9-Lambda_C1`; no mutation claim. |
| `OP-CF-005` | closed metadata | Explicit bounded automaton and fixed-modulus records. |
| `OP-CF-006` | closed metadata | All eight coefficient-match watch rows classify as aliases or known inverse Franel transforms. |
| `OP-CF-007` | closed metadata | Liu normalization is reconciled row by row; no unqualified 15/15 transfer is claimed. |

## Finite edge-classification summary

```yaml
input_watch_rows: 8
closed_known_metadata_rows: 8
still_watch_rows: 0
new_proof_obligations: 0
new_theorem_edges: 0
```

Coefficient matches alone are non-promotional. Source theorems retain their
original hypotheses, and unresolved comparison rows remain explicitly open or
blocked.


For the current Smith consequence, source errata, literal row-ID crosswalk,
and the limits of historical summary records, use the
[October addendum](CF_OCTOBER_2026_ADDENDUM.md).
