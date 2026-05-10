# C/F-Like Edge Watch Triage V1

**Date:** 2026-05-05
**Status:** complete
**Claim level:** triage metadata
**Input scan:** `data/relation_atlas/cf_like_mobius_binomial_edge_scan_v1.json`
**Public replay:** `scripts/run_atlas_count_replay.py` and `scripts/run_claim_class_audit.py`

## Summary

```yaml
watch_input_count: 8
bounded_negative_count: 0
still_watch_count: 0
proof_obligation_candidate_count: 0
closed_known_metadata_count: 8
blocked_count: 0
phase8_trigger: true
targeted_replay_terms: 80
```

Phase 7 did not run a generic search. It replayed only the eight V1 watch
hits and applied the roadmap promotion gates. Coefficient agreement alone was
not used to promote a new theorem edge.

Result: all eight V1 watch rows are reclassified as `closed_known_metadata`.
Six rows are the `apery_zeta3`/`az_gamma` canonical alias identity under the
inert transform `a=0, s=1`; the remaining two rows are inverse Franel
Mobius-binomial transforms already recorded in the local Franel transform
trace.

## Method

- The V1 scan JSON is treated as immutable provenance.
- Only rows with `classification: watch` were replayed.
- Replay window was raised from 12 terms to 80 terms.
- A row could be reclassified only by local alias/inverse-transform provenance,
  not by replay alone.
- No recurrence, ODE, modular, or CT proof obligation was created, because
  every watch row has a simpler known-metadata explanation.

## Watch Hit Table

| edge | source | target | r | a | s | replay | local overlay | decision |
| --- | --- | --- | ---: | ---: | ---: | --- | --- | --- |
| `watch_001_apery_zeta3_to_az_gamma_r1_a0_s1` | `apery_zeta3` | `az_gamma` | 1 | 0 | 1 | pass, 80 terms | canonical alias | `closed_known_metadata` |
| `watch_002_apery_zeta3_to_az_gamma_r2_a0_s1` | `apery_zeta3` | `az_gamma` | 2 | 0 | 1 | pass, 80 terms | canonical alias | `closed_known_metadata` |
| `watch_003_apery_zeta3_to_az_gamma_r3_a0_s1` | `apery_zeta3` | `az_gamma` | 3 | 0 | 1 | pass, 80 terms | canonical alias | `closed_known_metadata` |
| `watch_004_az_gamma_to_apery_zeta3_r1_a0_s1` | `az_gamma` | `apery_zeta3` | 1 | 0 | 1 | pass, 80 terms | canonical alias | `closed_known_metadata` |
| `watch_005_az_gamma_to_apery_zeta3_r2_a0_s1` | `az_gamma` | `apery_zeta3` | 2 | 0 | 1 | pass, 80 terms | canonical alias | `closed_known_metadata` |
| `watch_006_az_gamma_to_apery_zeta3_r3_a0_s1` | `az_gamma` | `apery_zeta3` | 3 | 0 | 1 | pass, 80 terms | canonical alias | `closed_known_metadata` |
| `watch_007_zagier_c_a002893_to_franel_a000172_r1_a-1_s1` | `zagier_c_a002893` | `franel_a000172` | 1 | -1 | 1 | pass, 80 terms | known inverse Franel transform | `closed_known_metadata` |
| `watch_008_zagier_f_a093388_to_franel_a000172_r1_a8_s-1` | `zagier_f_a093388` | `franel_a000172` | 1 | 8 | -1 | pass, 80 terms | known inverse Franel transform | `closed_known_metadata` |

## Individual Edge Reports

### Alias identity block: `apery_zeta3` / `az_gamma`

```yaml
rows:
  - watch_001_apery_zeta3_to_az_gamma_r1_a0_s1
  - watch_002_apery_zeta3_to_az_gamma_r2_a0_s1
  - watch_003_apery_zeta3_to_az_gamma_r3_a0_s1
  - watch_004_az_gamma_to_apery_zeta3_r1_a0_s1
  - watch_005_az_gamma_to_apery_zeta3_r2_a0_s1
  - watch_006_az_gamma_to_apery_zeta3_r3_a0_s1
transform:
  class: mobius_binomial
  a: 0
  s: 1
  r_values: [1, 2, 3]
coefficient_replay:
  status: pass
  n_terms: 80
inverse_transform:
  status: two_way_identity_alias
recurrence_compatibility:
  status: pass_by_catalog_alias
ode_pullback:
  status: not_needed_identity
modular_compatibility:
  status: pass_by_local_metadata
ct_diagonal_compatibility:
  status: not_a_new_ct_operation
literature_overlay:
  status: local_atlas_alias_found
  sources:
    - data/relation_atlas/cf_like_edge_watch_triage_v1.json
    - docs/atlas/CF_THEOREM_TRANSFER_REGISTRY_V1.md
    - docs/04_theorem_congruence/06_mod_p_galois/MOD_P_GALOIS_SIGNATURES_2026-04-29.md
decision:
  status: closed_known_metadata
  claim_level: closed_known_metadata
  reason: identity_transform_on_catalog_alias
  blocking_lemma: null
  next_action: "Use as calibration/alias metadata only; do not add theorem-transfer edge."
```

For `a=0` and `s=1`, the transform

```text
B(x) = (1-a*x)^(-r) A(s*x/(1-a*x))
```

reduces to `B(x)=A(x)` for every listed `r`. The local atlas already records
`apery_zeta3::az_gamma` as a canonical identity/calibration pair. These six
rows therefore close as known metadata, not as new C/F-like edges.

### Inverse Franel block

```yaml
rows:
  - watch_007_zagier_c_a002893_to_franel_a000172_r1_a-1_s1
  - watch_008_zagier_f_a093388_to_franel_a000172_r1_a8_s-1
coefficient_replay:
  status: pass
  n_terms: 80
inverse_transform:
  status: inverse_of_known_forward_edge
known_forward_edges:
  franel_to_c: "franel_a000172 -> zagier_c_a002893 with (r,a,s)=(1,1,1)"
  franel_to_f: "franel_a000172 -> zagier_f_a093388 with (r,a,s)=(1,8,-1)"
recurrence_compatibility:
  status: not_needed_known_inverse
ode_pullback:
  status: not_needed_known_inverse
modular_compatibility:
  status: not_needed
ct_diagonal_compatibility:
  status: not_needed_for_triage
literature_overlay:
  status: local_franel_transform_trace_found
  sources:
    - docs/03_franel_sun_liu/01_franel_cf_transforms/MOBIUS_BINOMIAL_TRANSFORM_SEARCH_2026-04-30.md
    - docs/03_franel_sun_liu/01_franel_cf_transforms/FRANEL_LITERATURE_TRACE_2026-04-29.md
    - data/relation_atlas/cf_like_mobius_binomial_edge_scan_v1.json
decision:
  status: closed_known_metadata
  claim_level: closed_known_metadata
  reason: known_inverse_franel_transform
  blocking_lemma: null
  next_action: "Record as inverse known Franel metadata; no new theorem-transfer proof obligation."
```

The two remaining watch hits are not new relations. They are inverse forms of
the known Franel transforms already recorded in the atlas:

```text
C(x) = (1-x)^(-1) R(x/(1-x))
R(x) = (1+x)^(-1) C(x/(1+x))

F(x) = (1-8x)^(-1) R(-x/(1-8x))
R(x) = (1-8x)^(-1) F(-x/(1-8x))
```

They are therefore closed as known inverse-transform metadata.

## Atlas Impact

- `OP-CF-006` no longer has eight unresolved V1 watch rows.
- No new C/F-like theorem-transfer edge is promoted.
- No new proof obligation is created.
- Phase 8 is triggered only as a packaging/readout refresh, because watch rows
  changed status to known metadata.

## Guardrails

- The `apery_zeta3`/`az_gamma` rows are catalog-alias calibration, not
  discovery evidence.
- The Franel inverse rows are inverse metadata for already-known transforms,
  not new edges.
- Beta/TDA or coefficient-only evidence is not used.
- Rowland-Yassawi, Dwork, Liu, and Sun layers are unaffected by this triage.

## Next Actions

1. Refresh roadmap/status readouts to record Phase 7 completion.
2. Activate Phase 8 packaging only if the atlas package wants status-count
   synchronization.
3. Do not rerun generic edge discovery unless a future phase explicitly opens a
   new bounded scan.
