# Build Notes

Build from this directory:

```bash
pdflatex -interaction=nonstopmode -halt-on-error cf_bridge_relation_atlas.tex
bibtex cf_bridge_relation_atlas
pdflatex -interaction=nonstopmode -halt-on-error cf_bridge_relation_atlas.tex
pdflatex -interaction=nonstopmode -halt-on-error cf_bridge_relation_atlas.tex
```

Expected output:

```text
cf_bridge_relation_atlas.pdf
```

The current unified-folder build succeeded with BibTeX and no undefined
references or citations:

```text
cf_bridge_relation_atlas.pdf: 16 pages
log scan: no undefined references/citations, no overfull/underfull warnings
```

MiKTeX may emit local update/log warnings depending on the machine; those are
environment-level warnings, not paper failures.

Before public release, run a build from a clean clone or clean exported folder,
not only from the current working tree.
