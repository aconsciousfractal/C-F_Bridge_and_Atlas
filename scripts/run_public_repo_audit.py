#!/usr/bin/env python3
"""Audit public links, package paths, and forbidden local/process residue."""

from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
TEXT_EXTENSIONS = {".bib", ".cff", ".json", ".md", ".py", ".tex", ".txt", ".yml", ".yaml"}
BAD_PATTERNS = [
    re.compile(r"(?:[A-Z]:\\(?:Users|Repositories|tmp)\\|C:/Users/)", re.IGNORECASE),
    re.compile(r"GitHub_puba|public_companion_staging|paper_ab", re.IGNORECASE),
    re.compile(r"docs/05_relation_atlas|projects/Apery|scripts/cf_like_edge_watch_triage\.py"),
    re.compile(r"\bPAPP\b|Gate-Disciplined", re.IGNORECASE),
    re.compile(r"\bphase(?:[-_ ]?\d)|\broadmap(?:\b|_)|next[_ -]?action", re.IGNORECASE),
    re.compile(r"\binternal\b|\bprivate\b", re.IGNORECASE),
    re.compile(r"after publication|paper is unchanged|no git tags", re.IGNORECASE),
    re.compile(r"\.codex|external[- ]agent", re.IGNORECASE),
]
ALLOWLIST = {
    Path("scripts/run_public_repo_audit.py"),
    Path("scripts/verify_public_package.py"),
}
PATH_PREFIXES = ("data/", "docs/", "paper/", "results/", "scripts/", "tests/")


def check_historical_external_references() -> list[str]:
    """Unavailable historical outputs are explicit exclusions, never delivered files."""
    data = ROOT / "data" / "relation_atlas"
    overlay = json.loads((data / "cf_theorem_transfer_registry_2026_10_extension.json").read_text(encoding="utf-8"))
    excluded = overlay["historical_external_references"]
    failures: list[str] = []
    if len(excluded) != 24 or len(set(excluded)) != 24:
        failures.append("historical exclusion inventory must contain exactly 24 unique references")
    found: set[str] = set()

    def walk(value: object) -> list[str]:
        if isinstance(value, dict):
            return [p for item in value.values() for p in walk(item)]
        if isinstance(value, list):
            return [p for item in value for p in walk(item)]
        return [value] if isinstance(value, str) and value.startswith("outputs/") else []

    for path in data.glob("*.json"):
        if path.name == "cf_theorem_transfer_registry_2026_10_extension.json":
            continue
        refs = set(walk(json.loads(path.read_text(encoding="utf-8"))))
        if refs and path.name not in {"source_cartier_prime_power_metadata_v1.json", "rowland_yassawi_fixed_modulus_theorem_certificates_v1.json"}:
            failures.append(f"undeclared historical output category: {path.name}")
        found.update(refs)
    if found != set(excluded):
        failures.append("historical external-reference inventory differs from received records")
    for ref in excluded:
        if not ref.startswith("outputs/_validation/") or ".." in Path(ref).parts or ":" in ref:
            failures.append(f"unsafe historical reference: {ref}")
    return failures


def rel(path: Path) -> Path:
    return path.relative_to(ROOT)


def iter_text_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or "__pycache__" in path.parts:
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
    return json.loads(path.read_text(encoding="utf-8"))


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
    return [path for path in sorted(set(iter_manifest_paths(load_manifest()))) if not (ROOT / path).exists()]


def check_markdown_links() -> list[str]:
    failures: list[str] = []
    for source in ROOT.rglob("*.md"):
        if ".git" in source.parts:
            continue
        text = source.read_text(encoding="utf-8")
        for target in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", text):
            target = unquote(target.split("#", 1)[0].strip())
            if not target or re.match(r"^(?:https?://|mailto:)", target):
                continue
            if not (source.parent / target).resolve().exists():
                failures.append(f"{rel(source)} -> {target}")
    return failures


def check_json_syntax() -> list[str]:
    failures: list[str] = []
    for path in sorted((ROOT / "data" / "relation_atlas").glob("*.json")):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            failures.append(f"{rel(path)}: {exc}")
    return failures


def main() -> int:
    failures = {
        "forbidden residue": scan_for_bad_patterns(),
        "missing manifest paths": check_manifest_paths(),
        "broken Markdown links": check_markdown_links(),
        "invalid JSON": check_json_syntax(),
        "historical external references": check_historical_external_references(),
    }
    active = {label: items for label, items in failures.items() if items}
    if active:
        for label, items in active.items():
            print(f"{label}:")
            for item in items:
                print(f"- {item}")
        raise SystemExit(1)

    print("public repo audit: PASS")
    print(f"checked_text_files: {len(iter_text_files())}")
    print(f"checked_manifest_paths: {len(set(iter_manifest_paths(load_manifest())))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
