#!/usr/bin/env python3
"""Audit claim-class guardrails for the public relation-atlas package."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "relation_atlas"
RESULTS = ROOT / "results"

NON_PROOF_LEVELS = {
    "finite_exact_replay",
    "source_attached_conjecture",
    "proof_obligation",
    "blocked",
    "watch",
    "explicit_automaton_metadata",
    "closed_known_metadata",
    "closed_metadata",
}

PROOFISH_STATUSES = {
    "closed_internal_result",
    "theorem_import_by_reference",
    "conditional_theorem_transfer",
}


def load_json(name: str) -> dict[str, Any]:
    with (DATA / name).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def audit_claim_level_membership(name: str) -> list[str]:
    payload = load_json(name)
    allowed = set(payload.get("allowed_claim_classes", []))
    failures: list[str] = []
    if not allowed:
        return failures
    for row in payload.get("statements", []):
        sid = row.get("statement_id")
        level = row.get("claim_level")
        if level not in allowed:
            failures.append(f"{name}:{sid}: claim_level {level} not in allowed_claim_classes")
    return failures


def audit_registry() -> list[str]:
    payload = load_json("cf_theorem_transfer_registry_v1.json")
    failures: list[str] = []
    for row in payload["statements"]:
        level = row.get("claim_level")
        status = row.get("status")
        sid = row.get("statement_id")
        if level in NON_PROOF_LEVELS and status in PROOFISH_STATUSES:
            failures.append(f"{sid}: non-proof claim_level {level} has proof-like status {status}")
        if level == "finite_exact_replay" and "proof" in str(row.get("cf_role", "")).lower():
            failures.append(f"{sid}: finite_exact_replay role uses proof language")
        if level == "source_attached_conjecture" and "prove" not in str(row.get("proof_obligation", "")).lower():
            failures.append(f"{sid}: conjecture row lacks explicit proof obligation")
    return failures


def audit_edge_scan() -> list[str]:
    payload = load_json("cf_like_mobius_binomial_edge_scan_v1.json")
    failures: list[str] = []
    for index, hit in enumerate(payload["hits"], start=1):
        if hit.get("classification") == "watch" and hit.get("promotion_status") != "not_promoted":
            failures.append(f"edge hit {index}: watch row was promoted")
        if hit.get("classification") == "already_known_in_atlas" and hit.get("promotion_status") != "not_promoted":
            failures.append(f"edge hit {index}: known metadata row was promoted")
    if payload["summary"].get("new_promoted_edge_count") != 0:
        failures.append("edge scan summary reports promoted theorem edges")
    return failures


def audit_watch_triage() -> list[str]:
    payload = load_json("cf_like_edge_watch_triage_v1.json")
    failures: list[str] = []
    for decision in payload["decisions"]:
        if decision.get("decision") != "closed_known_metadata":
            failures.append(f"{decision.get('edge_id')}: unexpected triage decision")
        if decision.get("claim_level") != "closed_known_metadata":
            failures.append(f"{decision.get('edge_id')}: unexpected claim level")
    return failures


def main() -> int:
    failures = (
        audit_claim_level_membership("cf_theorem_transfer_registry_v1.json")
        + audit_claim_level_membership("cf_theorem_transfer_registry_2026_06_extension.json")
        + audit_registry()
        + audit_edge_scan()
        + audit_watch_triage()
    )

    RESULTS.mkdir(exist_ok=True)
    out = RESULTS / "claim_class_audit.json"
    with out.open("w", encoding="utf-8") as handle:
        json.dump({"status": "pass" if not failures else "fail", "failures": failures}, handle, indent=2)
        handle.write("\n")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        raise SystemExit(f"claim class audit failed with {len(failures)} issue(s)")

    print("claim class audit: PASS")
    print(f"wrote: {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
