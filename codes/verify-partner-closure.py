#!/usr/bin/env python3
"""verify-partner-closure.py – companion of agent/derivations/101-partner-count.md, Step 2.

Question: do the Upsilon_2 couplings close the p_{2,2}^{-1} structures of the
eliminated elementary action at O(g^6) (and O(g^7))?  Record 101, claims C1.4,
C2.3.

Model.  Psi in R^N, Sigma_2, Upsilon_2 in Sym^2, Sigma_3 in Sym^3 (orthonormal
bases), generic symmetric tensors V_4..V_9 in place of the vertices.  The
elementary action S^Upsilon (record 101 eq. (D.1); appendix E of the paper with
the order-6 and order-7 couplings added) is cubic in the auxiliaries; their
joint classical value at complex g is found by Newton iteration, continued
around a circle |g| = r, and the Taylor coefficients of
    f(g) = S^Upsilon(classical) - sum_n g^{n-2}/n! V_n(Psi^n)
are extracted by a Cauchy sum (r = 0.1, 32 points).  The deficit at order m,
(m+2)! [f]_{g^m} (the convention of R49 at m = 5), is a polynomial of degree m+2 in Psi; it is projected on the
whole-slot tree structures of record 101 block A (re-enumerated here with the
same rules; each tree evaluated generically with p_{s,s}^{-1} on its lines) by
least squares over random Psi draws.  The fit residual is the completeness check
of the catalogue.  The dependence of the projected deficit on the coupling
parameters is fitted by a polynomial on a random design and validated on held-out
points; the closure system is then solved exactly on the rationalised
coefficients.

Checks (named after the claim-tree nodes of record 101).
  CAL-orders-0-5 : the g^0..g^5 coefficients of f vanish (appendix E closure,
                   R42) at random parameters – the harness reproduces the paper.
  CAL-R49        : with no O(g^5) coupling at all (a7 = b7 = c = d = d' = 0),
                   7! [f]_{g^5} projects on (V7(Psi^7), I_1, I_2) with
                   (-1, -42/25, 7(2+c6)/5) (R49, eq. wsp:deficit).
  CAL-R49-break  : a wrong coefficient (-42/25 -> -42/24) is rejected.
  C0-trees-8/9   : re-enumeration with the collapse rule N2' (a node V_{2s} with
                   a strand-s line collapses: p_{s,s}^{-1} V_{2s}(., A) = A for
                   any filling A of the other s strands, lines included): 7 and
                   14 structures (step 1 counted 9 and 22 with the narrower N2).
  C1.4-basis     : the degree-8 structures are linearly independent as
                   polynomials of Psi on the draw (condition number).
  C1.4-c6=*-complete : the order-6 deficit lies in their span (fit residual) at
                   every parameter point of the design, for c6 = 0 and 1/3.
  C1.4-c6=*-polyfit  : the projected deficit is a polynomial of degree <= 2 in
                   (a7, d, e8, f7, f6) (held-out residual).
  C1.4-c6=*-deficit  : the rationalised deficit vector (printed) – the result.
  C1.4-c6=*-closure  : the closure system has a real solution family (d free);
                   Jacobian ranks printed.
  C1.4-c6=*-closure-break : perturbing a new coupling reopens the deficit.
  C1.4-c6=*-closure-direct: the deficit vanishes at the solution point, computed
                   directly (not through the fit).
  C2.3-*         : the same at order 7 (degree 9, 14 structures) on the order-6
                   solution family, degree-3 fit in (d, e9, f8, f7b, f6b).
  C0-trees-10    : (flag --d10, ~5 min) the degree-10 recount with N2'.

Not verified: string vertices (PH14–PH16), Upsilon_3 couplings (the question is
closure with Upsilon_2 alone), Sigma_4 (not forced before order 8).
"""

from __future__ import annotations

import itertools
import math
import sys
from fractions import Fraction

import numpy as np

SEED = 20261018
rng = np.random.default_rng(SEED)
print(f"seed = {SEED}")
results: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, info: str = "") -> None:
    results.append((name, ok, info))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {info}")


# ----------------------------------------------------------------------------
# Tree catalogue (copied from codes/verify-partner-count.py, strands (2, 3))
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
    for e in range(0, (3 - m) * smax + 1):
        n = sum(inc) + e
        if n < 3 or any(n < 2 * s for s in inc):
            continue
        # N2' (step 2): a node V_{2s} with a line of strand s collapses whatever
        # fills the other s strands (lines or externals): p_{s,s}^{-1} V_{2s}(., A) = A.
        # Covers N2 (one line, e = s; two equal lines, e = 0) and V6(2,3|1), V8(4,2|2), ...
        if any(n == 2 * s for s in inc):
            continue
        opts.append(e)
    return opts


def catalogue(D: int, smax: int, strands=(2, 3), kmax: int = 6):
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
N = 3
NMAX = 9


def sym_tensor(k: int) -> np.ndarray:
    t = rng.standard_normal((N,) * k)
    out = np.zeros_like(t)
    perms = list(itertools.permutations(range(k)))
    for p in perms:
        out += np.transpose(t, p)
    return out / len(perms)


def sym_basis(k: int) -> np.ndarray:
    """Orthonormal (Frobenius) basis of Sym^k(R^N), shape (dim, N, ..., N)."""
    out = []
    for c in itertools.combinations_with_replacement(range(N), k):
        t = np.zeros((N,) * k)
        ps = set(itertools.permutations(c))
        for p in ps:
            t[p] = 1.0
        out.append(t / np.sqrt(len(ps)))
    return np.array(out)


V = {n: sym_tensor(n) for n in range(4, NMAX + 1)}
B = {2: sym_basis(2), 3: sym_basis(3)}
DIM = {2: B[2].shape[0], 3: B[3].shape[0]}


def kinetic_matrix(s: int) -> np.ndarray:
    """p_{s,s} in the orthonormal basis: M[a,b] = V_{2s}(B_a, B_b)."""
    half = np.tensordot(B[s], V[2 * s], axes=(range(1, s + 1), range(s)))  # (dim, N^s)
    return np.tensordot(half, B[s], axes=(range(1, s + 1), range(1, s + 1)))


M = {s: kinetic_matrix(s) for s in (2, 3)}
# M[s][a,b] = V_{2s}(B_a, B_b) = p_{s,s} in the orthonormal basis
LETTERS = "abcdefghijklmnopqrstuvwxyz"


def reduce_vertex(n: int, slots: list, Psi: np.ndarray) -> np.ndarray:
    """Contract V_n with Psi on 'p' slots and with the Sym^s basis on s-slots.

    slots: list of 'p', 2 or 3 (sum of strands = n).  Returns an array with one
    axis (basis index) per field slot, in the order of the field slots.
    """
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
    return np.einsum(",".join(sub) + "->" + "".join(out), *ops)


def tree_value(k: int, edges, ext, Psi: np.ndarray, Minv: dict) -> float:
    """Value of a whole-slot tree structure: vertices on nodes, p_{s,s}^{-1} on lines."""
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
# The elementary action (record 101 eq. (D.1)); field coordinates x = (s2, s3, u2)
# ----------------------------------------------------------------------------
FIELDS = {"S2": (2, 0), "S3": (3, DIM[2]), "U2": (2, DIM[2] + DIM[3])}
NX = 2 * DIM[2] + DIM[3]


def terms(par: dict, order_max: int) -> list:
    """List of (g-power, coefficient, n, slots) with slots in {'p','S2','S3','U2'}."""
    c6, a7, d = par["c6"], par["a7"], par["d"]
    b7 = par.get("b7", 1 - a7)  # a7 + b7 = 1 (A5) unless overridden
    dp = par.get("dprime", 2 + c6 - d)  # d' = 2 + c6 - d (A5) unless overridden
    T = [
        (2, -1 / 24, 4, ["S2", "S2"]),
        (2, 2 / 24, 4, ["S2", "p", "p"]),
        (3, 1 / 120, 5, ["S2", "S2", "p"]),
        (2, par["a"] / 24, 4, ["U2", "U2"]),
        (3, par["b"] / 120, 5, ["U2", "S2", "p"]),
        (4, c6 / 720, 6, ["S2", "S2", "S2"]),
        (4, -(1 - c6) / 720, 6, ["S3", "S3"]),
        (4, 2 * (1 - c6) / 720, 6, ["S3", "S2", "p"]),
        (5, a7 / 5040, 7, ["S3", "S3", "p"]),
        (5, b7 / 5040, 7, ["S3", "S2", "S2"]),
        (3, par["c"] / 120, 5, ["U2", "U2", "p"]),
        (4, d / 720, 6, ["U2", "S2", "S2"]),
        (4, dp / 720, 6, ["U2", "S3", "p"]),
    ]
    if order_max >= 6:
        T += [
            (6, par["e8"] / 40320, 8, ["S3", "S3", "S2"]),
            (5, par["f7"] / 5040, 7, ["U2", "S3", "S2"]),
            (4, par["f6"] / 720, 6, ["U2", "U2", "S2"]),
        ]
    if order_max >= 7:
        T += [
            (7, par["e9"] / 362880, 9, ["S3", "S3", "S3"]),
            (6, par["f8"] / 40320, 8, ["U2", "S3", "S3"]),
            (5, par["f7b"] / 5040, 7, ["U2", "U2", "S3"]),
            (4, par["f6b"] / 720, 6, ["U2", "U2", "U2"]),
        ]
    return T


class Action:
    """Cubic polynomial in x for fixed Psi: S = sum_m g^m (c_m + L_m x + x Q_m x + C_m xxx)."""

    def __init__(self, par: dict, order_max: int, Psi: np.ndarray):
        self.c = {}
        self.L = {}
        self.Q = {}
        self.C = {}
        for m, coef, n, slots in terms(par, order_max):
            fs = [s for s in slots if s != "p"]
            arr = coef * reduce_vertex(
                n, [("p" if s == "p" else FIELDS[s][0]) for s in slots], Psi
            )
            offs = [FIELDS[s][1] for s in fs]
            dims = [DIM[FIELDS[s][0]] for s in fs]
            if len(fs) == 1:
                L = self.L.setdefault(m, np.zeros(NX))
                L[offs[0] : offs[0] + dims[0]] += arr
            elif len(fs) == 2:
                Q = self.Q.setdefault(m, np.zeros((NX, NX)))
                Q[offs[0] : offs[0] + dims[0], offs[1] : offs[1] + dims[1]] += arr
            else:
                C = self.C.setdefault(m, np.zeros((NX, NX, NX)))
                C[
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
            grad = L + 2 * Q @ x + 3 * np.einsum("ijk,j,k->i", C, x, x)
            hess = 2 * Q + 6 * np.einsum("ijk,k->ij", C, x)
            dx = np.linalg.solve(hess, -grad)
            x = x + dx
            if np.max(np.abs(dx)) < 1e-15 * max(1.0, np.max(np.abs(x))):
                break
        grad = L + 2 * Q @ x + 3 * np.einsum("ijk,j,k->i", C, x, x)
        if np.max(np.abs(grad)) > 1e-10 * abs(g) ** 2:
            raise RuntimeError(
                f"Newton did not converge at g={g}: |grad|={np.max(np.abs(grad))}"
            )
        val = L @ x + x @ Q @ x + np.einsum("ijk,i,j,k", C, x, x, x)
        return val, x


def target(g: complex, Psi: np.ndarray, nmax: int) -> complex:
    tot = 0.0
    for n in range(4, nmax + 1):
        tot += g ** (n - 2) / math.factorial(n) * reduce_vertex(n, ["p"] * n, Psi)
    return tot


def veronese(Psi: np.ndarray) -> np.ndarray:
    x0 = np.zeros(NX)
    P2 = np.einsum("i,j->ij", Psi, Psi)
    P3 = np.einsum("i,j,k->ijk", Psi, Psi, Psi)
    x0[0 : DIM[2]] = np.einsum("aij,ij->a", B[2], P2)
    x0[DIM[2] : DIM[2] + DIM[3]] = np.einsum("aijk,ijk->a", B[3], P3)
    return x0


def taylor(
    par: dict, order_max: int, Psi: np.ndarray, orders, r: float = 0.1, K: int = 32
):
    """Taylor coefficients of f(g) = S^Upsilon(classical) - S_target at the given orders."""
    act = Action(par, order_max, Psi)
    x = veronese(Psi)
    vals = []
    for k in range(K):
        g = r * np.exp(2j * np.pi * k / K)
        v, x = act.saddle_value(g, x)
        vals.append(v - target(g, Psi, order_max + 2))
    vals = np.array(vals)
    ks = np.arange(K)
    return {
        m: complex(np.sum(vals * np.exp(-2j * np.pi * ks * m / K)) / (K * r**m))
        for m in orders
    }


# ----------------------------------------------------------------------------
# Baseline parameters (appendix E through O(g^5), R42/R49) and draws
# ----------------------------------------------------------------------------
BASE = {"a": 1.0, "b": 2.0, "c": 1.0}


def rand_par(order_max: int, box: float = 1.5) -> dict:
    par = dict(BASE)
    for name in ("c6", "a7", "d", "e8", "f7", "f6", "e9", "f8", "f7b", "f6b"):
        par[name] = float(rng.uniform(-box, box))
    # the Sigma_3 kinetic term carries (1 - c6): keep it away from 0 so that the
    # Taylor series of the saddle converges well inside |g| = r
    par["c6"] = float(rng.uniform(-0.5, 0.5))
    return par


Minv = {s: np.linalg.inv(M[s]) for s in (2, 3)}
PSI_DRAWS = [rng.standard_normal(N) for _ in range(30)]

# ----------------------------------------------------------------------------
# CAL: the harness reproduces appendix E through O(g^5)
# ----------------------------------------------------------------------------
Psi0 = PSI_DRAWS[0]
par0 = rand_par(7)
co = taylor(par0, 7, Psi0, range(0, 6))
scale = abs(reduce_vertex(6, ["p"] * 6, Psi0)) / 720
ok = all(abs(co[m]) < 1e-9 * scale for m in range(0, 6))
check(
    "CAL-orders-0-5",
    ok,
    f"(max |[f]_m|, m<=5: {max(abs(co[m]) for m in range(6)):.2e}, scale {scale:.2e})",
)


# R49: switch off the O(g^5) partner couplings; the g^5 deficit on (V7, I1, I2)
def structures_5(Psi):
    v = reduce_vertex(5, [2, "p", "p", "p"], Psi)
    W = reduce_vertex(5, [2, 2, "p"], Psi)
    g6 = reduce_vertex(6, [2, "p", "p", "p", "p"], Psi)
    pv = Minv[2] @ v
    return np.array([reduce_vertex(7, ["p"] * 7, Psi), pv @ W @ pv, g6 @ pv])


A = []
rhs = []
par5 = dict(
    par0, c=0.0, d=0.0, dprime=0.0, c6=0.4, a7=0.0, b7=0.0
)  # no O(g^5) coupling at all
for Psi in PSI_DRAWS[:8]:
    A.append(structures_5(Psi))
    rhs.append(5040 * taylor(par5, 5, Psi, [5])[5].real)
A = np.array(A)
rhs = np.array(rhs)
coef5, res5, rk5, sv5 = np.linalg.lstsq(A, rhs, rcond=None)
pred5 = np.array([-1.0, -42 / 25, 7 * (2 + par5["c6"]) / 5])
resid5 = np.max(np.abs(A @ coef5 - rhs)) / np.max(np.abs(rhs))
check(
    "CAL-R49",
    np.allclose(coef5, pred5, rtol=1e-6, atol=1e-9) and resid5 < 1e-8,
    f"(fit {coef5}, R49 {pred5}, fit residual {resid5:.1e})",
)
check(
    "CAL-R49-break",
    not np.allclose(coef5, [-1.0, -42 / 24, pred5[2]], rtol=1e-6),
    "(-42/24 rejected)",
)


# ----------------------------------------------------------------------------
# Structures and deficit projection at a given order
# ----------------------------------------------------------------------------
def structure_matrix(D: int, draws):
    cat = catalogue(D, 3)
    trees = sorted(cat.values(), key=lambda t: (t[0], describe(*t)))
    names = [describe(*t) for t in trees]
    S = np.array([[tree_value(*t, Psi, Minv) for t in trees] for Psi in draws])
    return names, trees, S


def deficit_vector(par: dict, order_max: int, draws, S: np.ndarray, norm: float):
    rhs = np.array(
        [
            norm * taylor(par, order_max, Psi, [order_max])[order_max].real
            for Psi in draws
        ]
    )
    coef, _, _, _ = np.linalg.lstsq(S, rhs, rcond=None)
    resid = np.max(np.abs(S @ coef - rhs)) / max(np.max(np.abs(rhs)), 1e-300)
    return coef, resid, rhs


def monomials(names: list[str], deg: int):
    mons = [()]
    for dd in range(1, deg + 1):
        mons += list(itertools.combinations_with_replacement(names, dd))
    return mons


def polyfit_params(
    fun, pnames: list[str], deg: int, order_max: int, npts: int, nhold: int
):
    mons = monomials(pnames, deg)
    pts = [rand_par(order_max) for _ in range(npts + nhold)]
    X = np.array([[np.prod([p[n] for n in mon]) for mon in mons] for p in pts])
    Y = np.array([fun(p) for p in pts])
    coef, *_ = np.linalg.lstsq(X[:npts], Y[:npts], rcond=None)
    hold = np.max(np.abs(X[npts:] @ coef - Y[npts:])) / max(np.max(np.abs(Y)), 1e-300)
    return mons, coef, hold


def rationalise(x: float, maxden: int = 20000, tol: float = 1e-6):
    fr = Fraction(x).limit_denominator(maxden)
    return fr if abs(float(fr) - x) < tol * max(1.0, abs(x)) else None


def poly_str(mons, col) -> str:
    out = []
    for mon, c in zip(mons, col):
        if abs(c) < 1e-7:
            continue
        fr = rationalise(c)
        cs = str(fr) if fr is not None else f"{c:.6g}"
        out.append(cs + ("*" + "*".join(mon) if mon else ""))
    return " + ".join(out) if out else "0"


# ----------------------------------------------------------------------------
# C1.4: order 6
# ----------------------------------------------------------------------------
print("\n== order 6 (degree 8) ==")
names8, trees8, S8 = structure_matrix(8, PSI_DRAWS)
check(
    "C0-trees-8",
    len(names8) == 7,
    f"({len(names8)} structures after the collapse rule N2'; step 1 counted 9, two of which collapse)",
)
for i, nm in enumerate(names8):
    print(f"   S{i + 1}: {nm}")
sv = np.linalg.svd(S8 / np.linalg.norm(S8, axis=0), compute_uv=False)
check(
    "C1.4-basis",
    sv[-1] / sv[0] > 1e-6,
    f"(column-normalised singular values {sv[0]:.2e} .. {sv[-1]:.2e})",
)

import sympy as sp

P5 = ["a7", "d", "e8", "f7", "f6"]


def to_sympy(mons, col, syms: dict, name: str):
    """Rationalised sympy polynomial from a fitted coefficient column; None if a
    coefficient is not a small rational."""
    expr = sp.Integer(0)
    for mon, c in zip(mons, col):
        if abs(c) < 1e-7:
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


def closure_analysis(label: str, names, mons, coef, pnames, solve_for, new_names):
    """Solve delta_k = 0 for `solve_for` (the other parameters stay free); report
    unreached structures, the solution family, the Jacobian ranks."""
    syms = {n: sp.Symbol(n) for n in pnames}
    polys = []
    for i, nm in enumerate(names):
        e = to_sympy(mons, coef[:, i], syms, f"delta_{i + 1}")
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
        f"unreached: {unreached or 'none'}; solutions (free: {[n for n in pnames if n not in solve_for]}): {real_sols}"
    )
    for sol in real_sols:
        J_new = sp.Matrix(
            [[sp.diff(e, syms[n]) for n in new_names] for e in nontriv]
        ).subs(sol)
        J_all = sp.Matrix(
            [[sp.diff(e, syms[n]) for n in pnames] for e in nontriv]
        ).subs(sol)
        print(
            f"   at the solution: Jacobian rank in the new couplings {J_new.rank()} (of {len(new_names)}), "
            f"in all parameters {J_all.rank()} (of {len(pnames)}); {len(pnames) - J_all.rank()} free direction(s)"
        )
    return polys, real_sols, syms


def closure_checks(
    tag: str,
    polys,
    sols,
    syms,
    pnames,
    new_names,
    fixed: dict,
    order_max: int,
    S,
    norm: float,
):
    check(
        f"{tag}-closure",
        bool(sols),
        f"({len(sols) if sols else 0} real solution family/ies)",
    )
    if not sols:
        return
    sol = dict(sols[0])
    free_vals = {syms[n]: sp.Rational(3, 7) for n in pnames if syms[n] not in sol}
    sol_num = {k: v.subs(free_vals) for k, v in sol.items()}
    sol_num.update(free_vals)
    # break: perturb one new coupling -> the deficit reopens
    key = syms[new_names[1]]
    pert = dict(sol_num)
    pert[key] = sol_num[key] + sp.Rational(1, 10)
    vals = [sp.simplify(e.subs(pert)) for e in polys]
    check(
        f"{tag}-closure-break",
        any(v != 0 for v in vals),
        f"(perturbed {key}: deficit {vals})",
    )
    # direct numerical confirmation at the solution point, not through the fit
    parsol = dict(BASE, **fixed, **{n: float(sol_num[syms[n]]) for n in pnames})
    if "f6_of_d" in fixed:
        parsol.pop("f6_of_d")
        parsol["f6"] = parsol["d"] * (8 - parsol["d"]) / 4
    _, _, rhs = deficit_vector(parsol, order_max, PSI_DRAWS, S, norm)
    scale = np.max(np.abs(S))
    check(
        f"{tag}-closure-direct",
        np.max(np.abs(rhs)) < 1e-9 * scale,
        f"(max |{order_max + 2}! [f]_{order_max}| over 30 Psi draws at {parsol}: {np.max(np.abs(rhs)):.1e}; structure scale {scale:.1e})",
    )


print("\n-- order 6, c6 fixed; quadratic fit in", P5)
for c6val in (0.0, 1 / 3):
    resids = []

    def dv6(par, c6val=c6val):
        par = dict(par, c6=c6val)
        coef, resid, _ = deficit_vector(par, 6, PSI_DRAWS, S8, math.factorial(8))
        resids.append(resid)
        return coef

    mons6, coef6, hold6 = polyfit_params(dv6, P5, 2, 6, 30, 6)
    tag = f"C1.4-c6={c6val:.3g}"
    check(
        f"{tag}-complete",
        max(resids) < 1e-8,
        f"(max projection residual over 36 parameter points {max(resids):.1e})",
    )
    check(
        f"{tag}-polyfit",
        hold6 < 1e-8,
        f"(held-out residual of the degree-2 fit: {hold6:.1e})",
    )
    print(f"   deficit vector 8! [S^Upsilon - S_<=8]_(g^6) at c6 = {c6val:.3g}:")
    polys, sols, syms = closure_analysis(
        tag, names8, mons6, coef6, P5, ["a7", "e8", "f7", "f6"], ["e8", "f7", "f6"]
    )
    check(
        f"{tag}-deficit", polys is not None, "(rational deficit vector printed above)"
    )
    closure_checks(
        tag,
        polys,
        sols,
        syms,
        P5,
        ["e8", "f7", "f6"],
        {"c6": c6val},
        6,
        S8,
        math.factorial(8),
    )

# ----------------------------------------------------------------------------
# C2.3: order 7 on the order-6 solution family (c6 = 0, a7 = -1, e8 = 1, f7 = 4,
# f6 = d (8 - d) / 4, d free)
# ----------------------------------------------------------------------------
print("\n== order 7 (degree 9) ==")
names9, trees9, S9 = structure_matrix(9, PSI_DRAWS)
check(
    "C0-trees-9",
    len(names9) == 14,
    f"({len(names9)} structures after N2', expected 14; step 1 counted 22 under N2)",
)
for i, nm in enumerate(names9):
    print(f"   T{i + 1}: {nm}")
sv = np.linalg.svd(S9 / np.linalg.norm(S9, axis=0), compute_uv=False)
check(
    "C2.3-basis",
    sv[-1] / sv[0] > 1e-6,
    f"(column-normalised singular values {sv[0]:.2e} .. {sv[-1]:.2e})",
)
P7 = ["d", "e9", "f8", "f7b", "f6b"]
FIX7 = {"c6": 0.0, "a7": -1.0, "e8": 1.0, "f7": 4.0}
resids = []


def dv7(par):
    par = dict(par, **FIX7)
    par["f6"] = par["d"] * (8 - par["d"]) / 4
    coef, resid, _ = deficit_vector(par, 7, PSI_DRAWS, S9, math.factorial(9))
    resids.append(resid)
    return coef


mons7, coef7, hold7 = polyfit_params(dv7, P7, 3, 7, 70, 10)
check(
    "C2.3-complete",
    max(resids) < 1e-8,
    f"(max projection residual over 80 parameter points {max(resids):.1e})",
)
# degree-3 fit on 70 points at the 9! scale: 1e-7 relative is the Cauchy-sum floor
check(
    "C2.3-polyfit",
    hold7 < 1e-7,
    f"(held-out residual of the degree-3 fit in {P7}: {hold7:.1e})",
)
print("   deficit vector 9! [S^Upsilon - S_<=9]_(g^7) on the order-6 solution family:")
polys7, sols7, syms7 = closure_analysis(
    "C2.3",
    names9,
    mons7,
    coef7,
    P7,
    ["e9", "f8", "f7b", "f6b"],
    ["e9", "f8", "f7b", "f6b"],
)
check("C2.3-deficit", polys7 is not None, "(rational deficit vector printed above)")
if polys7 is not None:
    closure_checks(
        "C2.3",
        polys7,
        sols7,
        syms7,
        P7,
        ["e9", "f8", "f7b", "f6b"],
        dict(FIX7, f6_of_d=True),
        7,
        S9,
        math.factorial(9),
    )

if "--d10" in sys.argv:
    cat10 = catalogue(10, 4, strands=(2, 3, 4))
    no2 = [v for v in cat10.values() if all(s != 2 for _, _, s in v[1])]
    # 35 cubic trees under N2'; the catalogue of record 101 adds the k = 3 collapse
    # product (rule N2''), 36 in all (verify-partner-octic.py C3.3-complete)
    check(
        "C0-trees-10",
        (len(cat10), len(no2)) == (35, 7),
        f"({len(cat10)} structures after N2' with Sigma_4, {len(no2)} without a strand-2 line; expected 35, 7; step 1 counted 77, 9 under N2)",
    )

# ----------------------------------------------------------------------------
nfail = sum(1 for _, ok, _ in results if not ok)
print(f"\n{len(results) - nfail}/{len(results)} checks PASS")
sys.exit(1 if nfail else 0)
