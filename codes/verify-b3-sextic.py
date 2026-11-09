#!/usr/bin/env python3
"""
verify-b3-sextic.py — machine checks for the B3 O(g_s^4) sextic milestone
(derivation 013): the V6(Sigma,Sigma,Sigma) step of Route B.

Finite-dimensional model, physical grading (all fields Grassmann-even), same
machinery as verify-b1-quintic.py: H_0 = R^N, V4/V5/V6 generic totally
symmetric tensors, orthonormal Sym^2 basis (all factor-2 traps absent).

Conventions (extend eq:SHS / derivations 011):
  S4(Psi,Sigma) = [shared V2,V3] - (g^2/4!) V4(Sig,Sig) + (2g^2/4!) V4(Sig,P)
                  + (g^3/5!) V5(Sig,Sig,Psi)
                  + (g^4/6!) [ c6 V6(Sig,Sig,Sig) - theta C(Sig,Sig,Sig) ]
  S_eff6(Psi)   = [shared] + (g^2/4!) V4(Psi^4) + (g^3/5!) V5(Psi^5)
                  + (g^4/6!) V6(Psi^6)
with P = Psi^{ox2} and C the COMPOSITE Sigma-channel kernel
  C(A,B,Z) = sum_strands < V5(., A, z1) , V4^{-1} V5(., B, z2) >,
  (Z = sum z1 ox z2; on the diagonal C(P,P,P) = v V4^{-1} v, v = V5(.,P,Psi)).
Headline: matching FORCES (c6, theta) = (1, 6/5); the pure geometric V6
(theta = 0) FAILS, mismatch = the (g^4/600) v V4^{-1} v feedback of 011 (B.2).

Checks
  (0) setup sanity: basis completeness, V4S invertible, V6S diagonal = V6,
      C(p,p,p) = v V4^{-1} v, T_act symmetric, dressed Hessian
      invertible for small g (no new flat directions)
  (1) EXACT rewriting (identity in (Sigma,Psi,g), ANY (c6,theta)):
      S4 - S_eff6 = -(g^2/24) K6(Xt6,Xt6) + (g^4/720) T_act(X^3)
                    + (g^4/600) v6 K6^{-1} v6
                    + (g^4/720) [T_act(p^3) - V6(psi^6)]
      with K6 = K - (g^2/10) T_act(.,.,p), v6 = v + (g/4) T_act(.,p,p),
      Xt6 = X - (g/5) K6^{-1} v6, K/v as in 011
  (2) saddle (tuned c6=1, theta=6/5): on-shell mismatch M(g) = S4(saddle)
      - S_eff6 splits EXACTLY as F6 + cubic remainder + quadratic remainder
      with the remainders O(g^7)/O(g^10) (log-slope tests), so M = O(g^5)
      with leading coefficient (verified directly on the exact F6 formula)
      A5 = (1/600) [ (1/2) T_act(V4^{-1}v, p, p) + (1/5) v V4^{-1}W V4^{-1}v ]
  (3) forcing/falsifiability:
      (a) theta = 0 (pure geometric V6): M/g^4 -> (1/600) v V4^{-1} v != 0
      (b) c6 = 1.3: M/g^4 -> (c6-1)/720 V6(psi^6)
      (c) the two invariants v V4^{-1} v and V6(psi^6) are independent
          functions of Psi => matching forces BOTH c6 = 1 and theta = 6/5
  (4) 6-point diagrammatics: per assignment {i,(jk) | l,(mn)} the
      [source-prop-V5 - Sigmaprop - V5-prop-source] tree =
      (g^4/75) V5(.,q_jk,psi_i) V4^{-1} V5(.,q_mn,psi_l); 90 assignments;
      sum = polarization of (g^4/600) v V4^{-1} v = polarization of the
      theta-C contact term (both checked; polarization operator = exact
      multilinear coefficient extraction, 2^6 evaluations)
  (5) EXACT gauge equality at O(g^4): with the corrected law
        dSigma = d[Sigma*(Psi)] + dY,
        dY = Kcal^{-1} [ -1/2 (dKcal)(.,Y) + (g^2/20) T_act(.,Y,dY) ]
      (implicit linear system; Y = Sigma - Sigma*, Kcal = saddle Hessian)
      one has dS4 - dS_eff6 = d[F5] EXACTLY (F5 = on-shell mismatch fn);
      homogeneity: on-shell Y=0 => dY=0 (Sigma transforms as its saddle);
      falsifiability: dropping the T-correction, or using the 011 law
      (B.8) alone, leaves a nonzero residual
  (6) arithmetic: ghost-number saturations (V6: 12 = 4+4+4; C-composite
      internally consistent) and the power-counting exclusion table (every
      non-three-Sigma O(g^4) addition contaminates an n-point tree at the
      wrong g_s order)

All checks PASS/FAIL; exit code = number of failures.
"""

import itertools
import math

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
    T = rng.standard_normal(shape)
    S = np.zeros_like(T)
    for perm in itertools.permutations(range(len(shape))):
        S += np.transpose(T, perm)
    return S / math.factorial(len(shape))


V4 = sym_tensor((N,) * 4)
V5 = sym_tensor((N,) * 5)
V6 = sym_tensor((N,) * 6)

# orthonormal Sym^2 basis Lambda_I (Frobenius)
Lam = []
for a in range(N):
    E = np.zeros((N, N)); E[a, a] = 1.0
    Lam.append(E)
for a in range(N):
    for b in range(a + 1, N):
        E = np.zeros((N, N)); E[a, b] = E[b, a] = 1 / np.sqrt(2)
        Lam.append(E)
Lam = np.array(Lam)                                         # (DS, N, N)

V4S = np.einsum('abcd,Iab,Jcd->IJ', V4, Lam, Lam)           # (DS,DS)
V5S = np.einsum('abcde,Iab,Jcd->IJe', V5, Lam, Lam)         # (DS,DS,N)
V6S3 = np.einsum('abcdef,Iab,Jcd,Kef->IJK', V6, Lam, Lam, Lam)  # (DS,DS,DS)
V4inv = np.linalg.inv(V4S)

# composite Sigma-channel kernel C_raw[I,J,K]: I,J = pair slots into the two
# V5's, K = the strand-split slot (Z's strands distributed one per V5)
C_raw = np.einsum('Kef,MIe,MN,NJf->IJK', Lam, V5S, V4inv, V5S)
T_C = (C_raw + C_raw.transpose(2, 1, 0) + C_raw.transpose(0, 2, 1)) / 3.0

THETA = 6.0 / 5.0


def T_action(c6=1.0, theta=THETA):
    return c6 * V6S3 - theta * T_C


def sym_coords(M):
    return np.einsum('Iab,ab->I', Lam, (M + M.T) / 2)


def pvec(psi):
    return sym_coords(np.outer(psi, psi))


def Kmat(psi, g):
    return V4S - (g / 5.0) * np.einsum('IJe,e->IJ', V5S, psi)


def vvec(psi):
    p = pvec(psi)
    return np.einsum('IJe,J,e->I', V5S, p, psi)


def S4_minus_shared(sig, psi, g, c6=1.0, theta=THETA):
    p = pvec(psi)
    Ta = T_action(c6, theta)
    return (-(g**2 / 24) * sig @ V4S @ sig
            + (g**2 / 12) * sig @ V4S @ p
            + (g**3 / 120) * np.einsum('IJe,I,J,e->', V5S, sig, sig, psi)
            + (g**4 / 720) * np.einsum('IJK,I,J,K->', Ta, sig, sig, sig))


def Seff6_minus_shared(psi, g):
    p = pvec(psi)
    return ((g**2 / 24) * p @ V4S @ p
            + (g**3 / 120) * np.einsum('IJe,I,J,e->', V5S, p, p, psi)
            + (g**4 / 720) * np.einsum('abcdef,a,b,c,d,e,f->', V6,
                                       psi, psi, psi, psi, psi, psi))


def grad_hess(sig, psi, g, c6=1.0, theta=THETA):
    p = pvec(psi)
    Ta = T_action(c6, theta)
    grad = (-(g**2 / 12) * V4S @ sig + (g**2 / 12) * V4S @ p
            + (g**3 / 60) * np.einsum('IJe,J,e->I', V5S, sig, psi)
            + (g**4 / 240) * np.einsum('IJK,J,K->I', Ta, sig, sig))
    hess = (-(g**2 / 12) * V4S
            + (g**3 / 60) * np.einsum('IJe,e->IJ', V5S, psi)
            + (g**4 / 120) * np.einsum('IJK,K->IJ', Ta, sig))
    return grad, hess


def solve_saddle(psi, g, c6=1.0, theta=THETA):
    """Newton with g-continuation from the perturbative start Sigma = P,
    tracking the perturbative branch (warm starts; convergence asserted,
    so a bad draw cannot silently return a non-saddle)."""
    sig = pvec(psi).copy()
    for gcur in np.linspace(0.0, g, 2 + int(g / 0.02))[1:]:
        for _ in range(60):
            grad, hess = grad_hess(sig, psi, gcur, c6, theta)
            sig = sig - np.linalg.solve(hess, grad)
            if np.abs(grad).max() < 1e-14:
                break
    gnorm = np.abs(grad_hess(sig, psi, g, c6, theta)[0]).max()
    assert gnorm < 1e-12, f"saddle not converged: |grad|={gnorm:.1e}"
    return sig


# ---------------------------------------------------------------- check 0
ok = True
det = []
comp = np.einsum('Iab,Icd->abcd', Lam, Lam)
idsym = 0.5 * (np.einsum('ac,bd->abcd', np.eye(N), np.eye(N))
               + np.einsum('ad,bc->abcd', np.eye(N), np.eye(N)))
ok &= np.allclose(comp, idsym, atol=1e-12)
cond = np.linalg.cond(V4S)
ok &= cond < 1e6
det.append(f"cond(V4S)={cond:.1f}")
psi0 = rng.standard_normal(N)
p0 = pvec(psi0)
# V6S3 diagonal reproduces V6(psi^6)
lhs = np.einsum('IJK,I,J,K->', V6S3, p0, p0, p0)
rhs = np.einsum('abcdef,a,b,c,d,e,f->', V6, *([psi0] * 6))
ok &= abs(lhs - rhs) < TOL * max(1, abs(rhs))
det.append(f"V6S3(p^3)-V6(psi^6) = {lhs-rhs:.1e}")
# C diagonal = v V4^{-1} v (both raw and symmetrized)
v0 = vvec(psi0)
target = v0 @ V4inv @ v0
for name, K3 in (("C_raw", C_raw), ("T_C", T_C)):
    val = np.einsum('IJK,I,J,K->', K3, p0, p0, p0)
    ok &= abs(val - target) < TOL * max(1, abs(target))
    det.append(f"{name}(p^3)-vV4invV = {val-target:.1e}")
# T_act fully symmetric
Ta = T_action()
for perm in itertools.permutations(range(3)):
    ok &= np.allclose(Ta, Ta.transpose(perm), atol=1e-10)
# dressed Hessian invertible for random data, small g (no new flat dirs)
g = 0.3
sig = rng.standard_normal(DS)
_, hess = grad_hess(sig, psi0, g)
condH = np.linalg.cond(hess)
ok &= condH < 1e6
det.append(f"cond(Hess)={condH:.1f} (no new flat directions)")
report(0, "setup sanity (basis, diagonals, C(p^3)=vV4inv v, symmetry)",
       ok, "; ".join(det))

# ---------------------------------------------------------------- check 1
ok = True
worst = 0.0
for trial in range(20):
    g = rng.uniform(0.02, 0.5)
    c6 = rng.uniform(0.5, 1.5)          # identity must hold for ANY (c6,theta)
    theta = rng.uniform(0.0, 2.0)
    psi = rng.standard_normal(N)
    sig = rng.standard_normal(DS)
    p = pvec(psi)
    Ta = T_action(c6, theta)
    K = Kmat(psi, g)
    v = vvec(psi)
    K6 = K - (g**2 / 10) * np.einsum('IJK,K->IJ', Ta, p)
    v6 = v + (g / 4.0) * np.einsum('IJK,J,K->I', Ta, p, p)
    K6inv_v6 = np.linalg.solve(K6, v6)
    X = sig - p
    Xt6 = X - (g / 5.0) * K6inv_v6
    V6diag = np.einsum('abcdef,a,b,c,d,e,f->', V6, *([psi] * 6))
    lhs = (S4_minus_shared(sig, psi, g, c6, theta)
           - Seff6_minus_shared(psi, g))
    rhs = (-(g**2 / 24) * Xt6 @ K6 @ Xt6
           + (g**4 / 720) * np.einsum('IJK,I,J,K->', Ta, X, X, X)
           + (g**4 / 600) * v6 @ K6inv_v6
           + (g**4 / 720) * (np.einsum('IJK,I,J,K->', Ta, p, p, p) - V6diag))
    worst = max(worst, abs(lhs - rhs) / max(1.0, abs(lhs)))
ok = worst < TOL
report(1, "EXACT rewriting with K6, v6, cubic remainder (any c6,theta)",
       ok, f"worst rel dev {worst:.1e} over 20 random (sig,psi,g,c6,theta)")

# ---------------------------------------------------------------- check 2
ok = True
det = []
psi = rng.standard_normal(N)
p = pvec(psi)
v = vvec(psi)
Ta = T_action()
Vinv_v = V4inv @ v
W = np.einsum('IJe,e->IJ', V5S, psi)
A5 = (0.5 * np.einsum('IJK,I,J,K->', Ta, Vinv_v, p, p)
      + 0.2 * Vinv_v @ W @ Vinv_v) / 600.0
def F6_exact(g):
    """The Sigma-independent feedback of the exact rewriting (check 1)."""
    K6 = Kmat(psi, g) - (g**2 / 10) * np.einsum('IJK,K->IJ', Ta, p)
    v6 = v + (g / 4.0) * np.einsum('IJK,J,K->I', Ta, p, p)
    return g**4 * (v6 @ np.linalg.solve(K6, v6) - v @ Vinv_v) / 600


# (a) exact on-shell decomposition M = F6 + cubic + quadratic remainders,
#     with the remainders O(g^7) and O(g^10) (log-slope tests under halving)
pieces = {}
for g in (0.04, 0.02, 0.01):
    sigstar = solve_saddle(psi, g)
    M = S4_minus_shared(sigstar, psi, g) - Seff6_minus_shared(psi, g)
    X = sigstar - p
    cub = (g**4 / 720) * np.einsum('IJK,I,J,K->', Ta, X, X, X)
    K6 = Kmat(psi, g) - (g**2 / 10) * np.einsum('IJK,K->IJ', Ta, p)
    v6 = v + (g / 4.0) * np.einsum('IJK,J,K->I', Ta, p, p)
    Xt6 = X - (g / 5.0) * np.linalg.solve(K6, v6)
    quad = -(g**2 / 24) * Xt6 @ K6 @ Xt6
    # both sides assembled from O(1) terms: absolute machine tolerance
    ok &= abs(M - (F6_exact(g) + cub + quad)) < 1e-12
    pieces[g] = (M, cub, quad)
slope_c = np.log2(pieces[0.02][1] / pieces[0.01][1])
slope_q = np.log2(pieces[0.02][2] / pieces[0.01][2])
ok &= abs(slope_c - 7) < 0.4 and abs(slope_q - 10) < 0.6
det.append("M = F6 + cubic + quadratic remainders (exact split; log-slopes "
           f"{slope_c:.2f}~7, {slope_q:.2f}~10)")
# (b) A5 = lim F6/g^5, directly on the exact formula (no cancellations)
g_tiny = 1e-5
r_tiny = F6_exact(g_tiny) / g_tiny**5
scale = max(abs(A5), abs(v @ Vinv_v) / 600)
ok &= abs(r_tiny - A5) < 1e-3 * scale
det.append(f"F6/g^5 at g=1e-5: {r_tiny:+.6f} vs analytic A5 {A5:+.6f}")
report(2, "saddle: on-shell mismatch = O(g^5) with analytic A5 coefficient",
       ok, "; ".join(det))

# ---------------------------------------------------------------- check 3
ok = True
det = []
psi = rng.standard_normal(N)
p = pvec(psi)
v = vvec(psi)
vViv = v @ V4inv @ v
V6d = np.einsum('abcdef,a,b,c,d,e,f->', V6, *([psi] * 6))
def quad_richardson(rfun, gs):
    """A + B g + C g^2 -> A, from r at (g, g/2, g/4)."""
    r1, r2, r3 = (rfun(g) for g in gs)
    return (r1 - 6 * r2 + 8 * r3) / 3.0


# (a) pure geometric V6 (theta=0) FAILS: M/g^4 -> (1/600) v V4inv v
def ratio4(g, c6, theta):
    sigstar = solve_saddle(psi, g, c6=c6, theta=theta)
    return (S4_minus_shared(sigstar, psi, g, c6, theta)
            - Seff6_minus_shared(psi, g)) / g**4


extr = quad_richardson(lambda g: ratio4(g, 1.0, 0.0), (0.04, 0.02, 0.01))
tgt = vViv / 600
ok &= abs(extr - tgt) < 2e-3 * max(1, abs(tgt)) and abs(tgt) > 1e-4
det.append(f"theta=0: mism/g^4 -> {extr:+.6f} = vV4inv v/600 {tgt:+.6f} != 0")
# (b) c6 != 1 leaves (c6-1)/720 V6(psi^6)
c_bad = 1.3
extr = quad_richardson(lambda g: ratio4(g, c_bad, THETA), (0.04, 0.02, 0.01))
tgt = (c_bad - 1) * V6d / 720
ok &= abs(extr - tgt) < 2e-3 * max(1, abs(tgt)) and abs(tgt) > 1e-4
det.append(f"c6=1.3: mism/g^4 -> {extr:+.6f} vs (c6-1)V6/720 {tgt:+.6f}")
# (c) independence of the two invariants across Psi draws => rank-2 forcing
ratios_inv = []
for _ in range(3):
    ps = rng.standard_normal(N)
    vv = vvec(ps)
    ratios_inv.append((vv @ V4inv @ vv)
                      / np.einsum('abcdef,a,b,c,d,e,f->', V6, *([ps] * 6)))
spread = np.ptp(ratios_inv) / max(abs(x) for x in ratios_inv)
ok &= spread > 1e-3
det.append(f"invariant ratios spread {spread:.2f} => (c6,theta) both forced")
report(3, "forcing: pure V6 fails by the (B.2) feedback; (c6,theta)=(1,6/5)",
       ok, "; ".join(det))

# ---------------------------------------------------------------- check 4
ok = True
det = []
g = 0.3
psis = [rng.standard_normal(N) for _ in range(6)]


def q_pair(i, j):
    return sym_coords(np.outer(psis[i], psis[j]))


def assignment_value(i, jk, l, mn):
    """[src-prop]-V5(.,q_jk,psi_i)-[Sigma-prop]-V5(.,q_mn,psi_l)-[prop-src].

    (g^3/120)^2 x 4 (two identical Sigma-slots per V5: source-vs-internal)
    x (12/g^2) internal prop x [2q telescoped]^2 = (g^4/75) kernel value.
    """
    left = np.einsum('MJe,J,e->M', V5S, q_pair(*jk), psis[i])
    right = np.einsum('MJe,J,e->M', V5S, q_pair(*mn), psis[l])
    return (g**4 / 75.0) * left @ V4inv @ right


def pol6(f):
    """Coefficient of t1...t6 in f(sum t_i psi_i), f homogeneous degree 6.

    Equals the full Wick-contraction sum of the contact term f onto six
    distinct externals (n! x multilinear symmetrized form)."""
    total = 0.0
    for mask in range(1, 64):
        vec = sum(psis[i] for i in range(6) if mask >> i & 1)
        total += (-1) ** (6 - bin(mask).count('1')) * f(vec)
    return total


# enumerate the 90 assignments: unordered {triple_A, triple_B}, single in each
vals = []
total = 0.0
count = 0
idx = list(range(6))
seen = set()
for tripleA in itertools.combinations(idx, 3):
    tripleB = tuple(x for x in idx if x not in tripleA)
    key = frozenset((tripleA, tripleB))
    if key in seen:
        continue
    seen.add(key)
    for i in tripleA:
        jk = tuple(x for x in tripleA if x != i)
        for l in tripleB:
            mn = tuple(x for x in tripleB if x != l)
            vals.append(assignment_value(i, jk, l, mn))
            total += vals[-1]
            count += 1
ok &= count == 90
det.append(f"count={count}")
# target 1: polarization of the theta=0 mismatch fn (g^4/600) v V4inv v
pol_feedback = pol6(lambda ps: (g**4 / 600)
                    * vvec(ps) @ V4inv @ vvec(ps))
ok &= abs(total - pol_feedback) < TOL * max(1, abs(pol_feedback))
det.append(f"sum vs pol[(g^4/600)vV4inv v] dev {total-pol_feedback:.1e}")
# target 2: polarization of the theta-C contact term of the action
pol_C = pol6(lambda ps: (THETA * g**4 / 720)
             * np.einsum('IJK,I,J,K->', T_C, pvec(ps), pvec(ps), pvec(ps)))
ok &= abs(total - pol_C) < TOL * max(1, abs(pol_C))
det.append(f"sum vs pol[theta C-contact] dev {total-pol_C:.1e}")
report(4, "6-pt diagrammatics: 90 two-V5 trees = feedback = C-contact",
       ok, "; ".join(det))

# ---------------------------------------------------------------- check 5
ok = True
det = []
Ta = T_action()


def dp_of(psi, dpsi):
    return sym_coords(np.outer(dpsi, psi) + np.outer(psi, dpsi))


def dSeff6(psi, dpsi, g):
    p = pvec(psi)
    dp = dp_of(psi, dpsi)
    return ((g**2 / 12) * p @ V4S @ dp
            + (g**3 / 60) * np.einsum('IJe,I,J,e->', V5S, dp, p, psi)
            + (g**3 / 120) * np.einsum('IJe,I,J,e->', V5S, p, p, dpsi)
            + (g**4 / 120) * np.einsum('abcdef,a,b,c,d,e,f->', V6,
                                       dpsi, psi, psi, psi, psi, psi))


def dS4_explicit_psi(sig, psi, dpsi, g):
    """Explicit-Psi part of dS4 (T-term has a fixed kernel: no Psi there)."""
    dp = dp_of(psi, dpsi)
    return ((g**2 / 12) * sig @ V4S @ dp
            + (g**3 / 120) * np.einsum('IJe,I,J,e->', V5S, sig, sig, dpsi))


worst_main = 0.0
worst_hom = 0.0
res_noT = None
res_b1law = None
redraws = 0
trial = 0
while trial < 10:
    g = rng.uniform(0.04, 0.25)
    psi = rng.standard_normal(N)
    dpsi = rng.standard_normal(N)
    sig = rng.standard_normal(DS)          # OFF-shell
    try:
        sigstar = solve_saddle(psi, g)
    except AssertionError:
        # draw beyond the fold of the perturbative branch: outside the
        # domain of the (perturbative) claim — resample
        redraws += 1
        assert redraws < 50
        continue
    _, hess = grad_hess(sigstar, psi, g)
    Y = sig - sigstar
    Kcal = -(12 / g**2) * hess             # = K6 - (g^2/10) T(.,.,X*)
    Kcal_inv = np.linalg.inv(Kcal)
    # dSigma* by the implicit function theorem (analytic)
    dp = dp_of(psi, dpsi)
    b = ((g**2 / 12) * V4S @ dp
         + (g**3 / 60) * np.einsum('IJe,J,e->I', V5S, sigstar, dpsi))
    dsigstar = -np.linalg.solve(hess, b)
    # dKcal = -(g/5) V5(.,.,dpsi) - (g^2/10) T(.,.,dSigma*)
    dKcal = (-(g / 5.0) * np.einsum('IJe,e->IJ', V5S, dpsi)
             - (g**2 / 10) * np.einsum('IJK,K->IJ', Ta, dsigstar))
    # corrected law: [1 - (g^2/20) Kcal^{-1} T(.,Y,.)] dY = -1/2 Kcal^{-1} dKcal Y
    TY = np.einsum('IJK,J->IK', Ta, Y)
    Msys = np.eye(DS) - (g**2 / 20) * Kcal_inv @ TY
    dY = np.linalg.solve(Msys, -0.5 * Kcal_inv @ (dKcal @ Y))
    dsig = dsigstar + dY
    # dS4 (all analytic)
    grad, _ = grad_hess(sig, psi, g)
    dS4 = grad @ dsig + dS4_explicit_psi(sig, psi, dpsi, g)
    # dF5 by the envelope theorem: grad_Sigma = 0 at the saddle
    dF5 = dS4_explicit_psi(sigstar, psi, dpsi, g) - dSeff6(psi, dpsi, g)
    resid = dS4 - dSeff6(psi, dpsi, g) - dF5
    worst_main = max(worst_main, abs(resid))
    # homogeneity: on-shell Y=0 => dY=0 exactly
    dY0 = np.linalg.solve(np.eye(DS), -0.5 * Kcal_inv @ (dKcal @ (0 * Y)))
    worst_hom = max(worst_hom, np.abs(dY0).max())
    if trial == 0:
        # falsifiability (i): drop the T-correction in the law
        dY_noT = -0.5 * Kcal_inv @ (dKcal @ Y)
        dS4_noT = grad @ (dsigstar + dY_noT) + dS4_explicit_psi(sig, psi,
                                                                dpsi, g)
        res_noT = dS4_noT - dSeff6(psi, dpsi, g) - dF5
        # falsifiability (ii): the 011 law (B.8) verbatim
        p = pvec(psi)
        K = Kmat(psi, g)
        vv = vvec(psi)
        Kinv = np.linalg.inv(K)
        Xstar_011 = (g / 5.0) * Kinv @ vv
        Xt = (sig - p) - Xstar_011
        dK = -(g / 5.0) * np.einsum('IJe,e->IJ', V5S, dpsi)
        dv = (np.einsum('IJe,J,e->I', V5S, dp, psi)
              + np.einsum('IJe,J,e->I', V5S, p, dpsi))
        dXstar_011 = (g / 5.0) * (-Kinv @ dK @ Kinv @ vv + Kinv @ dv)
        dXt = (g / 10.0) * Kinv @ np.einsum('IJe,J,e->I', V5S, Xt, dpsi)
        dsig_011 = dp + dXstar_011 + dXt
        dS4_011 = grad @ dsig_011 + dS4_explicit_psi(sig, psi, dpsi, g)
        res_b1law = dS4_011 - dSeff6(psi, dpsi, g) - dF5
    trial += 1
ok &= worst_main < 1e-10
ok &= worst_hom < 1e-14
ok &= abs(res_noT) > 1e-8 and abs(res_b1law) > 1e-8
det.append(f"exact equality worst {worst_main:.1e} (analytic, off-shell)")
det.append(f"homogeneity |dY(Y=0)| = {worst_hom:.1e}")
det.append(f"falsif: no-T-corr residual {res_noT:.2e}, "
           f"011-law residual {res_b1law:.2e}")
report(5, "EXACT gauge equality with corrected implicit law; homogeneous",
       ok, "; ".join(det))

# ---------------------------------------------------------------- check 6
ok = True
det = []
NG_Psi, NG_Sig, NG_strand = 2, 4, 2
# V6 saturation: 6 + dim_R M_{0,6} = 6 + 2(6-3) = 12; (Sig,Sig,Sig)=12
ok &= 6 + 2 * (6 - 3) == 12 and 3 * NG_Sig == 12
det.append("V6 saturation 12 = 4+4+4")
# C-composite: each V5 saturates 10 = Sig(4)+strand(2)+prop-slot(4);
# the V4^{-1} pairing joins two ghost-4 slots (V4 saturation 8 = 4+4);
# external total 4+4+2+2 = 12 matches the V6 slot it replaces
ok &= NG_Sig + NG_strand + 4 == 10
ok &= 4 + 4 == 8 == 6 + 2 * (4 - 3)
ok &= NG_Sig + NG_Sig + 2 * NG_strand == 12
det.append("C internal: V5 slots 4+2+4=10, prop pairing 4+4=8, external 12")
# power-counting exclusions: any non-three-Sigma O(g^4) cubic addition
# contaminates an n-point tree at order 4 != n-2 (target tree order)
contaminations = {          # term -> (n_point, target_order)
    "g^4 Psi^3 (3-pt contact)": (3, 1),
    "g^4 D(Sig,Psi^2) source corr (on-shell 4-pt)": (4, 2),
    "g^4 dW(Sig,Sig,Psi) coupling corr (on-shell 5-pt)": (5, 3),
    "g^4 dK(Sig,Sig) kinetic corr ([src-prop-dK-prop-src] 4-pt)": (4, 2),
    "g^4 V3(Sig,Psi) mixing ([ext-mix-prop-src] 3-pt)": (3, 1),
    "g^4 L(Sig) tadpole ([L-prop-src] 2-pt)": (2, 0),
}
for term, (n, tgt) in contaminations.items():
    ok &= 4 != tgt and tgt == n - 2
det.append(f"{len(contaminations)} exclusions: all contaminate at g^4 != "
           "g^(n-2) => only three-Sigma couplings admissible at O(g^4)")
report(6, "arithmetic: saturations + power-counting exclusion table",
       ok, "; ".join(det))

# ---------------------------------------------------------------- summary
print()
n = 7
print(f"{n - len(set(failures))}/{n} checks PASS"
      + (f"  FAILURES: {sorted(set(failures))}" if failures else ""))
raise SystemExit(len(set(failures)))
