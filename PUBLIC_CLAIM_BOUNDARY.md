# Public Claim Boundary

Companion documentation added 2026-07-08, after publication; it does not
modify the paper. Authoritative sources:
`docs/atlas/EXECUTABLE_REPLAY_SCOPE.md` and the machine-readable claim
classes audited by `scripts/run_claim_class_audit.py`.

## Can Say

- The C/F bridge theorem and its Hankel/ODE transport are proved in the
  paper (C1); the repo provides finite replays as sanity aids.
- The Chan-Cooper all-primes Lucas result is proved in the paper (C2).
- The W2 eta-multiplier constants replay exactly at the finite arithmetic
  scope used in the appendix (C3).
- The relation atlas is a claim-disciplined, machine-audited metadata
  package for theorem transfer (C4).

## Must Not Say

- That finite replays or fixed-modulus metadata prove anything new — the
  scope note's guardrail is explicit: they "are not promoted to new
  theorem-transfer proofs by themselves".
- That the package contains a full Sturm/valence modular-form certificate
  or a complete Rowland-Yassawi automaton archive — both are explicitly
  outside the curated package (O1).
- That atlas registry rows are theorems — they are transfer metadata with
  per-row claim levels; the `claim_level` field is the authority.
- That the replay scripts are the proofs — the paper carries the proofs.

## Scope Notes

- `scripts/run_public_repo_audit.py` mechanically checks that public
  docs/data cite no missing development paths — run it after any doc
  change.
- All scripts are standard-library Python; committed JSONs are canonical
  replay summaries.
