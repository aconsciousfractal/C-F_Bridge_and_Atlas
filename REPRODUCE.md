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
python scripts/run_atlas_schema_check.py
python scripts/run_atlas_count_replay.py
python scripts/run_claim_class_audit.py
```

The scripts use only the Python standard library.  Successful runs write:

```text
results/cf_bridge_replay.json
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

These checks are computational reproducibility aids.  They do not replace the
mathematical arguments in the paper.
