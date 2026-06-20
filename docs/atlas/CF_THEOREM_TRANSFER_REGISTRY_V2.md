# C/F Theorem-Transfer Registry V2

**Date:** 2026-05-06
**Public package update:** 2026-05-10
**Roadmap lineage:** Phase 8 + RY-31 sync
**Status:** V2 package/readout synchronization with RY fixed-modulus theorem-certificate overlay
**Claim level:** guarded theorem-transfer registry index, not a proof artifact

This V2 registry does not replace the V1 theorem-transfer registry row by row.
It treats V1 as the stable base and records the supplemental metadata closures
that changed claim class, blocker status, or package status.  All paths in this
public edition point to artifacts included in this repository.

Base registry:

```text
docs/atlas/CF_THEOREM_TRANSFER_REGISTRY_V1.md
data/relation_atlas/cf_theorem_transfer_registry_v1.json
data/relation_atlas/cf_theorem_transfer_registry_2026_06_extension.json
```

## Summary

```yaml
base_registry_version: cf_theorem_transfer_registry.v1
base_statement_count: 20
base_watch_count: 0
v2_supplement_count: 11
v2_base_supplement_count: 11
extension_2026_06_20_count: 6
total_public_registry_extension_rows: 17
new_theorem_transfer_edges_promoted_in_phase7: 0
phase7_watch_rows_reclassified: 8
phase7_reclassification: closed_known_metadata
phase8_package_status: complete
ry_level2a_fixed_modulus_certificate_count: 6
ry_level2b_all_good_primes_status: open
```

## V2 Supplemental Coverage

| supplement class | public artifact | claim level | status |
| --- | --- | --- | --- |
| Dwork C/F complement model | `docs/atlas/CF_THEOREM_ATLAS_V2_READOUT.md` | theorem import by reference metadata | metadata ready by reference |
| Liu convention repair | `docs/atlas/CF_THEOREM_ATLAS_V2_READOUT.md` | convention-mapped theorem metadata | closed metadata |
| Cooper s7 automata | `docs/atlas/CF_THEOREM_ATLAS_V2_READOUT.md` | explicit finite automaton metadata | closed metadata |
| Franel automata | `docs/atlas/CF_THEOREM_ATLAS_V2_READOUT.md` | Lucas/binomial automaton metadata | closed metadata |
| C/F rational diagonal contracts | `docs/atlas/CF_THEOREM_ATLAS_V2_READOUT.md` | rational diagonal contract metadata | closed metadata |
| C/F mod 2 and mod 3 automata | `docs/atlas/CF_THEOREM_ATLAS_V2_READOUT.md` | explicit automaton metadata | closed metadata |
| C/F mod 4 and mod 9 prime-power automata | `docs/atlas/CF_THEOREM_ATLAS_V2_READOUT.md` | explicit prime-power automaton metadata | closed metadata |
| Source-Cartier alpha=2 artifacts | `data/relation_atlas/source_cartier_prime_power_metadata_v1.json` | explicit prime-power automaton metadata | closed metadata, public companion data |
| Rowland-Yassawi fixed-modulus theorem certificates | `data/relation_atlas/rowland_yassawi_fixed_modulus_theorem_certificates_v1.json` | theorem import by reference at fixed modulus | closed Level 2a metadata |
| Straub derivative transport artifact | `docs/atlas/CF_OPEN_PROBLEM_ATLAS_V2.md` | proof-obligation metadata | blocked by `HYP-LOW-CARRY-ID` |
| Phase 7 edge watch triage | `docs/atlas/CF_LIKE_EDGE_WATCH_TRIAGE_V1.md` | triage metadata | closed known metadata |

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

## 2026-06-20 Extension Addendum

The following easy extensions are now paper-facing or replay-facing
supplements.  They do not alter the frozen V1 registry count or the frozen V2
base supplement count of 11.  The 2026-06-20 addendum contributes six
paper-facing extension rows, giving 17 public registry/readout rows when the
frozen V2 base and the addendum are read together.

| supplement class | public artifact | claim level | status |
| --- | --- | --- | --- |
| C/F Hankel determinant invariance | `paper/cf_bridge_relation_atlas.tex`; `scripts/run_cf_bridge_replay.py` | `closed_internal_result` | proved in paper; replayed through order 6; ordinary Hankel determinants only |
| Liu binomial-transform normalization | `paper/cf_bridge_relation_atlas.tex` | `closed_metadata` | closed normalization map; no blanket Liu theorem import |
| Franel source-layer clarification | `paper/cf_bridge_relation_atlas.tex` | `closed_metadata` | closed explanatory layer; no automatic Franel theorem promotion |
| Dwork complement split | `paper/cf_bridge_relation_atlas.tex` | `closed_metadata` | `9 - Lambda_C1` complement witness closed; comparison to `Q_F` open; no mutation or Newton-equivalence claim |
| Atkin-Lehner W2 parameter/theta audit | `paper/cf_bridge_relation_atlas.tex` | `closed_internal_result` | `W_2` gives affine parameter normalization and swaps theta forms; catalog bridge is not literally `W_2`; BTY `chi(w_d)` remains open |
| Chan-Cooper five-companion Lucas lane | `paper/cf_bridge_relation_atlas.tex`; `scripts/run_chan_cooper_lucas_replay.py` | `closed_internal_result` | direct binomial Lucas/Kummer proof for `V6A,V6B,V6C,V8,V9` companion rows; adjacent source layer, not C/F transfer or BTY import |

## Guardrails

- V2 does not upgrade finite replay to theorem proof.
- V2 declares only fixed-modulus Rowland-Yassawi Level 2a theorem certificates.
- V2 does not declare all-good-primes/all-alpha Rowland-Yassawi Level 2b.
- V2 treats source-Cartier alpha=2 product exposure as deferred beyond the
  included fixed-modulus metadata.
- V2 does not treat Dwork metadata as an active C/F theorem transfer.
- V2 does not create new C/F-like edges from the Phase 7 watch rows.
- V2 keeps `HYP-LOW-CARRY-ID` as the Straub derivative-transfer blocker.
- V2 treats the Chan-Cooper five-companion Lucas lane as an adjacent direct proof, not as a C/F theorem transfer and not as a BTY import.

## Next Action

Use this V2 registry as the Paper B source index. The next Rowland-Yassawi
registry task is not another fixed-modulus row; it is the Level 2b
all-good-primes/all-alpha certificate specification and prime-filter split.
