#!/usr/bin/env python3
"""
Verify the algebra of finite-field truncations of the cubic theory (record 057).

Verified:
  C2.*  the (t, sigma) model: sigma_* at S_3 (R17 conventions), the rational
        eliminated potential, its expansion through t^6 (target + feedback
        g^4/600 V5^2 t^6 / V4), the pole of the dressed kernel and the absence
        of a finite saddle there, the sextic (W_6) branches and the eliminated
        potential through t^6, the one-field specialisation of R19's exact
        rewriting, the g-scaling, the S_4 fold (discriminant zero) and the
        reality condition of the S_4 saddle at t_pole.
  C3.*  the five-field model (symbolic Hankel V4 block) and the general
        statement on generic tensors: exactness of the quartic elimination
        for S = Sym^2 U (fails for a Veronese-incomplete S), the O(g^4)
        truncated-inverse feedback, the Schur-complement formula for the
        deviation, the sextic on-shell mismatch of the truncated S_4 with the
        full-C vertex W_6, and its vanishing with the S-consistent vertex
        W_6^(S) = V_6 - (6/5) C_S (C_S built with (V4|_S)^-1).
  C4.*  part B (record 057 section 4), generic symmetric tensors on H = R^6,
        dim U = 2, three seeds, exact Taylor coefficients in g at fixed unit
        Psi in U (g nilpotent of order 7): the untruncated EOM components off
        (U, S) at a truncated saddle -- Psi-EOM along U^perp from O(g) with the
        level-truncation coefficients and the O(g^3) w-deviation; Sigma-EOM
        along S^c zero at S_2, -w/5 at O(g) at S_3/S_4; the Z_2-universal
        instance ((a) and the U.U^perp part of (b) vanish at all orders, the
        Sym^2 U^perp part does not), the one-leg (Sen-type) instance, broken
        tensors switching (a) on at O(g^(n-2)), the level axis (U + U'
        universal); the Schur absorption (relaxing S^c: +w M^-1 w g^4/600 at
        S_3 and S_4 full-C, zero through g^4 for W_6^(S) against R19's S_4),
        by series and by exact finite-g saddles with Richardson extrapolation.
Check labels follow the claim-tree node IDs of record 057.
Not verified: any CFT value of V_n (symbolic / random tensors only); that the
  real vertices obey the selection rule of H1 (a hypothesis, record 057 section 4); the
  identification of the truncated objects with sister-project numbers
  (Task 13); convergence questions beyond the finite algebraic layer.

Conventions: R1, R17, R19 of knowledge/results.md; coefficient g^{n-2}/n!.
Run: .venv/bin/python codes/verify-truncation-structure.py
"""

from __future__ import annotations

import itertools
import math
import sys

import numpy as np
import sympy as sp

SEED = 20260926
rng = np.random.default_rng(SEED)
print(f"seed = {SEED}")

results: list[tuple[str, bool]] = []


def report(name: str, ok: bool, detail: str = "") -> None:
    """Print and record one named PASS/FAIL check."""
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))
    results.append((name, bool(ok)))


def expect_fail(name: str, ok: bool, detail: str = "") -> None:
    """Break leg: the perturbed statement must FAIL; report PASS if it does."""
    report(f"{name}-break", not ok, detail)


# ============================================================ C2: (t, sigma)
t, sig, g = sp.symbols("t sigma g")
V2, V3, V4, V5, V6, CTT = sp.symbols("V2 V3 V4 V5 V6 C_TT")
W6 = V6 - sp.Rational(6, 5) * CTT
A = V2 * t**2 / 2 + g * V3 * t**3 / 6
S2 = A - g**2 / 24 * V4 * sig**2 + g**2 / 12 * V4 * sig * t**2
S3 = S2 + g**3 / 120 * V5 * sig**2 * t
S4 = S3 + g**4 / 720 * W6 * sig**3
Seff6 = (A + g**2 / 24 * V4 * t**4 + g**3 / 120 * V5 * t**5
         + g**4 / 720 * V6 * t**6)
K = V4 - g / 5 * V5 * t

# numeric points in general position (complex)
pts = [{s: complex(*rng.standard_normal(2)) for s in (t, g, V2, V3, V4, V5, V6, CTT)}
       for _ in range(5)]


def numeq(e1: sp.Expr, e2: sp.Expr, tol: float = 1e-10) -> bool:
    """Compare two expressions at the seeded complex points."""
    for p in pts:
        a, b = complex(e1.subs(p)), complex(e2.subs(p))
        if abs(a - b) > tol * (1 + abs(a)):
            return False
    return True


# C2.1: sigma_* from the S3 sigma-EOM
sol = sp.solve(sp.diff(S3, sig), sig)
sig_star = V4 * t**2 / K
ok = len(sol) == 1 and sp.simplify(sol[0] - sig_star) == 0 and numeq(sol[0], sig_star)
report("C2.1", ok, f"sigma_* = {sp.simplify(sol[0])}")
# cross-check against R17's Sigma_* = P + (g/5) K^{-1} v, v = V5 t^3
ok = sp.simplify(t**2 + g / 5 * V5 * t**3 / K - sig_star) == 0
report("C2.1-R17", ok, "sigma_* = t^2 + (g/5) K^-1 v")
wrong = V4 * t**2 / (V4 - g / 4 * V5 * t)
expect_fail("C2.1", numeq(sol[0], wrong), "g/4 instead of g/5 must not match")

# C2.2: closed form of V_eff
Veff3 = sp.simplify(S3.subs(sig, sig_star))
Veff3_cf = A + g**2 / 24 * V4**2 * t**4 / K
report("C2.2", sp.simplify(Veff3 - Veff3_cf) == 0 and numeq(Veff3, Veff3_cf),
       "V_eff = A + g^2 V4^2 t^4 / (24 (V4 - g V5 t/5))")
# R17 exact rewriting on-shell: V_eff - S_eff5 = g^4/600 v K^{-1} v
Seff5 = A + g**2 / 24 * V4 * t**4 + g**3 / 120 * V5 * t**5
fb = g**4 / 600 * (V5 * t**3) ** 2 / K
report("C2.2-R17", sp.simplify(Veff3 - Seff5 - fb) == 0 and numeq(Veff3 - Seff5, fb),
       "V_eff - S_eff^(5) = g^4/600 v^2/K")
expect_fail("C2.2", numeq(Veff3 - Seff5, g**4 / 720 * (V5 * t**3) ** 2 / K),
            "feedback 1/720 must not match")

# C2.3: series in t through t^6
ser = sp.series(Veff3, t, 0, 7).removeO()
target = Seff5 + g**4 / 600 * V5**2 * t**6 / V4
report("C2.3", sp.expand(ser - target) == 0, "through t^6: target + g^4/600 V5^2/V4 t^6")
# all-orders geometric coefficient: [t^{4+k}] = g^2/24 V4 (g V5/(5 V4))^k
ser12 = sp.series(Veff3, t, 0, 13).removeO()
ok = all(sp.simplify(ser12.coeff(t, 4 + k) - g**2 / 24 * V4 * (g * V5 / (5 * V4))**k) == 0
         for k in range(9))
report("C2.3-allorders", ok, "[t^{4+k}] V_eff = (g^2/24) V4 (g V5 / 5 V4)^k, k<=8")

# C2.4: pole and absence of a finite saddle at K = 0
t_pole = 5 * V4 / (g * V5)
report("C2.4-pole", sp.simplify(K.subs(t, t_pole)) == 0, "K(t_pole)=0, t_pole = 5 V4/(g V5)")
eom_at_pole = sp.simplify(sp.diff(S3, sig).subs(t, t_pole))
ok = (sp.simplify(eom_at_pole - g**2 / 12 * V4 * t_pole**2) == 0
      and sig not in eom_at_pole.free_symbols and sp.simplify(eom_at_pole) != 0)
report("C2.4-nosaddle", ok, f"sigma-EOM at t_pole = {sp.factor(eom_at_pole)} (sigma-independent, nonzero)")
res = sp.residue(Veff3_cf, t, t_pole)
res_expected = -sp.Rational(5, 24) * g * V4**2 * t_pole**4 / V5
report("C2.4-residue", sp.simplify(res - res_expected) == 0, f"Res = {sp.factor(res)}")

# C2.4-count: critical-point count: K^2 dV_eff/dt is t x (cubic)
num = sp.factor(sp.together(sp.diff(Veff3_cf, t)))
numer = sp.numer(sp.together(sp.diff(Veff3_cf, t) * K**2))
numer = sp.expand(sp.simplify(numer))
poly = sp.Poly(numer, t)
report("C2.4-count", poly.degree() == 4 and poly.eval(0) == 0,
       f"deg = {poly.degree()}, t=0 root; same count as the quintic polynomial")

# C2.6: sextic sigma-EOM branches
eq4 = sp.expand(sp.diff(S4, sig) * 12 / g**2)
eq4_expected = V4 * t**2 - K * sig + g**2 / 20 * W6 * sig**2
report("C2.6-eom", sp.expand(eq4 - eq4_expected) == 0, "V4 t^2 - K sigma + (g^2/20) W6 sigma^2 = 0")
disc = K**2 - g**2 * W6 * V4 * t**2 / 5
sig_m = 10 / (g**2 * W6) * (K - sp.sqrt(disc))
sig_p = 10 / (g**2 * W6) * (K + sp.sqrt(disc))
ok = numeq(eq4_expected.subs(sig, sig_m), sp.Integer(0) * t) and numeq(
    eq4_expected.subs(sig, sig_p), sp.Integer(0) * t)
report("C2.6-roots", ok, "both roots solve the quadratic EOM")
# perturbative branch as a power series in g (fixed-point iteration of
# sigma = (V4 t^2 + g^2/20 W6 sigma^2)/K, truncated at g^5); the other root by Vieta
ORD = 6
Kinv = sum((g * V5 * t / (5 * V4)) ** k for k in range(ORD)) / V4   # 1/K to O(g^ORD)


def trunc(e: sp.Expr, n: int = ORD) -> sp.Expr:
    """Drop powers g^k with k >= n."""
    e = sp.expand(e)
    return sum(e.coeff(g, k) * g**k for k in range(n))


sig_pert = t**2
for _ in range(ORD):
    sig_pert = trunc((V4 * t**2 + g**2 / 20 * W6 * sig_pert**2) * Kinv)
report("C2.6-perturbative", sp.expand(trunc(eq4_expected.subs(sig, sig_pert) * K)) == 0,
       "series branch solves the EOM to O(g^6); starts at sigma = t^2")
c2 = sp.simplify(sig_pert.coeff(g, 2) - (V5**2 * t**4 / (25 * V4**2) + W6 * t**4 / (20 * V4)))
report("C2.6-coeff", c2 == 0 and sp.simplify(sig_pert.coeff(g, 1) - V5 * t**3 / (5 * V4)) == 0,
       "sigma_pert = t^2 + g V5 t^3/(5V4) + g^2 (V5^2/(25V4^2) + W6/(20V4)) t^4 + ...")
# numerical: sig_m (principal sqrt) agrees with the series at small g where K ~ V4 > 0
pt = {t: 0.7, V4: 1.3, V5: -0.4, V6: 0.9, CTT: 0.3, g: 1e-2}
report("C2.6-branch", abs(complex(sig_m.subs(pt)) - complex(sig_pert.subs(pt))) < 1e-10,
       "closed-form root sigma_- = the perturbative series (V4>0 sample)")
# non-perturbative root: g^2 sigma_+ -> 20 V4/W6 as g -> 0 (closed-form root, not Vieta)
lim = sp.limit((g**2 * sig_p).subs({V4: 1.3, V5: -0.4, V6: 0.9, CTT: 0.3, t: 0.7}), g, 0)
report("C2.6-nonpert", abs(complex(lim) - 20 * 1.3 / (0.9 - 1.2 * 0.3)) < 1e-10,
       f"g^2 sigma_+ -> {complex(lim).real:.6f} = 20 V4/W6")

# C2.7: eliminated sextic potential through g^4 on the perturbative branch
Veff4 = trunc(S4.subs(sig, sig_pert), 5)
target4 = Seff6 + (g**4 / 600 * (V5**2 / V4 - CTT)) * t**6
report("C2.7", sp.simplify(sp.expand(Veff4 - target4)) == 0,
       "V_eff^(4) = S_eff^(6) + g^4/600 (V5^2/V4 - C_TT) t^6 + O(g^5)")
report("C2.7-full", sp.simplify(sp.expand(Veff4 - Seff6).subs(CTT, V5**2 / V4)) == 0,
       "U = H (C_TT = V5^2/V4): matched through g^4")
expect_fail("C2.7", sp.simplify(sp.expand(Veff4 - Seff6)) == 0,
            "with C_TT generic the t^6 mismatch must be nonzero")

# C2.7-R19: one-field R19 exact rewriting (identity in sigma, any T)
Tt = sp.symbols("T6")
X = sig - t**2
v = V5 * t**3
K6 = K - g**2 / 10 * Tt * t**2
v6 = v + g / 4 * Tt * t**4
Xt6 = X - g / 5 * v6 / K6
S4T = S3 + g**4 / 720 * Tt * sig**3
rhs = (-g**2 / 24 * K6 * Xt6**2 + g**4 / 720 * Tt * X**3 + g**4 / 600 * v6**2 / K6
       + g**4 / 720 * (Tt * t**6 - V6 * t**6))
report("C2.7-R19", sp.simplify(S4T - Seff6 - rhs) == 0, "R19 (4) exact rewriting, one field")

# C2.8: g-scaling tau = g t, s = g^2 sigma: g^2 S_4 is g-independent
tau, s = sp.symbols("tau s")
scaled = sp.expand(g**2 * S4.subs({t: tau / g, sig: s / g**2}))
report("C2.8", g not in scaled.free_symbols, "g^2 S_4(tau/g, s/g^2) independent of g")


# C2.9: the S_4 fold. sigma_pert and sigma_+ collide where the discriminant of
# (2.11) vanishes: K^2 = (g^2/5) W6 V4 t^2, i.e. tau_fold = 5V4/(V5 +- sqrt(5 W6 V4)).
rnd = {V4: 1.7, V5: 0.6, V6: 2.1, CTT: 0.4, g: 0.3}       # W6 V4 > 0: real fold
for sgn in (1, -1):
    tf = (5 * V4 / (V5 + sgn * sp.sqrt(5 * W6 * V4)) / g).subs(rnd)
    dq = sp.discriminant(eq4_expected.subs(rnd).subs(t, tf), sig)
    roots = sp.Poly(eq4_expected.subs(rnd).subs(t, tf), sig).nroots()
    report(f"C2.9-fold{'+' if sgn > 0 else '-'}", abs(complex(dq)) < 1e-9 and abs(roots[0] - roots[1]) < 1e-5 * abs(roots[0]),  # double root: split ~ sqrt(eps)
           f"t_fold = {float(tf):.6f}: discriminant {complex(dq).real:.1e}, double root")
tf_wrong = (5 * V4 / V5 / g).subs(rnd)                      # t_pole is not a fold
expect_fail("C2.9-fold", abs(complex(sp.discriminant(eq4_expected.subs(rnd).subs(t, tf_wrong), sig))) < 1e-9,
            "t_pole must not be a zero of the discriminant when W6 != 0")
# at t_pole the S_4 sigma-EOM is V4 t^2 + (g^2/20) W6 sigma^2 = 0: real root iff W6 V4 < 0
def pole_roots_real(vals: dict) -> bool:
    e = eq4_expected.subs(t, t_pole).subs(vals)
    return all(abs(complex(r).imag) < 1e-12 for r in sp.Poly(e, sig).nroots())
neg = {V4: 1.7, V5: 0.6, V6: -2.1, CTT: 0.4, g: 0.3}        # W6 V4 < 0
report("C2.9-pole", pole_roots_real(neg) and sp.simplify(K.subs(t, t_pole)) == 0,
       "S_4 at t_pole: finite real saddle for W6 V4 < 0")
expect_fail("C2.9-pole", pole_roots_real(rnd), "W6 V4 > 0 (sign flipped): no real saddle at t_pole")

# ============================================================ C3: five-field
tt, dd = sp.symbols("t d")
h = sp.symbols("h0:5")          # {T^4},{T^3D},{T^2D^2},{TD^3},{D^4}
V4blk = sp.Matrix(3, 3, lambda i, j: h[i + j])          # Hankel, e1,e2,e3 basis
Pv = sp.Matrix([tt**2, 2 * tt * dd, dd**2])             # P = t^2 e1 + 2td e2 + d^2 e3
sv = sp.Matrix(sp.symbols("s1:4"))
S2q = -sp.Rational(1, 24) * (sv.T * V4blk * sv)[0] + sp.Rational(1, 12) * (sv.T * V4blk * Pv)[0]
sol5 = sp.solve([sp.diff(S2q, x) for x in sv], list(sv), dict=True)[0]
elim = sp.simplify(S2q.subs(sol5))
V4psi4 = sum(sp.binomial(4, k) * tt**(4 - k) * dd**k * h[k] for k in range(5))
ok = sp.simplify(elim - V4psi4 / 24) == 0 and all(sp.simplify(sol5[sv[i]] - Pv[i]) == 0 for i in range(3))
report("C3.1-sym", ok, "five-field quartic elimination = (1/4!) V4(Psi^4), sigma_* = (t^2, 2td, d^2)")
# break: Veronese-incomplete S = span(e1, e3)
idx = [0, 2]
V4r = V4blk.extract(idx, idx)
sr = sp.Matrix(sp.symbols("r1:3"))
S2r = -sp.Rational(1, 24) * (sr.T * V4r * sr)[0] + sp.Rational(1, 12) * (sr.T * V4blk.extract(idx, [0, 1, 2]) * Pv)[0]
solr = sp.solve([sp.diff(S2r, x) for x in sr], list(sr), dict=True)[0]
elimr = sp.simplify(S2r.subs(solr))
expect_fail("C3.1-sym", sp.simplify(elimr - V4psi4 / 24) == 0, "S = span(e1,e3) must not be exact")

# ---- generic-tensor model: H = R^N, U = first NU coordinates
N, NU = 4, 2


def sym_tensor(shape: tuple[int, ...]) -> np.ndarray:
    """Generic totally symmetric tensor."""
    T0 = rng.standard_normal(shape)
    out = np.zeros_like(T0)
    for perm in itertools.permutations(range(len(shape))):
        out += np.transpose(T0, perm)
    return out / math.factorial(len(shape))


T4, T5, T6n = sym_tensor((N,) * 4), sym_tensor((N,) * 5), sym_tensor((N,) * 6)
pairs = [(a, a) for a in range(N)] + [(a, b) for a in range(N) for b in range(a + 1, N)]
Lam = []
for a, b in pairs:
    E = np.zeros((N, N))
    if a == b:
        E[a, a] = 1.0
    else:
        E[a, b] = E[b, a] = 1 / np.sqrt(2)
    Lam.append(E)
Lam = np.array(Lam)                                  # orthonormal Sym^2 basis
V4S = np.einsum("abcd,Iab,Jcd->IJ", T4, Lam, Lam)
V5S = np.einsum("abcde,Iab,Jcd->IJe", T5, Lam, Lam)
V6S3 = np.einsum("abcdef,Iab,Jcd,Kef->IJK", T6n, Lam, Lam, Lam)
V4inv = np.linalg.inv(V4S)
C_raw = np.einsum("Kef,MIe,MN,NJf->IJK", Lam, V5S, V4inv, V5S)
T_C = (C_raw + C_raw.transpose(2, 1, 0) + C_raw.transpose(0, 2, 1)) / 3.0
W6S = V6S3 - 1.2 * T_C                                # full-theory W_6 (R19)
Sidx = [i for i, (a, b) in enumerate(pairs) if a < NU and b < NU]   # Sym^2 U
Cidx = [i for i in range(len(pairs)) if i not in Sidx]


def pvec(psi: np.ndarray) -> np.ndarray:
    return np.einsum("Iab,a,b->I", Lam, psi, psi)


def target(psi: np.ndarray, gg: float, order: int) -> float:
    """S_eff^(order) minus the shared A(Psi)."""
    out = gg**2 / 24 * np.einsum("abcd,a,b,c,d->", T4, psi, psi, psi, psi)
    if order >= 5:
        out += gg**3 / 120 * np.einsum("abcde,a,b,c,d,e->", T5, *(psi,) * 5)
    if order >= 6:
        out += gg**4 / 720 * np.einsum("abcdef,a,b,c,d,e,f->", T6n, *(psi,) * 6)
    return out


def cubic_action(sig: np.ndarray, psi: np.ndarray, gg: float, idx: list[int], order: int,
                 W6t: np.ndarray | None = None) -> float:
    """S_order minus A(Psi), Sigma restricted to span(Lam[idx])."""
    A4, A5 = V4S[np.ix_(idx, idx)], V5S[np.ix_(idx, idx)]
    out = -gg**2 / 24 * sig @ A4 @ sig + gg**2 / 12 * sig @ V4S[idx] @ pvec(psi)
    if order >= 3:
        out += gg**3 / 120 * np.einsum("IJe,I,J,e->", A5, sig, sig, psi)
    if order >= 4:
        Wr = W6S[np.ix_(idx, idx, idx)] if W6t is None else W6t
        out += gg**4 / 720 * np.einsum("IJK,I,J,K->", Wr, sig, sig, sig)
    return out


def saddle(psi: np.ndarray, gg: float, idx: list[int], order: int,
           W6t: np.ndarray | None = None) -> np.ndarray:
    """Newton on the sigma-EOM, started at the V4-projection of P (perturbative branch)."""
    A4 = V4S[np.ix_(idx, idx)]
    u = V4S[idx] @ pvec(psi)
    sig = np.linalg.solve(A4, u)
    A5 = V5S[np.ix_(idx, idx)]
    Wr = W6S[np.ix_(idx, idx, idx)] if W6t is None else W6t
    for _ in range(100):
        grad = -gg**2 / 12 * A4 @ sig + gg**2 / 12 * u
        hess = -gg**2 / 12 * A4
        if order >= 3:
            grad = grad + gg**3 / 60 * np.einsum("IJe,J,e->I", A5, sig, psi)
            hess = hess + gg**3 / 60 * np.einsum("IJe,e->IJ", A5, psi)
        if order >= 4:
            grad = grad + gg**4 / 240 * np.einsum("IJK,J,K->I", Wr, sig, sig)
            hess = hess + gg**4 / 120 * np.einsum("IJK,K->IJ", Wr, sig)
        step = np.linalg.solve(hess, grad)
        sig = sig - step
        if np.abs(step).max() < 1e-15 * (1 + np.abs(sig).max()):
            break
    return sig


psi = np.zeros(N)
psi[:NU] = rng.standard_normal(NU)
full = list(range(len(pairs)))

# C3.2: quartic exactness for S = Sym^2 U, generic tensors
gg = 0.7
s2 = saddle(psi, gg, Sidx, 2)
dev = cubic_action(s2, psi, gg, Sidx, 2) - target(psi, gg, 4)
report("C3.1-generic", abs(dev) < 1e-12 * gg**2, f"|S_2(sigma_*) - S_eff^(4)| = {abs(dev):.1e}")
badS = [Sidx[0], Sidx[1]] + Cidx[:1]      # drops the mixed pair, adds an off-U pair
s2b = saddle(psi, gg, badS, 2)
devb = cubic_action(s2b, psi, gg, badS, 2) - target(psi, gg, 4)
expect_fail("C3.1-generic", abs(devb) < 1e-12 * gg**2, f"Veronese-incomplete S: deviation {abs(devb):.1e}")

# objects of the deviation
p = pvec(psi)
vfull = np.einsum("IJe,J,e->I", V5S, p, psi)
A4 = V4S[np.ix_(Sidx, Sidx)]
vS = vfull[Sidx]
fb_trunc = vS @ np.linalg.solve(A4, vS)
fb_full = vfull @ V4inv @ vfull

# C3.2: S_3 truncated: mismatch/g^4 -> fb_trunc/600 (Newton saddle, independent of formula)
ratios = []
for gg in (1e-2, 5e-3):
    s3 = saddle(psi, gg, Sidx, 3)
    ratios.append((cubic_action(s3, psi, gg, Sidx, 3) - target(psi, gg, 5)) / gg**4)
r0 = 2 * ratios[1] - ratios[0]          # Richardson: remove the O(g) correction
ok = abs(r0 - fb_trunc / 600) < 1e-3 * abs(fb_trunc / 600)
report("C3.2", ok, f"mismatch/g^4 (g->0) = {r0:.6e} vs v_S A^-1 v_S/600 = {fb_trunc/600:.6e}")
expect_fail("C3.2", abs(r0 - fb_full / 600) < 1e-3 * abs(fb_full / 600),
            f"full-inverse feedback {fb_full/600:.6e} must not match")

# C3.3: Schur-complement formula
B = V4S[np.ix_(Sidx, Cidx)]
D = V4S[np.ix_(Cidx, Cidx)]
M = D - B.T @ np.linalg.solve(A4, B)
w = vfull[Cidx] - B.T @ np.linalg.solve(A4, vS)
schur = w @ np.linalg.solve(M, w)
ok = abs(fb_full - fb_trunc - schur) < 1e-10 * (1 + abs(fb_full)) and abs(schur) > 1e-3
report("C3.3", ok, f"vV4^-1v - v_S A^-1 v_S = {fb_full - fb_trunc:.6e}, w M^-1 w = {schur:.6e}")
expect_fail("C3.3", abs(fb_full - fb_trunc + schur) < 1e-10 * (1 + abs(fb_full)), "sign flip")

# C3.4: truncated S_4 (full-theory W_6): mismatch/g^4 -> -(w M^-1 w)/600; full: O(g^5)
rat = []
for gg in (1e-2, 5e-3):
    s4 = saddle(psi, gg, Sidx, 4)
    rat.append((cubic_action(s4, psi, gg, Sidx, 4) - target(psi, gg, 6)) / gg**4)
r0 = 2 * rat[1] - rat[0]
ok = abs(r0 + schur / 600) < 1e-3 * abs(schur / 600)
report("C3.4", ok, f"truncated S_4 mismatch/g^4 (g->0) = {r0:.6e} vs -wM^-1w/600 = {-schur/600:.6e}")
expect_fail("C3.4", abs(r0 - fb_trunc / 600) < 1e-3 * abs(fb_trunc / 600),
            "the S_3 value v_S A^-1 v_S/600 must not survive at S_4")
rf = []
for gg in (1e-2, 5e-3):
    s4f = saddle(psi, gg, full, 4)
    rf.append(abs(cubic_action(s4f, psi, gg, full, 4) - target(psi, gg, 6)))
slope = math.log(rf[0] / rf[1]) / math.log(2)
report("C3.4-full", 4.6 < slope < 5.4, f"S = Sym^2 H: log-slope {slope:.3f} (expected 5, R19)")

# C3.6: S-consistent composite C_S (A^-1 = (V4|_S)^-1, all legs in U):
# W6^(S) = V6|_S - (6/5) C_S removes the O(g^4) Schur deviation of C3.4
Ainv = np.linalg.inv(A4)
V5SS = V5S[np.ix_(Sidx, Sidx)]                       # V5(e_I, e_M, a), I, M in S
LamS = Lam[Sidx]
CS_raw = np.einsum("Kef,MIe,MN,NJf->IJK", LamS, V5SS, Ainv, V5SS)
CS = (CS_raw + CS_raw.transpose(2, 1, 0) + CS_raw.transpose(0, 2, 1)) / 3.0
W6_Sc = V6S3[np.ix_(Sidx, Sidx, Sidx)] - 1.2 * CS
cs_val = np.einsum("IJK,I,J,K->", CS, p[Sidx], p[Sidx], p[Sidx])
report("C3.6-CS", abs(cs_val - fb_trunc) < 1e-10 * (1 + abs(fb_trunc)),
       f"C_S(P,P,P) = {cs_val:.6e} = v_S A^-1 v_S = {fb_trunc:.6e}")
rs, rfc = [], []
for gg in (2e-3, 1e-3):
    ss = saddle(psi, gg, Sidx, 4, W6_Sc)
    rs.append((cubic_action(ss, psi, gg, Sidx, 4, W6_Sc) - target(psi, gg, 6)) / gg**4)
    sf = saddle(psi, gg, Sidx, 4)
    rfc.append((cubic_action(sf, psi, gg, Sidx, 4) - target(psi, gg, 6)) / gg**4)
r0s, r0f = 2 * rs[1] - rs[0], 2 * rfc[1] - rfc[0]
report("C3.6", abs(r0s) < 1e-3 * abs(schur / 600),
       f"W6^(S): mismatch/g^4 (g->0) = {r0s:.2e} (Schur scale {schur/600:.3e})")
expect_fail("C3.6", abs(r0f) < 1e-3 * abs(schur / 600),
            f"full-C W6 restores the Schur term: {r0f:.6e}")

# C3.5: enlarging S by x = V4^{-1} v kills the Schur deviation (w = 0)
x = V4inv @ vfull
Qb = np.zeros((len(pairs), len(Sidx) + 1))
Qb[Sidx, range(len(Sidx))] = 1.0
Qb[:, -1] = x
Qo, _ = np.linalg.qr(Qb)                      # basis of Sym^2 U + span(x)
Aq = Qo.T @ V4S @ Qo
vq = Qo.T @ vfull
fb_enl = vq @ np.linalg.solve(Aq, vq)
report("C3.5", abs(fb_enl - fb_full) < 1e-10 * (1 + abs(fb_full)),
       f"S = Sym^2 U + span(V4^-1 v): v_S A^-1 v_S = {fb_enl:.6e} = vV4^-1v = {fb_full:.6e}")
Qb[:, -1] = rng.standard_normal(len(pairs))
Qo, _ = np.linalg.qr(Qb)
vq = Qo.T @ vfull
fb_rand = vq @ np.linalg.solve(Qo.T @ V4S @ Qo, vq)
expect_fail("C3.5", abs(fb_rand - fb_full) < 1e-10 * (1 + abs(fb_full)),
            "a random extra direction must not close the deviation")

# C3.2-exact: five-field quintic, symbolic g, random rational tensors restricted to U
q = [sp.Rational(int(x), 7) for x in rng.integers(-20, 21, 6)]   # {T^5-k D^k}
h_num = [sp.Rational(int(x), 5) for x in rng.integers(-20, 21, 5)]
V4n = sp.Matrix(3, 3, lambda i, j: h_num[i + j])
V5blk = [sp.Matrix(3, 3, lambda i, j: q[i + j] * tt + q[i + j + 1] * dd)]  # V5(e_i,e_j,Psi)
S3q = (-g**2 / 24 * (sv.T * V4n * sv)[0] + g**2 / 12 * (sv.T * V4n * Pv)[0]
       + g**3 / 120 * (sv.T * V5blk[0] * sv)[0])
sol3 = sp.solve([sp.diff(S3q, x) for x in sv], list(sv), dict=True)[0]
tv, dv = sp.Rational(3, 7), sp.Rational(-5, 11)
elim3 = sp.simplify(S3q.subs(sol3).subs({tt: tv, dd: dv}))
ser3 = sp.series(elim3, g, 0, 6).removeO()
V4v = sum(sp.binomial(4, k) * tv**(4 - k) * dv**k * h_num[k] for k in range(5))
V5v = sum(sp.binomial(5, k) * tv**(5 - k) * dv**k * q[k] for k in range(6))
ok = sp.simplify(ser3.coeff(g, 2) - V4v / 24) == 0 and sp.simplify(ser3.coeff(g, 3) - V5v / 120) == 0
PvN = Pv.subs({tt: tv, dd: dv})
vS5 = V5blk[0].subs({tt: tv, dd: dv}) * PvN
ok4 = sp.simplify(ser3.coeff(g, 4) - (vS5.T * V4n.inv() * vS5)[0] / 600) == 0
report("C3.2-exact", ok and ok4, "five-field S_3: [g^2],[g^3] = target, [g^4] = v_S A^-1 v_S/600 (exact)")

# ============================================================ C4: Part B, EOM components off (U, S)
# Exact Taylor coefficients in g at fixed Psi in U: g is nilpotent of order KS+1 (truncated
# power series, the one-variable form of the MD nilpotent technique of verify-gauge-algebra-ogs4).
# Sigma-EOM normalised as e = V4 s - V4 p - (g/5) V5(s,.,Psi) - (g^2/20) W6(s,s,.)  (= -12/g^2 dS/dSigma).
# Psi-EOM E_x = V2 Psi + (g/2) V3(Psi,Psi,x) + (g^2/6) V4(s,Psi,x) + (g^3/120) V5(s,s,x).
KS = 6
N4, NU4, NUP4 = 6, 2, 2          # H = R^6, U = first 2 coords; level-axis instance: U' = coords 2,3


def c4_model(seed: int, parity: np.ndarray | None, rule: str = "z2",
             break_n: int | None = None, a4: bool = True, v5zero: bool = False) -> dict:
    """
    Build random symmetric V2..V6 on R^N4; V2 block-diagonal on U + U^perp (A4).

    parity: +1/-1 per coordinate; rule 'z2' keeps components with an even number of odd
    legs, rule 'oneleg' removes only components with exactly one odd leg (Sen-type rule).
    break_n: the tensor V_n left unprojected (one broken tensor).
    """
    r = np.random.default_rng(seed)

    def symt(k: int) -> np.ndarray:
        """Generate a generic totally symmetric rank-k tensor."""
        T0 = r.standard_normal((N4,) * k)
        out = np.zeros_like(T0)
        for perm in itertools.permutations(range(k)):
            out += np.transpose(T0, perm)
        return out / math.factorial(k)

    Ts = {k: symt(k) for k in range(2, 7)}
    if a4:
        Ts[2][:NU4, NU4:] = 0.0
        Ts[2][NU4:, :NU4] = 0.0                  # A4: V2(U, U^perp) = 0
    if v5zero:
        Ts[5] = 0.0 * Ts[5]
    if parity is not None:
        for k in range(2, 7):
            if k == break_n:
                continue
            nodd = sum(np.ix_(*[(parity < 0).astype(int)] * k))   # number of odd legs
            keep = (nodd % 2 == 0) if rule == "z2" else (nodd != 1)
            Ts[k] = Ts[k] * keep
    return build_c4(Ts)


def build_c4(Ts: dict) -> dict:
    """Assemble Sym^2 blocks, the full-C W6 (R19) and the S-consistent W6^(S) (057 section 1)."""
    prs = [(a, a) for a in range(N4)] + [(a, b) for a in range(N4) for b in range(a + 1, N4)]
    L = []
    for a, b in prs:
        E = np.zeros((N4, N4))
        if a == b:
            E[a, a] = 1.0
        else:
            E[a, b] = E[b, a] = 1 / np.sqrt(2)
        L.append(E)
    L = np.array(L)
    m = {"T": Ts, "L": L, "pairs": prs}
    m["V4S"] = np.einsum("abcd,Iab,Jcd->IJ", Ts[4], L, L, optimize=True)
    m["V5S"] = np.einsum("abcde,Iab,Jcd->IJe", Ts[5], L, L, optimize=True)
    m["V6S3"] = np.einsum("abcdef,Iab,Jcd,Kef->IJK", Ts[6], L, L, L, optimize=True)
    m["S"] = [i for i, (a, b) in enumerate(prs) if a < NU4 and b < NU4]
    m["C"] = [i for i in range(len(prs)) if i not in m["S"]]
    m["mixed"] = [i for i, (a, b) in enumerate(prs) if a < NU4 <= b]          # U (.) U^perp
    m["perp2"] = [i for i, (a, b) in enumerate(prs) if a >= NU4]               # Sym^2 U^perp
    V4inv = np.linalg.inv(m["V4S"])
    Cr = np.einsum("Kef,MIe,MN,NJf->IJK", L, m["V5S"], V4inv, m["V5S"], optimize=True)
    m["TC"] = (Cr + Cr.transpose(2, 1, 0) + Cr.transpose(0, 2, 1)) / 3.0
    m["W6full"] = m["V6S3"] - 1.2 * m["TC"]
    S = m["S"]
    Ai = np.linalg.inv(m["V4S"][np.ix_(S, S)])
    V5SS = m["V5S"][np.ix_(S, S)]
    Csr = np.einsum("Kef,MIe,MN,NJf->IJK", L[S], V5SS, Ai, V5SS, optimize=True)
    CSs = (Csr + Csr.transpose(2, 1, 0) + Csr.transpose(0, 2, 1)) / 3.0
    D = len(prs)
    W6S = np.zeros((D, D, D))
    W6S[np.ix_(S, S, S)] = m["V6S3"][np.ix_(S, S, S)] - 1.2 * CSs
    CSe = np.zeros((D, D, D))
    CSe[np.ix_(S, S, S)] = CSs
    m["W6S"], m["CSe"] = W6S, CSe
    return m


def c4_sigma(m: dict, psi: np.ndarray, idx: list[int], order: int, W6: np.ndarray) -> list:
    """Taylor coefficients s_0..s_KS of the perturbative Sigma-saddle on span(idx)."""
    D = len(m["pairs"])
    p = np.einsum("Iab,a,b->I", m["L"], psi, psi)
    A = m["V4S"][np.ix_(idx, idx)]
    Wb = (m["V5S"] @ psi)[np.ix_(idx, idx)]
    W6b = W6[np.ix_(idx, idx, idx)]
    s = [np.linalg.solve(A, m["V4S"][idx] @ p)]
    for k in range(1, KS + 1):
        rhs = np.zeros(len(idx))
        if order >= 3:
            rhs += Wb @ s[k - 1] / 5
        if order >= 4:
            for i in range(0, k - 1):
                rhs += np.einsum("IJK,I,J->K", W6b, s[i], s[k - 2 - i]) / 20
        s.append(np.linalg.solve(A, rhs))
    out = []
    for sk in s:
        v = np.zeros(D)
        v[idx] = sk
        out.append(v)
    return out


def c4_eoms(m: dict, psi: np.ndarray, s: list, order: int, W6u: np.ndarray) -> tuple:
    """Series of the untruncated Sigma-EOM covector e_k and Psi-EOM E_k at (psi, s)."""
    T, L = m["T"], m["L"]
    p = np.einsum("Iab,a,b->I", L, psi, psi)
    W = m["V5S"] @ psi
    e, E = [], []
    for k in range(KS + 1):
        ek = m["V4S"] @ s[k] - (p @ m["V4S"] if k == 0 else 0.0)
        if order >= 3 and k >= 1:
            ek = ek - W @ s[k - 1] / 5
        if order >= 4:
            for i in range(0, k - 1):
                ek = ek - np.einsum("IJK,I,J->K", W6u, s[i], s[k - 2 - i]) / 20
        e.append(ek)
        Ek = np.zeros(N4)
        if k == 0:
            Ek += T[2] @ psi
        if k == 1:
            Ek += np.einsum("abx,a,b->x", T[3], psi, psi) / 2
        if k >= 2:
            sig = np.einsum("I,Iab->ab", s[k - 2], L)
            Ek += np.einsum("abcx,ab,c->x", T[4], sig, psi) / 6
        if order >= 3 and k >= 3:
            for i in range(0, k - 2):
                Ek += np.einsum("IJx,I,J->x", m["V5S"], s[i], s[k - 3 - i]) / 120
        E.append(Ek)
    return e, E


def c4_pot(m: dict, psi: np.ndarray, s: list, order: int, W6: np.ndarray) -> np.ndarray:
    """Taylor coefficients of S_order - A(Psi) at (psi, s)."""
    p = np.einsum("Iab,a,b->I", m["L"], psi, psi)
    W = m["V5S"] @ psi
    c = np.zeros(KS + 1)
    for k in range(KS + 1):
        for i in range(k - 1):
            j = k - 2 - i
            c[k] += -s[i] @ m["V4S"] @ s[j] / 24
        if k >= 2:
            c[k] += s[k - 2] @ m["V4S"] @ p / 12
        if order >= 3:
            for i in range(k - 2):
                c[k] += s[i] @ W @ s[k - 3 - i] / 120
        if order >= 4:
            for i in range(k - 3):
                for j in range(k - 3 - i):
                    c[k] += np.einsum("IJK,I,J,K->", W6, s[i], s[j], s[k - 4 - i - j]) / 720
    return c


def c4_target_E(m: dict, psi: np.ndarray, n: int) -> list:
    """Taylor coefficients of d/dPsi S_eff^(n): [g^(k-2)] = V_k(Psi^(k-1), .)/(k-1)!."""
    out = []
    for k in range(2, KS + 3):
        if k <= min(n, 6):
            term = m["T"][k]
            for _ in range(k - 1):
                term = np.tensordot(psi, term, axes=(0, 0))
            out.append(term / math.factorial(k - 1))
        else:
            out.append(np.zeros(N4))
    return out[: KS + 1]


def c4_w(m: dict, psi: np.ndarray) -> tuple:
    """057 (3.4): w = v_c - B^T A^-1 v_S, M = D_c - B^T A^-1 B (from the definitions)."""
    S, Cc = m["S"], m["C"]
    p = np.einsum("Iab,a,b->I", m["L"], psi, psi)
    v = np.einsum("IJe,J,e->I", m["V5S"], p, psi)
    A = m["V4S"][np.ix_(S, S)]
    B = m["V4S"][np.ix_(S, Cc)]
    Dc = m["V4S"][np.ix_(Cc, Cc)]
    w = v[Cc] - B.T @ np.linalg.solve(A, v[S])
    M = Dc - B.T @ np.linalg.solve(A, B)
    wf = np.zeros(len(m["pairs"]))
    wf[Cc] = w
    return wf, M, w


def lam_pair(m: dict, psi: np.ndarray, x: np.ndarray) -> np.ndarray:
    """Sym^2 components of Psi (x) x in the orthonormal basis."""
    return np.einsum("Iab,a,b->I", m["L"], psi, x)


def c4_psi(seed: int) -> np.ndarray:
    """Draw a unit vector Psi in U."""
    r = np.random.default_rng(seed + 7)
    psi = np.zeros(N4)
    psi[:NU4] = r.standard_normal(NU4)
    return psi / np.linalg.norm(psi)              # unit Psi: all Taylor coefficients O(1)


C4_SEEDS = [SEED + 1, SEED + 2, SEED + 3]
print(f"C4 seeds = {C4_SEEDS}, N = {N4}, dim U = {NU4}, Taylor order {KS}")

PERP = list(range(NU4, N4))


def c4_theories(m: dict) -> dict:
    """(order, W6 used in the truncation, W6 of the untruncated EOM) per theory."""
    return {"S2": (2, None, None), "S3": (3, None, None),
            "S4C": (4, m["W6full"], m["W6full"]), "S4S": (4, m["W6S"], m["W6full"])}


def c4_run(m: dict, psi: np.ndarray, name: str, idx: list[int] | None = None) -> tuple:
    """Return saddle, EOM and potential series, truncated (idx = S) or relaxed (idx = all)."""
    order, W6t, W6u = c4_theories(m)[name]
    if idx is None:
        idx = m["S"]
    else:
        W6t = W6u                                   # relaxed: the untruncated theory itself
    D = len(m["pairs"])
    z = np.zeros((D, D, D))
    s = c4_sigma(m, psi, idx, order, W6t if W6t is not None else z)
    e, E = c4_eoms(m, psi, s, order, W6u if W6u is not None else z)
    V = c4_pot(m, psi, s, order, W6t if W6t is not None else z)
    return s, e, E, V


def first_nonzero(arrs: list, tol: float) -> int:
    """Lowest k with |arrs[k]| > tol (KS + 1 if none)."""
    for k, a in enumerate(arrs):
        if np.max(np.abs(a)) > tol:
            return k
    return KS + 1


TOL = 1e-9
PAR_U = np.array([1] * NU4 + [-1] * (N4 - NU4))                  # U even, U^perp odd
PAR_L = np.array([1] * (NU4 + NUP4) + [-1] * (N4 - NU4 - NUP4))  # U + U' even, N odd

ok = {k: True for k in ["C4.1-g0", "C4.1-g1", "C4.1-S2", "C4.1-g3", "C4.1-g3b",
                        "C4.2-S2", "C4.2-g0", "C4.2-g1", "C4.2-g1b", "C4.2-V5zero",
                        "C4.3-a", "C4.3-b1", "C4.3-b2", "C4.3-relaxed", "C4.3-oneleg-a",
                        "C4.3-oneleg-b1", "C4.3-oneleg-S4", "C4.3-oneleg-relaxed",
                        "C4.3-level", "C4.3-break3", "C4.3-break4", "C4.3-break5",
                        "C4.3-break6", "C4.1-A4b",
                        "C4.4-S2", "C4.4-S3", "C4.4-S4C", "C4.4-S4S", "C4.4-S4Sb",
                        "C4.4-response", "C4.4-finite", "C4.4-finiteb", "C4.4-cS"]}
BREAKS = ["C4.1-g3b", "C4.2-g1b", "C4.1-A4b", "C4.4-S4Sb", "C4.4-finiteb"]
for kb in BREAKS:
    ok[kb] = False                                  # break legs: OR over seeds and theories
info: dict[str, str] = {}
for sd in C4_SEEDS:
    psi = c4_psi(sd)
    G = c4_model(sd, None)
    wf, M, w = c4_w(G, psi)
    schur = w @ np.linalg.solve(M, w)
    # scale of the Schur term without its cancellations (M is indefinite)
    sscale = np.linalg.norm(w) ** 2 * np.linalg.norm(np.linalg.inv(M), 2) / 600
    tgt4, tgt5 = c4_target_E(G, psi, 4), c4_target_E(G, psi, 5)
    runs = {nm: c4_run(G, psi, nm) for nm in ["S2", "S3", "S4C", "S4S"]}
    for nm, (_s, e, E, _V) in runs.items():
        Ex = [Ek[PERP] for Ek in E]
        ok["C4.1-g0"] &= np.max(np.abs(Ex[0])) < TOL
        ok["C4.1-g1"] &= (np.allclose(Ex[1], tgt4[1][PERP], atol=TOL)
                          and np.max(np.abs(Ex[1])) > 1e-3)
        if nm == "S2":
            ok["C4.1-S2"] &= all(np.allclose(E[k], tgt4[k], atol=TOL) for k in range(KS + 1))
            ok["C4.2-S2"] &= max(np.max(np.abs(ek[G["C"]])) for ek in e) < TOL
        else:
            pred = np.array([-(wf @ lam_pair(G, psi, np.eye(N4)[x])) / 30 for x in PERP])
            d3 = Ex[3] - tgt5[3][PERP]
            ok["C4.1-g3"] &= np.allclose(d3, pred, atol=TOL) and np.max(np.abs(pred)) > 1e-3
            ok["C4.1-g3b"] |= np.allclose(d3, -pred, atol=TOL)
            ok["C4.2-g0"] &= np.max(np.abs(e[0][G["C"]])) < TOL
            ok["C4.2-g1"] &= np.allclose(e[1][G["C"]], -w / 5, atol=TOL) and np.max(np.abs(w)) > 1e-3
            ok["C4.2-g1b"] |= np.allclose(e[1][G["C"]], w / 5, atol=TOL)
    # V5 -> 0: the S^c source disappears at S_3 (all orders)
    G0 = c4_model(sd, None, v5zero=True)
    _, e0, _, _ = c4_run(G0, psi, "S3")
    ok["C4.2-V5zero"] &= max(np.max(np.abs(ek[G0["C"]])) for ek in e0) < TOL
    # A4 break: V2(U, U^perp) != 0 turns (a) on at O(1)
    GA = c4_model(sd, None, a4=False)
    _, _, EA, _ = c4_run(GA, psi, "S3")
    ok["C4.1-A4b"] |= np.max(np.abs(EA[0][PERP])) < TOL
    # ---- C4.4 absorption
    for nm in ["S2", "S3", "S4C", "S4S"]:
        Vt = runs[nm][3]
        Vf = c4_run(G, psi, nm, idx=list(range(len(G["pairs"]))))[3]
        dV = Vf - Vt
        sc = sscale
        if nm == "S2":
            ok["C4.4-S2"] &= np.max(np.abs(dV)) < TOL
        elif nm in ("S3", "S4C"):
            ok[f"C4.4-{nm}"] &= (np.max(np.abs(dV[:4])) < TOL * (1 + sc)
                                 and abs(dV[4] - schur / 600) < 1e-8 * (1 + sc)
                                 and np.linalg.norm(w) > 1e-3)
        else:
            ok["C4.4-S4S"] &= np.max(np.abs(dV[:5])) < 1e-8 * (1 + sc)
            ok["C4.4-S4Sb"] |= abs(dV[4] - schur / 600) < 1e-8 * (1 + sc)
            info["S4S"] = f"[g^4] = {dV[4]:.2e} vs Schur/600 = {schur / 600:.4e}"
    e1c = runs["S3"][1][1][G["C"]]
    ok["C4.4-response"] &= abs(e1c @ np.linalg.solve(M, e1c) / 24 - schur / 600) < 1e-8 * (1 + abs(schur))
    # (c) for W6^(S): untruncated Sigma-EOM along S violated at relative O(g^2)
    p = np.einsum("Iab,a,b->I", G["L"], psi, psi)
    predc = 3 / 50 * np.einsum("IJK,I,J->K", G["TC"] - G["CSe"], p, p)[G["S"]]
    eS = runs["S4S"][1]
    ok["C4.4-cS"] &= (max(np.max(np.abs(eS[k][G["S"]])) for k in range(2)) < TOL
                      and np.allclose(eS[2][G["S"]], predc, atol=1e-8) and np.max(np.abs(predc)) > 1e-3)
    # finite-g, series-independent: exact linear saddles of S_3, full vs truncated
    S = G["S"]
    Wm = G["V5S"] @ psi
    rat = []

    def act3(sv: np.ndarray, gg: float, V4S_: np.ndarray, p_: np.ndarray, Wm_: np.ndarray) -> float:
        """S_3 minus A(Psi) at Sigma = sv (full Sym^2 H coordinates)."""
        return (-gg**2 / 24 * sv @ V4S_ @ sv + gg**2 / 12 * sv @ V4S_ @ p_
                + gg**3 / 120 * sv @ Wm_ @ sv)

    for gg in (2e-3, 1e-3):
        sf = np.linalg.solve(G["V4S"] - gg / 5 * Wm, G["V4S"] @ p)
        st = np.zeros_like(sf)
        st[S] = np.linalg.solve(G["V4S"][np.ix_(S, S)] - gg / 5 * Wm[np.ix_(S, S)], G["V4S"][S] @ p)
        ec = (G["V4S"] @ st - G["V4S"] @ p - gg / 5 * Wm @ st)[G["C"]]
        rat.append(((act3(sf, gg, G["V4S"], p, Wm) - act3(st, gg, G["V4S"], p, Wm)) / gg**4, gg**2 / 24 * ec @ np.linalg.solve(M, ec) / gg**4))
    # exact at S_3 (quadratic in Sigma): relaxation energy = (g^2/24) e_c^T (K_Psi^-1)_cc e_c
    # at a finite coupling g = 0.3 (vacuum-scale fields: no expansion in g)
    gx = 0.3
    Kf = G["V4S"] - gx / 5 * Wm
    sfx = np.linalg.solve(Kf, G["V4S"] @ p)
    stx = np.zeros_like(sfx)
    stx[S] = np.linalg.solve(Kf[np.ix_(S, S)], G["V4S"][S] @ p)
    ecx = (Kf @ stx - G["V4S"] @ p)[G["C"]]
    Kicc = np.linalg.inv(Kf)[np.ix_(G["C"], G["C"])]
    dVx = act3(sfx, gx, G["V4S"], p, Wm) - act3(stx, gx, G["V4S"], p, Wm)
    rx = gx**2 / 24 * ecx @ Kicc @ ecx
    ok.setdefault("C4.4-exact", True)
    ok["C4.4-exact"] &= abs(dVx - rx) < 1e-10 * (1 + abs(dVx)) and abs(dVx) > 1e-8
    ok.setdefault("C4.4-exactb", False)
    ok["C4.4-exactb"] |= abs(dVx - gx**4 / 600 * schur) < 1e-10 * (1 + abs(dVx))
    info.setdefault("exact", "")
    info["exact"] += f" {dVx:.6e} vs {rx:.6e};"
    rich = 2 * rat[1][0] - rat[0][0]
    richr = 2 * rat[1][1] - rat[0][1]
    ok["C4.4-finite"] &= (abs(rich - schur / 600) < 1e-5 * sscale
                          and abs(richr - schur / 600) < 1e-5 * sscale)
    ok["C4.4-finiteb"] |= abs(rich + schur / 600) < 1e-5 * sscale
    info.setdefault("finite", "")
    info["finite"] += f" seed {sd}: {rich:.6f} vs {schur / 600:.6f} (scale {sscale:.3f});"
    # ---- C4.3 universal instance: Z_2 with U even, U^perp odd
    Z = c4_model(sd, PAR_U)
    wfz, Mz, wz = c4_w(Z, psi)
    for nm in ["S2", "S3", "S4C", "S4S"]:
        s, e, E, V = c4_run(Z, psi, nm)
        ok["C4.3-a"] &= max(np.max(np.abs(Ek[PERP])) for Ek in E) < TOL
        ok["C4.3-b1"] &= max(np.max(np.abs(ek[Z["mixed"]])) for ek in e) < TOL
        if nm != "S2":
            ok["C4.3-b2"] &= (np.allclose(e[1][Z["perp2"]], -wfz[Z["perp2"]] / 5, atol=TOL)
                              and np.max(np.abs(wfz[Z["perp2"]])) > 1e-3)
            sr, er, Er, _ = c4_run(Z, psi, nm, idx=list(range(len(Z["pairs"]))))
            ok["C4.3-relaxed"] &= (max(np.max(np.abs(Ek[PERP])) for Ek in Er) < TOL
                                   and max(np.max(np.abs(sk[Z["mixed"]])) for sk in sr) < TOL)
    # one broken tensor V_n: (a) switches on at exactly O(g^(n-2)); V_6 broken: (b1) at O(g^2)
    for n in (3, 4, 5):
        Zb = c4_model(sd, PAR_U, break_n=n)
        _, _, Eb, _ = c4_run(Zb, psi, "S4C")
        ok[f"C4.3-break{n}"] &= first_nonzero([Ek[PERP] for Ek in Eb], 1e-6) == n - 2
    Zb = c4_model(sd, PAR_U, break_n=6)
    _, eb, Eb, _ = c4_run(Zb, psi, "S4C")
    ok["C4.3-break6"] &= (first_nonzero([ek[Zb["mixed"]] for ek in eb], 1e-6) == 2
                          and first_nonzero([Ek[PERP] for Ek in Eb], 1e-6) == KS + 1)
    # one-leg (Sen-type) rule only
    OL = c4_model(sd, PAR_U, rule="oneleg")
    for nm in ["S2", "S3", "S4C", "S4S"]:
        s, e, E, V = c4_run(OL, psi, nm)
        ok["C4.3-oneleg-a"] &= max(np.max(np.abs(Ek[PERP])) for Ek in E) < TOL
        if nm in ("S2", "S3"):
            ok["C4.3-oneleg-b1"] &= max(np.max(np.abs(ek[OL["mixed"]])) for ek in e) < TOL
        else:
            ok["C4.3-oneleg-S4"] &= first_nonzero([ek[OL["mixed"]] for ek in e], 1e-6) == 2
            # (4.6): coefficient (3/50) C(P,P,.) on U.U^perp
            pO = np.einsum("Iab,a,b->I", OL["L"], psi, psi)
            pr6 = 3 / 50 * np.einsum("IJK,I,J->K", OL["TC"], pO, pO)[OL["mixed"]]
            ok["C4.3-oneleg-S4"] &= np.allclose(e[2][OL["mixed"]], pr6, atol=1e-9)
    fo = {}
    for nm in ["S3", "S4C"]:
        _, _, Er, _ = c4_run(OL, psi, nm, idx=list(range(len(OL["pairs"]))))
        fo[nm] = first_nonzero([Ek[PERP] for Ek in Er], 1e-6)
    ok["C4.3-oneleg-relaxed"] &= fo["S3"] == 4 and fo["S4C"] == 5
    # (4.7): [g^4] of the relaxed S_3 Psi-EOM along x = (1/300) (d_x v)^T V4^-1 v
    _, _, Er3, _ = c4_run(OL, psi, "S3", idx=list(range(len(OL["pairs"]))))
    pO = np.einsum("Iab,a,b->I", OL["L"], psi, psi)
    vO = np.einsum("IJe,J,e->I", OL["V5S"], pO, psi)
    pr7 = []
    for xx in PERP:
        ex = np.eye(N4)[xx]
        dv = (2 * np.einsum("IJe,J,e->I", OL["V5S"], lam_pair(OL, psi, ex), psi)
              + np.einsum("IJe,J,e->I", OL["V5S"], pO, ex))
        pr7.append(dv @ np.linalg.solve(OL["V4S"], vO) / 300)
    ok["C4.3-oneleg-relaxed"] &= np.allclose(Er3[4][PERP], np.array(pr7), atol=1e-9)
    ok.setdefault("C4.3-oneleg-relaxedb", False)
    ok["C4.3-oneleg-relaxedb"] |= np.allclose(Er3[4][PERP], np.array(pr7) / 2, atol=1e-9)
    info.setdefault("oneleg", "")
    info["oneleg"] += f" {fo};"
    # level axis: U + U' even (universal), N odd; U = first NU4 coords only
    Lm = c4_model(sd, PAR_L)
    _, _, El, _ = c4_run(Lm, psi, "S4S")
    Up, Nn = list(range(NU4, NU4 + NUP4)), list(range(NU4 + NUP4, N4))
    ok["C4.3-level"] &= (max(np.max(np.abs(Ek[Nn])) for Ek in El) < TOL
                         and np.max(np.abs(El[1][Up])) > 1e-3)

report("C4.1-g0", ok["C4.1-g0"], "generic: [g^0] of Psi-EOM along U^perp = 0 (A4), S_2..S_4")
report("C4.1-g1", ok["C4.1-g1"], "generic: [g^1] = V3(Psi,Psi,.)/2 on U^perp, nonzero, S_2..S_4")
expect_fail("C4.1-A4", ok["C4.1-A4b"], "V2(U,U^perp) != 0 must switch (a) on at O(1)")
report("C4.1-S2", ok["C4.1-S2"], "S_2: Psi-EOM = d S_eff^(4) at all orders (level-truncation residual)")
report("C4.1-g3", ok["C4.1-g3"], "S_3, S_4: [g^3] of (a) minus d S_eff^(5) = -(1/30) w(Psi.x)")
expect_fail("C4.1-g3", ok["C4.1-g3b"], "sign-flipped prediction must fail")
report("C4.2-S2", ok["C4.2-S2"], "S_2: Sigma-EOM along S^c vanishes at all orders")
report("C4.2-g0", ok["C4.2-g0"], "S_3, S_4: [g^0] of Sigma-EOM along S^c = 0")
report("C4.2-g1", ok["C4.2-g1"], "S_3, S_4 (both W6): [g^1] = -w/5, w of 057 (3.4), nonzero")
expect_fail("C4.2-g1", ok["C4.2-g1b"], "+w/5 must fail")
report("C4.2-V5zero", ok["C4.2-V5zero"], "V5 -> 0: S^c component of the Sigma-EOM vanishes at all orders (S_3)")
report("C4.3-a", ok["C4.3-a"], "Z_2-universal U: Psi-EOM along U^perp = 0 at all orders, S_2..S_4")
report("C4.3-b1", ok["C4.3-b1"], "Z_2-universal U: Sigma-EOM along U.U^perp = 0 at all orders, S_2..S_4")
report("C4.3-b2", ok["C4.3-b2"], "Z_2-universal U: Sigma-EOM along Sym^2 U^perp = -w/5 at [g^1], not removed")
report("C4.3-relaxed", ok["C4.3-relaxed"], "Z_2: relaxed saddle stays even, (a) = 0 at all orders")
for n in (3, 4, 5):
    report(f"C4.3-break{n}", ok[f"C4.3-break{n}"], f"Z_2 broken in V{n} only: (a) first nonzero at [g^{n - 2}]")
report("C4.3-break6", ok["C4.3-break6"], "Z_2 broken in V6 only: (a) stays 0, (b1) first nonzero at [g^2] (S_4)")
report("C4.3-oneleg-a", ok["C4.3-oneleg-a"], "one-leg rule: (a) = 0 at all orders, S_2..S_4")
report("C4.3-oneleg-b1", ok["C4.3-oneleg-b1"], "one-leg rule: (b1) = 0 at all orders at S_2, S_3")
report("C4.3-oneleg-S4", ok["C4.3-oneleg-S4"], "one-leg rule: (b1) first nonzero at [g^2] at S_4, = (3/50) C(P,P,.) (4.6)")
report("C4.3-oneleg-relaxed", ok["C4.3-oneleg-relaxed"],
       f"one-leg rule, relaxed: (a) first nonzero at [g^4] (S_3, = (4.7)), [g^5] (S_4) {info['oneleg']}")
expect_fail("C4.3-oneleg-relaxed", ok["C4.3-oneleg-relaxedb"], "(4.7) with a factor 1/2 must fail")
report("C4.3-level", ok["C4.3-level"], "U + U' universal: (a) = 0 along N, nonzero at [g^1] along U' (level axis)")
report("C4.4-S2", ok["C4.4-S2"], "S_2: relaxing S^c changes nothing (all orders)")
report("C4.4-S3", ok["C4.4-S3"], "S_3: V_full - V_trunc = 0 through g^3, [g^4] = w M^-1 w/600")
report("C4.4-S4C", ok["C4.4-S4C"], "S_4 full-C: V_full - V_trunc = 0 through g^3, [g^4] = w M^-1 w/600")
report("C4.4-S4S", ok["C4.4-S4S"], f"S_4 W6^(S) vs R19 S_4: 0 through g^4 ({info['S4S']})")
expect_fail("C4.4-S4S", ok["C4.4-S4Sb"], "the Schur value must not be found at [g^4]")
report("C4.4-response", ok["C4.4-response"], "(1/24) e1_c M^-1 e1_c = w M^-1 w/600 (second-order response)")
report("C4.4-finite", ok["C4.4-finite"], f"finite g, exact S_3 saddles, Richardson:{info['finite']}")
expect_fail("C4.4-finite", ok["C4.4-finiteb"], "opposite sign must fail")
report("C4.4-exact", ok["C4.4-exact"],
       f"S_3, g = 0.3: V_full - V_trunc = (g^2/24) e_c (K^-1)_cc e_c exactly:{info['exact']}")
expect_fail("C4.4-exact", ok["C4.4-exactb"], "the leading Schur term alone must not be exact at g = 0.3")
report("C4.4-cS", ok["C4.4-cS"], "W6^(S): untruncated Sigma-EOM along S = (3/50)(C - C_S)(P,P,.) at [g^2]")

# ------------------------------------------------------------ summary
nf = sum(not ok for _, ok in results)
print(f"\nSUMMARY: {len(results) - nf}/{len(results)} PASS, {nf} FAIL (seed {SEED})")
sys.exit(1 if nf else 0)
