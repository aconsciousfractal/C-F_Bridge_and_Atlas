#!/usr/bin/env python3
"""Finite Lucas replay for the Chan-Cooper companion rows.

The paper proves the all-primes result. This script is only a finite sanity
check for the formulas, low-prime branches, and the negative-q level-8 sign
normalization used in the public companion package.
"""

from __future__ import annotations

import json
from math import comb
from pathlib import Path
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
N_MAX = 120
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19]


def s6a(n: int) -> int:
    total = 0
    for j in range(n + 1):
        franel = sum(comb(j, ell) ** 3 for ell in range(j + 1))
        total += (-8) ** (n - j) * comb(n, j) * franel
    return total


def s6b(n: int) -> int:
    return sum(comb(n, j) ** 2 * comb(2 * j, j) for j in range(n + 1))


def s6c(n: int) -> int:
    return sum(comb(n, j) ** 3 for j in range(n + 1))


def s8(n: int) -> int:
    return sum(
        4 ** (n - 2 * j) * comb(n, 2 * j) * comb(2 * j, j) ** 2
        for j in range(n // 2 + 1)
    )


def s9(n: int) -> int:
    return sum(
        (-3) ** (n - 3 * j) * comb(n, j) * comb(n - j, j) * comb(n - 2 * j, j)
        for j in range(n // 3 + 1)
    )


def central(n: int) -> int:
    return comb(2 * n, n)


def build_sequence(fn: Callable[[int], int]) -> list[int]:
    return [fn(n) for n in range(N_MAX + 1)]


def multiply_central(values: list[int]) -> list[int]:
    return [central(n) * values[n] for n in range(N_MAX + 1)]


def sign_twist(values: list[int]) -> list[int]:
    return [((-1) ** n) * values[n] for n in range(N_MAX + 1)]


def lucas_failures(values: list[int]) -> list[dict[str, int]]:
    failures: list[dict[str, int]] = []
    for p in PRIMES:
        for n, value in enumerate(values):
            n0 = n % p
            n1 = n // p
            lhs = value % p
            rhs = (values[n0] * values[n1]) % p
            if lhs != rhs:
                failures.append({"p": p, "n": n, "lhs": lhs, "rhs": rhs})
                if len(failures) >= 20:
                    return failures
    return failures


def main() -> int:
    s6a_values = build_sequence(s6a)
    s6b_values = build_sequence(s6b)
    s6c_values = build_sequence(s6c)
    s8_values = build_sequence(s8)
    s9_values = build_sequence(s9)

    sequences = {
        "s6A": s6a_values,
        "U6A": multiply_central(s6a_values),
        "s6B": s6b_values,
        "U6B": multiply_central(s6b_values),
        "s6C": s6c_values,
        "U6C": multiply_central(s6c_values),
        "s8": s8_values,
        "U8": multiply_central(s8_values),
        "U8_minus": sign_twist(multiply_central(s8_values)),
        "s9": s9_values,
        "U9": multiply_central(s9_values),
    }

    failures = {name: lucas_failures(values) for name, values in sequences.items()}
    failures = {name: bad for name, bad in failures.items() if bad}

    payload = {
        "artifact": "chan_cooper_lucas_replay",
        "status": "pass" if not failures else "fail",
        "n_max": N_MAX,
        "primes": PRIMES,
        "sequence_count": len(sequences),
        "sequences": sorted(sequences),
        "failures": failures,
        "guardrail": "finite sanity replay only; the all-primes Lucas theorem is proved in the paper",
    }

    RESULTS.mkdir(exist_ok=True)
    out = RESULTS / "chan_cooper_lucas_replay.json"
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    if failures:
        print(json.dumps(failures, indent=2, sort_keys=True))
        raise SystemExit("Chan-Cooper Lucas replay: FAIL")

    print("Chan-Cooper Lucas replay: PASS")
    print(f"checked_sequences: {len(sequences)}")
    print(f"n_max: {N_MAX}")
    print(f"primes: {PRIMES}")
    print(f"wrote: {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
