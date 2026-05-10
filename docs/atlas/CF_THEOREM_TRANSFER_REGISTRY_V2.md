# C/F Theorem-Transfer Registry V2

**Date:** 2026-05-06
**Roadmap:** `ROADMAP_V4.md`, Phase 8 + RY-31 sync
**Status:** V2 package/readout synchronization with RY fixed-modulus theorem-certificate overlay
**Claim level:** guarded theorem-transfer registry index, not a proof artifact

This V2 registry does not replace the V1 theorem-transfer registry row by row.
It treats V1 as the stable base and records the V4 supplemental metadata
closures that changed claim class, blocker status, or package status.

Base registry:

```text
docs/05_relation_atlas/01_registry/CF_THEOREM_TRANSFER_REGISTRY_V1.md
data/relation_atlas/cf_theorem_transfer_registry_v1.json
```

## Summary

```yaml
base_registry_version: cf_theorem_transfer_registry.v1
base_statement_count: 20
base_watch_count: 0
v2_supplement_count: 11
new_theorem_transfer_edges_promoted_in_phase7: 0
phase7_watch_rows_reclassified: 8
phase7_reclassification: closed_known_metadata
phase8_package_status: complete
ry_level2a_fixed_modulus_certificate_count: 6
ry_level2b_all_good_primes_status: open
```

## V2 Supplemental Artifacts

| supplement | artifact | claim level | status |
| --- | --- | --- | --- |
| Dwork C/F complement model | `docs/05_relation_atlas/05_v2_metadata/RELATION_ATLAS_V2_DWORK_CF_COMPLEMENT_MODEL.md` | theorem import by reference metadata | metadata ready by reference |
| Liu convention repair | `docs/05_relation_atlas/05_v2_metadata/RELATION_ATLAS_V2_LIU_CONVENTION_REPAIRED_METADATA.md` | convention-mapped theorem metadata | closed metadata |
| Cooper s7 automata | `docs/05_relation_atlas/05_v2_metadata/RELATION_ATLAS_V2_COOPER_S7_AUTOMATON_METADATA.md` | explicit finite automaton metadata | closed metadata |
| Franel automata | `docs/05_relation_atlas/05_v2_metadata/RELATION_ATLAS_V2_FRANEL_AUTOMATON_METADATA.md` | Lucas/binomial automaton metadata | closed metadata |
| C/F rational diagonal contracts | `docs/05_relation_atlas/05_v2_metadata/RELATION_ATLAS_V2_CF_DIAGONAL_CONTRACT_METADATA.md` | rational diagonal contract metadata | closed metadata |
| C/F mod 2 and mod 3 automata | `docs/05_relation_atlas/05_v2_metadata/RELATION_ATLAS_V2_CF_AUTOMATON_METADATA.md` | explicit automaton metadata | closed metadata |
| C/F mod 4 and mod 9 prime-power automata | `docs/05_relation_atlas/05_v2_metadata/RELATION_ATLAS_V2_CF_PRIME_POWER_AUTOMATON_METADATA.md` | explicit prime-power automaton metadata | closed metadata |
| Source-Cartier alpha=2 artifacts | `docs/05_relation_atlas/05_v2_metadata/RELATION_ATLAS_V2_SOURCE_CARTIER_PRIME_POWER_METADATA.md` | explicit prime-power automaton metadata | closed metadata, internal only |
| Rowland-Yassawi fixed-modulus theorem certificates | `docs/05_relation_atlas/05_v2_metadata/RELATION_ATLAS_V2_RY_FIXED_MODULUS_THEOREM_CERTIFICATES.md` | theorem import by reference at fixed modulus | closed Level 2a metadata |
| Straub derivative transport artifact | `docs/05_relation_atlas/05_v2_metadata/RELATION_ATLAS_V2_GESSEL_LUCAS_DERIVATIVE_METADATA_2026-04-30.md` | proof-obligation metadata | blocked by `HYP-LOW-CARRY-ID` |
| Phase 7 edge watch triage | `docs/05_relation_atlas/04_edge_scan/CF_LIKE_EDGE_WATCH_TRIAGE_V1.md` | triage metadata | closed known metadata |

## Phase 7 Registry Impact

```yaml
input_watch_rows: 8
closed_known_metadata_rows: 8
new_proof_obligations: 0
new_theorem_edges: 0
bounded_negative_rows: 0
still_watch_rows: 0
```

The six `apery_zeta3`/`az_gamma` watch rows are canonical alias identities
under the inert transform `a=0, s=1`. The two C/F-to-Franel watch rows are
known inverse Franel transform metadata. None is promoted as a new theorem
transfer.

## Guardrails

- V2 does not upgrade finite replay to theorem proof.
- V2 declares only fixed-modulus Rowland-Yassawi Level 2a theorem certificates.
- V2 does not declare all-good-primes/all-alpha Rowland-Yassawi Level 2b.
- V2 treats public source-Cartier alpha=2 product exposure as deferred.
- V2 does not treat Dwork metadata as an active C/F theorem transfer.
- V2 does not create new C/F-like edges from the Phase 7 watch rows.
- V2 keeps `HYP-LOW-CARRY-ID` as the Straub derivative-transfer blocker.

## Next Action

Use this V2 registry as the Paper B source index. The next Rowland-Yassawi
registry task is not another fixed-modulus row; it is the Level 2b
all-good-primes/all-alpha certificate specification and prime-filter split.
