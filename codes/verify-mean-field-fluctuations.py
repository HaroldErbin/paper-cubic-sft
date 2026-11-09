"""Verify record 060 (mean field I): Schur identity, BRST deformation, degenerate branch.

Record: ``agent/derivations/060-mean-field-fluctuations.md``. Check labels = claim-tree nodes.

Part 1 (C1, exact rational arithmetic, sympy). Generic random rational symmetric tensors
V2..V6. Cubic actions (R1, R17, R19):
    S2 = A - g^2/4! V4(Sig,Sig) + 2 g^2/4! V4(Sig,P),  A = V2(x^2)/2 + g/3! V3(x^3),
    S3 = S2 + g^3/5! V5(Sig,Sig,x),   S4 = S3 + g^4/6! W6(Sig^3),  W6 = V6 - 6/5 C,
with C(Sig^3) = Sig^{kl} V5(Sig,E_M,e_k) Ainv^{MN} V5(Sig,E_N,e_l) (full V4^{-1} on Sym^2 H,
or A^{-1} = (V4|_S)^{-1} for the S-consistent vertex of 057 C3.6).
The block Hessian is taken from sympy (independent of the hand formulas (1.2)-(1.4), which
are checked against it), the saddle Sigma_*(x0) is built by series Newton on the sympy
gradient, and the Schur complement over Sigma is compared, Taylor coefficient by Taylor
coefficient in g (exact rationals), with the Hessian of the target
S_eff^(n) = A + sum_{k>=4} g^{k-2}/k! Vk(x^k).
Off-saddle formula (exact at rational g).

Part 2 (C2, float). The finite cyclic L-infinity model of record 058 Part B (matrix
Chern-Simons DGLA A (x) End(W), tree-level transfer to a retract; builder and symplectic
Hodge decomposition imported from ``codes/verify-bv-master-equation.py``). 058's literal
model (A = span(1, eps)) has l3(psi, psi, .) = 0 on the classical field sector (check
C2.0-058), so the checks use the same construction with A = Lambda[th1, th2, th3],
W in degrees (0,0,0,1,1) with a rank-one D, massive fields integrated out (cut (1,)).
The shifted operator of the transferred theory is
    T_psi = p (Q + g ad_Phi)(1 + g h'' ad_Phi)^{-1} iota,  Phi = iota psi - g h''(Phi Phi)
(homological perturbation lemma), on all degrees. Checks: T_psi on fields = Hessian of the
transferred action; nilpotency at a Maurer-Cartan point (break: off shell, and l3 -> 0);
the g^2 coefficient T2 and its polarisation to Sym^2 H^1; R1's factor 1/3; the linear map
Delta -> {T0, T2(Delta)} (nilpotency defect of the Sigma-deformed operator).

Part 3 (C3, mpmath 40 digits). Five-field model (dim U = 2, S = Sym^2 U), generic rational
tensors, scaled variables (g = 1). Base points of the rational map Sigma_* (det K = 0 and
n.u = 0) via a resultant; the Sigma-EOM line, flatness of S3 along it, the Psi-EOM on it,
a tuned coupling giving a joint critical point, its continuation off the wall, the
blow-up limit, and the break legs (moving off either condition).

Not verified: the string-vertex statements (finite model only); Zwiebach's (4.117) is
cited, not re-derived; Part 2's model is not the random-tensor model (which is not
L-infinity).
"""

from __future__ import annotations

import importlib.util
import itertools
import sys
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp

failures: list[str] = []
npass = 0


def report(name: str, ok: bool, detail: str = "") -> None:
    """Print a labelled PASS/FAIL line and record failures."""
    global npass
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")
    if ok:
        npass += 1
    else:
        failures.append(name)


# =====================================================================================
# Part 1: exact Schur identity
# =====================================================================================
g = sp.Symbol("g")
ORD = 4  # Taylor order in g compared


def rand_sym(rng: np.random.Generator, n: int, k: int, lo: int = -5, hi: int = 6,
             den: int = 3) -> dict:
    """Random totally symmetric rational tensor, stored as dict index-tuple -> Rational."""
    T = {}
    for c in itertools.combinations_with_replacement(range(n), k):
        val = sp.Rational(int(rng.integers(lo, hi)), den)
        for p in set(itertools.permutations(c)):
            T[p] = val
    return T


def contract(T: dict, vecs: list) -> sp.Expr:
    """T(v1,...,vk) for vectors given as lists of sympy expressions."""
    tot = 0
    for idx, val in T.items():
        if val == 0:
            continue
        term = val
        for v, i in zip(vecs, idx):
            if v[i] == 0:
                term = 0
                break
            term = term * v[i]
        tot += term
    return sp.expand(tot)


def contract_mats(T: dict, mats: list, vecs: list) -> sp.Expr:
    """T(M1, ..., v...) with symmetric-matrix arguments (two legs each) then vectors."""
    tot = 0
    for idx, val in T.items():
        if val == 0:
            continue
        term = val
        pos = 0
        for M in mats:
            term = term * M[idx[pos]][idx[pos + 1]]
            pos += 2
            if term == 0:
                break
        if term == 0:
            continue
        for v in vecs:
            term = term * v[idx[pos]]
            pos += 1
        tot += term
    return sp.expand(tot)


class Model:
    """Finite model: H = R^N, U = first nU coordinates, S = Sym^2 U (pair coordinates)."""

    def __init__(self, seed: int, N: int, nU: int):
        rng = np.random.default_rng(seed)
        self.N, self.nU = N, nU
        self.V = {k: rand_sym(rng, N, k) for k in range(2, 7)}
        # make V4 on Sym^2 H comfortably invertible: add a symmetric "diagonal" piece
        self.pairsH = [(a, b) for a in range(N) for b in range(a, N)]
        self.pairsS = [(a, b) for a in range(nU) for b in range(a, nU)]
        self.x0 = [sp.Rational(int(rng.integers(-4, 5)) or 1, 2) for _ in range(nU)]

    @staticmethod
    def E(pair, N):
        a, b = pair
        M = [[0] * N for _ in range(N)]
        M[a][b] = 1
        M[b][a] = 1
        return M

    def V4mat(self, pairs):
        N = self.N
        Es = [self.E(p, N) for p in pairs]
        return sp.Matrix(len(pairs), len(pairs),
                         lambda i, j: contract_mats(self.V[4], [Es[i], Es[j]], []))

    def C_diag(self, Sig, pairs_inv):
        """C(Sig,Sig,Sig) with the inverse of V4 on span(pairs_inv)."""
        N = self.N
        Es = [self.E(p, N) for p in pairs_inv]
        Ainv = self.V4mat(pairs_inv).inv()
        e = [[1 if i == k else 0 for i in range(N)] for k in range(N)]
        vec = [[contract_mats(self.V[5], [Sig, Es[M]], [e[k]]) for M in range(len(Es))]
               for k in range(N)]
        tot = 0
        for k in range(N):
            for l in range(N):
                if Sig[k][l] == 0:
                    continue
                vk = sp.Matrix(vec[k])
                vl = sp.Matrix(vec[l])
                tot += Sig[k][l] * (vk.T * Ainv * vl)[0, 0]
        return sp.expand(tot)

    def build(self, order: int, w6: str = "S"):
        """Symbols and the cubic action S_order; w6 in {'S','full'}."""
        N, nU = self.N, self.nU
        xs = sp.symbols(f"x0:{nU}")
        ss = sp.symbols(f"s0:{len(self.pairsS)}")
        psi = list(xs) + [0] * (N - nU)
        Sig = [[0] * N for _ in range(N)]
        for s, (a, b) in zip(ss, self.pairsS):
            Sig[a][b] = s
            Sig[b][a] = s
        P = [[psi[a] * psi[b] for b in range(N)] for a in range(N)]
        A = sp.Rational(1, 2) * contract(self.V[2], [psi] * 2) + g / 6 * contract(
            self.V[3], [psi] * 3)
        S = (A - g**2 / 24 * contract_mats(self.V[4], [Sig, Sig], [])
             + g**2 / 12 * contract_mats(self.V[4], [Sig, P], []))
        if order >= 3:
            S += g**3 / 120 * contract_mats(self.V[5], [Sig, Sig], [psi])
        if order >= 4:
            pinv = self.pairsS if w6 == "S" else self.pairsH
            W6 = contract_mats(self.V[6], [Sig, Sig, Sig], []) - sp.Rational(6, 5) * \
                self.C_diag(Sig, pinv)
            S += g**4 / 720 * W6
        Seff = A + sum(g ** (k - 2) / sp.factorial(k) * contract(self.V[k], [psi] * k)
                       for k in range(4, order + 3))
        return xs, ss, sp.expand(S), sp.expand(Seff), psi, Sig


def trunc(e, k: int):
    """Truncate a polynomial in g at order g^k."""
    e = sp.expand(e)
    return sum(e.coeff(g, j) * g**j for j in range(k + 1))


def mtrunc(M: sp.Matrix, k: int) -> sp.Matrix:
    return M.applyfunc(lambda e: trunc(e, k))


def series_inv(M: sp.Matrix, k: int) -> sp.Matrix:
    """Inverse of a matrix polynomial in g as a series through g^k."""
    Ms = [M.applyfunc(lambda e: sp.expand(e).coeff(g, j)) for j in range(k + 1)]
    X0 = Ms[0].inv()
    Xs = [X0]
    for j in range(1, k + 1):
        acc = sp.zeros(*M.shape)
        for i in range(1, j + 1):
            acc += Ms[i] * Xs[j - i]
        Xs.append(-X0 * acc)
    return sum((Xs[j] * g**j for j in range(k + 1)), sp.zeros(*M.shape))


def saddle_series(xs, ss, S, x0, k: int):
    """Sigma_*(x0) as a polynomial in g through g^k: series Newton on the sympy gradient."""
    grad = sp.Matrix([sp.diff(S, s) for s in ss]).subs(dict(zip(xs, x0)))
    H0 = sp.Matrix([[sp.diff(S, a, b) for b in ss] for a in ss]).subs(
        dict(zip(xs, x0))).applyfunc(lambda e: sp.expand(e).coeff(g, 2))  # -A/12
    H0inv = H0.inv()
    sig = sp.zeros(len(ss), 1)
    for _ in range(k + 2):
        r = grad.subs(dict(zip(ss, list(sig)))).applyfunc(sp.expand)
        r = (r / g**2).applyfunc(sp.expand)  # every Sigma-term carries >= g^2
        sig = mtrunc(sig - H0inv * r, k)
    return sig, grad


def blocks(xs, ss, S, x0, sig):
    """Hessian blocks of S at (x0, sig) (sig polynomial in g)."""
    sub = dict(zip(xs, x0))
    sub.update(dict(zip(ss, list(sig))))
    Hxx = sp.Matrix([[sp.diff(S, a, b) for b in xs] for a in xs]).subs(sub)
    Hsx = sp.Matrix([[sp.diff(S, a, b) for b in xs] for a in ss]).subs(sub)
    Hss = sp.Matrix([[sp.diff(S, a, b) for b in ss] for a in ss]).subs(sub)
    return Hxx.applyfunc(sp.expand), Hsx.applyfunc(sp.expand), Hss.applyfunc(sp.expand)


def schur_series(Hxx, Hsx, Hss, k: int, kappa_shift: sp.Matrix | None = None):
    """Schur complement H_xx + (12/g^2) Hsx^T Kappa^{-1} Hsx through g^k, Kappa=-12Hss/g^2."""
    Kap = (-12 * Hss / g**2).applyfunc(sp.expand)
    if kappa_shift is not None:
        Kap = Kap + kappa_shift
    Kinv = series_inv(Kap, k)
    B = (Hsx / g**2).applyfunc(sp.expand)  # O(1)
    corr = mtrunc(12 * g**2 * B.T * Kinv * B, k)
    return mtrunc(Hxx + corr, k)


def coeffs(M: sp.Matrix, j: int) -> sp.Matrix:
    return M.applyfunc(lambda e: sp.expand(e).coeff(g, j))


def hess_at(f, xs, x0):
    return sp.Matrix([[sp.diff(f, a, b) for b in xs] for a in xs]).subs(
        dict(zip(xs, x0))).applyfunc(sp.expand)


def part1() -> None:
    print("\n=== Part 1: Schur identity (exact rationals) ===")
    # --- untruncated: H = U = R^2, S = Sym^2 H ---
    mod = Model(seed=601, N=2, nU=2)
    print(f"untruncated model: N=2, seed 601, x0={mod.x0}")
    A4 = mod.V4mat(mod.pairsS)
    print(f"  det V4|Sym2 = {A4.det()}")
    for order in (2, 3, 4):
        xs, ss, S, Seff, psi, Sig = mod.build(order)
        sig, grad = saddle_series(xs, ss, S, mod.x0, ORD + 1)
        res = grad.subs(dict(zip(ss, list(sig)))).applyfunc(sp.expand)
        low = max(abs(res[i].coeff(g, j)) for i in range(len(ss)) for j in range(ORD + 4))
        report(f"C1.1-saddle S{order}", low == 0 or all(
            res[i].coeff(g, j) == 0 for i in range(len(ss)) for j in range(ORD + 3)),
            "Sigma-EOM residual vanishes through g^(ORD+2)")
        Hxx, Hsx, Hss = blocks(xs, ss, S, mod.x0, sig)
        Ht = hess_at(Seff, xs, mod.x0)
        Hs = schur_series(Hxx, Hsx, Hss, ORD)
        diffs = [coeffs(Hs - Ht, j) for j in range(ORD + 1)]
        if order == 2:
            ok = all(d == sp.zeros(2, 2) for d in diffs)
            report("C1.2 S2", ok, "Schur == Hess S_eff^(4), coefficients g^0..g^4 all equal")
            # channel split: Psi-block Sigma_0-term = 1/3, delta-Sigma exchange = 2/3 of g^2/2 V4(P0)
            N = mod.N
            e = [[1 if i == k else 0 for i in range(N)] for k in range(N)]
            V4P = sp.Matrix(N, N, lambda i, j: contract(mod.V[4], [mod.x0, mod.x0, e[i], e[j]]))
            blockpart = coeffs(Hxx, 2)
            exch = coeffs(Hs - Hxx, 2)
            okc = (blockpart - V4P / 6 == sp.zeros(N, N)) and (exch - V4P / 3 == sp.zeros(N, N))
            report("C2.1-channels", okc and V4P != sp.zeros(N, N),
                   "S2 at the saddle: Psi-block g^2-term = V4(P0)/6, Schur term = V4(P0)/3")
            report("C2.1-channels-break", blockpart - V4P / 2 != sp.zeros(N, N),
                   "the Psi-block alone is not the l3 part V4(P0)/2 of Q_Psi0")
        elif order == 3:
            ok = all(diffs[j] == sp.zeros(2, 2) for j in range(4))
            # predicted g^4: (1/600) Hess (v V4^-1 v)
            N = mod.N
            Es = [mod.E(p, N) for p in mod.pairsS]
            P = [[psi[a] * psi[b] for b in range(N)] for a in range(N)]
            v = sp.Matrix([contract_mats(mod.V[5], [Es[M], P], [psi])
                           for M in range(len(Es))])
            f = sp.expand((v.T * A4.inv() * v)[0, 0])
            pred = hess_at(f, xs, mod.x0) / 600
            report("C1.3 S3", ok and diffs[4] == pred and pred != sp.zeros(2, 2),
                   f"g^0..g^3 equal; [g^4] = Hess(v V4^-1 v)/600 = {list(pred)}")
            # channel split of the l4 part at g^3: Psi-block (via the O(g) shift of Sigma_*) 1/5,
            # delta-Sigma exchange 4/5 of (g^3/6) V5(x0^3, ., .)
            e_ = [[1 if i == k else 0 for i in range(N)] for k in range(N)]
            V5P = sp.Matrix(N, N, lambda i, j: contract(mod.V[5], [mod.x0] * 3 + [e_[i], e_[j]]))
            b3 = coeffs(Hxx, 3)
            x3 = coeffs(Hs - Hxx, 3)
            report("C2.1-channels-g3", b3 == V5P / 30 and x3 == 2 * V5P / 15 and V5P != sp.zeros(N, N),
                   "S3: g^3 Psi-block term = V5(x0^3)/30 (1/5 of l4 part), exchange = 2V5/15 (4/5)")
            # break leg: wrong g/5 -> g/4 in K (Kappa -> Kappa - g/20 V5(x0))
            W = sp.Matrix(len(Es), len(Es), lambda i, j: contract_mats(
                mod.V[5], [Es[i], Es[j]], [mod.x0]))
            Hb = schur_series(Hxx, Hsx, Hss, ORD, kappa_shift=-g / 20 * W)
            bad = coeffs(Hb - Ht, 3)
            report("C1.3-break g/4", bad != sp.zeros(2, 2),
                   f"wrong dressing fails at g^3: {list(bad)}")
            # hand block formulas (1.2)-(1.4) against the sympy blocks
            J = lambda xv: [[sp.Rational(1, 2) * (mod.x0[a] * xv[b] + xv[a] * mod.x0[b])  # noqa: E731
                             for b in range(N)] for a in range(N)]
            e = [[1 if i == k else 0 for i in range(N)] for k in range(N)]
            sigm = [[0] * N for _ in range(N)]
            for s_, (a, b) in zip(list(sig), mod.pairsS):
                sigm[a][b] = s_
                sigm[b][a] = s_
            Hxx_h = sp.Matrix(N, N, lambda i, j: mod.V[2][(i, j)]
                              + g * contract(mod.V[3], [mod.x0, e[i], e[j]])
                              + g**2 / 6 * contract_mats(mod.V[4], [sigm], [e[i], e[j]]))
            Hsx_h = sp.Matrix(len(Es), N, lambda M, i: g**2 / 6 * contract_mats(
                mod.V[4], [Es[M], J(e[i])], []) + g**3 / 60 * contract_mats(
                mod.V[5], [Es[M], sigm], [e[i]]))
            Hss_h = -g**2 / 12 * (A4 - g / 5 * W)
            okb = ((Hxx_h - Hxx).applyfunc(sp.expand) == sp.zeros(N, N)
                   and (Hsx_h - Hsx).applyfunc(sp.expand) == sp.zeros(len(Es), N)
                   and (Hss_h - Hss).applyfunc(sp.expand) == sp.zeros(len(Es), len(Es)))
            report("C1.1-blocks", okb, "(1.2)-(1.4) == sympy Hessian blocks of S3")
            Hxx_b = Hxx_h.subs(g, g) + g**2 / 12 * contract_mats(mod.V[4], [sigm], [e[0], e[0]]) * sp.Matrix([[1, 0], [0, 0]])
            report("C1.1-blocks-break", (Hxx_b - Hxx).applyfunc(sp.expand) != sp.zeros(N, N),
                   "a wrong Sigma_0 coefficient in (1.2) is detected")
        else:
            ok = all(d == sp.zeros(2, 2) for d in diffs)
            report("C1.4 S4 untruncated", ok, "Schur == Hess S_eff^(6) through g^4")
    # --- truncated: H = R^3, U = R^2, S = Sym^2 U ---
    mod = Model(seed=602, N=3, nU=2)
    print(f"truncated model: N=3, U=R^2, seed 602, x0={mod.x0}")
    AS = mod.V4mat(mod.pairsS)
    AH = mod.V4mat(mod.pairsH)
    print(f"  det A_S = {AS.det()}, det V4|Sym2H = {AH.det()}")
    res4 = {}
    for w6 in ("S", "full"):
        xs, ss, S, Seff, psi, Sig = mod.build(4, w6)
        sig, grad = saddle_series(xs, ss, S, mod.x0, ORD + 1)
        Hxx, Hsx, Hss = blocks(xs, ss, S, mod.x0, sig)
        Ht = hess_at(Seff, xs, mod.x0)
        Hs = schur_series(Hxx, Hsx, Hss, ORD)
        res4[w6] = [coeffs(Hs - Ht, j) for j in range(ORD + 1)]
        if w6 == "S":
            N = mod.N
            psiH = psi
            P = [[psiH[a] * psiH[b] for b in range(N)] for a in range(N)]
            EsH = [mod.E(p, N) for p in mod.pairsH]
            EsS = [mod.E(p, N) for p in mod.pairsS]
            vH = sp.Matrix([contract_mats(mod.V[5], [E_, P], [psiH]) for E_ in EsH])
            vS = sp.Matrix([contract_mats(mod.V[5], [E_, P], [psiH]) for E_ in EsS])
            fdev = sp.expand((vS.T * AS.inv() * vS)[0, 0] - (vH.T * AH.inv() * vH)[0, 0])
            pred = hess_at(fdev, xs, mod.x0) / 600
    okS = all(d == sp.zeros(2, 2) for d in res4["S"])
    report("C1.5 S4 truncated, W6^(S)", okS, "Schur == Hess S_eff^(6)|_U through g^4")
    okF = all(res4["full"][j] == sp.zeros(2, 2) for j in range(4)) and \
        res4["full"][4] == pred and pred != sp.zeros(2, 2)
    report("C1.5-break full-C", okF,
           f"full-C vertex in a truncation: [g^4] = Hess(-w M^-1 w)/600 = {list(pred)} != 0")


def part1_offshell() -> None:
    print("\n=== Part 1b: off the saddle (exact, rational g) ===")
    mod = Model(seed=603, N=2, nU=2)
    gv = sp.Rational(1, 3)
    rng = np.random.default_rng(6031)
    for order in (2, 3):
        xs, ss, S, Seff, psi, Sig = mod.build(order)
        Sg = S.subs(g, gv)
        grad = sp.Matrix([sp.diff(Sg, s) for s in ss])
        sol = sp.solve(list(grad), list(ss), dict=True)[0]  # linear in Sigma
        sigstar = sp.Matrix([sp.together(sol[s]) for s in ss])  # rational in x
        Veff = Sg.subs(sol)
        HV = hess_at(Veff, xs, mod.x0)
        sig0 = sigstar.subs(dict(zip(xs, mod.x0)))
        Delta = sp.Matrix([sp.Rational(int(rng.integers(-5, 6)), 4) for _ in ss])
        sub = dict(zip(xs, mod.x0))
        sub.update(dict(zip(ss, list(sig0 + Delta))))
        Hxx = sp.Matrix([[sp.diff(Sg, a, b) for b in xs] for a in xs]).subs(sub)
        Hsx = sp.Matrix([[sp.diff(Sg, a, b) for b in xs] for a in ss]).subs(sub)
        Hss = sp.Matrix([[sp.diff(Sg, a, b) for b in ss] for a in ss]).subs(sub)
        Heff = Hxx - Hsx.T * Hss.inv() * Hsx
        # predicted difference
        Hss_x = sp.Matrix([[sp.diff(Sg, a, b) for b in ss] for a in ss])  # function of x
        d2sig = [[sigstar.applyfunc(lambda e: sp.diff(e, a, b)).subs(
            dict(zip(xs, mod.x0))) for b in xs] for a in xs]
        Hs0 = Hss_x.subs(sub)
        term1 = sp.Matrix(len(xs), len(xs), lambda i, j: -(Delta.T * Hs0 * d2sig[i][j])[0, 0])
        Bp = sp.Matrix(len(ss), len(xs), lambda M, i: sum(
            sp.diff(Hss_x[M, Nn], xs[i]).subs(sub) * Delta[Nn] for Nn in range(len(ss))))
        term2 = -Bp.T * Hs0.inv() * Bp
        diff = (Heff - HV - term1 - term2).applyfunc(sp.simplify)
        dev = (Heff - HV).applyfunc(sp.simplify)
        report(f"C1.6 S{order} off-saddle", diff == sp.zeros(2, 2) and dev != sp.zeros(2, 2),
               f"H_eff - Hess V_eff = -<H Delta, Sigma_*''> - (H'Delta)^T H^-1 (H'Delta) "
               f"exactly; deviation {[float(e) for e in dev]}")
        if order == 2:
            # S2: deviation = (g^2/6) V4(Delta, x, x)
            N = mod.N
            Dm = [[0] * N for _ in range(N)]
            for dv, (a, b) in zip(list(Delta), mod.pairsS):
                Dm[a][b] = dv
                Dm[b][a] = dv
            e = [[1 if i == k else 0 for i in range(N)] for k in range(N)]
            pred = sp.Matrix(N, N, lambda i, j: gv**2 / 6 * contract_mats(
                mod.V[4], [Dm], [e[i], e[j]]))
            report("C1.6-S2 closed form", (dev - pred).applyfunc(sp.simplify) == sp.zeros(2, 2),
                   "S2: H_eff - Hess S_eff^(4) = (g^2/6) V4(Sigma_0 - P_0, ., .)")
            report("C1.6-break", (dev - 2 * pred).applyfunc(sp.simplify) != sp.zeros(2, 2),
                   "factor 2 on the S2 closed form is detected")

# =====================================================================================
# Part 2: the L-infinity model of record 058 Part B
# =====================================================================================
def load_058():
    """Import record 058's model builder (build_parent, hodge, run_model)."""
    path = Path(__file__).with_name("verify-bv-master-equation.py")
    spec = importlib.util.spec_from_file_location("bv058", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def random_differential(wdeg: list[int], rng: np.random.Generator) -> np.ndarray:
    """Random degree +1 differential on W with D^2 = 0 (same recipe as 058's build_parent)."""
    m = len(wdeg)
    for _ in range(1000):
        D = np.zeros((m, m))
        for i in range(m):
            for j in range(m):
                if wdeg[i] == wdeg[j] + 1:
                    D[i, j] = rng.standard_normal()
        for d in sorted(set(wdeg)):
            rows = [i for i in range(m) if wdeg[i] == d + 1]
            cols = [j for j in range(m) if wdeg[j] == d]
            prev = [j for j in range(m) if wdeg[j] == d - 1]
            if rows and cols and prev:
                Dprev = D[np.ix_(cols, prev)]
                Pk = np.eye(len(cols)) - Dprev @ np.linalg.pinv(Dprev)
                D[np.ix_(rows, cols)] = D[np.ix_(rows, cols)] @ Pk
        if np.allclose(D @ D, 0):
            return D
    raise ValueError("no differential")


def rank1_differential(wdeg: list[int], rng: np.random.Generator, scale: float = 1.0,
                       base: tuple | None = None):
    """Rank-one degree +1 differential u v^T from degree 0 to degree 1 (two-step W)."""
    m = len(wdeg)
    rows = [i for i in range(m) if wdeg[i] == 1]
    cols = [j for j in range(m) if wdeg[j] == 0]
    if base is None:
        uu, vv = rng.standard_normal(len(rows)), rng.standard_normal(len(cols))
    else:
        uu = base[0] + scale * rng.standard_normal(len(rows))
        vv = base[1] + scale * rng.standard_normal(len(cols))
    D = np.zeros((m, m))
    D[np.ix_(rows, cols)] = np.outer(uu, vv)
    return D, (uu, vv)


def build_parent_T3(wdeg: list[int], rng: np.random.Generator):
    """Parent cyclic DGLA Lambda[th1,th2,th3] (x) End(W): constant-field matrix CS on T^3.

    Same construction as 058's build_parent with A = H*(S^3) = span(1, eps) replaced by
    A = Lambda[th1, th2, th3] (int th1 th2 th3 = 1); supertrace pairing, Q = [1 (x) D, .].
    """
    m = len(wdeg)
    subsets = [(), (0,), (1,), (2,), (0, 1), (0, 2), (1, 2), (0, 1, 2)]

    def mulA(I, J):
        if set(I) & set(J):
            return 0, None
        seq = list(I + J)
        sign = 1
        for a in range(len(seq)):  # bubble sort parity
            for b in range(len(seq) - 1 - a):
                if seq[b] > seq[b + 1]:
                    seq[b], seq[b + 1] = seq[b + 1], seq[b]
                    sign = -sign
        return sign, tuple(seq)

    basis = [(I, i, j) for I in subsets for i in range(m) for j in range(m)]
    idx = {b: n for n, b in enumerate(basis)}
    deg = np.array([len(I) + wdeg[i] - wdeg[j] for (I, i, j) in basis])
    N = len(basis)
    prod = np.zeros((N, N, N))
    for s_, (I, i, j) in enumerate(basis):
        for t_, (J, k, l) in enumerate(basis):
            if j != k:
                continue
            sg, K = mulA(I, J)
            if not sg:
                continue
            sign = sg * (-1) ** (((wdeg[i] - wdeg[j]) * len(J)) % 2)
            prod[s_, t_, idx[(K, i, l)]] += sign
    tau = np.array([1.0 * (I == (0, 1, 2) and i == j) * (-1) ** wdeg[i] for (I, i, j) in basis])
    G = np.einsum("stu,u->st", prod, tau)
    D, uv = rank1_differential(wdeg, rng)

    def hat(Dm):
        v = np.zeros(N)
        for i in range(m):
            for j in range(m):
                if Dm[i, j]:
                    v[idx[((), i, j)]] = Dm[i, j]
        return v
    Dhat = hat(D)
    Q = np.einsum("s,stu->ut", Dhat, prod) - np.einsum("t,tsu,s->ut", (-1.0) ** deg, prod, Dhat)
    return basis, deg, prod, G, Q, D, tau, (hat, uv)


class LinfModel:
    """Transferred matrix Chern-Simons L-infinity model (058 Part B), c-number sector."""

    def __init__(self, seed: int, wdeg: list[int], cut: tuple[int, ...], parent: str = "S3"):
        bv = load_058()
        rng = np.random.default_rng(seed)
        self.parent = parent
        if parent == "S3":
            basis, deg, prod, G, Q, D = bv.build_parent(wdeg, rng)
            self.hat = None
        else:
            basis, deg, prod, G, Q, D, tau_, (self.hat, self.uv) = build_parent_T3(wdeg, rng)
        self.D = D
        dec = bv.hodge(deg, G, Q, rng)
        keep, Iint, Cint = [], [], []
        for d, (H, _I, _C) in dec.items():
            keep += [H[:, c] for c in range(H.shape[1])]
        for d, (_H, _I, C) in dec.items():
            for c in range(C.shape[1]):
                v = C[:, c]
                (Cint if d in cut else keep).append(v)
                (Iint if d in cut else keep).append(Q @ v)
        Nn = len(deg)
        B = np.column_stack(keep + Iint + Cint)
        Binv = np.linalg.inv(B)
        nk, ni = len(keep), len(Iint)
        PI = B[:, nk:nk + ni] @ Binv[nk:nk + ni]
        Cm = np.column_stack(Cint)
        self.hpp = Cm @ np.linalg.pinv(Q @ Cm) @ PI
        self.iota = np.column_stack(keep)
        self.p = Binv[:nk]
        self.kdeg = np.array([int(round(deg[np.argmax(np.abs(v))])) for v in keep])
        self.deg, self.prod, self.G, self.Q, self.nk = deg, prod, G, Q, nk
        if parent == "S3":
            self.tau = np.array([1.0 * (a == 1 and i == j) * (-1) ** wdeg[i]
                                 for (a, i, j) in basis])
            ref = bv.run_model(seed, wdeg, cut)  # same model as 058 (same rng stream)
            self.same_as_058 = np.allclose(ref["Kb"], self.iota) and np.allclose(
                ref["hpp"], self.hpp)
        else:
            self.tau = tau_
            self.same_as_058 = False
        self.f1 = np.where(self.kdeg == 1)[0]  # field coordinates (ghost number 2)
        self.f2 = np.where(self.kdeg == 2)[0]
        self.Nn = Nn

    def _nnz(self):
        if not hasattr(self, "_S"):
            S_, T_, U_ = np.nonzero(self.prod)
            self._S, self._T, self._U, self._Vv = S_, T_, U_, self.prod[S_, T_, U_]
            self._sgn = (-1.0) ** self.deg
        return self._S, self._T, self._U, self._Vv

    def mul(self, X, Y):
        S_, T_, U_, Vv = self._nnz()
        out = np.zeros(self.Nn)
        np.add.at(out, U_, X[S_] * Y[T_] * Vv)
        return out

    def ad(self, Phi):
        """Matrix of [Phi, .] (graded commutator), Phi of degree 1 (sparse product table)."""
        S_, T_, U_, Vv = self._nnz()
        M = np.zeros((self.Nn, self.Nn))
        np.add.at(M, (U_, T_), Phi[S_] * Vv)  # Phi e_t
        np.add.at(M, (U_, S_), -self._sgn[S_] * Phi[T_] * Vv)  # -(-1)^{deg t} e_t Phi
        return M

    def Phi(self, psi, gv):
        """Solve Phi = iota psi - g h''(Phi Phi) by Newton from iota psi (perturbative branch)."""
        base = self.iota @ psi
        Ph = base.copy()
        for _ in range(60):
            r = Ph - base + gv * self.hpp @ self.mul(Ph, Ph)
            if np.max(np.abs(r)) < 1e-15 * (1 + np.max(np.abs(Ph))):
                break
            Jm = np.eye(self.Nn) + gv * self.hpp @ self.ad(Ph)
            Ph = Ph - np.linalg.solve(Jm, r)
        return Ph

    def T(self, psi, gv, drop_h=False):
        """Shifted operator T_psi = p (Q + g ad)(1 + g h'' ad)^{-1} iota on all degrees."""
        Ph = self.Phi(psi, gv)
        adP = self.ad(Ph)
        if drop_h:
            return self.p @ (self.Q + gv * adP) @ self.iota
        M = np.linalg.solve(np.eye(self.Nn) + gv * self.hpp @ adP, self.iota)
        return self.p @ (self.Q + gv * adP) @ M

    def F(self, psi, gv):
        Ph = self.Phi(psi, gv)
        return self.p @ (self.Q @ Ph + gv * self.mul(Ph, Ph))

    def S(self, psi, gv):
        Ph = self.Phi(psi, gv)
        return self.tau @ (0.5 * self.mul(Ph, self.Q @ Ph) + gv / 3 * self.mul(Ph, self.mul(Ph, Ph)))

    def T0(self):
        return self.p @ self.Q @ self.iota

    def T1(self, psi):
        return self.p @ self.ad(self.iota @ psi) @ self.iota

    def T2(self, psi):
        ip = self.iota @ psi
        return -(self.p @ self.ad(self.hpp @ self.mul(ip, ip)) @ self.iota
                 + self.p @ self.ad(ip) @ self.hpp @ self.ad(ip) @ self.iota)

    def T2_sym(self, Sig):
        """Linear extension of T2 to Sym^2 H^1: Sig symmetric (d1 x d1) in field coordinates."""
        d1 = len(self.f1)
        if not hasattr(self, "_B"):
            self._B = {}
            E = np.zeros((d1, self.nk))
            E[np.arange(d1), self.f1] = 1
            diag = [self.T2(E[a]) for a in range(d1)]
            for a in range(d1):
                self._B[(a, a)] = diag[a]
                for b in range(a + 1, d1):
                    self._B[(a, b)] = 0.5 * (self.T2(E[a] + E[b]) - diag[a] - diag[b])
                    self._B[(b, a)] = self._B[(a, b)]
        out = np.zeros((self.nk, self.nk))
        for a in range(d1):
            for b in range(d1):
                if Sig[a, b] != 0:
                    out += Sig[a, b] * self._B[(a, b)]
        return out


def part2() -> None:
    print("\n=== Part 2: BRST deformation in the L-infinity model of 058 ===")
    # (a) 058's literal model: l3(psi, psi, .) vanishes on the c-number field sector
    for seed in (11, 12, 13):
        lm = LinfModel(seed, [0, 1, 2], (-1, 3))
        rng = np.random.default_rng(1000 + seed)
        mx = 0.0
        for _ in range(5):
            psi = np.zeros(lm.nk)
            psi[lm.f1] = rng.standard_normal(len(lm.f1))
            mx = max(mx, np.max(np.abs(lm.T2(psi))),
                     np.max(np.abs(lm.T(psi, 0.3) - lm.T0() - 0.3 * lm.T1(psi))))
        report(f"C2.0-058 seed {seed}", lm.same_as_058 and mx < 1e-12,
               f"058's model (A = H*(S^3), cut (-1,3)) rebuilt identically; on the c-number "
               f"field sector T_psi is exactly linear in g (l3(psi,psi,.) = 0, max {mx:.1e}): "
               f"no l3 to compare with")
    # (b) same construction with A = Lambda[th1,th2,th3], massive fields integrated out
    for seed in (21, 22):
        lm = LinfModel(seed, [0, 0, 0, 1, 1], (1,), parent="T3")
        d1, d2 = len(lm.f1), len(lm.f2)
        rng = np.random.default_rng(2000 + seed)
        # structure checks of the parent cyclic DGLA
        Nn = lm.Nn
        rng.standard_normal((2, Nn))  # advance the stream as in run 1 (reproducibility)
        e_ = []
        e_.append(np.max(np.abs(lm.Q @ lm.Q)))
        lb = 0.0
        cyc = 0.0
        sym = 0.0
        for s_ in rng.choice(Nn, 12, replace=False):
            for t_ in rng.choice(Nn, 12, replace=False):
                es = np.eye(Nn)[s_]
                et = np.eye(Nn)[t_]
                ds = int(lm.deg[s_]) % 2
                lhs = lm.Q @ lm.mul(es, et)
                rhs = lm.mul(lm.Q @ es, et) + (-1) ** ds * lm.mul(es, lm.Q @ et)
                lb = max(lb, np.max(np.abs(lhs - rhs)))
                cyc = max(cyc, abs(lm.G[:, t_] @ (lm.Q @ es) + (-1) ** ds * es @ lm.G @ (lm.Q @ et)))
                sym = max(sym, abs(lm.G[s_, t_] - (-1) ** ((ds * int(lm.deg[t_])) % 2) * lm.G[t_, s_]))
        report(f"C2.0-T3 seed {seed}", e_[0] < 1e-12 and lb < 1e-12 and cyc < 1e-12 and sym < 1e-12,
               f"parent Lambda[th]x End(W): Q^2 = 0, Leibniz, graded-symmetric and "
               f"Q-invariant pairing ({max(e_[0], lb, cyc, sym):.1e}); retract dim {lm.nk}, "
               f"dim H^1 = {d1}, dim H^2 = {d2}")
        gv = 0.5
        psi = np.zeros(lm.nk)
        psi[lm.f1] = rng.standard_normal(d1) * 0.6
        # C2.2: T on fields = Hessian of the transferred action (directional, 3 pairs)
        h = 1e-4
        Om = lm.iota.T @ lm.G @ lm.iota
        Tm = lm.T(psi, gv)
        OT = Om[np.ix_(lm.f1, lm.f2)] @ Tm[np.ix_(lm.f2, lm.f1)]
        errs, errms = [], []
        for _ in range(3):
            xa = np.zeros(lm.nk)
            xb = np.zeros(lm.nk)
            xa[lm.f1] = rng.standard_normal(d1)
            xb[lm.f1] = rng.standard_normal(d1)

            def f(da, db):
                return lm.S(psi + da * xa + db * xb, gv)
            hs = (f(h, h) - f(h, -h) - f(-h, h) + f(-h, -h)) / (4 * h * h)
            ot = xa[lm.f1] @ OT @ xb[lm.f1]
            errs.append(abs(ot - hs) / abs(hs))
            errms.append(abs(-ot - hs) / abs(hs))
        err, errm = max(errs), min(errms)
        report(f"C2.2 seed {seed}", err < 1e-6 and errm > 1e-2,
               f"omega(x, T_psi y) == d^2 S_H(psi)[x,y], 3 random pairs (rel {err:.1e}; "
               f"opposite sign {errm:.1e})")
        dev = []
        for gg in (1e-2, 2e-2):
            dev.append(np.max(np.abs(lm.T(psi, gg) - lm.T0() - gg * lm.T1(psi)
                                     - gg**2 * lm.T2(psi))))
        slope = np.log2(dev[1] / dev[0])
        dev_b = np.max(np.abs(lm.T(psi, 1e-2) - lm.T0() - 1e-2 * lm.T1(psi)))
        t2f = np.max(np.abs(lm.T2(psi)[np.ix_(lm.f2, lm.f1)]))
        report(f"C2.2-taylor seed {seed}", abs(slope - 3) < 0.15 and dev_b / dev[0] > 20
               and t2f > 1e-3,
               f"T = T0 + g T1 + g^2 T2(P) + O(g^{slope:.2f}); without T2 the remainder is "
               f"{dev_b / dev[0]:.0f}x larger; T2 on fields {t2f:.2e} != 0 (V4 on fields)")
        pf = psi[lm.f1]
        polerr = np.max(np.abs(lm.T2_sym(np.outer(pf, pf)) - lm.T2(psi)))
        report(f"C2.2-polar seed {seed}", polerr < 1e-12 * (1 + np.max(np.abs(lm.T2(psi)))),
               f"T2 extended linearly to Sym^2 H^1 reproduces T2(P) ({polerr:.1e})")
        # C2.3: Maurer-Cartan point from a deformed differential D' (parent MC, cut (1,))
        Dp, _ = rank1_differential([0, 0, 0, 1, 1], rng, scale=0.3, base=lm.uv)
        Phi0 = (lm.hat(Dp) - lm.hat(lm.D)) / gv
        mc_par = np.max(np.abs(lm.Q @ Phi0 + gv * lm.mul(Phi0, Phi0)))
        psi0 = lm.p @ Phi0
        fix = np.max(np.abs(lm.Phi(psi0, gv) - Phi0))
        Fh = np.max(np.abs(lm.F(psi0, gv)))
        T_0 = lm.T(psi0, gv)
        sq = np.max(np.abs(T_0 @ T_0)) / np.max(np.abs(T_0)) ** 2
        Tr = lm.T(psi, gv)
        sq_off = np.max(np.abs(Tr @ Tr)) / np.max(np.abs(Tr)) ** 2
        l3part = gv**2 * lm.T2(psi0)
        Tb = T_0 - l3part
        sq_b = np.max(np.abs(Tb @ Tb)) / np.max(np.abs(Tb)) ** 2
        report(f"C2.3 seed {seed}", mc_par < 1e-12 and fix < 1e-10 and Fh < 1e-10 and sq < 1e-12
               and sq_off > 1e-4 and sq_b > 1e-4 and np.max(np.abs(l3part)) > 1e-3,
               f"MC point (D' = D + g Phi, |psi0| = {np.linalg.norm(psi0):.3f}, "
               f"|g^2 T2(P0)| = {np.max(np.abs(l3part)):.2e}): |T^2|/|T|^2 = {sq:.1e}; off "
               f"shell {sq_off:.1e}; break l3 -> 0 {sq_b:.1e}")
        eta = np.zeros(lm.nk)
        eta[lm.f1] = rng.standard_normal(d1)
        rat = []
        for ep in (1e-3, 1e-4):
            q = psi0 + ep * eta
            Tq = lm.T(q, gv)
            rat.append(np.max(np.abs(Tq @ Tq)) / np.max(np.abs(lm.F(q, gv))))
        report(f"C2.3-linear seed {seed}", abs(rat[0] / rat[1] - 1) < 2e-2,
               f"|T^2|/|F_H| = {rat[0]:.4f}, {rat[1]:.4f} at distance 1e-3, 1e-4: defect "
               f"linear in the EOM (Zwiebach (4.117))")
        # C2.4: the Sigma-deformed operator
        d_map = []
        for a in range(d1):
            for b in range(a, d1):
                Sg = np.zeros((d1, d1))
                Sg[a, b] = Sg[b, a] = 1.0
                T2S = lm.T2_sym(Sg)
                d_map.append((lm.T0() @ T2S + T2S @ lm.T0()).ravel())
        Lmat = np.array(d_map).T
        sv = np.linalg.svd(Lmat, compute_uv=False)
        rank = int((sv > 1e-10 * sv[0]).sum())
        P0 = np.outer(psi0[lm.f1], psi0[lm.f1])
        out = {}
        Rm = rng.standard_normal((d1, d1))
        for name, Delta in (("c=1/3 at Sigma_0=P_0 (R1 block)", -2.0 / 3.0 * P0),
                            ("c=1, random Sigma_0-P_0", 0.3 * (Rm + Rm.T)),
                            ("c=1, Sigma_0=P_0", 0 * P0)):
            Qd = T_0 + gv**2 * lm.T2_sym(Delta)
            out[name] = np.max(np.abs(Qd @ Qd)) / np.max(np.abs(Qd)) ** 2
        # {T0, T2(P0)} != 0: P0 is not in ker L, so c = 1/3 fails already at O(g^2)
        T2P = lm.T2_sym(P0)
        LP = np.max(np.abs(lm.T0() @ T2P + T2P @ lm.T0())) / max(np.max(np.abs(T2P)), 1e-300)
        # a Delta in ker L: the O(g^2) defect vanishes, the higher orders do not
        _, _, vt = np.linalg.svd(Lmat)
        kv = vt[rank:].T @ rng.standard_normal(Lmat.shape[1] - rank)
        Dk = np.zeros((d1, d1))
        iu = [(a, b) for a in range(d1) for b in range(a, d1)]
        for c_, (a, b) in zip(kv, iu):
            Dk[a, b] = Dk[b, a] = c_
        T2K = lm.T2_sym(Dk)
        lead = np.max(np.abs(lm.T0() @ T2K + T2K @ lm.T0())) / np.max(np.abs(T2K))
        Qk = T_0 + gv**2 * T2K
        full_k = np.max(np.abs(Qk @ Qk)) / np.max(np.abs(Qk)) ** 2
        report(f"C2.4-kernel seed {seed}", LP > 1e-6 and lead < 1e-10,
               f"|{{T0,T2(P0)}}|/|T2(P0)| = {LP:.2e} (P0 not in ker L); Delta in ker L: "
               f"leading defect {lead:.1e}, full |Q^2|/|Q|^2 = {full_k:.1e} (from g^3 on)")
        report(f"C2.4 seed {seed}", out["c=1, Sigma_0=P_0"] < 1e-12
               and out["c=1/3 at Sigma_0=P_0 (R1 block)"] > 1e-4
               and out["c=1, random Sigma_0-P_0"] > 1e-4,
               f"Delta -> {{T0, T2(Delta)}} on Sym^2 H^1 (dim {Lmat.shape[1]}): rank {rank}, "
               f"kernel {Lmat.shape[1] - rank}; |Q^2|/|Q|^2 at the MC point: " +
               ", ".join(f"{k}: {v:.1e}" for k, v in out.items()))


# =====================================================================================
# Part 3: the degenerate branch in the five-field model (g = 1, scaled variables)
# =====================================================================================
def five_field(seed: int):
    """Symbolic five-field model at g = 1: returns dict of sympy objects."""
    rng = np.random.default_rng(seed)
    N = 2
    V = {k: rand_sym(rng, N, k) for k in range(2, 6)}
    t = sp.symbols("t0:2")
    s = sp.symbols("s0:3")
    pairs = [(0, 0), (0, 1), (1, 1)]
    Es = [Model.E(p_, N) for p_ in pairs]
    P = [[t[a] * t[b] for b in range(N)] for a in range(N)]
    A = sp.Matrix(3, 3, lambda i, j: contract_mats(V[4], [Es[i], Es[j]], []))
    W = sp.Matrix(3, 3, lambda i, j: contract_mats(V[5], [Es[i], Es[j]], [list(t)]))
    u = sp.Matrix([contract_mats(V[4], [E_, P], []) for E_ in Es])
    K = A - W / 5
    Sig = [[s[0], s[1]], [s[1], s[2]]]
    S3 = (sp.Rational(1, 2) * contract(V[2], [list(t)] * 2) + contract(V[3], [list(t)] * 3) / 6
          - contract_mats(V[4], [Sig, Sig], []) / 24 + contract_mats(V[4], [Sig, P], []) / 12
          + contract_mats(V[5], [Sig, Sig], [list(t)]) / 120)
    return dict(V=V, t=t, s=s, A=A, W=W, u=u, K=K, S3=sp.expand(S3), Es=Es, pairs=pairs)


def base_points(m: dict) -> list:
    """Real solutions of det K = 0, adj(K) u = 0 (resultant in t1, then refine)."""
    t = m["t"]
    detK = sp.expand(m["K"].det())
    adju = (m["K"].adjugate() * m["u"]).applyfunc(sp.expand)
    R = sp.Poly(sp.resultant(detK, adju[0], t[1]), t[0])
    out = []
    for r in R.nroots(n=30, maxsteps=200):
        if abs(sp.im(r)) > 1e-12:
            continue
        r = sp.re(r)
        cub = sp.Poly(detK.subs(t[0], r), t[1])
        for r2 in cub.nroots(n=30, maxsteps=200):
            if abs(sp.im(r2)) > 1e-12:
                continue
            val = [abs(sp.N(e.subs({t[0]: r, t[1]: sp.re(r2)}), 30)) for e in adju]
            if max(val) < 1e-6 * (1 + abs(r) ** 4):
                out.append((r, sp.re(r2)))
    return out



def part3() -> None:
    print("\n=== Part 3: degenerate branch, five-field model (mp.dps = 40) ===")
    mp.mp.dps = 40
    found = None
    for seed in range(630, 660):
        m = five_field(seed)
        if m["A"].det() == 0:
            continue
        bp = base_points(m)
        if bp:
            found = (seed, m, bp)
            break
    if found is None:
        report("C3.4-exist", False, "no real base point for seeds 630..659")
        return
    seed, m, bp = found
    print(f"seed {seed}: {len(bp)} real base point(s) (seeds tried: 630..{seed})")
    t, s = m["t"], m["s"]
    tt = list(t) + list(s)
    fK = sp.lambdify(t, m["K"], "mpmath")
    fu = sp.lambdify(t, m["u"], "mpmath")
    fdet = sp.lambdify(t, m["K"].det(), "mpmath")
    adju = (m["K"].adjugate() * m["u"]).applyfunc(sp.expand)
    grad = [sp.diff(m["S3"], v) for v in tt]
    fgrad = sp.lambdify(tt, grad, "mpmath")
    fhess = sp.lambdify(tt, sp.hessian(m["S3"], tt), "mpmath")
    fS = sp.lambdify(tt, m["S3"], "mpmath")
    # refine the first base point with 40 digits
    r0 = [mp.mpf(str(sp.N(c, 30))) for c in bp[0]]
    j = int(np.argmax([abs(float(sp.N(e.subs({t[0]: bp[0][0], t[1]: bp[0][1]})))) + 0 for e in adju]))
    # solve det K = 0 and n.u = 0 using the adjugate component of the largest null entry
    Kn = [sp.lambdify(t, e, "mpmath") for e in adju]
    tau0 = mp.findroot(lambda a, b: [fdet(a, b), Kn[j](a, b)], r0)
    tau0 = [tau0[0], tau0[1]]
    K0 = mp.matrix(fK(*tau0))
    u0 = mp.matrix(fu(*tau0))
    U_, S_, V_ = mp.svd_r(K0)
    n = mp.matrix([V_[2, i] for i in range(3)])
    smin, smax = S_[2], S_[0]
    nu = (n.T * u0)[0]

    def corank_one(sv: list) -> bool:
        """Corank exactly one: sigma_2/sigma_max bounded away from zero (critic #15)."""
        return sv[1] / sv[0] > mp.mpf(10) ** -3

    report("C3.1-locus", abs(fdet(*tau0)) < mp.mpf(10) ** -30 and smin / smax < mp.mpf(10) ** -30
           and abs(nu) < mp.mpf(10) ** -30 * (1 + mp.norm(u0)) and corank_one(S_),
           f"tau0 = ({mp.nstr(tau0[0], 12)}, {mp.nstr(tau0[1], 12)}): sigma_min/sigma_max = "
           f"{mp.nstr(smin / smax, 3)}, sigma_2/sigma_max = {mp.nstr(S_[1] / S_[0], 3)} "
           f"(corank one), n.u = {mp.nstr(nu, 3)}; other base points: "
           f"{[(float(a), float(b)) for a, b in bp[1:]]}")
    # break leg: same singular vectors, middle singular value set to zero (corank two)
    S_c2 = mp.svd_r(U_ * mp.diag([S_[0], 0, 0]) * V_, compute_uv=False)
    report("C3.1-locus-break", not corank_one(S_c2),
           f"corank-two matrix: sigma_2/sigma_max = {mp.nstr(S_c2[1] / S_c2[0], 3)}; "
           "the corank-one test rejects it")
    # particular solution and the line
    Sig_p = mp.lu_solve(K0 + n * n.T, u0)
    lams = [mp.mpf(-2), mp.mpf("0.7"), mp.mpf(3)]
    eom = max(mp.norm(K0 * (Sig_p + lam * n) - u0) for lam in lams)
    Svals = [fS(*tau0, *(Sig_p + lam * n)) for lam in lams]
    report("C3.2-line", eom < mp.mpf(10) ** -30,
           f"Sigma-EOM K Sigma = u on Sigma_p + lambda n, lambda in {{-2,0.7,3}}: residual {mp.nstr(eom, 3)}")
    flat = max(abs(v - Svals[0]) for v in Svals)
    Sp_val = fS(*tau0, *Sig_p)
    A0 = fS(*tau0, 0, 0, 0)
    Kp = mp.lu_solve(K0 + n * n.T, u0)
    val_pred = A0 + (u0.T * Kp)[0] / 24
    report("C3.2-flat", flat < mp.mpf(10) ** -30 and abs(Sp_val - val_pred) < mp.mpf(10) ** -30,
           f"S3 constant along the line (spread {mp.nstr(flat, 3)}); value "
           f"A + u^T K^+ u/24 = {mp.nstr(val_pred, 15)}")
    # break (a): off det K = 0 -> unique saddle
    d_hat = [mp.mpf("0.6"), mp.mpf("0.8")]
    eps = mp.mpf("1e-6")
    Ka = mp.matrix(fK(tau0[0] + eps * d_hat[0], tau0[1] + eps * d_hat[1]))
    sa = mp.svd_r(Ka, compute_uv=False)
    report("C3.2-break-a", sa[2] / sa[0] > mp.mpf(10) ** -12,
           f"tau0 + 1e-6 d: K invertible (sigma_min/sigma_max = {mp.nstr(sa[2] / sa[0], 3)}), "
           f"unique Sigma saddle")
    # break (b): along det K = 0, n.u != 0 -> no Sigma solution
    gd = [mp.diff(lambda a: fdet(a, tau0[1]), tau0[0]), mp.diff(lambda b: fdet(tau0[0], b), tau0[1])]
    tang = [-gd[1], gd[0]]
    nt = mp.sqrt(tang[0] ** 2 + tang[1] ** 2)
    tang = [tang[0] / nt, tang[1] / nt]
    eta = mp.findroot(lambda e: fdet(tau0[0] + eps * tang[0] + e * gd[0],
                                     tau0[1] + eps * tang[1] + e * gd[1]), mp.mpf(0))
    tb = [tau0[0] + eps * tang[0] + eta * gd[0], tau0[1] + eps * tang[1] + eta * gd[1]]
    Kb = mp.matrix(fK(*tb))
    ub = mp.matrix(fu(*tb))
    _, Sb, Vb = mp.svd_r(Kb)
    nb = mp.matrix([Vb[2, i] for i in range(3)])
    report("C3.2-break-b", abs((nb.T * ub)[0]) > mp.mpf(10) ** -12 and Sb[2] / Sb[0] < mp.mpf(10) ** -25,
           f"on det K = 0 at distance 1e-6: n.u = {mp.nstr((nb.T * ub)[0], 3)} != 0, "
           f"K Sigma = u has no solution")
    # null direction of the Sigma block and of the full Hessian
    Hf = mp.matrix(fhess(*tau0, *Sig_p))
    Hss = Hf[2:5, 2:5]
    Hts = Hf[0:2, 2:5]
    report("C3.3-null", mp.norm(Hss * n) < mp.mpf(10) ** -30 and mp.norm(Hts * n) > mp.mpf(10) ** -6,
           f"H_SigSig n = 0 ({mp.nstr(mp.norm(Hss * n), 3)}); H_PsiSig n = "
           f"{mp.nstr(mp.norm(Hts * n), 6)} != 0: (0,n) is not null for the full Hessian")
    # Psi-EOM on the line: quadratic in lambda, generically no common root
    Ev = [mp.matrix(fgrad(*tau0, *(Sig_p + lam * n)))[0:2] for lam in (0, 1, -1)]
    E0 = Ev[0]
    E2 = (Ev[1] + Ev[2]) / 2 - E0
    E1 = (Ev[1] - Ev[2]) / 2
    r1 = mp.polyroots([E2[0], E1[0], E0[0]], maxsteps=500, extraprec=200)
    r2 = mp.polyroots([E2[1], E1[1], E0[1]], maxsteps=500, extraprec=200)
    sep = min(abs(a - b) / (abs(a) + abs(b)) for a in r1 for b in r2)
    report("C3.4-no-family", sep > mp.mpf("1e-3"),
           f"Psi-EOM on the line E(l) = E0 + l E1 + l^2 E2: roots of E_1: "
           f"{[mp.nstr(r, 6) for r in r1]}, of E_2: {[mp.nstr(r, 6) for r in r2]}; relative "
           f"separation {mp.nstr(sep, 3)}: no joint critical point on the branch")
    # break leg of the separation measure: two copies of the same quadratic share roots
    sep_b = min(abs(a - b) / (abs(a) + abs(b)) for a in r1 for b in r1)
    report("C3.4-no-family-break", sep_b < mp.mpf("1e-20"),
           "the separation measure detects common roots (E_1 against itself)")
    # tuned V2: joint critical point at lambda* = 1/2
    lam_s = mp.mpf("0.5")
    Es_ = mp.matrix(fgrad(*tau0, *(Sig_p + lam_s * n)))[0:2]
    Mt = mp.matrix([[tau0[0], tau0[1], 0], [0, tau0[0], tau0[1]]])
    abc = Mt.T * mp.lu_solve(Mt * Mt.T, -Es_)
    dV2 = mp.matrix([[abc[0], abc[1]], [abc[1], abc[2]]])

    def full_grad(z, dV):
        gr = mp.matrix(fgrad(*z))
        gr[0] += (dV * mp.matrix(z[0:2]))[0]
        gr[1] += (dV * mp.matrix(z[0:2]))[1]
        return gr

    z_star = list(tau0) + list(Sig_p + lam_s * n)
    r_star = mp.norm(full_grad(z_star, dV2))
    Hfull = mp.matrix(fhess(*z_star)) + mp.matrix([[dV2[0, 0], dV2[0, 1], 0, 0, 0],
                                                  [dV2[1, 0], dV2[1, 1], 0, 0, 0],
                                                  [0] * 5, [0] * 5, [0] * 5])
    ev = mp.eigsy(Hfull, eigvals_only=True)
    minev = min(abs(e) for e in ev)
    report("C3.4-tuned", r_star < mp.mpf(10) ** -30 and minev > mp.mpf(10) ** -8,
           f"one tuned coupling (dV2, |dV2| = {mp.nstr(mp.mnorm(dV2, 1), 4)}): full EOM residual "
           f"{mp.nstr(r_star, 3)} at lambda* = 1/2; full Hessian nondegenerate (min |eig| = "
           f"{mp.nstr(minev, 4)})")
    # continuation off the wall: nearby critical point with det K != 0, displacement ~ eps
    Rr = mp.matrix([[mp.mpf("0.3"), mp.mpf("-0.7")], [mp.mpf("-0.7"), mp.mpf("0.4")]])
    disp = []
    for ep in (mp.mpf("1e-5"), mp.mpf("2e-5")):
        dVe = dV2 + ep * Rr
        z = mp.matrix(z_star)
        for _ in range(30):
            Hz = mp.matrix(fhess(*z)) + mp.matrix([[dVe[0, 0], dVe[0, 1], 0, 0, 0],
                                                  [dVe[1, 0], dVe[1, 1], 0, 0, 0],
                                                  [0] * 5, [0] * 5, [0] * 5])
            z = z - mp.lu_solve(Hz, full_grad(list(z), dVe))
        dK = fdet(z[0], z[1])
        Kz = mp.matrix(fK(z[0], z[1]))
        sig_reg = mp.lu_solve(Kz, mp.matrix(fu(z[0], z[1])))
        disp.append((mp.norm(z - mp.matrix(z_star)), abs(dK),
                     mp.norm(sig_reg - z[2:5]), mp.norm(full_grad(list(z), dVe))))
    ratio = disp[1][0] / disp[0][0]
    report("C3.4-continuation", abs(ratio - 2) < mp.mpf("1e-3") and disp[0][1] > 0 and
           disp[0][2] < mp.mpf(10) ** -25 and disp[0][3] < mp.mpf(10) ** -25,
           f"coupling moved off the wall by eps: critical point moves by {mp.nstr(disp[0][0], 4)} "
           f"(ratio {mp.nstr(ratio, 6)} for eps x2), det K = {mp.nstr(disp[0][1], 3)} != 0, "
           f"Sigma = K^-1 u (regular branch) to {mp.nstr(disp[0][2], 3)}")
    # blow-up: Sigma_*(tau0 + t d) -> Sigma_p + lambda(d) n, lambda(d) = n.(u1 - K1 Sigma_p)/(n.K1 n)
    lams_d = []
    errs = []
    for d in ([mp.mpf("0.6"), mp.mpf("0.8")], [mp.mpf("-0.28"), mp.mpf("0.96")]):
        tt_ = mp.mpf("1e-18")
        tp = [tau0[0] + tt_ * d[0], tau0[1] + tt_ * d[1]]
        sig_t = mp.lu_solve(mp.matrix(fK(*tp)), mp.matrix(fu(*tp)))
        h = mp.mpf("1e-12")
        K1 = (mp.matrix(fK(tau0[0] + h * d[0], tau0[1] + h * d[1])) -
              mp.matrix(fK(tau0[0] - h * d[0], tau0[1] - h * d[1]))) / (2 * h)
        u1 = (mp.matrix(fu(tau0[0] + h * d[0], tau0[1] + h * d[1])) -
              mp.matrix(fu(tau0[0] - h * d[0], tau0[1] - h * d[1]))) / (2 * h)
        lam_d = (n.T * (u1 - K1 * Sig_p))[0] / (n.T * K1 * n)[0]
        errs.append(mp.norm(sig_t - (Sig_p + lam_d * n)))
        lams_d.append(lam_d)
        Veff_t = fS(*tp, *sig_t)
        errs.append(abs(Veff_t - val_pred))
    report("C3.5-blowup", max(errs) < mp.mpf(10) ** -10 and abs(lams_d[0] - lams_d[1]) > mp.mpf("1e-3"),
           f"lim Sigma_*(tau0 + t d) = Sigma_p + lambda(d) n with lambda = {mp.nstr(lams_d[0], 8)}, "
           f"{mp.nstr(lams_d[1], 8)} for two directions; V_eff -> the flat value (max err "
           f"{mp.nstr(max(errs), 3)})")
    # all base points: no common root of the two Psi-EOM components on the line
    seps = []
    coranks = []
    for b in bp:
        rb = [mp.mpf(str(sp.N(c, 30))) for c in b]
        jb = int(np.argmax([abs(float(sp.N(e.subs({t[0]: b[0], t[1]: b[1]})))) for e in adju]))
        tb0 = mp.findroot(lambda a, c: [fdet(a, c), Kn[jb](a, c)], rb)
        tb0 = [tb0[0], tb0[1]]
        Kb0 = mp.matrix(fK(*tb0))
        ub0 = mp.matrix(fu(*tb0))
        _, Sb0, Vb0 = mp.svd_r(Kb0)
        coranks.append(corank_one(Sb0))  # fix pass 2: corank exactly one at every base point
        nb0 = mp.matrix([Vb0[2, i] for i in range(3)])
        Spb = mp.lu_solve(Kb0 + nb0 * nb0.T, ub0)
        Evb = [mp.matrix(fgrad(*tb0, *(Spb + lam * nb0)))[0:2] for lam in (0, 1, -1)]
        e0, e2, e1 = Evb[0], (Evb[1] + Evb[2]) / 2 - Evb[0], (Evb[1] - Evb[2]) / 2
        q1 = mp.polyroots([e2[0], e1[0], e0[0]], maxsteps=500, extraprec=200)
        q2 = mp.polyroots([e2[1], e1[1], e0[1]], maxsteps=500, extraprec=200)
        seps.append(min(abs(a - c) / (abs(a) + abs(c)) for a in q1 for c in q2))
        print(f"  base point ({mp.nstr(tb0[0], 8)}, {mp.nstr(tb0[1], 8)}): roots "
              f"{[mp.nstr(r, 6) for r in q1]} | {[mp.nstr(r, 6) for r in q2]}")
    report("C3.4-no-family-all", min(seps) > mp.mpf("1e-3") and all(coranks),
           f"all {len(bp)} base points: min relative root separation {mp.nstr(min(seps), 3)}; "
           f"corank one at {sum(coranks)}/{len(coranks)}")
    report("C3.5-blowup-break", mp.norm(mp.lu_solve(mp.matrix(fK(tau0[0] + mp.mpf('1e-18') * mp.mpf('0.6'), tau0[1] + mp.mpf('1e-18') * mp.mpf('0.8'))), mp.matrix(fu(tau0[0] + mp.mpf('1e-18') * mp.mpf('0.6'), tau0[1] + mp.mpf('1e-18') * mp.mpf('0.8')))) - (Sig_p + lams_d[1] * n)) > mp.mpf("1e-4"),
           "the direction-0 limit differs from the direction-1 line point (limit is direction-dependent)")


if __name__ == "__main__":
    if "--only3" not in sys.argv:
        part1()
        part1_offshell()
    if "--only3" not in sys.argv:
        part2()
    part3()
    print(f"\nSUMMARY: {npass} PASS, {len(failures)} FAIL" + (f": {failures}" if failures else ""))
    sys.exit(1 if failures else 0)
