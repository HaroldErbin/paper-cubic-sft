"""
Companion script for derivation record 078 (PH31's falsifier).

Computes the joint rank, over sampled relative momenta Delta, of
pi_{<=K} pi_W Phi_2 on graded-symmetric inputs of level <= L, and compares it
with dim W^even_{<=K}(P), W = c_0^+ c_0^- H^down (record 074 (2.1)).

Method (record 078 section 1):
- rank pi_{<=K} pi_W Phi_2 = rank of the matrix of three-point amplitudes
  <V_3'| B (x) A_1 (x) A_2>, B over the Fock basis of H^down at ghost number 2,
  levels N, Nbar <= K (BPZ pairs W non-degenerately with H^down);
- maps of R2's V_3' (032 section 1) in the special-leg coordinate u:
  f_1(w) = ((a+1) w + g) / (2 beta ((a-1) w + g)), f_2 = -f_1, h_0(w) = 1/w;
- free-field Wick rules: matter Neumann coefficients
  N^{rs}_{mn} = [w^{m-1} w'^{n-1}] h_r'(w) h_s'(w') / (h_r(w) - h_s(w'))^2
  (singular part subtracted for r = s), linear terms
  L^r_m = sum_s l_s [w^{m-1}] (h_r'(w)/(h_r(w) - z_s) - delta_rs / w);
  ghosts by the sphere determinant
  <b(v_1)..b(v_N) c(u_1)..c(u_{N+3})> ~ (-1)^{N(N-1)/2} det[[1/(v_j - u_i)]; [u_i^k]_{k<3}]
  applied mode by mode (multilinearity);
- exact ranks over F_p (p = 2^31 - 1) with random momenta (Schwartz-Zippel);
  float SVD with complex Gaussian momenta as the second rank route.

What is verified (named checks, PASS/FAIL):
- C2-count: block dimensions from the Fock enumeration equal the generating
  function count (independent route).
- C1-route2-tachyon: amplitudes for tachyon inputs (all rows at K = 2) equal
  the operator-algebra route (ket from 071 (B.3), (B.6); BPZ bra and vacuum
  expectation value by anticommutation), matter and ghosts.
- C1-exchange: Phi_2(B@k2, A@k1) = (-1)^{N - Nbar} Phi_2(A@k1, B@k2) row by
  row on oscillator inputs (071 C3, now with ghosts and oscillators).
- C3-K<K>-L<L>: the rank table entries (exact mod p), with the float SVD route
  for the small entries.
- C4-*: origin of the deficit at alpha'_v = 0: it disappears for full-H inputs
  and for alpha'_v = 1/2; the conservation-law functionals of record 078 (4.3),
  chi o (b_1^- - z^2 b_-1^-), vanish on every sampled H_0 column and account
  for the whole ker-b_0^- cokernel at K = 2.
- BREAK-*: deliberately wrong maps/inputs must show a deficit; the sign-flipped
  conservation operator must not vanish.

Not verified: anything at unbounded level (PH31's extended statement);
d_eff = 2 matter components only (ghost sector complete); beta = 3/2;
vertex points (gamma', alpha'_v) = (3, 0), (2, 0), (3, 1/2); the L-type
relations (level matching) are measured, not constructed; the K = 2, L = 3
entry is a capped random column sample (the full scan and K = 3 are in the
scratch folder, record 078 section 3).
"""

from __future__ import annotations

import itertools
import json
import random
import sys
import time
from fractions import Fraction
from functools import lru_cache
from pathlib import Path

import numpy as np
import sympy as sp

PMOD = 2**31 - 1
SCRATCH = Path(__file__).resolve().parent / "output" / "ph31-rank"
RESULTS: list[tuple[str, bool, str]] = []


def report(name: str, ok: bool, detail: str = "") -> None:
    """Print and store one labelled PASS/FAIL line."""
    RESULTS.append((name, ok, detail))
    print(f"{'PASS' if ok else 'FAIL'}  {name}  {detail}", flush=True)


def fmod(x: Fraction) -> int:
    """Reduce a rational number mod PMOD."""
    return x.numerator % PMOD * pow(x.denominator % PMOD, PMOD - 2, PMOD) % PMOD


# ---------------------------------------------------------------- Neumann data
W, V = sp.symbols("w v")


def coeff2(expr: sp.Expr, a: int, b: int) -> Fraction:
    """[w^a v^b] of a rational function analytic at (0, 0)."""
    e = sp.diff(expr, W, a, V, b) if (a or b) else expr
    val = sp.Rational(
        sp.cancel(e.subs({W: 0, V: 0}) / (sp.factorial(a) * sp.factorial(b)))
    )
    return Fraction(int(val.p), int(val.q))


def coeff1(expr: sp.Expr, a: int) -> Fraction:
    """[w^a] of a rational function analytic at 0."""
    e = sp.diff(expr, W, a) if a else expr
    val = sp.Rational(sp.simplify(e.subs(W, 0) / sp.factorial(a)))
    return Fraction(int(val.p), int(val.q))


class Vertex:
    """Neumann data of the circle map for the maps f_1, f_2 = -f_1, h_0 = 1/w."""

    def __init__(self, beta, gamma, alpha_v, mmax: int, break_mode: str = ""):
        a, g, bt = sp.Rational(alpha_v), sp.Rational(gamma), sp.Rational(beta)
        f1 = ((a + 1) * W + g) / (2 * bt * ((a - 1) * W + g))
        self.h = {1: f1, 2: -f1}
        self.z = {1: f1.subs(W, 0), 2: -f1.subs(W, 0)}
        self.mmax = mmax
        self.break_mode = break_mode
        hv = {r: self.h[r].subs(W, V) for r in (1, 2)}
        dh = {r: sp.diff(self.h[r], W) for r in (1, 2)}
        dhv = {r: dh[r].subs(W, V) for r in (1, 2)}
        M = mmax
        # matter: N^{rs}_{mn}, r, s in {0,1,2}; leg 0 closed form, N^{00} = 0
        self.N = {}
        e12 = sp.cancel(dh[1] * dhv[2] / (self.h[1] - hv[2]) ** 2)
        e11 = sp.cancel(dh[1] * dhv[1] / (self.h[1] - hv[1]) ** 2 - 1 / (W - V) ** 2)
        e22 = sp.cancel(dh[2] * dhv[2] / (self.h[2] - hv[2]) ** 2 - 1 / (W - V) ** 2)
        for m in range(1, M + 1):
            for n in range(1, M + 1):
                self.N[(1, 2, m, n)] = coeff2(e12, m - 1, n - 1)
                self.N[(2, 1, n, m)] = self.N[(1, 2, m, n)]
                self.N[(1, 1, m, n)] = coeff2(e11, m - 1, n - 1)
                self.N[(2, 2, m, n)] = coeff2(e22, m - 1, n - 1)
                self.N[(0, 0, m, n)] = Fraction(0)
                for s in (1, 2):
                    # N^{0s}_{mn} = -n [w^n] h_s^m
                    val = -n * coeff1(self.h[s] ** m, n)
                    self.N[(0, s, m, n)] = val
                    self.N[(s, 0, n, m)] = val
        if break_mode == "no-cross":
            for key in self.N:
                if key[0] != key[1]:
                    self.N[key] = Fraction(0)
        # matter linear: a^{r,s}_m
        self.a = {}
        for m in range(1, M + 1):
            for s in (1, 2):
                self.a[(0, s, m)] = -Fraction(
                    int(sp.Rational(self.z[s] ** m).p),
                    int(sp.Rational(self.z[s] ** m).q),
                )
                for r in (1, 2):
                    ex = dh[r] / (self.h[r] - self.z[s])
                    if r == s:
                        ex = sp.cancel(ex - 1 / W)
                    self.a[(r, s, m)] = coeff1(ex, m - 1)
        # ghosts: E^{rs}_{nm} for b_n @ r (n <= -2), c_m @ s (m <= 1)
        self.E = {}
        bmodes = range(-M - 1, -1)
        cmodes = range(-M, 2)
        g12 = sp.cancel(dh[1] ** 2 / dhv[2] / (self.h[1] - hv[2]))
        g21 = sp.cancel(dh[2] ** 2 / dhv[1] / (self.h[2] - hv[1]))
        g11 = sp.cancel(dh[1] ** 2 / dhv[1] / (self.h[1] - hv[1]) - 1 / (W - V))
        g22 = sp.cancel(dh[2] ** 2 / dhv[2] / (self.h[2] - hv[2]) - 1 / (W - V))
        gg = {(1, 2): g12, (2, 1): g21, (1, 1): g11, (2, 2): g22}
        for n in bmodes:
            for m in cmodes:
                for (r, s), ex in gg.items():
                    self.E[(r, s, n, m)] = coeff2(ex, -n - 2, 1 - m)
                for s in (1, 2):
                    # b at leg 0: [w'^{1-m}] h_s^{1-n} / h_s'
                    self.E[(0, s, n, m)] = coeff1(self.h[s] ** (1 - n) / dh[s], 1 - m)
                    # c at leg 0: [w^{-n-2}] h_r'^2 h_r^{-2-m} (m <= -2)
                    self.E[(s, 0, n, m)] = (
                        coeff1(dh[s] ** 2 * self.h[s] ** (-2 - m), -n - 2)
                        if m <= -2
                        else Fraction(0)
                    )
                self.E[(0, 0, n, m)] = Fraction(0)
        # zero-mode rows Z^s_{k,m}
        self.Z = {}
        for m in cmodes:
            for k in range(3):
                for s in (1, 2):
                    self.Z[(s, k, m)] = coeff1(self.h[s] ** k / dh[s], 1 - m)
                self.Z[(0, k, m)] = Fraction(-1) if k == 1 + m else Fraction(0)
        if break_mode == "ghost-no-cross":
            for key in self.E:
                if key[0] != key[1]:
                    self.E[key] = Fraction(0)


# ------------------------------------------------------------------ Fock basis
def partitions_colored(level: int, d: int) -> list[tuple]:
    """Multisets of (mu, n), n >= 1, mu < d, with sum n = level."""
    out = []
    items = [(mu, n) for n in range(1, level + 1) for mu in range(d)]

    def rec(start: int, rem: int, acc: list) -> None:
        if rem == 0:
            out.append(tuple(acc))
            return
        for i in range(start, len(items)):
            mu, n = items[i]
            if n <= rem:
                rec(i, rem - n, acc + [(mu, n)])

    rec(0, level, [])
    return out


def ghost_sets(level: int) -> list[tuple[tuple, int]]:
    """Fermionic sets of b_{-n}, c_{-n} (n >= 1) of total level; (ops, q)."""
    modes = [("b", -n) for n in range(1, level + 1)] + [
        ("c", -n) for n in range(1, level + 1)
    ]
    out = []
    for k in range(len(modes) + 1):
        for sub in itertools.combinations(modes, k):
            if sum(-n for _, n in sub) == level:
                q = sum(1 if t == "c" else -1 for t, _ in sub)
                out.append((sub, q))
    return out


def chiral_states(lmax: int, d: int) -> list[tuple[int, int, tuple, tuple]]:
    """(level, q, matter, ghost ops) for one chirality, level <= lmax."""
    out = []
    for lev in range(lmax + 1):
        for lm in range(lev + 1):
            for mat in partitions_colored(lm, d):
                for gh, q in ghost_sets(lev - lm):
                    out.append((lev, q, mat, gh))
    return out


def closed_basis(lmax_h: int, d: int, qtot: int, level_matched: bool) -> list[dict]:
    """Closed-string monomials on c_1 cbar_1|0> with q + qbar = qtot."""
    cs = chiral_states(lmax_h, d)
    out = []
    for lh, qh, mh, gh in cs:
        for la, qa, ma, ga in cs:
            if qh + qa != qtot:
                continue
            if level_matched and lh != la:
                continue
            out.append(
                {
                    "N": lh,
                    "Nb": la,
                    "mat": tuple((0, mu, n) for mu, n in mh)
                    + tuple((1, mu, n) for mu, n in ma),
                    "gh": tuple((0, t, n) for t, n in gh)
                    + tuple((1, t, n) for t, n in ga),
                }
            )
    return out


def is_annihilator(op: tuple) -> bool:
    _, t, n = op
    return (t == "b" and n >= -1) or (t == "c" and n >= 2)


def reduce_on_vacuum(ops: tuple) -> list[tuple[int, tuple]]:
    """Normal-order a string of ghost modes on |0>: creation modes only."""
    idx = [i for i, op in enumerate(ops) if is_annihilator(op)]
    if not idx:
        return [(1, ops)]
    i = idx[-1]
    x = ops[i]
    out = []
    sign = 1
    for j in range(i + 1, len(ops)):
        y = ops[j]
        if y[0] == x[0] and y[1] != x[1] and y[2] + x[2] == 0:
            rest = ops[:i] + ops[i + 1 : j] + ops[j + 1 :]
            for s2, o2 in reduce_on_vacuum(rest):
                out.append((sign * s2, o2))
        sign = -sign
    return out


def state_strings(st: dict, zero: str = "") -> list[tuple[int, tuple, tuple]]:
    """(coef, matter, ghost string on |0>) for a monomial; zero = '', 'c0+'."""
    base = st["gh"] + ((0, "c", 1), (1, "c", 1))
    pref = {
        "": [()],
        "c0+": [((0, "c", 0),), ((1, "c", 0),)],
        "c0": [((0, "c", 0),)],
        "cb0": [((1, "c", 0),)],
        "c0cb0": [((0, "c", 0), (1, "c", 0))],
    }[zero]
    out = []
    for p in pref:
        for s, o in reduce_on_vacuum(p + base):
            out.append((s, st["mat"], o))
    return out


# ------------------------------------------------------------------ amplitudes
def partition_sign(seq: list, key) -> tuple[int, list, list]:
    """Stable partition (key True first) of fermions; returns sign and parts."""
    first, second, inv, n_second = [], [], 0, 0
    for x in seq:
        if key(x):
            first.append(x)
            inv += n_second
        else:
            second.append(x)
            n_second += 1
    return (-1) ** inv, first, second


class Field:
    """Arithmetic over F_p (mod = PMOD) or Q (mod = None, Fractions)."""

    def __init__(self, mod: int | None):
        self.mod = mod

    def conv(self, x: Fraction | int) -> int | Fraction:
        if self.mod is None:
            return Fraction(x)
        return fmod(Fraction(x))

    def red(self, x):
        return x % self.mod if self.mod else x

    def inv(self, x):
        return pow(x, self.mod - 2, self.mod) if self.mod else 1 / Fraction(x)


def det_field(mat: list[list], fld: Field):
    """Determinant by Gaussian elimination over the field."""
    a = [row[:] for row in mat]
    n = len(a)
    det = 1
    for c in range(n):
        piv = next((r for r in range(c, n) if fld.red(a[r][c])), None)
        if piv is None:
            return 0
        if piv != c:
            a[c], a[piv] = a[piv], a[c]
            det = -det
        det = fld.red(det * a[c][c])
        inv = fld.inv(a[c][c])
        for r in range(c + 1, n):
            f = fld.red(a[r][c] * inv)
            if f:
                a[r] = [fld.red(x - f * y) for x, y in zip(a[r], a[c])]
    return fld.red(det)


class Amplitudes:
    """Three-point amplitudes <V_3'| B (x) A_1 (x) A_2>, plane-wave prefactor dropped."""

    def __init__(self, vx: Vertex, d: int, fld: Field):
        self.vx = vx
        self.d = d
        self.f = fld
        self.Np = {k: fld.conv(x) for k, x in vx.N.items()}
        self.ap = {k: fld.conv(x) for k, x in vx.a.items()}
        self.Ep = {k: fld.conv(x) for k, x in vx.E.items()}
        self.Zp = {k: fld.conv(x) for k, x in vx.Z.items()}
        self.gcache: dict = {}
        self.mcache: dict = {}

    def ghost_amp(self, g0: tuple, g1: tuple, g2: tuple):
        key = (g0, g1, g2)
        if key in self.gcache:
            return self.gcache[key]
        seq = (
            [(0,) + op for op in g0]
            + [(1,) + op for op in g1]
            + [(2,) + op for op in g2]
        )
        sgn, hol, ahol = partition_sign(seq, lambda x: x[1] == 0)
        val = sgn
        for part in (hol, ahol):
            s2, bs, cs = partition_sign(part, lambda x: x[2] == "b")
            nb = len(bs)
            if len(cs) != nb + 3:
                val = 0
                break
            rows = [[self.Ep[(b[0], c[0], b[3], c[3])] for c in cs] for b in bs]
            rows += [[self.Zp[(c[0], k, c[3])] for c in cs] for k in range(3)]
            val = self.f.red(
                val * s2 * (-1) ** (nb * (nb - 1) // 2) * det_field(rows, self.f)
            )
        self.gcache[key] = val
        return val

    def msum(self, osc: tuple, ell: tuple):
        """Wick sum for one chirality and one component; osc = ((leg, n), ...)."""
        if not osc:
            return 1
        key = (osc, ell)
        if key in self.mcache:
            return self.mcache[key]
        (r, m), rest = osc[0], osc[1:]
        lin = self.f.red(sum(ell[s - 1] * self.ap[(r, s, m)] for s in (1, 2)))
        tot = lin * self.msum(rest, ell)
        for j, (s, n) in enumerate(rest):
            nn = self.Np[(r, s, m, n)]
            if nn:
                tot += nn * self.msum(rest[:j] + rest[j + 1 :], ell)
        tot = self.f.red(tot)
        self.mcache[key] = tot
        return tot

    def matter_amp(self, m0: tuple, m1: tuple, m2: tuple, l1: tuple, l2: tuple):
        val = 1
        for ch in (0, 1):
            for mu in range(self.d):
                osc = tuple(
                    (leg, n)
                    for leg, mm in ((0, m0), (1, m1), (2, m2))
                    for c, nu, n in mm
                    if c == ch and nu == mu
                )
                val = self.f.red(val * self.msum(osc, (l1[mu], l2[mu])))
        return val

    def amp(self, B: list, A1: list, A2: list, l1: tuple, l2: tuple):
        """B, A1, A2 as lists of (coef, matter, ghost string)."""
        mat = self.matter_amp(B[0][1], A1[0][1], A2[0][1], l1, l2)
        if not mat:
            return 0
        g = 0
        for cb, _, gb in B:
            for c1, _, g1 in A1:
                for c2, _, g2 in A2:
                    g += cb * c1 * c2 * self.ghost_amp(gb, g1, g2)
        return self.f.red(mat * g)


# ----------------------------------------------------------------- linear alg.
class Echelon:
    """Incremental column-space basis over F_p."""

    def __init__(self, n: int):
        self.n = n
        self.piv: dict[int, np.ndarray] = {}

    def add(self, v: np.ndarray) -> bool:
        v = v % PMOD
        for p, b in self.piv.items():
            if v[p]:
                v = (v - v[p] * b) % PMOD
        nz = np.nonzero(v)[0]
        if len(nz) == 0:
            return False
        p = int(nz[0])
        v = v * pow(int(v[p]), PMOD - 2, PMOD) % PMOD
        for q in list(self.piv):
            if self.piv[q][p]:
                self.piv[q] = (self.piv[q] - self.piv[q][p] * v) % PMOD
        self.piv[p] = v
        return True

    @property
    def rank(self) -> int:
        return len(self.piv)


def rank_modp(rows: list[np.ndarray]) -> int:
    e = Echelon(len(rows[0]) if rows else 0)
    for r in rows:
        e.add(np.array(r, dtype=np.int64))
    return e.rank


def left_null(ech: Echelon) -> list[np.ndarray]:
    """Basis of y with y . b = 0 for every basis column b (reduced echelon)."""
    piv = sorted(ech.piv)
    free = [i for i in range(ech.n) if i not in ech.piv]
    out = []
    for f in free:
        y = np.zeros(ech.n, dtype=np.int64)
        y[f] = 1
        # y . b_p = b_p[f] + y[p] = 0 for each pivot column b_p (b_p[p] = 1, b_p[q] = 0 for other pivots)
        for p in piv:
            y[p] = (-ech.piv[p][f]) % PMOD
        out.append(y)
    return out


# ------------------------------------------------------------------- counting
def gf_count(K: int, d: int) -> dict[tuple[int, int], int]:
    """dim of H^down at gh 2 (equivalently W at gh 4) per (N, Nbar), N, Nbar <= K.

    Generating function prod_n (1-q^n)^{-d} (1+y q^n)(1+q^n/y) per chirality,
    coefficient of y^0 in the product of the two chiralities.
    """

    def chiral() -> dict[tuple[int, int], int]:
        poly = {(0, 0): 1}  # (level, ycharge) -> count
        for n in range(1, K + 1):
            for _ in range(d):  # bosonic factor 1/(1-q^n)
                new = {}
                for (lv, y), c in poly.items():
                    k = 0
                    while lv + k * n <= K:
                        key = (lv + k * n, y)
                        new[key] = new.get(key, 0) + c
                        k += 1
                poly = new
            for sgn in (1, -1):  # fermionic factor (1 + y^{sgn} q^n)
                new = dict(poly)
                for (lv, y), c in poly.items():
                    if lv + n <= K:
                        key = (lv + n, y + sgn)
                        new[key] = new.get(key, 0) + c
                poly = new
        return poly

    ch = chiral()
    out: dict[tuple[int, int], int] = {}
    for (n1, y1), c1 in ch.items():
        for (n2, y2), c2 in ch.items():
            if y1 + y2 == 0:
                out[(n1, n2)] = out.get((n1, n2), 0) + c1 * c2
    return out


# ------------------------------------------------------------------ the scan
def row_label(st: dict) -> str:
    def op(o):
        c, t, n = o
        return f"{t}{'~' if c else ''}{n}"

    mat = " ".join(f"a{'~' if c else ''}{n}^{mu}" for c, mu, n in st["mat"])
    gh = " ".join(op(o) for o in st["gh"])
    return f"({st['N']},{st['Nb']})[{mat}|{gh}]"


def input_basis(
    L: int, d: int, only_matter: bool = False, full: bool = False
) -> list[tuple[dict, str]]:
    """H_0 at ghost number 2, N = Nbar <= L; full=True: all of H at gh 2, N, Nbar <= L."""
    if full:
        ins = [(st, "") for st in closed_basis(L, d, 0, False)]
        ins += [(st, z) for z in ("c0", "cb0") for st in closed_basis(L, d, -1, False)]
        ins += [(st, "c0cb0") for st in closed_basis(L, d, -2, False)]
        return ins
    ins = [(st, "") for st in closed_basis(L, d, 0, True)]
    ins += [(st, "c0+") for st in closed_basis(L, d, -1, True)]
    if only_matter:
        ins = [(st, z) for st, z in ins if not st["gh"] and not z]
    return ins


def run_entry(  # noqa: PLR0913
    amps: Amplitudes,
    K: int,
    L: int,
    d: int,
    rng: random.Random,
    P: tuple,
    max_delta: int = 12,
    only_matter: bool = False,
    log: list | None = None,
    full: bool = False,
    antisym: bool = False,
    ins_override: list | None = None,
) -> dict:
    """Joint rank over sampled Delta of the even-row amplitude matrix."""
    rows = [st for st in closed_basis(K, d, 0, False) if (st["N"] - st["Nb"]) % 2 == 0]
    rstr = [state_strings(st) for st in rows]
    ins = (
        ins_override
        if ins_override is not None
        else input_basis(L, d, only_matter, full)
    )
    sg = -1 if antisym else 1
    istr = [state_strings(st, z) for st, z in ins]
    ech = Echelon(len(rows))
    inv2 = pow(2, PMOD - 2, PMOD)
    hist = []
    ncols = 0
    t0 = time.time()
    for it in range(max_delta):
        D = tuple(rng.randrange(PMOD) for _ in range(d))
        l1 = tuple((p * inv2 + x) % PMOD for p, x in zip(P, D))
        l2 = tuple((p * inv2 - x) % PMOD for p, x in zip(P, D))
        added = 0
        pairs = [(i, j) for i in range(len(ins)) for j in range(len(ins))]
        rng.shuffle(pairs)
        for i, j in pairs:
            col = np.array(
                [
                    (
                        amps.amp(B, istr[i], istr[j], l1, l2)
                        + sg * amps.amp(B, istr[j], istr[i], l2, l1)
                    )
                    % PMOD
                    for B in rstr
                ],
                dtype=np.int64,
            )
            ncols += 1
            if ech.add(col):
                added += 1
            if ech.rank == len(rows):
                break
        hist.append(ech.rank)
        if log is not None:
            log.append(
                f"K={K} L={L} sample {it}: rank {ech.rank}/{len(rows)} (+{added}) t={time.time() - t0:.1f}s"
            )
            print(log[-1], flush=True)
        if ech.rank == len(rows) or (it >= 1 and added == 0):
            break
    # per-block ranks
    blocks = sorted({(st["N"], st["Nb"]) for st in rows})
    per_block = {}
    basis = list(ech.piv.values())
    for blk in blocks:
        idx = [k for k, st in enumerate(rows) if (st["N"], st["Nb"]) == blk]
        r = rank_modp([b[idx] for b in basis]) if basis else 0
        per_block[f"{blk[0]},{blk[1]}"] = (r, len(idx))
    nulls = left_null(ech)
    null_support = [[row_label(rows[k]) for k in np.nonzero(y)[0]] for y in nulls[:20]]
    return {
        "K": K,
        "L": L,
        "rows_even": len(rows),
        "inputs": len(ins),
        "columns_used": ncols,
        "n_delta": len(hist),
        "rank_history": hist,
        "rank": ech.rank,
        "deficit": len(rows) - ech.rank,
        "per_block": per_block,
        "null_support": null_support,
        "time_s": round(time.time() - t0, 1),
    }


# --------------------------------------------------------------------- checks
STD6 = ((0, "c", -1), (0, "c", 0), (0, "c", 1), (1, "c", -1), (1, "c", 0), (1, "c", 1))


def vev(ops: tuple) -> int:
    """<0| ops |0> with <0|c_{-1}c_0c_1 cbar_{-1}cbar_0cbar_1|0> = 1 (operator algebra)."""
    tot = 0
    for s, o in reduce_on_vacuum(ops):
        if sorted(o) != sorted(STD6) or len(o) != 6:
            continue
        perm = [STD6.index(x) for x in o]
        inv = sum(1 for i in range(6) for j in range(i + 1, 6) if perm[i] > perm[j])
        tot += s * (-1) ** inv
    return tot


def bpz_op(op: tuple) -> tuple[int, tuple]:
    """BPZ with I(w) = 1/w: c_m -> -c_{-m}, b_m -> b_{-m}."""
    c, t, n = op
    return (-1 if t == "c" else 1), (c, t, -n)


def route2_tachyon(
    vx: Vertex, K: int, d: int, l1: tuple, l2: tuple
) -> list[tuple[dict, Fraction]]:
    """<bpz(B)| rho^{-4} c cbar(z1) c cbar(z2) exp(sum K_n.alpha_{-n}/n + cc)|P>, all rows."""
    z1, z2 = Fraction(str(vx.z[1])), Fraction(str(vx.z[2]))
    rho1 = Fraction(str(sp.diff(vx.h[1], W).subs(W, 0)))
    rho2 = -rho1
    ms = range(-(K + 1), 2)
    ket = []
    for m1, m2, m3, m4 in itertools.product(ms, ms, ms, ms):
        cf = z1 ** (1 - m1) * z1 ** (1 - m2) * z2 ** (1 - m3) * z2 ** (1 - m4)
        ket.append((cf, ((0, "c", m1), (1, "c", m2), (0, "c", m3), (1, "c", m4))))
    pref = 1 / (rho1**2 * rho2**2)
    out = []
    rows = closed_basis(K, d, 0, False)
    for st in rows:
        g = st["gh"] + ((0, "c", 1), (1, "c", 1))
        F = len(g)
        sgn = (-1) ** (F * (F - 1) // 2)
        bra = []
        for op in reversed(g):
            s, o = bpz_op(op)
            sgn *= s
            bra.append(o)
        gval = sum(cf * vev(tuple(bra) + k) for cf, k in ket)
        mval = Fraction(1)
        for c, mu, n in st["mat"]:
            Kn = l1[mu] * z1**n + l2[mu] * z2**n
            mval *= -Kn
        out.append((st, sgn * gval * mval * pref))
    return out


def check_neumann_log(vx: Vertex) -> None:
    """N^{12}_{mn} = m n [w^m v^n] log(h1(w) - h2(v)); a^{rs}_m = m [w^m] log((h_r - z_s)/w^d)."""
    h1, h2 = vx.h[1], vx.h[2].subs(W, V)
    lg = sp.log(sp.cancel((h1 - h2) / (vx.z[1] - vx.z[2])))
    ok = True
    worst = ""
    ser = sp.series(lg, W, 0, 4).removeO()
    for m in range(1, 4):
        cm = sp.series(ser.coeff(W, m), V, 0, 4).removeO()
        for n in range(1, 4):
            val = m * n * sp.Rational(cm.coeff(V, n))
            if Fraction(int(val.p), int(val.q)) != vx.N[(1, 2, m, n)]:
                ok, worst = False, f"N12[{m},{n}]"
    for r in (1, 2):
        for s in (1, 2):
            ex = (vx.h[r] - vx.z[s]) / (W if r == s else 1)
            ser = sp.series(sp.log(sp.cancel(ex)), W, 0, 4).removeO()
            for m in range(1, 4):
                val = m * sp.Rational(ser.coeff(W, m))
                if Fraction(int(val.p), int(val.q)) != vx.a[(r, s, m)]:
                    ok, worst = False, f"a[{r},{s},{m}]"
    report(
        "C1-neumann-log",
        ok,
        "matter Neumann/linear coefficients vs log-series route " + worst,
    )


def check_exchange(
    amps: Amplitudes, K: int, L: int, d: int, rng: random.Random, npairs: int
) -> bool:
    """Phi_2(B@k2, A@k1) = (-1)^{N-Nbar} Phi_2(A@k1, B@k2), row by row (071 C3)."""
    rows = closed_basis(K, d, 0, False)
    rstr = [state_strings(st) for st in rows]
    ins = input_basis(L, d, full=True)
    istr = [state_strings(st, z) for st, z in ins]
    l1 = tuple(rng.randrange(PMOD) for _ in range(d))
    l2 = tuple(rng.randrange(PMOD) for _ in range(d))
    ok, nz = True, 0
    for _ in range(npairs):
        i, j = rng.randrange(len(ins)), rng.randrange(len(ins))
        ks = 1  # every input has ghost number 2: Grassmann even, no Koszul sign
        for st, B in zip(rows, rstr):
            a = amps.amp(B, istr[i], istr[j], l1, l2)
            b = amps.amp(B, istr[j], istr[i], l2, l1)
            target = ks * (-1) ** ((st["N"] - st["Nb"]) % 2) * a % PMOD
            if a:
                nz += 1
            if b % PMOD != target:
                ok = False
    return ok, nz


def string_levels(mat: tuple, gh: tuple) -> tuple[int, int]:
    """(N, Nbar) of a matter tuple and a ghost string on |0> (c_1|0> has level 0)."""
    lev = [1, 1]
    for c, _, n in mat:
        lev[c] += n
    for c, _, n in gh:
        lev[c] += -n
    return lev[0], lev[1]


ZPREF = {"": (), "c0": ((0, "c", 0),), "cb0": ((1, "c", 0),), "c0cb0": ((0, "c", 0), (1, "c", 0))}


def ob_functionals(vx: Vertex, K: int, d: int, sgn: int = -1, all_zero_modes: bool = False) -> list[list]:
    """y_chi = <V| [(b_{-1} - z^2 b_1) - c.c.]^{(0)} chi (x) . (x) . > for chi in H^down, gh 3.

    Record 078 (4.3) in the leg-0 frame: v = beta (u^2 - z^2) d_u = -beta (1 - z^2 w^2) d_w,
    so the conservation law reads (b_{-1} - z^2 b_1)^{(0)} = -/+ b_0 at legs 1, 2. Kept are the
    chi whose y_chi only involves output levels N, Nbar <= K. sgn = +1 is the break leg.
    """
    z2 = Fraction(str(vx.z[1])) ** 2
    out = []
    chis = [(z, st) for z in ZPREF for st in closed_basis(K + 1, d, 1 - len(ZPREF[z]), False)]
    if not all_zero_modes:
        chis = [(z, st) for z, st in chis if z == ""]
    for z, st in chis:
        base = ZPREF[z] + st["gh"] + ((0, "c", 1), (1, "c", 1))
        terms = [
            (Fraction(1), (0, "b", -1)),
            (sgn * z2, (0, "b", 1)),
            (Fraction(-1), (1, "b", -1)),
            (-sgn * z2, (1, "b", 1)),
        ]
        strings = []
        for cf, op in terms:
            for s2, o in reduce_on_vacuum((op,) + base):
                strings.append((cf * s2, st["mat"], o))
        if not strings:
            continue
        levs = [string_levels(st["mat"], o) for _, _, o in strings]
        if max(max(lv) for lv in levs) > K:
            continue
        if all((a - b) % 2 for a, b in levs):
            continue  # only odd rows: trivial on symmetric inputs
        if all_zero_modes:
            strings = [(fmod(c), m_, g) for c, m_, g in strings]
        out.append(strings)
    return out


def check_ob_identity(amps: Amplitudes, vx: Vertex, K: int, L: int, d: int, rng: random.Random, P: tuple, sgn: int):
    """Evaluate the y_chi on H_0 symmetric columns (must vanish) and on full-H ones (rank)."""
    ys = ob_functionals(vx, K, d, sgn)
    inv2 = pow(2, PMOD - 2, PMOD)
    D = tuple(rng.randrange(PMOD) for _ in range(d))
    l1 = tuple((p * inv2 + x) % PMOD for p, x in zip(P, D))
    l2 = tuple((p * inv2 - x) % PMOD for p, x in zip(P, D))

    def yval(y, a, b):
        tot = 0
        for cf, m, g in y:
            tot += fmod(cf) * (amps.amp([(1, m, g)], a, b, l1, l2) + amps.amp([(1, m, g)], b, a, l2, l1))
        return tot % PMOD

    h0 = [state_strings(st, z) for st, z in input_basis(L, d)]
    fh = [state_strings(st, z) for st, z in input_basis(L, d, full=True)]
    vanish = all(
        yval(y, h0[rng.randrange(len(h0))], h0[rng.randrange(len(h0))]) == 0 for y in ys for _ in range(150)
    )
    pairs = [(rng.randrange(len(fh)), rng.randrange(len(fh))) for _ in range(400)]
    mat = [[yval(y, fh[i], fh[j]) for i, j in pairs] for y in ys]
    return len(ys), vanish, rank_modp([np.array(r, dtype=np.int64) for r in mat]) if mat else 0


def apply_L(n: int, ch: int, cf, mat: tuple, gh: tuple, ell0: tuple, kmax: int) -> list:
    """L_n (n = +-1) of chirality ch on a leg-0 Fock string; matter alpha_0 = ell0 (mod p).

    L_n^mat = 1/2 sum_m alpha_{n-m}.alpha_m, L_n^gh = sum_m (n + m) b_{n-m} c_m (no
    ordering constant for n != 0). Returns (coef, mat, gh) with coef mod p.
    """
    out = []
    d = len(ell0)

    def lower(mt, mu, m):  # alpha_m^mu, m > 0, on a matter multiset
        res = []
        k = sum(1 for x in mt if x == (ch, mu, m))
        if k:
            lst = list(mt)
            lst.remove((ch, mu, m))
            res.append((k * m, tuple(lst)))
        return res

    for mu in range(d):
        for m in range(-kmax - 2, kmax + 3):
            k = n - m
            if k > m:
                continue  # each unordered pair once; k == m only for even n
            fac = Fraction(1, 2) if k == m else Fraction(1)
            # alpha_k alpha_m with k <= m: apply alpha_m first (rightmost)
            stage = [(Fraction(1), mat)]
            for mode in (m, k):
                new = []
                for c0, mt in stage:
                    if mode > 0:
                        new += [(c0 * a, t) for a, t in lower(mt, mu, mode)]
                    elif mode == 0:
                        new.append((c0 * ell0[mu], mt))
                    else:
                        new.append((c0, tuple(sorted(mt + ((ch, mu, -mode),)))))
                stage = new
            for c0, mt in stage:
                out.append((cf * fac * c0, mt, gh))
    for m in range(-kmax - 3, kmax + 4):
        if n + m == 0:
            continue
        for s2, o in reduce_on_vacuum(((ch, "b", n - m), (ch, "c", m)) + gh):
            out.append((cf * (n + m) * s2, mat, o))
    return [(fmod(Fraction(c)) if not isinstance(c, int) else c % PMOD, m_, g) for c, m_, g in out if c]


def ol_functionals(vx: Vertex, K: int, d: int, P: tuple, sgn: int = -1) -> list[list]:
    """y_chi = <V| [(L_{-1} - z^2 L_1) - c.c.]^{(0)} chi (x) . (x) . >, chi in H^down at gh 2.

    Leg-0 momentum ell0 = -(ell1 + ell2) = -P. Kept: chi whose image stays at levels <= K.
    """
    z2 = Fraction(str(vx.z[1])) ** 2
    ell0 = tuple((-p) % PMOD for p in P)
    out = []
    for z, st in [(z, st) for z in ZPREF for st in closed_basis(K + 1, d, -len(ZPREF[z]), False)]:
        base = ZPREF[z] + st["gh"] + ((0, "c", 1), (1, "c", 1))
        strings = []
        for cf, (n, ch) in ((1, (-1, 0)), (sgn * z2, (1, 0)), (-1, (-1, 1)), (-sgn * z2, (1, 1))):
            for s2, o in reduce_on_vacuum(base):
                strings += apply_L(n, ch, Fraction(cf) * s2, st["mat"], o, ell0, K + 1)
        strings = [x for x in strings if x[0] % PMOD]
        if not strings:
            continue
        if max(max(string_levels(m_, g)) for _, m_, g in strings) > K:
            continue
        out.append(strings)
    return out


def check_identity_span(amps: Amplitudes, vx: Vertex, K: int, L: int, d: int, rng: random.Random, P: tuple):
    """dim (span of b- and L-identity functionals) cap (span of W rows), on full-H columns."""
    inv2 = pow(2, PMOD - 2, PMOD)
    D = tuple(rng.randrange(PMOD) for _ in range(d))
    l1 = tuple((p * inv2 + x) % PMOD for p, x in zip(P, D))
    l2 = tuple((p * inv2 - x) % PMOD for p, x in zip(P, D))
    fh = [state_strings(st, z) for st, z in input_basis(L, d, full=True)]
    h0 = [state_strings(st, z) for st, z in input_basis(L, d)]
    pairs = [(rng.randrange(len(fh)), rng.randrange(len(fh))) for _ in range(1500)]

    def ev(y, a, b):
        tot = 0
        for cf, m, g in y:
            c = fmod(cf) if isinstance(cf, Fraction) else cf
            tot += c * (amps.amp([(1, m, g)], a, b, l1, l2) + amps.amp([(1, m, g)], b, a, l2, l1))
        return tot % PMOD

    yl = ol_functionals(vx, K, d, P)
    yb_all = ob_functionals(vx, K, d, -1, all_zero_modes=True)
    vanish = all(
        ev(y, h0[rng.randrange(len(h0))], h0[rng.randrange(len(h0))]) == 0 for y in yl + yb_all for _ in range(40)
    )
    yb = ob_functionals(vx, K, d, -1, all_zero_modes=True)
    rows = [st for st in closed_basis(K, d, 0, False) if (st["N"] - st["Nb"]) % 2 == 0]
    wr = [[(1, m, g) for _, m, g in state_strings(st)] for st in rows]
    F = [np.array([ev(y, fh[i], fh[j]) for i, j in pairs], dtype=np.int64) for y in yb + yl]
    Wv = [np.array([ev(y, fh[i], fh[j]) for i, j in pairs], dtype=np.int64) for y in wr]
    rF, rW, rFW = rank_modp(F), rank_modp(Wv), rank_modp(F + Wv)
    return len(yl), len(yb_all), vanish, rF + rW - rFW, rW


def canon(gh: tuple) -> tuple[int, tuple] | None:
    """Canonical order of a creation-only ghost string (sign of the sort), None if it vanishes."""
    if len(set(gh)) < len(gh):
        return None
    order = sorted(range(len(gh)), key=lambda i: gh[i])
    inv = sum(1 for i in range(len(order)) for j in range(i + 1, len(order)) if order[i] > order[j])
    return (-1) ** inv, tuple(gh[i] for i in order)


def identity_relations(vx: Vertex, K: int, d: int, P: tuple, kchi: int) -> int:
    """Exact count of W-relations at levels <= K implied by the b- and L-identities (4.3).

    Each functional y_chi (chi at levels <= kchi, every zero-mode sector) is a vector over
    leg-0 monomials; the relations are the combinations supported on W rows (no c_0, cbar_0)
    at levels <= K, counted modulo odd-(N - Nbar) rows (trivial on symmetric inputs).
    """
    z2 = Fraction(str(vx.z[1])) ** 2
    ell0 = tuple((-p) % PMOD for p in P)
    funcs = []
    for z, st in [(z, st) for z in ZPREF for st in closed_basis(kchi, d, 1 - len(ZPREF[z]), False)]:
        base = ZPREF[z] + st["gh"] + ((0, "c", 1), (1, "c", 1))
        strings = []
        for cf, op in ((1, (0, "b", -1)), (-z2, (0, "b", 1)), (-1, (1, "b", -1)), (z2, (1, "b", 1))):
            for s2, o in reduce_on_vacuum((op,) + base):
                strings.append((fmod(Fraction(cf) * s2), st["mat"], o))
        funcs.append(strings)
    for z, st in [(z, st) for z in ZPREF for st in closed_basis(kchi, d, -len(ZPREF[z]), False)]:
        base = ZPREF[z] + st["gh"] + ((0, "c", 1), (1, "c", 1))
        strings = []
        for cf, (n, ch) in ((1, (-1, 0)), (-z2, (1, 0)), (-1, (-1, 1)), (z2, (1, 1))):
            for s2, o in reduce_on_vacuum(base):
                strings += apply_L(n, ch, Fraction(cf) * s2, st["mat"], o, ell0, kchi + 1)
        funcs.append(strings)
    index: dict = {}
    vecs = []
    for strings in funcs:
        vec: dict = {}
        for cf, m, g in strings:
            cg = canon(g)
            if cg is None:
                continue
            key = (tuple(sorted(m)), cg[1])
            vec[key] = (vec.get(key, 0) + cf * cg[0]) % PMOD
        vec = {k: c for k, c in vec.items() if c}
        if vec:
            vecs.append(vec)
            for k in vec:
                index.setdefault(k, len(index))

    def inside(key):  # W row at levels <= K with even N - Nbar
        m, g = key
        if any(op[2] == 0 for op in g):
            return False
        a, b = string_levels(m, g)
        return a <= K and b <= K and (a - b) % 2 == 0

    out_keys = [k for k in index if not inside(k)]
    in_keys = [k for k in index if inside(k)]
    # relations: kernel of the projection to outside coordinates, then image in inside coordinates
    full = [np.array([v.get(k, 0) for k in out_keys + in_keys], dtype=np.int64) for v in vecs]
    nout = len(out_keys)
    # row-reduce [out | in]; relations = rank(all) - rank(out part)
    r_all = rank_modp(full) if full else 0
    r_out = rank_modp([f[:nout] for f in full]) if nout else 0
    return r_all - r_out


def check_ol_vanish(amps: Amplitudes, vx: Vertex, K: int, L: int, d: int, rng: random.Random, P: tuple, sgn: int):
    """(L_{-1} - z^2 L_1)^- functionals on symmetric H_0 columns: all zero?"""
    inv2 = pow(2, PMOD - 2, PMOD)
    D = tuple(rng.randrange(PMOD) for _ in range(d))
    l1 = tuple((p * inv2 + x) % PMOD for p, x in zip(P, D))
    l2 = tuple((p * inv2 - x) % PMOD for p, x in zip(P, D))
    h0 = [state_strings(st, z) for st, z in input_basis(L, d)]
    ys = ol_functionals(vx, K, d, P, sgn)
    nz = 0
    for y in ys:
        for _ in range(40):
            a, b = h0[rng.randrange(len(h0))], h0[rng.randrange(len(h0))]
            val = sum(c * (amps.amp([(1, m, g)], a, b, l1, l2) + amps.amp([(1, m, g)], b, a, l2, l1)) for c, m, g in y)
            nz += val % PMOD != 0
    return len(ys), nz


# ----------------------------------------------------------------------- main
def main() -> None:
    seed = 20261004
    print(f"seed = {seed}, p = {PMOD}, d_eff = 2, beta = 3/2")
    rng = random.Random(seed)
    d = 2
    SCRATCH.mkdir(parents=True, exist_ok=True)
    out: dict = {"seed": seed}
    log: list[str] = []

    # C2-count: enumeration vs generating function
    ok = True
    for K in (1, 2, 3):
        gf = gf_count(K, d)
        en: dict = {}
        for st in closed_basis(K, d, 0, False):
            en[(st["N"], st["Nb"])] = en.get((st["N"], st["Nb"]), 0) + 1
        ok &= gf == en
        ev = sum(c for (n1, n2), c in gf.items() if (n1 - n2) % 2 == 0)
        out[f"dimWeven_K{K}"] = ev
        out[f"blocks_K{K}"] = {f"{a},{b}": c for (a, b), c in sorted(gf.items())}
    report(
        "C2-count",
        ok,
        f"dim W^even_<=K = {[out[f'dimWeven_K{K}'] for K in (1, 2, 3)]} (K=1,2,3)",
    )

    vx = Vertex(Fraction(3, 2), 3, 0, 4)
    check_neumann_log(vx)

    # C1-route2-tachyon (exact rationals)
    ampsQ = Amplitudes(vx, d, Field(None))
    l1 = tuple(Fraction(rng.randint(-60, 60), rng.randint(1, 25)) for _ in range(d))
    l2 = tuple(Fraction(rng.randint(-60, 60), rng.randint(1, 25)) for _ in range(d))
    T = state_strings({"N": 0, "Nb": 0, "mat": (), "gh": ()})
    r2 = route2_tachyon(vx, 2, d, l1, l2)
    mine = [ampsQ.amp(state_strings(st), T, T, l1, l2) for st, _ in r2]
    bad = sum(1 for (st, val), m in zip(r2, mine) if m != val)
    nz = sum(1 for _, val in r2 if val)
    report(
        "C1-route2-tachyon",
        bad == 0 and nz > 0,
        f"{len(r2)} rows at K=2, {nz} non-zero, {bad} mismatches",
    )
    # break leg: flip the sign of one non-zero ghost-excited row in route 2
    k = next(i for i, (st, val) in enumerate(r2) if val and st["gh"])
    bad_b = sum(
        1
        for i, ((st, val), m) in enumerate(zip(r2, mine))
        if m != (-val if i == k else val)
    )
    report(
        "BREAK-route2-tachyon",
        bad_b > 0,
        f"one row sign-flipped -> {bad_b} mismatch (must be > 0)",
    )

    # C1-exchange
    ampsP = Amplitudes(vx, d, Field(PMOD))
    ok, nz = check_exchange(ampsP, 2, 2, d, rng, 60)
    report(
        "C1-exchange",
        ok,
        f"(-1)^(N-Nbar) exchange on full-H gh-2 inputs, K=L=2, {nz} non-zero entries",
    )

    # C3 table entries (alpha'_v = 0, gamma' = 3)
    P = tuple(rng.randrange(PMOD) for _ in range(d))
    res = run_entry(ampsP, 1, 1, d, rng, P, log=log)
    out["K1L1"] = res
    # second route: exact rank over Q and float SVD at random rational/complex momenta
    rows = [st for st in closed_basis(1, d, 0, False) if (st["N"] - st["Nb"]) % 2 == 0]
    ins = input_basis(1, d)
    rs = [state_strings(st) for st in rows]
    iss = [state_strings(st, z) for st, z in ins]
    Pq = tuple(Fraction(rng.randint(-40, 40), rng.randint(1, 9)) for _ in range(d))
    Dq = tuple(Fraction(rng.randint(-40, 40), rng.randint(1, 9)) for _ in range(d))
    q1 = tuple(p / 2 + x for p, x in zip(Pq, Dq))
    q2 = tuple(p / 2 - x for p, x in zip(Pq, Dq))
    cols = [
        [
            ampsQ.amp(B, iss[i], iss[j], q1, q2) + ampsQ.amp(B, iss[j], iss[i], q2, q1)
            for B in rs
        ]
        for i in range(len(ins))
        for j in range(len(ins))
    ]
    rq = sp.Matrix(
        [[sp.Rational(x.numerator, x.denominator) for x in c] for c in cols]
    ).rank()
    sv = np.linalg.svd(
        np.array([[float(x) for x in c] for c in cols]), compute_uv=False
    )
    gap = sv[len(rows) - 1] / sv[0]
    report(
        "C3-K1-L1",
        res["rank"] == 7 == out["dimWeven_K1"] and rq == 7,
        f"rank F_p {res['rank']}, rank Q {rq}, dim 7; float s_7/s_1 = {gap:.2e}",
    )
    res = run_entry(ampsP, 2, 2, d, rng, P, log=log)
    P2 = tuple(rng.randrange(PMOD) for _ in range(d))
    res2 = run_entry(ampsP, 2, 2, d, rng, P2, log=log)
    out["K2L2"], out["K2L2_P2"] = res, res2
    report(
        "C3-K2-L2",
        res["rank"] == 68 == res2["rank"] and res["rows_even"] == 73,
        f"rank {res['rank']}, {res2['rank']} (two P), dim 73, deficit 5; blocks {res['per_block']}",
    )
    # C3-K2-L3: capped random column sample (one Delta)
    res3 = run_entry_capped(ampsP, 2, 3, d, rng, P, cap=25000, log=log)
    out["K2L3_capped"] = res3
    report(
        "C3-K2-L3-capped",
        res3["rank"] == 68,
        f"rank {res3['rank']} after {res3['columns_used']} random symmetric columns, dim 73",
    )

    # C4: origin of the deficit
    full = run_entry(ampsP, 2, 2, d, rng, P, log=log, full=True)
    cb = closed_basis
    insA = [(st, "") for st in cb(2, d, 0, False)] + [
        (st, "c0+") for st in cb(2, d, -1, False)
    ]
    kb = run_entry(ampsP, 2, 2, d, rng, P, log=log, ins_override=insA)
    out["K2L2_fullH"], out["K2L2_kerb0_nolm"] = full["rank"], kb["rank"]
    report(
        "C4-deficit-from-H0",
        full["rank"] == 73 and kb["rank"] == 70,
        f"full-H gh-2 inputs: rank {full['rank']}/73; ker b0^- without level matching: {kb['rank']}/73",
    )
    n, van, rk = check_ob_identity(ampsP, vx, 2, 2, d, rng, P, -1)
    out["ob_identity_K2"] = (n, van, rk)
    report(
        "C4-ob-identity",
        van and rk == 73 - kb["rank"],
        f"(b_1^- - z^2 b_-1^-) Phi_2 = 0: {n} functionals vanish on H_0 columns, rank {rk} on full-H columns"
        f" = measured ker-b0^- cokernel {73 - kb['rank']}",
    )
    n, van, rk = check_ob_identity(ampsP, vx, 2, 2, d, rng, P, +1)
    report("BREAK-ob-identity", not van, "sign-flipped operator (b_-1 + z^2 b_1) must not vanish on H_0 columns")
    n3, van3, rk3 = check_ob_identity(ampsP, vx, 3, 2, d, rng, P, -1)
    out["ob_identity_K3"] = (n3, van3, rk3)
    report("C4-ob-identity-K3", van3, f"K=3: {n3} functionals vanish on H_0 columns, rank {rk3} (b-relations at K=3)")
    n, nzl = check_ol_vanish(ampsP, vx, 2, 2, d, rng, P, -1)
    report("C4-L-identity", nzl == 0, f"(L_-1 - z^2 L_1)^- Phi_2 = 0 on level-matched inputs: {n} functionals x 40 H_0 columns, {nzl} non-zero")
    n, nzl = check_ol_vanish(ampsP, vx, 2, 2, d, rng, P, +1)
    report("BREAK-L-identity", nzl > 0, f"sign-flipped (L_-1 + z^2 L_1): {nzl} non-zero values (must be > 0)")
    nrel = identity_relations(vx, 2, d, P, 3)
    out["identity_relations_K2"] = nrel
    report("C4-identity-count", nrel == 5 == 73 - out["K2L2"]["rank"], f"relations on W^even_<=2 implied by (4.3), chi level <= 3: {nrel}; measured deficit {73 - out['K2L2']['rank']}")
    vxa = Vertex(Fraction(3, 2), 3, Fraction(1, 2), 3)
    ampsA = Amplitudes(vxa, d, Field(PMOD))
    ra = run_entry(ampsA, 2, 2, d, rng, P, log=log)
    out["K2L2_alphav_half"] = ra["rank"]
    report(
        "C4-alpha-v",
        ra["rank"] == 73,
        f"alpha'_v = 1/2: rank {ra['rank']}/73 (no deficit)",
    )
    vx2 = Vertex(Fraction(3, 2), 2, 0, 3)
    r22 = run_entry(Amplitudes(vx2, d, Field(PMOD)), 2, 2, d, rng, P, log=log)
    report(
        "C4-gamma2",
        r22["rank"] == 68,
        f"gamma' = 2, alpha'_v = 0: rank {r22['rank']}/73",
    )

    # break legs
    bad = run_entry(ampsP, 2, 2, d, rng, P, log=log, antisym=True)
    report(
        "BREAK-antisym",
        bad["rank"] < 73,
        f"antisymmetrised inputs: rank {bad['rank']}/73 on even rows",
    )
    bm = run_entry(ampsP, 2, 2, d, rng, P, log=log, only_matter=True)
    report(
        "BREAK-matter-only",
        bm["rank"] < 73,
        f"ghost ground-state inputs: rank {bm['rank']}/73",
    )

    (SCRATCH / "results.json").write_text(json.dumps(out, indent=1, default=str))
    (SCRATCH / "scan.log").write_text("\n".join(log))
    nfail = sum(1 for _, ok, _ in RESULTS if not ok)
    print(f"SUMMARY: {len(RESULTS) - nfail}/{len(RESULTS)} PASS")
    sys.exit(1 if nfail else 0)


def run_entry_capped(amps, K, L, d, rng, P, cap, log) -> dict:
    """One Delta sample, at most `cap` random ordered input pairs (evidence, not proof)."""
    rows = [st for st in closed_basis(K, d, 0, False) if (st["N"] - st["Nb"]) % 2 == 0]
    rstr = [state_strings(st) for st in rows]
    ins = input_basis(L, d)
    istr = [state_strings(st, z) for st, z in ins]
    ech = Echelon(len(rows))
    inv2 = pow(2, PMOD - 2, PMOD)
    D = tuple(rng.randrange(PMOD) for _ in range(d))
    l1 = tuple((p * inv2 + x) % PMOD for p, x in zip(P, D))
    l2 = tuple((p * inv2 - x) % PMOD for p, x in zip(P, D))
    n = 0
    t0 = time.time()
    while n < cap and ech.rank < len(rows):
        i, j = rng.randrange(len(ins)), rng.randrange(len(ins))
        col = np.array(
            [
                (
                    amps.amp(B, istr[i], istr[j], l1, l2)
                    + amps.amp(B, istr[j], istr[i], l2, l1)
                )
                % PMOD
                for B in rstr
            ],
            dtype=np.int64,
        )
        ech.add(col)
        n += 1
    log.append(
        f"K={K} L={L} capped: rank {ech.rank}/{len(rows)} after {n} columns, {time.time() - t0:.0f}s"
    )
    print(log[-1], flush=True)
    return {
        "rank": ech.rank,
        "rows_even": len(rows),
        "columns_used": n,
        "inputs": len(ins),
    }


if __name__ == "__main__":
    main()
