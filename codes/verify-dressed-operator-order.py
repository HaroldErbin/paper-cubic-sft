"""Finite-model check of the truncation dependence of the dressed kinetic operators.

Record: agent/derivations/117-dressed-operator-order-label.md.

Model: the k-string spaces are C^{d_k}; the bare operators w_{k,k}, the odd
vertices O_k = W_{2k+1}(., ., Psi) and the source maps T_k (A -> Psi (x) A) are
random exact-rational matrices (w, O symmetric, w invertible).  The dressed
operator at truncation n is built by the recursion eq:all:nested of
paper/sections/03-all-orders.tex,

    k^{(n)}_{k} = w_k - gs/(2k+1) O_k - gs^2/((2k+1)(2k+2)) T_k^T w_{k+1} (k^{(n)}_{k+1})^{-1} w_{k+1} T_k,

with the top of the chain fixed by the truncation: n = 2K-1 -> k_K = w_K - gs/(2K+1) O_K;
n = 2K -> k_{K+1} = w_{K+1}.  Inverses are exact (sympy), the series in gs is
read off the exact result, so the hand-made Neumann expansions of the record
(eqs. (1.2), (1.4), (1.5)) are compared with an independent computation.

Verified: C1.2, C1.3, C1.4 (explicit coefficients for k = 2 through gs^4 and
the gs^4, gs^5 truncation differences), C2 (k^{(n+1)} - k^{(n)} = O(gs^{n-2k+3})
with non-zero leading coefficient, for k = 2, 3 and n = 3..7).
Not verified: anything about the actual string vertices (the model is abstract),
the kernel conditions (w_k is taken invertible), convergence (formal series).

Run from the project root:
    uv run python verify-dressed-operator-order.py
"""

from __future__ import annotations

import argparse
import random
import sys
from pathlib import Path

import sympy as sp

GS = sp.Symbol("g_s")
DIMS = {2: 2, 3: 2, 4: 2, 5: 2}  # d_k for k = 2..5


def rand_rational(rng: random.Random) -> sp.Rational:
    """Random non-zero rational in general position."""
    num = rng.choice([v for v in range(-9, 10) if v != 0])
    den = rng.randint(1, 7)
    return sp.Rational(num, den)


def rand_matrix(rng: random.Random, rows: int, cols: int) -> sp.Matrix:
    return sp.Matrix(rows, cols, lambda i, j: rand_rational(rng))


def rand_symmetric(rng: random.Random, dim: int, invertible: bool) -> sp.Matrix:
    while True:
        m = rand_matrix(rng, dim, dim)
        m = m + m.T
        if not invertible or m.det() != 0:
            return m


def build_model(rng: random.Random) -> dict:
    """Random bare operators w_k, odd vertices O_k, source maps T_k."""
    w = {k: rand_symmetric(rng, d, True) for k, d in DIMS.items()}
    odd = {k: rand_symmetric(rng, d, False) for k, d in DIMS.items()}
    t = {k: rand_matrix(rng, DIMS[k + 1], DIMS[k]) for k in DIMS if k + 1 in DIMS}
    return {"w": w, "O": odd, "T": t}


def dressed(model: dict, k: int, n: int) -> sp.Matrix:
    """k^{(n)}_{k,k;Psi} by the recursion eq:all:nested, exact in gs.

    Truncation n = 2K-1: top field Sigma_K with its odd vertex.
    Truncation n = 2K: top field Sigma_{K+1} with its bare operator only.
    """
    if n % 2 == 1:
        top, top_has_odd = (n + 1) // 2, True
    else:
        top, top_has_odd = n // 2 + 1, False
    if k > top:
        raise ValueError(f"Sigma_{k} is not in the action truncated at order {n}")
    w, odd, t = model["w"], model["O"], model["T"]
    op = w[k]
    if k < top or top_has_odd:
        op = op - GS / (2 * k + 1) * odd[k]
    if k < top:
        inner = dressed(model, k + 1, n)
        coeff = GS**2 / ((2 * k + 1) * (2 * k + 2))
        op = op - coeff * t[k].T * w[k + 1] * inner.inv() * w[k + 1] * t[k]
    return sp.simplify(op)


def series_coeff(mat: sp.Matrix, order: int) -> sp.Matrix:
    """Coefficient matrix of gs^order in the Taylor expansion at gs = 0."""
    return mat.applyfunc(
        lambda e: sp.series(e, GS, 0, order + 1).removeO().coeff(GS, order)
    )


def leading_order(mat: sp.Matrix, max_order: int = 8) -> int | None:
    """Smallest m with a non-zero gs^m coefficient (None if zero through max_order)."""
    for m in range(max_order + 1):
        if any(c != 0 for c in series_coeff(mat, m)):
            return m
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument(
        "--out",
        type=Path,
        default=Path(__file__).resolve().parent / "output" / "dressed-operator-order",
    )
    parser.add_argument(
        "--perturb",
        default=None,
        help="name of a -break check whose perturbation to apply",
    )
    parser.add_argument("--seed", type=int, default=20261109)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    print(f"seed = {args.seed}")
    rng = random.Random(args.seed)
    model = build_model(rng)
    w, odd, t = model["w"], model["O"], model["T"]
    results: list[tuple[str, bool]] = []

    def check(name: str, ok: bool, detail: str = "") -> None:
        results.append((name, ok))
        print(f"{'PASS' if ok else 'FAIL'}  {name}  {detail}")

    # Perturbation knobs for the -break legs: a wrong coefficient in the hand formula.
    c30 = sp.Rational(1, 31) if args.perturb == "C1.2-break" else sp.Rational(1, 30)
    c210 = sp.Rational(1, 211) if args.perturb == "C1.3-break" else sp.Rational(1, 210)

    k3 = dressed(model, 2, 3)
    k4 = dressed(model, 2, 4)
    k5 = dressed(model, 2, 5)
    k6 = dressed(model, 2, 6)
    k7 = dressed(model, 2, 7)

    # C1.1 (sanity of the model): quintic operator = p22 - gs/5 O2.
    check("C1.1", sp.simplify(k3 - (w[2] - GS / 5 * odd[2])) == sp.zeros(2, 2))

    # C1.2: k^{(4)} - k^{(3)} = -gs^2/30 T2^T w3 T2 exactly (eq. (1.2)).
    diff43 = sp.simplify(k4 - k3 + c30 * GS**2 * t[2].T * w[3] * t[2])
    check(
        "C1.2" if args.perturb != "C1.2-break" else "C1.2-break",
        diff43 == sp.zeros(2, 2),
        "exact in gs",
    )

    # C1.3: coefficients of k^{(5)} at gs^2, gs^3, gs^4 (eq. (1.4)).
    hand = {
        2: -sp.Rational(1, 30) * t[2].T * w[3] * t[2],
        3: -c210 * t[2].T * odd[3] * t[2],
        4: -sp.Rational(1, 30 * 49) * t[2].T * odd[3] * w[3].inv() * odd[3] * t[2],
    }
    ok = all(sp.simplify(series_coeff(k5, m) - hand[m]) == sp.zeros(2, 2) for m in hand)
    check(
        "C1.3" if args.perturb != "C1.3-break" else "C1.3-break",
        ok,
        "gs^2, gs^3, gs^4 of k^{(5)}_{2}",
    )
    # C1.3-nv: the three coefficients are non-zero (the check is not vacuous).
    check("C1.3-nv", all(any(c != 0 for c in hand[m]) for m in hand))

    # C1.4: k^{(6)} - k^{(5)} = -gs^4/1680 T2^T T3^T w4 T3 T2 + O(gs^5); k^{(7)} - k^{(6)} at gs^5.
    d65 = k6 - k5
    ok = (leading_order(d65) == 4) and sp.simplify(
        series_coeff(d65, 4)
        + sp.Rational(1, 30 * 56) * t[2].T * t[3].T * w[4] * t[3] * t[2]
    ) == sp.zeros(2, 2)
    check("C1.4", ok, "k^{(6)}-k^{(5)} = -gs^4/1680 W8(Psi^2 A, Psi^2 B) + O(gs^5)")
    d76 = k7 - k6
    ok = (leading_order(d76) == 5) and sp.simplify(
        series_coeff(d76, 5)
        + sp.Rational(1, 30 * 56 * 9) * t[2].T * t[3].T * odd[4] * t[3] * t[2]
    ) == sp.zeros(2, 2)
    check(
        "C1.4-gs5",
        ok,
        "k^{(7)}-k^{(6)} = -gs^5/15120 W9(Psi^2 A, Psi^2 B, Psi) + O(gs^6)",
    )

    # C2: leading order of k^{(n+1)} - k^{(n)} is n - 2k + 3, for k = 2, 3.
    ok_all = True
    for k in (2, 3):
        for n in range(2 * k - 1, 7):
            lo = leading_order(dressed(model, k, n + 1) - dressed(model, k, n))
            expect = n - 2 * k + 3
            good = lo == expect
            ok_all &= good
            print(f"      k={k} n={n}: leading order {lo}, expected {expect}")
    check("C2", ok_all, "k^{(n+1)}-k^{(n)} = O(gs^{n-2k+3}), non-zero")

    n_fail = sum(not ok for _, ok in results)
    summary = f"{len(results) - n_fail}/{len(results)} PASS"
    print(summary)
    (args.out / "verify-dressed-operator-order.txt").write_text(
        "\n".join(f"{'PASS' if ok else 'FAIL'} {name}" for name, ok in results)
        + f"\n{summary}\n"
    )
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
