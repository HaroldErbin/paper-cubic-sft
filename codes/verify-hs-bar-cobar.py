"""
Toy verification for derivation 024 (Route C vs the bar-cobar canonical equations), part 1 (5a).

VERIFIED (record 024 Sec. 2, claim (1)):
  C1  On the chain sigma_k = Psi^k/k! every split (i, n-i) of the factor-2 equation (1.5)
      holds, n <= 4, including the (2,2) split that Route C does not impose.
  C2  On the chain the rows L = 2, 3 of B Phi_1 = 0 (1.4) equal Sym(MC (x) Psi^{L-1}/(L-1)!),
      i.e. they are consequences of the row L = 1 -- for OFF-shell Psi (identity, not EOM).
  C3  Route C's Euler-Lagrange system: constraints solved, lambda tower solved top-down, and
      the Psi-gradient of S_C -- computed by FINITE DIFFERENCES of the action, the
      independent path -- equals the L = 1 row of B Phi_1 = 0 (the L_infty MC equation
      Q Psi + sum_n g^{n-2} ell_{n-1}(Psi^{n-1})/(n-1)!).  On-shell lambda_n != 0.
  C4  The dropped equations are NOT consequences of the single kept equation at their
      length: with sigma_2 off the chain and sigma_3, sigma_4 defined by Route C's
      projected constraints, the full (2,1) equation and the (2,2) equation FAIL, while
      the mu-projected (k-1,1) equations hold.  This exhibits the failing term of the
      literal identification (record 024 Sec. 2.4).
  C5  Break-on-purpose: C3 with the V_3 coefficient perturbed must FAIL.

NOT VERIFIED: Koszul signs on odd sectors (the toy is purely even, omega symmetric, no
ghost grading), the L_infty relations (irrelevant to the equation-level map tested here),
N_gh(lambda_k) = 3k (a grading statement, record 024 eq. (2.4), not machine-checked),
type-II sectors.  Part 2 (5b, record Sec. 3): T1a composite-multiplier identity (3.2) off-shell; T1b/T1c elimination of
sigma_2 returns S_eff^(4) (R8), completed square; T2 S_3(sigma_2^*) - S_eff^(5) = O(g^4) by exact Taylor
coefficients (Cauchy circle inside the nearest pole of sigma_2^*(g)); T3 break (coefficient 1/24).
Part 3 (5b, record Sec. 4): G1 L_infty gauge law from (B Lambda_1)_1; G2 delta sigma_2 = delta Psi ^ Psi
+ MC ^ lambda off-shell (4.3); G3 break; G4 an independent length-2 parameter changes S_HS (generic non-vanishing only:
the toy has no L_infty relations and no nilpotent Q, hence no gauge symmetry to serve as positive control -- G4 is
decorative; the "not a symmetry" claim rests on R18(1), record 024 Sec. 4.3).
Part 4 (5c, record Sec. 5): Q1 Route C's hand-written EL system is self-adjoint for the cotangent form (lowered
Jacobian symmetric; automatic for a correctly derived EL system, consistency check only), Q1b = finite-difference
gradient (the substantive check), Q1c break; Q2 Helmholtz test on the FULL tensor space H + H(x)H (not Sym^2; the
antisymmetric block decouples with unit Jacobian and admits the identity form, so the degeneracy conclusion transfers
to H + Sym^2 H): CMZ's undoubled canonical system admits no nondegenerate constant form (their obstruction 2 realised
on the toy); Q3 HS O(g^2) system self-adjoint for omega + omega^{(x)2} (consistency check only), Q3b gradient, Q3c
rank of V_4 on the full tensor space = dim Sym^2 (DECORATIVE: generic for a random symmetric V_4).
Part 5 (5c, record Sec. 6): the CMZ scalar phi^3 + phi^4 example on a 4-site lattice by Route C: P5a multiplier tower
solves the sigma/lambda equations, P5a' phi-gradient = collapsed EOM, P5b length-2 row EOM-proportional on the chain,
P5c break.  Parts 4-5 test structure (Helmholtz/cyclicity) on EVEN toys only: no Koszul signs, no ghost grading.

Usage: uv run python codes/verify-hs-bar-cobar.py [--seed S] [--dim d]
"""
from __future__ import annotations

import argparse
import itertools
import math
import sys

import numpy as np

FAILS: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))
    if not ok:
        FAILS.append(name)


def sym(T: np.ndarray) -> np.ndarray:
    """Full symmetrisation of a tensor (all slots even: plain average over permutations)."""
    n = T.ndim
    return sum(np.transpose(T, p) for p in itertools.permutations(range(n))) / math.factorial(n)


def tpow(v: np.ndarray, n: int) -> np.ndarray:
    out = np.array(1.0)
    for _ in range(n):
        out = np.multiply.outer(out, v)
    return out


def random_sym(d: int, n: int, rng: np.random.Generator) -> np.ndarray:
    return sym(rng.normal(size=(d,) * n))


class Toy:
    """Even toy: omega symmetric non-degenerate on R^d, Q with omega(.,Q.) symmetric,
    vertices V_n fully symmetric, ell_{n-1} defined by omega(x, ell_{n-1}(y..)) = V_n(x,y..)."""

    def __init__(self, d: int, nmax: int, rng: np.random.Generator):
        self.d, self.nmax = d, nmax
        A = rng.normal(size=(d, d))
        self.omega = A @ A.T + d * np.eye(d)
        self.omega_inv = np.linalg.inv(self.omega)
        self.M = random_sym(d, 2, rng)              # kinetic matrix, S_kin = Psi.M.Psi/2
        self.Q = self.omega_inv @ self.M            # Q Psi = omega^{-1} M Psi
        self.V = {n: random_sym(d, n, rng) for n in range(3, nmax + 1)}
        self.g = 0.7

    def ell(self, k: int, *args: np.ndarray) -> np.ndarray:
        """ell_k(x_1..x_k) = omega^{-1} V_{k+1}(., x_1..x_k); ell_1 = Q."""
        if k == 1:
            return self.Q @ args[0]
        T = self.V[k + 1]
        for x in args:
            T = np.tensordot(T, x, axes=([T.ndim - 1], [0]))
        return self.omega_inv @ T

    def mc(self, psi: np.ndarray) -> np.ndarray:
        """Row L=1 of B Phi_1 = 0 on the chain: Q Psi + sum_n g^{n-2} ell_{n-1}(Psi^{n-1})/(n-1)!"""
        out = self.Q @ psi
        for n in range(3, self.nmax + 1):
            out = out + self.g ** (n - 2) * self.ell(n - 1, *([psi] * (n - 1))) / math.factorial(n - 1)
        return out

    def barB_row(self, L: int, sig: dict[int, np.ndarray]) -> np.ndarray:
        """Length-L component of B Phi_1 (1.4): sum_k bar B_k sigma_{L+k-1}, with
        bar B_k T = C(n,k) Sym(ell_k ._k T) on a symmetric length-n tensor T; g^{k-1} weights."""
        out = np.zeros((self.d,) * L)
        for k in range(1, self.nmax):
            n = L + k - 1
            if n not in sig:
                continue
            T = sig[n]
            if k == 1:
                E = np.tensordot(self.Q, T, axes=([1], [0]))
            else:
                # contract V_{k+1} (indices 1..k) with the first k slots of T, raise the free index
                E = np.tensordot(self.V[k + 1], T, axes=(list(range(1, k + 1)), list(range(k))))
                E = np.tensordot(self.omega_inv, E, axes=([1], [0]))
            out = out + self.g ** (k - 1) * math.comb(n, k) * sym(E)
        return out


def pair(toy: Toy, lam: np.ndarray, X: np.ndarray) -> float:
    """<lambda, X> = lambda . (omega^{(x)k} X)."""
    Y = X
    for i in range(X.ndim):
        Y = np.moveaxis(np.tensordot(toy.omega, Y, axes=([1], [i])), 0, i)
    return float(np.sum(lam * Y))


def action_C(toy: Toy, psi: np.ndarray, sig: dict[int, np.ndarray], lam: dict[int, np.ndarray]) -> float:
    """S_C, record 024 eq. (2.2), group-like normalisation: constraint sigma_k - Sym(sigma_{k-1} (x) Psi)/k."""
    S = 0.5 * psi @ toy.M @ psi
    for n in range(3, toy.nmax + 1):
        S += toy.g ** (n - 2) * float(np.sum(toy.V[n] * sig[n]))
    full = dict(sig)
    full[1] = psi
    for k in range(2, toy.nmax + 1):
        S += pair(toy, lam[k], sig[k] - sym(np.multiply.outer(full[k - 1], psi)) / k)
    return S


def solve_lambda(toy: Toy, psi: np.ndarray) -> dict[int, np.ndarray]:
    """sigma_n-equations of (2.3), top down: omega^{(x)n} lambda_n = -g^{n-2} V_n + (omega^{(x)n+1} lambda_{n+1}) . Psi /(n+1)."""
    lam: dict[int, np.ndarray] = {}
    lowered_next = None
    for n in range(toy.nmax, 1, -1):
        rhs = -(toy.g ** (n - 2) * toy.V[n]) if n >= 3 else np.zeros((toy.d,) * n)
        if lowered_next is not None:
            rhs = rhs + np.tensordot(lowered_next, psi, axes=([n], [0])) / (n + 1)
        lowered_next = rhs                       # this is omega^{(x)n} lambda_n (all indices down)
        lam_n = rhs
        for i in range(n):
            lam_n = np.moveaxis(np.tensordot(toy.omega_inv, lam_n, axes=([1], [i])), 0, i)
        lam[n] = lam_n
    return lam


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=20260914)
    ap.add_argument("--dim", type=int, default=3)
    a = ap.parse_args()
    rng = np.random.default_rng(a.seed)
    print(f"seed={a.seed} dim={a.dim} nmax=4")
    toy = Toy(a.dim, 4, rng)
    psi = rng.normal(size=a.dim)
    chain = {k: tpow(psi, k) / math.factorial(k) for k in range(1, 6)}   # length 5 needed by row L=3, k=3
    tol = 1e-9

    # C1: all splits of (1.5) on the chain: C(n,i) phi_n = phi_i (x) phi_{n-i}
    for n in range(2, 6):
        for i in range(1, n // 2 + 1):
            res = math.comb(n, i) * chain[n] - np.multiply.outer(chain[i], chain[n - i])
            check(f"C1 split ({i},{n-i}) of (1.5) holds on chain", np.abs(res).max() < tol)

    # C2: rows L=2,3 of B Phi_1 on the chain equal Sym(MC (x) Psi^{L-1}/(L-1)!), off-shell Psi
    mc = toy.mc(psi)
    check("C2 row L=1 of B Phi_1 equals MC expression", np.abs(toy.barB_row(1, chain) - mc).max() < tol)
    for L in (2, 3):
        lhs = toy.barB_row(L, chain)
        rhs = sym(np.multiply.outer(mc, chain[L - 1]))
        check(f"C2 row L={L} of B Phi_1 = Sym(MC (x) Psi^{L-1}/{L-1}!) on chain",
              np.abs(lhs - rhs).max() < tol, f"|row|={np.abs(lhs).max():.3e}")

    # C3: Route C EL: constraints + lambda tower, then finite-difference Psi-gradient of S_C
    sig = {k: chain[k] for k in range(2, 5)}
    lam = solve_lambda(toy, psi)
    # sigma_n stationarity (finite differences), sanity
    for n in range(2, 5):
        E = rng.normal(size=(a.dim,) * n)
        h = 1e-6
        sp = {**sig, n: sig[n] + h * E}
        sm = {**sig, n: sig[n] - h * E}
        dS = (action_C(toy, psi, sp, lam) - action_C(toy, psi, sm, lam)) / (2 * h)
        check(f"C3 sigma_{n}-equation solved by lambda tower", abs(dS) < 1e-6, f"dS={dS:.2e}")
    check("C3 on-shell lambda_2 is nonzero (inhomogeneous tower)", np.abs(lam[2]).max() > 1e-3)

    def psi_grad(V3coef: float = 1.0) -> np.ndarray:
        gr = np.zeros(a.dim)
        h = 1e-5
        for i in range(a.dim):
            e = np.zeros(a.dim); e[i] = h
            gr[i] = (action_C(toy, psi + e, sig, lam) - action_C(toy, psi - e, sig, lam)) / (2 * h)
        return gr
    grad = psi_grad()
    # lowered MC: omega . MC = M Psi + sum g^{n-2} V_n(., Psi^{n-1})/(n-1)!
    target = toy.omega @ mc
    check("C3 Psi-gradient of S_C (finite differences) = omega.(row L=1 of B Phi_1)",
          np.abs(grad - target).max() < 1e-6, f"max diff={np.abs(grad - target).max():.2e}")

    # C4: dropped equations fail with sigma_2 off the chain, projected constraints hold
    sig2 = chain[2] + 0.3 * random_sym(a.dim, 2, rng)
    sig3 = sym(np.multiply.outer(sig2, psi)) / 3
    sig4 = sym(np.multiply.outer(sig3, psi)) / 4
    proj3 = 3 * sig3 - sym(np.multiply.outer(sig2, psi))
    check("C4 mu-projected (2,1) constraint holds off-chain by construction", np.abs(proj3).max() < tol)
    full21 = 3 * sig3 - np.multiply.outer(sig2, psi)
    check("C4 full (2,1) equation FAILS off-chain (ker mu part is a genuine extra condition)",
          np.abs(full21).max() > 1e-3, f"residual={np.abs(full21).max():.3e}")
    split22 = 6 * sig4 - np.multiply.outer(sig2, sig2)
    check("C4 (2,2) split at n=4 FAILS off-chain (the dropped term of Sec. 2.4)",
          np.abs(split22).max() > 1e-3, f"residual={np.abs(split22).max():.3e}")

    # C5: break on purpose
    bad = target + 0.1 * toy.g * np.tensordot(toy.V[3], np.multiply.outer(psi, psi), axes=([1, 2], [0, 1])) / 2
    check("C5 break-on-purpose: perturbed V_3 coefficient must FAIL",
          not (np.abs(grad - bad).max() < 1e-6), f"max diff={np.abs(grad - bad).max():.2e}")

    # ------------------------------------------------------------------ part 2 (5b, record Sec. 3)
    print("--- part 2: Sigma_2 truncation (record 024 Sec. 3.1) ---")
    toy5 = Toy(a.dim, 5, rng)          # fresh toy with V_5 (part 1 untouched)
    g = toy5.g
    psi5 = rng.normal(size=a.dim)
    sig_rand = random_sym(a.dim, 2, rng)

    def V4_form(A: np.ndarray, B: np.ndarray) -> float:
        return np.tensordot(np.tensordot(toy5.V[4], A, axes=([2, 3], [0, 1])), B, axes=([0, 1], [0, 1]))

    def V4_lin(A: np.ndarray) -> np.ndarray:                # V_4(A, . ) as a lowered 2-tensor
        return np.tensordot(toy5.V[4], A, axes=([2, 3], [0, 1]))

    def V5_form(A: np.ndarray, B: np.ndarray, v: np.ndarray) -> float:
        T = np.tensordot(toy5.V[5], v, axes=([4], [0]))
        return np.tensordot(np.tensordot(T, A, axes=([2, 3], [0, 1])), B, axes=([0, 1], [0, 1]))

    def S_eff(v: np.ndarray, nmax: int) -> float:
        S = 0.5 * v @ toy5.M @ v
        for n in range(3, nmax + 1):
            S += toy5.g ** (n - 2) * np.sum(toy5.V[n] * tpow(v, n)) / math.factorial(n)
        return S

    def S_HS(v: np.ndarray, sg: np.ndarray) -> float:       # record (3.2), sigma_2 normalisation
        return S_eff(v, 3) - toy5.g ** 2 / 6 * V4_form(sg, sg) + toy5.g ** 2 / 6 * V4_form(sg, np.multiply.outer(v, v))

    def S_3(v: np.ndarray, sg: np.ndarray, c5: float = 1 / 30) -> float:   # record (3.3)
        return S_HS(v, sg) + toy5.g ** 3 * c5 * V5_form(sg, sg, v)

    def raise2(L: np.ndarray) -> np.ndarray:                  # omega^{-1 (x) 2} L
        return toy5.omega_inv @ L @ toy5.omega_inv.T

    # T1a: composite multiplier identity (3.2): S_C^{(<=2)} with lambda_2 = -(g^2/3) omega^{-2} V_4(sigma_2,.)
    #      equals S_HS for OFF-shell random sigma_2 (uses `pair`, i.e. the multiplier pairing of part 1)
    X = sig_rand - np.multiply.outer(psi5, psi5) / 2
    lam2 = raise2(-(g ** 2 / 3) * V4_lin(sig_rand))
    S_C2 = S_eff(psi5, 3) + g ** 2 / 6 * V4_form(sig_rand, sig_rand) + pair(toy5, lam2, X)
    check("T1a (3.2): multiplier form with composite lambda_2 = -(g^2/3) V_4(sigma_2,.) equals S_HS off-shell",
          abs(S_C2 - S_HS(psi5, sig_rand)) < tol, f"diff={abs(S_C2 - S_HS(psi5, sig_rand)):.2e}")
    # T1b: eliminating sigma_2 from S_HS returns S_eff through V_4 (R8); sigma_2^* = Psi^2/2
    d2 = a.dim ** 2
    K = toy5.V[4].reshape(d2, d2)
    rhs = (V4_lin(np.multiply.outer(psi5, psi5)) / 2).reshape(d2)
    sig_star = np.linalg.lstsq(K, rhs, rcond=None)[0].reshape(a.dim, a.dim)
    check("T1b sigma_2^* = Psi^2/2 from the S_HS stationarity (V_4 invertible on Sym^2)",
          np.abs(sig_star - np.multiply.outer(psi5, psi5) / 2).max() < 1e-8)
    check("T1b S_HS(sigma_2^*) = S_eff^{(4)} incl. g^2 V_4(Psi^4)/4! (R8)",
          abs(S_HS(psi5, sig_star) - S_eff(psi5, 4)) < tol, f"diff={abs(S_HS(psi5, sig_star) - S_eff(psi5, 4)):.2e}")
    check("T1c completed square: S_HS - S_eff^{(4)} = -(g^2/6) V_4(X,X) off-shell",
          abs(S_HS(psi5, sig_rand) - S_eff(psi5, 4) + g ** 2 / 6 * V4_form(X, X)) < tol)

    # T2: O(g^3) with sigma_2 only: S_3(sigma_2^*) - S_eff^{(5)} = O(g^4) (R17), log-slope 4 under g -> g/2
    def residual(gval: float, c5: float) -> float:
        toy5.g = gval
        A = (gval ** 2 / 3) * toy5.V[4].reshape(d2, d2) \
            - (gval ** 3 / 15) * np.tensordot(toy5.V[5], psi5, axes=([2], [0])).reshape(d2, d2)  # V5(.,Psi,.) on slots (01)(34)
        b = ((gval ** 2 / 6) * V4_lin(np.multiply.outer(psi5, psi5))).reshape(d2)
        sg = sym(np.linalg.lstsq(A, b, rcond=None)[0].reshape(a.dim, a.dim))
        # stationarity check by finite differences (independent of the hand-derived linear system)
        eps, fd = 1e-6, 0.0
        for i in range(a.dim):
            for j in range(i, a.dim):
                E = np.zeros((a.dim, a.dim)); E[i, j] += eps / 2; E[j, i] += eps / 2
                fd = max(fd, abs(S_3(psi5, sg + E, c5) - S_3(psi5, sg - E, c5)) / (2 * eps))
        r = S_3(psi5, sg, c5) - S_eff(psi5, 5)
        toy5.g = g
        return r, fd

    # Exact Taylor coefficients of r(g) = S_3(sigma_2^*(g)) - S_eff^{(5)}(g) by Cauchy's formula on a
    # circle |g| = 0.05 (r is analytic there: sigma_2^* is rational in g with poles at |g| ~ O(1));
    # a two-point log-slope is polluted by g^5 since sigma_2^* - Psi^2/2 = O(g) with an O(1) coefficient.
    # radius: sigma_2^*(g) has poles where (1/3)V_4 - (g/15)V_5(.,Psi,.) is singular on Sym^2; stay well inside.
    Bsym = [np.array([[(1.0 if {r, c} == {i, j} else 0.0) for c in range(a.dim)] for r in range(a.dim)])
            for i in range(a.dim) for j in range(i, a.dim)]
    P = np.stack([b.reshape(d2) for b in Bsym], axis=1)            # d^2 x dim(Sym^2)
    A0 = P.T @ toy5.V[4].reshape(d2, d2) @ P / 3
    A1 = P.T @ np.tensordot(toy5.V[5], psi5, axes=([2], [0])).reshape(d2, d2) @ P / 15
    poles = np.abs(np.linalg.eigvals(np.linalg.solve(A1, A0)))      # g_pole = eig(A1^{-1} A0)
    Ncirc, rho = 32, 0.2 * poles.min()
    print(f"      nearest pole of sigma_2^*(g): |g|={poles.min():.3f}; Cauchy circle rho={rho:.4f}")
    def taylor(c5: float) -> tuple[complex, complex]:
        gk = rho * np.exp(2j * np.pi * np.arange(Ncirc) / Ncirc)
        rk = np.array([residual(gv, c5)[0] for gv in gk])
        coef = lambda n: np.sum(rk * gk ** (-n)) / Ncirc
        return coef(3), coef(4)
    _, fd1 = residual(0.01, 1 / 30)
    c3, c4 = taylor(1 / 30)
    check("T2 sigma_2^* is stationary for S_3 (finite-difference gradient ~ 0)", fd1 < 1e-6, f"|dS|={fd1:.1e}")
    check("T2 S_3(sigma_2^*) - S_eff^{(5)} = O(g^4): Taylor g^3 coefficient vanishes, g^4 one does not",
          abs(c3) < 1e-6 * max(1.0, abs(c4)) and abs(c4) > 1e-8, f"c3={abs(c3):.2e} c4={c4.real:.4e}")
    # T3: break on purpose: coefficient 1/24 instead of 1/30 leaves the O(g^3) mismatch (1/24-1/30) V_5(Psi^5)/4
    c3b, _ = taylor(1 / 24)
    expect = (1 / 24 - 1 / 30) * float(np.sum(toy5.V[5] * tpow(psi5, 5))) / 4
    check("T3 break-on-purpose: coefficient 1/24 gives c3 = (1/24-1/30) V_5(Psi^5)/4 != 0",
          abs(c3b - expect) < 1e-6 * abs(expect) and abs(expect) > 1e-10, f"c3={c3b.real:.4e} expected={expect:.4e}")

    # ------------------------------------------------------------------ part 3 (5b, record Sec. 4)
    print("--- part 3: CMZ gauge transformation on the canonical sector (record 024 Sec. 4.2) ---")
    # Even toy: lambda treated as an even vector (no Koszul signs); off-shell Psi.  Lambda_{1,l} = lambda ^ Psi^{l-1}/(l-1)!
    lamg = rng.normal(size=a.dim)
    Lchain = {l: sym(np.multiply.outer(lamg, tpow(psi, l - 1))) / math.factorial(l - 1) for l in range(1, 6)}
    # G1: length-1 component of B Lambda_1 = L_infty gauge law sum_k g^{k-1} ell_k(lambda, Psi^{k-1})/(k-1)!
    dpsi = toy.barB_row(1, Lchain)
    target_g = toy.Q @ lamg + sum(toy.g ** (k - 1) * toy.ell(k, lamg, *([psi] * (k - 1))) / math.factorial(k - 1)
                                  for k in range(2, toy.nmax))
    check("G1 (B Lambda_1)_{length 1} = L_infty gauge law on Psi (R11's delta Psi)", np.abs(dpsi - target_g).max() < tol)
    # G2: length-2 component = delta Psi ^ Psi + MC(Psi) ^ lambda, off-shell (4.3)
    dsig2 = toy.barB_row(2, Lchain)
    comp = sym(np.multiply.outer(target_g, psi))
    eom = sym(np.multiply.outer(toy.mc(psi), lamg))
    check("G2 (4.3): delta sigma_2 = delta Psi ^ Psi + MC(Psi) ^ lambda, off-shell", np.abs(dsig2 - comp - eom).max() < tol,
          f"|MC^lambda|={np.abs(eom).max():.2e} (nonzero off-shell)")
    # G3: break: the composite law alone fails off-shell by exactly the EOM term
    check("G3 break-on-purpose: composite law alone (no MC term) FAILS off-shell", np.abs(dsig2 - comp).max() > 1e-3,
          f"residual={np.abs(dsig2 - comp).max():.2e}")
    # G4: an independent length-2 parameter (delta sigma_2 = Q^ Lambda_2, delta Psi = g ell_2(Lambda_2)) is NOT a
    #     symmetry of S_HS on the type-I fields (record 4.3 (ii)).  Generic non-vanishing only: the toy has no ghost
    #     grading, no L_infty relations and no nilpotent Q, so S_HS_toy has no gauge symmetry at any order and no
    #     positive control (delta S_HS under the composite lambda-law = O(g^3)) exists on this toy.  Decorative.
    Lam2 = random_sym(a.dim, 2, rng)
    dS2 = sym(np.tensordot(toy.Q, Lam2, axes=([1], [0])))               # Q^ Lambda_2 = Sym(Q (x) 1) Lambda_2
    dP = toy.g * (toy.omega_inv @ np.tensordot(toy.V[3], Lam2, axes=([1, 2], [0, 1])))   # g ell_2(Lambda_2)
    def S_HS_toy(v, sg):
        V4 = lambda A, B: float(np.tensordot(np.tensordot(toy.V[4], A, axes=([2, 3], [0, 1])), B, axes=([0, 1], [0, 1])))
        return 0.5 * v @ toy.M @ v + toy.g / 6 * float(np.sum(toy.V[3] * tpow(v, 3))) \
            - toy.g ** 2 / 6 * V4(sg, sg) + toy.g ** 2 / 6 * V4(sg, np.multiply.outer(v, v))
    eps = 1e-6
    sg0 = tpow(psi, 2) / 2
    dSHS = (S_HS_toy(psi + eps * dP, sg0 + eps * dS2) - S_HS_toy(psi - eps * dP, sg0 - eps * dS2)) / (2 * eps)
    check("G4 [decorative, no positive control on this toy] independent Lambda_{1,2} changes S_HS (generic non-vanishing)",
          abs(dSHS) > 1e-3, f"delta S_HS={dSHS:.3e}")

    # ------------------------------------------------------------------ part 4 (5c, record Sec. 5)
    # Helmholtz test: a system E(x) = 0 derives from an action through a CONSTANT nondegenerate form
    # Omega iff Omega.J(x) is symmetric, J = dE/dx.  We compute the nullspace of Omega -> {Omega J(x_i) -
    # (Omega J(x_i))^T} over random points and test whether it contains a nondegenerate form.
    d = a.dim
    toy3 = Toy(d, 3, rng)                      # V_3 only: enough for the structure; g = 0.7

    def jac(E, x0, h=1e-6):
        n = x0.size
        J = np.zeros((E(x0).size, n))
        for i in range(n):
            e = np.zeros(n); e[i] = h
            J[:, i] = (E(x0 + e) - E(x0 - e)) / (2 * h)
        return J

    def helmholtz_nullspace(E, N, pts):
        rows = []
        for x0 in pts:
            J = jac(E, x0)
            # map Omega (N x N, flattened) -> Omega J - (Omega J)^T, flattened
            Mrow = np.zeros((N * N, N * N))
            for k in range(N * N):
                Om = np.zeros(N * N); Om[k] = 1.0
                A = Om.reshape(N, N) @ J
                Mrow[:, k] = (A - A.T).ravel()
            rows.append(Mrow)
        Mbig = np.vstack(rows)
        u, sv, vt = np.linalg.svd(Mbig)
        null = vt[sv.size - np.sum(sv < 1e-7 * sv[0]):] if np.any(sv < 1e-7 * sv[0]) else np.zeros((0, N * N))
        # include the exactly-null directions beyond the rank
        null = vt[np.sum(sv > 1e-7 * sv[0]):]
        return null

    def max_rank_in(null, N, rng, trials=5):
        best = 0
        for _ in range(trials):
            c = rng.normal(size=null.shape[0])
            Om = (c @ null).reshape(N, N)
            best = max(best, np.linalg.matrix_rank(Om, tol=1e-8))
        return best

    n1, n2 = d, d * d
    # Q2 / break leg: CMZ's UNDOUBLED canonical system at k <= 2 with V_3: E_Psi = Q Psi + g ell_2(sigma_2)
    # (linear, their row L = 1), E_sigma = sigma_2 - Psi (x) Psi / 2 (their factor-2 equation).  No constant form.
    def E_cmz(x):
        psi, sg = x[:n1], x[n1:].reshape(d, d)
        e1 = toy3.Q @ psi + toy3.g * toy3.omega_inv @ np.tensordot(toy3.V[3], sg, axes=([1, 2], [0, 1]))
        e2 = sg - np.multiply.outer(psi, psi) / 2
        return np.concatenate([e1, e2.ravel()])
    pts = [rng.normal(size=n1 + n2) for _ in range(3)]
    null = helmholtz_nullspace(E_cmz, n1 + n2, pts)
    r = max_rank_in(null, n1 + n2, rng) if null.shape[0] else 0
    check("Q2 obstruction 2 realised (full tensor space H+H(x)H): CMZ canonical (undoubled) system admits NO nondegenerate constant form",
          r < n1 + n2, f"nullspace dim={null.shape[0]}, max rank={r} < {n1 + n2}")

    # Q1: Route C's hand-written EL system (record (2.3)/(3.1) with V_3, k <= 2, sigma_3 = sigma_2 ^ Psi / 3):
    # lowered gradients E_Psi = M Psi + g V_3(sigma_2, .)/3 - Lambda.Psi,  E_sigma = g V_3(., ., Psi)/3 + Lambda,
    # E_lambda = omega^{(x)2}(sigma_2 - Psi Psi/2),  Lambda := omega^{(x)2} lambda_2.  Raised with Omega_cot^{-1}
    # they must be Omega_cot-self-adjoint  <=>  the lowered Jacobian is symmetric.
    W = toy3.omega
    def lower2(T):
        return W @ T @ W.T
    def E_routeC(x):
        psi, sg, lam = x[:n1], x[n1:n1 + n2].reshape(d, d), x[n1 + n2:].reshape(d, d)
        Lam = lower2(lam)
        e_psi = toy3.M @ psi + toy3.g / 3 * np.tensordot(toy3.V[3], sg, axes=([1, 2], [0, 1])) - (Lam + Lam.T) @ psi / 2
        e_sg = toy3.g / 3 * np.tensordot(toy3.V[3], psi, axes=([2], [0])) + Lam
        e_lam = lower2(sg - np.multiply.outer(psi, psi) / 2)
        return np.concatenate([e_psi, e_sg.ravel(), e_lam.ravel()])
    N3 = n1 + 2 * n2
    x0 = rng.normal(size=N3)
    J = jac(E_routeC, x0)
    check("Q1 Route C (multipliers) is cyclic for the cotangent form: lowered EL Jacobian symmetric",
          np.abs(J - J.T).max() < 1e-6, f"asym={np.abs(J - J.T).max():.1e}")
    # independent path: E_routeC equals the finite-difference gradient of the truncated action (3.1) with V_3
    def S31(x):
        psi, sg, lam = x[:n1], x[n1:n1 + n2].reshape(d, d), x[n1 + n2:].reshape(d, d)
        return 0.5 * psi @ toy3.M @ psi + toy3.g / 3 * float(np.einsum('abc,ab,c', toy3.V[3], sg, psi)) \
            + float(np.sum(lower2(lam) * (sg - np.multiply.outer(psi, psi) / 2)))
    grad = np.array([(S31(x0 + h) - S31(x0 - h)) / 2e-6 for h in np.eye(N3) * 1e-6])
    check("Q1b hand-written Route C EL system = finite-difference gradient of (3.1)", np.abs(grad - E_routeC(x0)).max() < 1e-6,
          f"maxdiff={np.abs(grad - E_routeC(x0)).max():.1e}")
    # Q1c break: drop the lambda-dependence of the Psi-equation (CMZ's undoubled Psi row) -> not symmetric
    def E_break(x):
        e = E_routeC(x).copy()
        psi, lam = x[:n1], x[n1 + n2:].reshape(d, d)
        Lam = lower2(lam)
        e[:n1] += (Lam + Lam.T) @ psi / 2
        return e
    Jb = jac(E_break, x0)
    check("Q1c break-on-purpose: Psi-row without the multiplier back-reaction is NOT symmetric", np.abs(Jb - Jb.T).max() > 1e-3,
          f"asym={np.abs(Jb - Jb.T).max():.2e}")
    # Q3: HS action at O(g^2) (toy with V_4): fields (Psi, sigma_2), form omega + omega^{(x)2}; the hand-written lowered
    # gradients E_Psi = M Psi + g V_3(Psi,Psi,.)/2 + g^2 V_4(sigma,Psi,.)/3,  E_sigma = -g^2 V_4(sigma,.)/3 + g^2 V_4(Psi Psi,.)/6
    def E_hs(x):
        psi, sg = x[:n1], x[n1:].reshape(d, d)
        V4 = toy.V[4]
        e1 = toy.M @ psi + toy.g / 2 * np.einsum('abcd,b,c->d', toy.V[3][..., None] * 0 + np.einsum('abc->abc', toy.V[3])[..., None], psi, psi)[0] if False else \
             toy.M @ psi + toy.g / 2 * np.einsum('abc,a,b->c', toy.V[3], psi, psi) + toy.g ** 2 / 3 * np.einsum('abcd,ab,c->d', V4, sg, psi)
        e2 = -toy.g ** 2 / 3 * np.einsum('abcd,ab->cd', V4, sg) + toy.g ** 2 / 6 * np.einsum('abcd,a,b->cd', V4, psi, psi)
        return np.concatenate([e1, e2.ravel()])
    x1 = rng.normal(size=n1 + n2)
    Jh = jac(E_hs, x1)
    check("Q3 HS action O(g^2): lowered EL Jacobian symmetric (cyclic for omega + omega^{(x)2})", np.abs(Jh - Jh.T).max() < 1e-6,
          f"asym={np.abs(Jh - Jh.T).max():.1e}")
    def S_hs(x):
        psi, sg = x[:n1], x[n1:].reshape(d, d)
        return S_HS_toy(psi, sg)
    gradh = np.array([(S_hs(x1 + h) - S_hs(x1 - h)) / 2e-6 for h in np.eye(n1 + n2) * 1e-6])
    check("Q3b hand-written HS EL system = finite-difference gradient of S_HS", np.abs(gradh - E_hs(x1)).max() < 1e-6,
          f"maxdiff={np.abs(gradh - E_hs(x1)).max():.1e}")
    # Q3c: the sigma_2 block of the HS form is DEGENERATE on ker V_4 when d is such that Sym^2 has a kernel: report rank
    K = np.einsum('abcd->abcd', toy.V[4]).reshape(d * d, d * d)
    rk = np.linalg.matrix_rank(K, tol=1e-10)
    check("Q3c [decorative: generic for random symmetric V_4] V_4 on the full tensor space: rank = dim Sym^2 (kernel = antisym. part)",
          rk == d * (d + 1) // 2, f"rank={rk}, dim Sym^2={d * (d + 1) // 2}, dim full={d * d}")

    # ------------------------------------------------------------------ part 5 (5c, record Sec. 6): scalar example
    # CMZ Sec. 7: S = sum_x [ phi K phi/2 + g phi^3/3 + lam phi^4/4 ], K = lattice Laplacian - m^2 (D = 1, periodic).
    # Route C (R13 normalisation sigma_k = phi^{(x)k}): S_C = phi K phi/2 + g/3 sum_x sigma_3(x,x,x) + lam/4 sum_x sigma_4(x,x,x,x)
    #   + sum_{k=2..4} lambda_k.(sigma_k - sigma_{k-1} (x) phi), Euclidean pairing (V has one component per site).
    L = 4
    m2, gs, lm = 0.9, 0.6, 0.35
    Kop = -2 * np.eye(L) + np.roll(np.eye(L), 1, 0) + np.roll(np.eye(L), -1, 0) - m2 * np.eye(L)
    sizes = [L, L ** 2, L ** 3, L ** 4, L ** 2, L ** 3, L ** 4]
    offs = np.cumsum([0] + sizes)
    def unpack(z):
        parts = [z[offs[i]:offs[i + 1]].reshape((L,) * k) for i, k in enumerate([1, 2, 3, 4, 2, 3, 4])]
        return parts
    def S_scalar_C(z):
        phi, s2, s3, s4, l2, l3, l4 = unpack(z)
        return 0.5 * phi @ Kop @ phi + gs / 3 * np.einsum('xxx', s3) + lm / 4 * np.einsum('xxxx', s4) \
            + np.sum(l2 * (s2 - np.multiply.outer(phi, phi))) + np.sum(l3 * (s3 - np.multiply.outer(s2, phi))) \
            + np.sum(l4 * (s4 - np.multiply.outer(s3, phi)))
    phi0 = rng.normal(size=L)
    s2c, s3c, s4c = tpow(phi0, 2), tpow(phi0, 3), tpow(phi0, 4)
    # multiplier tower from the sigma-equations, top down: l4 = -lam/4 delta_xxxx; l3 = -g/3 delta_xxx + l4.phi; l2 = l3.phi
    l4 = np.zeros((L,) * 4); l4[np.arange(L), np.arange(L), np.arange(L), np.arange(L)] = -lm / 4
    l3 = np.tensordot(l4, phi0, axes=([3], [0])); l3[np.arange(L), np.arange(L), np.arange(L)] += -gs / 3
    l2 = np.tensordot(l3, phi0, axes=([2], [0]))
    z0 = np.concatenate([phi0, s2c.ravel(), s3c.ravel(), s4c.ravel(), l2.ravel(), l3.ravel(), l4.ravel()])
    gz = np.array([(S_scalar_C(z0 + h) - S_scalar_C(z0 - h)) / 2e-6 for h in np.eye(z0.size) * 1e-6])
    check("P5a scalar Route C: sigma- and lambda-equations hold on the chain with the multiplier tower",
          np.abs(gz[L:]).max() < 1e-6, f"max residual={np.abs(gz[L:]).max():.1e}")
    collapsed = Kop @ phi0 + gs * phi0 ** 2 + lm * phi0 ** 3            # CMZ's collapsed EOM (d^2 - m^2) phi + g phi^2 + lam phi^3
    check("P5a' scalar Route C: phi-gradient of S_C (finite differences) = CMZ collapsed EOM K phi + g phi^2 + lam phi^3",
          np.abs(gz[:L] - collapsed).max() < 1e-6, f"maxdiff={np.abs(gz[:L] - collapsed).max():.1e}")
    # P5b (W4 redirect: no gauge parameter exists in the scalar theory, so (4.3) has no scalar analogue; the off-shell
    #      structure that survives is the L = 2 row of B Phi = 0 being EOM-proportional on the chain):
    #      row (i=2, k=1): K_1 phi_2(x1,x2) + g phi_3(x1,x1,x2) + lam phi_4(x1,x1,x1,x2) = E_1(x1) phi_1(x2) on the chain.
    phi4 = tpow(phi0, 4)
    row2 = np.einsum('xy,yz->xz', Kop, s2c) + gs * np.einsum('xxz->xz', s3c) + lm * np.einsum('xxxz->xz', phi4)
    check("P5b scalar: length-2 row of B Phi = 0 on the chain = collapsed EOM (x) phi (EOM-proportional, off-shell phi)",
          np.abs(row2 - np.multiply.outer(collapsed, phi0)).max() < 1e-12, f"maxdiff={np.abs(row2 - np.multiply.outer(collapsed, phi0)).max():.1e}")
    # P5c break: wrong multiplier coefficient (g/3 -> g/4 in lambda_3) leaves the sigma_3-equation unsatisfied
    l3b = l3.copy(); l3b[np.arange(L), np.arange(L), np.arange(L)] += gs / 3 - gs / 4
    zb = z0.copy(); zb[offs[5]:offs[6]] = l3b.ravel()
    gzb = np.array([(S_scalar_C(zb + h) - S_scalar_C(zb - h)) / 2e-6 for h in np.eye(zb.size) * 1e-6])
    check("P5c break-on-purpose: multiplier coefficient g/4 instead of g/3 FAILS the sigma_3-equation", np.abs(gzb[offs[2]:offs[3]]).max() > 1e-3,
          f"residual={np.abs(gzb[offs[2]:offs[3]]).max():.2e}")

    total = len(FAILS)
    print(f"SUMMARY: {'ALL PASS' if not FAILS else str(total) + ' FAIL'}: {FAILS}")
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
