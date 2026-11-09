"""
Verification for derivation 065 (integrating out Psi: the classical Sigma-only action).

Cubic (Hubbard-Stratonovich) closed SFT, algebraic layer.

Model (record 065 A3): H = R^2 (five-field model of 057 section 3 at S_2), fields even,
omega = identity so Q = V_2 as a matrix, V_n random rational totally symmetric tensors,
Sigma a symmetric 2x2 matrix (Sym^2 H, dimension 3). The scaling S = g^{-2} S(g Psi,
g^2 Sigma) is exact, so the model is run at g = 1 except where the g-dependence is
the claim (C1.2-neumann, C4-S3).

Action (R1, R17):
    S_2 = 1/2 V_2(Psi^2) + g/6 V_3(Psi^3) - g^2/24 V_4(Sigma,Sigma) + g^2/12 V_4(Sigma,Psi,Psi)
    S_3 = S_2 + g^3/120 V_5(Sigma,Sigma,Psi)

Verified (checks named after the claim-tree nodes of record 065):
    C0.1-c4          Psi-gradient of S_2 = V_2 Psi + g/2 V_3(Psi,Psi,.) + g^2/6 V_4(Sigma,Psi,.)
    C0.2-trivial     the gradient vanishes identically at Psi = 0 (S_2)
    C0.2-S3-source   at S_3 the gradient at Psi = 0 is g^3/120 V_5(Sigma,Sigma,.), nonzero
    C1.1-hess        Psi-Hessian at Psi = 0 is V_2 + g^2/6 V_4(Sigma), symmetric
    C1.2-neumann     det Q_Sigma at Sigma = s/g^2 is g-independent; nonzero for small s
    C1.2-D           an exact rational Sigma_0 with a prescribed kernel vector chi
    C2-g2, C2-g4     (L-infinity model of 060 part 2, imported) {T_0, T_2(Sigma)} != 0 and
                     T_2(Sigma)^2 != 0 while T_0^2 = 0: Q_Sigma is not nilpotent
    C3-iso           off D, no solution of the Psi-equation approaches 0 (exact resultants)
    C3-double        at Sigma_0 exactly, Psi = 0 is a double root and isolated
    C3-branch        slope of the transcritical branch, eq. (2.5), with break leg 1/3 -> 1/6
    C4-exact         Gamma_0 = -g^2/24 V_4(Sigma,Sigma) - g/12 V_3(Psi_*^3) on the branch
    C4-leading       eq. (4.2), the lambda^3 law
    C4-S3            exact g-series of Gamma_0 at S_3 through g^9 against eq. (4.4)
    C5-joint         joint critical points (Psi_c, Psi_c (x) Psi_c) of S_2
    C5-envelope      d Gamma_0 / d Sigma = 0 at Sigma_c on the branch through the joint
                     critical point, nonzero elsewhere; break leg c_4 = 1/5

Not verified: anything about the string vertices themselves (PH1, PH5 scope), the
Siegel-gauge invertibility of Q (A4), the L-infinity relation (1.5) beyond the model,
and the connectedness of the branch through (Psi_c, Sigma_c) with the transcritical
branch through D.

Run: OMP_NUM_THREADS=1 .venv/bin/python codes/verify-sigma-effective.py
"""

from __future__ import annotations

import importlib.util
import itertools
import sys
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp

SEED = 20261001
mp.mp.dps = 30
npass = 0
failures: list[str] = []


def report(name: str, ok: bool, detail: str = "") -> None:
    """Print a labelled PASS/FAIL line and record failures."""
    global npass
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")
    if ok:
        npass += 1
    else:
        failures.append(name)


# ------------------------------------------------------------------ tensors on R^2
N = 2


def rand_sym(rng: np.random.Generator, k: int, lo: int = -5, hi: int = 6, den: int = 3):
    """Random totally symmetric rational k-tensor on R^N as dict index-tuple -> Rational."""
    T = {}
    for c in itertools.combinations_with_replacement(range(N), k):
        val = sp.Rational(int(rng.integers(lo, hi)), den)
        if val == 0:
            val = sp.Rational(1, den)
        for p in set(itertools.permutations(c)):
            T[p] = val
    return T


def contract(T: dict, args: list) -> sp.Expr:
    """T(a_1, ..., a_m) where each a is a vector (list) or a symmetric matrix (2 legs)."""
    tot = 0
    for idx, val in T.items():
        term = val
        pos = 0
        for a in args:
            if isinstance(a[0], (list, tuple)):
                term = term * a[idx[pos]][idx[pos + 1]]
                pos += 2
            else:
                term = term * a[idx[pos]]
                pos += 1
        tot += term
    return sp.expand(tot)


def vec_of(T: dict, args: list) -> list:
    """T(args..., .) as a vector (contraction with the last leg free)."""
    return [
        contract(T, args + [[1 if i == j else 0 for j in range(N)]]) for i in range(N)
    ]


def mat_of(T: dict, args: list) -> sp.Matrix:
    """T(args..., ., .) as a symmetric matrix."""
    E = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
    return sp.Matrix(N, N, lambda i, j: contract(T, args + [E[i], E[j]]))


rng = np.random.default_rng(SEED)
V = {k: rand_sym(rng, k) for k in range(2, 6)}
g = sp.Symbol("g", positive=True)
t = list(sp.symbols("t0:2"))
s0, s1, s2 = sp.symbols("s0:3")
Sig = [[s0, s1], [s1, s2]]
svars = [s0, s1, s2]
Q = mat_of(V[2], [])
ndraw = 1
while Q.det() == 0:  # A4: Q invertible (the first draw of seed 20261001 is singular)
    V[2] = rand_sym(rng, 2)
    Q = mat_of(V[2], [])
    ndraw += 1
print(f"seed {SEED}; V_2 = {Q.tolist()} (draw {ndraw}), det V_2 = {Q.det()}")


C4_DEFAULT = sp.Rational(1, 6)


def action(order: int, c4=C4_DEFAULT):
    """S_2 (order=2) or S_3 (order=3) with the V_4(Sigma,Psi,Psi) coefficient c4/2."""
    S = (
        sp.Rational(1, 2) * contract(V[2], [t, t])
        + g / 6 * contract(V[3], [t, t, t])
        - g**2 / 24 * contract(V[4], [Sig, Sig])
        + c4 / 2 * g**2 * contract(V[4], [Sig, t, t])
    )
    if order == 3:
        S += g**3 / 120 * contract(V[5], [Sig, Sig, t])
    return sp.expand(S)


S2 = action(2)
S3 = action(3)
gradS2 = [sp.diff(S2, x) for x in t]
gradS3 = [sp.diff(S3, x) for x in t]

# Sym^2 invertibility of V_4 (A3)
HS = sp.hessian(contract(V[4], [Sig, Sig]), svars)
print(f"V_4 on Sym^2: det = {HS.det()} (must be nonzero)")
assert HS.det() != 0

# ------------------------------------------------------------------ C0
E2 = [
    sp.expand(a + g / 2 * b + g**2 / 6 * c)
    for a, b, c in zip(
        (Q * sp.Matrix(t)), vec_of(V[3], [t, t]), vec_of(V[4], [Sig, t]), strict=True
    )
]
ok = all(sp.expand(gradS2[i] - E2[i]) == 0 for i in range(N))
E2wrong = [
    sp.expand(a + g / 2 * b + g**2 / 3 * c)
    for a, b, c in zip(
        (Q * sp.Matrix(t)), vec_of(V[3], [t, t]), vec_of(V[4], [Sig, t]), strict=True
    )
]
bad = all(sp.expand(gradS2[i] - E2wrong[i]) == 0 for i in range(N))
report(
    "C0.1-c4",
    ok and not bad,
    "grad S_2 = Q Psi + g/2 V_3(Psi,Psi,.) + g^2/6 V_4(Sigma,Psi,.); c_4 = 1/3 fails",
)
at0 = {x: 0 for x in t}
report(
    "C0.2-trivial",
    all(sp.expand(e.subs(at0)) == 0 for e in gradS2),
    "grad S_2 at Psi = 0 vanishes identically in Sigma",
)
src = [sp.expand(e.subs(at0)) for e in gradS3]
jS = vec_of(V[5], [Sig, Sig])
rsig = {s0: sp.Rational(2, 3), s1: sp.Rational(-1, 2), s2: sp.Rational(5, 7)}
report(
    "C0.2-S3-source",
    all(sp.expand(src[i] - g**3 / 120 * jS[i]) == 0 for i in range(N))
    and any(jS[i].subs(rsig) != 0 for i in range(N)),
    f"grad S_3 at Psi = 0 = g^3/120 V_5(Sigma,Sigma,.); at a rational Sigma: {[jS[i].subs(rsig) for i in range(N)]}",
)

# ------------------------------------------------------------------ C1
H0 = sp.hessian(S2, t).subs(at0)
QSig = Q + g**2 / 6 * mat_of(V[4], [Sig])
report(
    "C1.1-hess",
    (H0 - QSig).applyfunc(sp.expand) == sp.zeros(N, N)
    and QSig.T == QSig
    and (H0 - (Q + g**2 / 3 * mat_of(V[4], [Sig]))).applyfunc(sp.expand)
    != sp.zeros(N, N),
    "Hess_Psi S_2 |_0 = V_2 + g^2/6 V_4(Sigma), symmetric; 1/3 fails",
)
sv = sp.symbols("sv0:3")
detQ_scaled = sp.expand(
    QSig.det().subs({s0: sv[0] / g**2, s1: sv[1] / g**2, s2: sv[2] / g**2})
)
small = {
    sv[0]: sp.Rational(1, 100),
    sv[1]: sp.Rational(-1, 100),
    sv[2]: sp.Rational(1, 50),
}
report(
    "C1.2-neumann",
    not detQ_scaled.has(g)
    and detQ_scaled.subs(small) != 0
    and abs(detQ_scaled.subs(small) / Q.det() - 1) < sp.Rational(1, 10),
    f"det Q_Sigma(s/g^2) g-free: {detQ_scaled}; at |s| ~ 0.01 it is {detQ_scaled.subs(small)} ~ det V_2 = {Q.det()}",
)

# exact Sigma_0 with prescribed kernel vector chi (g = 1)
chi = [sp.Rational(3, 2), sp.Rational(-1, 1)]
eqs = list(QSig.subs(g, 1) * sp.Matrix(chi))
sol = sp.solve(eqs, [s0, s1], dict=True)[0]
Sig0 = {
    s0: sol[s0].subs(s2, sp.Rational(1, 3)),
    s1: sol[s1].subs(s2, sp.Rational(1, 3)),
    s2: sp.Rational(1, 3),
}
Q0 = QSig.subs(g, 1).subs(Sig0)
report(
    "C1.2-D",
    Q0.det() == 0 and Q0.rank() == 1 and (Q0 * sp.Matrix(chi)) == sp.zeros(N, 1),
    f"Sigma_0 = {[Sig0[x] for x in svars]}, Q_Sigma0 chi = 0 exactly, corank one",
)

# ------------------------------------------------------------------ C2 (L-infinity model of 060)
try:
    path = Path(__file__).with_name("verify-mean-field-fluctuations.py")
    spec = importlib.util.spec_from_file_location("mf060", path)
    mf = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mf)
    lm = mf.LinfModel(21, [0, 0, 0, 1, 1], (1,), parent="T3")
    T0 = lm.T0()
    d1 = len(lm.f1)
    rng2 = np.random.default_rng(SEED + 1)
    Sg = rng2.standard_normal((d1, d1))
    Sg = Sg + Sg.T
    T2S = lm.T2_sym(Sg)
    nil0 = np.linalg.norm(T0 @ T0) / np.linalg.norm(T0) ** 2
    anti = np.linalg.norm(T0 @ T2S + T2S @ T0) / (
        np.linalg.norm(T0) * np.linalg.norm(T2S)
    )
    # Q-closed Sigma = psi (x) psi with T0 psi = 0 in the field sector
    Tf = T0[np.ix_(lm.f1, lm.f1)]
    # find psi in the field sector with T0 (iota psi) = 0 on the whole retract
    A = T0[:, lm.f1]
    _u, sv_, vh = np.linalg.svd(A)
    psi = vh[-1]
    closed = np.linalg.norm(A @ psi)
    T2P = lm.T2_sym(np.outer(psi, psi))
    antiP = np.linalg.norm(T0 @ T2P + T2P @ T0) / (
        np.linalg.norm(T0) * np.linalg.norm(T2P)
    )
    sq = np.linalg.norm(T2S @ T2S) / np.linalg.norm(T2S) ** 2
    report(
        "C2-g2",
        nil0 < 1e-12 and anti > 1e-3 and (closed < 1e-8 and antiP > 1e-3),
        f"T0^2 = {nil0:.1e}; |{{T0,T2(Sigma)}}|/(|T0||T2|) = {anti:.3f} (random Sigma); "
        f"Q-closed psi (x) psi (|T0 psi| = {closed:.1e}): {antiP:.3f}",
    )
    report(
        "C2-g4",
        sq > 1e-3,
        f"|T2(Sigma)^2|/|T2(Sigma)|^2 = {sq:.3f} (the O(g^4) term of (1.4) is nonzero)",
    )
except Exception as exc:  # noqa: BLE001
    report("C2-g2", False, f"L-infinity model import failed: {exc!r}")
    report("C2-g4", False, "not run")

# ------------------------------------------------------------------ C3 (g = 1)
E2g1 = [e.subs(g, 1) for e in E2]
dSig = {s0: sp.Rational(1, 2), s1: sp.Rational(1, 5), s2: sp.Rational(-2, 3)}
lam = sp.Symbol("lam")


def eom_at(sig_sub: dict) -> list:
    """Psi-equation (0.2) at g = 1 and the given Sigma."""
    return [sp.expand(e.subs(sig_sub)) for e in E2g1]


def all_roots(eqs: list) -> list:
    """All complex solutions (t0, t1) of two polynomial equations via resultant."""
    R = sp.Poly(sp.resultant(eqs[0], eqs[1], t[1]), t[0])
    out = []
    r0s = R.nroots(n=30, maxsteps=300)
    for r0 in r0s:
        p1 = sp.Poly(eqs[0].subs(t[0], r0), t[1])
        for r1 in p1.nroots(n=30, maxsteps=300):
            res = max(abs(sp.N(e.subs({t[0]: r0, t[1]: r1}), 30)) for e in eqs)
            if res < 1e-15:
                out.append((r0, r1))
    return out


def sig_line(base: dict, lam_val) -> dict:
    """Sigma = base + lam_val * dSigma."""
    return {x: base[x] + lam_val * dSig[x] for x in svars}


# C3-iso: generic Sigma_off, approached along lam -> 0: nonzero roots stay away from 0
Sig_off = {s0: sp.Rational(1, 4), s1: sp.Rational(-1, 3), s2: sp.Rational(1, 2)}
Qoff = QSig.subs(g, 1).subs(Sig_off)
mins = []
for lv in (sp.Rational(1, 100), sp.Rational(1, 1000), sp.Integer(0)):
    rts = all_roots(eom_at(sig_line(Sig_off, lv)))
    nz = [
        abs(sp.N(sp.sqrt(a * sp.conjugate(a) + b * sp.conjugate(b)), 30))
        for a, b in rts
    ]
    nz = [x for x in nz if x > 1e-12]
    mins.append(min(nz))
report(
    "C3-iso",
    Qoff.det() != 0 and min(mins) > 0.05 and max(mins) / min(mins) < 1.5,
    f"det Q_Sigma_off = {Qoff.det()} != 0; nearest nonzero root norm {[mp.nstr(mp.mpf(str(x)), 5) for x in mins]} as lam -> 0",
)

# C3-double: at Sigma_0 exactly
eq0 = eom_at(Sig0)
R0 = sp.Poly(sp.resultant(eq0[0], eq0[1], t[1]), t[0])
mult0 = sp.roots(R0).get(sp.Integer(0), 0)
rts0 = all_roots(eq0)
others = [
    abs(sp.N(sp.sqrt(a * sp.conjugate(a) + b * sp.conjugate(b)), 30)) for a, b in rts0
]
others = [x for x in others if x > 1e-12]
V3chi = contract(V[3], [chi, chi, chi])
report(
    "C3-double",
    mult0 == 2 and (not others or min(others) > 0.05),
    f"multiplicity of t0 = 0 in the resultant: {mult0}; other roots at distance >= {mp.nstr(mp.mpf(str(min(others))), 5) if others else 'none'}",
)
report("C3-caveat", V3chi != 0, f"V_3(chi,chi,chi) = {V3chi} != 0 (transcritical case)")

# C3-branch: slope (2.5)
V4dchi = contract(V[4], [[[dSig[s0], dSig[s1]], [dSig[s1], dSig[s2]]], chi, chi])
slope = -sp.Rational(1, 3) * V4dchi / V3chi  # epsilon / lambda
errs = []
branch_pts = {}
for lv in (sp.Rational(1, 100), sp.Rational(1, 200), sp.Rational(1, 400)):
    eqs = eom_at(sig_line(Sig0, lv))
    f = sp.lambdify(t, eqs, "mpmath")
    start = [mp.mpf(str(slope * lv * c)) for c in chi]
    root = mp.findroot(
        lambda a, b, f=f: f(a, b), start, tol=mp.mpf(10) ** -28, maxsteps=100
    )
    root = [root[0], root[1]]
    pred = [mp.mpf(str(slope * lv * c)) for c in chi]
    rel = mp.norm(mp.matrix(root) - mp.matrix(pred)) / mp.norm(mp.matrix(pred))
    errs.append(rel)
    branch_pts[lv] = root
r1 = errs[0] / errs[1]
r2 = errs[1] / errs[2]
slope_wrong = -sp.Rational(1, 6) * V4dchi / V3chi
rel_wrong = mp.norm(
    mp.matrix(branch_pts[sp.Rational(1, 400)])
    - mp.matrix([mp.mpf(str(slope_wrong * sp.Rational(1, 400) * c)) for c in chi])
) / mp.norm(mp.matrix(branch_pts[sp.Rational(1, 400)]))
report(
    "C3-branch",
    all(e < 0.1 for e in errs)
    and abs(r1 - 2) < 0.3
    and abs(r2 - 2) < 0.3
    and rel_wrong > 0.3,
    f"|Psi_* - eps chi|/|eps chi| = {[mp.nstr(e, 3) for e in errs]} at lam = 1/100, 1/200, 1/400 (ratios {mp.nstr(r1, 3)}, {mp.nstr(r2, 3)}); break 1/3 -> 1/6: {mp.nstr(rel_wrong, 3)}",
)

# ------------------------------------------------------------------ C4 (g = 1 at S_2)
S2g1 = S2.subs(g, 1)
fS2 = sp.lambdify(t + svars, S2g1, "mpmath")
fV4SS = sp.lambdify(svars, contract(V[4], [Sig, Sig]), "mpmath")
fV3 = sp.lambdify(t, contract(V[3], [t, t, t]), "mpmath")
devs, ratios = [], []
for lv, root in branch_pts.items():
    sg = [mp.mpf(str(sig_line(Sig0, lv)[x])) for x in svars]
    direct = fS2(*root, *sg)
    formula = -fV4SS(*sg) / 24 - fV3(*root) / 12
    devs.append(abs(direct - formula) / (abs(direct) + 1))
    triv = -fV4SS(*sg) / 24
    pred = mp.mpf(str(V4dchi**3 / V3chi**2 / 324)) * mp.mpf(str(lv)) ** 3
    ratios.append((direct - triv) / pred)
# break: an off-branch point
sg = [mp.mpf(str(sig_line(Sig0, sp.Rational(1, 100))[x])) for x in svars]
off = [
    branch_pts[sp.Rational(1, 100)][i] + mp.mpf("0.3") * mp.mpf(str(chi[i]))
    for i in range(N)
]
dev_off = abs(fS2(*off, *sg) - (-fV4SS(*sg) / 24 - fV3(*off) / 12)) / (
    abs(fS2(*off, *sg)) + 1
)
report(
    "C4-exact",
    max(devs) < mp.mpf("1e-25") and dev_off > mp.mpf("1e-4"),
    f"(4.1) holds to {mp.nstr(max(devs), 2)} on the branch; off-branch deviation {mp.nstr(dev_off, 2)}",
)
report(
    "C4-leading",
    abs(ratios[-1] - 1) < 0.1 and abs(ratios[0] - 1) > abs(ratios[-1] - 1),
    f"(Gamma_0 - Gamma_0^triv)/(g^4/324 V_4(dS,chi,chi)^3/V_3(chi^3)^2 lam^3) = {[mp.nstr(r, 5) for r in ratios]} at lam = 1/100, 1/200, 1/400",
)

# C4-S3: exact g-series of Gamma_0 at S_3 through g^9 around Psi = 0
ORD = 10
Sig_r = {s0: sp.Rational(2, 3), s1: sp.Rational(-1, 2), s2: sp.Rational(5, 7)}
E3 = [sp.expand((E2[i] + g**3 / 120 * jS[i]).subs(Sig_r)) for i in range(N)]
Qinv = Q.inv()


def trunc(e, k=ORD):
    """Truncate a g-series at order k."""
    return sp.expand(sp.series(sp.expand(e), g, 0, k).removeO())


psi = sp.Matrix([0, 0])
for _ in range(6):
    rhs = sp.Matrix(
        [
            trunc(E3[i].subs({t[0]: psi[0], t[1]: psi[1]}) - (Q * psi)[i])
            for i in range(N)
        ]
    )
    psi = (-Qinv * rhs).applyfunc(trunc)
resid = [trunc(E3[i].subs({t[0]: psi[0], t[1]: psi[1]})) for i in range(N)]
Gam = trunc(S3.subs(Sig_r).subs({t[0]: psi[0], t[1]: psi[1]}))
SigM = [[Sig_r[s0], Sig_r[s1]], [Sig_r[s1], Sig_r[s2]]]
jv = sp.Matrix([c.subs(Sig_r) for c in jS])
QSr = QSig.subs(Sig_r)
QSinv_ser = (
    Qinv
    - g**2 / 6 * Qinv * mat_of(V[4], [SigM]) * Qinv
    + g**4 / 36 * Qinv * mat_of(V[4], [SigM]) * Qinv * mat_of(V[4], [SigM]) * Qinv
)
pred43 = trunc(
    -(g**2) / 24 * contract(V[4], [SigM, SigM])
    - g**6 / 28800 * (jv.T * QSinv_ser * jv)[0]
)
x = Qinv * jv
pred44 = trunc(
    -(g**2) / 24 * contract(V[4], [SigM, SigM])
    - g**6 / 28800 * (jv.T * x)[0]
    + g**8 / 172800 * contract(V[4], [SigM, list(x), list(x)])
)
pred_wrong = trunc(
    -(g**2) / 24 * contract(V[4], [SigM, SigM])
    - g**6 / 14400 * (jv.T * QSinv_ser * jv)[0]
)
report(
    "C4-S3",
    all(r == 0 for r in resid)
    and trunc(Gam - pred43) == 0
    and trunc(Gam - pred44) == 0
    and trunc(Gam - pred_wrong) != 0,
    f"Gamma_0^S3 through g^9 = (4.3) = (4.4) exactly; coefficients [g^2,g^6,g^8] = "
    f"{[sp.Poly(Gam, g).coeff_monomial(g**k) for k in (2, 6, 8)]}; odd orders {[sp.Poly(Gam, g).coeff_monomial(g**k) for k in (3, 5, 7, 9)]}; 1/14400 fails",
)

# ------------------------------------------------------------------ C5 (g = 1 at S_2)
Pmat = [[t[0] * t[0], t[0] * t[1]], [t[0] * t[1], t[1] * t[1]]]
Veff = sp.expand(S2g1.subs({s0: Pmat[0][0], s1: Pmat[0][1], s2: Pmat[1][1]}))
gV = [sp.diff(Veff, x) for x in t]
crit = all_roots(gV)
real_nz = [
    (sp.re(a), sp.re(b))
    for a, b in crit
    if abs(sp.im(a)) < 1e-20 and abs(sp.im(b)) < 1e-20 and abs(a) + abs(b) > 1e-10
]
gS_all = sp.lambdify(t + svars, [sp.diff(S2g1, x) for x in t + svars], "mpmath")
joint_ok = []
for a, b in real_nz:
    pc = [mp.mpf(str(a)), mp.mpf(str(b))]
    sc = [pc[0] ** 2, pc[0] * pc[1], pc[1] ** 2]
    joint_ok.append(max(abs(v) for v in gS_all(*pc, *sc)))
report(
    "C5-joint",
    len(real_nz) >= 1 and max(joint_ok) < mp.mpf("1e-25"),
    f"{len(real_nz)} real nonzero critical points of V_eff; joint gradient of S_2 at (Psi_c, Psi_c (x) Psi_c) <= {mp.nstr(max(joint_ok), 2)}",
)


def gamma0_on_branch(c4val, psi_start, sig):
    """Gamma_0(sig) on the branch through psi_start for the action with V_4(Sigma,Psi,Psi) coefficient c4val/2."""
    Sc = action(2, c4=c4val).subs(g, 1)
    eqs = [sp.diff(Sc, x) for x in t]
    f = sp.lambdify(t + svars, eqs, "mpmath")
    fS = sp.lambdify(t + svars, Sc, "mpmath")
    root = mp.findroot(
        lambda a, b: f(a, b, *sig), psi_start, tol=mp.mpf(10) ** -28, maxsteps=100
    )
    return fS(root[0], root[1], *sig), [root[0], root[1]]


a, b = real_nz[0]
pc = [mp.mpf(str(a)), mp.mpf(str(b))]
sc = [pc[0] ** 2, pc[0] * pc[1], pc[1] ** 2]
h = mp.mpf("1e-10")


def dGamma(c4val, sig, psi_start):
    """Central-difference gradient of Gamma_0 on the branch through psi_start."""
    out = []
    for i in range(3):
        sp_ = list(sig)
        sm_ = list(sig)
        sp_[i] += h
        sm_[i] -= h
        gp, rp = gamma0_on_branch(c4val, psi_start, sp_)
        gm, rm = gamma0_on_branch(c4val, psi_start, sm_)
        out.append((gp - gm) / (2 * h))
    return out


dG_c = dGamma(sp.Rational(1, 6), sc, pc)
sig_d = [sc[0] + mp.mpf("0.05"), sc[1] - mp.mpf("0.03"), sc[2] + mp.mpf("0.02")]
_, psi_d = gamma0_on_branch(sp.Rational(1, 6), pc, sig_d)
dG_d = dGamma(sp.Rational(1, 6), sig_d, psi_d)
dS_d = gS_all(*psi_d, *sig_d)[2:]
env_err = max(abs(x - y) for x, y in zip(dG_d, dS_d, strict=True)) / max(
    abs(y) for y in dS_d
)
_, psi_w = gamma0_on_branch(sp.Rational(1, 5), pc, sc)
dG_w = dGamma(sp.Rational(1, 5), sc, psi_w)
report(
    "C5-envelope",
    max(abs(x) for x in dG_c) < mp.mpf("1e-12")
    and env_err < mp.mpf("1e-8")
    and max(abs(y) for y in dS_d) > mp.mpf("1e-3")
    and max(abs(x) for x in dG_w) > mp.mpf("1e-3"),
    f"|dGamma_0| at Sigma_c = {mp.nstr(max(abs(x) for x in dG_c), 2)}; envelope (4.5) at a displaced Sigma: rel err {mp.nstr(env_err, 2)} "
    f"with |dS/dSigma| = {mp.nstr(max(abs(y) for y in dS_d), 3)}; break c_4 = 1/5: |dGamma_0| = {mp.nstr(max(abs(x) for x in dG_w), 3)}",
)

print(
    f"\nSUMMARY: {npass} PASS, {len(failures)} FAIL"
    + (f": {failures}" if failures else "")
    + f"; seed {SEED}"
)
sys.exit(1 if failures else 0)
