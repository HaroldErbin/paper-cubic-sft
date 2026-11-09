#!/usr/bin/env python3
r"""
verify-gauge-algebra-ogs4.py — part B of derivation 053 (GAP-3d at O(g_s^4)).

Machine confirmation, in the finite model of ``verify-b3-sextic.py`` (lines 79–190:
generic totally symmetric V4, V5, V6 on H_0 = R^N, orthonormal Sym^2 basis, composite
kernel C, T = V6 - (6/5) C, dressed saddle Hessian), of the claims C1–C3 of record 053:

  Phi*(Y; Psi) = -(g^2/24) Kcal(Y,Y) + (g^4/720) T(Y,Y,Y),   Y = Sigma_2 - Sigma_*(Psi),
  Kcal = -(12/g^2) hess|_{Sigma_*} = p - (g/5) V5(.,.,Psi) - (g^2/10) T(.,.,Sigma_*).

Differentiation.  Every derivative (d_u through the Newton saddle, d_{u1} d_{u2}, the
Y-Jacobian along a vector, exact Taylor coefficients in g) is taken by forward-mode
automatic differentiation with *multi-dual numbers*: m nilpotent directions eps_a with
eps_a^2 = 0, eps_a eps_b != 0 (class ``MD``).  Seeding Psi -> Psi + eps_1 u1 + eps_2 u2 and
Y -> Y + eps_3 w gives d_{u1}, d_{u2}, d_{u1}d_{u2}, D_Y(.)w and the mixed terms exactly
(no step size, no truncation error); seeding g -> eps_4 + ... + eps_7 at g = 0 gives the
exact Taylor coefficients c_k = comp[k-subset]/k! of any polynomial-in-g quantity for
k <= 4.  All model quantities are written as polynomials in g (the O(g^2) prefactor of the
Sigma-sector action is divided out), so the g = 0 evaluation is regular.

Checks (named after the claim-tree nodes of record 053; each states what would fail it):
  S0     setup: Phi* from S4 around the saddle equals its cubic form (A3); d_u Kcal by
         forward mode equals the implicit-function-theorem value.
  C1.1   invariance residual (3.2) of R19's law F^(19) (linear solve of the implicit law)
         is zero to rounding.  Fails if F^(19) were not admissible (e.g. the law without
         its T-correction, checked as break).
  C1.3   F^(19) + Kcal^{-1} S(Y) nu(Y), S(Y) = S0 + S1.Y antisymmetric, stays admissible;
         break: symmetric S gives an O(1) residual.
  C1.2   least-squares residual of (3.7) is O(1) at D = 3 and D = 6 (no Y-linear law);
         breaks: T -> 0 (residual 0, the linear family of 043 exists) and a source placed
         in the image (residual 0).
  C2.1   Kcal(nu(Y), E_4[F^(19)]) = 0 to rounding ((4.3): E_4 is a trivial symmetry);
         break: the non-admissible law without T-correction gives a nonzero value.
  C2.2   E_4^(1) = [R^(19)_1, R^(19)_2] Y exactly (all g, to rounding); exact Taylor
         coefficients: c_2 = (1/100)[A_1,A_2]Y, c_3 - c_3[E_3] = (4.7); break: 1/100 -> 1/50
         in (4.7).
  C2.3   exact g^4 coefficient of the Y-quadratic sector of E_4 against (4.8); break: a
         wrong coefficient in (4.8).  (If the check fails the fitted coefficients of the
         two structures are printed as a diagnostic, never used to pass.)
  C2-R   Richardson slopes in g (g halving) of the residuals after removing the g^2, g^3
         terms (linear sector, last slope within 0.35 of 3, 4) and the g^4 term (quadratic
         sector, last slope >= 4.65, one-sided since the fix pass: pre-asymptotic g^6
         dominance at D = 6, seed 53); break: (4.8) as first written gives slope 4.
  C3.1   Morse map (5.3)–(5.4) iterated to n = 4: residual of (5.5) scales as g^{2n+2};
         at fixed g iterated to the tensor budget, residual at rounding level (D = 3) or
         at the truncation order (D = 6, reported).
  C3.2-expansion  (fix pass) exact g^3 Taylor coefficient of the Y-quadratic part of
         F^flat = -(D_Y G)^{-1} d_u G (computed from G, nilpotent g) equals the corrected
         boxed (5.6): (g^2/60) R19_u Kcal^-1 T(.,Y,Y) + (g^2/30) Kcal^-1 T(.,Y,R19_u Y),
         and its hand form in A_u; zero through g^2; degree-2 homogeneous.  Break: (5.6) as
         first written, (g^2/30) R19_u Kcal^-1 T(.,Y,Y), must fail.
  C3     E_4[F^flat] = 0 to rounding AND invariance residual of F^flat at rounding /
         truncation level; breaks: G = M_K^{1/2} alone (flat, not admissible) and F^(19)
         (admissible, not flat).
  C3-inv documentary: the brief's invariants of T-hat_Psi at two Psi (expected to differ).

Outcome history: run 6 (unpublished log) failed C2.3 and its
Richardson leg C2-R-quad-c4 against (4.8) as first written, with second coefficient
-19/2000; the exact g^4 coefficient of the Y-quadratic sector is (1/2000) s1 - (1/2000) s2
(fit residual 1e-15, four configurations; hand re-derivations in record 053 section 7 and
in the critic's report agree).  The fix pass corrected (4.8) in the record and here
(c4q_pred); run 7 (unpublished log) is the current run.

Not verified here: convergence of the Y-series beyond the sampled |Y| (~1), the
string-vertex realisation (PH14), and anything outside the finite model.

Usage: ``.venv/bin/python codes/verify-gauge-algebra-ogs4.py``; exit code = #failures.
"""

from __future__ import annotations

import itertools
import math
import sys
import time
from collections.abc import Callable

import numpy as np

SEEDS = (20260926, 53)
NS = (2, 3)
GS = (0.05, 0.1, 0.2)
GS_RICH = (0.2, 0.1, 0.05, 0.025, 0.0125, 0.00625, 0.003125)   # Richardson sequence (g halving)
GS_MORSE = (0.2, 0.1, 0.05, 0.025)                              # C3.1 / C3 truncation sequence
TOL = 1e-9
failures: list[str] = []
t_start = time.time()


def report(name: str, ok: bool, detail: str = "") -> None:
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}" + (f" — {detail}" if detail else ""), flush=True)
    if not ok:
        failures.append(name)


def report_break(name: str, ok: bool, detail: str = "") -> None:
    report(f"{name}-break", ok, detail)


# ============================================================ multi-dual numbers
def _popcount(m: int) -> int:
    return bin(m).count("1")


class MD:
    """Multi-dual number: dict mask -> ndarray, first order in each nilpotent direction."""

    __slots__ = ("c",)
    __array_ufunc__ = None   # make numpy defer to the reflected operators

    def __init__(self, c: dict[int, np.ndarray]) -> None:
        self.c = {k: np.asarray(v, dtype=float) for k, v in c.items()}

    @staticmethod
    def const(x: np.ndarray | float) -> MD:
        return MD({0: np.asarray(x, dtype=float)})

    @staticmethod
    def seed(x0: np.ndarray | float, seeds: dict[int, np.ndarray | float]) -> MD:
        c = {0: np.asarray(x0, dtype=float)}
        for a, v in seeds.items():
            c[1 << a] = np.asarray(v, dtype=float)
        return MD(c)

    @staticmethod
    def lift(x: MD | np.ndarray | float) -> MD:
        return x if isinstance(x, MD) else MD.const(x)

    @property
    def primal(self) -> np.ndarray:
        return self.c[0]

    def d(self, a: int) -> MD:
        """Coefficient of eps_a (a multi-dual in the remaining directions)."""
        bit = 1 << a
        return MD({m ^ bit: v for m, v in self.c.items() if m & bit})

    def without(self, a: int) -> MD:
        bit = 1 << a
        return MD({m: v for m, v in self.c.items() if not m & bit})

    def only_primal(self) -> MD:
        return MD({0: self.c[0]})

    def __add__(self, o: MD | np.ndarray | float) -> MD:
        o = MD.lift(o)
        c = dict(self.c)
        for m, v in o.c.items():
            c[m] = c[m] + v if m in c else v
        return MD(c)

    __radd__ = __add__

    def __neg__(self) -> MD:
        return MD({m: -v for m, v in self.c.items()})

    def __sub__(self, o: MD | np.ndarray | float) -> MD:
        return self + (-MD.lift(o))

    def __rsub__(self, o: MD | np.ndarray | float) -> MD:
        return MD.lift(o) + (-self)

    def scale(self, s: float) -> MD:
        return MD({m: s * v for m, v in self.c.items()})

    def __mul__(self, o: MD | np.ndarray | float) -> MD:
        """Elementwise (broadcasting) product."""
        o = MD.lift(o)
        c: dict[int, np.ndarray] = {}
        for ma, va in self.c.items():
            for mb, vb in o.c.items():
                if ma & mb:
                    continue
                m = ma | mb
                t = va * vb
                c[m] = c[m] + t if m in c else t
        return MD(c)

    __rmul__ = __mul__

    def __truediv__(self, s: float) -> MD:
        return self.scale(1.0 / s)

    def __matmul__(self, o: MD | np.ndarray) -> MD:
        o = MD.lift(o)
        c: dict[int, np.ndarray] = {}
        for ma, va in self.c.items():
            for mb, vb in o.c.items():
                if ma & mb:
                    continue
                m = ma | mb
                t = va @ vb
                c[m] = c[m] + t if m in c else t
        return MD(c)

    def __rmatmul__(self, o: np.ndarray) -> MD:
        return MD.const(o) @ self

    def map(self, f: Callable[[np.ndarray], np.ndarray]) -> MD:
        return MD({m: f(v) for m, v in self.c.items()})

    @property
    def T(self) -> MD:  # noqa: N802
        return self.map(lambda v: v.T)

    def norm(self) -> float:
        return max(float(np.abs(v).max()) for v in self.c.values())

    def powi(self, k: int) -> MD:
        out = MD.const(1.0)
        for _ in range(k):
            out = out * self
        return out


def md_einsum(subs: str, *ops: MD | np.ndarray) -> MD:
    """einsum over multi-dual operands (multilinear: expand in the nilpotents)."""
    md_idx = [i for i, o in enumerate(ops) if isinstance(o, MD)]
    arrays: list = [None if isinstance(o, MD) else o for o in ops]
    c: dict[int, np.ndarray] = {}

    def rec(j: int, mask: int) -> None:
        if j == len(md_idx):
            t = np.einsum(subs, *arrays)
            c[mask] = c[mask] + t if mask in c else t
            return
        i = md_idx[j]
        for m, v in ops[i].c.items():
            if m & mask:
                continue
            arrays[i] = v
            rec(j + 1, mask | m)

    rec(0, 0)
    return MD(c)


def md_solve(A: MD, V: MD | np.ndarray) -> MD:
    """Solve A X = V for multi-dual A (square matrix) and V (matrix or vector)."""
    V = MD.lift(V)
    A0 = A.c[0]
    # every subset of the directions present in A or V can appear in X = A^{-1} V (the
    # inverse is a full series in the nilpotents), so the recursion runs over all of them
    allbits = 0
    for mm in list(A.c) + list(V.c):
        allbits |= mm
    allm = [s for s in range(allbits + 1) if s & allbits == s]
    X: dict[int, np.ndarray] = {}
    for S in sorted(allm, key=_popcount):
        rhs = V.c[S].copy() if S in V.c else None
        for mA, vA in A.c.items():
            if mA == 0 or (mA & S) != mA:
                continue
            rest = S ^ mA
            if rest in X:
                t = vA @ X[rest]
                rhs = -t if rhs is None else rhs - t
        if rhs is None:
            continue
        X[S] = np.linalg.solve(A0, rhs)
    return MD(X)


def md_inv(A: MD) -> MD:
    return md_solve(A, np.eye(A.c[0].shape[0]))


# ============================================================ the finite model
class Model:
    """The tensors of verify-b3-sextic.py lines 79–190 (verbatim construction)."""

    def __init__(self, N: int, seed: int) -> None:
        rng = np.random.default_rng(seed)
        self.N, self.seed = N, seed

        def sym_tensor(shape: tuple[int, ...]) -> np.ndarray:
            T = rng.standard_normal(shape)
            S = np.zeros_like(T)
            for perm in itertools.permutations(range(len(shape))):
                S += np.transpose(T, perm)
            return S / math.factorial(len(shape))

        V4 = sym_tensor((N,) * 4)
        V5 = sym_tensor((N,) * 5)
        V6 = sym_tensor((N,) * 6)
        Lam = []
        for a in range(N):
            E = np.zeros((N, N))
            E[a, a] = 1.0
            Lam.append(E)
        for a in range(N):
            for b in range(a + 1, N):
                E = np.zeros((N, N))
                E[a, b] = E[b, a] = 1 / np.sqrt(2)
                Lam.append(E)
        self.Lam = np.array(Lam)
        self.D = len(Lam)
        self.V4S = np.einsum('abcd,Iab,Jcd->IJ', V4, self.Lam, self.Lam)
        self.V5S = np.einsum('abcde,Iab,Jcd->IJe', V5, self.Lam, self.Lam)
        V6S3 = np.einsum('abcdef,Iab,Jcd,Kef->IJK', V6, self.Lam, self.Lam, self.Lam)
        V4inv = np.linalg.inv(self.V4S)
        C_raw = np.einsum('Kef,MIe,MN,NJf->IJK', self.Lam, self.V5S, V4inv, self.V5S)
        T_C = (C_raw + C_raw.transpose(2, 1, 0) + C_raw.transpose(0, 2, 1)) / 3.0
        self.Ta = V6S3 - (6.0 / 5.0) * T_C          # T = V6 - (6/5) C, Psi-independent
        self.pinv = V4inv
        self.rng = rng

    # --- Sigma-sector action divided by g^2 (polynomial in g) ---
    def pvec(self, psi: MD) -> MD:
        return md_einsum('Iab,a,b->I', self.Lam, psi, psi)

    def odot(self, u: MD | np.ndarray, psi: MD | np.ndarray) -> MD:
        """u (.) psi in Sym^2 coordinates: d_u P = 2 u (.) psi."""
        return md_einsum('Iab,a,b->I', self.Lam, u, psi)

    def grad_red(self, sig: MD, psi: MD, g: MD) -> MD:
        p = self.pvec(psi)
        return ((self.V4S @ (p - sig)) / 12.0
                + (g / 60.0) * md_einsum('IJe,J,e->I', self.V5S, sig, psi)
                + (g.powi(2) / 240.0) * md_einsum('IJK,J,K->I', self.Ta, sig, sig))

    def hess_red(self, sig: MD, psi: MD, g: MD) -> MD:
        return (MD.const(-self.V4S / 12.0)
                + (g / 60.0) * md_einsum('IJe,e->IJ', self.V5S, psi)
                + (g.powi(2) / 120.0) * md_einsum('IJK,K->IJ', self.Ta, sig))

    def saddle(self, psi: MD, g: MD) -> MD:
        """Newton for Sigma_* (perturbative branch), forward mode through the iteration."""
        psi0, g0 = psi.primal, float(g.primal)
        sig0 = MD.const(self.pvec(MD.const(psi0)).primal)
        # primal continuation in g (as solve_saddle of verify-b3-sextic.py)
        for gcur in np.linspace(0.0, g0, 2 + int(g0 / 0.02))[1:]:
            gm, pm = MD.const(gcur), MD.const(psi0)
            for _ in range(60):
                gr, he = self.grad_red(sig0, pm, gm), self.hess_red(sig0, pm, gm)
                sig0 = sig0 - md_solve(he, gr)
                if np.abs(gr.primal).max() < 1e-15:
                    break
        # multi-dual iterations at the seeded (psi, g): the primal is converged, each
        # further Newton step converges one more nilpotent order (Newton map has zero
        # derivative at the fixed point)
        sig = sig0
        allmask = 0
        for mm in list(psi.c) + list(g.c):
            allmask |= mm
        for _ in range(_popcount(allmask) + 3):
            gr, he = self.grad_red(sig, psi, g), self.hess_red(sig, psi, g)
            sig = sig - md_solve(he, gr)
        gr = self.grad_red(sig, psi, g)
        assert gr.norm() < 1e-11, f"saddle not converged: {gr.norm():.1e}"
        return sig

    def Kcal(self, psi: MD, g: MD, sig: MD | None = None) -> MD:
        """Kcal = -(12/g^2) hess at the saddle = p - (g/5) V5.Psi - (g^2/10) T.Sigma_*."""
        if sig is None:
            sig = self.saddle(psi, g)
        return (MD.const(self.V4S)
                - (g / 5.0) * md_einsum('IJe,e->IJ', self.V5S, psi)
                - (g.powi(2) / 10.0) * md_einsum('IJK,K->IJ', self.Ta, sig))

    def Kpsi(self, psi: MD, g: MD) -> MD:
        """K_Psi = p - (g/5) V5.Psi (the O(g_s^3) Hessian of 043)."""
        return MD.const(self.V4S) - (g / 5.0) * md_einsum('IJe,e->IJ', self.V5S, psi)

    def A(self, w: np.ndarray) -> np.ndarray:
        return self.pinv @ np.einsum('IJe,e->IJ', self.V5S, w)

    def B(self, w: np.ndarray) -> np.ndarray:
        return self.pinv @ np.einsum('IJK,K->IJ', self.Ta, w)

    # --- Phi* and the invariance residual ---
    def TY(self, Y: MD) -> MD:
        """T(., Y, .) as a matrix."""
        return md_einsum('IJK,J->IK', self.Ta, Y)

    def nu(self, Y: MD, K: MD, g: MD) -> MD:
        return Y - (g.powi(2) / 20.0) * md_solve(K, md_einsum('IJK,J,K->I', self.Ta, Y, Y))

    def inv_residual(self, F: MD, Y: MD, K: MD, dK: MD, g: MD) -> tuple[float, float]:
        """(3.2): Kcal(nu(Y), F) + (1/2) dK(Y,Y); returns (|residual|, scale)."""
        r = md_einsum('I,IJ,J->', self.nu(Y, K, g), K, F) + 0.5 * md_einsum('I,IJ,J->', Y, dK, Y)
        s = 0.5 * md_einsum('I,IJ,J->', Y, dK, Y)
        return abs(float(r.primal)), abs(float(s.primal))


# ============================================================ laws
def law_R19(m: Model, Y: MD, K: MD, dK: MD, g: MD) -> MD:
    """F^(19): (Kcal - (g^2/20) T_Y) F = -(1/2) dK Y  (record (1.2), 013 boxed law)."""
    return md_solve(K - (g.powi(2) / 20.0) * m.TY(Y), (-0.5) * (dK @ Y))


def law_R19_noT(m: Model, Y: MD, K: MD, dK: MD, g: MD) -> MD:
    """Break law: R19's linear part alone (T-correction dropped): not admissible."""
    return md_solve(K, (-0.5) * (dK @ Y))


def law_R17(m: Model, Y: MD, Kp: MD, dKp: MD, g: MD) -> MD:
    """R17 = -(1/2) K_Psi^{-1} d_u K_Psi acting on Y (043's law, T -> 0)."""
    return md_solve(Kp, (-0.5) * (dKp @ Y))


# ============================================================ Morse map (5.3)–(5.4)
def shuffle_sym(X: MD, a: int, n1: int) -> MD:
    """Symmetrise the rank-n1 tensor X over all indices, given that its first a and its
    last n1-a indices are already symmetric (sum over the C(n1,a) shuffles)."""
    out: MD | None = None
    cnt = 0
    for pos in itertools.combinations(range(n1), a):
        rest = [k for k in range(n1) if k not in pos]
        axes = [0] * n1
        for j, k in enumerate(pos):
            axes[k] = j
        for j, k in enumerate(rest):
            axes[k] = a + j
        term = X.map(lambda v, ax=tuple(axes): np.transpose(v, ax))
        out = term if out is None else out + term
        cnt += 1
    assert out is not None
    return out / cnt


def morse_tensors(m: Model, K: MD, g: MD, nmax: int) -> dict[int, MD]:
    """The symmetric tensors q_n[I, J1..Jn] of (5.3)–(5.4), n = 2..nmax, canonical solution
    q_n(Y^n) = (1/2) Kcal^{-1} omega_{n+1}(., Y^n)."""
    D = m.D
    q: dict[int, MD] = {}
    om3 = (-(1.0 / 30.0)) * g.powi(2) * MD.const(m.Ta)
    q[2] = md_solve(K, om3.map(lambda v: v.reshape(D, D * D))).map(
        lambda v: 0.5 * v.reshape(D, D, D))
    for n in range(3, nmax + 1):
        om: MD | None = None
        for a in range(2, n):
            b = n + 1 - a
            if b < 2 or a > b:
                continue
            # X[J1..Ja, L1..Lb] = q_a[I, J..] K[I,I'] q_b[I', L..]
            qa = q[a].map(lambda v, a=a: v.reshape(D, D ** a))
            qb = q[b].map(lambda v, b=b: v.reshape(D, D ** b))
            X = md_einsum('Ij,IK,Kl->jl', qa, K, qb).map(lambda v: v.reshape((D,) * (n + 1)))
            Xs = shuffle_sym(X, a, n + 1)
            if a != b:
                Xs = Xs.scale(2.0)
            om = Xs if om is None else om + Xs
        assert om is not None
        om = -om
        q[n] = md_solve(K, om.map(lambda v: v.reshape(D, D ** n))).map(
            lambda v, n=n: 0.5 * v.reshape((D,) * (n + 1)))
    return q


def gtilde(m: Model, q: dict[int, MD], Y: MD) -> MD:
    """G-tilde(Y) = Y + sum_n q_n(Y^n)."""
    out = Y
    letters = 'abcdefghijklmnop'
    for n, qn in q.items():
        subs = 'I' + letters[:n] + ',' + ','.join(letters[:n]) + '->I'
        out = out + md_einsum(subs, qn, *([Y] * n))
    return out


def gtilde_jac(m: Model, q: dict[int, MD], Y: MD) -> MD:
    """D_Y G-tilde = 1 + sum_n n q_n(Y^{n-1}, .)."""
    out = MD.const(np.eye(m.D))
    letters = 'abcdefghijklmnop'
    for n, qn in q.items():
        subs = 'I' + letters[:n] + ',' + ','.join(letters[:n - 1]) + '->I' + letters[n - 1]
        out = out + md_einsum(subs, qn, *([Y] * (n - 1))).scale(float(n))
    return out


def sqrtm_db(M: MD, extra: int) -> tuple[MD, MD]:
    """Denman–Beavers: (M^{1/2}, M^{-1/2}); only inverses and sums (forward-mode safe)."""
    Yk, Zk = M, MD.const(np.eye(M.c[0].shape[0]))
    for _ in range(60):
        Yn = (Yk + md_inv(Zk)) / 2.0
        Zn = (Zk + md_inv(Yk)) / 2.0
        delta = np.abs(Yn.primal - Yk.primal).max()
        Yk, Zk = Yn, Zn
        if delta < 1e-16:
            break
    for _ in range(extra):
        Yn = (Yk + md_inv(Zk)) / 2.0
        Zn = (Zk + md_inv(Yk)) / 2.0
        Yk, Zk = Yn, Zn
    return Yk, Zk


class FlatLaw:
    """F^flat_u = -(D_Y G)^{-1} d_u G with G = M_K^{1/2} G-tilde (record (5.6))."""

    def __init__(self, m: Model, psi: MD, g: MD, nmax: int, with_morse: bool = True) -> None:
        self.m = m
        self.K = m.Kcal(psi, g)
        M = MD.const(m.pinv) @ self.K
        allmask = 0
        for mm in list(psi.c) + list(g.c):   # g nilpotents too (C3.2-expansion)
            allmask |= mm
        self.Mh, self.Mmh = sqrtm_db(M, extra=_popcount(allmask) + 3)
        self.q = morse_tensors(m, self.K, g, nmax) if with_morse else {}

    def G(self, Y: MD) -> MD:
        return self.Mh @ gtilde(self.m, self.q, Y)

    def jac(self, Y: MD) -> MD:
        return self.Mh @ gtilde_jac(self.m, self.q, Y)

    def law(self, Y: MD, a: int) -> MD:
        """F^flat_u(Y): u is the direction seeded in bit a of Psi."""
        dG = self.G(Y).d(a)
        J = self.jac(Y.without(a)).without(a)
        return -md_solve(J, dG)

    def truncated(self, n: int) -> FlatLaw:
        """The same object with the Morse map truncated at q_n."""
        other = object.__new__(FlatLaw)
        other.m, other.K, other.Mh, other.Mmh = self.m, self.K, self.Mh, self.Mmh
        other.q = {k: v for k, v in self.q.items() if k <= n}
        return other



# ============================================================ run
U1, U2, W = 0, 1, 2      # direction bits: u1, u2, Y-direction for the Lie bracket
GBITS = (3, 4, 5, 6)     # nilpotent g directions for the exact Taylor coefficients


def curvature(law: Callable[[MD, int], MD], Y0: MD) -> tuple[MD, float]:
    """E_4 = d_{u1} F_{u2} - d_{u2} F_{u1} + D_Y F_{u2}.F_{u1} - D_Y F_{u1}.F_{u2}   (4.1).

    ``law(Y, a)`` returns F_u(Y; Psi) with u the direction seeded in bit a of Psi (the Psi
    seeds are captured by the closure).  Y0 carries no u1, u2, W seeds.  Returns E_4 (a
    multi-dual in the remaining directions, e.g. the g-nilpotents) and the scale
    max |term| (primal)."""
    F2 = law(Y0, U2)                     # F_{u2}, still carrying eps_{u1}
    F1 = law(Y0, U1)
    d1F2, d2F1 = F2.d(U1), F1.d(U2)
    F1r, F2r = F1.without(U2), F2.without(U1)
    Yw1 = Y0 + MD({1 << W: 1.0}) * F1r   # Y + eps_W F_{u1}
    Yw2 = Y0 + MD({1 << W: 1.0}) * F2r
    DF2_F1 = law(Yw1, U2).d(W).without(U1)
    DF1_F2 = law(Yw2, U1).d(W).without(U2)
    E = d1F2 - d2F1 + DF2_F1 - DF1_F2
    scale = max(np.abs(t.primal).max() for t in (d1F2, d2F1, DF2_F1, DF1_F2))
    return E, float(scale)


def taylor(X: MD, k: int) -> np.ndarray:
    """Exact coefficient of g^k from the nilpotent-g components (all k-subsets agree)."""
    vals = []
    for sub in itertools.combinations(GBITS, k):
        mask = sum(1 << b for b in sub)
        vals.append(X.c.get(mask, np.zeros_like(X.c[0])) / math.factorial(k))
    for v in vals[1:]:
        assert np.allclose(v, vals[0], atol=1e-12, rtol=1e-8), "nilpotent bookkeeping"
    return vals[0]


def slope(r1: float, r2: float) -> float:
    """log2 ratio of residuals at g and g/2."""
    return math.log2(r1 / r2) if r2 > 0 and r1 > 0 else float('nan')


def rel(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.abs(a - b).max() / np.abs(b).max())


def main() -> int:  # noqa: PLR0915, PLR0912
    print(f"verify-gauge-algebra-ogs4.py — seeds {SEEDS}, N in {NS}, g in {GS}")
    worst: dict[str, float] = {}      # max over configurations
    least: dict[str, float] = {}      # min over configurations (break legs, nonzero-ness)
    c31: dict[str, dict[float, float]] = {}
    c3adm: dict[str, dict[float, float]] = {}
    trunc_level: dict[str, float] = {}
    slopes_rich: dict[str, list[float]] = {}

    def upd(key: str, val: float) -> None:
        worst[key] = max(worst.get(key, 0.0), float(val))

    def low(key: str, val: float) -> None:
        least[key] = min(least.get(key, np.inf), float(val))

    def mk_law(m: Model, Kf: MD, lawf: Callable, g: MD) -> Callable[[MD, int], MD]:
        def law(Y: MD, a: int) -> MD:
            return lawf(m, Y, Kf.without(a), Kf.d(a), g)
        return law

    for N in NS:
        for seed in SEEDS:
            m = Model(N, seed)
            D = m.D
            rng = np.random.default_rng(seed + 7)
            psi0 = rng.standard_normal(N)
            u1, u2 = rng.standard_normal(N), rng.standard_normal(N)
            # |Y| ~ 1 at D = 6 (the Y-series of the Morse map and of R19's law has a finite
            # radius; at |Y| ~ sqrt(6) the rank-8 tensor budget does not reach rounding)
            Y0v = rng.standard_normal(D) * (1.0 if D == 3 else 0.3)
            tag = f"D{D}-s{seed}"
            print(f"\n=== N={N} (D={D}), seed {seed} ===", flush=True)

            # ---------------------------------------------------------------- S0
            for gv in GS:
                g = MD.const(gv)
                psi = MD.seed(psi0, {U1: u1})
                sig = m.saddle(psi, g)
                K = m.Kcal(psi, g, sig)
                pv = m.pvec(MD.const(psi0)).primal

                def S4red(s: np.ndarray) -> float:
                    """(S4 - shared)/g^2 as a function of Sigma (verify-b3-sextic.py)."""
                    return float(-(1 / 24) * s @ m.V4S @ s + (1 / 12) * s @ m.V4S @ pv
                                 + (gv / 120) * np.einsum('IJe,I,J,e->', m.V5S, s, s, psi0)
                                 + (gv**2 / 720) * np.einsum('IJK,I,J,K->', m.Ta, s, s, s))
                s0 = sig.primal
                phi_action = S4red(s0 + Y0v) - S4red(s0)
                phi_cubic = (-(1 / 24) * Y0v @ K.primal @ Y0v
                             + (gv**2 / 720) * np.einsum('IJK,I,J,K->', m.Ta, Y0v, Y0v, Y0v))
                upd("S0a", abs(phi_action - phi_cubic) / abs(phi_cubic))
                dK_fm = K.d(U1).primal
                he = m.hess_red(sig.only_primal(), MD.const(psi0), g).primal
                dP = 2 * m.odot(u1, psi0).primal
                dgrad = (m.V4S @ dP) / 12 + (gv / 60) * np.einsum('IJe,J,e->I', m.V5S, s0, u1)
                dsig = -np.linalg.solve(he, dgrad)
                dK_ift = (-(gv / 5) * np.einsum('IJe,e->IJ', m.V5S, u1)
                          - (gv**2 / 10) * np.einsum('IJK,K->IJ', m.Ta, dsig))
                upd("S0b", rel(dK_fm, dK_ift))

            # ---------------------------------------------------------------- C1.1, C1.3
            for gv in GS:
                g = MD.const(gv)
                psi = MD.seed(psi0, {U1: u1})
                Kfull = m.Kcal(psi, g)
                K, dK = Kfull.without(U1), Kfull.d(U1)
                Y = MD.const(Y0v)
                F19 = law_R19(m, Y, K, dK, g)
                r, s = m.inv_residual(F19, Y, K, dK, g)
                upd("C1.1", r / s)
                r, s = m.inv_residual(law_R19_noT(m, Y, K, dK, g), Y, K, dK, g)
                low("C1.1-break", r / s)
                S0 = rng.standard_normal((D, D)); S0 = S0 - S0.T
                S1 = rng.standard_normal((D, D, D)); S1 = S1 - S1.transpose(1, 0, 2)
                SY = MD.const(S0 + np.einsum('IJK,K->IJ', S1, Y0v))
                Fb = F19 + md_solve(K, SY @ m.nu(Y, K, g))
                r, s = m.inv_residual(Fb, Y, K, dK, g)
                upd("C1.3", r / s)
                Ssym = MD.const(S0 @ S0.T + 0.5 * np.eye(D))
                Fbad = F19 + md_solve(K, Ssym @ m.nu(Y, K, g))
                r, s = m.inv_residual(Fbad, Y, K, dK, g)
                low("C1.3-break", r / s)

            # ---------------------------------------------------------------- C1.2
            def sym3(Tt: np.ndarray) -> np.ndarray:
                S = np.zeros_like(Tt)
                for perm in itertools.permutations(range(3)):
                    S += np.transpose(Tt, perm)
                return S / 6

            basis = []
            for i in range(D):
                for j in range(i + 1, D):
                    S = np.zeros((D, D)); S[i, j] = 1; S[j, i] = -1
                    basis.append(m.pinv @ S)

            def ls_system(Ta: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
                def cubic_form(Mx: np.ndarray) -> np.ndarray:
                    return sym3(np.einsum('IJK,IL->LJK', Ta, Mx))
                Amat = np.array([cubic_form(Bm).ravel() for Bm in basis]).T
                bvec = -(0.1 / 10) * cubic_form(m.A(u1)).ravel()     # g = 0.1, leading order
                return Amat, bvec

            def ls_residual(Amat: np.ndarray, bvec: np.ndarray) -> tuple[float, int]:
                sol, _, rank, _ = np.linalg.lstsq(Amat, bvec, rcond=None)
                nb = np.linalg.norm(bvec)
                return (np.linalg.norm(Amat @ sol - bvec) / nb if nb > 0 else 0.0), rank

            Amat, bvec = ls_system(m.Ta)
            res, rank = ls_residual(Amat, bvec)
            print(f"  C1.2: D={D}, {D*(D-1)//2} unknowns vs {math.comb(D+2,3)} equations, "
                  f"rank {rank}, relative LS residual of (3.7): {res:.3f}")
            low(f"C1.2-D{D}", res)
            upd("C1.2-break-T0", ls_residual(*ls_system(0 * m.Ta))[0])
            xin = rng.standard_normal(len(basis))
            upd("C1.2-break-image", ls_residual(Amat, Amat @ xin)[0])

            # ---------------------------------------------------------------- C2.2, C2.3 exact (nilpotent g)
            gN = MD({0: 0.0} | {(1 << b): 1.0 for b in GBITS})
            psiN = MD.seed(psi0, {U1: u1, U2: u2})
            KN = m.Kcal(psiN, gN)
            KpN = m.Kpsi(psiN, gN)
            A1, A2, Ap = m.A(u1), m.A(u2), m.A(psi0)
            B1, B2 = m.B(m.odot(u1, psi0).primal), m.B(m.odot(u2, psi0).primal)
            c2_pred = (A1 @ A2 - A2 @ A1) @ Y0v / 100                                         # 043 / (4.5)
            c3_pred_new = ((A1 @ B2 - B2 @ A1) - (A2 @ B1 - B1 @ A2)) @ Y0v / 100             # (4.7)
            c3_E3_pred = ((A1 @ Ap @ A2 - Ap @ A2 @ A1) + (Ap @ A1 @ A2 - A2 @ Ap @ A1)) @ Y0v / 500  # E_3 at g^3
            s1 = m.pinv @ np.einsum('IJK,J,K->I', m.Ta, Y0v, (A1 @ A2 - A2 @ A1) @ Y0v)
            s2 = (A2 @ (m.pinv @ np.einsum('IJK,J,K->I', m.Ta, Y0v, A1 @ Y0v))
                  - A1 @ (m.pinv @ np.einsum('IJK,J,K->I', m.Ta, Y0v, A2 @ Y0v)))
            c4q_pred = s1 / 2000 - s2 / 2000                                                  # (4.8), corrected (fix pass)
            c4q_wrong = s1 / 1000 - s2 / 2000                                                 # break of C2.3
            c4q_old = s1 / 2000 - 19 * s2 / 2000                                              # (4.8) as first written (Richardson break)
            t0 = time.time()
            E4p, _ = curvature(mk_law(m, KN, law_R19, gN), MD.const(Y0v))
            E4m, _ = curvature(mk_law(m, KN, law_R19, gN), MD.const(-Y0v))
            E3, _ = curvature(mk_law(m, KpN, law_R17, gN), MD.const(Y0v))
            E4lin, E4quad = (E4p - E4m) / 2, (E4p + E4m) / 2
            Kc = KN.without(U1).without(U2)
            R1 = md_solve(Kc, (-0.5) * KN.d(U1).without(U2))
            R2 = md_solve(Kc, (-0.5) * KN.d(U2).without(U1))
            comm = (R1 @ R2 - R2 @ R1) @ MD.const(Y0v)
            upd("C2.2-exact", (E4lin - comm).norm() / comm.norm())
            c2 = taylor(E4lin, 2)
            upd("C2.2-c01", (np.abs(taylor(E4lin, 0)).max() + np.abs(taylor(E4lin, 1)).max()) / np.abs(c2).max())
            upd("C2.2-c2", rel(c2, c2_pred))
            c3, c3E3 = taylor(E4lin, 3), taylor(E3, 3)
            upd("C2.2-c3E3", rel(c3E3, c3_E3_pred))
            upd("C2.2-c3", rel(c3 - c3E3, c3_pred_new))
            low("C2.2-c3-break", rel(c3 - c3E3, 2 * c3_pred_new))
            upd("C2.3-lowzero", max(np.abs(taylor(E4quad, k)).max() for k in range(4)) / np.abs(c2).max())
            c4q = taylor(E4quad, 4)
            err48 = rel(c4q, c4q_pred)
            upd("C2.3", err48)
            low("C2.3-break", rel(c4q, c4q_wrong))
            Mfit = np.stack([s1, s2], axis=1)
            coef, *_ = np.linalg.lstsq(Mfit, c4q, rcond=None)
            fit_res = np.linalg.norm(Mfit @ coef - c4q) / np.linalg.norm(c4q)
            print(f"  C2.2/C2.3 exact (nilpotent g, {time.time()-t0:.0f}s): |E^(1)-[R1,R2]Y| rel {worst['C2.2-exact']:.1e}; "
                  f"c3-c3[E3] vs (4.7): {rel(c3 - c3E3, c3_pred_new):.1e}; c3[E3] vs (1/500)(...): {rel(c3E3, c3_E3_pred):.1e}")
            print(f"  C2.3 diag: g^4 quadratic sector = a*s1 + b*s2 with fitted (a, b) = "
                  f"({coef[0]*2000:.6f}/2000, {coef[1]*2000:.6f}/2000), fit residual {fit_res:.1e}; "
                  f"(4.8) says (1/2000, -1/2000): rel. error {err48:.2e}", flush=True)
            c4q_fit = coef[0] * s1 + coef[1] * s2

            # ---------------------------------------------------------------- C2.1 and C2-R at fixed g
            rich: dict[str, list[float]] = {"E": [], "lin-c2": [], "lin-c3": [], "lin-c3-break": [], "quad-c4": [], "quad-c4-fit": [], "quad-c4-break": []}
            for gv in GS_RICH:
                g = MD.const(gv)
                psi = MD.seed(psi0, {U1: u1, U2: u2})
                Kf = m.Kcal(psi, g)
                lawf = mk_law(m, Kf, law_R19, g)
                Kc = Kf.without(U1).without(U2)
                ts = (1.0, -1.0, 0.5, -0.5, 0.25, -0.25)
                Es = []
                for t in ts:
                    E, sc = curvature(lawf, MD.const(t * Y0v))
                    Es.append(E.primal)
                    if t == 1.0 and gv in GS:
                        nuv = m.nu(MD.const(Y0v), Kc, g)
                        Knu = Kc.primal @ nuv.primal
                        upd("C2.1", abs(Knu @ E.primal) / (np.linalg.norm(Knu) * np.linalg.norm(E.primal)))
                        low("C2.1-nonzero", np.linalg.norm(E.primal) / sc)
                        Eb, _ = curvature(mk_law(m, Kf, law_R19_noT, g), MD.const(Y0v))
                        low("C2.1-break", abs(Knu @ Eb.primal) / (np.linalg.norm(Knu) * np.linalg.norm(Eb.primal)))
                V = np.array([[t**n for n in range(1, 7)] for t in ts])
                coeffs = np.linalg.solve(V, np.array(Es))
                E1, E2 = coeffs[0], coeffs[1]
                rich["E"].append(np.linalg.norm(E1 + E2))
                rich["lin-c2"].append(np.linalg.norm(E1 - gv**2 * c2_pred))
                rich["lin-c3"].append(np.linalg.norm(E1 - gv**2 * c2_pred - gv**3 * (c3_pred_new + c3_E3_pred)))
                rich["lin-c3-break"].append(np.linalg.norm(E1 - gv**2 * c2_pred - gv**3 * (2 * c3_pred_new + c3_E3_pred)))
                rich["quad-c4"].append(np.linalg.norm(E2 - gv**4 * c4q_pred))
                rich["quad-c4-fit"].append(np.linalg.norm(E2 - gv**4 * c4q_fit))
                rich["quad-c4-break"].append(np.linalg.norm(E2 - gv**4 * c4q_old))
            print("  Richardson (g halving over " + ", ".join(f"{gv}" for gv in GS_RICH) + "):")
            for key, target in (("E", 2), ("lin-c2", 3), ("lin-c3", 4), ("lin-c3-break", 3), ("quad-c4", 5), ("quad-c4-fit", 5), ("quad-c4-break", 4)):
                sl = [slope(rich[key][i], rich[key][i + 1]) for i in range(len(GS_RICH) - 1)]
                print(f"    {key:13s} residual norms {[f'{r:.2e}' for r in rich[key]]}  slopes {[f'{x:.2f}' for x in sl]}  (expected {target})")
                slopes_rich.setdefault(key, []).append(sl[-1])

            # ---------------------------------------------------------------- C3.2-expansion (exact Taylor, nilpotent g)
            # Boxed (5.6), corrected on the fix pass: the Y-quadratic part of
            # F^flat = -(D_Y G)^{-1} d_u G is, at its leading order g^3,
            #   (g^2/60) R19_u Kcal^{-1} T(., Y, Y) + (g^2/30) Kcal^{-1} T(., Y, R19_u Y),
            # R19_u = -(1/2) Kcal^{-1} d_u Kcal = (g/10) A_u + O(g^2).  F^flat is computed
            # directly from G (FlatLaw.law), never from the expansion.  Even part in Y:
            # (F(Y) + F(-Y))/2; its Y^4 part starts at g^7 (q_n = O(g^{2(n-1)})), so at g^3 it
            # is the Y^2 part alone (homogeneity checked with Y -> 2Y).
            t0 = time.time()
            psiE = MD.seed(psi0, {U1: u1})
            flN = FlatLaw(m, psiE, gN, 3)
            sqr = (flN.Mh @ flN.Mh - MD.const(m.pinv) @ flN.K).norm() / flN.K.norm()
            assert sqr < 1e-10, f"M^1/2 with nilpotent g: {sqr:.1e}"
            def fquad(Yv: np.ndarray) -> MD:
                return (flN.law(MD.const(Yv), U1) + flN.law(MD.const(-Yv), U1)) / 2.0
            Fq, Fq2 = fquad(Y0v), fquad(2 * Y0v)
            cq3 = taylor(Fq, 3)
            KE = flN.K.without(U1)
            RE = md_solve(KE, (-0.5) * flN.K.d(U1))
            YE = MD.const(Y0v)
            TYYE = md_solve(KE, md_einsum('IJK,J,K->I', m.Ta, YE, YE))
            pred56 = ((gN.powi(2) / 60.0) * (RE @ TYYE)
                      + (gN.powi(2) / 30.0) * md_solve(KE, md_einsum('IJK,J,K->I', m.Ta, YE, RE @ YE)))
            old56 = (gN.powi(2) / 30.0) * (RE @ TYYE)                    # (5.6) as first written
            Au = m.A(u1)
            hand56 = (Au @ (m.pinv @ np.einsum('IJK,J,K->I', m.Ta, Y0v, Y0v)) / 600
                      + m.pinv @ np.einsum('IJK,J,K->I', m.Ta, Y0v, Au @ Y0v) / 300)
            upd("C3.2-exp-low", max(np.abs(taylor(Fq, k)).max() for k in range(3)) / np.abs(cq3).max())
            upd("C3.2-exp", rel(cq3, taylor(pred56, 3)))
            upd("C3.2-exp-hand", rel(cq3, hand56))
            upd("C3.2-exp-homog", rel(taylor(Fq2, 3), 4 * cq3))
            low("C3.2-exp-break", rel(cq3, taylor(old56, 3)))
            print(f"  C3.2-expansion ({time.time()-t0:.0f}s): g^3 coeff of the Y^2 part of F^flat vs corrected (5.6): "
                  f"{rel(cq3, taylor(pred56, 3)):.1e}; vs hand form (1/600)A_u p^-1T(Y,Y)+(1/300)p^-1T(Y,A_uY): "
                  f"{rel(cq3, hand56):.1e}; vs (5.6) as first written: {rel(cq3, taylor(old56, 3)):.2f}", flush=True)

            # ---------------------------------------------------------------- C3.1 and C3
            nmax = 10 if D == 3 else 7
            for gv in GS_MORSE:
                g = MD.const(gv)
                psi = MD.seed(psi0, {U1: u1, U2: u2})
                t0 = time.time()
                fl = FlatLaw(m, psi, g, nmax)
                Kc = fl.K.without(U1).without(U2)
                Y = MD.const(Y0v)
                phi = (-(1 / 24) * float(md_einsum('I,IJ,J->', Y, Kc, Y).primal)
                       + (gv**2 / 720) * np.einsum('IJK,I,J,K->', m.Ta, Y0v, Y0v, Y0v))
                for n in range(2, nmax + 1):
                    qn = {k: v for k, v in fl.q.items() if k <= n}
                    Yh = fl.Mh @ gtilde(m, qn, Y)
                    resid = abs(phi + (1 / 24) * float(md_einsum('I,IJ,J->', Yh, MD.const(m.V4S), Yh).primal)) / abs(phi)
                    c31.setdefault(f"{tag}-n{n}", {})[gv] = resid
                print(f"  C3.1 g={gv}: relative residual of (5.5) by truncation n: "
                      + ", ".join(f"n={n}: {c31[f'{tag}-n{n}'][gv]:.1e}" for n in range(2, nmax + 1))
                      + f"  [{time.time()-t0:.0f}s]", flush=True)
                K1 = fl.K.without(U2)
                # admissibility residual of F^flat by truncation order (tracks the (5.5) residual)
                Ffl = fl.law(Y, U1).without(U2)
                r, s = m.inv_residual(Ffl, Y, K1.without(U1), K1.d(U1), g)
                radm = {n: m.inv_residual(fl.truncated(n).law(Y, U1).without(U2), Y, K1.without(U1), K1.d(U1), g)[0] / s
                        for n in range(2, nmax + 1)}
                for n, v in radm.items():
                    c3adm.setdefault(f"{tag}-n{n}", {})[gv] = v
                rho = np.linalg.norm(np.linalg.solve(Kc.primal, (gv**2 / 20) * m.TY(Y).primal), 2)
                print(f"  C3 g={gv}: invariance residual of F^flat by truncation n: "
                      + ", ".join(f"n={n}: {v:.1e}" for n, v in radm.items()) + f"; |(g^2/20) K^-1 T_Y|_2 = {rho:.2f}")
                if gv not in GS:
                    continue
                Eflat, sc = curvature(fl.law, Y)
                upd("C3-flat", np.linalg.norm(Eflat.primal) / sc)
                worst[f"C3-adm-{tag}-g{gv}"] = r / s
                trunc_level[f"{tag}-g{gv}"] = c31[f"{tag}-n{nmax}"][gv]
                fl0 = FlatLaw(m, psi, g, nmax, with_morse=False)
                E0, sc0 = curvature(fl0.law, Y)
                upd("C3-break1-flat", np.linalg.norm(E0.primal) / sc0)
                r0, s0 = m.inv_residual(fl0.law(Y, U1).without(U2), Y, K1.without(U1), K1.d(U1), g)
                worst[f"C3-break1-adm-{tag}-g{gv}"] = r0 / s0
                E19, sc19 = curvature(mk_law(m, fl.K, law_R19, g), Y)
                low("C3-break2-flat", np.linalg.norm(E19.primal) / sc19)
                F19 = law_R19(m, Y, K1.without(U1), K1.d(U1), g).without(U2)
                r19, s19 = m.inv_residual(F19, Y, K1.without(U1), K1.d(U1), g)
                upd("C3-break2-adm", r19 / s19)
                print(f"  C3 g={gv}: |E4[F^flat]|/scale {np.linalg.norm(Eflat.primal)/sc:.1e}, inv. residual F^flat {r/s:.1e}; "
                      f"break1 (M^1/2 alone): |E4| {np.linalg.norm(E0.primal)/sc0:.1e}, residual {r0/s0:.1e}; "
                      f"break2 (F19): |E4| {np.linalg.norm(E19.primal)/sc19:.1e}, residual {r19/s19:.1e}", flush=True)

            # ---------------------------------------------------------------- C3-invariants (documentary)
            gv = 0.1
            inv_vals = []
            for psiv in (psi0, psi0 + 0.7 * u1):
                K = m.Kcal(MD.const(psiv), MD.const(gv)).primal
                lam, Q = np.linalg.eigh(K)
                Kmh = Q @ np.diag(lam.astype(complex) ** -0.5) @ Q.T
                That = np.einsum('IJK,Ia,Jb,Kc->abc', m.Ta, Kmh, Kmh, Kmh)
                i1 = np.einsum('ijk,ijk->', That, That)
                ev = np.sort_complex(np.linalg.eigvals(np.einsum('ijk,ijl->kl', That, That)))
                inv_vals.append((i1, ev))
            print(f"  C3-inv (documentary, g={gv}): T-hat.T-hat = {inv_vals[0][0]:.6f} vs {inv_vals[1][0]:.6f}; "
                  f"eig(T-hat^2) = {np.round(inv_vals[0][1], 4)} vs {np.round(inv_vals[1][1], 4)}")

    # ================================================================ verdicts
    print("\n=== verdicts (worst over N, seeds, g) ===")
    report("S0", worst["S0a"] < TOL and worst["S0b"] < TOL,
           f"Phi* from the action = cubic form (rel. {worst['S0a']:.1e}); forward-mode d_u Kcal = IFT (rel. {worst['S0b']:.1e})")
    report("C1.1", worst["C1.1"] < TOL, f"invariance residual (3.2) of F^(19): {worst['C1.1']:.1e} (relative)")
    report_break("C1.1", least["C1.1-break"] > 1e-6,
                 f"the law without its T-correction is NOT admissible: residual >= {least['C1.1-break']:.1e}")
    report("C1.3", worst["C1.3"] < TOL, f"F^(19) + Kcal^-1 S(Y) nu(Y), S antisymmetric Y-dependent: residual {worst['C1.3']:.1e}")
    report_break("C1.3", least["C1.3-break"] > 1e-2, f"symmetric S breaks it: residual >= {least['C1.3-break']:.1e}")
    report("C1.2", least["C1.2-D3"] > 0.1 and least["C1.2-D6"] > 0.1,
           f"no Y-linear law: relative LS residual of (3.7) >= {least['C1.2-D3']:.3f} (D=3), {least['C1.2-D6']:.3f} (D=6)")
    report_break("C1.2", worst["C1.2-break-T0"] < TOL and worst["C1.2-break-image"] < 1e-8,
                 f"T -> 0: residual {worst['C1.2-break-T0']:.1e}; a source in the image: residual {worst['C1.2-break-image']:.1e}")
    report("C2.1", worst["C2.1"] < TOL,
           f"Kcal(nu, E_4[F^(19)]) = 0: {worst['C2.1']:.1e} (normalised); E_4 itself nonzero (>= {least['C2.1-nonzero']:.1e} of the term scale)")
    report_break("C2.1", least["C2.1-break"] > 1e-8,
                 f"for the non-admissible law (no T-correction) Kcal(nu, E) != 0: >= {least['C2.1-break']:.1e}")
    report("C2.2", worst["C2.2-exact"] < TOL and worst["C2.2-c01"] < TOL and worst["C2.2-c2"] < TOL and worst["C2.2-c3"] < TOL,
           f"E^(1) = [R19_1,R19_2]Y exactly ({worst['C2.2-exact']:.1e}); c0 = c1 = 0 ({worst['C2.2-c01']:.1e}); "
           f"c2 = (1/100)[A1,A2]Y ({worst['C2.2-c2']:.1e}); c3 - c3[E_3] = (4.7) ({worst['C2.2-c3']:.1e}); "
           f"c3[E_3] = (1/500)(...) ({worst['C2.2-c3E3']:.1e})")
    report_break("C2.2", least["C2.2-c3-break"] > 0.1, f"1/100 -> 1/50 in (4.7) fails: rel. error >= {least['C2.2-c3-break']:.2f}")
    report("C2.3", worst["C2.3-lowzero"] < TOL and worst["C2.3"] < TOL,
           f"quadratic sector zero through g^3 ({worst['C2.3-lowzero']:.1e}); exact g^4 coefficient vs (4.8): rel. error {worst['C2.3']:.2e}")
    report_break("C2.3", least["C2.3-break"] > 0.1, f"1/2000 -> 1/1000 in (4.8) fails: rel. error >= {least['C2.3-break']:.2f}")
    for key, target in (("E", 2), ("lin-c2", 3), ("lin-c3", 4)):
        sl = slopes_rich[key]
        report(f"C2-R-{key}", all(abs(x - target) < 0.35 for x in sl),
               f"last Richardson slopes {[f'{x:.2f}' for x in sl]} (expected {target})")
    # Quadratic sector: the claim is that the residual after removing g^4 x (4.8) is O(g^5),
    # i.e. slope >= 5 - 0.35.  One-sided (fix pass): at D = 6, seed 53, the g^6 term dominates
    # the g^5 one down to g ~ 0.002 (last slope 5.75 at 0.00625 -> 0.003125; extending the
    # sequence gives 5.31, 5.06, record 053 section 7), and the smaller configurations reach
    # the rounding floor if the sequence is extended.  A wrong (4.8) gives slope 4 (break).
    sl = slopes_rich["quad-c4"]
    report("C2-R-quad-c4", all(x > 5 - 0.35 for x in sl),
           f"last Richardson slopes {[f'{x:.2f}' for x in sl]} (expected >= 5: residual O(g^5))")
    report_break("C2-R-quad-c4", all(abs(x - 4) < 0.35 for x in slopes_rich["quad-c4-break"]),
                 f"with (4.8) as first written (-19/2000) the slopes stay at {[f'{x:.2f}' for x in slopes_rich['quad-c4-break']]} (4, not >= 5)")
    report_break("C2-R-lin-c3", all(abs(x - 4) > 0.35 for x in slopes_rich["lin-c3-break"]),
                 f"with 2x(4.7) the slopes stay at {[f'{x:.2f}' for x in slopes_rich['lin-c3-break']]} (not 4)")
    print(f"  C2-R quad-c4-fit (diagnostic, fitted coefficients): slopes {[f'{x:.2f}' for x in slopes_rich['quad-c4-fit']]}")
    # The residual of (5.5) is normalised by |Phi*| = O(g^2): the RELATIVE residual scales as
    # g^{2n}, i.e. the absolute residual as g^{2n+2} (record (5.4): q_{n+1} = O(g^{2n})).
    # Slopes from g = 0.1 -> 0.05 (at 0.025 the n = 4 residual reaches the rounding floor).
    def pair_slope(vals: dict[float, float]) -> tuple[float, float]:
        """Slope from the smallest-g halving pair whose smaller residual is above the
        rounding floor (1e-13 relative); falls back to the largest pair."""
        for hi, lo in ((0.05, 0.025), (0.1, 0.05), (0.2, 0.1)):
            if vals[lo] > 1e-13:
                return slope(vals[hi], vals[lo]), hi
        return slope(vals[0.2], vals[0.1]), 0.2

    ok31, det = True, []
    for key, vals in c31.items():
        n = int(key.split("-n")[-1])
        if n <= 4:
            sl, hi = pair_slope(vals)
            det.append(f"{key}: {sl:.2f} (exp {2*n}, pair {hi}->{hi/2})")
            ok31 &= abs(sl - 2 * n) < 0.5
    report("C3.1", ok31, "slopes of the relative (5.5) residual (absolute = +2): " + "; ".join(det))
    fin = {k: v for k, v in c31.items() if k.endswith("-n10") or (k.endswith("-n7") and "D6" in k)}
    print("  C3.1 residual of (5.5) at the largest truncation, per g: "
          + "; ".join(f"{k}: " + ", ".join(f"g={gv}: {r:.1e}" for gv, r in v.items()) for k, v in fin.items()))
    adm = {k: v for k, v in worst.items() if k.startswith("C3-adm-")}
    # Admissibility of F^flat: (i) wherever the Morse series has converged ((5.5) residual
    # < 1e-11 at n_max) the invariance residual is at rounding level (< TOL); (ii) elsewhere
    # (D = 6, seed 53, g >= 0.1: |(g^2/20) K^-1 T_Y| ~ 0.2-0.4, slow Y-series) it is at the
    # truncation level, <= 10x the (5.5) residual, and decreases with n at every g.  The
    # slopes in g of the truncated residual (asymptotically 2n) are printed, not asserted.
    conv = {k: trunc_level[k[7:]] < 1e-11 for k in adm}
    adm_ok = all((v < TOL) if conv[k] else (v <= 10 * trunc_level[k[7:]]) for k, v in adm.items())
    mono = all(all(vals[gv] <= 1.5 * c3adm[f"{key.rsplit('-n', 1)[0]}-n{n - 1}"][gv] or vals[gv] < 1e-13
                   for gv in vals)
               for key, vals in c3adm.items() for n in [int(key.split("-n")[-1])] if n >= 3)
    detadm = []
    for key, vals in c3adm.items():
        n = int(key.split("-n")[-1])
        if n <= 4:
            sl, hi = pair_slope(vals)
            detadm.append(f"{key}: {sl:.2f} ({hi}->{hi/2})")
    report("C3", worst["C3-flat"] < TOL and adm_ok and mono,
           f"E_4[F^flat]/scale <= {worst['C3-flat']:.1e}; invariance residual of F^flat at n_max: "
           + ", ".join(f"{k[7:]}: {v:.1e}" + ("" if conv[k] else f" [truncation level; (5.5) residual {trunc_level[k[7:]]:.1e}]") for k, v in adm.items())
           + f"; residual decreases with the truncation order at every g: {mono}")
    print("  C3 slopes in g of the truncated-F^flat residual, n<=4 (asymptotically 2n; recorded, not asserted): " + "; ".join(detadm))
    b1 = {k: v for k, v in worst.items() if k.startswith("C3-break1-adm-")}
    report_break("C3-1", worst["C3-break1-flat"] < TOL and all(v > 1e-7 for v in b1.values()),
                 f"G = M_K^1/2 alone: flat (E_4 <= {worst['C3-break1-flat']:.1e}) but NOT admissible: residual "
                 + ", ".join(f"{k[14:]}: {v:.1e}" for k, v in b1.items()))
    report_break("C3-2", least["C3-break2-flat"] > 1e-5 and worst["C3-break2-adm"] < TOL,
                 f"F^(19): admissible (residual {worst['C3-break2-adm']:.1e}) but NOT flat (E_4 >= {least['C3-break2-flat']:.1e})")
    report("C3.2-expansion", all(worst[k] < TOL for k in ("C3.2-exp-low", "C3.2-exp", "C3.2-exp-hand", "C3.2-exp-homog")),
           f"Y^2 part of F^flat: zero through g^2 ({worst['C3.2-exp-low']:.1e}); g^3 coefficient = corrected (5.6) "
           f"({worst['C3.2-exp']:.1e}), = hand form in A_u ({worst['C3.2-exp-hand']:.1e}); homogeneous of degree 2 ({worst['C3.2-exp-homog']:.1e})")
    report_break("C3.2-expansion", least["C3.2-exp-break"] > 0.1,
                 f"(5.6) as first written, (g^2/30) R19_u Kcal^-1 T(.,Y,Y), fails: rel. error >= {least['C3.2-exp-break']:.2f}")
    print(f"\nSUMMARY: {len(failures)} failure(s) {failures}; seeds {SEEDS}; {time.time()-t_start:.0f}s")
    return len(failures)


if __name__ == "__main__":
    sys.exit(main())
