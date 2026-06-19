# C/F Bridge And Relation Atlas Companion

Standalone computational companion for the paper:

```text
A Mobius-binomial C/F bridge and a claim-disciplined theorem-transfer atlas
for Apery-like sources
```

Author: Oleksiy Babanskyy

This repository contains the paper source/PDF, selected relation-atlas JSON
artifacts, human-readable atlas notes, and small reproducibility scripts. The
scripts include finite C/F bridge coefficient and Hankel replays, the
Atkin-Lehner W2 eta-multiplier certificate replay, and atlas audit/count
checks. The package is intentionally curated: it is not a dump of the
development workspace, and `docs/atlas/EXECUTABLE_REPLAY_SCOPE.md` states
exactly what is and is not included as an executable certificate.

## Layout

```text
paper/                paper source, PDF, bibliography, and build notes
data/relation_atlas/  curated JSON artifacts used by the checks
docs/atlas/           selected human-readable atlas artifacts and replay scope note
scripts/              standard-library replay and audit scripts
tests/                pytest smoke tests for the scripts
results/              generated replay summaries
REPRODUCE.md          command guide
CITATION.cff          citation metadata
LICENSE               MIT license
```

## Quick Check

```bash
python scripts/run_all_reproducibility_checks.py
python -m pytest
```

The checks are computational reproducibility aids. They do not replace the
mathematical arguments in the paper. For scope details, see
`docs/atlas/EXECUTABLE_REPLAY_SCOPE.md`.
