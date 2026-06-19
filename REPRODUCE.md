# Reproducing The Companion Checks

This repository is a standalone public companion for the combined C/F bridge
and theorem-transfer atlas paper.

From the repository root, run:

```bash
python scripts/run_all_reproducibility_checks.py
```

or run the checks separately:

```bash
python scripts/run_cf_bridge_replay.py
python scripts/run_atkin_lehner_w2_eta_multiplier_certificate.py
python scripts/run_atlas_schema_check.py
python scripts/run_atlas_count_replay.py
python scripts/run_claim_class_audit.py
python scripts/run_public_repo_audit.py
```

The scripts use only the Python standard library.  The C/F replay records
coefficient identities through `BOUND=30` and ordinary Hankel determinant
equality through order 6.  The Atkin-Lehner W2 replay records the exact
eta-multiplier arithmetic used in the paper appendix. Successful runs write:

```text
results/cf_bridge_replay.json
results/atkin_lehner_w2_eta_multiplier_certificate.json
results/atlas_count_replay.json
results/claim_class_audit.json
```

The paper can be rebuilt from `paper/`:

```bash
cd paper
pdflatex -interaction=nonstopmode -halt-on-error cf_bridge_relation_atlas.tex
bibtex cf_bridge_relation_atlas
pdflatex -interaction=nonstopmode -halt-on-error cf_bridge_relation_atlas.tex
pdflatex -interaction=nonstopmode -halt-on-error cf_bridge_relation_atlas.tex
```

These checks are computational reproducibility aids. They do not replace the
mathematical arguments in the paper. The exact executable scope is recorded in
`docs/atlas/EXECUTABLE_REPLAY_SCOPE.md`.
