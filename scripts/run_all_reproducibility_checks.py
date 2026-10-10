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
    summary = ROOT / "results" / "public_reproducibility_check.json"
    def save(status: str) -> None:
        summary.write_text(json.dumps({"status": status, "commands": commands}, indent=2) + "\n", encoding="utf-8", newline="\n")
    def run(command: list[str], recorded: list[str]) -> None:
        completed = subprocess.run(command, cwd=ROOT, check=False)
        commands.append({"command": recorded, "returncode": completed.returncode})
        save("running" if completed.returncode == 0 else "fail")
        if completed.returncode:
            raise SystemExit(completed.returncode)
    # A failed/incomplete invocation cannot leave an earlier PASS as its receipt.
    save("running")
    for script in CHECKS:
        print(f"\n== {script} ==")
        command = [sys.executable, str(SCRIPTS / script)]
        run(command, ["python", f"scripts/{script}"])

    pytest_command = [sys.executable, "-m", "pytest", "-q", "-x"]
    run(pytest_command, ["python", "-m", "pytest", "-q", "-x"])

    verifier_command = [sys.executable, str(SCRIPTS / "verify_public_package.py")]
    run(verifier_command, ["python", "scripts/verify_public_package.py"])

    save("pass")
    print(f"\nall reproducibility checks: PASS\nwrote: {summary.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
