# Claim Ledger

Companion documentation added 2026-07-08, after publication (branch main,
no git tags; history includes "Harden C/F atlas red-team guardrails"); it
does not modify the paper. This repository's claim discipline is already
machine-readable: the two theorem-transfer registry JSONs carry per-row
`claim_level` fields membership-validated against their
`allowed_claim_classes` lists by `scripts/run_claim_class_audit.py`
(canonical output `results/claim_class_audit.json`, status `pass`,
verified 2026-07-08); the other atlas JSONs carry their own per-row
labels (e.g. `classification`, `atlas_claim_level`), and
`docs/atlas/EXECUTABLE_REPLAY_SCOPE.md` states
exactly what is and is not an executable certificate. **Those artifacts
are authoritative; this file is a thin index.**

The **CL** column uses the official taxonomy
(`Gate-Disciplined-Computational-Mathematics/docs/CLAIM_LEVELS.md`); added
2026-07-17 (ledger A-1). It is an additive official-code overlay on the
existing prose **Level** words, which are unchanged; the code assignments
reuse the GATE paper CFB-V4-* map (paper tex L491–498).

| ID | Level | CL | Statement (scoped) | Source locator | Evidence in repo |
| --- | --- | --- | --- | --- | --- |
| C1 | theorem-in-paper | CL5 | The Möbius-binomial C/F bridge: F(x) = (1−9x)⁻¹ C(−x/(1−9x)) between Zagier's C and F Apéry-like sequences; equivalently an involutive binomial-coefficient transform between the catalog-normalized coefficient sequences, preserving ordinary Hankel determinants and transporting the differential equation. | Abstract; proofs in paper | Finite replay through BOUND=30 incl. Hankel equality through order 6: `scripts/run_cf_bridge_replay.py` (green 2026-07-08). Replay is a sanity aid, not the proof. |
| C2 | theorem-in-paper | CL5 | Chan-Cooper companion Lucas result (all primes), as proved in the paper; the repo replay covers the five companion rows and the negative-q level-8 sign twist at finite scope only. | Paper (Chan-Cooper lane) | `scripts/run_chan_cooper_lucas_replay.py` (finite sanity check, green 2026-07-08). |
| C3 | certified-finite | CL3 | Atkin-Lehner W2 eta-multiplier constants used by the paper appendix: exact finite multiplier arithmetic reproduced by script. NOT a full modular-form proof engine. | Paper appendix; `docs/atlas/EXECUTABLE_REPLAY_SCOPE.md` | `scripts/run_atkin_lehner_w2_eta_multiplier_certificate.py` (green 2026-07-08). |
| C4 | metadata (machine-audited) | CLM | The curated relation-atlas package (`data/relation_atlas/*.json`: theorem-transfer registries, Rowland-Yassawi fixed-modulus certificates, Cartier prime-power metadata, edge scans/watch triage): the two theorem-transfer registries carry claim_level fields membership-validated against allowed_claim_classes; the other files carry their own per-row label vocabularies; schema and counts replay. Atlas rows are theorem-transfer METADATA, not new theorems. | `docs/atlas/EXECUTABLE_REPLAY_SCOPE.md` | `run_atlas_schema_check.py`, `run_atlas_count_replay.py`, `run_claim_class_audit.py`, `run_public_repo_audit.py` — all green 2026-07-08 (`run_all_reproducibility_checks.py`: PASS; pytest 6 passed). |
| O1 | open / out of package | CLO | Full modular-form q-expansion/Sturm/valence proof certificate; complete Rowland-Yassawi all-good-primes/all-alpha automaton archive. Explicitly outside this curated package unless archived separately. | `docs/atlas/EXECUTABLE_REPLAY_SCOPE.md` ("Not Included As Executable Proof Certificates") | — |

Guardrail (verbatim from the replay scope): "finite replay and
fixed-modulus metadata are not promoted to new theorem-transfer proofs by
themselves."
