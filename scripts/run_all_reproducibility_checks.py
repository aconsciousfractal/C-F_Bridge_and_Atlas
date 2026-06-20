#!/usr/bin/env python3
"""Run the public reproducibility checks in sequence."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"

CHECKS = [
    "run_cf_bridge_replay.py",
    "run_atkin_lehner_w2_eta_multiplier_certificate.py",
    "run_chan_cooper_lucas_replay.py",
    "run_atlas_schema_check.py",
    "run_atlas_count_replay.py",
    "run_claim_class_audit.py",
    "run_public_repo_audit.py",
]


def main() -> int:
    for script in CHECKS:
        print(f"\n== {script} ==")
        subprocess.run([sys.executable, str(SCRIPTS / script)], cwd=ROOT, check=True)
    print("\nall reproducibility checks: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
