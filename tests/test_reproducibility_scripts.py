from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run_script(name: str) -> None:
    subprocess.run([sys.executable, str(ROOT / "scripts" / name)], cwd=ROOT, check=True)


def test_schema_check() -> None:
    run_script("run_atlas_schema_check.py")


def test_cf_bridge_replay() -> None:
    run_script("run_cf_bridge_replay.py")


def test_count_replay() -> None:
    run_script("run_atlas_count_replay.py")


def test_claim_class_audit() -> None:
    run_script("run_claim_class_audit.py")
