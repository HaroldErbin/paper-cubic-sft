#!/usr/bin/env python3
"""verify-partner-octic.py – companion of agent/derivations/101-partner-count.md, Step 3.

Question: with Sigma_4 in the model, do the Upsilon_2 couplings close the
exchange structures of the eliminated elementary action at O(g^8) (claim C3.3 of
record 101), after re-running O(g^6) and O(g^7) with the V_8, V_9 contact menus
that contain Sigma_4?  Tests the hypothesis H1 (triangular closure).

Model (as codes/verify-partner-closure.py, extended).  Psi in R^N, Sigma_2,
Upsilon_2 in Sym^2, Sigma_3 in Sym^3, Sigma_4 in Sym^4 (orthonormal bases),
generic symmetric tensors V_4..V_10.  The elementary action, record 101
eqs. (D.1) and (E.1): appendix E through O(g^5) with (a7, b7) = (-1, 2),
c6 = 0, the order-6 contact menu alpha V8(S4^2) + beta V8(S4, S3, Psi)
+ gamma V8(S4, S2^2) + delta V8(S3^2, S2) with alpha = -1 (normalisation of
Sigma_4), the order-7 menu lambda V9(S4^2, Psi) + mu V9(S4, S3, S2)
+ nu V9(S3^3), the order-8 menu rho V10(S4^2, S2) + sigma V10(S4, S3^2), and the
Upsilon_2 couplings f7 V7(U2, S3, S2), f6 V6(U2^2, S2) [order 6];
f8 V8(U2, S3^2), f8p V8(U2, S4, S2), f7b V7(U2^2, S3), f6b V6(U2^3) [order 7];
f9 V9(U2, S4, S3), f8c V8(U2^2, S4) [order 8; f7c V7(U2^3, Psi) is quartic
in the fields and kept only as a diagnostic, switched off].  The joint
classical value of the auxiliaries at complex g is found by Newton iteration
around |g| = r and the Taylor coefficients of
    f(g) = S^Upsilon(classical) - sum_n g^{n-2}/n! V_n(Psi^n)
by a Cauchy sum.  (m+2)! [f]_{g^m} is projected on the whole-slot tree
structures of degree m+2 (catalogue with strands 2, 3, 4 and the collapse rule
N2') by least squares over random Psi draws; its polynomial dependence on the
parameters is fitted on a random design and validated on held-out points; the
closure system is solved exactly on the rationalised coefficients.

Checks (named after the claim-tree nodes of record 101).
  CAL-orders-0-5    : g^0..g^5 coefficients of f vanish at random parameters.
  CAL-step2-order6  : at alpha = beta = gamma = 0 (no Sigma_4 term but a kinetic
                      regulator), the order-6 deficit of Step 2, eq. (D.3) at
                      a7 = -1, c6 = 0, is reproduced.
  C0-trees-10       : the degree-10 catalogue with strands (2, 3, 4) under N2'.
  C3a-*             : order 6 with the V_8 menu (complete, polyfit, deficit,
                      closure, closure-break, closure-direct).
  C3b-*             : order 7 on the order-6 family with the V_9 menu.
  C3.3-*            : order 8 on the order-7 family: basis conditioning,
                      completeness (catalogue with rule N2'': 36 structures),
                      polynomial fit, deficit vector, closure, break, direct;
                      C3.3-H1-falsified (the recorded set of structures with a
                      deficit, including four multi-node trees and the k = 3 star
                      that no cubic coupling reaches; a regression guard on the
                      recorded set, not a test of H1); C3.3-d-fixed (d = 0).
  F-rule-*          : fix pass (record 101 block F).  Fit-free direct evaluations
                      of the deficit at the rule point "Sigma_2 -> Sigma_2 + Upsilon_2
                      in every coupling" (d = 3 c6, d' = 2 (1 - c6), f6 = 3 c6,
                      f6b = c6, f7 = 4, f7b = 2, f8 = 0, f8p = 4, f8c = 2, f9 = mu,
                      beta = 0, gamma = 2, delta = 0, mu = -2 lam, nu = 1 + lam,
                      rho + sigma = 1) at orders 6, 7, 8 for c6 = 0 and c6 = 1/3
                      (must vanish, record 101 eq. (F.5)); and at the departure
                      d = 2 (the table's value at c6 = 0) on the order-7 family,
                      where the projected order-8 deficit must reproduce
                      delta_27 = 18 d^3 / 25, delta_29 = 36 d^2 / 35 of eq. (E.6)
                      (fit-free check of the exclusion).  Run with --n4 to address
                      the D = 10 basis conditioning at N = 3.

Run: uv run --no-sync python codes/verify-partner-octic.py [--step 6|7|8] [--rule] [--n4]
Not verified: string vertices (PH14–PH16), Upsilon_3 couplings.
"""

from __future__ import annotations

import itertools
import math
import sys
import time
from fractions import Fraction

import numpy as np
import sympy as sp

SEED = 20261018
rng = np.random.default_rng(SEED)
print(f"seed = {SEED}")
results: list[tuple[str, bool, str]] = []
STEPS = {6, 7, 8}
if "--step" in sys.argv:
    STEPS = {int(sys.argv[sys.argv.index("--step") + 1])}
RULE = "--rule" in sys.argv
if RULE:
    STEPS = set()
N = 4 if "--n4" in sys.argv else 3
T0 = time.time()


def check(name: str, ok: bool, info: str = "") -> None:
    results.append((name, ok, info))
    print(
        f"[{'PASS' if ok else 'FAIL'}] {name} {info}   (t = {time.time() - T0:.0f} s)"
    )


# ----------------------------------------------------------------------------
# Tree catalogue (verify-partner-count.py / -closure.py, strands up to 4)
# ----------------------------------------------------------------------------
def labeled_trees(k: int):
    if k == 1:
        yield []
        return
    if k == 2:
        yield [(0, 1)]
        return
    for seq in itertools.product(range(k), repeat=k - 2):
        degree = [1] * k
        for x in seq:
            degree[x] += 1
        edges = []
        for x in seq:
            for leaf in range(k):
                if degree[leaf] == 1:
                    edges.append((leaf, x))
                    degree[leaf] -= 1
                    degree[x] -= 1
                    break
        u, v = [i for i in range(k) if degree[i] == 1]
        edges.append((u, v))
        yield edges


def canon(k: int, edges, ext) -> str:
    adj = {i: [] for i in range(k)}
    for i, j, s in edges:
        adj[i].append((j, s))
        adj[j].append((i, s))

    def enc(v, parent, s_in):
        subs = sorted(enc(w, v, s) for w, s in adj[v] if w != parent)
        return f"({s_in}:{ext[v]}" + "".join(subs) + ")"

    return min(enc(r, -1, 0) for r in range(k))


def shapes(k: int):
    seen = {}
    for edges in labeled_trees(k):
        key = canon(k, [(i, j, 0) for i, j in edges], [0] * k)
        seen.setdefault(key, edges)
    return list(seen.values())


def ext_options(inc: list[int], smax: int) -> list[int]:
    m = len(inc)
    if m > 3:
        return []
    opts = []
    # N2'' (step 3): the collapse p_{3,3}^{-1} V_6(., x, Psi) = x (.) Psi turns a cubic
    # node V_n(3, a, b) into an effective node V_n(2_line, 1_ext, a, b) with four slots;
    # a node with three lines may therefore carry one external strand.  (At D = 10 the
    # only such tree is V7(2,2,2|1) V5(2|3)^3, the k = 3 star; found because the
    # order-8 deficit left the span of the cubic catalogue, run6-step8.log.)
    emax = (3 - m) * smax if m < 3 else 1
    for e in range(0, emax + 1):
        n = sum(inc) + e
        if n < 3 or any(n < 2 * s for s in inc):
            continue
        if any(n == 2 * s for s in inc):  # N2'
            continue
        opts.append(e)
    return opts


def catalogue(D: int, smax: int, strands=(2, 3, 4), kmax: int = 6):
    found = {}
    for k in range(1, kmax + 1):
        for shape in shapes(k):
            for strs in itertools.product(strands, repeat=len(shape)):
                edges = [(i, j, s) for (i, j), s in zip(shape, strs)]
                opts = []
                for i in range(k):
                    inc = [s for a, b, s in edges if i in (a, b)]
                    opts.append(ext_options(inc, smax))
                if any(not o for o in opts):
                    continue
                for ext in itertools.product(*opts):
                    if sum(ext) != D:
                        continue
                    key = canon(k, edges, list(ext))
                    if key not in found:
                        found[key] = (k, edges, list(ext))
    return found


def describe(k, edges, ext) -> str:
    nodes = []
    for i in range(k):
        inc = sorted(s for a, b, s in edges if i in (a, b))
        nodes.append(f"V{sum(inc) + ext[i]}({','.join(map(str, inc))}|{ext[i]})")
    return " ".join(nodes)


# ----------------------------------------------------------------------------
# Tensor model
# ----------------------------------------------------------------------------
NMAX = 10
STRANDS = (2, 3, 4)


def sym_tensor(k: int) -> np.ndarray:
    """Generic symmetric tensor: one Gaussian value per multiset of indices."""
    out = np.zeros((N,) * k)
    for c in itertools.combinations_with_replacement(range(N), k):
        val = rng.standard_normal()
        for p in set(itertools.permutations(c)):
            out[p] = val
    return out


def sym_basis(k: int) -> np.ndarray:
    out = []
    for c in itertools.combinations_with_replacement(range(N), k):
        t = np.zeros((N,) * k)
        ps = set(itertools.permutations(c))
        for p in ps:
            t[p] = 1.0
        out.append(t / np.sqrt(len(ps)))
    return np.array(out)


V = {n: sym_tensor(n) for n in range(4, NMAX + 1)}
B = {s: sym_basis(s) for s in STRANDS}
DIM = {s: B[s].shape[0] for s in STRANDS}


def kinetic_matrix(s: int) -> np.ndarray:
    half = np.tensordot(B[s], V[2 * s], axes=(range(1, s + 1), range(s)))
    return np.tensordot(half, B[s], axes=(range(1, s + 1), range(1, s + 1)))


M = {s: kinetic_matrix(s) for s in STRANDS}
Minv = {s: np.linalg.inv(M[s]) for s in STRANDS}
LETTERS = "abcdefghijklmnopqrstuvwxyz"
_RV_CACHE: dict = {}


def reduce_vertex(n: int, slots: list, Psi: np.ndarray) -> np.ndarray:
    """Contract V_n with Psi on 'p' slots and with the Sym^s basis on s-slots."""
    key = (n, tuple(slots), id(Psi))
    if key in _RV_CACHE:
        return _RV_CACHE[key]
    ops = [V[n]]
    sub = [LETTERS[:n]]
    pos = 0
    out = []
    nxt = n
    for sl in slots:
        if sl == "p":
            ops.append(Psi)
            sub.append(LETTERS[pos])
            pos += 1
        else:
            s = int(sl)
            ops.append(B[s])
            sub.append(LETTERS[nxt] + LETTERS[pos : pos + s])
            out.append(LETTERS[nxt])
            nxt += 1
            pos += s
    assert pos == n
    arr = np.einsum(",".join(sub) + "->" + "".join(out), *ops, optimize=True)
    _RV_CACHE[key] = arr
    return arr


def tree_value(k: int, edges, ext, Psi: np.ndarray) -> float:
    adj = {i: [] for i in range(k)}
    for i, j, s in edges:
        adj[i].append((j, s))
        adj[j].append((i, s))

    def node(v, parent, s_in):
        children = [(w, s) for w, s in adj[v] if w != parent]
        slots = ([s_in] if s_in else []) + [s for _, s in children] + ["p"] * ext[v]
        n = sum(int(s) for s in slots if s != "p") + ext[v]
        arr = reduce_vertex(n, slots, Psi)
        for ci, (w, s) in enumerate(children):
            vec = Minv[s] @ node(w, v, s)
            axis = 1 if s_in else 0
            arr = np.tensordot(arr, vec, axes=([axis], [0]))
        return arr

    return float(node(0, -1, 0))


# ----------------------------------------------------------------------------
# The elementary action, record 101 eqs. (D.1), (E.1); x = (S2, S3, U2, S4)
# ----------------------------------------------------------------------------
FIELDS = {
    "S2": (2, 0),
    "S3": (3, DIM[2]),
    "U2": (2, DIM[2] + DIM[3]),
    "S4": (4, 2 * DIM[2] + DIM[3]),
}
NX = 2 * DIM[2] + DIM[3] + DIM[4]
FACT = {n: math.factorial(n) for n in range(3, 11)}


def terms(par: dict) -> list:
    """(g-power, coefficient, n, slots); every parameter defaults to 0."""
    p = lambda k, default=0.0: par.get(k, default)  # noqa: E731
    c6 = p("c6")
    a7 = p("a7", -1.0)
    b7 = p("b7", 1 - a7)
    d = p("d")
    dp = p("dprime", 2 + c6 - d)
    T = [
        (2, -1 / 24, 4, ["S2", "S2"]),
        (2, 2 / 24, 4, ["S2", "p", "p"]),
        (3, 1 / 120, 5, ["S2", "S2", "p"]),
        (2, p("a", 1.0) / 24, 4, ["U2", "U2"]),
        (3, p("b", 2.0) / 120, 5, ["U2", "S2", "p"]),
        (4, c6 / 720, 6, ["S2", "S2", "S2"]),
        (4, -(1 - c6) / 720, 6, ["S3", "S3"]),
        (4, 2 * (1 - c6) / 720, 6, ["S3", "S2", "p"]),
        (5, a7 / 5040, 7, ["S3", "S3", "p"]),
        (5, b7 / 5040, 7, ["S3", "S2", "S2"]),
        (3, p("c", 1.0) / 120, 5, ["U2", "U2", "p"]),
        (4, d / 720, 6, ["U2", "S2", "S2"]),
        (4, dp / 720, 6, ["U2", "S3", "p"]),
        # order 6: V_8 contact menu with Sigma_4, Upsilon_2 couplings
        (6, p("alpha", -1.0) / FACT[8], 8, ["S4", "S4"]),
        (6, p("beta") / FACT[8], 8, ["S4", "S3", "p"]),
        (6, p("gamma") / FACT[8], 8, ["S4", "S2", "S2"]),
        (6, p("delta") / FACT[8], 8, ["S3", "S3", "S2"]),
        (5, p("f7") / FACT[7], 7, ["U2", "S3", "S2"]),
        (4, p("f6") / FACT[6], 6, ["U2", "U2", "S2"]),
        # order 7
        (7, p("lam") / FACT[9], 9, ["S4", "S4", "p"]),
        (7, p("mu") / FACT[9], 9, ["S4", "S3", "S2"]),
        (7, p("nu") / FACT[9], 9, ["S3", "S3", "S3"]),
        (6, p("f8") / FACT[8], 8, ["U2", "S3", "S3"]),
        (6, p("f8p") / FACT[8], 8, ["U2", "S4", "S2"]),
        (5, p("f7b") / FACT[7], 7, ["U2", "U2", "S3"]),
        (4, p("f6b") / FACT[6], 6, ["U2", "U2", "U2"]),
        # order 8
        (8, p("rho") / FACT[10], 10, ["S4", "S4", "S2"]),
        (8, p("sigma") / FACT[10], 10, ["S4", "S3", "S3"]),
        (7, p("f9") / FACT[9], 9, ["U2", "S4", "S3"]),
        (6, p("f8c") / FACT[8], 8, ["U2", "U2", "S4"]),
        (5, p("f7c") / FACT[7], 7, ["U2", "U2", "U2", "p"]),
    ]
    return [t for t in T if t[1] != 0.0]


class Action:
    """Cubic polynomial in x at fixed Psi: S = sum_m g^m (L_m x + x Q_m x + C_m xxx)."""

    def __init__(self, par: dict, Psi: np.ndarray):
        self.L, self.Q, self.C = {}, {}, {}
        for m, coef, n, slots in terms(par):
            fs = [s for s in slots if s != "p"]
            arr = coef * reduce_vertex(
                n, [("p" if s == "p" else FIELDS[s][0]) for s in slots], Psi
            )
            offs = [FIELDS[s][1] for s in fs]
            dims = [DIM[FIELDS[s][0]] for s in fs]
            if len(fs) == 1:
                Lm = self.L.setdefault(m, np.zeros(NX))
                Lm[offs[0] : offs[0] + dims[0]] += arr
            elif len(fs) == 2:
                Qm = self.Q.setdefault(m, np.zeros((NX, NX)))
                Qm[offs[0] : offs[0] + dims[0], offs[1] : offs[1] + dims[1]] += arr
            else:
                Cm = self.C.setdefault(m, np.zeros((NX, NX, NX)))
                Cm[
                    offs[0] : offs[0] + dims[0],
                    offs[1] : offs[1] + dims[1],
                    offs[2] : offs[2] + dims[2],
                ] += arr
        for m in self.Q:
            self.Q[m] = (self.Q[m] + self.Q[m].T) / 2
        for m in self.C:
            Cm = self.C[m]
            self.C[m] = (
                sum(np.transpose(Cm, p) for p in itertools.permutations(range(3))) / 6
            )

    def assemble(self, g: complex):
        L = sum((g**m) * Lm for m, Lm in self.L.items())
        Q = sum((g**m) * Qm for m, Qm in self.Q.items())
        C = sum((g**m) * Cm for m, Cm in self.C.items())
        return L, Q, C

    def saddle_value(self, g: complex, x0: np.ndarray):
        L, Q, C = self.assemble(g)
        x = x0.astype(complex)
        for _ in range(60):
            Cx = np.einsum("ijk,k->ij", C, x)
            grad = L + 2 * Q @ x + 3 * Cx @ x
            hess = 2 * Q + 6 * Cx
            dx = np.linalg.solve(hess, -grad)
            x = x + dx
            if np.max(np.abs(dx)) < 1e-15 * max(1.0, np.max(np.abs(x))):
                break
        Cx = np.einsum("ijk,k->ij", C, x)
        grad = L + 2 * Q @ x + 3 * Cx @ x
        if np.max(np.abs(grad)) > 1e-10 * abs(g) ** 2:
            raise RuntimeError(
                f"Newton did not converge at g={g}: |grad|={np.max(np.abs(grad))}"
            )
        val = L @ x + x @ Q @ x + x @ Cx @ x
        return val, x


def target(g: complex, Psi: np.ndarray, nmax: int) -> complex:
    return sum(
        g ** (n - 2) / FACT[n] * reduce_vertex(n, ["p"] * n, Psi)
        for n in range(4, nmax + 1)
    )


def veronese(Psi: np.ndarray) -> np.ndarray:
    x0 = np.zeros(NX)
    for name, (s, off) in FIELDS.items():
        if name == "U2":
            continue
        Ps = Psi
        for _ in range(s - 1):
            Ps = np.multiply.outer(Ps, Psi)
        x0[off : off + DIM[s]] = np.tensordot(B[s], Ps, axes=s)
    return x0


def taylor(par: dict, Psi: np.ndarray, orders, r: float = 0.1, K: int = 32):
    act = Action(par, Psi)
    x = veronese(Psi)
    # homotopy in |g| from the Veronese point to the circle (Newton's basin at g = r
    # can exclude the g = 0 saddle for couplings of order one)
    for t in (0.25, 0.5, 0.75):
        _, x = act.saddle_value(t * r, x)
    vals = []
    for k in range(K):
        g = r * np.exp(2j * np.pi * k / K)
        v, x = act.saddle_value(g, x)
        vals.append(v - target(g, Psi, NMAX))
    vals = np.array(vals)
    ks = np.arange(K)
    return {
        m: complex(np.sum(vals * np.exp(-2j * np.pi * ks * m / K)) / (K * r**m))
        for m in orders
    }


# ----------------------------------------------------------------------------
# Fits
# ----------------------------------------------------------------------------
NDRAW = 50
PSI_DRAWS = [rng.standard_normal(N) for _ in range(NDRAW)]


def structure_matrix(D: int, draws):
    cat = catalogue(D, 4)
    trees = sorted(cat.values(), key=lambda t: (t[0], describe(*t)))
    names = [describe(*t) for t in trees]
    S = np.array([[tree_value(*t, Psi) for t in trees] for Psi in draws])
    return names, trees, S


def deficit_vector(par: dict, order: int, draws, S: np.ndarray):
    rhs = np.array(
        [FACT[order + 2] * taylor(par, Psi, [order])[order].real for Psi in draws]
    )
    coef, _, _, _ = np.linalg.lstsq(S, rhs, rcond=None)
    resid = np.max(np.abs(S @ coef - rhs)) / max(np.max(np.abs(rhs)), 1e-300)
    return coef, resid, rhs


def polyfit_params(fun, mons, draw_par, npts: int, nhold: int):
    pts = [draw_par() for _ in range(npts + nhold)]
    X = np.array([[np.prod([p[n] for n in mon]) for mon in mons] for p in pts])
    Y = np.array([fun(p) for p in pts])
    coef, *_ = np.linalg.lstsq(X[:npts], Y[:npts], rcond=None)
    hold = np.max(np.abs(X[npts:] @ coef - Y[npts:])) / max(np.max(np.abs(Y)), 1e-300)
    return coef, hold


def monomials(names, deg: int):
    mons = [()]
    for dd in range(1, deg + 1):
        mons += list(itertools.combinations_with_replacement(names, dd))
    return mons


def rationalise(x: float, maxden: int = 20000, tol: float = 1e-6):
    fr = Fraction(x).limit_denominator(maxden)
    return fr if abs(float(fr) - x) < tol * max(1.0, abs(x)) else None


def to_sympy(mons, col, syms: dict, name: str, thr: float = 1e-7):
    expr = sp.Integer(0)
    for mon, c in zip(mons, col):
        if abs(c) < thr:
            continue
        fr = rationalise(c)
        if fr is None:
            print(f"   !! {name}: coefficient {c} of {mon} not rational")
            return None
        term = sp.Rational(fr.numerator, fr.denominator)
        for v in mon:
            term *= syms[v]
        expr += term
    return sp.expand(expr)


def closure_analysis(label, names, mons, coef, pnames, solve_for, new_names, thr):
    syms = {n: sp.Symbol(n) for n in pnames}
    polys = []
    for i, nm in enumerate(names):
        e = to_sympy(mons, coef[:, i], syms, f"delta_{i + 1}", thr)
        polys.append(e)
        print(f"   delta_{i + 1} [{nm}] = {sp.factor(e) if e is not None else None}")
    if any(e is None for e in polys):
        return None, None, None
    unreached = [
        names[i] for i, e in enumerate(polys) if e.free_symbols == set() and e != 0
    ]
    nontriv = [e for e in polys if e != 0]
    sols = sp.solve(nontriv, [syms[n] for n in solve_for], dict=True)
    real_sols = [
        sol
        for sol in sols
        if all(
            sp.im(v.subs({syms[n]: sp.Rational(3, 7) for n in pnames})) == 0
            for v in sol.values()
        )
    ]
    print(
        f"   {label}: {len(nontriv)} nontrivial equations, {len(polys) - len(nontriv)} identically zero; "
        f"unreached: {unreached or 'none'}; solutions: {real_sols}"
    )
    for sol in real_sols:
        J_new = sp.Matrix(
            [[sp.diff(e, syms[n]) for n in new_names] for e in nontriv]
        ).subs(sol)
        J_all = sp.Matrix(
            [[sp.diff(e, syms[n]) for n in pnames] for e in nontriv]
        ).subs(sol)
        print(
            f"   Jacobian rank in the new couplings {J_new.rank()} (of {len(new_names)}), "
            f"in all parameters {J_all.rank()} (of {len(pnames)}); free: {[n for n in pnames if syms[n] not in sol]}"
        )
    return polys, real_sols, syms


def closure_checks(tag, polys, sols, syms, pnames, new_names, fixed, order, S):
    check(f"{tag}-closure", bool(sols), f"({len(sols) if sols else 0} real family/ies)")
    if not sols:
        return None
    sol = dict(sols[0])
    free_vals = {syms[n]: sp.Rational(3, 7) for n in pnames if syms[n] not in sol}
    sol_num = {k: v.subs(free_vals) for k, v in sol.items()}
    sol_num.update(free_vals)
    key = syms[new_names[-1]]
    pert = dict(sol_num)
    pert[key] = sol_num[key] + sp.Rational(1, 10)
    vals = [sp.simplify(e.subs(pert)) for e in polys]
    check(
        f"{tag}-closure-break",
        any(v != 0 for v in vals),
        f"(perturbed {key}: deficit {vals})",
    )
    parsol = fixed(dict({n: float(sol_num[syms[n]]) for n in pnames}))
    _, _, rhs = deficit_vector(parsol, order, PSI_DRAWS, S)
    scale = np.max(np.abs(S))
    check(
        f"{tag}-closure-direct",
        np.max(np.abs(rhs)) < 1e-9 * scale,
        f"(max |{order + 2}! [f]_{order}| at the solution point: {np.max(np.abs(rhs)):.1e}; structure scale {scale:.1e}; point {parsol})",
    )
    return sol


def run_order(
    tag,
    order,
    pnames,
    mons,
    draw_par,
    fixed,
    solve_for,
    new_names,
    npts,
    nhold,
    thr=1e-7,
    hold_thr=1e-7,
):
    print(f"\n== {tag}: order {order} (degree {order + 2}) ==")
    names, trees, S = structure_matrix(order + 2, PSI_DRAWS)
    print(f"   {len(names)} structures (N2', strands 2,3,4)")
    for i, nm in enumerate(names):
        print(f"   S{i + 1}: {nm}")
    sv = np.linalg.svd(S / np.linalg.norm(S, axis=0), compute_uv=False)
    check(
        f"{tag}-basis",
        sv[-1] / sv[0] > 1e-6,
        f"(normalised singular values {sv[0]:.2e} .. {sv[-1]:.2e}, {len(names)} structures, {len(PSI_DRAWS)} draws)",
    )
    resids = []

    def dv(par):
        coef, resid, _ = deficit_vector(fixed(par), order, PSI_DRAWS, S)
        resids.append(resid)
        return coef

    coef, hold = polyfit_params(dv, mons, draw_par, npts, nhold)
    check(
        f"{tag}-complete",
        max(resids) < 1e-8,
        f"(max projection residual over {npts + nhold} parameter points {max(resids):.1e})",
    )
    check(
        f"{tag}-polyfit",
        hold < hold_thr,
        f"(held-out residual {hold:.1e}, {len(mons)} monomials)",
    )
    polys, sols, syms = closure_analysis(
        tag, names, mons, coef, pnames, solve_for, new_names, thr
    )
    check(
        f"{tag}-deficit", polys is not None, "(rational deficit vector printed above)"
    )
    sol = None
    if polys is not None:
        sol = closure_checks(tag, polys, sols, syms, pnames, new_names, fixed, order, S)
    return names, trees, polys, sols, syms, sol


def uni(lo, hi):
    return float(rng.uniform(lo, hi))


# ----------------------------------------------------------------------------
# CAL
# ----------------------------------------------------------------------------
par0 = {
    "d": uni(-1.5, 1.5),
    "beta": uni(-1, 1),
    "gamma": uni(-1, 1),
    "delta": uni(-1, 1),
    "lam": uni(-1, 1),
    "mu": uni(-1, 1),
    "nu": uni(-1, 1),
    "rho": uni(-1, 1),
    "sigma": uni(-1, 1),
}
for k in ("f7", "f6", "f8", "f8p", "f7b", "f6b", "f9", "f8c", "f7c"):
    par0[k] = uni(-1.5, 1.5)
Psi0 = PSI_DRAWS[0]
co = taylor(par0, Psi0, range(0, 6))
scale = abs(reduce_vertex(6, ["p"] * 6, Psi0)) / 720
check(
    "CAL-orders-0-5",
    all(abs(co[m]) < 1e-9 * scale for m in range(6)),
    f"(max |[f]_m|, m<=5: {max(abs(co[m]) for m in range(6)):.2e}, scale {scale:.2e})",
)

# ----------------------------------------------------------------------------
# 3a: order 6 with the V_8 menu
# ----------------------------------------------------------------------------
P6 = ["d", "beta", "gamma", "delta", "f7", "f6"]
if 6 in STEPS:

    def fixed6(par):
        return dict(par)

    def draw6():
        return {n: uni(-1.5, 1.5) for n in P6}

    names8, _, polys6, sols6, syms6, sol6 = run_order(
        "C3a",
        6,
        P6,
        monomials(P6, 2),
        draw6,
        fixed6,
        ["delta", "f7", "f6"],
        ["delta", "f7", "f6"],
        40,
        8,
    )
    # Step-2 comparison: at beta = gamma = 0 the contact equation must be delta - 1,
    # and delta_2, delta_6 as in (D.3) at a7 = -1, c6 = 0.
    if polys6 is not None:
        sub = {syms6["beta"]: 0, syms6["gamma"]: 0}
        d, f7, f6, delta = (syms6[n] for n in ("d", "f7", "f6", "delta"))
        expect = {
            0: delta - 1,
            1: sp.Rational(4, 5) * (8 - 2 * f7),
            5: sp.Rational(14, 25) * (d**2 - 8 * d + 4 * f6),
        }
        okc = all(sp.expand(polys6[i].subs(sub) - e) == 0 for i, e in expect.items())
        check(
            "CAL-step2-order6",
            okc,
            "(contact, S2, S6 of eq. (D.3) reproduced at beta = gamma = 0)",
        )


# ----------------------------------------------------------------------------
# 3b: order 7 on the order-6 family
# ----------------------------------------------------------------------------
# order-6 family (3a): beta, gamma, d free; delta = 1 - (beta + gamma)^2 / 4;
# f7 = 4; f6 = d (8 - d) / 4   [filled from the 3a run, see the record]
def family6(par):
    par = dict(par)
    par.setdefault("f7", 4.0)
    par["delta"] = 1 - (par["beta"] + par["gamma"]) ** 2 / 4
    par["f6"] = par["d"] * (8 - par["d"]) / 4
    return par


# A6 (Step 3): Sigma_4 at its Veronese point, beta + gamma = 2 (s = 1); the general s
# is block C's alpha-family (a mixing with the pure-Sigma_3 contact).
def veronese4(par):
    par = dict(par)
    par["gamma"] = 2 - par["beta"]
    return family6(par)


P7 = ["d", "beta", "lam", "mu", "nu", "f8", "f8p", "f7b", "f6b"]
if 7 in STEPS:

    def draw7():
        return {n: uni(-1, 1) for n in P7}

    # expected: degree <= 3 in (d, beta, lam, mu), linear in the five others
    low7 = ["d", "beta", "lam", "mu"]
    new7 = ["nu", "f8", "f8p", "f7b", "f6b"]
    mons7 = monomials(low7, 3) + [(n,) for n in new7]
    run_order(
        "C3b", 7, P7, mons7, draw7, veronese4, ["nu", "f8", "f7b", "f6b"], new7, 150, 12
    )


# order-7 family (3b) at the Veronese point s = 1 (gamma = 2 - beta): see the record,
# eq. (E.5); FAMILY7 is filled from the 3b run
def family7(par):
    par = veronese4(par)
    d, beta, lam, mu, f8p = (par[n] for n in ("d", "beta", "lam", "mu", "f8p"))
    par["nu"] = 1 - lam - mu
    par["f8"] = 4 - 2 * beta + beta * d / 2 - f8p
    par["f7b"] = F7B(d, beta, lam, mu, f8p)
    par["f6b"] = F6B(d, beta, lam, mu, f8p)
    return par


def F7B(d, beta, lam, mu, f8p):
    return d * d / 4 + 2  # (E.5), from the 3b run (as Step 2)


def F6B(d, beta, lam, mu, f8p):
    return d * (4 - d) / 4  # (E.5), from the 3b run (as Step 2)


STARS10 = {
    "V10(|10)",
    "V9(2|7) V5(2|3)",
    "V8(2,2|4) V5(2|3) V5(2|3)",
    "V7(2,2,2|1) V5(2|3) V5(2|3) V5(2|3)",
}
P8 = ["d", "beta", "lam", "mu", "f8p", "rho", "sigma", "f9", "f8c"]
if 8 in STEPS:

    def draw8():
        return {n: uni(-1, 1) for n in P8}

    low8 = ["d", "beta", "lam", "mu", "f8p"]
    new8 = [
        "rho",
        "sigma",
        "f9",
        "f8c",
    ]  # V7(U2^3, Psi) is quartic in the fields: excluded (A1)
    mons8 = monomials(low8, 4) + [(n,) for n in new8]
    names10, _, polys8, sols8, syms8, sol8 = run_order(
        "C3.3",
        8,
        P8,
        mons8,
        draw8,
        family7,
        ["d", "beta", "mu", "sigma", "f9", "f8c"],
        new8,
        200,
        14,
        thr=1e-5,  # fit-noise floor of the degree-4, 130-monomial fit (~1e-6); genuine coefficients >= 0.2
    )
    if polys8 is not None:
        key = lambda nm: tuple(sorted(nm.split()))  # noqa: E731
        hit = {key(nm) for nm, e in zip(names10, polys8) if e != 0}
        stars = {key(nm) for nm in STARS10}
        # H1 predicted: deficits on the four stars only.  Found (run7-step8.log): the
        # stars k = 0, 1, 2, 3 and four multi-node trees – the two exchanges
        # u8 p33 u8 (beta^2), u9 p44 u9 ((2 lam + mu)^2), the mixed V7(2,3|2) V5 V8
        # (beta d) and V7(2,3|2)^2 V5^2 (d^2); the k = 3 star carries 18 d^3 / 25 and
        # no coupling.  H1 is falsified; closure holds at d = 0, beta = 0, mu = -2 lam.
        found = {
            key(nm)
            for nm in (
                "V10(|10)",
                "V5(2|3) V9(2|7)",
                "V8(3|5) V8(3|5)",
                "V9(4|5) V9(4|5)",
                "V7(2,3|2) V5(2|3) V8(3|5)",
                "V8(2,2|4) V5(2|3) V5(2|3)",
                "V7(2,2,2|1) V5(2|3) V5(2|3) V5(2|3)",
                "V7(2,3|2) V7(2,3|2) V5(2|3) V5(2|3)",
            )
        }
        check(
            "C3.3-H1-falsified",
            hit == found and not hit <= stars,
            f"(regression guard on the recorded set; structures with a deficit: {sorted(' '.join(k) for k in hit)}; non-star: {len(hit - stars)})",
        )
        if sol8 is not None:
            d_fixed = syms8["d"] in sol8 and sol8[syms8["d"]] == 0
            check("C3.3-d-fixed", d_fixed, f"(solution: {sol8})")

# ----------------------------------------------------------------------------
# Fix pass: block F of record 101 (the rule), fit-free direct evaluations
# ----------------------------------------------------------------------------
if RULE:

    def rule_par(c6: float, lam: float, rho: float) -> dict:
        """Partner couplings from Sigma_2 -> Sigma_2 + Upsilon_2 in every coupling (F.6)."""
        return dict(
            c6=c6,
            d=3 * c6,
            dprime=2 * (1 - c6),
            f6=3 * c6,
            f6b=c6,
            f7=4.0,
            f7b=2.0,
            beta=0.0,
            gamma=2.0,
            delta=0.0,
            lam=lam,
            mu=-2 * lam,
            nu=1 + lam,
            f8=0.0,
            f8p=4.0,
            f8c=2.0,
            f9=-2 * lam,
            rho=rho,
            sigma=1 - rho,
        )

    lam0, rho0 = uni(-1, 1), uni(-1, 1)
    print(f"\n== F: rule point, lam = {lam0:.4f}, rho = {rho0:.4f}, N = {N} ==")
    SMAT = {}
    for order in (6, 7, 8):
        names, trees, S = structure_matrix(order + 2, PSI_DRAWS)
        SMAT[order] = (names, S)
        scale = np.max(np.abs(S))
        for c6 in (0.0, 1 / 3):
            par = rule_par(c6, lam0, rho0)
            _, _, rhs = deficit_vector(par, order, PSI_DRAWS, S)
            check(
                f"F-rule-order{order}-c6={c6:.3f}",
                np.max(np.abs(rhs)) < 1e-9 * scale,
                f"(max |{order + 2}! [f]_{order}| at the rule point: {np.max(np.abs(rhs)):.1e}; structure scale {scale:.1e})",
            )
    # departure d = 2 (table's value at c6 = 0) on the order-7 family: orders 6, 7
    # close, order 8 shows the recorded delta_27, delta_29 (fit-free projection)
    dep = rule_par(0.0, lam0, rho0)
    dep["d"] = 2.0
    dep["dprime"] = 2 + dep["c6"] - dep["d"]  # A5: d + d' = 2 + c6 (here d' = 0)
    dep = family7(dep)  # f6, f6b, f7b, f8 of (E.3), (E.5) at d = 2
    for order in (6, 7):
        names, S = SMAT[order]
        _, _, rhs = deficit_vector(dep, order, PSI_DRAWS, S)
        check(
            f"F-departure-order{order}-closed",
            np.max(np.abs(rhs)) < 1e-9 * np.max(np.abs(S)),
            f"(max |{order + 2}! [f]_{order}| at d = 2 on the family: {np.max(np.abs(rhs)):.1e})",
        )
    names, S = SMAT[8]
    coef, resid, rhs = deficit_vector(dep, 8, PSI_DRAWS, S)
    key = lambda nm: tuple(sorted(nm.split()))  # noqa: E731
    idx = {key(nm): i for i, nm in enumerate(names)}
    i27 = idx[key("V7(2,2,2|1) V5(2|3) V5(2|3) V5(2|3)")]
    i29 = idx[key("V7(2,3|2) V7(2,3|2) V5(2|3) V5(2|3)")]
    d = dep["d"]
    pred27, pred29 = 18 * d**3 / 25, 36 * d**2 / 35
    check(
        "F-departure-order8-complete",
        resid < 1e-8,
        f"(projection residual of the order-8 deficit at d = 2: {resid:.1e})",
    )
    check(
        "F-departure-order8-d3-d2",
        abs(coef[i27] - pred27) < 1e-6 * pred27
        and abs(coef[i29] - pred29) < 1e-6 * pred29
        and np.max(np.abs(rhs)) > 1e-3 * np.max(np.abs(S)),
        f"(k = 3 star {coef[i27]:.8f} vs 18 d^3/25 = {pred27:.8f}; "
        f"V7(2,3|2)^2 tree {coef[i29]:.8f} vs 36 d^2/35 = {pred29:.8f}; "
        f"max |10! [f]_8| {np.max(np.abs(rhs)):.2e})",
    )
    nz = [(nm, c) for nm, c in zip(names, coef) if abs(c) > 1e-6 * np.max(np.abs(coef))]
    print("   nonzero components at d = 2:")
    for nm, c in nz:
        print(f"     {c:+.6f}  {nm}")

# ----------------------------------------------------------------------------
nfail = sum(1 for _, ok, _ in results if not ok)
print(
    f"\n{len(results) - nfail}/{len(results)} checks PASS   ({time.time() - T0:.0f} s)"
)
sys.exit(1 if nfail else 0)
