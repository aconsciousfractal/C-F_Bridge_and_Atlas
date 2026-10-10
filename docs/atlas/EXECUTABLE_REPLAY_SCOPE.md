# Executable replay scope

The scripts are reproducibility aids; the mathematical proofs are in the paper.

| Command | Scope actually checked |
|---|---|
| `run_cf_bridge_replay.py` | C/F coefficient identities n=0..30 and ordinary Hankel determinant equality through order6. |
| `run_atkin_lehner_w2_eta_multiplier_certificate.py` | Exact arithmetic for four eta-multiplier factorizations. |
| `run_chan_cooper_lucas_replay.py` | Eleven sequences, n<=120 and primes2,3,5,7,11,13,17,19. |
| `run_atlas_schema_check.py` | Required JSON keys, including the October addendum. |
| `run_atlas_count_replay.py` | Record recounts and declared-summary comparisons; received historical scan/build/replay totals remain identified as received. |
| `run_claim_class_audit.py` | Allowed claim classes and explicit metadata guardrails. |
| `run_public_repo_audit.py` | Local links, distributed paths and explicit historical path exclusions; forbidden local/process residue. |
| `verify_public_package.py` | Complete LF-normalized inventory of included JSON artifacts, record/count consistency, claims, primary links and citation fields. |

The proof of Smith equality is unimodular congruence for every N, not a finite
Smith replay. The theta-ratio proof is an explicit small eta/valence argument;
no large q-expansion engine is needed for it. A full Sturm/valence engine is
not distributed. The all-primes Lucas proof is arithmetic in the paper;
its replay is only a finite check of formulas and sign conventions.

Six Cartier and six RY records summarize certificates whose full payloads
are absent. Historical `outputs/` references are explicitly excluded and
counted, not treated as delivered files. The old scan denominator and 80-term
triage are not regenerated. See [the October addendum](CF_OCTOBER_2026_ADDENDUM.md).
