# C/F theorem-transfer registry: base 20-row release

Release: `v1.0.0`
Claim level: guarded registry, not a proof artifact

This table is the human-readable index of
`data/relation_atlas/cf_theorem_transfer_registry_v1.json`. The machine record
contains source/target objects, rewrites, finite evidence, proof obligations,
and a public `scope_note` for every row.

## Claim classes

`proved_in_paper`, `theorem_import_by_reference`,
`conditional_theorem_transfer`, `finite_exact_replay`,
`source_attached_conjecture`, `proof_obligation`, `blocked`, `watch`,
`bounded_negative`, and `explicit_automaton_metadata`.

## Certified counts

```yaml
statement_count: 20
proved_in_paper_count: 3
conditional_transfer_count: 6
theorem_import_by_reference_count: 5
source_attached_conjecture_count: 1
finite_exact_replay_count: 1
proof_obligation_count: 2
blocked_count: 2
watch_count: 0
```

## Registry rows

| ID | Source label | Claim class | Public status |
|---|---|---|---|
| `cf_mobius_binomial_bridge` | C/F bridge, Theorem 1 | `proved_in_paper` | proved in paper |
| `cf_coefficient_transform_involution` | C/F bridge, Corollary 1 | `proved_in_paper` | proved in paper |
| `cf_ode_pullback` | C/F bridge, Corollary 2 | `proved_in_paper` | proved in paper |
| `cf_sun_q_to_tc_transfer_contract` | C/F bridge, Corollary 3 | `conditional_theorem_transfer` | explicit signed transfer only |
| `cf_ct_newton_guardrail` | CT/Newton guardrail | `blocked` | no mutation/Newton-equivalence claim |
| `sun_2022_intro_1_3_minus8` | Sun 2022, introduction (1.3), `d=8` | `conditional_theorem_transfer` | cited source hypotheses retained |
| `sun_2022_intro_1_3_minus9` | Sun 2022, introduction (1.3), `d=9` | `conditional_theorem_transfer` | cited source hypotheses retained |
| `sun_2022_theorem_3_4_eq_3_2` | Sun 2022, Theorem 3.4 (3.2) | `conditional_theorem_transfer` | cited source hypotheses retained |
| `sun_2022_theorem_3_4_eq_3_3` | Sun 2022, Theorem 3.4 (3.3) | `conditional_theorem_transfer` | cited source hypotheses retained |
| `sun_2022_theorem_3_4_eq_3_4` | Sun 2022, Theorem 3.4 (3.4) | `conditional_theorem_transfer` | cited source hypotheses retained |
| `sun_2022_conjecture_3_5_raw_c` | Sun 2022, Conjecture 3.5 | `source_attached_conjecture` | addressed by a separate paper, not by C/F transfer |
| `liu_2025_binomial_transform_profile` | Liu 2025, 15-sequence profile | `theorem_import_by_reference` | row-level normalization guard |
| `straub_2023_theorem_1_1` | Straub 2023, Theorem 1.1 | `theorem_import_by_reference` | cited theorem metadata |
| `straub_2023_theorem_1_3` | Straub 2023, Theorem 1.3 | `theorem_import_by_reference` | derivative-transfer conditions retained |
| `bty_2024_theorem_1_1_row_registry` | BTY, Theorem 1.1 | `theorem_import_by_reference` | row-level hypotheses retained |
| `bty_2024_theorem_1_3_weight1_rows` | BTY, Theorem 1.3 weight-1 branch | `proof_obligation` | missing `chi(w_d)` values |
| `dwork_mellit_vlasenko_ct_metadata` | Mellit-Vlasenko 2016, Theorem 1 | `finite_exact_replay` | finite metadata only |
| `dwork_catalog_f_p_blocked` | F catalog `P_F` row | `blocked` | Newton condition fails |
| `rowland_yassawi_2015_contract` | Rowland-Yassawi 2015 | `theorem_import_by_reference` | source theorem contract only |
| `rowland_yassawi_cooper_s7_pilot` | Cooper `s7` finite-state row | `explicit_automaton_metadata` | closed finite metadata |

The registry is schema-checked, count-replayed, claim-class audited, and covered
by the release SHA-256 manifest.
