"""Verify record 066: the Hessian of the cubic HS action is affine in the background.

Record: ``agent/derivations/066-hessian-affine-background.md``. Check labels = claim-tree
nodes. Finite cubic HS model of records 057/060 (generic random rational totally symmetric
tensors, exact sympy arithmetic; inertia counted with mpmath at 50 digits, kernel
dimension by exact rank).

Actions (A2 of the record):
    S3  = V2/2 + g V3/3! - g^2/4! V4(S2,S2) + 2g^2/4! V4(S2,Psi^2) + g^3/5! V5(S2,S2,Psi)
    S4  = S3 + g^4/6! W6(S2^3)                          (W6 a generic symmetric tensor here)
    tower (R26 scheme B, K=3) = S3 + g^4/6! [ -M3(S3,S3) + 2 T6(S3,S2,Psi) ]
                                   + g^5/7! T7(S3,S3,Psi)
Checks:
  C1.2 / C1.3  hand blocks (1.4)/(1.5) == sympy Hessian, exactly, at a random background;
               every Hessian entry has total degree <= 1 in the fields (affine); break leg:
               a quartic monomial added to the action gives degree-2 entries; a wrong
               coefficient (g^3/48 for g^3/60) fails the block comparison.
  C2.1         In(H) = In(Hess V_eff) + In(H_aux) at an engineered joint critical point,
               with Hess V_eff computed by an independent epsilon-expansion of the
               eliminated action (series solve of the linear auxiliary equations), not by
               the Schur formula; break leg: the sign of H_aux flipped.
  C2.2         the critical point is engineered so that Hess V_eff has a one-dimensional
               kernel x; then dim ker H = 1 exactly and (x, Sigma_*' x) is in ker H, with
               Sigma_*' x the first-order saddle shift from the epsilon-expansion; break
               leg: (x, 0) is not a zero mode.
  C2.3         the pencil eigenvalues of G^{-1} H and of the block direct sum differ
               (congruent, not isospectral) for a random indefinite G = w1 (+) w1^2 (+) w1^3.
  C3           one-field S4 model: at the fold (Sigma-EOM = 0 = H_ss) the joint Hessian
               has det H = -H_ts^2 != 0, inertia (1,1), while V_eff'' on the sheet diverges
               as delta^{-1/2}.
Not verified: anything about the string vertices (finite model only); the exhaustion
orders of Tables 1.1-1.2 are presentation facts (R17, R19, R26), not tested here.
"""

from __future__ import annotations

import itertools
import sys

import mpmath as mp
import numpy as np
import sympy as sp

SEED = 20261001
failures: list[str] = []
npass = 0
g = sp.Symbol("g")


def report(name: str, ok: bool, detail: str = "") -> None:
    """Print a labelled PASS/FAIL line and record failures."""
    global npass
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")
    if ok:
        npass += 1
    else:
        failures.append(name)


# ------------------------------------------------------------------ tensors
def rand_sym(rng: np.random.Generator, n: int, k: int, den: int = 3) -> dict:
    """Random totally symmetric rational tensor: dict full-index -> Rational."""
    T = {}
    for c in itertools.combinations_with_replacement(range(n), k):
        val = sp.Rational(int(rng.integers(-5, 6)), den)
        for p in set(itertools.permutations(c)):
            T[p] = val
    return T


def basis_elem(idx: tuple) -> dict:
    """Symmetric basis tensor E_idx: 1 on every permutation of idx."""
    return {p: sp.Integer(1) for p in set(itertools.permutations(idx))}


def contract(T: dict, args: list) -> sp.Expr:
    """T(a_1, ..., a_m) for symmetric tensor arguments (dicts full-index -> expr)."""
    ranks = [len(next(iter(a))) for a in args]
    tot = sp.Integer(0)
    for idx, val in T.items():
        term = val
        pos = 0
        for a, r in zip(args, ranks):
            v = a.get(idx[pos:pos + r], 0)
            if v == 0:
                term = 0
                break
            term = term * v
            pos += r
        if term != 0:
            tot += term
    return sp.expand(tot)


def sym_coords(n: int, k: int, prefix: str):
    """Coordinates on Sym^k R^n: independent components, and the tensor dict."""
    idxs = list(itertools.combinations_with_replacement(range(n), k))
    syms = sp.symbols(f"{prefix}0:{len(idxs)}")
    tens = {}
    for s, idx in zip(syms, idxs):
        for p in set(itertools.permutations(idx)):
            tens[p] = s
    return idxs, list(syms), tens


class Model:
    """Fields Psi in R^n, Sigma_2 in Sym^2, Sigma_3 in Sym^3, all coordinates symbolic."""

    def __init__(self, seed: int, n: int, tower: bool):
        rng = np.random.default_rng(seed)
        self.n, self.tower = n, tower
        self.V = {k: rand_sym(rng, n, k) for k in range(2, 8)}
        self.W6 = rand_sym(rng, n, 6)
        self.M3 = rand_sym(rng, n, 6)  # Sym^3 x Sym^3 form
        self.T6 = rand_sym(rng, n, 6)
        self.T7 = rand_sym(rng, n, 7)
        self.xs = list(sp.symbols(f"x0:{n}"))
        self.psi = {(a,): self.xs[a] for a in range(n)}
        self.i2, self.ys, self.S2 = sym_coords(n, 2, "y")
        self.i3, self.zs, self.S3 = sym_coords(n, 3, "z")
        self.E2 = [basis_elem(i) for i in self.i2]
        self.E3 = [basis_elem(i) for i in self.i3]
        self.e1 = [basis_elem((a,)) for a in range(n)]
        self.aux = self.ys + (self.zs if tower else [])
        self.fields = self.xs + self.aux
        self.rng = rng

    def action(self, order: int, with_V2: bool = True, quartic_break: bool = False,
               coef_break: bool = False) -> sp.Expr:
        V, psi, S2, S3 = self.V, self.psi, self.S2, self.S3
        S = g / 6 * contract(V[3], [psi] * 3)
        if with_V2:
            S += sp.Rational(1, 2) * contract(V[2], [psi] * 2)
        S += -g**2 / 24 * contract(V[4], [S2, S2]) + g**2 / 12 * contract(V[4], [S2, psi, psi])
        c5 = sp.Rational(1, 96) if coef_break else sp.Rational(1, 120)
        S += g**3 * c5 * contract(V[5], [S2, S2, psi])
        if order >= 4 and not self.tower:
            S += g**4 / 720 * contract(self.W6, [S2, S2, S2])
        if self.tower:
            S += g**4 / 720 * (-contract(self.M3, [S3, S3]) + 2 * contract(self.T6, [S3, S2, psi]))
            S += g**5 / 5040 * contract(self.T7, [S3, S3, psi])
        if quartic_break:
            S += g**4 / 24 * contract(V[4], [S2, S2]) * contract(V[2], [psi] * 2)
        return sp.expand(S)

    def hessian(self, S: sp.Expr) -> sp.Matrix:
        f = self.fields
        return sp.Matrix(len(f), len(f), lambda i, j: sp.diff(S, f[i], f[j]))

    def hand_blocks(self, order: int, x0, y0, z0) -> sp.Matrix:
        """Tables 1.1 / 1.2 of the record assembled from the vertices and the background."""
        n, V = self.n, self.V
        P0 = {(a,): x0[a] for a in range(n)}
        S20 = {p: y0[k] for k, i in enumerate(self.i2) for p in set(itertools.permutations(i))}
        S30 = {p: z0[k] for k, i in enumerate(self.i3) for p in set(itertools.permutations(i))}
        e1, E2, E3 = self.e1, self.E2, self.E3
        Hxx = sp.Matrix(n, n, lambda a, b: contract(V[2], [e1[a], e1[b]])
                        + g * contract(V[3], [P0, e1[a], e1[b]])
                        + g**2 / 6 * contract(V[4], [S20, e1[a], e1[b]]))
        Hyx = sp.Matrix(len(E2), n, lambda P, a: g**2 / 6 * contract(V[4], [E2[P], P0, e1[a]])
                        + g**3 / 60 * contract(V[5], [E2[P], S20, e1[a]]))
        Hyy = sp.Matrix(len(E2), len(E2), lambda P, Q: -g**2 / 12 * contract(V[4], [E2[P], E2[Q]])
                        + g**3 / 60 * contract(V[5], [E2[P], E2[Q], P0]))
        if order >= 4 and not self.tower:
            Hyy += sp.Matrix(len(E2), len(E2), lambda P, Q: g**4 / 120 * contract(
                self.W6, [S20, E2[P], E2[Q]]))
        blocks = [[Hxx, Hyx.T], [Hyx, Hyy]]
        if self.tower:
            Hyx += sp.Matrix(len(E2), n, lambda P, a: g**4 / 360 * contract(
                self.T6, [S30, E2[P], e1[a]]))
            Hzx = sp.Matrix(len(E3), n, lambda P, a: g**4 / 360 * contract(self.T6, [E3[P], S20, e1[a]])
                            + g**5 / 2520 * contract(self.T7, [E3[P], S30, e1[a]]))
            Hzy = sp.Matrix(len(E3), len(E2), lambda P, Q: g**4 / 360 * contract(
                self.T6, [E3[P], E2[Q], P0]))
            Hzz = sp.Matrix(len(E3), len(E3), lambda P, Q: -g**4 / 360 * contract(self.M3, [E3[P], E3[Q]])
                            + g**5 / 2520 * contract(self.T7, [E3[P], E3[Q], P0]))
            blocks = [[Hxx, Hyx.T, Hzx.T], [Hyx, Hyy, Hzy.T], [Hzx, Hzy, Hzz]]
        return sp.Matrix(sp.BlockMatrix(blocks)).applyfunc(sp.expand)

    def rand_point(self):
        r = lambda: sp.Rational(int(self.rng.integers(-4, 5)) or 1, 2)  # noqa: E731
        return ([r() for _ in self.xs], [r() for _ in self.ys], [r() for _ in self.zs])


# ------------------------------------------------------------------ helpers
def inertia(M: sp.Matrix, tol: str = "1e-25"):
    """(n_+, n_-, n_0) with n_0 from the exact rank, n_+/- from mpmath eigenvalues."""
    mp.mp.dps = 50
    n = M.shape[0]
    n0 = n - M.rank()
    A = mp.matrix([[mp.mpf(sp.Rational(M[i, j]).p) / mp.mpf(sp.Rational(M[i, j]).q)
                    for j in range(n)] for i in range(n)])
    ev = mp.eigsy(A)[0]
    t = mp.mpf(tol)
    npos = sum(1 for e in ev if e > t)
    nneg = sum(1 for e in ev if e < -t)
    assert npos + nneg + n0 == n, "inertia count inconsistent with exact rank"
    return (npos, nneg, n0)


def eff_expansion(mod: Model, S_noV2: sp.Expr, x0: list, gval):
    """Epsilon-expansion of the eliminated action at Psi = x0 + eps*xi (V2 = 0).

    Returns (b, N, sig0, sig1) with b = grad V_eff (V2=0), N = Hess V_eff (V2=0),
    sig0 = Sigma_*(x0), sig1 = the linear map xi -> first-order saddle shift (matrix).
    The auxiliary gradient is linear in the tower jointly: grad = M(Psi) Sigma + c(Psi).
    """
    eps = sp.Symbol("eps")
    xi = list(sp.symbols(f"xi0:{mod.n}"))
    sub = {x: x0i + eps * xii for x, x0i, xii in zip(mod.xs, x0, xi)}
    S = sp.expand(S_noV2.subs(g, gval).subs(sub))
    aux = mod.aux
    grad = sp.Matrix([sp.diff(S, a) for a in aux])
    Mm = sp.Matrix([[sp.diff(gi, a) for a in aux] for gi in grad]).applyfunc(sp.expand)
    c = grad.subs({a: 0 for a in aux}).applyfunc(sp.expand)
    assert all(sp.Poly(e, *aux).total_degree() <= 0 for e in Mm), "aux sector not linear"
    M0 = Mm.applyfunc(lambda e: e.coeff(eps, 0))
    M1 = Mm.applyfunc(lambda e: e.coeff(eps, 1))
    assert Mm.applyfunc(lambda e: sp.expand(e).coeff(eps, 2)) == sp.zeros(*Mm.shape)
    c0, c1, c2 = (c.applyfunc(lambda e: e.coeff(eps, k)) for k in range(3))
    M0i = M0.inv()
    s0 = -M0i * c0
    s1 = (-M0i * (c1 + M1 * s0)).applyfunc(sp.expand)
    s2 = (-M0i * (c2 + M1 * s1)).applyfunc(sp.expand)
    sig = s0 + eps * s1 + eps**2 * s2
    Veff = sp.expand(S.subs(dict(zip(aux, list(sig)))))
    V1 = Veff.coeff(eps, 1)
    V2c = Veff.coeff(eps, 2)
    b = sp.Matrix([sp.diff(V1, v) for v in xi])
    N = sp.Matrix(mod.n, mod.n, lambda i, j: sp.diff(V2c, xi[i], xi[j]))
    sig1 = sp.Matrix(len(aux), mod.n, lambda i, j: sp.diff(s1[i], xi[j]))
    return b, N, s0, sig1


def engineer_V2(mod: Model, x0: list, b: sp.Matrix, N: sp.Matrix, xk: list) -> sp.Matrix:
    """Symmetric V2 with V2 x0 = -b (critical point) and (V2 + N) xk = 0 (kernel)."""
    n = mod.n
    syms = {}
    V2 = sp.zeros(n, n)
    for i in range(n):
        for j in range(i, n):
            syms[(i, j)] = sp.Symbol(f"v{i}{j}")
            V2[i, j] = V2[j, i] = syms[(i, j)]
    # consistency: xk.(V2 x0) = x0.(V2 xk) forces xk.(b - N x0) = 0, which xk satisfies
    # by construction (kernel_direction); the system then has rank 5 on 6 unknowns and
    # the free parameter is fixed to a random rational.
    eqs = list(V2 * sp.Matrix(x0) + b) + list((V2 + N) * sp.Matrix(xk))
    sol = sp.solve(eqs, list(syms.values()), dict=True)
    assert len(sol) == 1, "V2 engineering inconsistent"
    V2 = V2.subs(sol[0])
    free = sorted(V2.free_symbols, key=str)
    assert len(free) == (1 if n == 3 else 0), f"unexpected free parameters {free}"
    return V2.subs(free[0], sp.Rational(int(mod.rng.integers(-3, 4)) or 1, 5)) if free else V2


def kernel_direction(x0: list, b: sp.Matrix, N: sp.Matrix) -> list:
    """A rational xk with xk.(b - N x0) = 0 (needed for a symmetric V2 to exist)."""
    d = list(b - N * sp.Matrix(x0))
    xk = [d[1], -d[0]] if len(d) == 2 else [d[1] + d[2] / 2, -d[0], -d[0] / 2]
    assert sum(a * c for a, c in zip(xk, d)) == 0 and any(v != 0 for v in xk)
    return xk


def set_V2(mod: Model, V2: sp.Matrix) -> None:
    mod.V[2] = {(i, j): V2[i, j] for i in range(mod.n) for j in range(mod.n)}


# ------------------------------------------------------------------ Part 1: affine blocks
def part1() -> None:
    print("\n=== Part 1: affine Hessian, hand blocks vs sympy (exact) ===")
    for tower, order, label in ((False, 3, "S3"), (False, 4, "S4"), (True, 4, "tower")):
        mod = Model(SEED + (1 if tower else 0), n=2, tower=tower)
        S = mod.action(order)
        H = mod.hessian(S)
        degs = [sp.Poly(e, *mod.fields).total_degree() if e != 0 else 0 for e in H]
        node = "C1.3" if tower else "C1.2"
        report(f"{node}-affine-{label}", max(degs) <= 1 and max(degs) == 1,
               f"max total degree of Hessian entries in the fields = {max(degs)} (affine)")
        x0, y0, z0 = mod.rand_point()
        sub = dict(zip(mod.fields, x0 + y0 + (z0 if tower else [])))
        Hs = H.subs(sub).applyfunc(sp.expand)
        Hh = mod.hand_blocks(order, x0, y0, z0)
        report(f"{node}-blocks-{label}", Hs == Hh,
               f"sympy Hessian == Table {'1.2' if tower else '1.1'} blocks at a random point, "
               f"dim {H.shape[0]}, all g-orders")
        # lambda-scaling: H(lambda phi0) linear in lambda, second difference zero
        lam = sp.Symbol("lam")
        Hl = H.subs({f: lam * v for f, v in sub.items()})
        d2 = (Hl.subs(lam, 2) - 2 * Hl.subs(lam, 1) + Hl.subs(lam, 0)).applyfunc(sp.expand)
        lin = (Hl.subs(lam, 1) - Hl.subs(lam, 0)).applyfunc(sp.expand)
        report(f"{node}-scaling-{label}", d2 == sp.zeros(*H.shape) and lin != sp.zeros(*H.shape),
               "second lambda-difference of H(lambda phi0) vanishes, first does not")
        if not tower and order == 3:
            Sb = mod.action(order, quartic_break=True)
            Hb = mod.hessian(Sb)
            degb = max(sp.Poly(e, *mod.fields).total_degree() if e != 0 else 0 for e in Hb)
            report("C1.2-break-quartic-term", degb == 2,
                   f"a quartic monomial in the action gives Hessian degree {degb}")
            Sc = mod.action(order, coef_break=True)
            Hc = mod.hessian(Sc).subs(sub).applyfunc(sp.expand)
            report("C1.2-break-coefficient", Hc != Hh,
                   "g^3/48 in place of g^3/60 fails the block comparison")


# ------------------------------------------------------------------ Part 2: inertia, zero modes
def part2() -> None:
    print("\n=== Part 2: congruence, inertia and zero modes at engineered critical points ===")
    gval = sp.Rational(1, 2)
    for tower, label in ((False, "S3"), (True, "tower")):
        # n = 3 for S3 (dim 9); n = 2 for the tower (dim 9): n = 3 there (dim 19) is too slow
        mod = Model(SEED + (3 if tower else 2), n=2 if tower else 3, tower=tower)
        order = 4 if tower else 3
        S0 = mod.action(order, with_V2=False)
        x0 = [sp.Rational(1, 2), sp.Rational(-1, 3), sp.Rational(3, 4)][:mod.n]
        b, N, s0, sig1 = eff_expansion(mod, S0, x0, gval)
        xk = kernel_direction(x0, b, N)
        V2 = engineer_V2(mod, x0, b, N, xk)
        set_V2(mod, V2)
        S = mod.action(order).subs(g, gval)
        pt = dict(zip(mod.fields, x0 + list(s0)))
        grad = sp.Matrix([sp.diff(S, f) for f in mod.fields]).subs(pt).applyfunc(sp.expand)
        report(f"C2.1-critical-point-{label}", grad == sp.zeros(len(mod.fields), 1),
               f"joint gradient vanishes exactly at the engineered point (dim {len(mod.fields)})")
        H = mod.hessian(S).subs(pt).applyfunc(sp.expand)
        n = mod.n
        Heff = V2 + N  # Hess V_eff from the epsilon-expansion (independent of Schur)
        Hxx, Hax, Haa = H[:n, :n], H[n:, :n], H[n:, n:]
        schur = (Hxx - Hax.T * Haa.inv() * Hax).applyfunc(sp.expand)
        report(f"C2.4-schur-equals-HessVeff-{label}", schur == Heff,
               "Schur complement of the joint Hessian == Hess V_eff (epsilon-expansion), exact")
        InH, InE, InA = inertia(H), inertia(Heff), inertia(Haa)
        ok = InH == tuple(a + c for a, c in zip(InE, InA))
        report(f"C2.1-inertia-{label}", ok, f"In(H)={InH} = In(HessVeff){InE} + In(Haux){InA}")
        # break leg: the mean-field Psi block in place of Hess V_eff (the naive reading)
        InP = inertia(Hxx)
        broken = InH != tuple(a + c for a, c in zip(InP, InA))
        report(f"C2.1-inertia-break-psi-block-{label}", broken,
               f"In(H_PsiPsi)={InP} + In(Haux) != In(H): the Psi block alone miscounts")
        InAm = inertia(-Haa)
        if InAm != InA:
            report(f"C2.1-inertia-break-sign-{label}",
                   InH != tuple(a + c for a, c in zip(InE, InAm)),
                   f"with the sign of H_aux flipped, In(Haux)->{InAm}: sum != In(H)")
        else:
            print(f"[INFO] C2.1-inertia-break-sign-{label}: vacuous for this seed, In(Haux) balanced {InA}")
        # never-vacuous break leg (critic #12): Heff + delta*1 lifts the zero eigenvalue with
        # delta small enough to keep the signs of the nonzero ones, so the sum has no zero
        # while In(H) has one; fails for every seed, independently of In(Haux).
        Hpert = Heff + sp.Rational(1, 10**12) * sp.eye(n)
        InPert = inertia(Hpert)
        report(f"C2.1-inertia-break-shift-{label}",
               InPert[2] == 0 and InH != tuple(a + c for a, c in zip(InPert, InA)),
               f"In(Heff+delta 1)={InPert} (no zero): sum with In(Haux) != In(H)={InH}")
        # zero modes
        kx = sp.Matrix(xk)
        report(f"C2.2-kernel-Heff-{label}", (Heff * kx == sp.zeros(n, 1)) and Heff.rank() == n - 1,
               "Hess V_eff has the engineered one-dimensional kernel")
        v = sp.Matrix(list(kx) + list(sig1 * kx))
        report(f"C2.2-zero-mode-{label}", (H * v == sp.zeros(H.shape[0], 1)) and H.rank() == H.shape[0] - 1,
               "(x, Sigma_*' x) with Sigma_*' from the epsilon-expansion spans ker H; dim ker H = 1")
        v0 = sp.Matrix(list(kx) + [0] * (H.shape[0] - n))
        report(f"C2.2-zero-mode-break-{label}", H * v0 != sp.zeros(H.shape[0], 1),
               "(x, 0) is not a zero mode of H")
        # pencil: congruent, not isospectral
        rng = np.random.default_rng(SEED + 7)
        w1 = sp.diag(*[sp.Rational(int(rng.integers(1, 4)) * (1 if k % 2 else -1)) for k in range(n)])
        w1d = {(i, j): w1[i, j] for i in range(n) for j in range(n)}
        def wk(E):
            m = len(E)
            return sp.Matrix(m, m, lambda P, Q: sum(
                E[P].get(p, 0) * E[Q].get(q, 0) * sp.prod([w1d[(pi, qi)] for pi, qi in zip(p, q)])
                for p in E[P] for q in E[Q]))
        Gblocks = [w1, wk(mod.E2)] + ([wk(mod.E3)] if tower else [])
        G = sp.diag(*Gblocks)
        Gaux = sp.diag(*Gblocks[1:])
        def eigs(M):
            A = np.array(sp.Matrix(M).evalf(20).tolist(), dtype=float)
            return sorted(np.linalg.eigvals(A), key=lambda e: (e.real, e.imag))
        ev_joint = eigs(G.inv() * H)
        Dsum = sp.diag(Heff, Haa)
        Gd = sp.diag(w1, Gaux)
        ev_sum = eigs(Gd.inv() * Dsum)
        diff = max(abs(a - c) for a, c in zip(ev_joint, ev_sum))
        scale = max(abs(e) for e in ev_joint)
        nz_joint = sum(1 for e in ev_joint if abs(e) < 1e-9 * scale)
        nz_sum = sum(1 for e in ev_sum if abs(e) < 1e-9 * scale)
        report(f"C2.3-not-isospectral-{label}", diff > 1e-6 and nz_joint == nz_sum == 1,
               f"max |eig(G^-1 H) - eig(direct sum)| = {diff:.3e} (nonzero); both have one zero eigenvalue")


# ------------------------------------------------------------------ Part 3: fold
def part3() -> None:
    print("\n=== Part 3: the fold of the one-field S4 model (exact algebraic) ===")
    t, s = sp.symbols("t sigma", real=True)
    # a W > 0 is needed for a real fold (Sigma-EOM = 0 = H_ss gives sigma^2 = 20 a t^2 / W);
    # 20 a / W = 16 makes the fold points rational.
    v2, v3, a, w, W = sp.Rational(2, 3), sp.Rational(-1, 2), sp.Integer(1), sp.Rational(5, 3), sp.Rational(5, 4)
    gv = sp.Integer(1)
    S = (v2 / 2 * t**2 + gv * v3 / 6 * t**3 - gv**2 / 24 * a * s**2 + gv**2 / 12 * a * s * t**2
         + gv**3 / 120 * w * s**2 * t + gv**4 / 720 * W * s**3)
    Es = sp.diff(S, s)
    Hss = sp.diff(S, s, s)
    Hts = sp.diff(S, t, s)
    Htt = sp.diff(S, t, t)
    fold = sp.solve([Es, Hss], [t, s], dict=True)
    fold = [f for f in fold if all(sp.im(sp.N(f[k], 30)) == 0 for k in (t, s))]
    ok_all = True
    for f in fold:
        Hf = sp.Matrix([[Htt, Hts], [Hts, Hss]]).subs(f).applyfunc(sp.simplify)
        detH = sp.simplify(Hf.det())
        Hts_f = sp.simplify(Hts.subs(f))
        ok_all &= sp.simplify(detH + Hts_f**2) == 0 and Hts_f != 0 and sp.N(detH) < 0
    report("C3-fold-regular", bool(ok_all) and len(fold) >= 1,
           f"{len(fold)} real fold point(s): det H = -H_ts^2 < 0 exactly, inertia (1,1), H_ss = 0")
    # V_eff'' on the sheet diverges as delta^{-1/2}
    f = fold[0]
    tf = f[t]
    sheets = sp.solve(Es, s)  # two sheets sigma_pm(t)
    Veff = [sp.expand(S.subs(s, sh)) for sh in sheets]
    growth_ok = False
    for Ve in Veff:
        V2e = sp.diff(Ve, t, 2)
        vals = []
        for k in (1, 2, 3):
            d = sp.Rational(1, 10**(2 * k))
            # approach from the side where the sheet is real
            for sgn in (1, -1):
                val = sp.N(V2e.subs(t, tf + sgn * d), 30)
                if sp.im(val) == 0:
                    vals.append(abs(val))
                    break
        if len(vals) == 3:
            r1, r2 = vals[1] / vals[0], vals[2] / vals[1]
            growth_ok = growth_ok or (abs(r1 - 10) < 1 and abs(r2 - 10) < 0.5)
            print(f"      |V_eff''| at delta=1e-2,1e-4,1e-6: {[float(v) for v in vals]}, ratios {float(r1):.3f}, {float(r2):.3f}")
    report("C3-fold-Veff-diverges", growth_ok,
           "|V_eff''| on the sheet grows by ~10 per factor 100 in delta (exponent -1/2)")


if __name__ == "__main__":
    print(f"seed {SEED}")
    part1()
    part2()
    part3()
    print(f"\n{npass} PASS / {len(failures)} FAIL")
    if failures:
        print("failed:", failures)
        sys.exit(1)
