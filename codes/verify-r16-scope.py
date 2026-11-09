"""
Scope of R16/R31: the augmented obstruction P_{k,l} != 0 at every (k,l) with k, l >= 2.

Record: agent/derivations/026-linfty-to-ibl-repackaging.md, Sec. 9 (addendum 2026-09-26).

Claim tested (026 Prop. 9.1).  Let (h, omega_h) be a cyclic L_infty algebra with purely cubic
master action S_h (Q = 0, only ell_2), e.g. the Chevalley-Eilenberg algebra g_(1) + g*_(4)
of a Lie algebra g (026 eq. (3.19)).  Extend by an even ghost-2 direction e and its odd
ghost-3 partner e* (omega(e, e*) = 1, orthogonal sum) and put S'(Psi) = g(eps) S_h(psi),
eps = e-coordinate of Psi, g a power series.  Then S' solves the master equation and, with
x, y the e-coordinates of Psi, chi,

    M'(Psi, chi) = h_g(x, y) M^h_{2,2}(psi, xi),
    h_g(x, y)    = g(x + y) [g(x) + g(y)] - g(x) g(y),
    P'_{k,l}     = -(1/2) [h_g]_{k-2,l-2} x^{k-2} y^{l-2} M^h_{2,2}(psi, xi),

and for g = exp, [h]_{a,b} = (2^a + 2^b - 1)/(a! b!) > 0, so P'_{k,l} != 0 at every k,l >= 2
when M^h_{2,2} != 0 (g = sl_2).

Method (independent of the factorised proof): exact sparse Grassmann polynomials over
Fractions in the doubled coordinates (psi^a, xi^a), parity eps_a = N_gh mod 2.  Everything
is computed from the DEFINITIONS of 026 Sec. 3.1: H_{p,q} = bidegree parts of S(Psi + chi),
{F, G} = d_{Psi^a} F Dt^{ab} d_{chi^b} G (left derivatives, Dt^{ab} = (-1)^{eps_a} Delta^{ab},
Delta = omega^{-1}), T(i,j|m,n) = {H_{i+1,j}, H_{m,n+1}}, R, M, P, B as in (3.4)-(3.5).
M^h_{2,2} is computed by the same code on S_h alone; h_g is computed with sympy.

Checks (named after the claims of 026 Sec. 9):
  9.2-master     B'_{k,l} = 0 (the extension is cyclic L_infty)       [break: Jacobi-violating f]
  9.2-nonhollow  individual configurations T(i,j|m,n) nonzero at each signature
  3.15           M'_{k,l} = -2 P'_{k,l}
  9.2-closed     P'_{k,l} equals the closed form, exactly     [break: sign of g(x)g(y) flipped]
  9.2-nonzero    P'_{k,l} != 0 at every signature tested
  9.2-hexp       [h_exp]_{a,b} = (2^a + 2^b - 1)/(a! b!), a, b <= 8 (sympy)
  9.2-cancel     g = 1 + eps - eps^2/4: P'_{3,3} = 0 exactly with nonzero configurations,
                 P'_{2,4}, P'_{4,2} != 0 (non-hollow CFL-satisfying control at (3,3))
  9.2-nonaug     non-augmented relation B = 0 while R = -P != 0 (the augmented residual)
  9.2-aff1       closed form on a second base algebra (2-dim aff(1))
NOT verified here: anything about the physical closed-SFT L_infty algebra (the statement is
existence of counterexamples in the class of cyclic L_infty algebras); the dense-tensor
conventions of codes/verify-linfty-ibl-repackaging.py are not re-used (independent code path);
generator (iv) of 026 Sec. 1.5 is not evaluated beyond (2,2), (2,3), (3,2).

Usage:  .venv/bin/python codes/verify-r16-scope.py [--kmax 5]   (default 5: k, l = 2..5, plus (2,6), (6,2))
"""

from __future__ import annotations

import argparse
import random
import sys
from fractions import Fraction
from math import factorial

import sympy as sp

SEED = 20260926
RESULTS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    """Record and print one named PASS/FAIL check."""
    RESULTS.append((name, bool(ok)))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


# ---------------------------------------------------------------------------
# Sparse graded-commutative polynomials.  A monomial is a sorted tuple of variable
# indices (even variables may repeat, odd ones may not); the stored coefficient is that
# of the product of the variables in sorted order.
# ---------------------------------------------------------------------------
class Alg:
    """Graded-commutative polynomial algebra on variables with given parities."""

    def __init__(self, par: list[int]) -> None:  # noqa: D107
        self.par = par

    def mono_mul(self, m1: tuple, m2: tuple) -> tuple[int, tuple] | None:
        """Sign and sorted monomial of m1*m2 (Koszul sign of the sorting permutation)."""
        lst = list(m1) + list(m2)
        # inversions between odd variables coming from different factors only
        # (each factor is already sorted)
        sign = 1
        for a in m1:
            if self.par[a]:
                for b in m2:
                    if self.par[b] and b < a:
                        sign = -sign
        srt = sorted(lst)
        for p in range(len(srt) - 1):
            if srt[p] == srt[p + 1] and self.par[srt[p]]:
                return None
        return sign, tuple(srt)

    def mul(self, F: dict, G: dict) -> dict:
        """Product F*G with Koszul signs."""
        out: dict = {}
        for m1, c1 in F.items():
            for m2, c2 in G.items():
                r = self.mono_mul(m1, m2)
                if r is None:
                    continue
                s, m = r
                out[m] = out.get(m, 0) + s * c1 * c2
        return {m: c for m, c in out.items() if c != 0}

    @staticmethod
    def add(*Fs: dict, coeffs: list | None = None) -> dict:
        """Linear combination sum_i coeffs[i] * Fs[i]."""
        out: dict = {}
        coeffs = coeffs or [1] * len(Fs)
        for F, a in zip(Fs, coeffs, strict=True):
            for m, c in F.items():
                out[m] = out.get(m, 0) + a * c
        return {m: c for m, c in out.items() if c != 0}

    def dleft(self, F: dict, v: int) -> dict:
        """Left derivative d/dv."""
        out: dict = {}
        for m, c in F.items():
            if v not in m:
                continue
            p = m.index(v)
            if self.par[v]:
                nodd = sum(self.par[w] for w in m[:p])
                s = -1 if nodd % 2 else 1
                mm = m[:p] + m[p + 1:]
                out[mm] = out.get(mm, 0) + s * c
            else:
                mult = m.count(v)
                mm = m[:p] + m[p + 1:]
                out[mm] = out.get(mm, 0) + mult * c
        return {m: c for m, c in out.items() if c != 0}


def norm(F: dict) -> Fraction:
    """Largest absolute coefficient (0 for the zero polynomial)."""
    return max((abs(c) for c in F.values()), default=Fraction(0))


# ---------------------------------------------------------------------------
# The extended graded space  h + <e, e*>,  h = g_(1) + g*_(4)  (CE form, 026 (3.19)).
# Basis order: c^1..c^n (ghost 1, odd), e (ghost 2, even), e* (ghost 3, odd),
# c*_1..c*_n (ghost 4, even).  omega(c^a, c*_a) = 1 = omega(e, e*), antisymmetric.
# Doubled coordinates: psi^v = index v, xi^v = index v + N.
# ---------------------------------------------------------------------------
class Space:
    """Extended space h + <e, e*> with S'(Psi) = g(eps) S_h(psi) and the doubled bracket."""

    def __init__(self, f: list, gcoef: list) -> None:  # noqa: D107
        n = len(f)
        self.n = n
        self.N = N = 2 * n + 2
        self.ic = list(range(n))
        self.ie = n
        self.iestar = n + 1
        self.icstar = list(range(n + 2, 2 * n + 2))
        ngh = [1] * n + [2, 3] + [4] * n
        self.par1 = [g % 2 for g in ngh]
        self.alg = Alg(self.par1 + self.par1)
        W = sp.zeros(N, N)
        for a in range(n):
            W[self.ic[a], self.icstar[a]] = 1
            W[self.icstar[a], self.ic[a]] = -1
        W[self.ie, self.iestar] = 1
        W[self.iestar, self.ie] = -1
        Delta = W.inv()
        # weighted bivector Dt^{ab} = (-1)^{eps_a} Delta^{ab}  (026 W3.2)
        self.Dt = {(a, b): Fraction(int((-1) ** self.par1[a] * Delta[a, b]))
                   for a in range(N) for b in range(N) if Delta[a, b] != 0}
        self.f = f
        self.g = [Fraction(x) for x in gcoef]

    def lin(self, v: int) -> dict:
        """psi^v + xi^v (the coordinate v of u = Psi + chi)."""
        return {(v,): Fraction(1), (v + self.N,): Fraction(1)}

    def action_u(self, with_g: bool = True) -> dict:
        """S(u) = g(eps_u) * (1/2) sum f[b][c][a] c*_a c^b c^c at u = Psi + chi."""
        alg, n = self.alg, self.n
        S3: dict = {}
        for a in range(n):
            for b in range(n):
                for c in range(n):
                    fa = self.f[b][c][a]
                    if fa == 0:
                        continue
                    t = alg.mul(alg.mul(self.lin(self.icstar[a]), self.lin(self.ic[b])), self.lin(self.ic[c]))
                    S3 = alg.add(S3, t, coeffs=[1, Fraction(fa) / 2])
        if not with_g:
            return S3
        G: dict = {}
        pw = {(): Fraction(1)}
        for gr in self.g:
            if gr != 0:
                G = alg.add(G, pw, coeffs=[1, gr])
            pw = alg.mul(pw, self.lin(self.ie))
        return alg.mul(G, S3)

    def bideg(self, F: dict, p: int, q: int) -> dict:
        """Part of F with p Psi-variables and q chi-variables."""
        N = self.N
        return {m: c for m, c in F.items()
                if sum(1 for v in m if v < N) == p and sum(1 for v in m if v >= N) == q}

    def bracket(self, F: dict, G: dict) -> dict:
        """{F, G} = d_{Psi^a} F Dt^{ab} d_{chi^b} G  (026 (3.1)-(3.2), (4.2))."""
        alg, N = self.alg, self.N
        out: dict = {}
        for (a, b), w in self.Dt.items():
            dF = alg.dleft(F, a)
            if not dF:
                continue
            dG = alg.dleft(G, b + N)
            if not dG:
                continue
            out = alg.add(out, alg.mul(dF, dG), coeffs=[1, w])
        return out

    def sums(self, Su: dict, k: int, ell: int) -> tuple[dict, dict, dict, dict, list]:
        """B, R, M, P at bidegree (k, ell) from the configurations T(i,j|m,n) (026 (3.4)-(3.5))."""
        H = {}
        B: dict = {}
        R: dict = {}
        M: dict = {}
        cfg = []
        for i in range(k + 1):
            m = k - i
            for j in range(ell + 1):
                nn = ell - j
                if (i, j) == (0, 0) or (m, nn) == (0, 0):
                    continue
                for key in ((i + 1, j), (m, nn + 1)):
                    if key not in H:
                        H[key] = self.bideg(Su, *key)
                T = self.bracket(H[(i + 1, j)], H[(m, nn + 1)])
                cfg.append(((i, j, m, nn), norm(T)))
                B = self.alg.add(B, T)
                if j >= 1 and m >= 1:
                    R = self.alg.add(R, T)
                    if i >= 1 and nn >= 1:
                        M = self.alg.add(M, T)
        P = self.alg.add(R, M, coeffs=[1, -1])
        return B, R, M, P, cfg


def h_coeffs(g: list, amax: int, wrong: bool = False) -> dict:
    """[h_g]_{a,b} by sympy; wrong=True flips the sign of the g(x)g(y) term (break leg)."""
    x, y = sp.symbols("x y")
    gg = lambda z: sum(sp.Rational(c.numerator, c.denominator) * z**r for r, c in enumerate(g))  # noqa: E731
    h = gg(x + y) * (gg(x) + gg(y)) + (1 if wrong else -1) * gg(x) * gg(y)
    poly = sp.Poly(sp.expand(h), x, y)
    return {(a, b): Fraction(str(poly.coeff_monomial(x**a * y**b)))
            for a in range(amax + 1) for b in range(amax + 1)}


def closed_form(spc: Space, m22: dict, hab: Fraction, a: int, b: int) -> dict:
    """-(1/2) h_ab x^a y^b M^h_{2,2}(psi, xi)."""
    mono = tuple([spc.ie] * a + [spc.ie + spc.N] * b)
    xy = {tuple(sorted(mono)): Fraction(1)}
    return spc.alg.add(spc.alg.mul(xy, m22), coeffs=[-hab / 2])


def sl2() -> list:
    """f[b][c][a] = coefficient of e_a in [e_b, e_c]; basis (H, E, F)."""
    f = [[[0] * 3 for _ in range(3)] for _ in range(3)]
    H, E, F = 0, 1, 2
    for (b, c, a, v) in [(H, E, E, 2), (H, F, F, -2), (E, F, H, 1)]:
        f[b][c][a] = v
        f[c][b][a] = -v
    return f


def aff1() -> list:
    """2-dim non-abelian Lie algebra [X, Y] = Y (not 2-step nilpotent)."""
    f = [[[0] * 2 for _ in range(2)] for _ in range(2)]
    f[0][1][1] = 1
    f[1][0][1] = -1
    return f


def run_family(f: list, gcoef: list, sigs: list, tag: str, full: bool = True) -> dict:
    """Evaluate the checks of 026 Sec. 9 on S' = g(eps) S_h for one base algebra."""
    spc = Space(f, gcoef)
    base = Space(f, [1])
    _, _, M22, _, _ = base.sums(base.action_u(), 2, 2)
    check(f"{tag} base M^h_22 != 0 (obstruction of the base algebra, 026 (3.19))",
          norm(M22) > 0, f"|M^h_22| = {norm(M22)}, {len(M22)} monomials")
    amax = max(k + ell for k, ell in sigs)
    hab = h_coeffs(spc.g, amax)
    hwrong = h_coeffs(spc.g, amax, wrong=True)
    Su = spc.action_u()
    out = {}
    for (k, ell) in sigs:
        B, R, M, P, cfg = spc.sums(Su, k, ell)
        out[(k, ell)] = (B, R, M, P, cfg)
        nz = [c for c in cfg if c[1] > 0]
        s = f"{tag} ({k},{ell})"
        check(f"{s} 9.2-master: B'_(k,l) = 0 (extension is cyclic L_infty)", not B,
              f"|B| = {norm(B)}")
        if not full:
            continue
        check(f"{s} 9.2-nonhollow: configurations T(i,j|m,n) nonzero", len(nz) >= 2,
              f"{len(nz)}/{len(cfg)} nonzero, max |T| = {max(c[1] for c in cfg)}")
        check(f"{s} 3.15: M' = -2 P'", not spc.alg.add(M, P, coeffs=[1, 2]),
              f"|M + 2P| = {norm(spc.alg.add(M, P, coeffs=[1, 2]))}")
        pred = closed_form(spc, M22, hab[(k - 2, ell - 2)], k - 2, ell - 2)
        diff = spc.alg.add(P, pred, coeffs=[1, -1])
        check(f"{s} 9.2-closed: P' = -(1/2) h_(k-2,l-2) x^(k-2) y^(l-2) M^h_22", not diff,
              f"h = {hab[(k - 2, ell - 2)]}, |P'| = {norm(P)}, |diff| = {norm(diff)}")
        check(f"{s} 9.2-nonzero: P'_(k,l) != 0 iff [h]_(k-2,l-2) != 0",
              (norm(P) > 0) == (hab[(k - 2, ell - 2)] != 0), f"|P'| = {norm(P)}, {len(P)} monomials")
        # break leg: the variant with +g(x)g(y) (sign of the Jacobi cross term flipped) must FAIL
        wrong = closed_form(spc, M22, hwrong[(k - 2, ell - 2)], k - 2, ell - 2)
        check(f"{s} break leg: closed form with +g(x)g(y) (sign flipped) is rejected",
              bool(spc.alg.add(P, wrong, coeffs=[1, -1])), "")
        # non-augmented control: B = 0 while the augmented residual R = M/2 = -P != 0
        check(f"{s} 9.2-nonaug: augmented residual R = -P (nonzero iff [h] != 0) while non-augmented B = 0",
              not spc.alg.add(R, P) and (norm(R) > 0) == (hab[(k - 2, ell - 2)] != 0) and not B,
              f"|R| = {norm(R)}")
    return out


def main() -> int:
    """Run all checks; exit code 1 on any FAIL."""
    ap = argparse.ArgumentParser()
    ap.add_argument("--kmax", type=int, default=5, help="largest k, l tested (sum <= kmax + 1 also tested)")
    args = ap.parse_args()
    print(f"seed = {SEED}")
    random.seed(SEED)
    sigs = [(k, ell) for k in range(2, args.kmax + 1) for ell in range(2, args.kmax + 1)]
    sigs += [(2, args.kmax + 1), (args.kmax + 1, 2)]
    rmax = max(k + ell for k, ell in sigs) - 4
    gexp = [Fraction(1, factorial(r)) for r in range(rmax + 1)]
    print(f"signatures: {sigs}; g = exp truncated at eps^{rmax}")

    # 9.2-hexp: closed form of h for g = exp (truncation at eps^8 is exact for a + b <= 8)
    hx = h_coeffs([Fraction(1, factorial(r)) for r in range(9)], 8)
    bad = [(a, b) for a in range(9) for b in range(9) if a + b <= 8
           and hx[(a, b)] != Fraction(2**a + 2**b - 1, factorial(a) * factorial(b))]
    check("9.2-hexp: [h_exp]_ab = (2^a + 2^b - 1)/(a! b!) for a + b <= 8", not bad, f"mismatches {bad}")

    run_family(sl2(), gexp, sigs, "sl2/exp")

    # 9.2-cancel: g = 1 + eps - eps^2/4 kills [h]_{1,1} (P'_{3,3}) but not [h]_{0,2}, [h]_{2,0}
    gc = [Fraction(1), Fraction(1), Fraction(-1, 4)]
    hc = h_coeffs(gc, 4)
    res = run_family(sl2(), gc, [(3, 3), (2, 4), (4, 2)], "sl2/cancel")
    B, R, M, P, cfg = res[(3, 3)]
    nz = [c for c in cfg if c[1] > 0]
    check("9.2-cancel: g = 1 + eps - eps^2/4 gives P'_33 = 0 with >= 2 nonzero configurations",
          hc[(1, 1)] == 0 and not P and len(nz) >= 2,
          f"[h]_11 = {hc[(1, 1)]}, nonzero configurations {len(nz)}: {[c[0] for c in nz]}")
    check("9.2-cancel: same g gives P'_24, P'_42 != 0 ([h]_02 = [h]_20 = 1/2)",
          norm(res[(2, 4)][3]) > 0 and norm(res[(4, 2)][3]) > 0 and hc[(0, 2)] == Fraction(1, 2),
          f"|P'_24| = {norm(res[(2, 4)][3])}, |P'_42| = {norm(res[(4, 2)][3])}")

    # second base algebra
    run_family(aff1(), gexp[: 4], [(2, 2), (2, 3), (3, 3), (2, 4)], "aff1/exp")

    # break leg on the master equation: a Jacobi-violating bracket (random antisymmetric f)
    rnd = [[[0] * 3 for _ in range(3)] for _ in range(3)]
    for b in range(3):
        for c in range(b + 1, 3):
            for a in range(3):
                v = random.randint(-3, 3)
                rnd[b][c][a], rnd[c][b][a] = v, -v
    spc = Space(rnd, gexp[:2])
    Su = spc.action_u()
    B, R, M, P, _ = spc.sums(Su, 2, 3)
    check("break leg: Jacobi-violating f gives B'_23 != 0 (master-equation check is live)",
          norm(B) > 0, f"|B| = {norm(B)}")
    check("break leg: Jacobi-violating f gives M' != -2P' at (2,3) (3.15 check is live)",
          bool(spc.alg.add(M, P, coeffs=[1, 2])), f"|M + 2P| = {norm(spc.alg.add(M, P, coeffs=[1, 2]))}")

    npass = sum(ok for _, ok in RESULTS)
    print(f"summary: {npass}/{len(RESULTS)} PASS (seed {SEED})")
    return 0 if npass == len(RESULTS) else 1


if __name__ == "__main__":
    sys.exit(main())
