# Relation Atlas V2 public package manifest

Package version: `1.0.1`
Claim level: package index, not a proof artifact

The public package contains one 20-row base registry, 11 historical V2 supplement
artifact units, six June statement rows and one October statement row.
These units give the mixed aggregate 18, not a theorem count. The counts are independent:
the six extensions do not alter the frozen V2 supplement count.

## Human-readable artifacts

| Role | Artifact |
|---|---|
| Public index | `docs/atlas/README.md` |
| Executable boundary | `docs/atlas/EXECUTABLE_REPLAY_SCOPE.md` |
| Base registry | `docs/atlas/CF_THEOREM_TRANSFER_REGISTRY_V1.md` |
| Current registry index | `docs/atlas/CF_THEOREM_TRANSFER_REGISTRY_V2.md` |
| V2 count/readout record | `docs/atlas/CF_THEOREM_ATLAS_V2_READOUT.md` |
| Open questions and blocked transfers | `docs/atlas/CF_OPEN_PROBLEM_ATLAS_V2.md` |
| Finite edge classification | `docs/atlas/CF_LIKE_EDGE_WATCH_TRIAGE_V1.md` |
| Sun 3.5 scope note | `docs/atlas/SUN_3_5_SEPARATE_PAPER_STATUS_UPDATE.md` |

## Machine-readable artifacts

| Artifact | Public role |
|---|---|
| `data/relation_atlas/cf_theorem_transfer_registry_v1.json` | 20-row base registry |
| `data/relation_atlas/cf_theorem_transfer_registry_2026_06_extension.json` | Six paper-facing extension rows |
| `data/relation_atlas/cf_like_mobius_binomial_edge_scan_v1.json` | Historical bounded edge-scan summary and hits |
| `data/relation_atlas/cf_like_edge_watch_triage_v1.json` | Classification of eight watch rows |
| `data/relation_atlas/cf_opposite_side_candidates.json` | Guarded comparison metadata |
| `data/relation_atlas/source_cartier_prime_power_metadata_v1.json` | Fixed-modulus Cartier metadata |
| `data/relation_atlas/rowland_yassawi_fixed_modulus_theorem_certificates_v1.json` | Six received fixed-modulus certificate summaries |
| `data/relation_atlas/cf_theorem_transfer_registry_2026_10_extension.json` | One Smith statement and the current source-correction overlay |
| `data/relation_atlas/cf_theorem_atlas_v2_package_manifest.json` | Machine-readable package index |

## Record-count units

```yaml
base_registry_statement_count: 20
v2_base_supplement_count: 11
paper_facing_extension_count: 6
total_public_registry_extension_rows: 18
october_statement_rows: 1
finite_edge_input_watch_rows: 8
finite_edge_closed_known_metadata_rows: 8
finite_edge_new_theorem_edges: 0
```

Guardrails: the manifest is an index, finite matches are not proofs, fixed-
modulus certificates do not imply an all-primes theorem, and no atlas row is
promoted beyond its explicit claim class.


For the current Smith consequence, source errata, literal row-ID crosswalk,
and the limits of historical summary records, use the
[October addendum](CF_OCTOBER_2026_ADDENDUM.md).
