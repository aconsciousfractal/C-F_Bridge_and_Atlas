# Public claim boundary

Release: `v1.0.0`

Authoritative sources are the paper, `CLAIM_LEDGER.md`,
`docs/atlas/EXECUTABLE_REPLAY_SCOPE.md`, and the machine-readable claim classes
verified by `scripts/run_claim_class_audit.py`.

## Supported statements

- The C/F bridge and its coefficient, ordinary-Hankel, ODE, and constant-term
  consequences are proved in the paper.
- The Chan-Cooper companion Lucas result is proved in the paper.
- The `W2` eta-multiplier constants replay exactly at the finite arithmetic
  scope used in the appendix.
- The relation atlas is a claim-classified, machine-audited metadata package
  for theorem transfer.

## Unsupported statements

- Finite replays or fixed-modulus metadata do not prove a new theorem.
- Registry rows are not automatically theorems; their `claim_level` controls
  their public status.
- The package does not contain a complete Sturm/valence certificate engine or
  a complete Rowland-Yassawi all-primes automaton archive.
- The replay scripts are not substitutes for the paper's proofs.
- The C/F bridge does not by itself prove Sun's raw-C conjecture or a general
  Dwork/Newton equivalence.

Run `scripts/verify_public_package.py` after any public-document or artifact
change.
