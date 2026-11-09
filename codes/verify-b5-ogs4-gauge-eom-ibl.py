#!/usr/bin/env python3
"""
verify-b5-ogs4-gauge-eom-ibl.py — machine checks for derivation 015 (B5):
gauge transformations, EOMs, and IBL_infty rewriting at O(g_s^4), for BOTH
Route-B presentations (P-dressed = Harold's Annotation; P-elementary = R20).

Extends verify-b4-sigma3.py (reuse the Sym^2 + Sym^3 basis machinery and the
generic V4/V5/V6 tensors) with:
  - the Phi-map construction of the dressed composite kinetic tilde_M and source
    tilde_u (section 2 of derivation 015);
  - the on-shell Veronese collapses tilde_M(p3,p3) = W6(psi^6) and tilde_u(P) =
    tilde_M p3 (checks 1-2);
  - the Sigma_3 gauge law delta Y_3 = 0, GENUINELY tested (check 3, rewritten
    after the 2026-07-08 blind critic pass [S1]: independent-route agreement of
    the analytic law vs central finite differences of the saddle map;
    Y_3-independence of the transported action variation; and a FALSIFICATION
    leg with an artificially Psi-dependent kernel, where saddle-tracking alone
    fails by the predicted amount and the R25-type kernel rotation
    delta Y_3 = -1/2 K3^{-1}(delta K3) Y_3 restores invariance);
  - the ON-SHELL saddle equality S(sigma*) - S_eff^(6) = F(Psi) for both
    presentations (check 4 — a PROXY: the exact OFF-SHELL equality
    delta S - delta S_eff^(6) = delta[F] is analytic, inherited from R19's
    hand-verified off-shell law; it is NOT independently machine-checked here);
  - saddle stationarity, O(eps^2) response (check 5 — a PROXY for the gauge
    homogeneity delta Y|_{Y=0} = 0, not the transformation statement itself);
  - the (4,1,0) combination [Q,l4] + [l2,l3] is NONZERO on generic data
    (check 6, dim-4 toy — the falsifiability leg ONLY; no symbolic imposition
    of the L_infty axioms is performed).

Finite-dimensional model, physical grading (all fields Grassmann-even), SAME
conventions as verify-b4-sigma3.py. CFT-level analytics of inverses = carve-out.

All checks PASS/FAIL; exit code = number of failures.
"""

import itertools
import math

import numpy as np

rng = np.random.default_rng(20260706)
np.set_printoptions(precision=6, suppress=True)

N = 3
DS2 = N * (N + 1) // 2
DS3 = N * (N + 1) * (N + 2) // 6
TOL = 1e-9
TOL_G = 1e-9  # gauge-law finite-difference tolerance (analytic identities)

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

# orthonormal Sym^2 basis
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

V4S = np.einsum("abcd,Iab,Jcd->IJ", V4, Lam2, Lam2)
V5S = np.einsum("abcde,Iab,Jcd->IJe", V5, Lam2, Lam2)
V4inv = np.linalg.inv(V4S)

# orthonormal Sym^3 basis
Lam3 = []
for a in range(N):
    for b in range(a, N):
        for c in range(b, N):
            M = np.zeros((N, N, N))
            for perm in itertools.permutations((a, b, c)):
                M[perm] += 1.0
            M /= np.linalg.norm(M)
            Lam3.append(M)
Lam3 = np.array(Lam3)

V6M = np.einsum("abcdef,Iabc,Jdef->IJ", V6, Lam3, Lam3)  # bare Sigma_3 kinetic


def sym_coords2(Mmat):
    return np.einsum("Iab,ab->I", Lam2, (Mmat + Mmat.T) / 2)


def pvec(psi):
    return sym_coords2(np.outer(psi, psi))


def p3vec(psi):
    return np.einsum("Iabc,a,b,c->I", Lam3, psi, psi, psi)


def source3(sig2, psi):
    Sig2mat = np.einsum("I,Iab->ab", sig2, Lam2)
    return np.einsum("abcdef,Kabc,de,f->K", V6, Lam3, Sig2mat, psi)


def V6_psi6(psi):
    return np.einsum("abcdef,a,b,c,d,e,f->", V6, *([psi] * 6))


def vvec(psi):
    p = pvec(psi)
    return np.einsum("IJe,J,e->I", V5S, p, psi)


def vvec_sig2(sig2, psi):
    """Sigma_2-dependent extension: v(Sigma_2)_I = V5(Lambda^2_I, Sigma_2, Psi)."""
    return np.einsum("IJe,J,e->I", V5S, sig2, psi)


def Kmat(psi, g):
    return V4S - (g / 5.0) * np.einsum("IJe,e->IJ", V5S, psi)


# ---- the Phi-map and the dressed composite objects (section 2 of deriv 015) ----
# Phi: Sym^3 -> (Sym^2)^*,  Phi(X)_I = V5(Lambda^2_I, X).
# In bases: Phi_{IK} = V5(Lambda^2_I, Lambda^3_K) (V5 with 2 slots on Lambda^2,
# 3 slots on Lambda^3).
Phi = np.einsum("abcd,abc,Kdef->IK", V5, *[None] * 0, Lam3) if False else None
# compute Phi_{IK} = sum V5 * Lam2_I(2 slots) * Lam3_K(3 slots). V5 has 5 slots;
# contract slots (0,1) with Lam2_I and (2,3,4) with Lam3_K. By total symmetry of V5
# the slot choice is immaterial.
Phi = np.einsum("abcde,Iab,Kcde->IK", V5, Lam2, Lam3)

# N = Phi^T V4^{-1} Phi  (composite bilinear on Sym^3)
Nmat = Phi.T @ V4inv @ Phi
# dressed kinetic and source
M_tilde = V6M - (6.0 / 5.0) * Nmat
M_tilde_inv = np.linalg.inv(M_tilde)


def source3_tilde(sig2, psi):
    """Dressed source: tilde_u = u - (6/5) Phi^T V4^{-1} v(Sigma_2)."""
    u = source3(sig2, psi)
    v_s2 = vvec_sig2(sig2, psi)
    return u - (6.0 / 5.0) * (Phi.T @ (V4inv @ v_s2))


# ---------------------------------------------------------------- check 1
# Lemma 2.1: Phi(psi^{ox3}) = v  (the Veronese collapse of Phi)
ok = True
det = []
psi0 = rng.standard_normal(N)
p3_0 = p3vec(psi0)
Phi_p3 = Phi @ p3_0
v0 = vvec(psi0)
ok &= np.allclose(Phi_p3, v0, atol=TOL)
det.append(f"Phi(p3) - v = {np.abs(Phi_p3 - v0).max():.1e}")
# N symmetric
ok &= np.allclose(Nmat, Nmat.T, atol=TOL)
det.append("N = Phi^T V4inv Phi symmetric")
# N(p3,p3) = v V4^{-1} v
Ndiag = p3_0 @ Nmat @ p3_0
vViv = v0 @ V4inv @ v0
ok &= abs(Ndiag - vViv) < TOL * max(1, abs(vViv))
det.append(f"N(p3,p3)={Ndiag:+.6f} = vV4inv v={vViv:+.6f}")
report(
    1,
    "Lemma 2.1: Phi-Veronese collapse + N symmetric + N(p3,p3)=vV4inv v",
    ok,
    "; ".join(det),
)

# ---------------------------------------------------------------- check 2
# Dressed kinetic on Veronese: tilde_M(p3,p3) = W6(psi^6) = V6(psi^6) - 6/5 vV4inv v
# Dressed source Veronese collapse: tilde_u(P) = tilde_M p3
ok = True
det = []
p0 = pvec(psi0)
W6diag = V6_psi6(psi0) - (6.0 / 5.0) * vViv
Mtilde_diag = p3_0 @ M_tilde @ p3_0
ok &= abs(Mtilde_diag - W6diag) < TOL * max(1, abs(W6diag))
det.append(f"tilde_M(p3,p3)={Mtilde_diag:+.6f} = W6={W6diag:+.6f}")
# source collapse
utilde_P = source3_tilde(p0, psi0)
Mtilde_p3 = M_tilde @ p3_0
ok &= np.allclose(utilde_P, Mtilde_p3, atol=TOL)
det.append(f"tilde_u(P) - tilde_M p3 = {np.abs(utilde_P - Mtilde_p3).max():.1e}")
# tilde_M Psi-independence is STRUCTURAL (Phi, Nmat, M_tilde are built from
# V4, V5, V6 and the fixed bases only; no psi appears in their construction).
# Recorded as a by-construction fact, NOT a numerical test [critic M3].
det.append("tilde_M Psi-independent (structural: no psi in construction; not a test)")
report(
    2, "dressed Veronese: tilde_M(p3,p3)=W6, tilde_u(P)=tilde_M p3", ok, "; ".join(det)
)


# ---------------------------------------------------------------- action pieces
def S_HS_part(sig2, psi, g):
    """S_HS + O(g^3) V5 term, minus shared V2,V3 (as in verify-b4)."""
    p = pvec(psi)
    return (
        -(g**2 / 24) * sig2 @ V4S @ sig2
        + (g**2 / 12) * sig2 @ V4S @ p
        + (g**3 / 120) * np.einsum("IJe,I,J,e->", V5S, sig2, sig2, psi)
    )


def Seff6_minus_shared(psi, g):
    p = pvec(psi)
    return (
        (g**2 / 24) * p @ V4S @ p
        + (g**3 / 120) * np.einsum("IJe,I,J,e->", V5S, p, p, psi)
        + (g**4 / 720) * V6_psi6(psi)
    )


def S_sig3_gauss(sig3, sig2, psi, g, a, b, dressed):
    K3 = M_tilde if dressed else V6M
    s = source3_tilde(sig2, psi) if dressed else source3(sig2, psi)
    return (g**4 / 720) * (-a * sig3 @ K3 @ sig3 + b * sig3 @ s)


def sig3_saddle(sig2, psi, a, b, dressed):
    K3 = M_tilde if dressed else V6M
    s = source3_tilde(sig2, psi) if dressed else source3(sig2, psi)
    return (b / (2 * a)) * np.linalg.solve(K3, s)


def grad_hess_sig2(sig2, psi, g, a, b, dressed):
    """Gradient/Hessian of S wrt Sigma_2 with Sigma_3 eliminated (Gaussian)."""
    p = pvec(psi)
    K3 = M_tilde if dressed else V6M
    K3inv = M_tilde_inv if dressed else np.linalg.inv(V6M)
    coeff = (b**2 / (4 * a)) * (g**4 / 720)
    # source s(Sigma_2) is LINEAR in Sigma_2: s_K = sum_I Gsrc[K,I] Sigma_2_I,
    # with Gsrc the map Sigma_2 -> source (shape DS3 x DS2).
    # bare:  Gsrc_bare[K,I] = V6(Lam3_K, Lam2_I, Psi)
    G_bare_IK = np.einsum("abcdef,Kabc,Ide,f->IK", V6, Lam3, Lam2, psi)  # (DS2,DS3)
    Gsrc_bare = G_bare_IK.T  # (DS3, DS2): source = Gsrc_bare @ sig2
    # dressed source correction: -6/5 Phi^T V4inv v(Sigma_2), v(Sigma_2)_L = V5S[L,J,e] Sig2_J Psi_e
    # => map Sigma_2 -> v is Jv[L,J] = V5S[L,J,e] Psi_e (DS2 x DS2); correction map = Phi^T V4inv Jv (DS3 x DS2)
    Jv = np.einsum("MJe,e->MJ", V5S, psi)  # (DS2, DS2)
    Gsrc_dress = Gsrc_bare - (6.0 / 5.0) * (Phi.T @ V4inv @ Jv)  # (DS3, DS2)
    Gsrc = Gsrc_dress if dressed else Gsrc_bare
    Dmat = Gsrc.T @ K3inv @ Gsrc  # (DS2, DS2): E = sig2^T Dmat sig2
    grad = (
        -(g**2 / 12) * V4S @ sig2
        + (g**2 / 12) * V4S @ p
        + (g**3 / 60) * np.einsum("IJe,J,e->I", V5S, sig2, psi)
        + 2 * coeff * (Dmat @ sig2)
    )
    hess = (
        -(g**2 / 12) * V4S
        + (g**3 / 60) * np.einsum("IJe,e->IJ", V5S, psi)
        + 2 * coeff * Dmat
    )
    return grad, hess


def solve_sig2_saddle(psi, g, a, b, dressed):
    sig2 = pvec(psi).copy()
    for gcur in np.linspace(0.0, g, 2 + int(g / 0.02))[1:]:
        for _ in range(80):
            grad, hess = grad_hess_sig2(sig2, psi, gcur, a, b, dressed)
            sig2 = sig2 - np.linalg.solve(hess, grad)
            if np.abs(grad).max() < 1e-14:
                break
    gnorm = np.abs(grad_hess_sig2(sig2, psi, g, a, b, dressed)[0]).max()
    assert gnorm < 1e-10, f"sig2 saddle: |grad|={gnorm:.1e}"
    return sig2


def onshell_minus_shared(psi, g, a, b, dressed):
    sig2 = solve_sig2_saddle(psi, g, a, b, dressed)
    sig3 = sig3_saddle(sig2, psi, a, b, dressed)
    return S_HS_part(sig2, psi, g) + S_sig3_gauss(sig3, sig2, psi, g, a, b, dressed)


# ---------------------------------------------------------------- check 3
# Sigma_3 gauge law: delta Y_3 = 0 — GENUINE test.
# REWRITTEN after the 2026-07-08 blind critic pass [finding S1]: the original
# check DEFINED dsig3 by solving the linear condition and then re-evaluated the
# same condition — tautological (0 = 0 by construction, never referencing
# Sigma_3). Now three independent legs, per presentation:
#   (a) INDEPENDENT-ROUTE agreement: the analytic law
#       delta Sigma_3^* = (b/2a) K3^{-1} [ds/dPsi dpsi + ds/dSigma_2 dsig2]
#       must equal the central finite difference of the saddle map
#       Sigma_3^*(Psi ± eps dpsi, Sigma_2 ± eps dsig2), computed only from the
#       source functions (never from the analytic derivative formulas).
#   (b) Y_3-INDEPENDENCE of the transported action variation: transport the
#       fields with the saddle-tracking-only law (delta Y_3 = 0) and central-
#       difference the Sigma_3-sector action at two different random Y_3.
#       The two variations must AGREE — this holds iff delta Y_3 = 0 is the
#       right law, and it fails when the kernel is Psi-dependent (leg c).
#   (c) FALSIFICATION leg (dressed only): perturb the kernel to a Psi-DEPENDENT
#       K3(Psi) = K3 + lam W(.,.,Psi) (mimicking the O(g^5) tilde_V7 dressing,
#       cf. 018 §7). Saddle-tracking alone now FAILS leg (b) by exactly the
#       predicted amount -a(g^4/720)[Y3a.dK3.Y3a - Y3b.dK3.Y3b], and the
#       R25-type kernel rotation delta Y_3 = -1/2 K3^{-1}(delta K3) Y_3
#       RESTORES Y_3-independence. The check therefore distinguishes
#       Psi-independent kernels (rotation = 0) from Psi-dependent ones.
ok = True
det = []
psi = rng.standard_normal(N)
sig2 = pvec(psi) + 0.1 * rng.standard_normal(DS2)
dpsi = 0.05 * rng.standard_normal(N)
g = 0.3
a, b = 1.0, 2.0
PREF = g**4 / 720.0
EPS3 = 1e-4
TOL_FD = 1e-10


def saddle_map(sig2_, psi_, dressed):
    """Sigma_3^* from the source functions only (route independent of the
    analytic derivative formulas used in the law)."""
    K3 = M_tilde if dressed else V6M
    s = (source3_tilde if dressed else source3)(sig2_, psi_)
    return (b / (2 * a)) * np.linalg.solve(K3, s)


# delta Sigma_2 from the composite law (stand-in): delta(Psi^2) = dpsi psi + psi dpsi
dP = np.outer(psi, dpsi) + np.outer(dpsi, psi)
dsig2 = sym_coords2(dP)

for dressed in (True, False):
    tag = "dressed" if dressed else "elementary"
    K3 = M_tilde if dressed else V6M
    # analytic law: dsig3 = (b/2a) K3^{-1} (ds/dPsi dpsi + ds/dSigma_2 dsig2)
    Sig2mat = np.einsum("I,Iab->ab", sig2, Lam2)
    du_dpsi = np.einsum("abcdef,Kabc,de->Kf", V6, Lam3, Sig2mat)  # (DS3, N)
    dv_dpsi = np.einsum("MJf,J->Mf", V5S, sig2)  # (DS2, N)
    ds_dpsi = du_dpsi - (6.0 / 5.0) * (Phi.T @ V4inv @ dv_dpsi) if dressed else du_dpsi
    G_bare_IK = np.einsum("abcdef,Kabc,Ide,f->IK", V6, Lam3, Lam2, psi)  # (DS2, DS3)
    Gsrc_bare = G_bare_IK.T  # (DS3, DS2)
    Jv = np.einsum("MJe,e->MJ", V5S, psi)  # (DS2, DS2)
    Gsrc = (Gsrc_bare - (6.0 / 5.0) * (Phi.T @ V4inv @ Jv)) if dressed else Gsrc_bare
    dsig3_analytic = (b / (2 * a)) * np.linalg.solve(K3, ds_dpsi @ dpsi + Gsrc @ dsig2)
    # --- leg (a): central finite difference of the saddle map (independent route)
    dsig3_fd = (
        saddle_map(sig2 + EPS3 * dsig2, psi + EPS3 * dpsi, dressed)
        - saddle_map(sig2 - EPS3 * dsig2, psi - EPS3 * dpsi, dressed)
    ) / (2 * EPS3)
    lega = np.abs(dsig3_analytic - dsig3_fd).max()
    ok &= lega < 1e-8
    det.append(f"{tag}(a): |analytic - FD saddle-tracking| = {lega:.1e}")
    # --- leg (b): Y_3-independence of the transported action variation
    sig3_star = saddle_map(sig2, psi, dressed)
    Y3a = rng.standard_normal(DS3)
    Y3b = rng.standard_normal(DS3)

    def var_S3(sig3_, dsig3_, dressed_):
        Sp = S_sig3_gauss(
            sig3_ + EPS3 * dsig3_, sig2 + EPS3 * dsig2, psi + EPS3 * dpsi,
            g, a, b, dressed_,
        )
        Sm = S_sig3_gauss(
            sig3_ - EPS3 * dsig3_, sig2 - EPS3 * dsig2, psi - EPS3 * dpsi,
            g, a, b, dressed_,
        )
        return (Sp - Sm) / (2 * EPS3)

    var_a = var_S3(sig3_star + Y3a, dsig3_analytic, dressed)
    var_b = var_S3(sig3_star + Y3b, dsig3_analytic, dressed)
    legb = abs(var_a - var_b)
    ok &= legb < TOL_FD
    det.append(f"{tag}(b): |var(Y3a) - var(Y3b)| = {legb:.1e}")

# --- leg (c): falsification with a Psi-DEPENDENT kernel (dressed base)
lam = 0.1
W3 = rng.standard_normal((DS3, DS3, N))
W3 = (W3 + np.transpose(W3, (1, 0, 2))) / 2  # symmetric in the two Sym^3 slots


def K3p(psi_):
    return M_tilde + lam * np.einsum("KLf,f->KL", W3, psi_)


def saddle_map_p(sig2_, psi_):
    return (b / (2 * a)) * np.linalg.solve(K3p(psi_), source3_tilde(sig2_, psi_))


def S3_gauss_p(sig3_, sig2_, psi_):
    s = source3_tilde(sig2_, psi_)
    return PREF * (-a * sig3_ @ K3p(psi_) @ sig3_ + b * sig3_ @ s)


def var_S3p(sig3_, dsig3_):
    Sp = S3_gauss_p(sig3_ + EPS3 * dsig3_, sig2 + EPS3 * dsig2, psi + EPS3 * dpsi)
    Sm = S3_gauss_p(sig3_ - EPS3 * dsig3_, sig2 - EPS3 * dsig2, psi - EPS3 * dpsi)
    return (Sp - Sm) / (2 * EPS3)


sig3_star_p = saddle_map_p(sig2, psi)
Y3a = rng.standard_normal(DS3)
Y3b = rng.standard_normal(DS3)
# saddle-tracking-only transport (delta Y_3 = 0), FD route
dsig3_track = (
    saddle_map_p(sig2 + EPS3 * dsig2, psi + EPS3 * dpsi)
    - saddle_map_p(sig2 - EPS3 * dsig2, psi - EPS3 * dpsi)
) / (2 * EPS3)
var_a = var_S3p(sig3_star_p + Y3a, dsig3_track)
var_b = var_S3p(sig3_star_p + Y3b, dsig3_track)
dK3 = lam * np.einsum("KLf,f->KL", W3, dpsi)
resid_pred = -a * PREF * (Y3a @ dK3 @ Y3a - Y3b @ dK3 @ Y3b)
mismatch = var_a - var_b
falsified = abs(mismatch) > 1e-9 and abs(mismatch - resid_pred) < 1e-8 * max(
    1, abs(resid_pred)
)
ok &= falsified
det.append(
    f"falsification: Psi-dep kernel breaks tracking-only law, "
    f"mismatch {mismatch:.3e} = predicted {resid_pred:.3e}"
)
# kernel rotation restores Y_3-independence
Kp_inv_now = np.linalg.inv(K3p(psi))
rot_a = -0.5 * Kp_inv_now @ dK3 @ Y3a
rot_b = -0.5 * Kp_inv_now @ dK3 @ Y3b
var_a_rot = var_S3p(sig3_star_p + Y3a, dsig3_track + rot_a)
var_b_rot = var_S3p(sig3_star_p + Y3b, dsig3_track + rot_b)
restored = abs(var_a_rot - var_b_rot)
ok &= restored < TOL_FD
det.append(f"rotation -K3^-1(dK3)Y3/2 restores: |var_a - var_b| = {restored:.1e}")
report(
    3,
    "Sigma_3 gauge law delta Y_3 = 0: independent-route + Y_3-independence + falsification",
    ok,
    "; ".join(det),
)

# ---------------------------------------------------------------- check 4
# ON-SHELL saddle equality S(sigma*) - S_eff^(6) = F(Psi) — a PROXY [critic S2]:
# the exact OFF-SHELL equality delta S - delta S_eff^(6) = delta[F] asserted in
# 015 §4.2 is ANALYTIC (inherited from R19's hand-verified off-shell law with
# the Sigma_3-exchange folded in, which is quadratic in Y_2); this check tests
# only its on-shell value, which is automatic once the saddle is solved. What
# it DOES test non-trivially: the O(g^4) coefficient of F. For the DRESSED
# presentation F = O(g^5) (closes); for ELEMENTARY F = (g^4/600) vV4inv v + ...
# (R20 residual). Richardson-extrapolate the O(g^4) coefficient.
ok = True
det = []


def quad_richardson(rfun, gs):
    r1, r2, r3 = (rfun(g) for g in gs)
    return (r1 - 6 * r2 + 8 * r3) / 3.0


psi = rng.standard_normal(N)
v = vvec(psi)
vViv = v @ V4inv @ v
V6d = V6_psi6(psi)


# dressed: on-shell mismatch / g^4 -> 0 (closes at O(g^4); residual is O(g^5))
def mism_dr(g):
    return (
        onshell_minus_shared(psi, g, 1.0, 2.0, True) - Seff6_minus_shared(psi, g)
    ) / g**4


extr_dr = quad_richardson(mism_dr, (0.04, 0.02, 0.01))
ok &= abs(extr_dr) < 5e-3
det.append(f"dressed: mism/g^4 -> {extr_dr:+.6f} (closes, =O(g^5))")


# elementary: on-shell mismatch / g^4 -> (1/600) vV4inv v (R20, with c6=0,a=1,b=2)
def mism_el(g):
    return (
        onshell_minus_shared(psi, g, 1.0, 2.0, False) - Seff6_minus_shared(psi, g)
    ) / g**4


extr_el = quad_richardson(mism_el, (0.04, 0.02, 0.01))
target_el = vViv / 600 + (0 + 4 / 4 - 1) * V6d / 720  # c6=0, b^2/4a=1
ok &= abs(extr_el - target_el) < 5e-3 * max(1, abs(target_el))
det.append(f"elementary: mism/g^4 -> {extr_el:+.6f} = {target_el:+.6f} (R20 residual)")
report(
    4,
    "on-shell saddle equality (proxy for the analytic off-shell law): dressed closes (O(g^5)), elementary = R20 residual",
    ok,
    "; ".join(det),
)

# ---------------------------------------------------------------- check 5
# SADDLE STATIONARITY — a PROXY for the gauge homogeneity delta Y|_{Y=0} = 0
# [critic S2]: what is executed is that the joint saddle is a stationary point
# of S wrt (Sigma_2, Sigma_3) (O(eps^2) response to a perturbation off the
# saddle), NOT the gauge-transformation statement delta Y|_{Y=0} = 0 itself.
# The gauge-homogeneity statement is analytic (the delta Y_2 law of 015 §4.2 is
# linear-homogeneous in Y_2 by construction; delta Y_3 = 0 is check 3's leg b).
# Stationarity is the ingredient that makes saddle-tracking consistent.
ok = True
det = []
g = 0.2
sig2star = solve_sig2_saddle(psi, g, 1.0, 2.0, True)
sig3star = sig3_saddle(sig2star, psi, 1.0, 2.0, True)
Sstar = S_HS_part(sig2star, psi, g) + S_sig3_gauss(
    sig3star, sig2star, psi, g, 1.0, 2.0, True
)
eps = 1e-5
# perturb Sigma_2: response should be O(eps^2) (stationary => homogeneity)
sig2p = sig2star + eps * rng.standard_normal(DS2)
sig3p_saddle = sig3_saddle(sig2p, psi, 1.0, 2.0, True)
Sp = S_HS_part(sig2p, psi, g) + S_sig3_gauss(
    sig3p_saddle, sig2p, psi, g, 1.0, 2.0, True
)
resp2 = abs(Sp - Sstar) / eps
# perturb Sigma_3 off its saddle: response also O(eps^2) (Gaussian stationary)
sig3p = sig3star + eps * rng.standard_normal(DS3)
S3p = S_HS_part(sig2star, psi, g) + S_sig3_gauss(
    sig3p, sig2star, psi, g, 1.0, 2.0, True
)
resp3 = abs(S3p - Sstar) / eps
ok &= resp2 < 1e-3 and resp3 < 1e-3
det.append(
    f"|dS/dSigma_2|~{resp2:.1e} (O(eps^2)), |dS/dSigma_3|~{resp3:.1e} (O(eps^2))"
)
det.append("=> saddle stationary (proxy; delta Y|_{Y=0}=0 itself is analytic)")
report(
    5,
    "saddle stationarity (proxy for homogeneity delta Y|_{Y=0} = 0)",
    ok,
    "; ".join(det),
)

# ---------------------------------------------------------------- check 6
# (4,1,0) combination [Q, l4] + [l2, l3]: NONZERO on generic data — the
# falsifiability leg ONLY [critic S2]. This shows the relation is not an
# algebraic identity (it constrains the maps), supporting "L_infty-required".
# NOT executed here: the converse leg (impose the L_infty axioms and verify
# the combination vanishes) — that direction rests on the analytic argument
# of 015 §5.2 (the (4,1,0) relation IS the L_infty Jacobi axiom through l4).
# Toy is dim-4 (NOT dim-16; the docstring/§5.4 prose previously misstated
# both the dimension and the symbolic-imposition leg). This mirrors
# the R16 METHOD NOTE: generic data first; relations imposed symbolically only
# if the generic test fails. (Full lemma proof of (3,2,0),(4,2,0) = flagged
# follow-up; here we probe the (k,1,0) L_infty-requirement, the backbone of the
# IBL verdict of section 5.)
#
# Toy: dim 4, Z2-graded (indices 0,1 odd; 2,3 even). Q odd, Q^2=0, contractible.
# l2 (2 in -> 1 out), l3 (3 in -> 1 out), l4 (4 in -> 1 out) = GENERIC random
# maps (graded-symmetric in inputs). Compute the (4,1,0) combination
#   R_{4,1,0}(x1,x2,x3,x4) = Q(l4(x1,x2,x3,x4)) + sum_i l4(..,Q xi,..)
#                            + l2(l3(x1,x2,x3),x4) + permutations   (schematic)
# and confirm |R| > 0 on generic data. (Graded signs suppressed in this probe —
# the nonzero magnitude is the falsifiable signal; a full Koszul treatment would
# only change signs, not the generic-nonzero verdict, cf. R16's degenerate-toy
# warning which is why we use generic random maps not Q-compatible ones.)
Nt = 4
PAR_t = np.array([1, 1, 0, 0])  # 0,1 odd; 2,3 even
Qt = np.zeros((Nt, Nt))
Qt[2, 0] = 1.0
Qt[3, 1] = 1.0  # Q: odd -> even (ghost +1)
ok_q2 = np.allclose(Qt @ Qt, 0)


def gsym_in(T, rank):
    """Graded-symmetrize T in its first `rank` (input) axes (last axis = output)."""
    S = np.zeros_like(T)
    for perm in itertools.permutations(range(rank)):
        sign = 1.0
        for i in range(rank):
            for j in range(i + 1, rank):
                if perm[i] > perm[j] and PAR_t[perm[i]] and PAR_t[perm[j]]:
                    sign = -sign
        idx = list(perm) + [rank]
        S += sign * np.transpose(T, idx)
    return S / math.factorial(rank)


# generic random maps (no L_infty constraints)
L2 = gsym_in(rng.standard_normal((Nt, Nt, Nt)), 2)  # (out, in1, in2)
L3 = gsym_in(rng.standard_normal((Nt, Nt, Nt, Nt)), 3)
L4 = gsym_in(rng.standard_normal((Nt, Nt, Nt, Nt, Nt)), 4)

# (4,1,0) combination [Q, l4] + [l2, l3], schematic (un-graded sum; the point is
# generic-nonzero). L4 has shape (out, in1, in2, in3, in4).
# [Q,l4]: Q on output + Q on each of the 4 inputs.
Ql4_out = np.einsum("ab,bcdef->acdef", Qt, L4)  # Q on output index
Ql4_in = np.zeros_like(L4)
for i in range(4):  # Q on input i
    perm = list(range(5))
    perm[0], perm[i + 1] = perm[i + 1], perm[0]  # swap output and input-i axes
    L4p = np.transpose(L4, perm)
    Qc = np.einsum("ab,bcdef->acdef", Qt, L4p)  # Q acts on the (now-first) input axis
    Ql4_in += np.transpose(Qc, perm)

# [l2,l3]: l2(l3(triple), remaining) summed over the 4 choices of the triple
l2_l3 = np.zeros_like(L4)
for i in range(Nt):
    for j in range(Nt):
        for k in range(Nt):
            for l in range(Nt):
                for o in range(Nt):
                    # 4 ways to pick 3 of {i,j,k,l} for l3, the 4th for l2
                    for a, b, c, d in [
                        (i, j, k, l),
                        (i, j, l, k),
                        (i, k, l, j),
                        (j, k, l, i),
                    ]:
                        for oo3 in range(Nt):
                            l2_l3[o, i, j, k, l] += L3[oo3, a, b, c] * L2[o, oo3, d]

rel41 = Ql4_out + Ql4_in + l2_l3
nonzero_generic = np.abs(rel41).max() > 1e-3
ok = ok_q2 and nonzero_generic
det6 = [
    f"Q^2=0 ({ok_q2})",
    f"|R_(4,1,0)|_generic = {np.abs(rel41).max():.2f} > 0 => L_infty-required (not agnostic)",
]
report(
    6,
    "(4,1,0) [Q,l4]+[l2,l3] nonzero on generic data (falsifiability leg only, dim-4 toy)",
    ok,
    "; ".join(det6),
)

# ---------------------------------------------------------------- summary
print()
n = 6
print(
    f"{n - len(set(failures))}/{n} checks PASS"
    + (f"  FAILURES: {sorted(set(failures))}" if failures else "")
)
raise SystemExit(len(set(failures)))
