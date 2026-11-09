"""
Verification for derivation 056 (GAP-3e): the BV consequences of the flat representative.

What is verified (finite model of verify-gauge-algebra-ogs4.py, generic tensors PH14, N=2,3,
two seeds):

  C1        the cotangent lift (2.2)/(2.4) of Y -> G_Psi(Y) = M_Psi^{1/2} Y preserves the
            antibracket: J^T Omega J = Omega for the Jacobian J of tau, and
            (f o tau, g o tau) = (f, g) o tau for random cubic f, g.  Break: inverse instead
            of inverse-transpose on Y^+, or the Psi^+ shift dropped.
  C2.1      (3.2): Psi^+.u + Y^+.Rhat_u Y = Psihat^+.u exactly, with Rhat_u = (d_u M^-1/2)M^1/2
            computed by forward-mode AD (not from (2.7)) and Psihat^+ from (2.4).  Break: the
            R17 law kept in the Y^+ term (residual O(g^2) != 0).
  C2.1-ogs4 the same at O(g_s^4) with FlatLaw (053 (5.6)): the hatted Y^+-term vanishes for
            F^flat (by construction of F^flat — documented as such), and for F^(19) it is
            nonzero yet Kcal(nu, F^(19) - F^flat) = 0 (a trivial symmetry, 053 C1).
  C2.2      d_Psi [ p(G_Psi(Y), G_Psi(Y)) ] = 0 (constant coefficients); break: G = M_Psi.
  C2.3      decoupling lemma (3.6) in the all-even representation of the antibracket:
            (S,S) - (S^Psi, S^Psi) = 0 for a random Psi-sector; breaks: a Psi-dependent
            auxiliary kinetic K_Psi(Yhat,Yhat), or a Yhat^+ term kept.
  C3        the lambda^Sigma coefficient mu^E = -(12/g^2) E K^{-1} equals, at O(g^0), the
            antisymmetrised Psi-derivative of the generator mu_u = -(12/g^2)(R17_u - Rhat_u)K^{-1}
            of the antifield-quadratic canonical transformation: E_2 = d_1 D_2 - d_2 D_1,
            exact Taylor coefficients via nilpotent g.  Break: factor 1/2.

What is NOT verified: the Grassmann signs of the antibracket (the checks use even
antifields; every identity tested is parity-blind, see record 056 §2, §3(e)); the master
equation of the Psi-sector itself (Task 7); the all-orders form of the C3 coboundary; the BV
content of C3 at antifield number two (record 056 C3.3: with commuting antifields,
Xi = 1/2 Y^+ mu Y^+ with antisymmetric mu vanishes identically, so no check here can test it).
C3 tests the classical leading-order identity (4.5) only.

Check count: 60 PASS/FAIL lines (30 per seed; C2.1-ogs4 at N=2 only).

Usage: .venv/bin/python codes/verify-gap3e-contractible-pair.py
"""
from __future__ import annotations

import importlib.util
import itertools
import math
import sys
from pathlib import Path

import numpy as np

_spec = importlib.util.spec_from_file_location(
    "ogs4", Path(__file__).with_name("verify-gauge-algebra-ogs4.py"))
ogs4 = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(ogs4)
MD, Model, FlatLaw = ogs4.MD, ogs4.Model, ogs4.FlatLaw
md_einsum, md_solve, md_inv, sqrtm_db = ogs4.md_einsum, ogs4.md_solve, ogs4.md_inv, ogs4.sqrtm_db
law_R19 = ogs4.law_R19

SEEDS = (20260926, 56)
failures: list[str] = []


def report(name: str, ok: bool, detail: str = "") -> None:
    """Print PASS/FAIL for a named check and record failures."""
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""), flush=True)
    if not ok:
        failures.append(name)


def report_break(name: str, ok: bool, detail: str = "") -> None:
    """Report a break leg: ok means the perturbed check failed as it should."""
    report(f"{name}-break", ok, detail)


# ------------------------------------------------------------------ O(g_s^3) model, plain numpy
class Cubic:
    """M_Psi = 1 - (g/5) A_Psi, K_Psi = p M_Psi, R17_u = (g/10) M^{-1} A_u  (043 Part D)."""

    def __init__(self, m: Model, g: float) -> None:
        """Wrap the ogs4 Model tensors at coupling g."""
        self.m, self.g, self.p = m, g, m.V4S
        self.N, self.D = m.N, m.D

    def A(self, w: np.ndarray) -> np.ndarray:
        """A_w = p^{-1} p_{3,2}(., ., w)."""
        return self.m.pinv @ np.einsum('IJe,e->IJ', self.m.V5S, w)

    def M(self, psi: np.ndarray) -> np.ndarray:
        """M_Psi = 1 - (g/5) A_Psi."""
        return np.eye(self.D) - (self.g / 5.0) * self.A(psi)

    @staticmethod
    def sqrtm(M: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        """Denman–Beavers (analytic in the entries: complex-step safe)."""
        Y, Z = M, np.eye(M.shape[0], dtype=M.dtype)
        for _ in range(80):
            Yn = (Y + np.linalg.inv(Z)) / 2
            Zn = (Z + np.linalg.inv(Y)) / 2
            delta = np.abs(Yn - Y).max()
            Y, Z = Yn, Zn
            if delta < 1e-17:
                break
        return Y, Z

    def G(self, psi: np.ndarray, Y: np.ndarray) -> np.ndarray:
        """G_Psi(Y) = M_Psi^{1/2} Y (043 §5)."""
        return self.sqrtm(self.M(psi))[0] @ Y

    def dpsi(self, f, psi: np.ndarray, u: np.ndarray, *args):
        """Complex-step directional derivative d_u f(psi, ...)."""
        h = 1e-20
        return f(psi + 1j * h * u, *args).imag / h

    def tau(self, z: np.ndarray, variant: str = "canonical") -> np.ndarray:
        """(Psi, Y, Psi^+, Y^+) -> (Psi, Yhat, Psihat^+, Yhat^+), eqs (2.2), (2.4)."""
        N, D = self.N, self.D
        psi, Y, psip, Yp = z[:N], z[N:N + D], z[N + D:2 * N + D], z[2 * N + D:]
        Mh = self.sqrtm(self.M(psi))[0]
        Yhat = Mh @ Y
        Jinv = np.linalg.inv(Mh)                       # (D_Y G)^{-1}
        Yhp = Jinv.T @ Yp if variant != "no-transpose" else Jinv @ Yp
        # (d_Psi G)^T Yhat^+ : component a = Yhat^+ . (d_a M^{1/2}) Y
        dG = np.stack([self.dpsi(lambda q: self.sqrtm(self.M(q))[0] @ Y, psi, e)
                       for e in np.eye(N)], axis=1)   # D x N, complex-step needs real psi
        psihp = psip - dG.T @ Yhp if variant != "no-shift" else psip
        return np.concatenate([psi, Yhat, psihp, Yhp])


def omega(n: int) -> np.ndarray:
    """Antibracket matrix in the all-even representation: (f,g) = grad f^T Omega grad g."""
    Om = np.zeros((2 * n, 2 * n))
    Om[:n, n:] = np.eye(n)
    Om[n:, :n] = -np.eye(n)
    return Om


def grad_fd(f, z: np.ndarray, h: float = 1e-6) -> np.ndarray:
    """Central finite-difference gradient (used only where complex step cannot be nested)."""
    out = np.zeros_like(z)
    for i in range(len(z)):
        e = np.zeros_like(z)
        e[i] = h
        out[i] = (f(z + e) - f(z - e)) / (2 * h)
    return out


def random_cubic(rng: np.random.Generator, n: int):
    """Build a random cubic polynomial on R^n and its gradient."""
    a, B, C = rng.standard_normal(n), rng.standard_normal((n, n)), rng.standard_normal((n, n, n))

    def f(z: np.ndarray) -> float:
        return float(a @ z + z @ B @ z + np.einsum('ijk,i,j,k->', C, z, z, z))

    def grad(z: np.ndarray) -> np.ndarray:
        return a + (B + B.T) @ z + (np.einsum('ijk,j,k->i', C, z, z)
                                    + np.einsum('jik,j,k->i', C, z, z)
                                    + np.einsum('jki,j,k->i', C, z, z))
    return f, grad


def check_C1(cm: Cubic, rng: np.random.Generator, tag: str) -> None:
    """C1: the cotangent lift preserves the antibracket (all-even representation)."""
    n = cm.N + cm.D
    z = rng.standard_normal(2 * n)
    Om = omega(n)
    for variant, expect in (("canonical", True), ("no-transpose", False), ("no-shift", False)):
        J = np.stack([grad_fd(lambda q, i=i, v=variant: cm.tau(q, v)[i], z) for i in range(2 * n)])
        res = np.abs(J.T @ Om @ J - Om).max()
        f, gf = random_cubic(rng, 2 * n)
        g, gg = random_cubic(rng, 2 * n)
        zh = cm.tau(z, variant)
        br_hat = gf(zh) @ Om @ gg(zh)                     # (f, g) at tau(z), hatted chart
        br_old = (J.T @ gf(zh)) @ Om @ (J.T @ gg(zh))      # (f o tau, g o tau)(z)
        res2 = abs(br_hat - br_old) / max(1.0, abs(br_hat))
        if expect:
            report(f"C1{tag}", res < 1e-6 and res2 < 1e-6,
                   f"J^T Omega J = Omega ({res:.1e}); (f o tau, g o tau) = (f,g) o tau ({res2:.1e})")
        else:
            report_break(f"C1{tag}-{variant}", res > 1e-3,
                         f"{variant}: J^T Omega J - Omega = {res:.2e} (not canonical)")


def check_C2_cubic(cm: Cubic, rng: np.random.Generator, tag: str) -> None:
    """C2.1 (3.2) and C2.2 (constant coefficients) at O(g_s^3)."""
    N, D, g = cm.N, cm.D, cm.g
    psi, Y, Yp, psip, u = (rng.standard_normal(k) for k in (N, D, D, N, N))
    Mh, Mmh = cm.sqrtm(cm.M(psi))
    # Rhat_u = (d_u M^{-1/2}) M^{1/2}, computed from its 043 definition
    dMmh = cm.dpsi(lambda q: cm.sqrtm(cm.M(q))[1], psi, u)
    Rhat = dMmh @ Mh
    R17 = (g / 10.0) * np.linalg.inv(cm.M(psi)) @ cm.A(u)
    # Psihat^+ . u from (2.4): Psi^+.u - Yhat^+ . d_u G
    Yhp = np.linalg.inv(Mh).T @ Yp
    dG = cm.dpsi(lambda q: cm.sqrtm(cm.M(q))[0] @ Y, psi, u)
    psihp_u = psip @ u - Yhp @ dG
    scale = abs(Yp @ (R17 @ Y))
    res_flat = abs(psip @ u + Yp @ (Rhat @ Y) - psihp_u)
    res_17 = abs(psip @ u + Yp @ (R17 @ Y) - psihp_u)
    report(f"C2.1{tag}", res_flat < 1e-12 * max(1, scale),
           f"(3.2) holds exactly for Rhat: residual {res_flat:.1e} (scale {scale:.2e})")
    report_break(f"C2.1{tag}", res_17 > 1e-3 * g**2,
                 f"R17 kept in the Y^+ term: hatted Y^+-term = {res_17:.2e} = O(g^2), nonzero")
    # C2.2: constant coefficients
    # C2.2: at fixed Yhat, K_Psi(G^{-1}Yhat, G^{-1}Yhat) is Psi-independent (043 (5.5))
    Yhat = Y.copy()

    def kin(q, Ginv):
        Yq = Ginv(q) @ Yhat
        return Yq @ (cm.p @ cm.M(q)) @ Yq

    d_good = abs(cm.dpsi(kin, psi, u, lambda q: cm.sqrtm(cm.M(q))[1]))
    d_bad = abs(cm.dpsi(kin, psi, u, lambda q: np.linalg.inv(cm.M(q))))
    report(f"C2.2{tag}", d_good < 1e-12,
           f"d_u [K_Psi(Y,Y)]_(Yhat fixed) = {d_good:.1e} for G = M^1/2 (constant coefficients)")
    report_break(f"C2.2{tag}", d_bad > 1e-3,
                 f"G = M: d_u [K_Psi(Y,Y)]_(Yhat fixed) = {d_bad:.2e} != 0")


def check_C2_3(cm: Cubic, rng: np.random.Generator, tag: str) -> None:
    """Decoupling lemma (3.6) in the all-even representation."""
    N, D, g = cm.N, cm.D, cm.g
    # coordinates: (Psi, c, Yhat, Psihat^+, c^+, Yhat^+); n = 2N + D
    n = 2 * N + D
    fpsi, gpsi = random_cubic(rng, 2 * (2 * N))   # random Psi-sector "BV action"
    Wt = rng.standard_normal((D, D, N))
    Wt = Wt + Wt.transpose(1, 0, 2)
    Sa = rng.standard_normal((D, D))
    Sa = Sa - Sa.T

    def split(z):
        return z[:N], z[N:2 * N], z[2 * N:2 * N + D], z[n:n + N], z[n + N:n + 2 * N], z[n + 2 * N:]

    def S(z, variant="flat"):
        psi, c, Yh, psip, cp, Yhp = split(z)
        val = fpsi(np.concatenate([psi, c, psip, cp])) - g**2 / 24 * Yh @ cm.p @ Yh
        if variant == "psi-dependent-kinetic":
            val += -g**3 / 24 * Yh @ np.einsum('IJe,e->IJ', Wt, psi) @ Yh
        if variant == "Yhat-plus-term":
            val += g**2 * Yhp @ (np.linalg.solve(cm.p, Sa) @ Yh) * c[0]
        return val

    def Spsi(z):
        psi, c, Yh, psip, cp, Yhp = split(z)
        return fpsi(np.concatenate([psi, c, psip, cp]))

    z = rng.standard_normal(2 * n)

    def bracket(F, z):
        # (S,S) for even S: 2 sum_i d_{phi^i} S d_{phi^+_i} S (the antisymmetric form
        # g^T Omega g vanishes identically for commuting coordinates; this is the graded
        # formula's value with the ordering signs of odd factors dropped — the decoupling
        # lemma (3.6) holds term by term, without sign cancellations, so it is parity-blind)
        gr = grad_fd(F, z)
        return 2 * gr[:n] @ gr[n:]
    bb = bracket(Spsi, z)
    for variant, expect in (("flat", True), ("psi-dependent-kinetic", False), ("Yhat-plus-term", False)):
        d = abs(bracket(lambda q, v=variant: S(q, v), z) - bb)
        if expect:
            report(f"C2.3{tag}", d < 1e-7 * max(1, abs(bb)), f"(S,S) - (S^Psi,S^Psi) = {d:.1e}")
        else:
            report_break(f"C2.3{tag}-{variant}", d > 1e-6, f"{variant}: (S,S) - (S^Psi,S^Psi) = {d:.2e}")


# ------------------------------------------------------------------ C3: nilpotent g, MD
U1, U2 = 0, 1
GBITS = (2, 3, 4)


def taylor(X: MD, k: int) -> np.ndarray:
    """Exact coefficient of g^k from the nilpotent-g components."""
    vals = []
    for sub in itertools.combinations(GBITS, k):
        mask = sum(1 << b for b in sub)
        vals.append(X.c.get(mask, np.zeros_like(X.c[0])) / math.factorial(k))
    for v in vals[1:]:
        assert np.allclose(v, vals[0], atol=1e-12, rtol=1e-8)
    return vals[0]


def check_C3(m: Model, rng: np.random.Generator, tag: str) -> None:
    """C3: the lambda^Sigma coefficient is the exterior derivative of the generator (4.5)."""
    D = m.D
    psi0, u1, u2 = (rng.standard_normal(m.N) for _ in range(3))
    gN = MD({0: 0.0} | {(1 << b): 1.0 for b in GBITS})    # g nilpotent (exact coefficients)
    psi = MD.seed(psi0, {U1: u1, U2: u2})
    Apsi = MD.const(m.pinv) @ md_einsum('IJe,e->IJ', MD.const(m.V5S), psi)
    Mop = MD.const(np.eye(D)) - (gN / 5.0) * Apsi
    Mh, Mmh = sqrtm_db(Mop, extra=8)
    Minv = md_inv(Mop)
    A1, A2 = m.A(u1), m.A(u2)

    def R17(Au):
        return (gN / 10.0) * (Minv @ MD.const(Au))

    def Rhat(a):
        return Mmh.d(a) @ Mh.without(a)      # (d_u M^{-1/2}) M^{1/2}, u = direction a

    # curvature of R17 (constant u's: w = [u1,u2] = 0)
    R1, R2 = R17(A1), R17(A2)
    E = R2.d(U1) - R1.d(U2) + R2.without(U1) @ R1.without(U2) - R1.without(U2) @ R2.without(U1)
    E2 = taylor(E, 2)
    pred = ([A1 @ A2 - A2 @ A1][0]) / 100.0
    report(f"C3{tag}-E2", np.allclose(E2, pred, atol=1e-10), "E[R17] = (g^2/100)[A1,A2] + O(g^3) (R45)")
    # shift Delta R_u = R17_u - Rhat_u, its g^2 coefficient and its Psi-derivative
    dR1 = R1.without(U2) - Rhat(U1)
    # d_{u1} D2(u2) - d_{u2} D2(u1) at g^2
    d1D2 = taylor((R17(A2) - Rhat(U2)).d(U1), 2)
    d2D1 = taylor((R17(A1) - Rhat(U1)).d(U2), 2)
    # D_u := R17_u - Rhat_u is the shift generated by Xi (record §4); E[R17] = E[Rhat] + dD + O(g^3)
    lhs = E2
    rhs = d1D2 - d2D1
    ok = np.allclose(lhs, rhs, atol=1e-10)
    report(f"C3{tag}", ok,
           f"mu^E_12 = d_1 mu_2 - d_2 mu_1 at O(g^0): |E_2 - (d_1 D_2 - d_2 D_1)| = {np.abs(lhs - rhs).max():.1e}")
    report_break(f"C3{tag}", not np.allclose(lhs, 0.5 * rhs, atol=1e-8),
                 "a factor 1/2 in the generator fails")
    # the generator mu_u = -(12/g^2) Delta R_u K^{-1} is antisymmetric (043 D4) at g^2
    D2 = taylor(dR1, 2)
    mu0 = -12.0 * D2 @ m.pinv
    report(f"C3{tag}-antisym", np.allclose(mu0, -mu0.T, atol=1e-10),
           "mu_u antisymmetric at leading order (HT trivial symmetry, 043 D4)")


def check_C2_1_ogs4(m: Model, rng: np.random.Generator, tag: str, g: float = 0.1) -> None:
    """C2.1 at O(g_s^4) with FlatLaw (053 (5.6))."""
    psi0, u1 = rng.standard_normal(m.N), rng.standard_normal(m.N)
    psi = MD.seed(psi0, {U1: u1})
    gM = MD.const(g)
    fl = FlatLaw(m, psi, gM, nmax=4)
    Y = MD.const(0.3 * rng.standard_normal(m.D))
    Yp = rng.standard_normal(m.D)
    Ff = fl.law(Y, U1)                       # F^flat_{u1}(Y)
    J = fl.jac(Y).without(U1)
    dG = fl.G(Y).d(U1)
    # hatted Y^+-term: Yhat^+ . [ (D_Y G) F + d_u G ], Yhat^+ = J^{-T} Y^+
    Yhp = np.linalg.solve(J.primal.T, Yp)
    term_flat = Yhp @ (J.primal @ Ff.primal + dG.primal)
    K = m.Kcal(psi, gM)
    dK = K.d(U1)
    F19 = law_R19(m, Y, K.without(U1), dK, gM)
    term_19 = Yhp @ (J.primal @ F19.primal + dG.primal)
    nu = m.nu(Y, K.without(U1), gM)
    triv = float(nu.primal @ K.primal @ (F19.primal - Ff.primal))
    report(f"C2.1-ogs4{tag}", abs(term_flat) < 1e-12 * max(1, abs(term_19)),
           f"hatted Y^+-term for F^flat = {abs(term_flat):.1e} (by construction of F^flat, 053 (5.6))")
    report_break(f"C2.1-ogs4{tag}", abs(term_19) > 1e-6 and abs(triv) < 1e-10 * max(1, abs(Yp @ F19.primal)),
                 f"F^(19) kept: hatted Y^+-term = {term_19:.2e} != 0, and Kcal(nu, F19 - Fflat) = {triv:.1e} (trivial symmetry)")


def main() -> int:
    """Run all checks; nonzero exit on failure."""
    print(f"seeds {SEEDS}")
    for seed in SEEDS:
        for N in (2, 3):
            tag = f"-N{N}s{seed}"
            m = Model(N, seed)
            rng = np.random.default_rng(seed + 7 * N)
            cm = Cubic(m, g=0.1)
            check_C1(cm, rng, tag)
            check_C2_cubic(cm, rng, tag)
            check_C2_3(cm, rng, tag)
            check_C3(m, rng, tag)
            if N == 2:
                check_C2_1_ogs4(m, rng, tag)
    print(f"SUMMARY: {len(failures)} failures" + (f": {failures}" if failures else " — all PASS"))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
