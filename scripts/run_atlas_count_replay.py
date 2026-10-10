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
        "proved_in_paper_count": 3,
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
        "v2_base_supplement_count": 11,
        "extension_2026_06_20_count": 6,
        "extension_2026_10_10_count": 1,
        "total_public_registry_extension_rows": 18,
        "finite_edge_input_watch_rows": 8,
        "finite_edge_closed_known_metadata_rows": 8,
        "finite_edge_still_watch_rows": 0,
        "finite_edge_new_theorem_edges": 0,
        "finite_edge_new_proof_obligations": 0,
        "active_or_blocked_open_problem_count_at_v2_freeze": 6,
        "post_sun_3_5_active_or_blocked_open_problem_count": 4,
        "closed_or_reconciled_open_problem_count": 4,
        "ry_level2a_fixed_modulus_certificate_count": 6,
        "ry_level2b_status": "open",
    },
    "extension_registry": {
        "extension_statement_count": 6,
        "proved_in_paper_count": 3,
        "closed_metadata_count": 3,
        "theorem_transfer_edge_count": 0,
    },
    "extension_registry_2026_10": {
        "extension_statement_count": 1,
        "proved_in_paper_count": 1,
        "closed_metadata_count": 0,
        "theorem_transfer_edge_count": 0,
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

JUNE = "cf_theorem_transfer_registry_2026_06_extension.json"
OCTOBER = "cf_theorem_transfer_registry_2026_10_extension.json"
ADDENDA = [f"data/relation_atlas/{name}" for name in (JUNE, OCTOBER)]
SMITH_ID = "cf_integral_hankel_smith_transport"
BASE_SUPPLEMENTS = {
    "docs/atlas/CF_THEOREM_ATLAS_V2_READOUT.md",
    "docs/atlas/CF_THEOREM_TRANSFER_REGISTRY_V2.md",
    "docs/atlas/CF_OPEN_PROBLEM_ATLAS_V2.md",
    "docs/atlas/CF_LIKE_EDGE_WATCH_TRIAGE_V1.md",
    "docs/atlas/SUN_3_5_SEPARATE_PAPER_STATUS_UPDATE.md",
    "docs/atlas/EXECUTABLE_REPLAY_SCOPE.md",
    "data/relation_atlas/cf_theorem_transfer_registry_v1.json",
    "data/relation_atlas/cf_like_edge_watch_triage_v1.json",
    "data/relation_atlas/cf_opposite_side_candidates.json",
    "data/relation_atlas/source_cartier_prime_power_metadata_v1.json",
    "data/relation_atlas/rowland_yassawi_fixed_modulus_theorem_certificates_v1.json",
}

# Recounting metadata is not rerunning the originating scan or automata.
COUNT_SOURCES = {
    "registry": "statement records recounted",
    "extension_registry": "June statement records recounted",
    "extension_registry_2026_10": "October statement records recounted",
    "manifest": "11 artifact units + 6 June statements + 1 October statement; remaining freeze summaries inherited; aggregate is not a theorem count",
    "edge_scan": "hit classifications and promotion statuses recounted; checked_transform_count and bounded_negative_count inherited from received scan summary; no scan rerun",
    "watch_triage": "decision records recounted",
    "opposite_side": "candidate records, classifications and high_value flags recounted",
    "cartier_metadata": "edge records and stored build_replay.bad_count recounted; raw automaton payloads not replayed",
    "rowland_yassawi": "certificate records recounted; replay_bad_count inherited from received summary because not all raw certificate/replay payloads are present",
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


def compare_summary(payload: dict[str, Any], actual: dict[str, Any], name: str) -> None:
    for key, value in actual.items():
        if payload["summary"].get(key) != value:
            raise ValueError(f"{name}: summary {key} does not match record recount")


def validate_statements(payload: dict[str, Any], name: str) -> None:
    allowed = payload.get("allowed_claim_classes")
    if not isinstance(allowed, list) or not allowed or any(not isinstance(x, str) or not x.strip() for x in allowed):
        raise ValueError(f"{name}: allowed_claim_classes must be nonempty")
    if len(set(allowed)) != len(allowed):
        raise ValueError(f"{name}: duplicate allowed claim class")
    rows = payload.get("statements")
    if not isinstance(rows, list):
        raise ValueError(f"{name}: statements must be a list")
    identifiers = [row.get("statement_id") for row in rows]
    if any(not isinstance(sid, str) or not sid.strip() for sid in identifiers) or len(set(identifiers)) != len(identifiers):
        raise ValueError(f"{name}: missing or duplicate statement_id")
    if any(row.get("claim_level") not in allowed for row in rows):
        raise ValueError(f"{name}: claim_level outside allowed_claim_classes")


def replay_extension(payload: dict[str, Any], *, october: bool = False) -> dict[str, int]:
    name = OCTOBER if october else JUNE
    validate_statements(payload, name)
    rows = payload["statements"]
    guardrails = payload.get("guardrails")
    if not isinstance(guardrails, list) or not guardrails or any(not isinstance(g, str) or not g.strip() for g in guardrails):
        raise ValueError(f"{name}: nonempty guardrails required")
    if any(not isinstance(row.get("guardrail"), str) or not row["guardrail"].strip() for row in rows):
        raise ValueError(f"{name}: statement guardrail required")
    if october:
        if len(rows) != 1 or rows[0].get("statement_id") != SMITH_ID:
            raise ValueError(f"{name}: exactly one Smith transport statement required")
        row = rows[0]
        if payload["allowed_claim_classes"] != ["proved_in_paper"] or row.get("claim_level") != "proved_in_paper" or row.get("status") != "proved_in_paper":
            raise ValueError(f"{name}: Smith transport class/status must be proved_in_paper")
        if not all(token in row["guardrail"].lower() for token in ("ordinary", "unimodular", "equality_not_classification")):
            raise ValueError(f"{name}: Smith transport scope guardrail incomplete")
    levels = Counter(row["claim_level"] for row in rows)
    actual = {
        "extension_statement_count": len(rows),
        "proved_in_paper_count": levels["proved_in_paper"],
        "closed_metadata_count": levels["closed_metadata"],
        "theorem_transfer_edge_count": levels["conditional_theorem_transfer"],
    }
    compare_summary(payload, actual, name)
    return actual


def replay_registry(payload: dict[str, Any]) -> dict[str, Any]:
    validate_statements(payload, "V1 registry")
    levels = Counter(row["claim_level"] for row in payload["statements"])
    actual = {
        "statement_count": len(payload["statements"]),
        "proved_in_paper_count": levels["proved_in_paper"],
        "conditional_transfer_count": levels["conditional_theorem_transfer"],
        "source_attached_conjecture_count": levels["source_attached_conjecture"],
        "theorem_import_by_reference_count": levels["theorem_import_by_reference"],
        "finite_exact_replay_count": levels["finite_exact_replay"],
        "proof_obligation_count": levels["proof_obligation"] + levels["explicit_automaton_metadata"],
        "blocked_count": levels["blocked"],
        "watch_count": levels["watch"],
        "explicit_automaton_metadata_count": levels["explicit_automaton_metadata"],
    }
    compare_summary(payload, {key: actual[key] for key in EXPECTED["registry"]}, "V1 registry")
    return actual


def replay_edge_scan(payload: dict[str, Any]) -> dict[str, Any]:
    classifications = Counter(hit["classification"] for hit in payload["hits"])
    summary = payload["summary"]
    return {
        "checked_transform_count": summary["checked_transform_count"],
        "hit_count": len(payload["hits"]),
        "known_hit_count": classifications["already_known_in_atlas"],
        "watch_hit_count": classifications["watch"],
        "new_promoted_edge_count": sum(hit["promotion_status"] != "not_promoted" for hit in payload["hits"]),
        "bounded_negative_count": summary["bounded_negative_count"],
    }


def compute_counts(payloads: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
    """Recount the supplied curated records, without external scientific replay."""
    registry = replay_registry(payloads["cf_theorem_transfer_registry_v1.json"])
    june = replay_extension(payloads[JUNE])
    october = replay_extension(payloads[OCTOBER], october=True)
    scan_payload = payloads["cf_like_mobius_binomial_edge_scan_v1.json"]
    scan = replay_edge_scan(scan_payload)
    compare_summary(scan_payload, scan, "edge scan")
    triage_payload = payloads["cf_like_edge_watch_triage_v1.json"]
    decisions = Counter(row["decision"] for row in triage_payload["decisions"])
    triage = {"closed_known_metadata_count": decisions["closed_known_metadata"], "still_watch_count": decisions["watch"]}
    compare_summary(triage_payload, triage, "watch triage")
    if dict(decisions) != triage_payload["summary"].get("decision_counts"):
        raise ValueError("watch triage: decision classifications differ from summary")
    triage.update({"decision_count": len(triage_payload["decisions"]), "decision_counts": dict(decisions)})
    opposite_payload = payloads["cf_opposite_side_candidates.json"]
    candidates = opposite_payload["candidates"]
    opposite = {"candidate_count": len(candidates), "high_value_candidate_count": sum(row["high_value"] is True for row in candidates)}
    compare_summary(opposite_payload, opposite, "opposite side")
    classifications = Counter(row["classification"] for row in candidates)
    if dict(classifications) != opposite_payload["summary"].get("classification_counts"):
        raise ValueError("opposite side: classifications differ from summary")
    opposite["classification_counts"] = dict(classifications)
    cartier_payload = payloads["source_cartier_prime_power_metadata_v1.json"]
    cartier = {"edge_count": len(cartier_payload["edges"]), "build_bad_count": sum(row["build_replay"]["bad_count"] for row in cartier_payload["edges"])}
    compare_summary(cartier_payload, cartier, "Cartier metadata")
    ry_payload = payloads["rowland_yassawi_fixed_modulus_theorem_certificates_v1.json"]
    ry = {"certificate_count": len(ry_payload["certificates"]), "replay_bad_count": ry_payload["summary"]["replay_bad_count"]}
    compare_summary(ry_payload, ry, "RY certificates")
    manifest_payload = payloads["cf_theorem_atlas_v2_package_manifest.json"]
    base = manifest_payload["v2_base_supplement_artifacts"]
    addenda = manifest_payload["current_addenda"]
    supplements = manifest_payload["v2_supplements"]
    if len(base) != 11 or len(set(base)) != len(base) or set(base) != BASE_SUPPLEMENTS:
        raise ValueError("manifest: base supplement inventory differs from the eleven antecedent artifact units")
    if addenda != ADDENDA or set(base).intersection(addenda):
        raise ValueError("manifest: current addenda or base/addendum separation drifted")
    if len(supplements) != 12 or len(set(supplements)) != len(supplements) or set(supplements) != BASE_SUPPLEMENTS | {ADDENDA[0]}:
        raise ValueError("manifest: frozen v2_supplements inventory drifted")
    manifest = dict(manifest_payload["summary"])
    recounted = {
        "base_registry_statement_count": registry["statement_count"],
        "v2_supplement_count": len(base),
        "v2_base_supplement_count": len(base),
        "extension_2026_06_20_count": june["extension_statement_count"],
        "extension_2026_10_10_count": october["extension_statement_count"],
        "total_public_registry_extension_rows": len(base) + june["extension_statement_count"] + october["extension_statement_count"],
        "finite_edge_input_watch_rows": scan["watch_hit_count"],
        "finite_edge_closed_known_metadata_rows": triage["closed_known_metadata_count"],
        "finite_edge_still_watch_rows": triage["still_watch_count"],
        "finite_edge_new_theorem_edges": scan["new_promoted_edge_count"],
        "ry_level2a_fixed_modulus_certificate_count": ry["certificate_count"],
    }
    compare_summary(manifest_payload, recounted, "manifest")
    manifest.update(recounted)
    return {"registry": registry, "manifest": manifest, "extension_registry": june, "extension_registry_2026_10": october, "edge_scan": scan, "watch_triage": triage, "opposite_side": opposite, "cartier_metadata": cartier, "rowland_yassawi": ry}


def main() -> int:
    actual = compute_counts({path.name: load_json(path.name) for path in DATA.glob("*.json")})

    for section in EXPECTED:
        assert_expected(section, actual[section])

    RESULTS.mkdir(exist_ok=True)
    out = RESULTS / "atlas_count_replay.json"
    with out.open("w", encoding="utf-8") as handle:
        json.dump({"status": "pass", "actual": actual, "count_sources": COUNT_SOURCES}, handle, indent=2, sort_keys=True)
        handle.write("\n")

    print("atlas count replay: PASS")
    print(f"wrote: {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
