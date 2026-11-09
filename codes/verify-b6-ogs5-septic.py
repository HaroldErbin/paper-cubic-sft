#!/usr/bin/env python3
"""
verify-b6-ogs5-septic.py — machine checks for derivation 018 (B6): the O(g_s^5)
septic closure of the cubic (Hubbard-Stratonovich) tower, dressed presentation.

Setting (finite-dimensional binding, physical grading, all fields even, e^S
weight, generic totally symmetric V4..V7 — same conventions as
verify-b4-sigma3.py / verify-b5-ogs4-gauge-eom-ibl.py; CFT analytics of the
inverses = A2(iii)/T4 carve-out).  Fields: Psi in H (dim N), Sigma_2 in Sym^2,
Sigma_3 in Sym^3.  The O(g^4)-closed dressed action (R21) is

  S_dr = -(g^2/4!) V4(S2,S2) + (2g^2/4!) V4(S2,P) + (g^3/5!) V5(S2,S2,Psi)
         + (g^4/6!) [ -tilde_M(S3,S3) + 2 <tilde_u(S2), S3> ],

tilde_M = M - (6/5) Phi^T V4inv Phi,  tilde_u = u - (6/5) Phi^T V4inv v(S2).

Checks:
 (0) kernel constructions + on-shell diagonals: the septic composite invariants
     S1 = v V4inv W V4inv v (three-V5 chain), S2c = V6(Psi^4, V4inv v)
     (V6-V4inv-V5 chain), S3c = C(P,P,V4inv v) (strand-split three-V5 chain);
     the (3,3,1) kernels A_S1, A_S2 and the (3,2,2) kernels B_S1, B_S2 hit
     these diagonals; independence rank of {V7(Psi^7), S1, S2c, S3c}.
 (1) the EXACT closed-form feedback of the dressed action (sequential Gaussian):
       F_dr(g) = S_dr(saddles) - S_eff  (all orders in g, closed form)
     against the independent joint Newton saddle solve; and the O(g^5) headline
       A5_dr = (1/600) [ (1/3) S2c - (1/5) S1 ]
     by Richardson extrapolation.
 (2) CLOSURE at O(g^5): adding the single dressed (3,3,1) coupling
       (g^5/7!) tilde_V7(S3,S3,Psi),
       tilde_V7 = V7|331 + (42/25) A_S1 - (14/5) A_S2,
     the on-shell mismatch against S_eff^(7) is O(g^6) (Richardson + log-slope);
     lower orders undisturbed.
 (3) coefficient FORCING: bare V7 alone leaves A5_dr; perturbing each of the
     three coefficients (1, 42/25, -14/5) leaves the matching invariant's
     residual, at the predicted size.
 (4) the (3,2,2) alternative and the mix: the strand-split kernels
     B = V7|322 + (42/25) B_S1 - (14/5) B_S2 close with (a7,b7)=(0,1), and the
     mix (0.4,0.6) closes too => the partition menu is presentation freedom.
 (5) scheme-A-literal FAILURE: on the minimal Sigma_2-only O(g^4) action
     (W6 = V6 - 6/5 C, R19) with Sigma_3 entering only at O(g^5) (kinetic
     V6(S3,S3) at O(g^4), NO O(g^4) source), the (3,2,2) coupling cannot supply
     the V7 contact: mismatch/g^5 -> A5_min - V7(Psi^7)/7! for ANY (b7, kernel);
     the Sigma_3-sector value scales as g^6.  Also corroborates
     A5_min = (1/600) [ (1/2) S2c - (1/5) S1 - (1/5) S3c ]  (013 check 2 in the
     S-basis).
 (6) power-counting / saturation table for the O(g^5) menu: only (3,3,1) and
     (3,2,2) admissible; Sigma_4 excluded (divergent branch); ghost saturations.
 (7) gauge law at O(g^5) (dressed + (3,3,1)): the Sigma_3 kinetic becomes
     Psi-dependent, so R21's delta Y3 = 0 FAILS; the exact kernel-rotation laws
       delta Y3 = -(1/2) Mhat^{-1} (delta Mhat) Y3,
       delta Y2 = -(1/2) Hhat^{-1} (delta Hhat) Y2
     restore the exact off-shell equality delta S = delta[S_eff^(7) + F6]
     (all directional derivatives analytic; falsification legs match the
     predicted residuals).

All checks PASS/FAIL; exit code = number of failures.
"""

import itertools
import math
import sys

import numpy as np

SEED = int(sys.argv[1]) if len(sys.argv) > 1 else 20260707
rng = np.random.default_rng(SEED)
np.set_printoptions(precision=6, suppress=True)

N = 3
DS2 = N * (N + 1) // 2
DS3 = N * (N + 1) * (N + 2) // 6
TOL = 1e-9

failures = []


def report(num, name, ok, detail=""):
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] check ({num}) {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        failures.append(num)


def sym_tensor(shape):
    T = rng.standard_normal(shape)
    S = np.zeros_like(T)
    for perm in itertools.permutations(range(len(shape))):
        S += np.transpose(T, perm)
    return S / math.factorial(len(shape))


V4 = sym_tensor((N,) * 4)
V5 = sym_tensor((N,) * 5)
V6 = sym_tensor((N,) * 6)
V7 = sym_tensor((N,) * 7)

# ---- orthonormal Sym^2 / Sym^3 bases (as in verify-b5) ----
Lam2 = []
for a in range(N):
    E = np.zeros((N, N))
    E[a, a] = 1.0
    Lam2.append(E)
for a in range(N):
    for b in range(a + 1, N):
        E = np.zeros((N, N))
        E[a, b] = E[b, a] = 1 / np.sqrt(2)
        Lam2.append(E)
Lam2 = np.array(Lam2)

Lam3 = []
for a in range(N):
    for b in range(a, N):
        for c in range(b, N):
            M3 = np.zeros((N, N, N))
            for perm in itertools.permutations((a, b, c)):
                M3[perm] += 1.0
            M3 /= np.linalg.norm(M3)
            Lam3.append(M3)
Lam3 = np.array(Lam3)

V4S = np.einsum("abcd,Iab,Jcd->IJ", V4, Lam2, Lam2)
V5S = np.einsum("abcde,Iab,Jcd->IJe", V5, Lam2, Lam2)
V6M = np.einsum("abcdef,Iabc,Jdef->IJ", V6, Lam3, Lam3)
V6S3 = np.einsum("abcdef,Iab,Jcd,Kef->IJK", V6, Lam2, Lam2, Lam2)
V4inv = np.linalg.inv(V4S)

# Phi-map (015 section 2) and dressed kinetic
Phi = np.einsum("abcde,Iab,Kcde->IK", V5, Lam2, Lam3)  # (DS2, DS3)
Nmat = Phi.T @ V4inv @ Phi
M_tilde = V6M - 1.2 * Nmat
M_tilde_inv = np.linalg.inv(M_tilde)

# R19 composite C (strand-split, from verify-b3) and W6 kernel for scheme A
C_raw = np.einsum("Kef,MIe,MN,NJf->IJK", Lam2, V5S, V4inv, V5S)
T_C = (C_raw + C_raw.transpose(2, 1, 0) + C_raw.transpose(0, 2, 1)) / 3.0
W6kern = V6S3 - 1.2 * T_C  # scheme-A three-Sigma_2 vertex (R19)

# V7 restrictions
V7_331 = np.einsum("abcdefg,Kabc,Ldef->KLg", V7, Lam3, Lam3)  # (DS3,DS3,N)
V7_322 = np.einsum("abcdefg,Kabc,Ide,Jfg->KIJ", V7, Lam3, Lam2, Lam2)
V7_322 = 0.5 * (V7_322 + V7_322.transpose(0, 2, 1))

# ---- composite septic kernels ----
V4invPhi = V4inv @ Phi  # (DS2, DS3)
# (3,3,1): A_S1(A,B,psi) = Phi(A)^T V4inv V5(.,.,psi) V4inv Phi(B)
A_S1 = np.einsum("AK,ABe,BL->KLe", V4invPhi, V5S, V4invPhi)
A_S1 = 0.5 * (A_S1 + A_S1.transpose(1, 0, 2))
# (3,3,1): A_S2(A,B,psi) = sym_{AB} V6(A, psi, V4inv Phi(B))
V6_312 = np.einsum("abcdef,Kabc,Ief->KdI", V6, Lam3, Lam2)  # (DS3, N, DS2)
A_S2 = np.einsum("KeM,ML->KLe", V6_312, V4invPhi)
A_S2 = 0.5 * (A_S2 + A_S2.transpose(1, 0, 2))
# (3,2,2): B_S2(A,X,Y) = sym_{XY} sum_strands V6(A, x1, V4inv V5(., Y, x2))
Z1 = np.einsum("MI,IJg->MJg", V4inv, V5S)  # (DS2:M, DS2:J=Y, N:g)
B_S2 = np.einsum("KdM,MJg,Idg->KIJ", V6_312, Z1, Lam2)
B_S2 = 0.5 * (B_S2 + B_S2.transpose(0, 2, 1))
# (3,2,2): B_S1(A,X,Y) = sym_{XY} sum_strands Phi(A)^T V4inv V5(.,.,x1) V4inv V5(.,Y,x2)
B_S1 = np.einsum("AK,ABd,BC,CJg,Idg->KIJ", V4invPhi, V5S, V4inv, V5S, Lam2)
B_S1 = 0.5 * (B_S1 + B_S1.transpose(0, 2, 1))

# forced coefficients (analytic prediction): tilde_V7 = V7 + (42/25) S1-kernel - (14/5) S2-kernel
CF1, CF2 = 42.0 / 25.0, -14.0 / 5.0
K331_dressed = V7_331 + CF1 * A_S1 + CF2 * A_S2
K322_dressed = V7_322 + CF1 * B_S1 + CF2 * B_S2


# ---- basic field maps ----
def sym_coords2(Mmat):
    return np.einsum("Iab,ab->I", Lam2, (Mmat + Mmat.T) / 2)


def pvec(psi):
    return sym_coords2(np.outer(psi, psi))


def p3vec(psi):
    return np.einsum("Iabc,a,b,c->I", Lam3, psi, psi, psi)


def vvec(psi):
    return np.einsum("IJe,J,e->I", V5S, pvec(psi), psi)


def Wpsi(psi):
    return np.einsum("IJe,e->IJ", V5S, psi)


def V6_psi6(psi):
    return np.einsum("abcdef,a,b,c,d,e,f->", V6, *([psi] * 6))


def V7_psi7(psi):
    return np.einsum("abcdefg,a,b,c,d,e,f,g->", V7, *([psi] * 7))


def g6vec(psi):
    """g6_I = V6(Psi^{x4}, Lam2_I)."""
    return np.einsum("abcdef,a,b,c,d,Ief->I", V6, psi, psi, psi, psi, Lam2)


def septic_invariants(psi):
    v = vvec(psi)
    Viv = V4inv @ v
    S1 = v @ V4inv @ Wpsi(psi) @ Viv
    S2c = g6vec(psi) @ Viv
    S3c = np.einsum("IJK,I,J,K->", C_raw, pvec(psi), pvec(psi), sym_coords2(np.einsum("I,Iab->ab", Viv, Lam2)))
    return S1, S2c, S3c


# dressed Sigma_3 source machinery (from verify-b5)
def Gsrc_dressed(psi):
    G_bare_IK = np.einsum("abcdef,Kabc,Ide,f->IK", V6, Lam3, Lam2, psi)  # (DS2,DS3)
    Jv = np.einsum("MJe,e->MJ", V5S, psi)
    return G_bare_IK.T - 1.2 * (Phi.T @ V4inv @ Jv)  # (DS3, DS2): u_tilde = Gsrc @ sig2


# ---------------------------------------------------------------- check 0
ok = True
det = []
psi0 = rng.standard_normal(N)
p0, p30 = pvec(psi0), p3vec(psi0)
v0 = vvec(psi0)
S1_0, S2_0, S3_0 = septic_invariants(psi0)
V7d = V7_psi7(psi0)
# V7 restrictions hit the diagonal
d331 = np.einsum("KLe,K,L,e->", V7_331, p30, p30, psi0)
d322 = np.einsum("KIJ,K,I,J->", V7_322, p30, p0, p0)
ok &= abs(d331 - V7d) < TOL * max(1, abs(V7d)) and abs(d322 - V7d) < TOL * max(1, abs(V7d))
det.append(f"V7|331(p3,p3,psi)=V7|322(p3,P,P)=V7(psi^7)={V7d:+.4f}")
# composite kernels hit S1 / S2c
dA1 = np.einsum("KLe,K,L,e->", A_S1, p30, p30, psi0)
dA2 = np.einsum("KLe,K,L,e->", A_S2, p30, p30, psi0)
dB1 = np.einsum("KIJ,K,I,J->", B_S1, p30, p0, p0)
dB2 = np.einsum("KIJ,K,I,J->", B_S2, p30, p0, p0)
ok &= abs(dA1 - S1_0) < TOL * abs(S1_0) and abs(dB1 - S1_0) < TOL * abs(S1_0)
ok &= abs(dA2 - S2_0) < TOL * abs(S2_0) and abs(dB2 - S2_0) < TOL * abs(S2_0)
det.append(f"A_S1=B_S1 diag={S1_0:+.4f}; A_S2=B_S2 diag={S2_0:+.4f}; S3c={S3_0:+.4f}")
# independence: {V7(psi^7), S1, S2c, S3c} have rank 4 across draws
rows = []
for _ in range(6):
    ps = rng.standard_normal(N)
    s1, s2, s3 = septic_invariants(ps)
    rows.append([V7_psi7(ps), s1, s2, s3])
sv = np.linalg.svd(np.array(rows), compute_uv=False)
ok &= sv[3] / sv[0] > 1e-6
det.append(f"invariant matrix svals ratio min/max = {sv[3] / sv[0]:.1e} (rank 4)")
report(0, "kernels, on-shell diagonals, invariant independence", ok, "; ".join(det))


# ---------------------------------------------------------------- actions
def S_total(sig2, sig3, psi, g, a7=0.0, b7=0.0, k331=None, k322=None, schemeA=False):
    """Total action minus shared V2,V3 part."""
    p = pvec(psi)
    S = (
        -(g**2 / 24) * sig2 @ V4S @ sig2
        + (g**2 / 12) * sig2 @ V4S @ p
        + (g**3 / 120) * np.einsum("IJe,I,J,e->", V5S, sig2, sig2, psi)
    )
    if schemeA:
        # minimal Sigma_2-only O(g^4) sector (R19 W6) + bare Sigma_3 kinetic, NO source
        S += (g**4 / 720) * np.einsum("IJK,I,J,K->", W6kern, sig2, sig2, sig2)
        S += (g**4 / 720) * (-(sig3 @ V6M @ sig3))
    else:
        u_t = Gsrc_dressed(psi) @ sig2
        S += (g**4 / 720) * (-(sig3 @ M_tilde @ sig3) + 2 * sig3 @ u_t)
    if a7 and k331 is not None:
        S += (g**5 / 5040) * a7 * np.einsum("KLe,K,L,e->", k331, sig3, sig3, psi)
    if b7 and k322 is not None:
        S += (g**5 / 5040) * b7 * np.einsum("KIJ,K,I,J->", k322, sig3, sig2, sig2)
    return S


def grad_total(sig2, sig3, psi, g, a7=0.0, b7=0.0, k331=None, k322=None, schemeA=False):
    p = pvec(psi)
    g2 = (
        -(g**2 / 12) * V4S @ sig2
        + (g**2 / 12) * V4S @ p
        + (g**3 / 60) * np.einsum("IJe,J,e->I", V5S, sig2, psi)
    )
    if schemeA:
        g2 += (g**4 / 240) * np.einsum("IJK,J,K->I", W6kern, sig2, sig2)
        g3 = (g**4 / 720) * (-2 * V6M @ sig3)
    else:
        Gs = Gsrc_dressed(psi)
        g2 += (g**4 / 360) * (Gs.T @ sig3)
        g3 = (g**4 / 720) * (-2 * M_tilde @ sig3 + 2 * Gs @ sig2)
    if a7 and k331 is not None:
        g3 += (g**5 / 2520) * a7 * np.einsum("KLe,L,e->K", k331, sig3, psi)
    if b7 and k322 is not None:
        g2 += (g**5 / 2520) * b7 * np.einsum("KIJ,K,J->I", k322, sig3, sig2)
        g3 += (g**5 / 5040) * b7 * np.einsum("KIJ,I,J->K", k322, sig2, sig2)
    return np.concatenate([g2, g3])


def solve_saddle(psi, g, **kw):
    """Joint (Sigma_2, Sigma_3) Newton with g-continuation, init (P, p3)."""
    z = np.concatenate([pvec(psi), p3vec(psi)])
    for gcur in np.linspace(0.0, g, 2 + int(g / 0.02))[1:]:
        for _ in range(60):
            gr = grad_total(z[:DS2], z[DS2:], psi, gcur, **kw)
            if np.abs(gr).max() < 1e-14:
                break
            J = np.zeros((DS2 + DS3, DS2 + DS3))
            h = 1e-6
            for i in range(DS2 + DS3):
                zp, zm = z.copy(), z.copy()
                zp[i] += h
                zm[i] -= h
                J[:, i] = (
                    grad_total(zp[:DS2], zp[DS2:], psi, gcur, **kw)
                    - grad_total(zm[:DS2], zm[DS2:], psi, gcur, **kw)
                ) / (2 * h)
            z = z - np.linalg.solve(J, gr)
    gn = np.abs(grad_total(z[:DS2], z[DS2:], psi, g, **kw)).max()
    assert gn < 1e-11, f"saddle |grad|={gn:.1e}"
    return z[:DS2], z[DS2:]


def Seff7_minus_shared(psi, g):
    p = pvec(psi)
    return (
        (g**2 / 24) * p @ V4S @ p
        + (g**3 / 120) * np.einsum("IJe,I,J,e->", V5S, p, p, psi)
        + (g**4 / 720) * V6_psi6(psi)
        + (g**5 / 5040) * V7_psi7(psi)
    )


def mismatch(psi, g, **kw):
    s2, s3 = solve_saddle(psi, g, **kw)
    return S_total(s2, s3, psi, g, **kw) - Seff7_minus_shared(psi, g)


def richardson5(f, g0):
    """Extract c5 from f(g) = c5 g^5 + c6 g^6 + c7 g^7 (3-point, halving)."""
    f1, f2, f3 = f(g0) / g0**5, f(g0 / 2) / (g0 / 2) ** 5, f(g0 / 4) / (g0 / 4) ** 5
    return (f1 - 6 * f2 + 8 * f3) / 3.0


# ---- exact closed-form on-shell value for the (3,3,1)-dressed family ----
def onshell_closed(psi, g, a7=0.0, k331=None):
    """Sequential exact Gaussian: eliminate Sigma_3, then Sigma_2 (both exact)."""
    p, p3 = pvec(psi), p3vec(psi)
    v = vvec(psi)
    Mhat = M_tilde - (g / 7) * a7 * np.einsum("KLe,e->KL", k331, psi) if a7 else M_tilde
    Mhat_inv = np.linalg.inv(Mhat)
    Gs = Gsrc_dressed(psi)  # u_tilde = Gs @ sig2 ; L_tilde = Gs (linear map)
    uP = Gs @ p  # = M_tilde p3 (collapse) — independent of a7
    # X-sector data: K5 = V4 - (g/5) W - (g^2/30) Gs^T Mhat^{-1} Gs ; w = Gs^T Mhat^{-1} uP
    K5 = V4S - (g / 5) * Wpsi(psi) - (g**2 / 30) * (Gs.T @ Mhat_inv @ Gs)
    w = Gs.T @ Mhat_inv @ uP
    bvec = v + (g / 6) * w
    return (
        (g**2 / 24) * p @ V4S @ p
        + (g**3 / 120) * np.einsum("IJe,I,J,e->", V5S, p, p, psi)
        + (g**4 / 720) * uP @ Mhat_inv @ uP
        + (g**4 / 600) * bvec @ np.linalg.solve(K5, bvec)
    )


# ---------------------------------------------------------------- check 1
ok = True
det = []
psi = rng.standard_normal(N)
# (a) closed form vs joint Newton at finite g (exactness of the sequential Gaussian)
g_test = 0.25
s2, s3 = solve_saddle(psi, g_test)
S_newton = S_total(s2, s3, psi, g_test)
S_closed = onshell_closed(psi, g_test)
ok &= abs(S_newton - S_closed) < 1e-12 * max(1, abs(S_closed))
det.append(f"closed form = Newton at g={g_test}: |diff|={abs(S_newton - S_closed):.1e}")
# (b) A5_dr headline by Richardson on the closed form
S1_, S2_, S3_ = septic_invariants(psi)
A5_dr_pred = (S2_ / 3 - S1_ / 5) / 600


def mism_closed(g):
    return onshell_closed(psi, g) - Seff7_minus_shared(psi, g) + (g**5 / 5040) * V7_psi7(psi)
    # note: S_dr has no O(g^5) coupling, so compare against S_eff^(6): add back the V7 term


A5_num = richardson5(mism_closed, 0.04)
ok &= abs(A5_num - A5_dr_pred) < 1e-5 * max(1, abs(A5_dr_pred))
det.append(f"A5_dr = {A5_num:+.8f} vs (1/600)[S2c/3 - S1/5] = {A5_dr_pred:+.8f}")
report(1, "exact dressed feedback F_dr + A5_dr = (1/600)[(1/3)S2c - (1/5)S1]", ok, "; ".join(det))

# ---------------------------------------------------------------- check 2
ok = True
det = []


def mism_closed_331(g):
    return onshell_closed(psi, g, a7=1.0, k331=K331_dressed) - Seff7_minus_shared(psi, g)


c5 = richardson5(mism_closed_331, 0.04)
ok &= abs(c5) < 1e-6 * max(1, abs(A5_dr_pred))
det.append(f"mismatch/g^5 -> {c5:+.2e} (closes)")
# log-slope -> 6
m1, m2 = mism_closed_331(0.04), mism_closed_331(0.02)
slope = math.log2(abs(m1 / m2))
ok &= abs(slope - 6) < 0.15
det.append(f"log-slope = {slope:.3f} (O(g^6) residual)")
# lower orders undisturbed: mismatch/g^4 -> 0 too
m4 = mism_closed_331(0.01) / 0.01**4
ok &= abs(m4) < 1e-4
det.append(f"mismatch/g^4 at g=0.01: {m4:.1e} (lower orders intact)")
report(2, "CLOSURE at O(g^5): dressed (3,3,1) tilde_V7 = V7 + (42/25)A_S1 - (14/5)A_S2", ok, "; ".join(det))

# ---------------------------------------------------------------- check 3
ok = True
det = []
# bare V7 alone leaves exactly A5_dr
c5_bare = richardson5(lambda g: onshell_closed(psi, g, a7=1.0, k331=V7_331) - Seff7_minus_shared(psi, g), 0.04)
ok &= abs(c5_bare - A5_dr_pred) < 1e-5 * max(1, abs(A5_dr_pred))
det.append(f"bare V7: residual/g^5 = {c5_bare:+.6f} = A5_dr (dressing forced)")
# perturbing each coefficient leaves the predicted residual: delta * diag / 5040
for name, kern, diag in (
    ("V7-coeff", V7_331, V7_psi7(psi)),
    ("S1-coeff", A_S1, S1_),
    ("S2-coeff", A_S2, S2_),
):
    dlt = 0.5
    kpert = K331_dressed + dlt * kern
    c5p = richardson5(lambda g: onshell_closed(psi, g, a7=1.0, k331=kpert) - Seff7_minus_shared(psi, g), 0.04)
    pred = dlt * diag / 5040
    ok &= abs(c5p - pred) < 1e-4 * max(1, abs(pred))
    det.append(f"{name}+0.5: residual = {c5p:+.6f} = pred {pred:+.6f}")
report(3, "coefficient forcing: (1, 42/25, -14/5) all pinned", ok, "; ".join(det))

# ---------------------------------------------------------------- check 4
ok = True
det = []
# pure (3,2,2) with strand-split dressed kernels
c5_322 = richardson5(lambda g: mismatch(psi, g, b7=1.0, k322=K322_dressed), 0.04)
ok &= abs(c5_322) < 1e-5 * max(1, abs(A5_dr_pred))
det.append(f"(a7,b7)=(0,1) dressed B-kernels: mismatch/g^5 = {c5_322:+.2e} (closes)")
# mix
c5_mix = richardson5(
    lambda g: mismatch(psi, g, a7=0.4, b7=0.6, k331=K331_dressed, k322=K322_dressed), 0.04
)
ok &= abs(c5_mix) < 1e-5 * max(1, abs(A5_dr_pred))
det.append(f"(a7,b7)=(0.4,0.6): mismatch/g^5 = {c5_mix:+.2e} (closes)")
report(4, "(3,2,2) and mixed realizations close: partition menu = presentation freedom", ok, "; ".join(det))

# ---------------------------------------------------------------- check 5
ok = True
det = []
A5_min_pred = (S2_ / 2 - S1_ / 5 - S3_ / 5) / 600
for tag, b7, k322 in (
    ("b7=0", 0.0, None),
    ("b7=1 bare", 1.0, V7_322),
    ("b7=1 dressed", 1.0, K322_dressed),
):
    c5A = richardson5(lambda g: mismatch(psi, g, b7=b7, k322=k322, schemeA=True), 0.04)
    pred = A5_min_pred - V7_psi7(psi) / 5040
    ok &= abs(c5A - pred) < 1e-4 * max(1, abs(pred))
    det.append(f"{tag}: mism/g^5 = {c5A:+.6f} (pred {pred:+.6f})")
# Sigma_3-sector on-shell value scales as g^6 (no O(g^5) contact possible)
def sig3_sector_value(g):
    s2, s3 = solve_saddle(psi, g, b7=1.0, k322=K322_dressed, schemeA=True)
    return (g**4 / 720) * (-(s3 @ V6M @ s3)) + (g**5 / 5040) * np.einsum(
        "KIJ,K,I,J->", K322_dressed, s3, s2, s2
    )


sv1, sv2 = sig3_sector_value(0.08), sig3_sector_value(0.04)
slope3 = math.log2(abs(sv1 / sv2))
ok &= abs(slope3 - 6) < 0.2
det.append(f"Sigma_3-sector value log-slope = {slope3:.3f} (= 6: no O(g^5) contact)")
report(
    5,
    "scheme-A-literal fails: V7-contact deficit survives for any (b7,kernel); A5_min corroborated",
    ok,
    "; ".join(det),
)

# ---------------------------------------------------------------- check 6
ok = True
det = []
# ghost saturation: V_n saturates 2n; N_gh(Sigma_k) = 2k
NG = lambda k: 2 * k
ok &= NG(3) + NG(3) + NG(1) == 14  # (3,3,1)
ok &= NG(3) + NG(2) + NG(2) == 14  # (3,2,2)
# other partitions of 7 into <=3 parts need Sigma_4+ : (4,2,1),(4,3),(5,2),(5,1,1),(6,1),(7)
# Sigma_4 kinetic = V8(S4,S4) at O(g^6) (saturation 16=8+8); an O(g^5) source
# gives Sigma_4* ~ g^{5-6} = g^{-1}: divergent perturbative branch — excluded
# (the R20 section-1 argument, one order up).
ok &= NG(4) + NG(4) == 16
ok &= 5 - 6 == -1  # source order minus kinetic order < 0
# contamination: any O(g^5) coupling with on-shell footprint n<7 hits an n-point
# amplitude at g^5 != g^{n-2}: partitions (3,2,1)->6, (2,2,2)->6, (3,3)->6, (2,2)->4...
for parts in ((3, 2, 1), (2, 2, 2), (3, 3), (2, 2)):
    n = sum(parts)
    ok &= 5 != n - 2
det.append("saturations 14=6+6+2=6+4+4; Sigma_4 divergent-branch excluded;")
det.append("all footprint-n<7 couplings contaminate (5 != n-2): menu = {(3,3,1),(3,2,2)}")
report(6, "power counting: O(g^5) menu is exactly {(3,3,1),(3,2,2)} [arithmetic bookkeeping of the counting, not an independent test -- critic C1]", ok, " ".join(det))

# ---------------------------------------------------------------- check 7
ok = True
det = []
g = 0.3
a7 = 1.0
k331 = K331_dressed
psi7 = rng.standard_normal(N)
dpsi = rng.standard_normal(N)  # finite direction; all derivatives analytic


def A331_psi(x):
    return np.einsum("KLe,e->KL", k331, x)


Mhat = M_tilde - (g / 7) * a7 * A331_psi(psi7)
Mhat_inv = np.linalg.inv(Mhat)
Gs = Gsrc_dressed(psi7)
dGs = Gsrc_dressed(dpsi)  # Gsrc is linear in psi
p7, p37 = pvec(psi7), p3vec(psi7)
dp = sym_coords2(np.outer(psi7, dpsi) + np.outer(dpsi, psi7))
dMhat = -(g / 7) * a7 * A331_psi(dpsi)

# Sigma_2-effective (after exact Sigma_3 elimination): value = <B,s2> + (1/2) s2 H s2
# B = (g^2/12) V4S p ;  H = -(g^2/12)V4S + (g^3/60)W + (g^4/360) Gs^T Mhat^{-1} Gs
Hhat = -(g**2 / 12) * V4S + (g**3 / 60) * Wpsi(psi7) + (g**4 / 360) * (Gs.T @ Mhat_inv @ Gs)
Bv = (g**2 / 12) * V4S @ p7
sig2_star = -np.linalg.solve(Hhat, Bv)
sig3_star = Mhat_inv @ (Gs @ sig2_star)
# saddle consistency
gr = grad_total(sig2_star, sig3_star, psi7, g, a7=a7, k331=k331)
ok &= np.abs(gr).max() < 1e-11
det.append(f"exact saddle |grad|={np.abs(gr).max():.1e}")

# off-shell point
sig2 = sig2_star + 0.3 * rng.standard_normal(DS2)
sig3 = sig3_star + 0.3 * rng.standard_normal(DS3)
Y2 = sig2 - sig2_star
Y3 = sig3 - Mhat_inv @ (Gs @ sig2)  # deviation from the CONDITIONAL Sigma_3 saddle

# variations
dHhat = (
    (g**3 / 60) * Wpsi(dpsi)
    + (g**4 / 360) * (dGs.T @ Mhat_inv @ Gs + Gs.T @ Mhat_inv @ dGs
                      - Gs.T @ Mhat_inv @ dMhat @ Mhat_inv @ Gs)
)
dBv = (g**2 / 12) * V4S @ dp
dY2 = -0.5 * np.linalg.solve(Hhat, dHhat @ Y2)
dY3 = -0.5 * np.linalg.solve(Mhat, dMhat @ Y3)
dsig2_star = -np.linalg.solve(Hhat, dBv + dHhat @ sig2_star)
dsig2 = dsig2_star + dY2
# conditional Sigma_3 saddle variation (full dsig2 + explicit psi-dependence)
dsig3_cond = Mhat_inv @ (-dMhat @ (Mhat_inv @ (Gs @ sig2)) + dGs @ sig2 + Gs @ dsig2)
dsig3 = dsig3_cond + dY3


def dpsi_S(s2, s3, x, dx):
    """Analytic directional derivative of S_total wrt explicit Psi (a7-leg only)."""
    dpv = sym_coords2(np.outer(x, dx) + np.outer(dx, x))
    out = (g**2 / 12) * s2 @ V4S @ dpv
    out += (g**3 / 120) * np.einsum("IJe,I,J,e->", V5S, s2, s2, dx)
    out += (g**4 / 360) * s3 @ (Gsrc_dressed(dx) @ s2)
    out += (g**5 / 5040) * a7 * np.einsum("KLe,K,L,e->", k331, s3, s3, dx)
    return out


lhs = (
    grad_total(sig2, sig3, psi7, g, a7=a7, k331=k331)[:DS2] @ dsig2
    + grad_total(sig2, sig3, psi7, g, a7=a7, k331=k331)[DS2:] @ dsig3
    + dpsi_S(sig2, sig3, psi7, dpsi)
)
rhs = dpsi_S(sig2_star, sig3_star, psi7, dpsi)  # envelope: = delta[S_eff^(7) + F6]
scale = max(abs(lhs), abs(rhs), 1e-3)
ok &= abs(lhs - rhs) < 1e-10 * scale
det.append(f"exact equality deltaS = delta[Seff7+F6]: |lhs-rhs|/scale = {abs(lhs - rhs) / scale:.1e}")

# falsification 1: delta Y3 = 0 leaves EXACTLY the predicted residual
lhs_noY3 = (
    grad_total(sig2, sig3, psi7, g, a7=a7, k331=k331)[:DS2] @ dsig2
    + grad_total(sig2, sig3, psi7, g, a7=a7, k331=k331)[DS2:] @ (dsig3_cond)
    + dpsi_S(sig2, sig3, psi7, dpsi)
)
resid_pred = -(g**4 / 720) * Y3 @ dMhat @ Y3  # = +(g^5/5040) a7 k331(Y3,Y3,dpsi)
ok &= abs((lhs_noY3 - rhs) - resid_pred) < 1e-10 * max(abs(resid_pred), 1e-6)
ok &= abs(resid_pred) > 1e-8  # the R21 delta Y3 = 0 law genuinely fails now
det.append(f"deltaY3=0 residual = {lhs_noY3 - rhs:+.3e} = pred {resid_pred:+.3e} (R21 law fails at O(g^5))")
# falsification 2: delta Y2 = 0 leaves the predicted residual too
lhs_noY2 = (
    grad_total(sig2, sig3, psi7, g, a7=a7, k331=k331)[:DS2] @ dsig2_star
    + grad_total(sig2, sig3, psi7, g, a7=a7, k331=k331)[DS2:]
    @ (Mhat_inv @ (-dMhat @ (Mhat_inv @ (Gs @ sig2)) + dGs @ sig2 + Gs @ dsig2_star) + dY3)
    + dpsi_S(sig2, sig3, psi7, dpsi)
)
resid2_pred = 0.5 * Y2 @ dHhat @ Y2
ok &= abs((lhs_noY2 - rhs) - resid2_pred) < 1e-10 * max(abs(resid2_pred), 1e-6)
ok &= abs(resid2_pred) > 1e-10  # critic M1: guard against a vacuously-passing leg
det.append(f"deltaY2=0 residual = {lhs_noY2 - rhs:+.3e} = pred {resid2_pred:+.3e}")
# genuine homogeneity test (critic M1): the law is linear in Y and nonzero on generic Y
dY3_1 = -0.5 * np.linalg.solve(Mhat, dMhat @ Y3)
dY3_2 = -0.5 * np.linalg.solve(Mhat, dMhat @ (2.0 * Y3))
ok &= np.abs(dY3_2 - 2.0 * dY3_1).max() < 1e-12 * max(np.abs(dY3_1).max(), 1e-12)
ok &= np.abs(dY3_1).max() > 1e-12
det.append(f"laws homogeneous: deltaY3(2Y) = 2 deltaY3(Y) at {np.abs(dY3_2 - 2.0 * dY3_1).max():.1e}, |deltaY3| = {np.abs(dY3_1).max():.2e}")
report(7, "gauge law at O(g^5): kernel-rotation laws, exact equality, R21 dY3=0 superseded", ok, "; ".join(det))

# ---------------------------------------------------------------- summary
print()
ntot = 8
print(
    f"{ntot - len(set(failures))}/{ntot} checks PASS"
    + (f"  FAILURES: {sorted(set(failures))}" if failures else "")
)
raise SystemExit(len(set(failures)))
