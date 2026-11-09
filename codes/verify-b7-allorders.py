#!/usr/bin/env python3
"""
verify-b7-allorders.py — machine checks for derivation 019 (B7): the ALL-ORDERS
closure of the dressed (scheme-B) cubic tower — the fixed-point theorem.

Setting (finite-dimensional binding, physical grading, all fields even, e^S
weight, generic V4..V9 — same conventions as verify-b6-ogs5-septic.py; CFT
analytics of the inverses = A2(iii)/T4 carve-out).  Fields: Psi in H (dim N),
Sigma_k in Sym^k, k = 2..K (K = 4 here).  The scheme-B action

  S = 1/2 V2 + (g/3!) V3
      + sum_k [ g^{2k-2}/(2k)! ( -Mt_k(S_k,S_k) + 2 <u_k(S_{k-1}), S_k> )
                + g^{2k-1}/(2k+1)! T_{2k+1}(S_k,S_k,Psi) ]

is JOINTLY QUADRATIC in the auxiliary tower (S_2,...,S_K) with a
block-TRIDIAGONAL (Jacobi) Hessian: diagonal blocks -a_k Mhat_k(Psi,g)
(Mhat_k = Mt_k - g/(2k+1) O_k(Psi)), off-diagonal blocks the source maps
L_k(Psi), and the only inhomogeneity u_2 = V4(., Psi^2) in the k=2 block.
Hence the on-shell value is ONE exact Gaussian,

  S(saddles) = shared + (g^2/4!) u_2^T Hhat_2(g,Psi)^{-1} u_2 ,
  Hhat_k = Mhat_k - g^2 (2k)!/(2k+2)! L_{k+1}^T Hhat_{k+1}^{-1} L_{k+1}
  (operator continued fraction / nested Schur complements),

and closure against S_eff = sum_n g^{n-2}/n! V_n(Psi^n) is ONE Veronese-
diagonal condition per order:  d_n := T_n(Psi^n) = V_n(Psi^n) - n! A_{n-2},
with A_{n-2} = [g^{n-2}] of the previous tower's feedback (a homogeneous
degree-n polynomial in Psi, so a symmetric solution T_n always exists by
polarization; the diagonal is FORCED, coefficient 1/n! from the telescoping
(1/4!)*(4!/6!)*(6!/8!)*...*((2k-2)!/(2k)!) = 1/(2k)!).

Checks:
 (0) machinery: g-power-series evaluator == contour-FFT of the closed form ==
     block-tridiagonal joint solve == direct action evaluation; K=2 analytic
     coefficients (c2 = V4d/4!, c3 = V5d/5!, c4 = v V4inv v / 600); collapse
     identity u_3(P_2) = Mt_3 P_3 for the canonical (R21) level-3 kernels.
 (1) tower A (canonical R21/R25 levels 2,3) reproduces R21 + R25 in the new
     machinery: c4 = t4, c5 = t5 (closure through O(g^5)); with O_3 removed the
     deficit is exactly A5_dr - V7(Psi^7)/7!, A5_dr = (1/600)[S2c/3 - S1/5].
 (2) the diagonal RECURSION executes one more rung: fit A6, A7 (exact series
     coefficients + homogeneous-polynomial fit + polarization) -> T8, T9 ->
     level-4 pair (Mt_4, u_4(Sigma_3)) + odd (4,4,1) coupling; closure through
     O(g^7): c[2..7] == targets, finite-g mismatch log-slope ~ 8; collapse
     u_4(P_3) = Mt_4 P_4; Sigma_4* -> P_4.  ** = the O(g^6)+O(g^7) closure,
     the k=4 tower instance of 018 §6 — CONFIRMED. **
 (3) exactness + triangularity at K=4: closed form == block solve == action at
     finite (also complex) g; adding level 4 leaves c[2..5] unchanged to
     machine precision (no contamination of lower orders).
 (4) forcing: perturbing T8 by eps*a^{x8} shifts c6 by exactly
     eps (a.Psi)^8/8! and leaves c[2..5] untouched; same for T9 at c7.
 (5) presentation freedom: tower B (uniform fully-polarized kernels at ALL
     levels) closes too; its T6 has the same Veronese diagonal as the R21
     block kernel but differs as a tensor; the freedom feeds forward
     (d7^B != d7^A) and the recursion re-absorbs it.
 (6) gauge law at K=4: exact completed-square decomposition
     S = S_onshell + sum_k (-a_k) Hhat_k(Y_k,Y_k); kernel-rotation laws
     delta Y_k = -(1/2) Hhat_k^{-1} (delta Hhat_k) Y_k give the exact
     off-shell equality delta S = delta S_onshell; falsification legs
     (drop delta Y_4 / delta Y_2) leave the predicted residuals.
 (7) the level-4 source is FORCED and USES Sigma_3: zeroing u_4 removes the
     V8 contact (c6 deficit = A6 exactly); dSigma_4*/dSigma_3 =
     Hhat_4^{-1} L_4 != 0.

All checks PASS/FAIL; exit code = number of failures.
"""

import itertools
import math
import sys

import numpy as np

SEED = int(sys.argv[1]) if len(sys.argv) > 1 else 20260708
rng = np.random.default_rng(SEED)
np.set_printoptions(precision=6, suppress=True)

N = 3
ORD = 8  # keep g^0..g^ORD in the series evaluator
TOL = 1e-8

failures = []


def report(num, name, ok, detail=""):
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] check ({num}) {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        failures.append(num)


# ---------------------------------------------------------------- bases
def sym_basis(k):
    elems = []
    for combo in itertools.combinations_with_replacement(range(N), k):
        M = np.zeros((N,) * k)
        for perm in set(itertools.permutations(combo)):
            M[perm] += 1.0
        M /= np.linalg.norm(M)
        elems.append(M)
    return np.array(elems)


Lam2, Lam3, Lam4 = sym_basis(2), sym_basis(3), sym_basis(4)
D2, D3, D4 = len(Lam2), len(Lam3), len(Lam4)
L2f, L3f, L4f = Lam2.reshape(D2, -1), Lam3.reshape(D3, -1), Lam4.reshape(D4, -1)
LF = {2: L2f, 3: L3f, 4: L4f}
DIM = {2: D2, 3: D3, 4: D4}


def sym_tensor_perm(n):
    T = rng.standard_normal((N,) * n)
    S = np.zeros_like(T)
    for perm in itertools.permutations(range(n)):
        S += np.transpose(T, perm)
    return S / math.factorial(n)


def sym_tensor_rank1(n, terms):
    S = np.zeros((N,) * n)
    for _ in range(terms):
        a = rng.standard_normal(N)
        a /= np.linalg.norm(a)
        c = rng.standard_normal()
        out = np.array(c)
        for _ in range(n):
            out = np.multiply.outer(out, a)
        S += out
    return S


V4 = sym_tensor_perm(4)
V5 = sym_tensor_perm(5)
V6 = sym_tensor_perm(6)
V7 = sym_tensor_perm(7)
V8 = sym_tensor_rank1(8, 90)
V9 = sym_tensor_rank1(9, 120)
VN = {4: V4, 5: V5, 6: V6, 7: V7, 8: V8, 9: V9}


def vdiag(T, psi):
    out = T
    for _ in range(T.ndim):
        out = np.tensordot(out, psi, axes=([0], [0]))
    return float(out)


def pveck(k, psi):
    v = psi
    out = np.array(1.0)
    for _ in range(k):
        out = np.multiply.outer(out, psi)
    return LF[k] @ out.ravel()


V4S = L2f @ V4.reshape(N**2, N**2) @ L2f.T
V4inv = np.linalg.inv(V4S)
V5S = np.einsum("abcde,Iab,Jcd->IJe", V5, Lam2, Lam2)


def u2vec(psi):
    return V4S @ pveck(2, psi)


def Wpsi(psi):
    return np.einsum("IJe,e->IJ", V5S, psi)


def vvec(psi):
    return np.einsum("IJe,J,e->I", V5S, pveck(2, psi), psi)


def g6vec(psi):
    return np.einsum("abcdef,a,b,c,d,Ief->I", V6, psi, psi, psi, psi, Lam2)


# ---------------------------------------------------------------- levels
class Level:
    """One auxiliary level: kinetic Mt (Dk,Dk), source L(psi) (Dk,Dk-1) linear
    in psi, odd dressing O(psi) (Dk,Dk) linear in psi (or None)."""

    def __init__(self, k, Mt, Lfun, Ofun):
        self.k, self.Mt, self.L, self.O = k, Mt, Lfun, Ofun


def level_from_parents(k, T2k, T2k1=None):
    """Build a level from a 2k-strand parent array (shape (N,)*2k, at least
    block-consistent) and an optional (2k+1)-strand odd parent."""
    Lkf, Lk1f = LF[k], LF[k - 1]
    Mt = Lkf @ T2k.reshape(N**k, N**k) @ Lkf.T
    Tsrc = T2k.reshape(N**k, N ** (k - 1), N)

    def Lfun(psi, Tsrc=Tsrc, Lkf=Lkf, Lk1f=Lk1f):
        return Lkf @ np.tensordot(Tsrc, psi, axes=([2], [0])) @ Lk1f.T

    Ofun = None
    if T2k1 is not None:
        Todd = T2k1.reshape(N**k, N**k, N)

        def Ofun(psi, Todd=Todd, Lkf=Lkf):
            return Lkf @ np.tensordot(Todd, psi, axes=([2], [0])) @ Lkf.T

    return Level(k, Mt, Lfun, Ofun)


# level 2 is universal: kinetic V4, source u2 (handled separately), odd V5
def O2fun(psi):
    return Wpsi(psi)


LEVEL2 = Level(2, V4S, None, O2fun)

# ---- canonical (R21/R25) level 3: block composites, from verify-b6 ----
Phi = np.einsum("abcde,Iab,Kcde->IK", V5, Lam2, Lam3)  # (D2, D3)
Nmat = Phi.T @ V4inv @ Phi
V6M = np.einsum("abcdef,Iabc,Jdef->IJ", V6, Lam3, Lam3)
M_tilde = V6M - 1.2 * Nmat


def Gsrc_dressed(psi):
    G_bare_IK = np.einsum("abcdef,Kabc,Ide,f->IK", V6, Lam3, Lam2, psi)  # (D2,D3)
    Jv = np.einsum("MJe,e->MJ", V5S, psi)
    return G_bare_IK.T - 1.2 * (Phi.T @ V4inv @ Jv)  # (D3, D2)


V7_331 = np.einsum("abcdefg,Kabc,Ldef->KLg", V7, Lam3, Lam3)
V4invPhi = V4inv @ Phi
A_S1 = np.einsum("AK,ABe,BL->KLe", V4invPhi, V5S, V4invPhi)
A_S1 = 0.5 * (A_S1 + A_S1.transpose(1, 0, 2))
V6_312 = np.einsum("abcdef,Kabc,Ief->KdI", V6, Lam3, Lam2)
A_S2 = np.einsum("KeM,ML->KLe", V6_312, V4invPhi)
A_S2 = 0.5 * (A_S2 + A_S2.transpose(1, 0, 2))
K331_dressed = V7_331 + (42.0 / 25.0) * A_S1 - (14.0 / 5.0) * A_S2  # R25 tilde_V7


def O3fun_canon(psi):
    return np.einsum("KLe,e->KL", K331_dressed, psi)


LEVEL3_CANON = Level(3, M_tilde, Gsrc_dressed, O3fun_canon)

# ---------------------------------------------------------------- series algebra
def series_inv(A):
    """Inverse of a matrix power series A[0] + g A[1] + ... (list of arrays)."""
    R = [np.linalg.inv(A[0])]
    for m in range(1, len(A)):
        acc = sum(A[j] @ R[m - j] for j in range(1, m + 1))
        R.append(-R[0] @ acc)
    return R


def H2inv_series(levels, psi, order):
    """Series (in g) of Hhat_2^{-1} for a dict {k: Level}. Top-down Schur."""
    prev_inv, prev_L = None, None
    for k in sorted(levels, reverse=True):
        lev = levels[k]
        Dk = DIM[k]
        M = [np.array(lev.Mt, dtype=float)] + [np.zeros((Dk, Dk)) for _ in range(order)]
        if lev.O is not None:
            M[1] = M[1] - lev.O(psi) / (2 * k + 1)
        if prev_inv is not None:
            fac = math.factorial(2 * k) / math.factorial(2 * k + 2)
            for m in range(order - 1):
                M[m + 2] = M[m + 2] - fac * (prev_L.T @ prev_inv[m] @ prev_L)
        prev_inv = series_inv(M)
        prev_L = lev.L(psi) if lev.L is not None else None
    return prev_inv


def value_series(levels, psi, order=ORD):
    """Coefficients c[m] of g^m in S(saddles) minus the shared V2,V3 part."""
    Hinv = H2inv_series(levels, psi, order)
    u = u2vec(psi)
    c = np.zeros(order + 1)
    for m in range(order - 1):
        c[m + 2] = (u @ Hinv[m] @ u) / 24.0
    return c


def targets(psi, order=ORD):
    t = np.zeros(order + 1)
    for m in range(2, order + 1):
        n = m + 2
        if n in VN:
            t[m] = vdiag(VN[n], psi) / math.factorial(n)
    return t


# ---------------------------------------------------------------- finite-g evaluators
def H2_finite(levels, psi, g):
    prev_inv, prev_L = None, None
    for k in sorted(levels, reverse=True):
        lev = levels[k]
        M = np.array(lev.Mt, dtype=complex if isinstance(g, complex) else float)
        if lev.O is not None:
            M = M - (g / (2 * k + 1)) * lev.O(psi)
        if prev_inv is not None:
            fac = math.factorial(2 * k) / math.factorial(2 * k + 2)
            M = M - g * g * fac * (prev_L.T @ prev_inv @ prev_L)
        prev_inv = np.linalg.inv(M)
        prev_L = lev.L(psi) if lev.L is not None else None
    return prev_inv


def onshell_closed(levels, psi, g):
    """Closed-form on-shell value (minus shared): (g^2/24) u2 Hhat_2^{-1} u2."""
    u = u2vec(psi)
    return (g * g / 24.0) * (u @ H2_finite(levels, psi, g) @ u)


def block_system(levels, psi, g):
    """Assemble the joint block-tridiagonal system A z = b (S = -z A z + 2 b z)."""
    ks = sorted(levels)
    offs, D = {}, 0
    for k in ks:
        offs[k] = D
        D += DIM[k]
    A = np.zeros((D, D), dtype=complex if isinstance(g, complex) else float)
    b = np.zeros(D, dtype=A.dtype)
    for k in ks:
        lev = levels[k]
        a_k = g ** (2 * k - 2) / math.factorial(2 * k)
        Mhat = np.array(lev.Mt, dtype=A.dtype)
        if lev.O is not None:
            Mhat = Mhat - (g / (2 * k + 1)) * lev.O(psi)
        sl = slice(offs[k], offs[k] + DIM[k])
        A[sl, sl] = a_k * Mhat
        if k == 2:
            b[sl] = a_k * u2vec(psi)
        else:
            Lk = lev.L(psi)
            slm = slice(offs[k - 1], offs[k - 1] + DIM[k - 1])
            A[sl, slm] = -a_k * Lk
            A[slm, sl] = -a_k * Lk.T
    return A, b, offs


def onshell_block(levels, psi, g):
    A, b, _ = block_system(levels, psi, g)
    z = np.linalg.solve(A, b)
    return b @ z, z


def action_direct(levels, psi, g, z, offs):
    """Direct term-by-term action evaluation (independent of the A-matrix)."""
    S = 0.0
    sig = {k: z[offs[k] : offs[k] + DIM[k]] for k in sorted(levels)}
    for k in sorted(levels):
        lev = levels[k]
        a_k = g ** (2 * k - 2) / math.factorial(2 * k)
        S += -a_k * (sig[k] @ lev.Mt @ sig[k])
        if lev.O is not None:
            S += (g ** (2 * k - 1) / math.factorial(2 * k + 1)) * (
                sig[k] @ lev.O(psi) @ sig[k]
            )
        if k == 2:
            S += 2 * a_k * (u2vec(psi) @ sig[k])
        else:
            S += 2 * a_k * (sig[k] @ (lev.L(psi) @ sig[k - 1]))
    return S


# ---------------------------------------------------------------- polynomial fits
def alphas(n):
    return [(i, j, n - i - j) for i in range(n + 1) for j in range(n + 1 - i)]


def multinom(n, a):
    return math.factorial(n) // (
        math.factorial(a[0]) * math.factorial(a[1]) * math.factorial(a[2])
    )


def fit_hom_poly(f, n):
    """Fit f (homogeneous degree n in Psi, exact evaluations) in the monomial
    basis; return coefficient dict + validation error at fresh points."""
    al = alphas(n)
    pts = rng.standard_normal((4 * len(al), N))
    rows = np.array([[p[0] ** a * p[1] ** b * p[2] ** c for (a, b, c) in al] for p in pts])
    y = np.array([f(p) for p in pts])
    c, *_ = np.linalg.lstsq(rows, y, rcond=None)
    cd = dict(zip(al, c))
    errs = []
    for _ in range(8):
        p = rng.standard_normal(N)
        val = sum(cc * p[0] ** a * p[1] ** b * p[2] ** c for (a, b, c), cc in cd.items())
        fv = f(p)
        errs.append(abs(val - fv) / max(1.0, abs(fv)))
    return cd, max(errs)


def pol_full_tensor(cd, n):
    """Fully symmetric tensor whose Veronese diagonal is sum c_alpha Psi^alpha."""
    T = np.zeros((N,) * n)
    for idx in itertools.product(range(N), repeat=n):
        a = (idx.count(0), idx.count(1), idx.count(2))
        T[idx] = cd[a] / multinom(n, a)
    return T


def mismatch_coeff(levels, m):
    """A_m(psi) = [g^m](value) - target, as an exact-evaluation function."""

    def f(psi, levels=levels, m=m):
        return value_series(levels, psi, order=m)[m] - targets(psi, order=m)[m]

    return f


# ================================================================ check 0
ok = True
det = []
psi0 = rng.standard_normal(N)
lev2only = {2: LEVEL2}
c = value_series(lev2only, psi0)
c2_pred = vdiag(V4, psi0) / 24.0
c3_pred = vdiag(V5, psi0) / 120.0
v0 = vvec(psi0)
c4_pred = (v0 @ V4inv @ v0) / 600.0
ok &= abs(c[2] - c2_pred) < TOL * max(1, abs(c2_pred))
ok &= abs(c[3] - c3_pred) < TOL * max(1, abs(c3_pred))
ok &= abs(c[4] - c4_pred) < TOL * max(1, abs(c4_pred))
det.append(f"K=2 analytic c2,c3,c4 ok (c4 = vV4inv v/600 = {c4_pred:+.5f})")
# series == contour-FFT of the closed form (tower A, K=3)
towerA3 = {2: LEVEL2, 3: LEVEL3_CANON}
cA = value_series(towerA3, psi0)
Mfft, r = 64, 0.15
gs = r * np.exp(2j * np.pi * np.arange(Mfft) / Mfft)
vals = np.array([onshell_closed(towerA3, psi0, g) for g in gs])
coef = np.fft.fft(vals) / Mfft
cfft = np.array([(coef[m] / r**m).real for m in range(ORD + 1)])
ok &= np.max(np.abs(cA[: ORD + 1] - cfft)) < 1e-7
det.append(f"series==FFT max|diff|={np.max(np.abs(cA[:ORD + 1] - cfft)):.1e}")
# closed == block solve == direct action at finite g
gt = 0.25
S_closed = onshell_closed(towerA3, psi0, gt)
S_block, z0 = onshell_block(towerA3, psi0, gt)
_, _, offs3 = block_system(towerA3, psi0, gt)
S_act = action_direct(towerA3, psi0, gt, z0, offs3)
ok &= abs(S_closed - S_block) < 1e-12 * max(1, abs(S_closed))
ok &= abs(S_closed - S_act) < 1e-12 * max(1, abs(S_closed))
det.append(f"closed==block==action at g={gt}: {abs(S_closed - S_act):.1e}")
# collapse identity for the canonical level 3
coll = Gsrc_dressed(psi0) @ pveck(2, psi0) - M_tilde @ pveck(3, psi0)
ok &= np.abs(coll).max() < 1e-9
det.append(f"collapse u3(P2)=Mt3 P3: {np.abs(coll).max():.1e}")
report(0, "machinery: evaluators agree; K=2 analytic; canonical collapse", ok, "; ".join(det))

# ================================================================ check 1
ok = True
det = []
t0 = targets(psi0)
ok &= abs(cA[4] - t0[4]) < TOL * max(1, abs(t0[4]))
ok &= abs(cA[5] - t0[5]) < TOL * max(1, abs(t0[5]))
det.append(f"tower A closes O(g^4),O(g^5): |c4-t4|={abs(cA[4] - t0[4]):.1e}, |c5-t5|={abs(cA[5] - t0[5]):.1e}")
# with O_3 removed: deficit = A5_dr - V7d/5040, A5_dr = (S2c/3 - S1/5)/600
towerA3_noO = {2: LEVEL2, 3: Level(3, M_tilde, Gsrc_dressed, None)}
c_noO = value_series(towerA3_noO, psi0)
S1 = v0 @ V4inv @ Wpsi(psi0) @ (V4inv @ v0)
S2c = g6vec(psi0) @ (V4inv @ v0)
A5dr = (S2c / 3.0 - S1 / 5.0) / 600.0
pred = A5dr - vdiag(V7, psi0) / 5040.0
ok &= abs((c_noO[5] - t0[5]) - pred) < 1e-7 * max(1, abs(pred))
det.append(f"O3 removed: c5-t5 = {c_noO[5] - t0[5]:+.6f} = A5_dr - V7d/7! = {pred:+.6f} (R25)")
report(1, "tower A == R21/R25 in the Jacobi machinery", ok, "; ".join(det))

# ================================================================ check 2
ok = True
det = []
# recursion: A6 from tower A (levels 2,3) -> T8 -> level 4 (Mt, L)
# NB: A_m is the mismatch against the FULL target (V_{m+2} included), so the
# new kernel is T_n = -n! Pol(A_{n-2}); the geometric V_n reappears through the
# polarization (Pol(A) contains -V_n/n!), i.e. T_n = V_n - n! Pol(feedback).
cd6, err6 = fit_hom_poly(mismatch_coeff(towerA3, 6), 8)
T8 = -math.factorial(8) * pol_full_tensor(cd6, 8)
lev4_noO = level_from_parents(4, T8)
towerA4_noO = {2: LEVEL2, 3: LEVEL3_CANON, 4: lev4_noO}
# A7 from tower A + level 4 (no O_4) -> T9 -> O_4
cd7, err7 = fit_hom_poly(mismatch_coeff(towerA4_noO, 7), 9)
T9 = -math.factorial(9) * pol_full_tensor(cd7, 9)
LEVEL4 = level_from_parents(4, T8, T9)
towerA4 = {2: LEVEL2, 3: LEVEL3_CANON, 4: LEVEL4}
ok &= err6 < 1e-8 and err7 < 1e-8
det.append(f"fit validation errors: A6 {err6:.1e}, A7 {err7:.1e}")
# closure through g^7 at fresh psi
psi1 = rng.standard_normal(N)
c4t = value_series(towerA4, psi1)
t1 = targets(psi1)
resid = np.max(np.abs(c4t[2:8] - t1[2:8]))
ok &= resid < 1e-7
det.append(f"c[2..7]==targets: max|resid|={resid:.1e}")
# finite-g mismatch slope ~ 8
def mism_final(g, psi=psi1):
    tgt = sum(
        g ** (n - 2) / math.factorial(n) * vdiag(VN[n], psi) for n in range(4, 10)
    )
    return onshell_closed(towerA4, psi, g) - tgt


m1, m2 = mism_final(0.08), mism_final(0.04)
slope = math.log2(abs(m1 / m2))
ok &= abs(slope - 8) < 0.25
det.append(f"mismatch log-slope = {slope:.3f} (O(g^8) residual)")
# collapse at level 4 + Veronese saddle
coll4 = LEVEL4.L(psi1) @ pveck(3, psi1) - LEVEL4.Mt @ pveck(4, psi1)
ok &= np.abs(coll4).max() < 1e-6 * max(1, np.abs(LEVEL4.Mt @ pveck(4, psi1)).max())
devs = []
for gsml in (2e-4, 1e-4):
    _, z1 = onshell_block(towerA4, psi1, gsml)
    _, _, offs4 = block_system(towerA4, psi1, gsml)
    devs.append(np.abs(z1[offs4[4] : offs4[4] + D4] - pveck(4, psi1)).max())
ok &= abs(math.log2(devs[0] / devs[1]) - 1) < 0.05  # deviation is O(g)
det.append(
    f"collapse u4(P3)=Mt4 P4: {np.abs(coll4).max():.1e}; Sigma4*-P4 = O(g) (slope {math.log2(devs[0] / devs[1]):.3f})"
)
report(2, "recursion -> T8,T9: O(g^6)+O(g^7) CLOSE (k=4 tower instance, 018 §6)", ok, "; ".join(det))

# ================================================================ check 3
ok = True
det = []
for gt in (0.2, 0.1 + 0.08j):
    S_c = onshell_closed(towerA4, psi1, gt)
    S_b, zb = onshell_block(towerA4, psi1, gt)
    _, _, off = block_system(towerA4, psi1, gt)
    S_a = action_direct(towerA4, psi1, gt, zb, off)
    ok &= abs(S_c - S_b) < 1e-11 * max(1, abs(S_c))
    ok &= abs(S_c - S_a) < 1e-11 * max(1, abs(S_c))
    det.append(f"g={gt}: closed==block==action ({abs(S_c - S_a):.1e})")
# triangularity: adding level 4 leaves c[2..5] unchanged
cA3 = value_series(towerA3, psi1)
ok &= np.max(np.abs(c4t[2:6] - cA3[2:6])) < 1e-12
det.append(f"level 4 leaves c[2..5] unchanged: {np.max(np.abs(c4t[2:6] - cA3[2:6])):.1e}")
report(3, "K=4 exactness (joint Gaussian, incl. complex g) + triangularity", ok, "; ".join(det))

# ================================================================ check 4
ok = True
det = []
eps = 0.3


def draw_nondegenerate(psi):
    """Perturbation direction with |a.psi| bounded away from 0 (else the
    diagonal-response prediction is vacuously ~0)."""
    while True:
        a = rng.standard_normal(N)
        if abs(a @ psi) > 0.5:
            return a


avec = draw_nondegenerate(psi1)
pert8 = np.array(1.0)
for _ in range(8):
    pert8 = np.multiply.outer(pert8, avec)
lev4p = level_from_parents(4, T8 + eps * pert8, T9)
cp = value_series({2: LEVEL2, 3: LEVEL3_CANON, 4: lev4p}, psi1)
shift_pred = eps * (avec @ psi1) ** 8 / math.factorial(8)
ok &= abs((cp[6] - c4t[6]) - shift_pred) < 1e-8 * max(1e-6, abs(shift_pred))
ok &= np.max(np.abs(cp[2:6] - c4t[2:6])) < 1e-12
det.append(f"T8+eps a^x8: dc6 = {cp[6] - c4t[6]:+.3e} = eps(a.psi)^8/8! = {shift_pred:+.3e}; c[2..5] fixed")
bvec = draw_nondegenerate(psi1)
pert9 = np.array(1.0)
for _ in range(9):
    pert9 = np.multiply.outer(pert9, bvec)
lev4q = level_from_parents(4, T8, T9 + eps * pert9)
cq = value_series({2: LEVEL2, 3: LEVEL3_CANON, 4: lev4q}, psi1)
shift_pred9 = eps * (bvec @ psi1) ** 9 / math.factorial(9)
ok &= abs((cq[7] - c4t[7]) - shift_pred9) < 1e-8 * max(1e-6, abs(shift_pred9))
ok &= np.max(np.abs(cq[2:7] - c4t[2:7])) < 1e-12
det.append(f"T9+eps b^x9: dc7 = {cq[7] - c4t[7]:+.3e} = eps(b.psi)^9/9! = {shift_pred9:+.3e}")
report(4, "diagonal FORCING: c_n responds to T_n exactly by diag/n!", ok, "; ".join(det))

# ================================================================ check 5
ok = True
det = []
# tower B: uniform polarized kernels from scratch
cd4, e4 = fit_hom_poly(mismatch_coeff(lev2only, 4), 6)
T6B = -math.factorial(6) * pol_full_tensor(cd4, 6)
lev3B_noO = level_from_parents(3, T6B)
cd5, e5 = fit_hom_poly(mismatch_coeff({2: LEVEL2, 3: lev3B_noO}, 5), 7)
T7B = -math.factorial(7) * pol_full_tensor(cd5, 7)
lev3B = level_from_parents(3, T6B, T7B)
cd6B, e6B = fit_hom_poly(mismatch_coeff({2: LEVEL2, 3: lev3B}, 6), 8)
T8B = -math.factorial(8) * pol_full_tensor(cd6B, 8)
lev4B_noO = level_from_parents(4, T8B)
cd7B, e7B = fit_hom_poly(mismatch_coeff({2: LEVEL2, 3: lev3B, 4: lev4B_noO}, 7), 9)
T9B = -math.factorial(9) * pol_full_tensor(cd7B, 9)
towerB = {2: LEVEL2, 3: level_from_parents(3, T6B, T7B), 4: level_from_parents(4, T8B, T9B)}
cB = value_series(towerB, psi1)
residB = np.max(np.abs(cB[2:8] - t1[2:8]))
ok &= max(e4, e5, e6B, e7B) < 1e-8 and residB < 1e-7
det.append(f"tower B (all-polarized) closes: max|c-t|={residB:.1e}")
# same diagonal, different tensor at n=6
Mt3B = towerB[3].Mt
dpsi_diag = pveck(3, psi1) @ Mt3B @ pveck(3, psi1) - pveck(3, psi1) @ M_tilde @ pveck(3, psi1)
tdist = np.abs(Mt3B - M_tilde).max()
ok &= abs(dpsi_diag) < 1e-7 * max(1, abs(pveck(3, psi1) @ M_tilde @ pveck(3, psi1)))
ok &= tdist > 1e-3
det.append(f"T6: diag equal ({dpsi_diag:+.1e}) but kernels differ (max|dM|={tdist:.3f})")
# the freedom feeds forward: d7 differs between towers
d7A = vdiag(V7, psi1) + (42.0 / 25.0) * (
    vvec(psi1) @ V4inv @ Wpsi(psi1) @ (V4inv @ vvec(psi1))
) - (14.0 / 5.0) * (g6vec(psi1) @ (V4inv @ vvec(psi1)))
d7B = sum(cc * psi1[0] ** a * psi1[1] ** b * psi1[2] ** c for (a, b, c), cc in cd5.items())
d7B = -math.factorial(7) * d7B
ok &= abs(d7A - d7B) > 1e-4 * max(1, abs(d7A))
det.append(f"d7 differs between towers: {d7A:+.4f} vs {d7B:+.4f} (feeds forward, re-absorbed)")
report(5, "presentation freedom: polarized tower closes; off-diagonal free, diagonal pinned", ok, "; ".join(det))

# ================================================================ check 6
ok = True
det = []
g = 0.2
psig = rng.standard_normal(N)
dpsi = rng.standard_normal(N)
levels = towerA4
ks = sorted(levels)
# assemble Hhat_k, Mhat_k, L_k top-down, plus their delta-psi variations
Mhat, Hhat, Lk, dMhat, dLk = {}, {}, {}, {}, {}
for k in ks:
    lev = levels[k]
    Mh = np.array(lev.Mt)
    dMh = np.zeros_like(Mh)
    if lev.O is not None:
        Mh = Mh - (g / (2 * k + 1)) * lev.O(psig)
        dMh = dMh - (g / (2 * k + 1)) * lev.O(dpsi)
    Mhat[k], dMhat[k] = Mh, dMh
    if k > 2:
        Lk[k], dLk[k] = lev.L(psig), lev.L(dpsi)
dHhat = {}
for k in reversed(ks):
    if k == ks[-1]:
        Hhat[k], dHhat[k] = Mhat[k], dMhat[k]
    else:
        fac = math.factorial(2 * k) / math.factorial(2 * k + 2)
        Hip = np.linalg.inv(Hhat[k + 1])
        Hhat[k] = Mhat[k] - g * g * fac * (Lk[k + 1].T @ Hip @ Lk[k + 1])
        dHhat[k] = dMhat[k] - g * g * fac * (
            dLk[k + 1].T @ Hip @ Lk[k + 1]
            + Lk[k + 1].T @ Hip @ dLk[k + 1]
            - Lk[k + 1].T @ Hip @ dHhat[k + 1] @ Hip @ Lk[k + 1]
        )
u2g = u2vec(psig)
dp = LF[2] @ (np.multiply.outer(psig, dpsi) + np.multiply.outer(dpsi, psig)).ravel()
du2 = V4S @ dp
# saddles and completed square
sstar = {}
sstar[2] = np.linalg.solve(Hhat[2], u2g)
for k in ks[1:]:
    sstar[k] = np.linalg.solve(Hhat[k], Lk[k] @ sstar[k - 1])
value = u2g @ sstar[2] * (g * g / 24.0)
# off-shell point
sig = {k: sstar[k] + 0.4 * rng.standard_normal(DIM[k]) for k in ks}
Y = {2: sig[2] - sstar[2]}
for k in ks[1:]:
    Y[k] = sig[k] - np.linalg.solve(Hhat[k], Lk[k] @ sig[k - 1])
zoff = np.concatenate([sig[k] for k in ks])
_, _, offG = block_system(levels, psig, g)
S_off = action_direct(levels, psig, g, zoff, offG)
S_sq = value + sum(
    -(g ** (2 * k - 2) / math.factorial(2 * k)) * (Y[k] @ Hhat[k] @ Y[k]) for k in ks
)
ok &= abs(S_off - S_sq) < 1e-11 * max(1, abs(S_off))
det.append(f"completed square exact: |S - (value + sum -a_k Y Hhat Y)| = {abs(S_off - S_sq):.1e}")
# gauge variation: laws dY_k = -1/2 Hhat^-1 dHhat Y_k; saddle tracking
dY = {k: -0.5 * np.linalg.solve(Hhat[k], dHhat[k] @ Y[k]) for k in ks}
dsstar = {2: np.linalg.solve(Hhat[2], du2 - dHhat[2] @ sstar[2])}
dsig = {2: dsstar[2] + dY[2]}
for k in ks[1:]:
    dcond = np.linalg.solve(
        Hhat[k], dLk[k] @ sig[k - 1] + Lk[k] @ dsig[k - 1] - dHhat[k] @ np.linalg.solve(Hhat[k], Lk[k] @ sig[k - 1])
    )
    dsig[k] = dcond + dY[k]


def dpsi_S_explicit(sigd, x, dx):
    out = (g * g / 12.0) * (
        sigd[2] @ (V4S @ (LF[2] @ (np.multiply.outer(x, dx) + np.multiply.outer(dx, x)).ravel()))
    )
    for k in ks:
        lev = levels[k]
        a_k = g ** (2 * k - 2) / math.factorial(2 * k)
        if lev.O is not None:
            out += (g ** (2 * k - 1) / math.factorial(2 * k + 1)) * (
                sigd[k] @ lev.O(dx) @ sigd[k]
            )
        if k > 2:
            out += 2 * a_k * (sigd[k] @ (lev.L(dx) @ sigd[k - 1]))
    return out


def grad_S(sigd):
    gr = {}
    for k in ks:
        a_k = g ** (2 * k - 2) / math.factorial(2 * k)
        gk = -2 * a_k * (Mhat[k] @ sigd[k])
        gk += 2 * a_k * (u2g if k == 2 else Lk[k] @ sigd[k - 1])
        if k + 1 in levels:
            a_k1 = g ** (2 * k) / math.factorial(2 * k + 2)
            gk += 2 * a_k1 * (Lk[k + 1].T @ sigd[k + 1])
        gr[k] = gk
    return gr


gr = grad_S(sig)
lhs = sum(gr[k] @ dsig[k] for k in ks) + dpsi_S_explicit(sig, psig, dpsi)
rhs = dpsi_S_explicit(sstar, psig, dpsi)  # envelope: = delta(value)
scale = max(abs(lhs), abs(rhs), 1e-3)
ok &= abs(lhs - rhs) < 1e-9 * scale
det.append(f"exact invariance deltaS = delta[value]: |lhs-rhs|/scale = {abs(lhs - rhs) / scale:.1e}")
# falsification legs
for kf in (4, 2):
    dsigf = dict(dsig)
    # rebuild the chain with dY_kf = 0
    dsf = {2: dsstar[2] + (dY[2] if kf != 2 else 0 * dY[2])}
    for k in ks[1:]:
        dcond = np.linalg.solve(
            Hhat[k],
            dLk[k] @ sig[k - 1] + Lk[k] @ dsf[k - 1] - dHhat[k] @ np.linalg.solve(Hhat[k], Lk[k] @ sig[k - 1]),
        )
        dsf[k] = dcond + (dY[k] if k != kf else 0 * dY[k])
    lhs_f = sum(gr[k] @ dsf[k] for k in ks) + dpsi_S_explicit(sig, psig, dpsi)
    a_kf = g ** (2 * kf - 2) / math.factorial(2 * kf)
    resid_pred = -a_kf * (Y[kf] @ dHhat[kf] @ Y[kf])
    ok &= abs((lhs_f - rhs) - resid_pred) < 1e-9 * max(abs(resid_pred), 1e-6)
    ok &= abs(resid_pred) > 1e-10
    det.append(f"dY{kf}=0 residual = {lhs_f - rhs:+.3e} = pred {resid_pred:+.3e}")
# genuine homogeneity test (critic M1): the law is linear in Y and nonzero on generic Y
dY4_1 = -0.5 * np.linalg.solve(Hhat[4], dHhat[4] @ Y[4])
dY4_2 = -0.5 * np.linalg.solve(Hhat[4], dHhat[4] @ (2.0 * Y[4]))
ok &= np.abs(dY4_2 - 2.0 * dY4_1).max() < 1e-12 * max(np.abs(dY4_1).max(), 1e-12)
ok &= np.abs(dY4_1).max() > 1e-12
det.append(f"laws homogeneous: deltaY4(2Y) = 2 deltaY4(Y) at {np.abs(dY4_2 - 2.0 * dY4_1).max():.1e}, |deltaY4| = {np.abs(dY4_1).max():.2e}")
report(6, "all-orders gauge law at K=4: kernel rotations, exact equality, falsification legs", ok, "; ".join(det))

# ================================================================ check 7
ok = True
det = []
# zero the level-4 source: V8 contact lost, c6 deficit = A6 exactly
lev4_noL = Level(4, LEVEL4.Mt, lambda psi: np.zeros((D4, D3)), LEVEL4.O)
c_noL = value_series({2: LEVEL2, 3: LEVEL3_CANON, 4: lev4_noL}, psi1)
A6_psi1 = mismatch_coeff(towerA3, 6)(psi1)
ok &= abs((c_noL[6] - t1[6]) - A6_psi1) < 1e-9 * max(1, abs(A6_psi1))
ok &= abs(A6_psi1) > 1e-8
det.append(f"u4=0: c6-t6 = {c_noL[6] - t1[6]:+.5f} = A6 = {A6_psi1:+.5f} (contact lost => source forced)")
# Sigma_4* uses Sigma_3: dSigma4*/dSigma3 = Hhat4^{-1} L4 != 0
sens = np.linalg.solve(Mhat[4], Lk[4])
ok &= np.abs(sens).max() > 1e-3
det.append(f"dSigma4*/dSigma3 = Hhat4^-1 L4, max entry {np.abs(sens).max():.3f} != 0 (uses Sigma_3)")
report(7, "level-4 source u4(Sigma_3) forced and uses Sigma_3 (Harold's O(g^6) reading)", ok, "; ".join(det))

# ---------------------------------------------------------------- summary
print()
ntot = 8
print(
    f"{ntot - len(set(failures))}/{ntot} checks PASS"
    + (f"  FAILURES: {sorted(set(failures))}" if failures else "")
)
raise SystemExit(len(set(failures)))
