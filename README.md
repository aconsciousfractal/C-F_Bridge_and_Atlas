# C/F Bridge and Relation Atlas

Public companion for the paper:

> *A Möbius-binomial C/F bridge and a claim-disciplined theorem-transfer atlas
> for Apéry-like sources*

Author: Oleksiy Babanskyy
Package version: `1.0.1`

## Start here

1. Read the canonical paper:
   [`paper/cf_bridge_relation_atlas.pdf`](paper/cf_bridge_relation_atlas.pdf).
2. Use [`README_REVIEWER.md`](README_REVIEWER.md) for a short verification path.
3. Check the exact claim boundary in
   [`CLAIM_LEDGER.md`](CLAIM_LEDGER.md) and
   [`PUBLIC_CLAIM_BOUNDARY.md`](PUBLIC_CLAIM_BOUNDARY.md).
4. Reproduce the finite certificates with [`REPRODUCE.md`](REPRODUCE.md).
5. Browse the curated atlas through
   [`docs/atlas/README.md`](docs/atlas/README.md).

## Main result and scope

The paper proves the direct bridge

```text
F(x) = (1 - 9x)^(-1) C(-x / (1 - 9x))
```

between Zagier's C and F Apéry-like sequences. It derives the involutive
coefficient transform, ordinary integral Hankel congruence and Smith equality, the differential
operator pullback, and a constant-term complement construction. The paper also
proves the Chan-Cooper companion Lucas lane and records the exact finite
Atkin-Lehner `W2` multiplier arithmetic used in its appendix.

The relation atlas deliberately separates:

- results proved in this paper;
- theorems imported with explicit citations;
- conditional transfers;
- exact finite replays and metadata;
- conjectures, proof obligations, and blocked rows.

Finite computation is evidence at its stated bound, never a replacement for a
proof. The package does not contain a full Sturm/valence proof engine or a
complete Rowland-Yassawi all-primes automaton archive.

## Quick verification

```bash
python -m pip install -r requirements.txt
python scripts/run_all_reproducibility_checks.py
```

The command runs all producers, the thirteen-test suite, the claim/count audits,
and the fail-closed public-package verifier.

## Repository map

```text
paper/                paper source, PDF, bibliography, and build notes
data/relation_atlas/  curated machine-readable atlas records
docs/atlas/           public artifact index and human-readable atlas notes
scripts/              standard-library replay and verification tools
tests/                pytest entrypoint tests
results/              canonical finite replay summaries
REPRODUCE.md          exact commands and artifact policy
CITATION.cff          release citation metadata
```

The checks are reproducibility aids. The mathematical proofs remain in the
paper.


For the current Smith consequence, source errata, literal row-ID crosswalk,
and the limits of historical summary records, use the
[October addendum](docs/atlas/CF_OCTOBER_2026_ADDENDUM.md).
