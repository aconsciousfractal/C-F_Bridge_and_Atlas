# Relation Atlas V2 Package Manifest

**Date:** 2026-05-06
**Roadmap:** `ROADMAP_V4.md`, Phase 8 + RY-31 sync
**Status:** complete with RY fixed-modulus theorem-certificate overlay
**Claim level:** package manifest

## Core V2 Package

| role | artifact |
| --- | --- |
| Registry base | `docs/05_relation_atlas/01_registry/CF_THEOREM_TRANSFER_REGISTRY_V1.md` |
| Registry V2 index | `docs/05_relation_atlas/01_registry/CF_THEOREM_TRANSFER_REGISTRY_V2.md` |
| Open problem atlas V2 | `docs/05_relation_atlas/02_open_problems/CF_OPEN_PROBLEM_ATLAS_V2.md` |
| V2 readout | `docs/05_relation_atlas/00_status_readouts/CF_THEOREM_ATLAS_V2_READOUT.md` |
| Master status | `docs/05_relation_atlas/00_status_readouts/CF_THEOREM_ATLAS_MASTER_STATUS.md` |
| Package manifest JSON | `data/relation_atlas/cf_theorem_atlas_v2_package_manifest.json` |

## V2 Metadata Supplements

| artifact | purpose |
| --- | --- |
| `docs/05_relation_atlas/05_v2_metadata/RELATION_ATLAS_V2_DWORK_CF_COMPLEMENT_MODEL.md` | Dwork C/F complement metadata |
| `docs/05_relation_atlas/05_v2_metadata/RELATION_ATLAS_V2_LIU_CONVENTION_REPAIRED_METADATA.md` | Liu convention repair |
| `docs/05_relation_atlas/05_v2_metadata/RELATION_ATLAS_V2_COOPER_S7_AUTOMATON_METADATA.md` | Cooper s7 automata |
| `docs/05_relation_atlas/05_v2_metadata/RELATION_ATLAS_V2_FRANEL_AUTOMATON_METADATA.md` | Franel automata |
| `docs/05_relation_atlas/05_v2_metadata/RELATION_ATLAS_V2_CF_DIAGONAL_CONTRACT_METADATA.md` | C/F rational diagonal contract |
| `docs/05_relation_atlas/05_v2_metadata/RELATION_ATLAS_V2_CF_AUTOMATON_METADATA.md` | C/F mod 2/mod 3 automata |
| `docs/05_relation_atlas/05_v2_metadata/RELATION_ATLAS_V2_CF_PRIME_POWER_AUTOMATON_METADATA.md` | C/F mod 4/mod 9 automata |
| `docs/05_relation_atlas/05_v2_metadata/RELATION_ATLAS_V2_SOURCE_CARTIER_PRIME_POWER_METADATA.md` | source-Cartier alpha=2 fixed-modulus metadata |
| `docs/05_relation_atlas/05_v2_metadata/RELATION_ATLAS_V2_RY_FIXED_MODULUS_THEOREM_CERTIFICATES.md` | Rowland-Yassawi Level 2a fixed-modulus theorem certificates |
| `docs/05_relation_atlas/05_v2_metadata/RELATION_ATLAS_V2_GESSEL_LUCAS_DERIVATIVE_METADATA_2026-04-30.md` | Straub derivative metadata/proof obligation |
| `docs/05_relation_atlas/04_edge_scan/CF_LIKE_EDGE_WATCH_TRIAGE_V1.md` | Phase 7 edge watch triage |

## Data Artifacts

| artifact | purpose |
| --- | --- |
| `data/relation_atlas/cf_theorem_transfer_registry_v1.json` | V1 registry companion |
| `data/relation_atlas/cf_like_mobius_binomial_edge_scan_v1.json` | immutable V1 edge scan |
| `data/relation_atlas/cf_like_edge_watch_triage_v1.json` | Phase 7 triage companion |
| `data/relation_atlas/source_cartier_prime_power_metadata_v1.json` | source-Cartier alpha=2 metadata companion |
| `data/relation_atlas/rowland_yassawi_fixed_modulus_theorem_certificates_v1.json` | Rowland-Yassawi Level 2a fixed-modulus theorem-certificate companion |
| `data/relation_atlas/cf_theorem_atlas_v2_package_manifest.json` | Phase 8 package manifest |

## Phase 8 Trigger

```yaml
triggered_by:
  - Phase 7 changed 8 watch rows to closed_known_metadata
  - RY-30 promoted selected fixed-modulus Rowland-Yassawi certificates to Level 2a
not_triggered_by:
  - finite replay alone
  - new generic discovery
  - Beta/TDA evidence
```

## Guardrails

- This manifest is a package index, not a proof.
- V1 scan artifacts remain immutable provenance.
- V2 supplement artifacts keep their own claim levels.
- No new theorem-transfer edge is introduced by Phase 8.
- The RY overlay is fixed-modulus Level 2a only; no all-good-primes/all-alpha
  Level 2b import is claimed.
