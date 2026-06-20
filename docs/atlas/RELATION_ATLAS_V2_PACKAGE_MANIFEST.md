# Relation Atlas V2 Public Package Manifest

**Date:** 2026-05-06
**Public package update:** 2026-05-10
**Paper-facing extension addendum:** 2026-06-20
**Roadmap lineage:** Phase 8 + RY-31 sync
**Status:** curated public companion package with RY fixed-modulus theorem-certificate overlay
**Claim level:** package manifest, not a proof artifact

This file is the public-package manifest for the companion repository.  It keeps
the V2 atlas counts and claim classes from the development atlas, but all paths
below are paths that exist in this standalone repository.

## Core Public Package

| role | artifact |
| --- | --- |
| Registry base | `docs/atlas/CF_THEOREM_TRANSFER_REGISTRY_V1.md` |
| Registry V2 index | `docs/atlas/CF_THEOREM_TRANSFER_REGISTRY_V2.md` |
| Open problem atlas V2 | `docs/atlas/CF_OPEN_PROBLEM_ATLAS_V2.md` |
| V2 readout | `docs/atlas/CF_THEOREM_ATLAS_V2_READOUT.md` |
| Sun 3.5 separate-paper status note | `docs/atlas/SUN_3_5_SEPARATE_PAPER_STATUS_UPDATE.md` |
| Package manifest JSON | `data/relation_atlas/cf_theorem_atlas_v2_package_manifest.json` |

## Public Metadata Artifacts

| artifact | purpose |
| --- | --- |
| `data/relation_atlas/cf_theorem_transfer_registry_v1.json` | V1 registry companion |
| `data/relation_atlas/cf_theorem_transfer_registry_2026_06_extension.json` | June 2026 paper-facing extension registry companion |
| `data/relation_atlas/cf_like_mobius_binomial_edge_scan_v1.json` | immutable V1 edge scan |
| `data/relation_atlas/cf_like_edge_watch_triage_v1.json` | Phase 7 triage companion |
| `data/relation_atlas/source_cartier_prime_power_metadata_v1.json` | source-Cartier alpha=2 metadata companion |
| `data/relation_atlas/rowland_yassawi_fixed_modulus_theorem_certificates_v1.json` | Rowland-Yassawi Level 2a fixed-modulus theorem-certificate companion |
| `data/relation_atlas/cf_opposite_side_candidates.json` | opposite-side C/F candidate classifications |
| `data/relation_atlas/cf_theorem_atlas_v2_package_manifest.json` | Phase 8 package manifest |

## V2 Supplement Coverage

The original V2 atlas contains 11 frozen supplement classes.  In this public
companion package, those classes are represented by the registry/readout
documents and by the curated JSON artifacts above rather than by copying every
development note as a separate Markdown file.  The 2026-06-20 paper-facing
addendum adds six extension rows: Hankel, Liu, Franel, Dwork complement
wording, Atkin-Lehner W2 normalization, and the Chan-Cooper five-companion
Lucas lane.  These rows do not alter the frozen V2 base manifest count.

| supplement class | public representation |
| --- | --- |
| Dwork C/F complement, Liu convention, Cooper and Franel automata, C/F diagonal and automata metadata | `docs/atlas/CF_THEOREM_ATLAS_V2_READOUT.md` and `docs/atlas/CF_THEOREM_TRANSFER_REGISTRY_V2.md` |
| Source-Cartier alpha=2 fixed-modulus metadata | `data/relation_atlas/source_cartier_prime_power_metadata_v1.json` |
| Rowland-Yassawi fixed-modulus theorem certificates | `data/relation_atlas/rowland_yassawi_fixed_modulus_theorem_certificates_v1.json` |
| Straub derivative transport proof-obligation metadata | `docs/atlas/CF_OPEN_PROBLEM_ATLAS_V2.md` |
| Phase 7 edge-watch triage | `docs/atlas/CF_LIKE_EDGE_WATCH_TRIAGE_V1.md` and `data/relation_atlas/cf_like_edge_watch_triage_v1.json` |

## Public Count Reconciliation

```yaml
v2_base_supplement_count: 11
extension_2026_06_20_count: 6
total_public_registry_extension_rows: 17
```

The public package keeps the frozen V2 base count and records later
paper-facing extensions separately.

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
- V2 supplement classes keep their own claim levels.
- No new theorem-transfer edge is introduced by Phase 8.
- The RY overlay is fixed-modulus Level 2a only; no all-good-primes/all-alpha
  Level 2b import is claimed.
