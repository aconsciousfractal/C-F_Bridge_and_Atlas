# C/F Theorem Atlas V2 Readout

**Date:** 2026-05-06
**Roadmap:** `ROADMAP_V4.md`, Phase 8 + RY-31 sync
**Status:** package/readout complete with RY fixed-modulus theorem-certificate overlay
**Claim level:** human-readable atlas readout, not a proof artifact

## V2 Headline

The V4 atlas package is synchronized. Phase 7 closed the eight residual
C/F-like watch hits as known metadata, so there are no unresolved V1 watch rows
left from the Mobius-binomial scan.

RY-31 adds the Rowland-Yassawi fixed-modulus theorem-certificate overlay:
Cooper s7 and C/F have Level 2a certificates at mod 4 and mod 9. This is a
fixed-modulus theorem-by-reference layer only; the all-good-primes/all-alpha
Level 2b layer remains open.

## Status Counts

```yaml
base_registry_statement_count: 20
v2_supplement_count: 11
v2_base_supplement_count: 11
extension_2026_06_20_count: 6
total_public_registry_extension_rows: 17
phase7_input_watch_rows: 8
phase7_closed_known_metadata_rows: 8
phase7_still_watch_rows: 0
phase7_new_theorem_edges: 0
phase7_new_proof_obligations: 0
active_or_blocked_open_problem_count_at_v2_freeze: 6
post_sun_3_5_active_or_blocked_open_problem_count: 4
closed_or_reconciled_open_problem_count: 4
rowland_yassawi_level_2a_fixed_modulus_certificate_count: 6
rowland_yassawi_level_2b_status: open
```

## Closed V4 Metadata Layers

| layer | status |
| --- | --- |
| C/F CT complement operation | closed metadata |
| C/F Dwork complement witness | metadata ready by reference |
| Liu eta/s18 convention repair | closed convention-mapped metadata |
| Cooper s7 mod 2/mod 3 automata | closed explicit automaton metadata |
| Franel mod 2/mod 3 automata | closed Lucas/binomial metadata |
| C/F rational diagonal contracts | closed metadata |
| C/F mod 2/mod 3 automata | closed explicit automaton metadata |
| C/F mod 4/mod 9 prime-power mini-theorems | closed explicit prime-power automaton metadata |
| Source-Cartier alpha=2 fixed-modulus artifacts | closed explicit prime-power metadata, internal only |
| Rowland-Yassawi fixed-modulus theorem certificates | closed Level 2a theorem-import-by-reference metadata |
| C/F-like edge watch triage | closed known metadata |

## 2026-06-20 Extension Notes

| extension | status | guardrail |
| --- | --- | --- |
| C/F Hankel determinant invariance | closed internal result; finite replay through order 6 | ordinary Hankel determinants only |
| Liu normalization bridge | closed convention map: $v_m^{(C)}(9)=(-1)^mF_m$ and $v_m^{(F)}(9)=(-1)^mC_m$ | no blanket Liu theorem import |
| Franel source-layer exposition | source provenance/context | no automatic Franel theorem promotion |
| Dwork complement wording | distinguishes $\Lambda_{C,1}$, $9-\Lambda_{C,1}$, and independent $Q_F$ | no mutation or Newton-equivalence claim |
| Atkin-Lehner W2 normalization | closed parameter/theta audit: $t_C\vert W_2=1-8t_F^{\rm cat}$ and W2 swaps the C/F theta forms up to explicit constants | catalog bridge is affine-normalized, not literal W2 |
| Rowland-Yassawi automata | fixed-modulus Level 2a only; all-good-primes Level 2b remains open | no full Rowland-Yassawi import |
| Chan--Cooper five-companion Lucas lane | closed internal direct Lucas result for $\mathrm{V6A},\mathrm{V6B},\mathrm{V6C},\mathrm{V8},\mathrm{V9}$ companion rows; finite replay included | not C/F transfer; not BTY import; raw $\chi(w_d)$ still blocked |
| BTY / Atkin-Lehner $\chi(w_d)$ | remains open pending row-specific multiplier data | W2 audit does not compute BTY multipliers |
| periods, mod-p Galois, q-bridge | watch tracks only | no paper claim activated |

## Remaining Hard Blocks

```yaml
sun_raw_c_bridge: OP-CF-001
a2b_global_bm_core_glue: OP-CF-002
bty_chi_wd_values: OP-CF-003
dwork_complement_vs_qf_equivalence: OP-CF-004b
straub_derivative_transport_low_carry_identity: OP-CF-008
rowland_yassawi_level_2b_all_good_primes_all_alpha: OP-CF-009
```

## Paper B Use

Use V2 as the Paper B atlas source map:

```text
registry base: CF_THEOREM_TRANSFER_REGISTRY_V1.md
registry V2 index: CF_THEOREM_TRANSFER_REGISTRY_V2.md
open problems V2: CF_OPEN_PROBLEM_ATLAS_V2.md
phase7 triage: CF_LIKE_EDGE_WATCH_TRIAGE_V1.md
manifest: RELATION_ATLAS_V2_PACKAGE_MANIFEST.md
ry_level2a_overlay: RELATION_ATLAS_V2_RY_FIXED_MODULUS_THEOREM_CERTIFICATES.md
```

## Guardrails

- No Phase 7 watch row becomes a new theorem-transfer edge.
- V2 now records fixed-modulus Rowland-Yassawi Level 2a theorem certificates.
- This does not conflict with the paper guardrail against a full Rowland-Yassawi
  theorem import: the overlay is fixed-modulus/prime-power metadata, while the
  excluded claim is all-good-primes/all-alpha.
- V2 does not claim all-good-primes/all-alpha Rowland-Yassawi Level 2b import.
- V2 keeps source-Cartier alpha=2 product exposure internal; no public
  alpha=2 product route is activated.
- V2 keeps Dwork and Liu layers as theorem metadata, not active C/F proof
  inputs.
- V2 keeps Straub proof obligations separate from the closed C/F bridge.  The
  Sun target is retained as V2 provenance but is addressed in the companion
  Franel-Domb Sun 3.5 paper, not by the C/F bridge.
