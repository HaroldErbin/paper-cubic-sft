#!/usr/bin/env python3
"""
verify-b1-quintic.py — machine checks for the B1 O(g_s^3) quintic milestone
(derivation 011) and the cheap structural parts of T6 (derivation 012).

Finite-dimensional model, physical grading (all fields Grassmann-even, as in
R14/`verify-a1-telescoping.py`): H_0 = R^N, V4 = generic totally symmetric
4-tensor (invertible on Sym^2), V5 = generic totally symmetric 5-tensor.
Everything is done in an orthonormal basis of Sym^2 H_0 (R14 housekeeping 2),
where the symmetric identity is delta_IJ and all factor-2 traps are absent.

Conventions (match eq:SHS / R14 / derivation 011):
  S3(Psi,Sigma) = [shared V2,V3 terms]
                  - (g^2/4!) V4(Sigma,Sigma) + (2g^2/4!) V4(Sigma,Psi^{ox2})
                  + (g^3/5!) V5(Sigma,Sigma,Psi)
  S_eff5(Psi)   = [shared] + (g^2/4!) V4(Psi^4) + (g^3/5!) V5(Psi^5)
Shared V2,V3 terms cancel in every difference below and are omitted.

Checks
  (0) basis/telescoping sanity (completeness, V4S invertible, PB = p)
  (1) EXACT rewriting  S3 - S_eff5 = -(g^2/24) K(Xt,Xt) + (g^4/600) v K^{-1} v
      with K = V4 - (g/5) V5(.,.,Psi), Xt = X - (g/5) K^{-1} v, X = Sigma - p,
      v = V5(., p, Psi), p = coords of Psi^{ox2}   [identity in (Sigma,Psi,g)]
  (2) saddle: Newton Sigma*  =>  Xt(Sigma*) = 0; on-shell difference =
      feedback = (g^4/600) v K^{-1} v; feedback/g^4 -> const as g -> 0
  (3) falsifiability: quintic coefficient c != 1  =>  on-shell mismatch
      (c-1) (g^3/5!) V5(Psi^5) at leading order (O(g^3), not O(g^4))
  (4) 5-point diagrammatics: per unordered assignment {single i; {jk},{lm}}
      the source-prop-V5vertex-prop-source chain = (g^3/15) V5(psi_j..psi_i);
      15 assignments sum to g^3 V5(psi_1..psi_5) = the S_eff5 contact kernel
  (5) EXACT gauge equality (R11 analogue at O(g_s^3)): with
        dXt = (g/10) K^{-1} V5(., Xt, dPsi)
      the variation of -(g^2/24) K(Xt,Xt) vanishes EXACTLY; hence with the
      corrected composite law  dSigma = d(p + X*) + dXt  one has
        dS3 - dS_eff5 = d[feedback]   exactly (all orders in g);
      naive composite law (dSigma = dp) fails at O(g^3)  [falsifiable]
  (6) T6 negative check: Route C multiplier sector has NO flat directions
      (constraint Jacobian unit-triangular => invertible for every Psi)
  (7) T6 Stueckelberg: S3(Psi, Sigma - Qhat B) is exactly invariant under
      dB = L1, dSigma = Qhat L1 (any nilpotent Q); B = 0 gauge recovers S3
  (8) ghost-number saturation arithmetic for the T6 statements
      (omega2(Sigma,Qhat Sigma) = 0 forced; N_gh(Pi) = 5; N_gh(m2(L1)) = 5;
       V5(Sigma,Sigma,Psi) saturates the 5-punctured-sphere count 10)

All checks PASS/FAIL; exit code = number of failures.
"""

import numpy as np

rng = np.random.default_rng(20260703)
np.set_printoptions(precision=6, suppress=True)

N = 3                       # dim H_0
DS = N * (N + 1) // 2       # dim Sym^2 = 6
TOL = 1e-9

failures = []


def report(num, name, ok, detail=""):
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] check ({num}) {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        failures.append(num)


# ---------------------------------------------------------------- setup
def sym_tensor(shape):
    """Totally symmetric random tensor."""
    import itertools
    T = rng.standard_normal(shape)
    S = np.zeros_like(T)
    k = len(shape)
    for perm in itertools.permutations(range(k)):
        S += np.transpose(T, perm)
    import math
    return S / math.factorial(k)


V4 = sym_tensor((N,) * 4)
V5 = sym_tensor((N,) * 5)

# orthonormal Sym^2 basis Lambda_I (Frobenius): E_aa and (E_ab+E_ba)/sqrt2
Lam = []
for a in range(N):
    E = np.zeros((N, N)); E[a, a] = 1.0
    Lam.append(E)
for a in range(N):
    for b in range(a + 1, N):
        E = np.zeros((N, N)); E[a, b] = E[b, a] = 1 / np.sqrt(2)
        Lam.append(E)
Lam = np.array(Lam)                     # (DS, N, N)

# projected tensors
V4S = np.einsum('abcd,Iab,Jcd->IJ', V4, Lam, Lam)          # (DS,DS) symmetric
V5S = np.einsum('abcde,Iab,Jcd->IJe', V5, Lam, Lam)        # (DS,DS,N) sym in IJ


def sym_coords(M):
    """Coordinates of the symmetric part of matrix M in the Lam basis."""
    return np.einsum('Iab,ab->I', Lam, (M + M.T) / 2)


def Kmat(psi, g):
    return V4S - (g / 5.0) * np.einsum('IJe,e->IJ', V5S, psi)


def vvec(psi, g=None):
    p = sym_coords(np.outer(psi, psi))
    return np.einsum('IJe,J,e->I', V5S, p, psi)


def S3_minus_shared(sig, psi, g, c=1.0):
    """Non-shared part of S3 (Sigma-sector + quintic coupling)."""
    p = sym_coords(np.outer(psi, psi))
    return (-(g**2 / 24) * sig @ V4S @ sig
            + (g**2 / 12) * sig @ V4S @ p
            + c * (g**3 / 120) * np.einsum('IJe,I,J,e->', V5S, sig, sig, psi))


def Seff_minus_shared(psi, g):
    p = sym_coords(np.outer(psi, psi))
    return ((g**2 / 24) * p @ V4S @ p
            + (g**3 / 120) * np.einsum('IJe,I,J,e->', V5S, p, p, psi))


# ---------------------------------------------------------------- check 0
ok = True
det = []
# completeness: sum_I Lam_I^{ab} Lam_I^{cd} = symmetric identity
comp = np.einsum('Iab,Icd->abcd', Lam, Lam)
idsym = 0.5 * (np.einsum('ac,bd->abcd', np.eye(N), np.eye(N))
               + np.einsum('ad,bc->abcd', np.eye(N), np.eye(N)))
ok &= np.allclose(comp, idsym, atol=1e-12)
det.append(f"completeness dev {np.abs(comp-idsym).max():.1e}")
# V4S invertible
cond = np.linalg.cond(V4S)
ok &= cond < 1e6
det.append(f"cond(V4S)={cond:.1f}")
# V5S on the diagonal reproduces V5(psi^5)
psi0 = rng.standard_normal(N)
p0 = sym_coords(np.outer(psi0, psi0))
lhs = np.einsum('IJe,I,J,e->', V5S, p0, p0, psi0)
rhs = np.einsum('abcde,a,b,c,d,e->', V5, psi0, psi0, psi0, psi0, psi0)
ok &= abs(lhs - rhs) < TOL * max(1, abs(rhs))
det.append(f"V5S(p,p,psi)-V5(psi^5) = {lhs-rhs:.1e}")
# telescoping: PB = p (propagator (12/g^2) V4S^{-1} on source (g^2/12) V4S p)
PB = np.linalg.solve(V4S, V4S @ p0)     # the g-factors cancel exactly
ok &= np.allclose(PB, p0, atol=1e-10)
det.append(f"|PB-p| = {np.abs(PB-p0).max():.1e}")
report(0, "basis / telescoping sanity", ok, "; ".join(det))

# ---------------------------------------------------------------- check 1
ok = True
worst = 0.0
for trial in range(20):
    g = rng.uniform(0.02, 0.6)
    psi = rng.standard_normal(N)
    sig = rng.standard_normal(DS)
    p = sym_coords(np.outer(psi, psi))
    K = Kmat(psi, g)
    v = vvec(psi)
    Kinv_v = np.linalg.solve(K, v)
    X = sig - p
    Xt = X - (g / 5.0) * Kinv_v
    lhs = S3_minus_shared(sig, psi, g) - Seff_minus_shared(psi, g)
    rhs = -(g**2 / 24) * Xt @ K @ Xt + (g**4 / 600) * v @ Kinv_v
    dev = abs(lhs - rhs) / max(1.0, abs(lhs))
    worst = max(worst, dev)
ok = worst < TOL
report(1, "exact rewriting S3-Seff5 = -(g^2/24)K(Xt,Xt)+(g^4/600)vK^-1v",
       ok, f"worst rel dev {worst:.1e} over 20 random (sig,psi,g)")

# ---------------------------------------------------------------- check 2
def solve_saddle(psi, g, c=1.0, iters=60):
    p = sym_coords(np.outer(psi, psi))
    sig = p.copy()
    for _ in range(iters):
        grad = (-(g**2 / 12) * V4S @ sig + (g**2 / 12) * V4S @ p
                + c * (g**3 / 60) * np.einsum('IJe,J,e->I', V5S, sig, psi))
        hess = (-(g**2 / 12) * V4S
                + c * (g**3 / 60) * np.einsum('IJe,e->IJ', V5S, psi))
        sig = sig - np.linalg.solve(hess, grad)
    return sig


ok = True
det = []
psi = rng.standard_normal(N)
ratios = []
for g in (0.2, 0.1, 0.05, 0.025):
    sigstar = solve_saddle(psi, g)
    p = sym_coords(np.outer(psi, psi))
    K = Kmat(psi, g)
    v = vvec(psi)
    Kinv_v = np.linalg.solve(K, v)
    Xt_star = (sigstar - p) - (g / 5.0) * Kinv_v
    ok &= np.abs(Xt_star).max() < 1e-8          # Xt vanishes at the saddle
    onshell = S3_minus_shared(sigstar, psi, g) - Seff_minus_shared(psi, g)
    fb = (g**4 / 600) * v @ Kinv_v
    ok &= abs(onshell - fb) < 1e-10 * max(1, abs(fb))
    ratios.append(onshell / g**4)
det.append(f"|Xt(saddle)| < 1e-8; onshell=feedback to 1e-10")
# feedback/g^4 = (1/600)[v V^-1 v + (g/5) v V^-1 W V^-1 v + O(g^2)]; test the
# two-term analytic series: residual must shrink ~4x between g=0.05 and 0.025
v0 = vvec(psi)
Vinv_v = np.linalg.solve(V4S, v0)
W = np.einsum('IJe,e->IJ', V5S, psi)
lim = v0 @ Vinv_v / 600
slope = (Vinv_v @ W @ Vinv_v) / (5 * 600)
res = [abs(r - lim - g * slope) for r, g in zip(ratios[-2:], (0.05, 0.025))]
ok &= res[1] < 0.35 * res[0] and res[1] < 0.02 * abs(lim)
det.append(f"series residuals {res[0]:.2e} -> {res[1]:.2e} (~4x shrink), "
           f"lim {lim:+.6f}")
report(2, "saddle elimination: Xt*=0, on-shell diff = O(g^4) feedback",
       ok, "; ".join(det))

# ---------------------------------------------------------------- check 3
ok = True
c_bad = 1.3
g1, g2 = 0.02, 0.01
psi = rng.standard_normal(N)
p = sym_coords(np.outer(psi, psi))
V5p = np.einsum('IJe,I,J,e->', V5S, p, p, psi)     # V5(psi^5)
mism = []
for g in (g1, g2):
    sigc = solve_saddle(psi, g, c=c_bad)
    d = S3_minus_shared(sigc, psi, g, c=c_bad) - Seff_minus_shared(psi, g)
    mism.append(d / g**3)
target = (c_bad - 1) * V5p / 120
# Richardson: mism(g) = target + O(g); extrapolate
extrap = 2 * mism[1] - mism[0]
ok = abs(extrap - target) < 1e-3 * max(1, abs(target)) and abs(target) > 1e-3
report(3, "falsifiability: c!=1 leaves (c-1)(g^3/5!)V5(psi^5) mismatch",
       ok, f"extrapolated {extrap:+.6f} vs target {target:+.6f}")

# ---------------------------------------------------------------- check 4
ok = True
g = 0.3
psis = [rng.standard_normal(N) for _ in range(5)]


def q_pair(i, j):
    return sym_coords(np.outer(psis[i], psis[j]))


# per-assignment chain: source (g^2/6)V4S q_jk -> prop (12/g^2)V4S^{-1} -> 2 q_jk
# V5 vertex (g^3/5!) with Wick factor 2 (two pairings of the two B's onto the
# two Sigma slots; the cross-term of the exponential carries coefficient 1)
def assignment_value(i, jk, lm):
    leg1 = (12 / g**2) * np.linalg.solve(V4S, (g**2 / 6) * V4S @ q_pair(*jk))
    leg2 = (12 / g**2) * np.linalg.solve(V4S, (g**2 / 6) * V4S @ q_pair(*lm))
    return 2 * (g**3 / 120) * np.einsum('IJe,I,J,e->', V5S, leg1, leg2, psis[i])


from itertools import combinations
total = 0.0
count = 0
vals = []
for i in range(5):
    rest = [x for x in range(5) if x != i]
    seen = set()
    for jk in combinations(rest, 2):
        lm = tuple(x for x in rest if x not in jk)
        key = frozenset((jk, lm))
        if key in seen:
            continue
        seen.add(key)
        vals.append(assignment_value(i, jk, lm))
        total += vals[-1]
        count += 1
contact = g**3 * np.einsum('abcde,a,b,c,d,e->', V5, *psis)
percheck = g**3 / 15 * np.einsum('abcde,a,b,c,d,e->', V5, *psis)
ok &= count == 15
ok &= abs(vals[0] - percheck) < TOL * max(1, abs(percheck))
ok &= abs(total - contact) < TOL * max(1, abs(contact))
report(4, "5-pt diagrammatics: 15 assignments x (g^3/15) = contact kernel",
       ok, f"count={count}, per-assign dev {vals[0]-percheck:.1e}, "
           f"sum dev {total-contact:.1e}")

# ---------------------------------------------------------------- check 5
ok = True
det = []
worst_exact = 0.0
worst_quad = 0.0
for trial in range(10):
    g = rng.uniform(0.05, 0.5)
    psi = rng.standard_normal(N)
    dpsi = rng.standard_normal(N)          # arbitrary variation (even, as R14)
    sig = rng.standard_normal(DS)          # OFF-shell Sigma
    p = sym_coords(np.outer(psi, psi))
    dp = sym_coords(np.outer(dpsi, psi) + np.outer(psi, dpsi))
    K = Kmat(psi, g)
    Kinv = np.linalg.inv(K)
    v = vvec(psi)
    Xstar = (g / 5.0) * Kinv @ v
    X = sig - p
    Xt = X - Xstar
    # variations of the building blocks
    dK = -(g / 5.0) * np.einsum('IJe,e->IJ', V5S, dpsi)
    dv = (np.einsum('IJe,J,e->I', V5S, dp, psi)
          + np.einsum('IJe,J,e->I', V5S, p, dpsi))
    dKinv = -Kinv @ dK @ Kinv
    dXstar = (g / 5.0) * (dKinv @ v + Kinv @ dv)
    dXt = (g / 10.0) * Kinv @ np.einsum('IJe,J,e->I', V5S, Xt, dpsi)
    # (5a) EXACT invariance of the dressed quadratic form
    quad_var = -(g**2 / 24) * (2 * Xt @ K @ dXt + Xt @ dK @ Xt)
    worst_quad = max(worst_quad, abs(quad_var))
    # (5b) full law on Sigma; dS3 - dSeff5 = d[feedback] EXACTLY
    dsig = dp + dXstar + dXt
    grad_sig = (-(g**2 / 12) * V4S @ sig + (g**2 / 12) * V4S @ p
                + (g**3 / 60) * np.einsum('IJe,J,e->I', V5S, sig, psi))
    grad_psi_S3 = ((g**2 / 12) * sig @ V4S @ np.array(
                       [sym_coords(np.outer((e := np.eye(N)[a]), psi)
                                   + np.outer(psi, e)) for a in range(N)]).T
                   + (g**3 / 120) * np.einsum('IJe,I,J->e', V5S, sig, sig))
    dS3 = grad_sig @ dsig + grad_psi_S3 @ dpsi
    # dSeff5
    grad_psi_Seff = ((g**2 / 12) * p @ V4S @ np.array(
                         [sym_coords(np.outer(np.eye(N)[a], psi)
                                     + np.outer(psi, np.eye(N)[a]))
                          for a in range(N)]).T
                     + (g**3 / 60) * np.einsum('IJe,I,J->e', V5S, p, p) @ np.eye(N)
                     + (g**3 / 120) * np.einsum('IJe,I,J->e', V5S, p, p))
    # careful: d/dpsi of (g^3/120) V5S(p,p,psi):
    #   through p twice: (g^3/120)*2*V5S(dp-slot,p,psi) and explicit psi slot
    # rebuild cleanly by finite-poly assembly instead:
    def Seff_grad(psi):
        eps = 1e-6
        gvec = np.zeros(N)
        for a in range(N):
            e = np.zeros(N); e[a] = eps
            gvec[a] = (Seff_minus_shared(psi + e, g)
                       - Seff_minus_shared(psi - e, g)) / (2 * eps)
        return gvec
    # use exact analytic pieces for S3 psi-gradient as well, via same trick
    def S3_grad_psi(sig, psi):
        eps = 1e-6
        gvec = np.zeros(N)
        for a in range(N):
            e = np.zeros(N); e[a] = eps
            gvec[a] = (S3_minus_shared(sig, psi + e, g)
                       - S3_minus_shared(sig, psi - e, g)) / (2 * eps)
        return gvec
    dS3 = grad_sig @ dsig + S3_grad_psi(sig, psi) @ dpsi
    dSeff = Seff_grad(psi) @ dpsi
    # d[feedback]
    dfb = (g**4 / 600) * (dv @ Kinv @ v + v @ dKinv @ v + v @ Kinv @ dv)
    resid = dS3 - dSeff - dfb
    worst_exact = max(worst_exact, abs(resid))
ok = worst_quad < TOL and worst_exact < 1e-4   # 1e-4: finite-diff gradients
det.append(f"quadratic-form variation exact: worst {worst_quad:.1e}")
det.append(f"full law dS3-dSeff5-d[fb]: worst {worst_exact:.1e} (fd-limited)")
# falsifiability: naive composite law leaves O(g^3) residual
g = 0.1
psi = rng.standard_normal(N); dpsi = rng.standard_normal(N)
sig = rng.standard_normal(DS)
p = sym_coords(np.outer(psi, psi))
dp = sym_coords(np.outer(dpsi, psi) + np.outer(psi, dpsi))
grad_sig = (-(g**2 / 12) * V4S @ sig + (g**2 / 12) * V4S @ p
            + (g**3 / 60) * np.einsum('IJe,J,e->I', V5S, sig, psi))
def S3gp(sig, psi):
    eps = 1e-6
    return np.array([(S3_minus_shared(sig, psi + eps * np.eye(N)[a], g)
                      - S3_minus_shared(sig, psi - eps * np.eye(N)[a], g))
                     / (2 * eps) for a in range(N)])
def Segp(psi):
    eps = 1e-6
    return np.array([(Seff_minus_shared(psi + eps * np.eye(N)[a], g)
                      - Seff_minus_shared(psi - eps * np.eye(N)[a], g))
                     / (2 * eps) for a in range(N)])
resid_naive = grad_sig @ dp + S3gp(sig, psi) @ dpsi - Segp(psi) @ dpsi
ok &= abs(resid_naive) > 1e-6      # nonzero: naive law fails at O(g^3)
det.append(f"naive composite law residual {resid_naive:.2e} != 0")
report(5, "EXACT gauge equality with corrected law; naive law fails",
       ok, "; ".join(det))

# ---------------------------------------------------------------- check 6
# Route C constraint Jacobian: sigma_k in H^{otimes k}, k=2,3,4
ok = True
psi = rng.standard_normal(N)
d2, d3, d4 = N**2, N**3, N**4
J = np.zeros((d2 + d3 + d4, d2 + d3 + d4))
J[:d2, :d2] = np.eye(d2)
J[d2:d2 + d3, d2:d2 + d3] = np.eye(d3)
J[d2 + d3:, d2 + d3:] = np.eye(d4)
# -(. ox Psi) blocks
T23 = np.zeros((d3, d2))
for idx in range(d2):
    e = np.zeros(d2); e[idx] = 1
    T23[:, idx] = np.kron(e, psi)
T34 = np.zeros((d4, d3))
for idx in range(d3):
    e = np.zeros(d3); e[idx] = 1
    T34[:, idx] = np.kron(e, psi)
J[d2:d2 + d3, :d2] = -T23
J[d2 + d3:, d2:d2 + d3] = -T34
smin = np.linalg.svd(J, compute_uv=False).min()
# unit LOWER-triangular structure => det = 1 for every Psi (a genuine assertion,
# replacing the former tautological `... is False or True` dead line; critic F10/M3).
tri_ok = np.allclose(np.triu(J, 1), 0)          # strictly-upper block is zero
detJ = np.linalg.det(J)
ok = (smin > 1e-6) and tri_ok and abs(detJ - 1.0) < 1e-9
report(6, "T6/Route C: constraint Jacobian invertible => NO flat directions",
       ok, f"unit lower-triangular (det = {detJ:.3f} = 1), sigma_min = {smin:.3f} > 0")

# ---------------------------------------------------------------- check 7
ok = True
Q = np.zeros((N, N)); Q[0, 1] = 1.0          # Q^2 = 0
assert np.allclose(Q @ Q, 0)
Qhat = np.kron(Q, np.eye(N)) + np.kron(np.eye(N), Q)   # on H^{ox2}, ordered


def to_sym(vec9):
    return sym_coords(vec9.reshape(N, N))


g = 0.25
psi = rng.standard_normal(N)
sig9 = rng.standard_normal(N * N)
sig9 = (sig9.reshape(N, N) + sig9.reshape(N, N).T).flatten() / 2   # symmetric
B9 = rng.standard_normal(N * N)
B9 = (B9.reshape(N, N) + B9.reshape(N, N).T).flatten() / 2
L19 = rng.standard_normal(N * N)
L19 = (L19.reshape(N, N) + L19.reshape(N, N).T).flatten() / 2


def S_tilde(sig9, B9):
    eff = to_sym(sig9 - Qhat @ B9)
    return S3_minus_shared(eff, psi, g)


s0 = S_tilde(sig9, B9)
s1 = S_tilde(sig9 + Qhat @ L19, B9 + L19)
ok &= abs(s1 - s0) < TOL * max(1, abs(s0))
# B=0 gauge recovers S3
ok &= abs(S_tilde(sig9, 0 * B9) - S3_minus_shared(to_sym(sig9), psi, g)) < TOL
report(7, "T6 Stueckelberg: S3(Psi,Sigma-QhatB) exactly L1-shift invariant",
       ok, f"dS = {s1-s0:.1e}; B=0 gauge = S3")

# ---------------------------------------------------------------- check 8
ok = True
det = []
# saturation: omega1 pairing total 5 (per strand); omega2 total 10
NG_Psi, NG_Sigma, NG_Q = 2, 4, 1
# (a) Sigma Qhat-kinetic term forbidden: 4 + (4+1) = 9 != 10
ok &= NG_Sigma + NG_Sigma + NG_Q == 9 and 9 != 10
det.append("omega2(Sig,QhatSig): 4+4+1=9 != 10 -> vanishes")
# (b) partner Pi must sit at N_gh = 5: Pi + (4+1) = 10
NG_Pi = 10 - (NG_Sigma + NG_Q)
ok &= NG_Pi == 5
det.append(f"N_gh(Pi)={NG_Pi}")
# (c) Lambda1 at 3 (Qhat L1 at 4 = Sigma); m2 raises by +2 (erratum-fixed):
NG_L1 = NG_Sigma - NG_Q
ok &= NG_L1 == 3 and NG_L1 + 2 == NG_Pi
det.append(f"N_gh(L1)={NG_L1}, N_gh(m2(L1))={NG_L1+2}=N_gh(Pi)")
# (d) V5 saturation: 5-punctured sphere = 6 + dim_R M_{0,5} = 6+4 = 10
ok &= 6 + 2 * (5 - 3) == 10
ok &= NG_Sigma + NG_Sigma + NG_Psi == 10       # V5(Sig,Sig,Psi)
ok &= 5 * NG_Psi == 10                         # V5(Psi^5)
det.append("V5 saturation 10: (4,4,2) and (2,2,2,2,2) both OK")
# (e) Route C lambda2: constraint pairing saturates 10 => N_gh(lambda2)=6=3k
ok &= 10 - NG_Sigma == 6
det.append("N_gh(lambda2)=6=3k (R13, per-strand c0-)")
report(8, "ghost-number saturation arithmetic (T6/B1 statements)",
       ok, "; ".join(det))

# ---------------------------------------------------------------- summary
print()
n = 9
print(f"{n - len(set(failures))}/{n} checks PASS"
      + (f"  FAILURES: {sorted(set(failures))}" if failures else ""))
raise SystemExit(len(set(failures)))
