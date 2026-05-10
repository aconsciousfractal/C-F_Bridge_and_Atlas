#!/usr/bin/env python3
"""Replay the finite C/F bridge checks used by the companion package.

The paper proves the bridge mathematically.  This script is only a finite
computational replay of the coefficient identities around that theorem.
It uses the Python standard library only.
"""

from __future__ import annotations

import json
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
BOUND = 30


def zagier_c(n: int) -> int:
    return sum(comb(n, k) ** 2 * comb(2 * k, k) for k in range(n + 1))


def franel(n: int) -> int:
    return sum(comb(n, k) ** 3 for k in range(n + 1))


def zagier_f_by_recurrence(bound: int) -> list[int]:
    values = [1]
    for n in range(bound):
        prev = values[n - 1] if n > 0 else 0
        current = values[n]
        numerator = (17 * n * n + 17 * n + 6) * current - 72 * n * n * prev
        denominator = (n + 1) ** 2
        if numerator % denominator != 0:
            raise ArithmeticError(f"F recurrence is nonintegral at n={n}")
        values.append(numerator // denominator)
    return values


def cf_transform(values: list[int], m: int) -> int:
    return sum(comb(m, n) * (-1) ** n * 9 ** (m - n) * values[n] for n in range(m + 1))


def c_from_franel(franel_values: list[int], m: int) -> int:
    return sum(comb(m, n) * franel_values[n] for n in range(m + 1))


def f_from_franel(franel_values: list[int], m: int) -> int:
    return sum(comb(m, n) * (-1) ** n * 8 ** (m - n) * franel_values[n] for n in range(m + 1))


def first_bad(left: list[int], right: list[int]) -> list[dict[str, int]]:
    return [
        {"n": n, "left": a, "right": b, "difference": a - b}
        for n, (a, b) in enumerate(zip(left, right))
        if a != b
    ]


def main() -> int:
    c_values = [zagier_c(n) for n in range(BOUND + 1)]
    f_recurrence = zagier_f_by_recurrence(BOUND)
    t_c = [cf_transform(c_values, m) for m in range(BOUND + 1)]
    t_t_c = [cf_transform(t_c, m) for m in range(BOUND + 1)]

    r_values = [franel(n) for n in range(BOUND + 1)]
    c_franel = [c_from_franel(r_values, m) for m in range(BOUND + 1)]
    f_franel = [f_from_franel(r_values, m) for m in range(BOUND + 1)]

    checks = {
        "T_C_equals_F_recurrence": first_bad(t_c, f_recurrence),
        "T_is_involutive_on_C": first_bad(t_t_c, c_values),
        "C_matches_Franel_route": first_bad(c_values, c_franel),
        "F_matches_Franel_route": first_bad(f_recurrence, f_franel),
    }
    bad_count = sum(len(items) for items in checks.values())

    payload = {
        "status": "pass" if bad_count == 0 else "fail",
        "bound": BOUND,
        "checked_terms": BOUND + 1,
        "bad_count": bad_count,
        "checks": {name: {"bad_count": len(items), "first_bad": items[:3]} for name, items in checks.items()},
        "sample_coefficients": {
            "C": c_values[:10],
            "F": f_recurrence[:10],
            "Franel": r_values[:10],
        },
    }

    RESULTS.mkdir(exist_ok=True)
    out = RESULTS / "cf_bridge_replay.json"
    with out.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")

    if bad_count:
        print("C/F bridge replay: FAIL")
        print(f"wrote: {out.relative_to(ROOT)}")
        return 1

    print("C/F bridge replay: PASS")
    print(f"checked_terms: {BOUND + 1}")
    print(f"wrote: {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
