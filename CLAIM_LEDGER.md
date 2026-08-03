# Claim ledger

Release: `v1.0.0`

The machine-readable registries carry row-level claim classes; this file is the
public theorem/certificate index. The compact levels used here are:

- `CL5`: theorem proved in the paper;
- `CL3`: exact finite certificate;
- `CLM`: machine-audited metadata, not a theorem;
- `CLO`: open or expressly outside the package.

| ID | Level | Statement | Paper/source locator | Evidence in this repository |
|---|---|---|---|---|
| `CF-C1` | `CL5` | The Möbius-binomial bridge `F(x)=(1-9x)^(-1)C(-x/(1-9x))`, the involutive coefficient transform, ordinary Hankel invariance, ODE pullback, and constant-term complement consequence. | Main theorem and consequences in the paper. | `scripts/run_cf_bridge_replay.py` provides a bounded sanity replay. |
| `CF-C2` | `CL5` | The Chan-Cooper five-companion Lucas result for all primes, including the level-8 sign twist. | Chan-Cooper section of the paper. | `scripts/run_chan_cooper_lucas_replay.py` checks the stated finite range. |
| `CF-C3` | `CL3` | Exact `W2` eta-multiplier arithmetic used in the appendix. | Atkin-Lehner appendix. | `scripts/run_atkin_lehner_w2_eta_multiplier_certificate.py`. |
| `CF-C4` | `CLM` | The curated relation atlas preserves claim classes, source labels, finite counts, and guarded theorem-transfer metadata. | Data-package section and `docs/atlas/README.md`. | Schema, count, claim-class, link, and SHA-256 audits. |
| `CF-O1` | `CLO` | Full Sturm/valence certificate machinery and complete Rowland-Yassawi all-good-primes/all-alpha automata are outside this package. | `docs/atlas/EXECUTABLE_REPLAY_SCOPE.md`. | No theorem claim is made from the bounded metadata. |

Guardrail: finite replay and fixed-modulus metadata are not promoted to new
theorem-transfer proofs by themselves.
