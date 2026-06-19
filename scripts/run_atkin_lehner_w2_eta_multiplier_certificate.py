#!/usr/bin/env python3
"""Replay the exact eta-multiplier arithmetic for the C/F W2 theta audit.

The paper appendix proves the Atkin-Lehner W2 parameter/theta audit.  This
script reproduces the finite exact multiplier arithmetic in that appendix using
only the Python standard library.  It is not a full modular-form proof engine.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from fractions import Fraction
from math import gcd
from pathlib import Path
from typing import Dict


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
W2 = (2, -1, 6, -2)
THETA_C = {1: -3, 2: 6, 3: 1, 6: -2}
THETA_F = {1: 6, 2: -3, 3: -2, 6: 1}


@dataclass(frozen=True)
class EtaFactor:
    source_delta: int
    target_delta: int
    gamma: tuple[int, int, int, int]
    binary_sqrt_factor: int


FACTORS = {
    1: EtaFactor(1, 2, (1, -1, 3, -2), 2),
    2: EtaFactor(2, 1, (2, -1, 3, -1), 1),
    3: EtaFactor(3, 6, (1, -3, 1, -2), 2),
    6: EtaFactor(6, 3, (2, -3, 1, -1), 1),
}


def matmul(a: tuple[int, int, int, int], b: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    a11, a12, a21, a22 = a
    b11, b12, b21, b22 = b
    return (
        a11 * b11 + a12 * b21,
        a11 * b12 + a12 * b22,
        a21 * b11 + a22 * b21,
        a21 * b12 + a22 * b22,
    )


def det(m: tuple[int, int, int, int]) -> int:
    a, b, c, d = m
    return a * d - b * c


def primitive(m: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    common = 0
    for entry in m:
        common = gcd(common, abs(entry))
    return tuple(entry // common for entry in m)


def sawtooth(x: Fraction) -> Fraction:
    floor = x.numerator // x.denominator
    frac = x - floor
    if frac == 0:
        return Fraction(0)
    return frac - Fraction(1, 2)


def dedekind_sum(d_value: int, c_value: int) -> Fraction:
    return sum(
        sawtooth(Fraction(n, c_value)) * sawtooth(Fraction(d_value * n, c_value))
        for n in range(1, c_value)
    )


def eta_multiplier_exponent(gamma: tuple[int, int, int, int]) -> Fraction:
    """Return R such that epsilon(gamma)=exp(pi*i*R), for c>0."""
    a, _b, c, d_value = gamma
    if c <= 0:
        raise ValueError("this certificate expects c > 0")
    return Fraction(a + d_value, 12 * c) - dedekind_sum(d_value, c) - Fraction(1, 4)


def target_exponents(source: Dict[int, int]) -> Dict[int, int]:
    out: Dict[int, int] = {}
    for delta, exponent in source.items():
        target = FACTORS[delta].target_delta
        out[target] = out.get(target, 0) + exponent
    return {key: out[key] for key in sorted(out)}


def multiplier_exponent(source: Dict[int, int]) -> Fraction:
    return sum(exponent * eta_multiplier_exponent(FACTORS[delta].gamma) for delta, exponent in source.items())


def binary_exponent_after_slash(source: Dict[int, int]) -> Fraction:
    eta_binary = sum(
        Fraction(exponent, 2)
        for delta, exponent in source.items()
        if FACTORS[delta].binary_sqrt_factor == 2
    )
    slash_binary = Fraction(-1, 2)  # sqrt(2)/(6 tau - 2) = 2^(-1/2) * (3 tau - 1)^(-1)
    return eta_binary + slash_binary


def tau_power_after_slash(source: Dict[int, int]) -> Fraction:
    eta_tau_power = sum(Fraction(exponent, 2) for exponent in source.values())
    slash_tau_power = Fraction(-1)
    return eta_tau_power + slash_tau_power


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def assert_equal(name: str, observed, expected) -> None:
    if observed != expected:
        raise AssertionError(f"{name}: observed {observed!r}, expected {expected!r}")
    print(f"PASS {name}: {observed!r}")


def check_factorizations() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for delta, factor in FACTORS.items():
        scaled_w2 = (delta * W2[0], delta * W2[1], W2[2], W2[3])
        diag = (factor.target_delta, 0, 0, 1)
        factored = matmul(factor.gamma, diag)
        expected = primitive(scaled_w2)
        assert_equal(f"det gamma delta={delta}", det(factor.gamma), 1)
        assert_equal(f"primitive factorization delta={delta}", factored, expected)
        rows.append(
            {
                "delta": delta,
                "gamma": list(factor.gamma),
                "target_delta": factor.target_delta,
                "eta_R": fraction_text(eta_multiplier_exponent(factor.gamma)),
                "binary_sqrt_factor": factor.binary_sqrt_factor,
            }
        )
    return rows


def check_theta(
    name: str,
    source: Dict[int, int],
    expected_target: Dict[int, int],
    expected_unit_exponent_mod_2: Fraction,
    expected_binary_exponent: Fraction,
) -> dict[str, object]:
    observed_target = target_exponents(source)
    unit_exponent = multiplier_exponent(source) % 2
    binary_exponent = binary_exponent_after_slash(source)
    tau_exponent = tau_power_after_slash(source)

    assert_equal(f"{name} target eta exponents", observed_target, expected_target)
    assert_equal(f"{name} eta unit exponent mod 2", unit_exponent, expected_unit_exponent_mod_2)
    assert_equal(f"{name} binary constant exponent", binary_exponent, expected_binary_exponent)
    assert_equal(f"{name} residual tau exponent", tau_exponent, Fraction(0))

    return {
        "target_eta_exponents": {str(k): v for k, v in observed_target.items()},
        "eta_unit_exponent_mod_2": fraction_text(unit_exponent),
        "binary_constant_exponent": fraction_text(binary_exponent),
        "residual_tau_exponent": fraction_text(tau_exponent),
    }


def main() -> int:
    factor_rows = check_factorizations()
    theta_c = check_theta("Theta_C|W2", THETA_C, THETA_F, Fraction(0), Fraction(-3, 2))
    theta_f = check_theta("Theta_F|W2", THETA_F, THETA_C, Fraction(1), Fraction(3, 2))

    payload = {
        "status": "pass",
        "statement": {
            "Theta_C_slash_W2": "2^(-3/2) Theta_F = (2 sqrt(2))^(-1) Theta_F",
            "Theta_F_slash_W2": "-2^(3/2) Theta_C = -2 sqrt(2) Theta_C",
        },
        "factorizations": factor_rows,
        "theta_checks": {
            "Theta_C_slash_W2": theta_c,
            "Theta_F_slash_W2": theta_f,
        },
        "scope": "finite exact eta-multiplier arithmetic used in the paper appendix",
    }

    RESULTS.mkdir(exist_ok=True)
    out = RESULTS / "atkin_lehner_w2_eta_multiplier_certificate.json"
    with out.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")

    print("PASS exact C/F W2 theta-multiplier certificate")
    print("Theta_C |_1 W2 = 2^(-3/2) Theta_F = (2 sqrt(2))^(-1) Theta_F")
    print("Theta_F |_1 W2 = -2^(3/2) Theta_C = -2 sqrt(2) Theta_C")
    print(f"wrote: {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
