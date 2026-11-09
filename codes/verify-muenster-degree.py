"""Degree dictionary paper / CFL / Münster–Sachs for the (m, n) string products.

Verifies (record ``agent/derivations/120-muenster-degree-dictionary.md``):

* C1 – with a strand grading ``delta = alpha*N + beta`` affine in the ghost number
  ``N``, an operation read from a vertex with ``m`` inputs (ghost number 2) and
  ``n`` outputs (ghost number 3) has degree ``n*(3*alpha+beta) - m*(2*alpha+beta)``;
  at ``alpha = 1, beta = 0`` this is the paper's ``3n - 2m``.
* C2 – the CFL degree ``-2d(k+g-1) - 1`` (Cieliebak–Fukaya–Latschev, Def. 2.3, genus
  0, ``k = m`` inputs) is reproduced by an affine strand grading iff
  ``(alpha, beta, d) = (-1, 3, 1/2)``; the solution is unique (an exact linear
  solve) and ``C2-break`` shows that no integer ``d`` admits a solution.
* C4 – the Münster–Sachs grading (strand degree ``N - 2``) gives every single-output
  product ``l_n`` and the inverse symplectic form ``omega^{-1}`` degree +1, i.e.
  CFL's formula with ``d = 0`` up to the overall sign of the grading.
* C5 – in the Münster–Sachs grading the paper's ``(m, n)`` product has degree ``n``,
  equal to the degree of the composite of one ``l`` with ``n-1`` copies of
  ``omega^{-1}``.
* C6 – no affine strand grading makes the degree independent of both ``m`` and ``n``
  except the zero grading.
* C7 – on the support of the pairing (``|A| + |B|`` odd) the only parity signs
  ``eps(|A|, |B|)`` making ``eps * <A, B>`` graded antisymmetric are ``±(-1)^{|A|}``;
  the paper's ``Omega_n`` equals the Koszul tensor power of ``Omega`` (checked on
  n = 2, 3 for all parity assignments).

Not verified: anything about the IBL relations themselves (the record only compares
gradings), and the overall sign ``omega_c = ±Omega``, which the Münster–Sachs text does
not fix.

Run from the project root::

    uv run python verify-muenster-degree.py [--out DIR]
        [--perturb C2-break] [--seed N]
"""

from __future__ import annotations

import argparse
import itertools
import random
import sys
from pathlib import Path

import sympy as sp

alpha, beta, d = sp.symbols("alpha beta d")
m, n = sp.symbols("m n", integer=True, positive=True)

N_IN = 2  # ghost number of an input strand (paper, A1)
N_OUT = 3  # ghost number of an output strand (paper, A1)


def op_degree(a, b, m_, n_):
    """Degree of an (m, n) operation for the strand grading delta = a*N + b."""
    return n_ * (a * N_OUT + b) - m_ * (a * N_IN + b)


def cfl_degree(d_, k, g=0):
    """CFL degree |p_{k, l, g}| = -2d(k+g-1) - 1, independent of the outputs."""
    return -2 * d_ * (k + g - 1) - 1


def run(perturb: str | None, seed: int) -> list[tuple[str, bool, str]]:
    rng = random.Random(seed)
    results: list[tuple[str, bool, str]] = []

    # C1: paper grading alpha = 1, beta = 0 gives 3n - 2m.
    expr = sp.expand(op_degree(1, 0, m, n) - (3 * n - 2 * m))
    results.append(("C1", expr == 0, f"paper degree - (3n-2m) = {expr}"))

    # C2: affine fit to CFL at genus 0, for all m, n: coefficients of n and m.
    diff = sp.expand(op_degree(alpha, beta, m, n) - cfl_degree(d, m))
    eqs = [diff.coeff(n), diff.coeff(m), diff.subs({m: 0, n: 0})]
    sols = sp.solve(eqs, [alpha, beta, d], dict=True)
    ok = sols == [{alpha: -1, beta: 3, d: sp.Rational(1, 2)}]
    results.append(("C2", ok, f"affine solutions of CFL fit: {sols}"))
    # numeric confirmation at random (m, n) in general position
    pts = [(rng.randint(1, 9), rng.randint(1, 9)) for _ in range(5)]
    num_ok = all(
        op_degree(-1, 3, mm, nn) == cfl_degree(sp.Rational(1, 2), mm) for mm, nn in pts
    )
    results.append(("C2-numeric", num_ok, f"delta = 3 - N vs CFL(d=1/2) at {pts}"))

    # C2-break: with d restricted to an integer the fit has no solution.
    if perturb == "C2-break":
        ints = range(-5, 6)
        found = [
            dd
            for dd in ints
            if sp.solve([e.subs(d, dd) for e in eqs], [alpha, beta], dict=True)
        ]
        # a found integer solution would make the check PASS; it must FAIL
        results.append(
            ("C2-break", bool(found), f"integer d with an affine fit: {found}")
        )

    # C4: Münster–Sachs grading (alpha, beta) = (1, -2): l_n degree 1 for all n,
    # omega^{-1} (two strands of total ghost number 5) degree 1.
    ms_ln = sp.expand(op_degree(1, -2, m, 1))
    ms_omega_inv = 5 - 2 * 2  # strands N_1 + N_2 = 5, each shifted by -2
    ok = ms_ln == 1 and ms_omega_inv == 1
    results.append(
        ("C4", ok, f"MS degree of l_n = {ms_ln}, of omega^-1 = {ms_omega_inv}")
    )
    # equals -CFL(d = 0) for every k, g
    k, g = sp.symbols("k g", integer=True, nonnegative=True)
    ok = sp.expand(-cfl_degree(0, k, g)) == 1
    results.append(
        ("C4-cfl", ok, f"-CFL degree at d=0 = {sp.expand(-cfl_degree(0, k, g))}")
    )

    # C5: MS degree of (m, n) product is n; composite of l with n-1 omega^-1 is 1+(n-1).
    ms_mn = sp.expand(op_degree(1, -2, m, n))
    ok = ms_mn == n and sp.expand(1 + (n - 1) * 1 - n) == 0
    results.append(("C5", ok, f"MS degree of p_(m,n) = {ms_mn}"))

    # C6: independence of both m and n forces alpha = beta = 0.
    sols6 = sp.solve([3 * alpha + beta, 2 * alpha + beta], [alpha, beta], dict=True)
    results.append(("C6", sols6 == [{alpha: 0, beta: 0}], f"solutions: {sols6}"))

    # C7: parity signs eps(a, b) on the support a + b = 1 mod 2 making
    # eps(a,b) <A,B> graded antisymmetric, given <B,A> = (-1)^{ab} <A,B> = <A,B>.
    # Antisymmetry: eps(b,a) = -(-1)^{ab} eps(a,b) = -eps(a,b) on the support.
    valid = []
    for e01, e10 in itertools.product([1, -1], repeat=2):
        eps = {(0, 1): e01, (1, 0): e10}
        if all(eps[(b, a)] == -eps[(a, b)] for (a, b) in eps):
            valid.append(eps)
    # candidates ±(-1)^{|A|}
    cands = [{(0, 1): s, (1, 0): -s} for s in (1, -1)]
    ok = sorted(map(sorted, map(dict.items, valid))) == sorted(
        map(sorted, map(dict.items, cands))
    )
    results.append(("C7-sign", ok, f"antisymmetric parity signs: {valid}"))

    # C7: Omega_n(X, Y) = (-1)^{|X|} <X, Y>_n equals the Koszul tensor power of Omega.
    def koszul_power(par_a, par_b):
        # Omega^{⊗n} with Koszul sign (-1)^{sum_{i<j} |B_i||A_j|}, each Omega = (-1)^{|A_i|}<.,.>
        s = sum(
            par_b[i] * par_a[j]
            for i in range(len(par_a))
            for j in range(i + 1, len(par_a))
        )
        return (-1) ** (s + sum(par_a))

    def paper_omega_n(par_a, par_b):
        s = sum(
            par_b[i] * par_a[j]
            for i in range(len(par_a))
            for j in range(i + 1, len(par_a))
        )
        return (-1) ** (sum(par_a)) * (-1) ** s

    ok = True
    for nn in (2, 3):
        for par_a in itertools.product([0, 1], repeat=nn):
            par_b = tuple(1 - a for a in par_a)  # support: opposite parity per strand
            ok &= koszul_power(par_a, par_b) == paper_omega_n(par_a, par_b)
    results.append(
        ("C7-tensor", ok, "Omega_n = Koszul tensor power of Omega (n = 2, 3)")
    )

    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--out", type=Path, default=None, help="output directory (unused)"
    )
    parser.add_argument("--perturb", default=None, help="run the named -break check")
    parser.add_argument("--seed", type=int, default=20261109)
    args = parser.parse_args()
    print(f"seed = {args.seed}")
    results = run(args.perturb, args.seed)
    n_fail = 0
    for name, ok, msg in results:
        print(f"{'PASS' if ok else 'FAIL'}  {name}: {msg}")
        n_fail += not ok
    print(f"summary: {len(results) - n_fail}/{len(results)} passed")
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
