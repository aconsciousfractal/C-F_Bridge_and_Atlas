#!/usr/bin/env python3
"""Validate the curated relation-atlas JSON package.

This script is intentionally small and standard-library only.  It checks that
the public package contains the expected files and that each file exposes the
top-level keys used by the paper-facing replay scripts.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "relation_atlas"

EXPECTED = {
    "cf_theorem_transfer_registry_v1.json": {
        "registry_version",
        "allowed_claim_classes",
        "summary",
        "statements",
    },
    "cf_theorem_atlas_v2_package_manifest.json": {
        "artifact",
        "summary",
        "v2_core_artifacts",
        "v2_data_artifacts",
        "v2_supplements",
    },
    "cf_like_mobius_binomial_edge_scan_v1.json": {
        "artifact",
        "summary",
        "hits",
        "guardrails",
    },
    "cf_like_edge_watch_triage_v1.json": {
        "artifact",
        "summary",
        "decisions",
        "guardrails",
    },
    "cf_opposite_side_candidates.json": {
        "artifact",
        "summary",
        "candidates",
        "classifications",
    },
    "source_cartier_prime_power_metadata_v1.json": {
        "artifact",
        "summary",
        "edges",
        "guardrails",
    },
    "rowland_yassawi_fixed_modulus_theorem_certificates_v1.json": {
        "artifact",
        "summary",
        "certificates",
        "guardrails",
    },
}


def load_json(name: str) -> dict:
    path = DATA / name
    if not path.exists():
        raise SystemExit(f"missing required file: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main() -> int:
    checked: dict[str, list[str]] = {}
    for name, keys in EXPECTED.items():
        payload = load_json(name)
        missing = sorted(keys.difference(payload))
        if missing:
            raise SystemExit(f"{name}: missing keys {missing}")
        checked[name] = sorted(keys)

    print("atlas schema check: PASS")
    print(f"checked_files: {len(checked)}")
    for name in sorted(checked):
        print(f"- {name}: {', '.join(checked[name])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
