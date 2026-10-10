"""Hostile metadata checks; no originating scan or external replay is run."""

from copy import deepcopy
import importlib.util
import json
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("atlas_count_guardrails", ROOT / "scripts" / "run_atlas_count_replay.py")
COUNTS = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(COUNTS)


@pytest.fixture
def october():
    return json.loads((ROOT / "data" / "relation_atlas" / COUNTS.OCTOBER).read_text(encoding="utf-8"))


def test_omitted_smith_row_is_rejected(october):
    payload = deepcopy(october)
    payload["statements"] = []
    with pytest.raises(ValueError, match="exactly one Smith"):
        COUNTS.replay_extension(payload, october=True)


def test_duplicate_statement_id_is_rejected(october):
    payload = deepcopy(october)
    payload["statements"].append(deepcopy(payload["statements"][0]))
    with pytest.raises(ValueError, match="duplicate statement_id"):
        COUNTS.replay_extension(payload, october=True)


def test_altered_class_and_status_are_rejected(october):
    for field, value in (("claim_level", "closed_metadata"), ("status", "closed_metadata")):
        payload = deepcopy(october)
        payload["statements"][0][field] = value
        with pytest.raises(ValueError):
            COUNTS.replay_extension(payload, october=True)


def test_false_summary_is_rejected(october):
    payload = deepcopy(october)
    payload["summary"]["extension_statement_count"] = 2
    with pytest.raises(ValueError, match="summary extension_statement_count"):
        COUNTS.replay_extension(payload, october=True)
    payloads = {
        path.name: json.loads(path.read_text(encoding="utf-8"))
        for path in (ROOT / "data" / "relation_atlas").glob("*.json")
    }
    payloads["cf_theorem_atlas_v2_package_manifest.json"]["summary"]["total_public_registry_extension_rows"] = 19
    with pytest.raises(ValueError, match="summary total_public_registry_extension_rows"):
        COUNTS.compute_counts(payloads)


def test_empty_classes_and_guardrails_are_rejected(october):
    for field in ("allowed_claim_classes", "guardrails"):
        payload = deepcopy(october)
        payload[field] = []
        with pytest.raises(ValueError):
            COUNTS.replay_extension(payload, october=True)
