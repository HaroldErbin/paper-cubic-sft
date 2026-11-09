"""
Toy check of the L_infty-morphism identities for the comparison map
F(Psi) = (Psi, c Psi^{(x)2}) between the quartic-truncated cyclic L_infty
algebra T = (H_0; Q, ell_2, ell_3) and the enlarged algebra E of
presentation (b) on H_0 (+) Sym^2 H_0 (record 029, brief 9b).

Physical grading (eps = N_gh mod 2); Psi at N_gh = 2 (even), Sigma in Sym^2 of
the gh-2 sector (N_gh = 4, even).  All identities are evaluated in the
even-polarised generating-function form (record 029 eq. (1.2)):

    Ltilde(F(Psi)) =?= dF|_Psi [ L(Psi) ].

VERIFIED
  A  the enlarged brackets (1.5) read off S_HS (eq:SHS): omega-dual of the
     directional derivative of S_HS equals Ltilde(Phi) (checks the 1/12, 1/6,
     1/3 coefficients against the action, both components).
  B  H_0-component of the defect vanishes for c = 1 (all inputs, exactly);
     fails for c != 1 (break-on-purpose).
  C  Sym^2-component: Ltilde(F(Psi))|_Sym2 = 0 for c = 1 (R8 sufficiency),
     != 0 for c != 1.
  D  Sym^2-component of dF[L(Psi)] at g = 0 equals Qhat(Psi^{(x)2}) and is
     NONZERO for generic Psi (the failing two-input identity (2.5)); it
     vanishes for Psi in ker Q (on-shell at g = 0).
  E  three-input Sym^2 term (2.6) is nonzero on generic data.
  F  no-repair in the ansatz phi_1 = iota, phi_2|_Sym2 = B arbitrary symmetric
     bilinear (gh 4-valued), phi_3 = 0: the linear system {Qhat B(Psi,Psi) = 0,
     ell_3(B(Psi,Psi)/2 - Psi^{(x)2}, Psi) = 0 for all Psi} has no solution
     (least-squares residual > 0), while the second family alone is solved
     by B = 2 Psi^{(x)2} (sanity).
  G  grading (9c): with deg_H0 = N_gh - 2, deg_Sym2 = (N_gh - 4)/2 every bracket
     of (1.5) has degree +1 and omega_2 degree -1 on the classical complex
     (H_0 at gh {2,3}, Sym^2 at gh {4,6}); the odd-ghost Sym^2 state
     Lambda x Psi has half-integer degree; on the full toy space the mixed
     brackets are inhomogeneous and no ghost-number-based Z or Z_2 grading of
     Sym^2 makes all of (1.5) homogeneous (m_2 wants slope 1/2, m_2(A x B)
     slope 1).
NOT VERIFIED: odd-input (suspension-sign) sectors; L_infty relations of T
  (not needed for any identity above); the phi_3-exact escape in F;
  uniqueness.  Generic random data, seeded.
"""
from __future__ import annotations

import sys
from itertools import combinations_with_replacement, permutations

import numpy as np

SEED = int(sys.argv[1]) if len(sys.argv) > 1 else 2029
rng = np.random.default_rng(SEED)
print(f"[info] seed = {SEED}")
TOL = 1e-9
FAILS = 0


def report(name: str, ok: bool, detail: str = "") -> None:
    global FAILS
    print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
    if not ok:
        FAILS += 1


# --- graded toy space: ghost numbers (1,2,2,3,3,4); omega pairs a <-> 5-a ---
NGH = np.array([1, 2, 2, 3, 3, 4])
N = len(NGH)
PAR = NGH % 2
GH2 = np.where(NGH == 2)[0]
GH3 = np.where(NGH == 3)[0]

# odd graded-antisymmetric pairing omega_1, saturating N_gh = 5
omega = np.zeros((N, N))
for a in range(N):
    for b in range(N):
        if NGH[a] + NGH[b] == 5 and a < b:
            x = rng.standard_normal() + 1.0
            omega[a, b] = x
            omega[b, a] = -((-1) ** (PAR[a] * PAR[b])) * x
Delta = np.linalg.inv(omega)          # Delta^{ab}: omega_{ab} Delta^{bc} = delta_a^c


def koszul_perm(idx, perm) -> float:
    s = 1.0
    for i in range(len(perm)):
        for j in range(i + 1, len(perm)):
            if perm[i] > perm[j] and PAR[idx[perm[i]]] and PAR[idx[perm[j]]]:
                s = -s
    return s


def sym_unit(idx):
    r = len(idx)
    T = np.zeros((N,) * r)
    for perm in permutations(range(r)):
        pidx = tuple(idx[perm[t]] for t in range(r))
        T[pidx] += koszul_perm(idx, perm)
    return None if np.abs(T).max() < 1e-12 else T / np.abs(T).max()


def vertex_basis(rank: int, target: int):
    out = []
    for idx in combinations_with_replacement(range(N), rank):
        if sum(NGH[list(idx)]) != target:
            continue
        T = sym_unit(idx)
        if T is not None:
            out.append(T)
    return out


def rand_vertex(rank, target):
    B = vertex_basis(rank, target)
    return sum(c * T for c, T in zip(rng.standard_normal(len(B)), B))


# kinetic form K = omega Q, symmetric on the gh-2 block (=> Q cyclic), rank 1
# so that ker Q on gh 2 is one-dimensional (used in check D).
u = rng.standard_normal(2)
K = np.zeros((N, N))
K[np.ix_(GH2, GH2)] = np.outer(u, u)
Q = Delta @ K                          # Q^a_b = Delta^{ac} K_{cb}; maps gh2 -> gh3
V3 = rand_vertex(3, 6)
V4 = rand_vertex(4, 8)
L2 = np.einsum("ea,abc->ebc", Delta, V3)          # ell_2^e_{bc}
L3 = np.einsum("ea,abcd->ebcd", Delta, V4)        # ell_3^e_{bcd}
M2 = np.einsum("ea,fb,abcd->efcd", Delta, Delta, V4)  # m_2^{ef}_{cd}

g = 0.7


def omega2(A, B):
    return np.einsum("ab,ae,bf,ef->", A, omega, omega, B)


def L_trunc(P):
    return Q @ P + g / 2 * np.einsum("ebc,b,c->e", L2, P, P) \
        + g**2 / 6 * np.einsum("ebcd,b,c,d->e", L3, P, P, P)


def S_HS(P, Sig):
    return (0.5 * P @ omega @ Q @ P
            + g / 6 * np.einsum("abc,a,b,c->", V3, P, P, P)
            - g**2 / 24 * np.einsum("abcd,ab,cd->", V4, Sig, Sig)
            + g**2 / 12 * np.einsum("abcd,ab,c,d->", V4, Sig, P, P))


def Ltilde(P, Sig):
    """Enlarged brackets (1.5), summed: Ltilde_1 Phi + 1/2 Ltilde_2(Phi,Phi)."""
    lpsi = Q @ P + g / 2 * np.einsum("ebc,b,c->e", L2, P, P) \
        + g**2 / 6 * np.einsum("ebcd,bc,d->e", L3, Sig, P)
    lsig = -g**2 / 12 * np.einsum("efcd,cd->ef", M2, Sig - np.outer(P, P))
    return lpsi, lsig


def rand_psi():
    P = np.zeros(N)
    P[GH2] = rng.standard_normal(len(GH2))
    return P


def sym2(A, B):
    return np.outer(A, B) + np.outer(B, A)


# ---------------- A: brackets vs action -------------------------------------
P = rand_psi()
Sig = np.zeros((N, N)); s = rng.standard_normal((2, 2)); Sig[np.ix_(GH2, GH2)] = s + s.T
dP = rand_psi()
dS = np.zeros((N, N)); s = rng.standard_normal((2, 2)); dS[np.ix_(GH2, GH2)] = s + s.T
t = 1e-4
dS_num = (S_HS(P + t * dP, Sig + t * dS) - S_HS(P - t * dP, Sig - t * dS)) / (2 * t)
lp, ls = Ltilde(P, Sig)
dS_alg = dP @ omega @ lp + omega2(dS, ls)
report("A  omega-dual of dS_HS = Ltilde (coefficients 1/12,1/6,1/3)", abs(dS_num - dS_alg) < 1e-7,
       f"|diff|={abs(dS_num-dS_alg):.2e}, |dS|={abs(dS_num):.2e}")
# break-on-purpose: wrong source coefficient 1/6 -> 1/12 in Ltilde_psi
lp_bad = lp - g**2 / 12 * np.einsum("ebcd,bc,d->e", L3, Sig, P)
report("A' wrong coefficient detected", abs(dS_num - (dP @ omega @ lp_bad + omega2(dS, ls))) > 1e-6)


# ---------------- defect D(Psi) = Ltilde(F) - dF[L] --------------------------
def defect(P, c):
    Lp = L_trunc(P)
    lp, ls = Ltilde(P, c * np.outer(P, P))
    return lp - Lp, ls, -c * sym2(Lp, P), ls - c * sym2(Lp, P)


P = rand_psi()
dH, lhsS, rhsS, dS2 = defect(P, 1.0)
report("B  H_0-component of defect = 0 at c=1", np.abs(dH).max() < TOL, f"max={np.abs(dH).max():.2e}")
dH13 = defect(P, 1.3)[0]
report("B' H_0-component != 0 at c=1.3 (break)", np.abs(dH13).max() > 1e-6, f"max={np.abs(dH13).max():.2e}")
report("C  Ltilde(F)|_Sym2 = 0 at c=1 (R8 sufficiency)", np.abs(lhsS).max() < TOL, f"max={np.abs(lhsS).max():.2e}")
report("C' Ltilde(F)|_Sym2 != 0 at c=1.3 (break)", np.abs(defect(P, 1.3)[1]).max() > 1e-6)
report("D0 full Sym2 defect != 0 (strict morphism fails)", np.abs(dS2).max() > 1e-6, f"max={np.abs(dS2).max():.2e}")

# D: g^0 part = Qhat(Psi^(x)2); nonzero generically, zero for Psi in ker Q
g_save = g; g = 0.0
_, _, rhs0, d0 = defect(P, 1.0)
Qhat = sym2(Q @ P, P)
report("D  g=0 Sym2 defect = -Qhat(Psi^(x)2)", np.abs(d0 + Qhat).max() < TOL and np.abs(d0).max() > 1e-6,
       f"|d0|={np.abs(d0).max():.2e}")
kerQ = np.zeros(N); v = np.array([u[1], -u[0]]); kerQ[GH2] = v
report("D' ker-Q input: Sym2 defect vanishes (on-shell at g=0)", np.abs(defect(kerQ, 1.0)[3]).max() < TOL
       and np.abs(Q @ kerQ).max() < TOL)
g = g_save

# E: three-input term (2.6): g^1 coefficient of the Sym2 defect at c = 1
def sym2_defect_at(gv, P):
    global g
    gs = g; g = gv
    d = defect(P, 1.0)[3]
    g = gs
    return d
d_g1 = (sym2_defect_at(1e-3, P) - sym2_defect_at(-1e-3, P)) / 2e-3
E_expected = -0.5 * sym2(np.einsum("ebc,b,c->e", L2, P, P), P)
report("E  three-input Sym2 term (2.6) matches and is nonzero", np.abs(d_g1 - E_expected).max() < 1e-6
       and np.abs(E_expected).max() > 1e-6, f"max={np.abs(E_expected).max():.2e}")

# F: no-repair least squares.  Unknown B: symmetric bilinear gh2 x gh2 -> Sym2 at gh 4
# (components on pairs (a,b) with NGH[a]+NGH[b] = 4, symmetric).
pairs4 = [(a, b) for a in range(N) for b in range(a, N) if NGH[a] + NGH[b] == 4]
in_pairs = [(i, j) for i in range(2) for j in range(i, 2)]     # symmetric in the two gh-2 inputs
nB = len(pairs4) * len(in_pairs)
def B_of(coef, P):
    out = np.zeros((N, N)); x = P[GH2]; k = 0
    for (a, b) in pairs4:
        for (i, j) in in_pairs:
            val = coef[k] * (x[i] * x[j] * (1 if i == j else 2)); k += 1
            out[a, b] += val
            if a != b: out[b, a] += val
    return out
rows_Q, rows_l3, rows_l3_rhs = [], [], []
for _ in range(8):
    Pt = rand_psi()
    cols_Q, cols_l3 = [], []
    for k in range(nB):
        e = np.zeros(nB); e[k] = 1.0
        Bk = B_of(e, Pt)
        cols_Q.append((np.einsum("ea,ab->eb", Q, Bk) + np.einsum("fb,ab->af", Q, Bk)).ravel())
        cols_l3.append(0.5 * np.einsum("ebcd,bc,d->e", L3, Bk, Pt))
    rows_Q.append(np.array(cols_Q).T)
    rows_l3.append(np.array(cols_l3).T)
    rows_l3_rhs.append(np.einsum("ebcd,b,c,d->e", L3, Pt, Pt, Pt))
AQ = np.vstack(rows_Q); Al3 = np.vstack(rows_l3); bl3 = np.concatenate(rows_l3_rhs)
# sanity: ell_3 family alone solved by B = 2 Psi^(x)2
sol, *_ = np.linalg.lstsq(Al3, bl3, rcond=None)
res_l3 = np.linalg.norm(Al3 @ sol - bl3)
report("F0 ell_3-family alone is solvable (B = 2 Psi^(x)2)", res_l3 < 1e-8, f"res={res_l3:.2e}")
A = np.vstack([AQ, Al3]); b = np.concatenate([np.zeros(AQ.shape[0]), bl3])
sol, *_ = np.linalg.lstsq(A, b, rcond=None)
res = np.linalg.norm(A @ sol - b)
report("F  no B with Qhat B = 0 and ell_3(B/2 - Psi^2, Psi) = 0 (phi_3 = 0)", res > 1e-3,
       f"residual={res:.3e}, |b|={np.linalg.norm(b):.3e}")

# G: grading (record 029 §1(ii), 9c re-derivation).  deg_H0 = N_gh - 2, deg_Sym2 = (N_gh - 4)/2.
# Every nonzero bracket component must have deg(out) - sum deg(in) = 1, omega_2 degree -1.
def degH(a): return NGH[a] - 2.0
def degS(a, b): return (NGH[a] + NGH[b] - 4.0) / 2
def shifts(classical: bool):
    """Return the set of degree shifts over nonzero components; classical restricts
    H_0 inputs/outputs to gh {2,3} and Sym^2 pairs to total gh {4,6}."""
    inH = lambda a: (not classical) or NGH[a] in (2, 3)
    inS = lambda a, b: (not classical) or NGH[a] + NGH[b] in (4, 6)
    out = {}
    def add(key, val):
        out.setdefault(key, set()).add(round(float(val), 6))
    for e in range(N):
        for b in range(N):
            if abs(Q[e, b]) > 1e-12 and inH(e) and inH(b):
                add("Q", degH(e) - degH(b))
            for c in range(N):
                if classical and NGH[b] + NGH[c] not in (4, 6) and (not inH(b) or not inH(c)):
                    continue
                if abs(L2[e, b, c]) > 1e-12 and inH(e) and inH(b) and inH(c):
                    add("ell_2", degH(e) - degH(b) - degH(c))
                for d in range(N):
                    if abs(L3[e, b, c, d]) > 1e-12 and inH(e) and inS(b, c) and inH(d):
                        add("ell_3(Sigma,Psi)", degH(e) - degS(b, c) - degH(d))
                    for f in range(N):
                        if abs(M2[e, f, c, d]) > 1e-12 and inS(e, f):
                            if inS(c, d):
                                add("m_2", degS(e, f) - degS(c, d))
                            if inH(c) and inH(d):
                                add("m_2(A x B)", degS(e, f) - degH(c) - degH(d))
                        if abs(omega[b, e] * omega[c, f]) > 1e-12 and inS(b, c) and inS(e, f):
                            add("omega_2", degS(b, c) + degS(e, f))
    return out
sh_cl = shifts(True)
# omega_2 of degree -1 <=> nonzero only on deg A + deg B = +1 (same as omega_1: gh 2 with gh 3)
ok = all(v == {1.0} for k, v in sh_cl.items() if k != "omega_2") and sh_cl["omega_2"] == {1.0} \
    and len(sh_cl) == 6
report("G  classical complex: every bracket of (1.5) has degree +1, omega_2 degree -1", ok,
       f"shifts={ {k: sorted(v) for k, v in sh_cl.items()} }")
# G': odd-ghost Sym^2 state (Lambda x Psi, gh 3) has half-integer degree
lam = np.where(NGH == 1)[0][0]
dS_LP = degS(lam, GH2[0])
report("G' odd-ghost Sym2 state Lambda x Psi has half-integer degree (break)", abs(dS_LP - round(dS_LP)) > 0.4,
       f"deg={dS_LP}")
# G'': full space: shifts are not all +1 (mixed brackets off the classical complex), and no
# ghost-number-based grading h(n) of Sym^2 (Z, via least squares; Z_2, by enumeration) exists.
sh_full = shifts(False)
report("G'' full toy space: brackets inhomogeneous in this grading (break)",
       any(v != {1.0} for k, v in sh_full.items() if k != "omega_2"),
       f"shifts={ {k: sorted(v) for k, v in sh_full.items()} }")
def grading_system(classical: bool):
    """Rows: h(n_out) - h(n_in) = 1 (m_2), h(n_out) = degH+degH+1 (m_2(AxB)),
    degH(out) = h(n_in) + degH + 1 (ell_3(Sigma,Psi)), over nonzero components; unknowns h(n)."""
    nmax = 2 * NGH.max(); rows, rhs = [], []
    inH = lambda a: (not classical) or NGH[a] in (2, 3)
    inS = lambda a, b: (not classical) or NGH[a] + NGH[b] in (4, 6)
    for e, f, c, d in zip(*np.nonzero(np.abs(M2) > 1e-12)):
        if inS(e, f) and inS(c, d):
            r = np.zeros(nmax + 1); r[NGH[e] + NGH[f]] += 1; r[NGH[c] + NGH[d]] -= 1; rows.append(r); rhs.append(1)
        if inS(e, f) and inH(c) and inH(d):
            r = np.zeros(nmax + 1); r[NGH[e] + NGH[f]] += 1; rows.append(r); rhs.append(degH(c) + degH(d) + 1)
    for e, b, c, d in zip(*np.nonzero(np.abs(L3) > 1e-12)):
        if inH(e) and inS(b, c) and inH(d):
            r = np.zeros(nmax + 1); r[NGH[b] + NGH[c]] += 1; rows.append(r); rhs.append(degH(e) - degH(d) - 1)
    return np.array(rows), np.array(rhs, dtype=float)
A_cl, b_cl = grading_system(True)
res_cl = np.linalg.norm(A_cl @ np.linalg.lstsq(A_cl, b_cl, rcond=None)[0] - b_cl)
A_fu, b_fu = grading_system(False)
res_fu = np.linalg.norm(A_fu @ np.linalg.lstsq(A_fu, b_fu, rcond=None)[0] - b_fu)
z2_ok = False
nmax = 2 * NGH.max()
for bits in range(2 ** (nmax + 1)):
    h = np.array([(bits >> n) & 1 for n in range(nmax + 1)], dtype=float)
    if np.all(np.mod(A_fu @ h - b_fu, 2) == 0):
        z2_ok = True; break
report("G3 Z-grading of Sym2 by ghost number exists on the classical complex, none on the full space (Z or Z_2)",
       res_cl < 1e-9 and res_fu > 1e-3 and not z2_ok,
       f"res_classical={res_cl:.1e}, res_full={res_fu:.2e}, Z2_full_exists={z2_ok}")

print(f"[summary] {'ALL PASS' if FAILS == 0 else f'{FAILS} FAIL'}")
sys.exit(1 if FAILS else 0)
