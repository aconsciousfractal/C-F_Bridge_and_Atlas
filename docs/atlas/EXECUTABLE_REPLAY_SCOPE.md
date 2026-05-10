# Executable Replay Scope

This public companion has two roles:

1. It provides executable sanity checks for the finite coefficient identities and
   the curated relation-atlas metadata used by the paper.
2. It records the claim discipline of the atlas in machine-readable JSON.

The replay scripts are deliberately small, standard-library Python programs.
They are reproducibility aids, not replacements for the mathematical proofs in
the paper.

## Included Executable Checks

| command | purpose |
| --- | --- |
| `python scripts/run_cf_bridge_replay.py` | replays the finite C/F bridge coefficient identities over the public prime range |
| `python scripts/run_atlas_schema_check.py` | validates required JSON keys for the curated atlas package |
| `python scripts/run_atlas_count_replay.py` | replays the public atlas count summaries |
| `python scripts/run_claim_class_audit.py` | checks allowed claim classes and known guardrails |
| `python scripts/run_public_repo_audit.py` | checks that public docs/data do not cite missing development paths |

## Not Included As Executable Proof Certificates

The paper contains mathematical proofs for the C/F bridge theorem and discusses
atlas theorem-transfer metadata.  This companion does not currently include a
full modular-form q-expansion/Sturm/valence proof certificate, nor a complete
Rowland-Yassawi all-good-primes/all-alpha automaton archive.  Those items are
outside the scope of this curated public package unless archived separately.

The absence of those larger certificates is reflected in the atlas guardrails:
finite replay and fixed-modulus metadata are not promoted to new theorem-transfer
proofs by themselves.