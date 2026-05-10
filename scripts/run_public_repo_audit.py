#!/usr/bin/env python3
"""Audit that the public companion does not cite missing development paths."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXT_EXTENSIONS = {".bib", ".cff", ".json", ".md", ".py", ".tex", ".txt", ".yml", ".yaml"}
BAD_PATTERNS = [
    re.compile(r"P:\\\\", re.IGNORECASE),
    re.compile(r"GitHub_puba", re.IGNORECASE),
    re.compile(r"\bPAPP\b", re.IGNORECASE),
    re.compile(r"public_companion_staging", re.IGNORECASE),
    re.compile(r"paper_ab", re.IGNORECASE),
    re.compile(r"docs/05_relation_atlas"),
    re.compile(r"projects/Apery"),
    re.compile(r"scripts/cf_like_edge_watch_triage\.py"),
]
ALLOWLIST = {
    Path("scripts/run_public_repo_audit.py"),
}
PATH_PREFIXES = ("data/", "docs/", "paper/", "results/", "scripts/", "tests/")


def rel(path: Path) -> Path:
    return path.relative_to(ROOT)


def iter_text_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        parts = set(path.parts)
        if ".git" in parts or "__pycache__" in parts:
            continue
        if path.suffix.lower() in TEXT_EXTENSIONS:
            files.append(path)
    return files


def scan_for_bad_patterns() -> list[str]:
    failures: list[str] = []
    for path in iter_text_files():
        rpath = rel(path)
        if rpath in ALLOWLIST:
            continue
        text = path.read_text(encoding="utf-8")
        for lineno, line in enumerate(text.splitlines(), 1):
            for pattern in BAD_PATTERNS:
                if pattern.search(line):
                    failures.append(f"{rpath}:{lineno}: {pattern.pattern}: {line.strip()}")
    return failures


def load_manifest() -> dict:
    path = ROOT / "data" / "relation_atlas" / "cf_theorem_atlas_v2_package_manifest.json"
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def iter_manifest_paths(payload: object) -> list[str]:
    paths: list[str] = []
    if isinstance(payload, dict):
        for value in payload.values():
            paths.extend(iter_manifest_paths(value))
    elif isinstance(payload, list):
        for value in payload:
            paths.extend(iter_manifest_paths(value))
    elif isinstance(payload, str) and payload.startswith(PATH_PREFIXES):
        paths.append(payload)
    return paths


def check_manifest_paths() -> list[str]:
    failures: list[str] = []
    for public_path in sorted(set(iter_manifest_paths(load_manifest()))):
        if not (ROOT / public_path).exists():
            failures.append(public_path)
    return failures


def main() -> int:
    bad_patterns = scan_for_bad_patterns()
    missing_paths = check_manifest_paths()

    if bad_patterns or missing_paths:
        if bad_patterns:
            print("stale internal references:")
            for failure in bad_patterns:
                print(f"- {failure}")
        if missing_paths:
            print("missing manifest paths:")
            for failure in missing_paths:
                print(f"- {failure}")
        raise SystemExit(1)

    print("public repo audit: PASS")
    print(f"checked_text_files: {len(iter_text_files())}")
    print(f"checked_manifest_paths: {len(set(iter_manifest_paths(load_manifest())))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())