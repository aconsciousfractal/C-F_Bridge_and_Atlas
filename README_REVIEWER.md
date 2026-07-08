# Reviewer Guide

Companion documentation added 2026-07-08, after publication; it does not
modify the paper.

## Ten-Minute Path

1. Read the abstract in `paper/` — the bridge
   F(x) = (1−9x)⁻¹ C(−x/(1−9x)) and its transport properties.
2. Read `docs/atlas/EXECUTABLE_REPLAY_SCOPE.md` — the two roles of this
   companion and, critically, "Not Included As Executable Proof
   Certificates".
3. Run everything:
   `python scripts/run_all_reproducibility_checks.py`
   (expects "all reproducibility checks: PASS"; ~1 min, verified
   2026-07-08) and `python -m pytest -q` (6 passed).

## Thirty-Minute Path

4. Open `results/claim_class_audit.json` (status `pass`, empty failures)
   and cross-check the `claim_level` fields of
   `data/relation_atlas/cf_theorem_transfer_registry_v1.json` against its
   `allowed_claim_classes` list (the membership audit covers the two
   registry JSONs).
5. Replay one lane end to end: `scripts/run_cf_bridge_replay.py` (bridge
   coefficients through BOUND=30, Hankel order 6) against the paper's
   bridge theorem statement.
6. Note `scripts/run_public_repo_audit.py` — the repo mechanically checks
   that public docs cite no missing development paths.
7. Read `PUBLIC_CLAIM_BOUNDARY.md` and `CLAIM_LEDGER.md`.

## Main Claims

- C/F Möbius-binomial bridge theorem with Hankel/ODE transport (proved in
  paper; finitely replayed here).
- Chan-Cooper companion Lucas result (proved in paper; finite replay).
- W2 eta-multiplier exact finite arithmetic (certified finite).
- Claim-disciplined relation atlas (machine-audited metadata).

## Known Limits

- No full Sturm/valence certificate; no complete Rowland-Yassawi
  automaton archive (explicitly out of package).
- Finite replays never substitute for the paper's proofs.
- No git tags; cite by commit (HEAD at retrofit: 60a54ef).
