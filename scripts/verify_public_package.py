"""Fail-closed verification of the public C/F release package."""

from __future__ import annotations

import json
import re
from pathlib import Path, PurePosixPath
from urllib.parse import unquote

from make_public_manifest import MANIFEST, ROOT, artifact_paths, artifact_sha256
from run_atlas_count_replay import COUNT_SOURCES, EXPECTED as EXPECTED_COUNTS, assert_expected, compute_counts


LINE_RE = re.compile(r"^([0-9a-f]{64})  ([^\\]+)$")
PRIMARY_MARKDOWN = [
    "README.md",
    "README_REVIEWER.md",
    "REPRODUCE.md",
    "CLAIM_LEDGER.md",
    "PUBLIC_CLAIM_BOUNDARY.md",
    "docs/atlas/README.md",
    "docs/atlas/EXECUTABLE_REPLAY_SCOPE.md",
    "docs/atlas/RELATION_ATLAS_V2_PACKAGE_MANIFEST.md",
    "docs/atlas/CF_THEOREM_TRANSFER_REGISTRY_V2.md",
    "docs/atlas/CF_OPEN_PROBLEM_ATLAS_V2.md",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def parse_manifest() -> dict[str, str]:
    entries: dict[str, str] = {}
    for number, raw in enumerate(MANIFEST.read_text(encoding="utf-8").splitlines(), 1):
        match = LINE_RE.fullmatch(raw)
        if not match:
            raise ValueError(f"malformed manifest line {number}: {raw!r}")
        digest, rel = match.groups()
        posix = PurePosixPath(rel)
        if posix.is_absolute() or ":" in rel or ".." in posix.parts or rel.startswith("/"):
            raise ValueError(f"unsafe manifest path on line {number}: {rel!r}")
        if rel in entries:
            raise ValueError(f"duplicate manifest path: {rel}")
        entries[rel] = digest
    return entries


def verify_links() -> None:
    missing: list[tuple[str, str]] = []
    for rel in PRIMARY_MARKDOWN:
        source = ROOT / rel
        text = source.read_text(encoding="utf-8")
        for target in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", text):
            target = unquote(target.split("#", 1)[0].strip())
            if not target or re.match(r"^(?:https?://|mailto:)", target):
                continue
            if not (source.parent / target).resolve().exists():
                missing.append((rel, target))
    require(not missing, f"broken primary Markdown links: {missing}")


def assert_no_process_residue() -> None:
    paths = [ROOT / rel for rel in PRIMARY_MARKDOWN]
    paths.append(ROOT / "paper" / "cf_bridge_relation_atlas.tex")
    text = "\n".join(path.read_text(encoding="utf-8") for path in paths)
    patterns = {
        "workflow phase": r"\bphase(?:[-_ ]?\d)",
        "roadmap": r"\broadmap(?:\b|_)",
        "operational next-action field": r"next[_ -]?action",
        "private/internal provenance": r"\binternal\b|\bprivate\b",
        "stale publication history": r"after publication|paper is unchanged|no git tags",
        "local path": r"(?:[A-Z]:\\(?:Users|Repositories|tmp)\\|C:/Users/)",
        "agent metadata": r"\.codex|external[- ]agent",
        "external governance taxonomy": r"\bPAPP\b|Gate-Disciplined",
    }
    for label, pattern in patterns.items():
        require(re.search(pattern, text, re.IGNORECASE) is None, f"{label} remains in reader surface")


def main() -> int:
    entries = parse_manifest()
    expected = set(artifact_paths())
    require(
        set(entries) == expected,
        f"manifest inventory mismatch: missing={sorted(expected-set(entries))}, extra={sorted(set(entries)-expected)}",
    )

    artifacts: dict[str, object] = {}
    for rel in sorted(expected):
        path = ROOT / rel
        require(path.is_file(), f"missing artifact: {rel}")
        require(artifact_sha256(path) == entries[rel], f"SHA-256 mismatch for {rel}")
        artifacts[rel] = json.loads(path.read_text(encoding="utf-8"))

    bridge = artifacts["results/cf_bridge_replay.json"]
    require(bridge["status"] == "pass" and bridge["bad_count"] == 0, "C/F replay drifted")
    require(bridge["bound"] == 30 and bridge["checked_terms"] == 31, "C/F replay bound drifted")
    require(
        bridge["sample_hankel_determinants"]["C"] == bridge["sample_hankel_determinants"]["F"],
        "Hankel replay equality drifted",
    )

    chan = artifacts["results/chan_cooper_lucas_replay.json"]
    require(chan["status"] == "pass" and chan["sequence_count"] == 11, "Chan-Cooper replay drifted")

    w2 = artifacts["results/atkin_lehner_w2_eta_multiplier_certificate.json"]
    require(w2["status"] == "pass" and len(w2["factorizations"]) == 4, "W2 certificate drifted")

    count_result = artifacts["results/atlas_count_replay.json"]
    counts = compute_counts({PurePosixPath(rel).name: payload for rel, payload in artifacts.items() if rel.startswith("data/relation_atlas/")})
    require(count_result.get("status") == "pass", "count result status drifted")
    require(count_result.get("actual") == counts, "reported counts differ from current curated records")
    require(count_result.get("count_sources") == COUNT_SOURCES, "count provenance annotation drifted")
    for section in EXPECTED_COUNTS:
        assert_expected(section, counts[section])
    require(counts["registry"]["statement_count"] == 20, "registry count drifted")
    require(counts["registry"]["proved_in_paper_count"] == 3, "proved-in-paper count drifted")
    require(counts["manifest"]["total_public_registry_extension_rows"] == 18, "extension aggregate drifted")
    require(counts["edge_scan"]["checked_transform_count"] == 17684, "edge-scan count drifted")
    require(counts["watch_triage"]["closed_known_metadata_count"] == 8, "edge classification drifted")
    require(counts["rowland_yassawi"]["certificate_count"] == 6, "RY certificate count drifted")

    audit = artifacts["results/claim_class_audit.json"]
    require(audit == {"status": "pass", "failures": []}, "claim-class audit drifted")

    registry = artifacts["data/relation_atlas/cf_theorem_transfer_registry_v1.json"]
    require("proved_in_paper" in registry["allowed_claim_classes"], "public theorem class missing")
    require("closed_internal_result" not in registry["allowed_claim_classes"], "obsolete theorem class remains")
    require(all("scope_note" in row for row in registry["statements"]), "registry scope note missing")
    require(all("next_action" not in row for row in registry["statements"]), "operational next_action remains")

    ledger = (ROOT / "CLAIM_LEDGER.md").read_text(encoding="utf-8")
    for claim_id in ("CF-C1", "CF-C2", "CF-C3", "CF-C4", "CF-O1"):
        require(claim_id in ledger, f"claim ledger ID missing: {claim_id}")

    citation = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    require('version: "1.0.1"' in citation, "CITATION.cff version drifted")
    require(re.search(r"^\s*date-released\s*:", citation, re.MULTILINE) is None, "CITATION.cff invents a release date")
    require("https://orcid.org/0009-0001-6176-6208" in citation, "ORCID missing")

    verify_links()
    assert_no_process_residue()
    print(f"ALL CHECKS PASSED ({len(entries)} JSON artifacts; counts, claims, links, hashes, and reader surface checked)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
