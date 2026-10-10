# Reviewer guide

This guide describes package version `1.0.1` of the repository.

## Ten-minute path

1. Read the abstract and main bridge theorem in
   `paper/cf_bridge_relation_atlas.pdf`.
2. Read `docs/atlas/EXECUTABLE_REPLAY_SCOPE.md` and
   `PUBLIC_CLAIM_BOUNDARY.md`.
3. Install the test dependency and run the complete check:

   ```bash
   python -m pip install -r requirements.txt
   python scripts/run_all_reproducibility_checks.py
   ```

   Expected result: all producers pass, thirteen pytest tests pass, and the public
   verifier reports a complete SHA-256 inventory of the included JSON artifacts.

## Thirty-minute path

4. Inspect `CLAIM_LEDGER.md`. Its five rows distinguish theorem-level results,
   certified finite arithmetic, machine-audited metadata, and excluded claims.
5. Replay the core bridge with `scripts/run_cf_bridge_replay.py`; it checks 31
   coefficients and ordinary Hankel determinants through order 6.
6. Inspect `results/claim_class_audit.json` and
   `results/atlas_count_replay.json` against the registries in
   `data/relation_atlas/`.
7. Run `scripts/verify_public_package.py` directly to check exact inventory,
   hashes, central counts, links, release metadata, and forbidden local/process
   residue.

## Main claims

- The Möbius-binomial C/F bridge and its coefficient, Hankel, ODE, and
  constant-term consequences are proved in the paper.
- The Chan-Cooper companion Lucas result is proved in the paper; the included
  computation is a bounded sanity replay.
- The `W2` eta-multiplier computation is an exact finite certificate, not a
  full modular-form proof engine.
- Atlas rows are claim-classified transfer metadata unless the paper or a cited
  source explicitly proves them.

## Known limits

- No full Sturm/valence certificate archive is shipped.
- No complete Rowland-Yassawi all-good-primes/all-alpha automaton archive is
  shipped.
- Finite replays never promote metadata into a theorem.

For citation of this revision, identify the repository commit and package
version. A version field alone does not establish a tag or GitHub release.
