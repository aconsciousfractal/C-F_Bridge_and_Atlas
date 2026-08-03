#!/usr/bin/env python3
"""Run the public reproducibility checks in sequence."""

from __future__ import annotations

import subprocess
import sys
import json
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
    commands: list[dict[str, object]] = []
    for script in CHECKS:
        print(f"\n== {script} ==")
        command = [sys.executable, str(SCRIPTS / script)]
        completed = subprocess.run(command, cwd=ROOT, check=True)
        commands.append({"command": ["python", f"scripts/{script}"], "returncode": completed.returncode})

    pytest_command = [sys.executable, "-m", "pytest", "-q"]
    completed = subprocess.run(pytest_command, cwd=ROOT, check=True)
    commands.append({"command": ["python", "-m", "pytest", "-q"], "returncode": completed.returncode})

    verifier_command = [sys.executable, str(SCRIPTS / "verify_public_package.py")]
    completed = subprocess.run(verifier_command, cwd=ROOT, check=True)
    commands.append({"command": ["python", "scripts/verify_public_package.py"], "returncode": completed.returncode})

    summary = ROOT / "results" / "public_reproducibility_check.json"
    summary.write_text(
        json.dumps({"status": "pass", "commands": commands}, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(f"\nall reproducibility checks: PASS\nwrote: {summary.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
