#!/usr/bin/env python3
"""Replay paper-facing counts from the curated JSON package."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "relation_atlas"
RESULTS = ROOT / "results"


EXPECTED = {
    "registry": {
        "statement_count": 20,
        "closed_internal_result_count": 3,
        "conditional_transfer_count": 6,
        "source_attached_conjecture_count": 1,
        "theorem_import_by_reference_count": 5,
        "finite_exact_replay_count": 1,
        "proof_obligation_count": 2,
        "blocked_count": 2,
        "watch_count": 0,
    },
    "manifest": {
        "base_registry_statement_count": 20,
        "v2_supplement_count": 11,
        "phase7_input_watch_rows": 8,
        "phase7_closed_known_metadata_rows": 8,
        "phase7_still_watch_rows": 0,
        "phase7_new_theorem_edges": 0,
        "phase7_new_proof_obligations": 0,
        "active_or_blocked_open_problem_count": 6,
        "closed_or_reconciled_open_problem_count": 4,
        "ry_level2a_fixed_modulus_certificate_count": 6,
        "ry_level2b_status": "open",
    },
    "edge_scan": {
        "checked_transform_count": 17684,
        "hit_count": 12,
        "known_hit_count": 4,
        "watch_hit_count": 8,
        "new_promoted_edge_count": 0,
        "bounded_negative_count": 17672,
    },
    "watch_triage": {
        "closed_known_metadata_count": 8,
        "still_watch_count": 0,
    },
    "opposite_side": {
        "candidate_count": 20,
        "high_value_candidate_count": 14,
    },
    "cartier_metadata": {
        "edge_count": 6,
        "build_bad_count": 0,
    },
    "rowland_yassawi": {
        "certificate_count": 6,
        "replay_bad_count": 0,
    },
}


def load_json(name: str) -> dict[str, Any]:
    with (DATA / name).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def assert_expected(section: str, actual: dict[str, Any]) -> None:
    expected = EXPECTED[section]
    mismatches = {
        key: {"expected": value, "actual": actual.get(key)}
        for key, value in expected.items()
        if actual.get(key) != value
    }
    if mismatches:
        formatted = json.dumps(mismatches, indent=2, sort_keys=True)
        raise SystemExit(f"{section}: count mismatch\n{formatted}")


def replay_registry(payload: dict[str, Any]) -> dict[str, Any]:
    levels = Counter(row["claim_level"] for row in payload["statements"])
    return {
        "statement_count": len(payload["statements"]),
        "closed_internal_result_count": levels["closed_internal_result"],
        "conditional_transfer_count": levels["conditional_theorem_transfer"],
        "source_attached_conjecture_count": levels["source_attached_conjecture"],
        "theorem_import_by_reference_count": levels["theorem_import_by_reference"],
        "finite_exact_replay_count": levels["finite_exact_replay"],
        "proof_obligation_count": levels["proof_obligation"] + levels["explicit_automaton_metadata"],
        "blocked_count": levels["blocked"],
        "watch_count": levels["watch"],
        "explicit_automaton_metadata_count": levels["explicit_automaton_metadata"],
    }


def replay_edge_scan(payload: dict[str, Any]) -> dict[str, Any]:
    classifications = Counter(hit["classification"] for hit in payload["hits"])
    summary = payload["summary"]
    return {
        "checked_transform_count": summary["checked_transform_count"],
        "hit_count": len(payload["hits"]),
        "known_hit_count": classifications["already_known_in_atlas"],
        "watch_hit_count": classifications["watch"],
        "new_promoted_edge_count": summary["new_promoted_edge_count"],
        "bounded_negative_count": summary["bounded_negative_count"],
    }


def main() -> int:
    actual = {
        "registry": replay_registry(load_json("cf_theorem_transfer_registry_v1.json")),
        "manifest": load_json("cf_theorem_atlas_v2_package_manifest.json")["summary"],
        "edge_scan": replay_edge_scan(load_json("cf_like_mobius_binomial_edge_scan_v1.json")),
        "watch_triage": load_json("cf_like_edge_watch_triage_v1.json")["summary"],
        "opposite_side": load_json("cf_opposite_side_candidates.json")["summary"],
        "cartier_metadata": load_json("source_cartier_prime_power_metadata_v1.json")["summary"],
        "rowland_yassawi": load_json(
            "rowland_yassawi_fixed_modulus_theorem_certificates_v1.json"
        )["summary"],
    }

    for section in EXPECTED:
        assert_expected(section, actual[section])

    RESULTS.mkdir(exist_ok=True)
    out = RESULTS / "atlas_count_replay.json"
    with out.open("w", encoding="utf-8") as handle:
        json.dump({"status": "pass", "actual": actual}, handle, indent=2, sort_keys=True)
        handle.write("\n")

    print("atlas count replay: PASS")
    print(f"wrote: {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
