# Reproducing the C/F companion

## Environment

The replay and verification scripts use the Python standard library. `pytest`
is required only for the test suite and is declared explicitly:

```bash
python -m pip install -r requirements.txt
```

## Complete check

From the repository root:

```bash
python scripts/run_all_reproducibility_checks.py
```

This runs the seven scientific/package checks, thirteen pytest tests, and the
fail-closed package verifier. The command rewrites the canonical files under
`results/`; a clean release must reproduce them without semantic drift.

## Individual checks

```bash
python scripts/run_cf_bridge_replay.py
python scripts/run_atkin_lehner_w2_eta_multiplier_certificate.py
python scripts/run_chan_cooper_lucas_replay.py
python scripts/run_atlas_schema_check.py
python scripts/run_atlas_count_replay.py
python scripts/run_claim_class_audit.py
python scripts/run_public_repo_audit.py
python -m pytest -q
python scripts/verify_public_package.py
```

The main outputs are:

```text
results/cf_bridge_replay.json
results/atkin_lehner_w2_eta_multiplier_certificate.json
results/chan_cooper_lucas_replay.json
results/atlas_count_replay.json
results/claim_class_audit.json
```

`results/PUBLIC_ARTIFACTS.sha256` is the canonical LF-normalized SHA-256
inventory for every JSON under `data/relation_atlas/` and `results/`, excluding
the execution summary itself. Rebuild it only after an intentional artifact
change:

```bash
python scripts/make_public_manifest.py
python scripts/verify_public_package.py
```

## Building the paper

```bash
cd paper
pdflatex -interaction=nonstopmode -halt-on-error cf_bridge_relation_atlas.tex
bibtex cf_bridge_relation_atlas
pdflatex -interaction=nonstopmode -halt-on-error cf_bridge_relation_atlas.tex
pdflatex -interaction=nonstopmode -halt-on-error cf_bridge_relation_atlas.tex
```

The October package PDF has 16 pages. A valid build has no undefined references,
overfull boxes, or LaTeX errors.

The scripts provide bounded computational evidence. The paper contains the
mathematical proofs and controls the scope of every theorem-level statement.
