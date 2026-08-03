"""Build the canonical SHA-256 inventory for public JSON artifacts."""

from __future__ import annotations

import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "results" / "PUBLIC_ARTIFACTS.sha256"
EXCLUDED = {"results/public_reproducibility_check.json"}


def artifact_paths() -> list[str]:
    paths: list[str] = []
    for directory in (ROOT / "data" / "relation_atlas", ROOT / "results"):
        for path in directory.rglob("*.json"):
            rel = path.relative_to(ROOT).as_posix()
            if rel not in EXCLUDED:
                paths.append(rel)
    return sorted(paths)


def canonical_bytes(path: Path) -> bytes:
    return path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def artifact_sha256(path: Path) -> str:
    return hashlib.sha256(canonical_bytes(path)).hexdigest()


def main() -> int:
    lines = [f"{artifact_sha256(ROOT / rel)}  {rel}" for rel in artifact_paths()]
    MANIFEST.write_bytes(("\n".join(lines) + "\n").encode("utf-8"))
    print(f"Manifest written: {MANIFEST.relative_to(ROOT)}")
    print(f"Artifacts: {len(lines)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
