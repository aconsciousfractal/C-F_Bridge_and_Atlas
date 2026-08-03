# C/F theorem-transfer registry V2 index

Release: `v1.0.0`
Claim level: guarded registry index, not a proof artifact

The V2 index preserves the 20-row base registry and records 11 supplementary
metadata classes. A six-row paper-facing extension is counted separately.

```yaml
base_registry_statement_count: 20
v2_base_supplement_count: 11
paper_facing_extension_count: 6
total_public_registry_extension_rows: 17
finite_edge_input_watch_rows: 8
finite_edge_closed_known_metadata_rows: 8
finite_edge_new_theorem_edges: 0
ry_fixed_modulus_certificate_count: 6
ry_all_good_primes_status: open
```

## Supplement classes

| Supplement | Public claim class | Scope |
|---|---|---|
| Dwork C/F complement | `closed_metadata` | Constant-term complement only; no Newton equivalence. |
| Liu normalization | `closed_metadata` | Row-level convention map; no blanket theorem import. |
| Cooper and Franel automata | `explicit_automaton_metadata` | Explicit finite-state records. |
| C/F rational diagonals and small-modulus automata | `closed_metadata` | Fixed models/moduli only. |
| Source-Cartier alpha-2 records | `explicit_automaton_metadata` | Curated fixed-modulus records. |
| Rowland-Yassawi fixed-modulus certificates | theorem import by reference at fixed modulus | Six public certificates; no all-primes claim. |
| Straub derivative transport | `proof_obligation` | Low-carry identity is missing. |
| Finite edge classification | `closed_known_metadata` | Eight aliases/known inverse transforms; zero new theorem edges. |

## Paper-facing extension rows

The six extensions record Hankel invariance, Liu normalization, Franel source
clarification, the Dwork complement split, the exact `W2` arithmetic, and the
Chan-Cooper Lucas lane. Three are results proved in the paper and three are
closed metadata. None creates a new theorem-transfer edge.

The exact rows and counts live in
`data/relation_atlas/cf_theorem_transfer_registry_2026_06_extension.json`.
