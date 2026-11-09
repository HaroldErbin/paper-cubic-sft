"""Verify record 067: the linearised BRST operator of the cubic theory around a background.

Record: ``agent/derivations/067-brst-around-background.md``. Check labels = claim-tree nodes.

Model (float, numpy; 060 part 2's precedent). The finite cyclic L-infinity model of record 058
Part B in 060's variant: tree-level transfer of matrix Chern-Simons on T^3,
A = Lambda[th1,th2,th3] (x) End(W), W in degrees (0,0,1,1) with a rank-one D, massive
fields in degree 1 integrated out (cut (1,)). Builder ``LinfModel`` imported from
``codes/verify-mean-field-fluctuations.py``. The unrestricted field psi (all degrees; ghost
number = degree + 1) carries Zwiebach's master action S^(k) = sum_{n<=k+2} g^{n-2} S_n, whose
Hessian at psi_0 is omega T^(k)_{psi_0}, T^(k) = T_0 + g T_1 + g^2 T_2 + [g^3 T_3]
(homological perturbation lemma; T_3 = p[A_2 - A_1 h A_0 - A_0 h A_1 + A_0 h A_0 h A_0] iota).
The auxiliary Sigma lives in S = Sym^2 H^1 / ker V_4, realised as im V_4 (basis U); the
Sym^2 basis is E_ab = e_a (x) e_b + e_b (x) e_a (a<b), E_aa = e_a (x) e_a, so that the Gram
matrix V_4(E_ab, E_cd) = (2-d_ab)(2-d_cd) V_abcd is symmetric.

Background: a one-parameter Maurer-Cartan family psi_0(g) = p Phi_0, Phi_0 = (D' - D)/g with
D' = (u + g a)(v + g b)^T (exact MC point of the untruncated theory, O(1) in g), and
Sigma_0 = Sigma_*(psi_0) (exact Sigma-EOM).

The joint operator Q_0 on (psi, y = dSigma, y+ = dSigma+) is built as P_ext H_ext with
P_ext = P (+) J (058's antibracket P = om^{-1} diag((-1)^deg), J the (y, y+) pair), and
H_ext the graded-symmetric extended Hessian: the psi block P^{-1} T^cub (T^(k) with its
field-antifield block replaced by the cubic action's, R66), the classical cross blocks
H_{Sigma Psi}, H_{Sigma Sigma} of 060 (1.2)-(1.4) with the same overall sign as the psi
classical block, and the (Sigma+, c) entry fixed by the linearised flat law
s y = Sigma_*' s x. No constant is fitted from nilpotency.

Checks (node IDs of record 067):
  C1-sym       H_ext is graded symmetric in the same pattern as P^{-1} T (even-even symmetric,
               odd-odd antisymmetric).
  C1-blocks    the field block of T^cub equals Q + g l_2(Psi_0) + g^2/3 L_3(Sigma_0) (R66:
               one third of T_2(P_0) on fields), and T^cub off the field block equals T^(k).
  C4-T3        T_3 is the g^3 Taylor coefficient of T_psi (slope 4 of the remainder).
  C2-order     |Q_0^2| = O(g^{k+1}) (log-slope between g and g/2), and the psi block alone
               |T^cub 2| = O(g^2) (R66's non-nilpotency), and off the EOM O(g).
  C3-canonical L_ext preserves P_ext.
  C3-decouple  L Q_0 L^{-1} is block diagonal, with blocks T^eff and the pair
               (y' -> 0, y+ -> -g^2/12 K y') exactly; T^eff = T^(2) exactly at k=2.
  C4-k3-R38    at k=3, T^eff - T^(3) = O(g^3), not O(g^4): this model has ker V4 != 0 (dim 211)
               and a generic V5, so R17's double collapse fails at g^3 (R38 violated); the joint
               operator inherits that O(g^3) defect (C2-order at k=3 expects 3, T^(3) itself 4).
  C3-coh       rank/kernel counts: rank Q_0 = rank T^(k) + dim S, ker Q_0 = ker T^(k) + dim S,
               so h(Q_0) = h(T^(k)) (h = dim - 2 rank for an operator nilpotent to the order
               tested), with the singular-value gap printed; h(T^(k)) at the MC point equals the
               cohomology of the deformed parent (8 dim End H(W, D')^2 ... printed as anchor).
  C3-Kbreak    keeping ker V_4 directions in S (K singular, R67's locus): the pair does not
               decouple, h(Q_0) = h(T) + 2 dim ker.
  Break legs: coefficient 1 instead of 1/3 in the cubic field block (T^eff != T^(k): the
  exchange over-counts l3; the decoupling itself is structural and survives); y-coupling
  dropped (O(g^2) defect); off-EOM background (O(g^2) = g x residual).

Not verified: the string-vertex statements (finite model only); the O(g^4) nilpotency of the
joint operator at k=3 (the model violates R38, see C4-k3-R38); 40-digit arithmetic is not
used (float with printed singular-value gaps; slopes confirmed down to g = 0.0025 in a
scratch run for the k=2 quantities). R66's O(g^2) block defect is O(g^3) on the MC family
used here ({T0, T2(P0)|blk} = O(g): the Jacobiator vanishes on the family's leading term).
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import numpy as np

failures: list[str] = []
npass = 0


def report(name: str, ok: bool, detail: str = "") -> None:
    """Print a labelled PASS/FAIL line and record failures."""
    global npass
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")
    if ok:
        npass += 1
    else:
        failures.append(name)


def load_mf():
    path = Path(__file__).with_name("verify-mean-field-fluctuations.py")
    spec = importlib.util.spec_from_file_location("mf060", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def slope(f, g1: float, g2: float) -> float:
    return np.log(f(g1) / f(g2)) / np.log(g1 / g2)


class Cubic:
    """The cubic HS theory with Sigma in S = Sym^2 H^1 / ker V_4, on top of an LinfModel."""

    def __init__(self, lm, seed: int):
        self.lm = lm
        rng = np.random.default_rng(seed)
        self.f1, self.f2 = lm.f1, lm.f2
        self.d1 = len(self.f1)
        self.f0 = np.where(lm.kdeg == 0)[0]
        self.f3 = np.where(lm.kdeg == 3)[0]
        self.Om = lm.iota.T @ lm.G @ lm.iota
        self.Om21 = self.Om[np.ix_(self.f2, self.f1)]
        self.P = np.linalg.inv(self.Om) @ np.diag((-1.0) ** lm.kdeg)
        # MC family: D' = (u + g a)(v + g b)^T
        uu, vv = lm.uv
        self.a, self.b = rng.standard_normal(len(uu)), rng.standard_normal(len(vv))
        # Sym^2 basis and Gram matrix of V_4
        d1 = self.d1
        self.pairs = [(a, b) for a in range(d1) for b in range(a, d1)]
        self.w = np.array([2.0 if a != b else 1.0 for (a, b) in self.pairs])
        rows = []
        self.T2E = {}
        for (a, b) in self.pairs:
            Sg = np.zeros((d1, d1))
            Sg[a, b] = Sg[b, a] = 1.0
            T2S = lm.T2_sym(Sg)
            self.T2E[(a, b)] = T2S
            M = 2 * self.Om[np.ix_(self.f1, self.f2)] @ T2S[np.ix_(self.f2, self.f1)]
            rows.append(np.array([M[c, d] for (c, d) in self.pairs]) * self.w)
        self.V4 = np.array(rows)  # Gram matrix on Sym^2 in the E basis
        u_, s_, vt_ = np.linalg.svd(self.V4)
        self.rankV4 = int((s_ > 1e-9 * s_[0]).sum())
        self.U = u_[:, : self.rankV4]  # basis of im V_4 = S
        self.Uker = u_[:, self.rankV4 :]
        self.VS = self.U.T @ self.V4 @ self.U

    # ---- background
    def psi0(self, g: float):
        lm = self.lm
        uu, vv = lm.uv
        Dp = np.zeros_like(lm.D)
        rows = [i for i in range(lm.D.shape[0]) if lm.D[i].any() or True]
        # rank-one differential from degree 0 to degree 1 (same layout as rank1_differential)
        m = lm.D.shape[0]
        wdeg = self._wdeg
        r_ = [i for i in range(m) if wdeg[i] == 1]
        c_ = [j for j in range(m) if wdeg[j] == 0]
        Dp[np.ix_(r_, c_)] = np.outer(uu + g * self.a, vv + g * self.b)
        Phi0 = (lm.hat(Dp) - lm.hat(lm.D)) / g
        return lm.p @ Phi0, Phi0

    def cvec(self, x, y):
        """Coordinates of x (.) y (symmetrised) in the E basis."""
        return np.array([0.5 * (x[a] * y[b] + x[b] * y[a]) if a != b else x[a] * y[a]
                         for (a, b) in self.pairs])

    def Jmap(self, psi0f):
        """J_{Psi0}: x -> c(Psi0 (.) x), a (dim Sym^2) x d1 matrix."""
        return np.column_stack([self.cvec(psi0f, np.eye(self.d1)[c]) for c in range(self.d1)])

    def V4_form(self, Sig):
        """V_4(Sig, x, y) as a d1 x d1 matrix, Sig a symmetric d1 x d1 matrix."""
        T2S = self.lm.T2_sym(Sig)
        return 2 * self.Om[np.ix_(self.f1, self.f2)] @ T2S[np.ix_(self.f2, self.f1)]

    def sig_to_mat(self, c):
        """E-basis coordinates -> symmetric d1 x d1 matrix."""
        S = np.zeros((self.d1, self.d1))
        for k_, (a, b) in enumerate(self.pairs):
            S[a, b] = S[b, a] = c[k_]
        return S

    # ---- T_3 from the HPL (g^3 coefficient of T_psi)
    def T3(self, psi):
        lm = self.lm
        P0 = lm.iota @ psi
        P1 = -lm.hpp @ lm.mul(P0, P0)
        P2 = -lm.hpp @ (lm.mul(P0, P1) + lm.mul(P1, P0))
        A0, A1, A2 = lm.ad(P0), lm.ad(P1), lm.ad(P2)
        h = lm.hpp
        return lm.p @ (A2 - A1 @ h @ A0 - A0 @ h @ A1 + A0 @ h @ A0 @ h @ A0) @ lm.iota

    def T3_tri(self, u, v, w):
        """Symmetric trilinear polarisation of the cubic T3 (inclusion-exclusion, exact)."""
        T = self.T3
        return (T(u + v + w) - T(u + v) - T(u + w) - T(v + w) + T(u) + T(v) + T(w)) / 6.0

    def V5_tensor(self):
        """V_abcde = omega(e_c, l4(e_a,e_b,e_d) e_e) on the field sector, cached (totally symmetric)."""
        if hasattr(self, "_V5"):
            return self._V5
        nk, d1, f1, f2 = self.lm.nk, self.d1, self.f1, self.f2
        E = np.eye(nk)
        ea = [E[f1[c]] for c in range(d1)]
        Om12 = self.Om[np.ix_(f1, f2)]
        V5 = np.zeros((d1,) * 5)
        for a in range(d1):
            for b in range(a, d1):
                for d in range(b, d1):
                    M = 6.0 * Om12 @ self.T3_tri(ea[a], ea[b], ea[d])[np.ix_(f2, f1)]  # [c, e]
                    for (p, q, r) in {(a, b, d), (a, d, b), (b, a, d), (b, d, a), (d, a, b), (d, b, a)}:
                        V5[p, q, :, r, :] = M
        self._V5 = V5
        # total symmetry check (c <-> e, and a <-> c) recorded for the report
        self._V5_sym = max(np.max(np.abs(V5 - V5.transpose(0, 1, 4, 3, 2))),
                           np.max(np.abs(V5 - V5.transpose(2, 1, 0, 3, 4))))
        return V5

    def Tk(self, psi, g: float, k: int):
        lm = self.lm
        T = lm.T0() + g * lm.T1(psi) + g**2 * lm.T2(psi)
        if k == 3:
            T = T + g**3 * self.T3(psi)
        return T


def build_operator(cb: Cubic, g: float, k: int, coef: float = 1.0 / 3.0,
                   keep_kernel: bool = False, drop_y_coupling: bool = False,
                   psi_shift=None):
    """Assemble Q_0 = P_ext H_ext on (psi, y, y+) and the canonical L_ext; return dict."""
    lm = cb.lm
    f1, f2, f0, f3 = cb.f1, cb.f2, cb.f0, cb.f3
    nk, d1 = lm.nk, cb.d1
    psi0, Phi0 = cb.psi0(g)
    if psi_shift is not None:
        psi0 = psi0 + psi_shift
    x0 = psi0[f1]
    Ub = np.column_stack([cb.U, cb.Uker]) if keep_kernel else cb.U
    ns = Ub.shape[1]
    VS = Ub.T @ cb.V4 @ Ub
    J = cb.Jmap(x0)  # Sym^2 x d1
    cP0 = cb.cvec(x0, x0)
    # classical blocks (060 (1.2)-(1.4)); at k=3 with K = V4 - g/5 V5(.,.,Psi0)
    if k == 2:
        K = VS.copy()
        rhs = Ub.T @ cb.V4 @ cP0  # u = V4(., P0)
        sig = np.linalg.solve(K, rhs) if not keep_kernel else np.linalg.lstsq(K, rhs, rcond=None)[0]
        Sig0 = cb.sig_to_mat(Ub @ sig)
        HSP = (g**2 / 6.0) * Ub.T @ cb.V4 @ J  # ns x d1
        HSS = -(g**2 / 12.0) * K
        HPP_extra = (g**2 / 6.0) * cb.V4_form(Sig0)  # the Sigma_0 term of H_PsiPsi
        V5_Sig0 = None
    else:
        # V5 as the totally symmetric 5-tensor V_abcde = omega(e_c, l4(e_a,e_b,e_d) e_e) on the
        # field sector (cached once; l4(u,v,w,.) = 6 T3_tri(u,v,w), C4), then
        # K = V4 - g/5 V5(.,.,Psi0) and H_SP's V5(y, Sigma0, x) by contraction.
        V5 = cb.V5_tensor()
        V5P = np.einsum("abcde,e->abcd", V5, x0)  # V5(a,b,c,d,Psi0)
        wab = cb.w
        Gram5 = np.array([[wab[i] * wab[j] * V5P[a, b, c, d] for j, (c, d) in enumerate(cb.pairs)]
                          for i, (a, b) in enumerate(cb.pairs)])
        K = VS - (g / 5.0) * Ub.T @ Gram5 @ Ub
        rhs = Ub.T @ cb.V4 @ cP0
        sig = np.linalg.solve(K, rhs)
        Sig0 = cb.sig_to_mat(Ub @ sig)
        V5Sx = np.einsum("abcde,cd->abe", V5, Sig0)  # V5(a,b,Sigma0,x)
        V5S = np.array([wab[i] * V5Sx[a, b] for i, (a, b) in enumerate(cb.pairs)])
        HSP = (g**2 / 6.0) * Ub.T @ cb.V4 @ J + (g**3 / 60.0) * Ub.T @ V5S
        HSS = -(g**2 / 12.0) * K
        HPP_extra = (g**2 / 6.0) * cb.V4_form(Sig0)
        V5_Sig0 = V5S
    # psi-sector: T^cub = T^(k) with the field block replaced
    Tk = cb.Tk(psi0, g, k)
    Tcub = Tk.copy()
    blk = np.ix_(f2, f1)
    T2P = lm.T2_sym(np.outer(x0, x0))
    # field block of T^(k): T0 + g T1 + g^2 T2(P0) [+ g^3 T3]; cubic: replace g^2 T2(P0) by coef*g^2*T2sym(Sig0)*...
    # in R66's form: Q + g l2(Psi0) + (g^2/3) L3(Sigma0) = ... + (g^2/3) T2sym(Sigma0) (T2sym = L3 polarised)
    Tcub[blk] = Tk[blk] - g**2 * T2P[blk] + coef * g**2 * lm.T2_sym(Sig0)[blk]  # (1.3): g^2/3 L_3(Sigma_0), T2_sym = L_3
    if k == 3:  # the V5 term of H_PsiPsi: none (060 (1.2)); but T3 on the field block is
        # not part of the cubic action's Psi block: remove it
        Tcub[blk] = Tcub[blk] - g**3 * cb.T3(psi0)[blk]
    Hpsi = np.linalg.inv(cb.P) @ Tcub
    # extended Hessian
    N = nk + 2 * ns
    H = np.zeros((N, N))
    H[:nk, :nk] = Hpsi
    iy = slice(nk, nk + ns)
    iyp = slice(nk + ns, N)
    if not drop_y_coupling:
        H[iy, f1] = -HSP
        H[np.ix_(f1, range(nk, nk + ns))] = -HSP.T
    H[iy, iy] = -HSS
    Sstar = -np.linalg.solve(HSS, HSP) if not keep_kernel else -np.linalg.lstsq(HSS, HSP, rcond=None)[0]
    D = Tk[np.ix_(f1, f0)]  # ghost -> field
    SD = Sstar @ D
    H[np.ix_(range(nk + ns, N), f0)] = SD
    H[np.ix_(f0, range(nk + ns, N))] = -SD.T
    Pext = np.zeros((N, N))
    Pext[:nk, :nk] = cb.P
    Pext[iy, iyp] = np.eye(ns)
    Pext[iyp, iy] = -np.eye(ns)
    Q0 = Pext @ H
    # canonical L: y' = y - Sstar x ; psi'_f2 = psi_f2 + Om21^{-1} Sstar^T y+
    L = np.eye(N)
    L[np.ix_(range(nk, nk + ns), f1)] = -Sstar
    L[np.ix_(f2, range(nk + ns, N))] = np.linalg.inv(cb.Om[np.ix_(f1, f2)]) @ Sstar.T  # (3.2): K = Om_12^{-1} Sstar^T
    return dict(Q0=Q0, H=H, Pext=Pext, L=L, Tk=Tk, Tcub=Tcub, nk=nk, ns=ns, K=K, HSS=HSS,
                HSP=HSP, Sstar=Sstar, psi0=psi0, Sig0=Sig0, T2P=T2P, D=D, VS=VS, Ub=Ub,
                x0=x0, g=g)


def graded_sym_defect(H, par):
    """max |H_ab - eps_ab H_ba| with eps = +1 (even,even), -1 (odd,odd)."""
    n = len(par)
    E = np.array([[(-1.0) ** (par[a] * par[b]) if par[a] == par[b] else 0.0 for b in range(n)]
                  for a in range(n)])
    mixed = np.array([[1.0 if par[a] != par[b] else 0.0 for b in range(n)] for a in range(n)])
    return np.max(np.abs(H - E * H.T)), np.max(np.abs(H * mixed))


def rank_gap(M, tol_hi=1e-6):
    s = np.linalg.svd(M, compute_uv=False)
    r = int((s > tol_hi).sum())
    gap = (s[r - 1], s[r] if r < len(s) else 0.0)
    return r, gap


def run(seed: int, wdeg: list[int], k: int) -> None:
    mf = load_mf()
    lm = mf.LinfModel(seed, wdeg, (1,), parent="T3")
    cb = Cubic(lm, 100 + seed)
    cb._wdeg = wdeg
    nk, d1 = lm.nk, cb.d1
    print(f"\n=== seed {seed}, W {wdeg}, k = {k}: retract dim {nk}, dim H^1-sector {d1}, "
          f"Sym^2 {len(cb.pairs)}, rank V4 {cb.rankV4} (dim S), ker V4 {len(cb.pairs) - cb.rankV4}")
    par = [int((1 - d) % 2) for d in lm.kdeg]
    # MC family sanity
    for g in (0.04, 0.02):
        psi0, Phi0 = cb.psi0(g)
        mc = np.max(np.abs(lm.Q @ Phi0 + g * lm.mul(Phi0, Phi0)))
        Fh = np.max(np.abs(lm.F(psi0, g)))
        fix = np.max(np.abs(lm.Phi(psi0, g) - Phi0))
        report(f"C4-MC seed {seed} g={g}", mc < 1e-12 and Fh < 1e-9 and fix < 1e-9,
               f"parent MC {mc:.1e}, transferred EOM {Fh:.1e}, fixed point {fix:.1e}, |psi0| = {np.linalg.norm(psi0):.3f}")
    if k == 3:
        cb.V5_tensor()
        report(f"C4-V5sym seed {seed}", cb._V5_sym < 1e-9, f"V5 from T3 totally symmetric (C4 cyclicity): defect {cb._V5_sym:.1e}")
        psi0, _ = cb.psi0(0.03)
        def rem(g):
            return np.max(np.abs(lm.T(psi0, g) - cb.Tk(psi0, g, 3)))
        sl = slope(rem, 0.02, 0.01)
        report(f"C4-T3 seed {seed}", abs(sl - 4) < 0.2 and np.max(np.abs(cb.T3(psi0))) > 1e-6,
               f"T - (T0 + g T1 + g^2 T2 + g^3 T3) = O(g^{sl:.2f}); |T3| = {np.max(np.abs(cb.T3(psi0))):.2e}")
    g = 0.04
    op = build_operator(cb, g, k)
    N = op["Q0"].shape[0]
    ns = op["ns"]
    # C1-sym
    par_ext = par + [0] * ns + [1] * ns
    dpsi = graded_sym_defect(np.linalg.inv(cb.P) @ op["Tk"], par)
    dext = graded_sym_defect(op["H"], par_ext)
    report(f"C1-sym seed {seed} k={k}", max(dpsi) < 1e-10 and max(dext) < 1e-10,
           f"P^-1 T^(k) graded-symmetric ({dpsi[0]:.1e}, mixed {dpsi[1]:.1e}); H_ext ({dext[0]:.1e}, mixed {dext[1]:.1e})")
    # C1-blocks: field block of T^cub = T^(k) field block - (2/3) g^2 T2(P0) [+ no T3]; off-block equal
    blk = np.ix_(cb.f2, cb.f1)
    off = op["Tcub"] - op["Tk"]
    off_blk = off.copy()
    off_blk[blk] = 0
    pred2 = -(2.0 / 3.0) * g**2 * op["T2P"][blk]
    R3 = off[blk] - pred2
    if k == 2:
        ok_ = np.max(np.abs(R3)) < 1e-10 * (1 + np.max(np.abs(pred2))) and np.max(np.abs(pred2)) > 1e-6
        info = ""
    else:
        # the g^3 part: (g^2/3) L_3(Sigma_0 - P_0) - g^3 T_3 on the block; = -(4/5) g^3 T_3 when the
        # Sigma-saddle shift is (g/5) V_4^{-1} v exactly (R17 double collapse, i.e. R38 on ker V_4)
        def r3(gg):
            o = build_operator(cb, gg, 3)
            return np.max(np.abs((o["Tcub"] - o["Tk"])[blk] + (2.0 / 3.0) * gg**2 * o["T2P"][blk]))
        s3 = slope(r3, 0.04, 0.02)
        ratio = np.max(np.abs(R3 + 0.8 * g**3 * cb.T3(op["psi0"])[blk])) / np.max(np.abs(g**3 * cb.T3(op["psi0"])[blk]))
        ok_ = abs(s3 - 3) < 0.3
        info = f"; g^3 part = O(g^{s3:.2f}), mismatch to -(4/5) g^3 T3 rel {ratio:.2f} (0 iff R38 holds on ker V4)"
    report(f"C1-blocks seed {seed} k={k}", np.max(np.abs(off_blk)) < 1e-14 and ok_,
           f"T^cub - T^(k) supported on the field block; g^2 part = -(2/3) g^2 T2(P0) exactly "
           f"(|.| = {np.max(np.abs(pred2)):.2e}, R66's one third){info}")
    # C3-canonical
    L, Pext = op["L"], op["Pext"]
    dcan = np.max(np.abs(L @ Pext @ L.T - Pext))
    report(f"C3-canonical seed {seed} k={k}", dcan < 1e-12, f"L P_ext L^T = P_ext ({dcan:.1e})")
    # C3-decouple
    Qp = L @ op["Q0"] @ np.linalg.inv(L)
    nk_ = op["nk"]
    offdiag = Qp.copy()
    offdiag[:nk_, :nk_] = 0
    offdiag[nk_:, nk_:] = 0
    pair = Qp[nk_:, nk_:]
    pair_pred = np.zeros((2 * ns, 2 * ns))
    pair_pred[ns:, :ns] = op["HSS"]  # y+ -> +H_SS y' = -(g^2/12) K y'
    Teff = Qp[:nk_, :nk_]
    dT = np.max(np.abs(Teff - op["Tk"]))
    sc = np.max(np.abs(op["Q0"]))
    report(f"C3-decouple seed {seed} k={k}", np.max(np.abs(offdiag)) / sc < 1e-12 and
           np.max(np.abs(pair - pair_pred)) / sc < 1e-12 and (dT / sc < 1e-12 if k == 2 else True),
           f"L Q0 L^-1 block-diagonal (off-diag {np.max(np.abs(offdiag)) / sc:.1e}); pair = (y'->0, y+ -> -(g^2/12) K y') "
           f"({np.max(np.abs(pair - pair_pred)) / sc:.1e}); |T^eff - T^(k)|/|Q0| = {dT / sc:.1e}")
    if k == 3:
        def dTeff(gg):
            o = build_operator(cb, gg, 3)
            Qq = o["L"] @ o["Q0"] @ np.linalg.inv(o["L"])
            return np.max(np.abs(Qq[:nk_, :nk_] - o["Tk"]))
        sl = slope(dTeff, 0.04, 0.02)
        report(f"C4-k3-R38 seed {seed}", abs(sl - 3) < 0.3 if len(cb.pairs) > cb.rankV4 else abs(sl - 4) < 0.3,
               f"T^eff - T^(3) = O(g^{sl:.2f}): {'4 expected (R65 (1.10)) since ker V4 = 0' if len(cb.pairs) == cb.rankV4 else '3 = the R38 defect (ker V4 != 0, V5 generic: R17 double collapse fails at g^3, 036 C2.2-raw); 4 would need R38'}")
    # C2-order: nilpotency
    def nil(gg, **kw):
        o = build_operator(cb, gg, k, **kw)
        return np.max(np.abs(o["Q0"] @ o["Q0"]))
    def nil_psi(gg):
        o = build_operator(cb, gg, k)
        return np.max(np.abs(o["Tcub"] @ o["Tcub"]))
    def nil_Tk(gg):
        o = build_operator(cb, gg, k)
        return np.max(np.abs(o["Tk"] @ o["Tk"]))
    s_full, s_psi, s_Tk = slope(nil, 0.04, 0.02), slope(nil_psi, 0.04, 0.02), slope(nil_Tk, 0.04, 0.02)
    # R66's O(g^2) defect of the Psi block is {T0, X}, X = (2/3) T2(P0) on the field block:
    # the Jacobiator of l2 on (Psi0, Psi0, .) paired with the ghosts (060 (2.6)); it may vanish
    # in a given model, in which case the block's defect starts at O(g^3).
    def jacn(gg):
        o = build_operator(cb, gg, k)
        X = np.zeros_like(o["T2P"]); X[blk] = o["T2P"][blk]
        return np.max(np.abs(lm.T0() @ X + X @ lm.T0())) / np.max(np.abs(X))
    s_jac = slope(jacn, 0.04, 0.02)
    jac = jacn(0.04)
    # The block's O(g^2) defect is -(2/3){T0, X}; if {T0, X} = O(g) on the MC family (the
    # Jacobiator vanishes on the leading term), the block's defect is O(g^3): same order as
    # the k=2 truncation error, one order below the k=3 joint operator (R66 by order at k=3).
    psi_ok = abs(s_psi - (2 + min(round(s_jac), 1))) < 0.3 if k == 2 else abs(s_psi - 3) < 0.3
    r38 = (k == 3 and len(cb.pairs) > cb.rankV4)
    exp_full = 3 if r38 else k + 1
    def nil_eff(gg):
        o = build_operator(cb, gg, k)
        Qq = o["L"] @ o["Q0"] @ np.linalg.inv(o["L"])
        return np.max(np.abs(Qq[:nk_, :nk_] @ Qq[:nk_, :nk_]))
    s_eff = slope(nil_eff, 0.04, 0.02)
    report(f"C2-order seed {seed} k={k}", abs(s_full - exp_full) < 0.3 and abs(s_Tk - (k + 1)) < 0.3 and psi_ok
           and abs(s_eff - exp_full) < 0.3,
           f"|Q0^2| = O(g^{s_full:.2f}) [expected {exp_full}{' = the R38 defect of T^eff, not the pair' if r38 else ''}]; "
           f"|(T^eff)^2| = O(g^{s_eff:.2f}); |T^(k)2| = O(g^{s_Tk:.2f}) [expected {k + 1}]; "
           f"Psi block alone |T^cub 2| = O(g^{s_psi:.2f}) [R66: 2 + order of |{{T0, T2(P0)|blk}}|/|T2(P0)|blk| "
           f"= {jac:.1e} = O(g^{s_jac:.2f}) on this MC family]; values at g=0.04: {nil(0.04):.2e}, {nil_Tk(0.04):.2e}, {nil_psi(0.04):.2e}")
    rng = np.random.default_rng(seed + 7)
    # off-shell shift: among 6 random field directions take the one with the largest O(g)
    # residual (Q = 0 on the retained field sector, so the residual starts at O(g))
    cands = []
    for _ in range(6):
        e_ = np.zeros(nk)
        e_[cb.f1] = 0.3 * rng.standard_normal(d1)
        cands.append((np.max(np.abs(lm.F(cb.psi0(0.005)[0] + e_, 0.005))) / 0.005, e_))
    eta = max(cands, key=lambda t: t[0])[1]
    def resid(gg):
        return np.max(np.abs(lm.F(cb.psi0(gg)[0] + eta, gg)))
    s_res = slope(resid, 0.04, 0.02)
    s_off = slope(lambda gg: nil(gg, psi_shift=eta), 0.04, 0.02)
    v3 = np.max(np.abs(lm.T1(op["psi0"])[blk]))
    report(f"C2-break-offshell seed {seed} k={k}", s_off < k + 0.5,
           f"background off the EOM: |Q0^2| = O(g^{s_off:.2f}) = g x residual O(g^{s_res:.2f}) "
           f"(Q = 0 on the retained field sector, so the residual is O(g) unless l2 vanishes there: "
           f"|T1(psi0)| on fields = {v3:.1e}); not O(g^{k + 1})")
    s_c1 = slope(lambda gg: nil(gg, coef=1.0), 0.04, 0.02)
    o1 = build_operator(cb, g, k, coef=1.0)
    Qp1 = o1["L"] @ o1["Q0"] @ np.linalg.inv(o1["L"])
    dT1 = np.max(np.abs(Qp1[:nk_, :nk_] - o1["Tk"])) / sc
    report(f"C3-break-coef seed {seed} k={k}", dT1 > 1e-6,
           f"coefficient 1 instead of 1/3 in the Psi block: T^eff != T^(k) (rel {dT1:.1e}: the exchange "
           f"over-counts the l3 part); |Q0^2| = O(g^{s_c1:.2f})")
    s_ny = slope(lambda gg: nil(gg, drop_y_coupling=True), 0.04, 0.02)
    report(f"C3-break-coupling seed {seed} k={k}", s_ny < 2.5,
           f"delta-Sigma coupling dropped: |Q0^2| = O(g^{s_ny:.2f})")
    # C3-coh: rank counts
    for gg in (0.04, 0.02):
        o = build_operator(cb, gg, k)
        tol = 5 * o["g"] ** exp_full  # the nilpotency order actually established (3 at k=3 without R38)
        rQ, gQ = rank_gap(o["Q0"], tol)
        rT, gT = rank_gap(o["Tk"], tol)
        hQ, hT = o["Q0"].shape[0] - 2 * rQ, nk - 2 * rT
        report(f"C3-coh seed {seed} k={k} g={gg}", rQ == rT + o["ns"] and hQ == hT and gQ[0] > 10 * gQ[1] and gT[0] > 10 * gT[1],
               f"rank Q0 = {rQ} = rank T^(k) + dim S = {rT} + {o['ns']}; h(Q0) = {hQ} = h(T^(k)) = {hT}; "
               f"sv gaps Q0 {gQ[0]:.1e}/{gQ[1]:.1e}, T {gT[0]:.1e}/{gT[1]:.1e} (threshold {tol:.1e})")
    # anchor: cohomology of the exact T at the MC point (untruncated), and parent count
    o = build_operator(cb, 0.04, k)
    Tex = lm.T(o["psi0"], 0.04)
    rE, gE = rank_gap(Tex, 1e-8)
    print(f"    anchor: exact T_psi0 (untruncated): h = {nk - 2 * rE} (gap {gE[0]:.1e}/{gE[1]:.1e}); "
          f"parent prediction 8 * dim End H(W,D') = 8 * (dim W - 2)^2 = {8 * (len(wdeg) - 2) ** 2}")
    # C3-Kbreak: keep ker V4 in S
    if len(cb.pairs) > cb.rankV4 and k == 2:  # at k=3 the g V5 term lifts ker V4 partially: no clean count
        ok = build_operator(cb, 0.04, k, keep_kernel=True)
        nker = len(cb.pairs) - cb.rankV4
        tol = 5 * 0.04 ** (k + 1)
        rQ, gQ = rank_gap(ok["Q0"], tol)
        rT, gT = rank_gap(ok["Tk"], tol)
        hQ, hT = ok["Q0"].shape[0] - 2 * rQ, nk - 2 * rT
        report(f"C3-Kbreak seed {seed} k={k}", hQ == hT + 2 * nker,
               f"ker V4 kept in S (K singular, dim ker {nker}): h(Q0) = {hQ} = h(T) + 2 dim ker = {hT} + {2 * nker}: "
               f"the pair does not decouple")


if __name__ == "__main__":
    print("seeds: model 21, 22 (LinfModel); Cubic 121, 122; eta 28, 29")
    if "--only-k3" not in sys.argv:
        for seed in (21, 22, 23):
            run(seed, [0, 0, 1, 1], 2)
        run(21, [0, 0, 0, 1, 1], 2)
    if "--no-k3" not in sys.argv:
        run(21, [0, 0, 1, 1], 3)
        run(22, [0, 0, 1, 1], 3)
    print(f"\nSUMMARY: {npass} PASS, {len(failures)} FAIL" + (f": {failures}" if failures else ""))
    sys.exit(1 if failures else 0)
