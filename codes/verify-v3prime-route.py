"""Companion script for agent/derivations/032-v3prime-route-feasibility.md (Task 14a).

Part 1: coordinate-extension precondition for Harold's V3' maps (disc-overlap test).
Part 2: the covering map (6.1): per-channel regions, gap and overlap in M'_x.
Part 3 (14b): the operator identity (6.2) on shell — tachyon integrand, (s,theta) quadrature
        with the plumbing Jacobian vs direct integration over M'_x; break legs on the Jacobian
        power and on a constant sigma.
Part 4 (14d, rewritten after critic 032): the seam question with the coordinate phases quotiented
        out — first-order moduli agree on the S_3 seam (reflection R = g_t o conj, checked in closed
        form), second-order / disc-image mismatch O(1) on every admissible seam; ray scan; break legs.

Verified: closed-form sigma_max against numeric disc tangency; disjointness of the
Feynman regions; gap/overlap numbers of the cross-ratio sweep; star-shapedness of the
S_3-symmetric seam in log-polar q coordinates; transported coordinates exactly Moebius;
first-order (modulus) continuity on the S_3 seam and O(1) second-order / disc-image mismatch on
every admissible seam (part 4).  The seam integral (5.1') itself is NOT evaluated.  Not verified: the CFT-level
sewing identity (4.5) itself (argued in 032 §4.2, tested only through its on-shell consequence),
anything off shell, or the sewability of five-point composites.
Each check prints PASS/FAIL; break legs must FAIL; exit code nonzero on unexpected outcome.
"""
import sys
import numpy as np

SEED = 20260914
rng = np.random.default_rng(SEED)
print(f"seed = {SEED}")
RESULTS = []


def check(name, ok, expect=True):
    tag = "PASS" if ok == expect else "FAIL"
    RESULTS.append(tag == "PASS")
    print(f"[{tag}] {name}" + ("" if expect else "  (break leg: expected FAIL, got FAIL)" if ok == expect else ""))


# ---- Part 1: coordinate-extension precondition -------------------------------
# V3' maps (Harold, hb_4pt.tex): f0(w)=w/(a w+g), finf(w)=(a w+g)/w, f1(w)=(2b-w)/(2b+w).

def f0(w, a, g): return w / (a * w + g)
def finf(w, a, g): return (a * w + g) / w
def f1(w, b): return (2 * b - w) / (2 * b + w)
def f1inv(z, b): return 2 * b * (1 - z) / (1 + z)


def gdisc(F, r=1.0):
    """Generalized disc = image of {|w|<=r} under a Moebius map F (numeric).
    Returns (centre, radius, inside) with inside=True if the image is the interior."""
    pts = F(r * np.exp(1j * np.array([0.3, 2.1, 4.4])))
    # circumcentre of three points
    z1, z2, z3 = pts
    w = (z3 - z1) / (z2 - z1)
    c = z1 + (z2 - z1) * (w - abs(w) ** 2) / (2j * w.imag)
    rad = abs(z1 - c)
    inside = abs(F(1e-9 * r) - c) < rad  # puncture image (may be infinite -> exterior)
    return c, rad, inside


def disjoint(d1, d2):
    (c1, r1, i1), (c2, r2, i2) = d1, d2
    d = abs(c1 - c2)
    tol = 1e-9  # tangent discs count as disjoint
    if i1 and i2: return d >= r1 + r2 - tol
    if i1 and not i2: return d + r1 <= r2 + tol
    if i2 and not i1: return d + r2 <= r1 + tol
    return False  # two exteriors always meet at infinity


def sigma_max_strict(a, g, b):
    """Largest r such that f1({|w|<=r}) is disjoint from f0(D) and finf(D); returns ln r."""
    lo, hi = 1e-9, 2 * b * (1 - 1e-9)
    d0, dinf = gdisc(lambda w: f0(w, a, g)), gdisc(lambda w: finf(w, a, g))
    ok = lambda r: disjoint(gdisc(lambda w: f1(w, b), r), d0) and disjoint(gdisc(lambda w: f1(w, b), r), dinf)
    if not ok(lo): return -np.inf
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if ok(mid): lo = mid
        else: hi = mid
    return np.log(lo)


def composite_discs(q, a, g, b):
    """Four coordinate discs on the s-channel composite: sphere 2 glued into sphere 1's
    special leg by w1 w2 = q.  Legs 3,4 are f0,finf of sphere 2 transported by
    z = f1(q / f1inv(z')).  Valid formula for any q (continuation to |q|>1)."""
    T = lambda zp: f1(q / f1inv(zp, b), b)
    return [gdisc(lambda w: f0(w, a, g)), gdisc(lambda w: finf(w, a, g)),
            gdisc(lambda w: T(f0(w, a, g))), gdisc(lambda w: T(finf(w, a, g)))]


def composite_ok(q, a, g, b):
    D = composite_discs(q, a, g, b)
    return all(disjoint(D[i], D[j]) for i in range(4) for j in range(i + 1, 4))


def sigma_max_composite(theta, a, g, b, smax=3.0, n=600):
    """Largest sigma in [0,smax] with the four composite discs disjoint at q=e^{sigma+i theta}."""
    sig = np.linspace(0, smax, n)
    good = [composite_ok(np.exp(s + 1j * theta), a, g, b) for s in sig]
    if not good[0]: return -np.inf
    k = next((i for i, gd in enumerate(good) if not gd), n)
    return sig[k - 1]


B = 1.5
G_SAT = (2 * B + 1) / (2 * B - 1)   # gamma' saturating f0-f1 non-overlap at alpha'=0
print("\n== Part 1: precondition ==")
# (1a) reproduce Harold's non-overlap conditions at alpha'=0: saturation exactly at gamma'=G_SAT
check("P1a  alpha'=0: f0(D),f1(D) tangent at gamma'=(2b+1)/(2b-1)",
      abs(sigma_max_strict(0.0, G_SAT, B)) < 1e-6)
check("P1a' alpha'=0, gamma' slightly below saturation: discs overlap already at r=1",
      sigma_max_strict(0.0, 0.98 * G_SAT, B) < 0)
# (1b) closed form sigma_max = ln[2b (g-1)/(g+1)] at alpha'=0, against the bisection
for gfac in (1.0, 1.1, 2.0):
    g = gfac * G_SAT
    cf = np.log(2 * B * (g - 1) / (g + 1))
    num = sigma_max_strict(0.0, g, B)
    print(f"   alpha'=0 gamma'={g:.4f}: sigma_max strict = {num:.6f}  closed form {cf:.6f}")
    check(f"P1b  closed-form sigma_max at gamma'={g:.3f}", abs(cf - num) < 1e-6)
# break leg: a wrong closed form (drop the 2b) must fail
g = 1.1 * G_SAT
check("P1b-break wrong closed form ln[(g-1)/(g+1)]", abs(np.log((g - 1) / (g + 1)) - sigma_max_strict(0.0, g, B)) < 1e-6, expect=False)
# (1c) general (alpha',gamma'): the numeric bound agrees with the analytic tangency inequality
#      |c1(1)-c0| >= rho1(1)+rho0 with c0=-a/(g^2-a^2), rho0=g/(g^2-a^2), c1=(4b^2+1)/(4b^2-1), rho1=4b/(4b^2-1)
#      (independent path: closed-form disc data, not the three-point circumcircle).
def analytic_ok(a, g, b):
    c0, r0 = -a / (g**2 - a**2), g / (g**2 - a**2)
    c1, r1 = (4 * b**2 + 1) / (4 * b**2 - 1), 4 * b / (4 * b**2 - 1)
    return abs(c1 - c0) >= r1 + r0 - 1e-9
smp = [(a, g) for a, g in ((rng.uniform(-3, 3), rng.uniform(1.01, 8)) for _ in range(400)) if g > abs(a) + 0.05][:200]
agree = all(analytic_ok(a, g, B) == (sigma_max_strict(a, g, B) >= -1e-9) for a, g in smp)
check("P1c  numeric r=1 non-overlap == analytic tangency inequality (200 seeded points)", agree)
smp = [(a, g) for a, g in smp if analytic_ok(a, g, B)]
strict = np.array([sigma_max_strict(a, g, B) for a, g in smp])
print(f"   {len(smp)} allowed points: sigma_max strict in [{strict.min():.4f}, {strict.max():.4f}]")
# the f1-f0 and f1-finf tangencies coincide (z -> 1/z symmetry): test on sample via the two one-sided bounds
def one_sided(a, g, b, which):
    d = gdisc(lambda w: f0(w, a, g)) if which == 0 else gdisc(lambda w: finf(w, a, g))
    lo, hi = 1e-9, 2 * b * (1 - 1e-9)
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if disjoint(gdisc(lambda w: f1(w, b), mid), d): lo = mid
        else: hi = mid
    return np.log(lo)
sym = max(abs(one_sided(a, g, B, 0) - one_sided(a, g, B, 1)) for a, g in smp[:10])
check("P1d  f1-f0 and f1-finf extension bounds coincide (z->1/z symmetry)", sym < 1e-6)
# (1e) composite test at |q|=1: legal for all theta iff the V3' cone holds
th = np.linspace(0, 2 * np.pi, 37)[:-1]
check("P1e  composite discs disjoint at |q|=1 for all theta (saturated vertex)",
      all(composite_ok(np.exp(1j * t), 0.0, G_SAT, B) for t in th))
# (1f) composite bound sigma_comp(theta) vs strict bound, saturated and slack vertices
for gfac in (1.0, 1.1, 2.0):
    g = gfac * G_SAT
    sc = np.array([sigma_max_composite(t, 0.0, g, B) for t in th])
    st = sigma_max_strict(0.0, g, B)
    print(f"   gamma'={g:.4f}: sigma_comp(theta) in [{sc.min():.4f},{sc.max():.4f}]  strict {st:.4f}")
    check(f"P1f  composite bound >= strict bound (gamma'={g:.3f})", np.all(sc >= st - 6e-3))
    if gfac == 1.0:
        check("P1f' saturated vertex: min_theta of the composite bound is 0 (theta-dependent, not identically 0)",
              sc.min() < 6e-3 and sc.max() > 0.5)
        k = int(np.argmin(sc)); print(f"   saturated: composite bound vanishes at theta = {th[k]:.4f}; max {sc.max():.4f} at theta = {th[int(np.argmax(sc))]:.4f}")
# ---- Part 2: the covering map (6.1) -----------------------------------------
# Z_s(q) = (q+4b^2)^2/(16 b^2 q), invariant under q -> 16 b^4/q; injective on |q| < 4 b^2.
def Zs(q, b=B): return (q + 4 * b**2) ** 2 / (16 * b**2 * q)


def q_of_zs(z, b=B):
    """Inverse of Zs on |q| < 4b^2 (branch inside the fixed circle of the involution)."""
    z = np.asarray(z, dtype=complex)
    bb, c = 8 * b**2 - 16 * b**2 * z, 16 * b**4
    disc = np.sqrt(bb**2 - 4 * c)
    q1, q2 = (-bb + disc) / 2, (-bb - disc) / 2
    return np.where(abs(q1) <= abs(q2), q1, q2)


CLOSURE = {"s": lambda z: z, "t": lambda z: z / (z - 1), "u": lambda z: 1 - 1 / z}  # z -> Z_s-equivalent
def q_channel(z, alpha, closure=CLOSURE): return q_of_zs(closure[alpha](z))


print("\n== Part 2: covering map ==")
qs = np.exp(rng.uniform(-2, np.log(4 * B**2) - 0.05, 300) + 1j * rng.uniform(0, 2 * np.pi, 300))
check("C2a  q_of_zs inverts Zs on |q|<4b^2 (300 seeded points)", np.allclose(q_of_zs(Zs(qs)), qs, atol=1e-8))
phi = rng.uniform(0, 2 * np.pi, 50)
check("C2a2 image of |q|=4b^2 is the real segment [0,1]: Zs = cos^2(phi/2)",
      np.allclose(Zs(4 * B**2 * np.exp(1j * phi)), np.cos(phi / 2) ** 2, atol=1e-10))

# grid on the cross-ratio plane (Euclidean area); M'_x is bounded
H = 0.004
xs, ys = np.arange(-3.0, 4.0, H), np.arange(-3.0, 3.0, H)
X, Y = np.meshgrid(xs, ys); Zg = X + 1j * Y
Zg = np.where((abs(Zg) < 1e-9) | (abs(Zg - 1) < 1e-9), Zg + 1e-7, Zg)
absq = {a: abs(q_channel(Zg, a)) for a in "stu"}
inF = {a: absq[a] <= 1 for a in "stu"}
Mx = ~(inF["s"] | inF["t"] | inF["u"])
dA = H * H
AMX = Mx.sum() * dA
print(f"   grid step {H}, box [-3,4]x[-3,3]; |M'_x| = {AMX:.5f} (Euclidean)")
check("C2b  the three Feynman regions F'_a are pairwise disjoint on the grid",
      not np.any((inF["s"] & inF["t"]) | (inF["s"] & inF["u"]) | (inF["t"] & inF["u"])))
check("C2b2 M'_x is bounded: it does not touch the box edge",
      not (Mx[0].any() or Mx[-1].any() or Mx[:, 0].any() or Mx[:, -1].any()))
check("C2b3 real-axis data at b=3/2: Zs(-1)=-16/9, Zs(1)=25/9, F'_t end 25/16 -> 25/9, F'_u end -9/16",
      np.allclose([Zs(-1.0), Zs(1.0)], [-16 / 9, 25 / 9]) and np.isclose(CLOSURE["t"](25 / 16), 25 / 9)
      and np.isclose(1 / (1 - Zs(1.0)), -9 / 16))
check("C2b4 e^{i pi/3} lies in M'_x (all three |q_a| > 1)",
      all(abs(q_channel(np.exp(1j * np.pi / 3), a)) > 1 for a in "stu"))

# constant sigma: gap closes at sigma* = ln max_{M'_x} min_a |q_a|; overlap starts at sigma_ov = ln min_{M'_x} 2nd-smallest |q_a|
stack = np.sort(np.stack([absq[a] for a in "stu"]), axis=0)
sig_star = np.log(stack[0][Mx].max())
sig_ov = np.log(stack[1][Mx].min())
print(f"   constant sigma: gap closes at sigma* = {sig_star:.4f} (|q| = {np.exp(sig_star):.4f});"
      f" overlap starts at sigma_ov = {sig_ov:.4f} (|q| = {np.exp(sig_ov):.4f})")
check("C2c  constant sigma is over-determined: sigma_ov < sigma*", sig_ov < sig_star - 1e-3)
check("C2c2 sigma* is below the precondition ceiling ln 2b' = ln 3 (a slack V3' can reach it)", sig_star < np.log(2 * B))
g_min_star = (1 + np.exp(sig_star) / (2 * B)) / (1 - np.exp(sig_star) / (2 * B))
print(f"   minimal gamma' (alpha'=0) with sigma_max >= sigma*: gamma' >= {g_min_star:.4f}")
k = np.argmax(np.where(Mx, stack[0], -1)); zlast = Zg.flat[k]
print(f"   last point of M'_x to be covered (constant sigma): z = {zlast:.4f}")


def regions(sigma_of_theta, closure=CLOSURE):
    """R_a on the grid: 1 < |q_a| <= exp(sigma(arg q_a))."""
    out = {}
    for a in "stu":
        q = q_channel(Zg, a, closure)
        out[a] = (abs(q) > 1) & (abs(q) <= np.exp(sigma_of_theta(np.angle(q))))
    return out


def report(R, label):
    union = R["s"] | R["t"] | R["u"]
    gap = (Mx & ~union).sum() * dA
    ov = (sum(R[a].sum() for a in "stu") - union.sum()) * dA
    spill = sum((R[a] & (inF["s"] | inF["t"] | inF["u"])).sum() for a in "stu") * dA
    print(f"   {label}: |R_s|={R['s'].sum()*dA:.5f} |R_t|={R['t'].sum()*dA:.5f} |R_u|={R['u'].sum()*dA:.5f}"
          f" gap={gap:.5f} overlap={ov:.5f} spill-into-F'={spill:.5f}  (|M'_x|={AMX:.5f})")
    return gap, ov, spill


gap0, ov0, _ = report(regions(lambda th: sig_star + 0 * th), f"const sigma=sigma*={sig_star:.4f}")
check("C2d  at sigma* the gap is closed (< 20 grid cells)", gap0 < 20 * dA)
check("C2d2 at sigma* the overlap is a finite fraction of |M'_x|", ov0 > 0.05 * AMX)
gap1, ov1, _ = report(regions(lambda th: sig_ov + 0 * th), f"const sigma=sigma_ov={sig_ov:.4f}")
check("C2d3 at sigma_ov there is no overlap but a gap", ov1 < 20 * dA and gap1 > 0.05 * AMX)
report(regions(lambda th: np.log(2 * B) + 0 * th), "const sigma=ln 2b' (precondition ceiling)")
for gfac in (1.1, 2.0):
    g = gfac * G_SAT
    report(regions(lambda th, g=g: np.log(2 * B * (g - 1) / (g + 1)) + 0 * th), f"const sigma=sigma_max(gamma'={g:.2f})")

# S_3-symmetric seam: D_s = {|z|>1, |z-1|>1}; sigma(theta) = first exit of the ray Zs(e^{sigma+i theta}) from D_s
def in_Ds(z): return (abs(z) > 1) & (abs(z - 1) > 1)
th = np.linspace(-np.pi, np.pi, 721)
sg = np.linspace(0, np.log(4 * B**2) - 1e-6, 4000)
sig_seam = np.empty_like(th); star = True
for i, t in enumerate(th):
    inside = in_Ds(Zs(np.exp(sg + 1j * t)))
    k = int(np.argmin(inside)) if not inside.all() else len(sg) - 1
    sig_seam[i] = sg[k - 1] if k > 0 else 0.0
    if inside[k:].any(): star = False  # ray re-enters D_s: seam not a graph over theta
check("C2e  F'_s lies inside D_s (ray starts inside for every theta)", all(in_Ds(Zs(np.exp(1j * t))) for t in th))
check("C2e2 preimage of D_s is star-shaped in q: sigma(theta) single-valued (no re-entry)", star)
print(f"   S_3 seam: sigma(theta) in [{sig_seam.min():.4f}, {sig_seam.max():.4f}];"
      f" min at theta={th[np.argmin(sig_seam)]:.4f}, max at theta={th[np.argmax(sig_seam)]:.4f}")
sig_interp = lambda ang: np.interp(ang, th, sig_seam)
gap2, ov2, spill2 = report(regions(sig_interp), "S_3 seam sigma(theta)")
check("C2f  S_3 seam covers M'_x: gap below 1% of |M'_x|", gap2 < 0.01 * AMX)
check("C2f2 S_3 seam: overlap below 1% of |M'_x|", ov2 < 0.01 * AMX)
check("C2f3 S_3 seam: no spill into the Feynman regions", spill2 < 0.01 * AMX)
check("C2g  the S_3 seam stays below the precondition ceiling ln 2b'", sig_seam.max() < np.log(2 * B))
g_min_seam = (1 + np.exp(sig_seam.max()) / (2 * B)) / (1 - np.exp(sig_seam.max()) / (2 * B))
print(f"   minimal gamma' (alpha'=0) with sigma_max >= max sigma(theta): gamma' >= {g_min_seam:.4f}")
check("C2g2 z -> 1-z symmetry of the s-family: 1 - Zs(q) = Zs(-q)", np.allclose(1 - Zs(qs), Zs(-qs)))
check("C2g3 seam sigma(theta) is pi-periodic (consequence of C2g2 and D_s symmetric)",
      np.allclose(sig_seam, sig_interp(np.angle(np.exp(1j * (th + np.pi)))), atol=2e-3))
# break leg: the inverse closure 1/(1-z) in place of 1-1/z puts R_u around z=1 (on top of R_t): gap must change
bad = dict(CLOSURE); bad["u"] = lambda z: 1 / (1 - z)
gapb, _, _ = report(regions(sig_interp, bad), "BREAK: wrong u-closure 1/(1-z)")
check("C2h-break wrong closure formula leaves the gap unchanged", abs(gapb - gap2) < 1e-6, expect=False)

# ---- Part 3 (14b): the operator identity (6.2) on shell -----------------------
# On shell (four tachyons, generic momenta) both sides of (6.2) are integrals of the same
# coordinate-free function f(Z) = |Z|^{2a} |1-Z|^{2b} (record 032 §4.3): the LHS in the
# (s, theta) plumbing parametrisation with the Jacobian J = |q|^2 |Z_a'(q)|^2 (4.6) over
# 0 < s' <= sigma(theta) per channel; the RHS as the grid integral over M'_x.  The two are
# computed independently (fine (s,theta) quadrature vs the Part-2 grid); the break legs
# perturb the Jacobian power and replace the seam by a constant sigma (gap 20 %).
print("\n== Part 3: operator identity (6.2) on shell ==")


def dZs(q, b=B): return (q + 4 * b**2) * (q - 4 * b**2) / (16 * b**2 * q**2)


INV_CLOSURE = {"s": lambda z: z, "t": lambda z: z / (z - 1), "u": lambda z: 1 / (1 - z)}  # Z_a = g_a(Z_s)
DG = {"s": lambda z: 1 + 0 * z, "t": lambda z: -1 / (z - 1) ** 2, "u": lambda z: 1 / (1 - z) ** 2}

qq = np.exp(rng.uniform(0, 0.88, 200) + 1j * rng.uniform(-np.pi, np.pi, 200))
eps = 1e-6
fd = (Zs(qq + eps) - Zs(qq - eps)) / (2 * eps)
check("C3a  closed-form Z_s'(q) (4.6) against a finite difference on 200 seeded q in the annulus",
      np.allclose(fd, dZs(qq), rtol=1e-6))
for a_ in "tu":
    zz = Zs(qq)
    check(f"C3a2 closure Jacobian g_{a_}' by finite difference", np.allclose(
        (INV_CLOSURE[a_](zz + eps) - INV_CLOSURE[a_](zz - eps)) / (2 * eps), DG[a_](zz), rtol=1e-5))
check("C3a3 inverse closures: g_a(CLOSURE_a(z)) = z on the grid sample",
      all(np.allclose(INV_CLOSURE[a_](CLOSURE[a_](Zs(qq))), Zs(qq)) for a_ in "tu"))


def f_tach(Z, a, b): return abs(Z) ** (2 * a) * abs(1 - Z) ** (2 * b)


def lhs_channel(alpha, sigma_of_theta, a, b, jac_power=2, nth=1440, ns=400):
    """LHS of (6.2), one channel: int dtheta int_0^{sigma(theta)} ds' f(Z_a(q)) J_a(q), q = e^{s'+i theta}."""
    th_m = (np.arange(nth) + 0.5) * 2 * np.pi / nth - np.pi
    tot = 0.0
    for t in th_m:
        smax = sigma_of_theta(t)
        s_m = (np.arange(ns) + 0.5) * smax / ns
        q = np.exp(s_m + 1j * t)
        zs = Zs(q)
        Z = INV_CLOSURE[alpha](zs)
        J = abs(q) ** 2 * abs(DG[alpha](zs) * dZs(q)) ** jac_power
        tot += (f_tach(Z, a, b) * J).sum() * (smax / ns)
    return tot * (2 * np.pi / nth)


def rhs_region(mask, a, b, step=1):
    m = mask[::step, ::step]
    return (f_tach(Zg[::step, ::step][m], a, b)).sum() * dA * step**2


Rseam = regions(sig_interp)
# two generic "momentum points": exponents (a, b) of |Z|^{2a}|1-Z|^{2b}; M'_x avoids 0,1,inf so any exponents converge
for k in range(2):
    a, b = rng.uniform(-1.5, 0.5, 2)
    print(f"   momentum point {k+1}: (a, b) = ({a:.4f}, {b:.4f})")
    L = {al: lhs_channel(al, sig_interp, a, b) for al in "stu"}
    R = {al: rhs_region(Rseam[al], a, b) for al in "stu"}
    lhs, rhs = sum(L.values()), rhs_region(Mx, a, b)
    rhs2 = rhs_region(Mx, a, b, step=2)
    grid_err = abs(rhs - rhs2) / rhs
    print(f"   LHS per channel (s,theta) quadrature: s={L['s']:.5f} t={L['t']:.5f} u={L['u']:.5f}; sum={lhs:.5f}")
    print(f"   RHS grid over R_a: s={R['s']:.5f} t={R['t']:.5f} u={R['u']:.5f}; over M'_x: {rhs:.5f}"
          f" (h vs 2h relative change {grid_err:.2e})")
    print(f"   relative difference (LHS-RHS)/RHS = {(lhs-rhs)/rhs:+.3e}")
    check(f"C3b{k+1} per-channel measure identity: (s,theta) quadrature = grid integral over R_a within 1 %",
          all(abs(L[al] - R[al]) / R[al] < 0.01 for al in "stu"))
    check(f"C3c{k+1} (6.2) on shell: sum_a LHS_a = int_{{M'_x}} f within 1 % (gap 0.09 % + grid error)",
          abs(lhs - rhs) / rhs < 0.01)
    check(f"C3c{k+1}b LHS < RHS by at most the covering gap fraction + grid error (nothing over-counted)",
          (rhs - lhs) / rhs < gap2 / AMX + 5 * grid_err + 2e-3)
    if k == 0:
        lhs_bad = sum(lhs_channel(al, sig_interp, a, b, jac_power=1) for al in "stu")
        print(f"   BREAK: Jacobian power 1 instead of 2: LHS = {lhs_bad:.5f} (rel. diff {(lhs_bad-rhs)/rhs:+.3e})")
        check("C3d-break wrong Jacobian power |Z'|^1 still matches the RHS within 1 %", abs(lhs_bad - rhs) / rhs < 0.01, expect=False)
        lhs_const = sum(lhs_channel(al, lambda t: sig_ov + 0 * t, a, b) for al in "stu")
        print(f"   BREAK: constant sigma_ov instead of the seam: LHS = {lhs_const:.5f} (rel. diff {(lhs_const-rhs)/rhs:+.3e})")
        check("C3e-break constant sigma_ov (20 % gap) still matches the RHS within 1 %", abs(lhs_const - rhs) / rhs < 0.01, expect=False)
        # (l): pi-periodicity of the seam means odd Fourier modes of sigma(theta) vanish
        ft = np.fft.rfft(sig_seam[:-1])
        check("C3f  seam sigma(theta) has no odd Fourier modes (only even L_0^- sourced, 4.1)",
              abs(ft[1::2]).max() < 1e-2 * abs(ft[0]))


# ---- Part 4 (14d, rewritten after critic 032 H4): the seam question with phases quotiented ----
# At a point Z of the s-t seam (|Z-1|=1, Re Z>1/2) the s- and t-composites are the same
# four-punctured sphere (labels 1,2,3,4 at 0,1,inf,Z) with DIFFERENT local coordinates F_i^(s),
# F_i^(t).  Every F_i is a composition of Moebius maps, hence Moebius: it is fixed by
# (F(0), c1=F'(0), c2=F''(0)/2), and its image of the unit disc is a disc.  A coordinate is
# physical only up to w -> e^{i phi} w (acts as e^{i phi L_0^-} = 1 on H_0), so the phase of c1
# is gauge; the invariant data are |c1| (first order, 1 real) and kappa = c2/c1^2 (second order,
# 2 real) per puncture, equivalently the image disc (centre, radius; 3 real).  Count per seam
# point: 4 (first order) + 8 (second order) = 12 real conditions vs 1 unknown sigma(theta).
print("\n== Part 4: seam coordinate mismatch across the s-t seam, phases quotiented ==")
A4, G4 = 0.0, 9.5   # slack vertex (gamma' >= 3.15 symmetric cut / 9.19 one-sided cut; 032 (3.4))
gt_map = lambda z: z / (z - 1)


def s_composite_maps(q, a=A4, g=G4, b=B):
    """Transported coordinates F_i(w) of the s-composite at q, frame (0,1,inf,Z_s(q)), labels
    1,2 on sphere 1 (f0, finf), 3,4 on sphere 2 (T o f0, T o finf); puncture 3 in the chart 1/z."""
    T = lambda zp: f1(q / f1inv(zp, b), b)
    z3 = T(f0(0.0, a, g))                      # = (4b^2-q)/(4b^2+q)
    M = lambda z: z / (z - z3)                 # 0->0, inf->1, z3->inf
    return [lambda w: M(f0(w, a, g)), lambda w: M(finf(w, a, g)),
            lambda w: 1.0 / M(T(f0(w, a, g))), lambda w: M(T(finf(w, a, g)))]


def t_composite_maps(Z, a=A4, g=G4, b=B):
    """t-composite (pairs (13)|(24)): s-type composite at Z_t = g_t(Z) with labels 1'=1, 2'=3,
    3'=2, 4'=4, pulled back by the involution g_t.  Physical 3 (at inf) in the chart 1/z."""
    Zt = gt_map(Z)
    qt = q_of_zs(np.array([Zt]), b)[0]
    Fs = s_composite_maps(qt, a, g, b)         # frame (0,1,inf,Zt), labels 1',2',3',4'
    return [lambda w: gt_map(Fs[0](w)),                 # physical 1 at 0
            lambda w: gt_map(1.0 / Fs[2](w)),           # physical 2 at 1   (3' at inf -> 1)
            lambda w: 1.0 / gt_map(Fs[1](w)),           # physical 3 at inf (2' at 1 -> inf), chart 1/z
            lambda w: gt_map(Fs[3](w))]                 # physical 4 at Z


def mobius(F):
    """Exact (a,b,c,d) of a Moebius map from three sample points (SVD null vector)."""
    ws = np.array([0.31, 0.22j, -0.27 + 0.11j])
    Fw = F(ws)
    Mx = np.stack([ws, np.ones(3), -Fw * ws, -Fw], axis=1)
    return np.linalg.svd(Mx)[2][-1].conj()


def germs(F):
    """(c1, kappa) with c1 = F'(0), kappa = F''(0)/(2 F'(0)^2), from the Moebius coefficients."""
    a, b, c, d = mobius(F)
    det = a * d - b * c
    return det / d**2, -c * d / det


def disc_image(F):
    """Image of the unit disc: (centre, radius); asserts it is an interior disc."""
    c, r, inside = gdisc(F)
    assert inside, "coordinate disc image is an exterior disc — chart error"
    return c, r


def seam_data(Z, b=B, same_side=False, g_t=G4):
    """Per puncture i=1..4: Re m_i (log modulus ratio), Im m_i (phase), Delta kappa_i, and the
    Hausdorff distance between the two image discs divided by the s-disc radius."""
    qs = q_of_zs(np.array([Z]), b)[0]
    Fs = s_composite_maps(qs)
    Ft = s_composite_maps(qs) if same_side else t_composite_maps(Z, g=g_t)
    gs = np.array([germs(F) for F in Fs]); gt_ = np.array([germs(F) for F in Ft])
    m = np.log(gs[:, 0] / gt_[:, 0])
    dk = gs[:, 1] - gt_[:, 1]
    ds = [disc_image(F) for F in Fs]; dt = [disc_image(F) for F in Ft]
    haus = np.array([(abs(cs - ct) + abs(rs - rt)) / rs for (cs, rs), (ct, rt) in zip(ds, dt)])
    return m.real, m.imag, dk, haus


def positions(Z, b=B):
    qs = q_of_zs(np.array([Z]), b)[0]
    Zt = gt_map(Z); qt = q_of_zs(np.array([Zt]), b)[0]
    return Zs(qs, b), gt_map(Zs(qt, b))


phis = np.linspace(-0.9 * np.pi / 3, 0.9 * np.pi / 3, 25)         # seam |Z-1|=1, Re Z>1/2 <=> |phi|<pi/3
seam_pts = 1 + np.exp(1j * phis)
check("C4a  s- and t-composites reproduce the same cross-ratio Z on the seam (positions agree)",
      all(abs(positions(Z)[0] - Z) < 1e-9 and abs(positions(Z)[1] - Z) < 1e-9 for Z in seam_pts))
# (4b) the transported coordinates are Moebius maps: the 3-point fit predicts a 4th point exactly
Zc = 1 + np.exp(1j * 0.4)
ok = True
for F in s_composite_maps(q_of_zs(np.array([Zc]))[0]) + t_composite_maps(Zc):
    a, b_, c, d = mobius(F); w4 = 0.5 * np.exp(1j * 1.3)
    ok &= abs((a * w4 + b_) / (c * w4 + d) - F(w4)) < 1e-10
check("C4b  transported coordinates are exactly Moebius (3-point fit predicts a 4th point to 1e-10)", ok)
# (4c) first order, phases quotiented: the moduli agree on the S_3 seam, the phases are a common rotation
D = [seam_data(Z) for Z in seam_pts]
Rem = np.array([d[0] for d in D]); Imm = np.array([d[1] for d in D])
spread = np.array([abs(np.exp(1j * (im - im[0])) - 1).max() for im in Imm])
print(f"   S_3 seam, 25 pts: max|Re m| = {abs(Rem).max():.2e};  Im m in [{Imm.min():.3f},{Imm.max():.3f}],"
      f" max spread across punctures (mod 2pi) = {spread.max():.2e}")
check("C4c  first-order moduli |F_s'(0)| = |F_t'(0)| at all 4 punctures on the S_3 seam (|Re m| < 1e-6)", abs(Rem).max() < 1e-6)
check("C4c2 the phase mismatch is a common rotation of the four coordinates (spread < 1e-6)", spread.max() < 1e-6)
Rem_p = np.array([seam_data(Z, g_t=G4 * 1.05)[0] for Z in seam_pts])
check("C4c-break perturbed A_1 disc (gamma' x 1.05) in the t-composite only keeps |Re m| < 1e-6",
      abs(Rem_p).max() < 1e-6, expect=False)
print(f"   (perturbed gamma': max|Re m| = {abs(Rem_p).max():.2e})")
# (4g) the reflection identity F_t^i = R o F_s^{pi(i)} o conj, R = g_t o conj, pi = (23), on the seam:
#      c1_t^i = conj(dg_i) conj(c1_s^{pi(i)}) and kappa_t^i = conj(kappa_s^{pi(i)})/dg_i + ddg_i/(2 dg_i^2),
#      with (dg, ddg) the derivatives of g_t in the charts: at 0: (-1,-2); at 1 from inf-chart: (1,2);
#      at inf-chart from 1: (1,-2); at Z: (-1/(Zb-1)^2, 2/(Zb-1)^3).
def reflection_pred(Z, gs, wrong=False):
    Zb = np.conj(Z)
    dg = np.array([-1, 1, 1, -1 / (Zb - 1) ** 2]); ddg = np.array([-2, 2, -2, 2 / (Zb - 1) ** 3])
    if wrong: dg, ddg = np.ones(4), np.zeros(4)           # plain conjugation instead of R
    pi = [0, 2, 1, 3]
    c1 = dg * np.conj(gs[pi, 0]); ka = np.conj(gs[pi, 1]) / dg + ddg / (2 * dg**2)
    return c1, ka
okc1 = okka = okw = True
for Z in seam_pts:
    qs = q_of_zs(np.array([Z]))[0]
    gs = np.array([germs(F) for F in s_composite_maps(qs)]); gt_ = np.array([germs(F) for F in t_composite_maps(Z)])
    c1p, kap = reflection_pred(Z, gs); c1w, kaw = reflection_pred(Z, gs, wrong=True)
    okc1 &= np.allclose(c1p, gt_[:, 0], atol=1e-9); okka &= np.allclose(kap, gt_[:, 1], atol=1e-8)
    okw &= np.allclose(c1w, gt_[:, 0], atol=1e-9)
check("C4g  first-order germs of the t-composite = reflection R=g_t o conj of the s-germs (labels 2<->3)", okc1)
check("C4g2 second-order germs kappa_t = conj(kappa_s)/g' + g''/(2g'^2) (same reflection, per chart)", okka)
check("C4g-break plain conjugation (no g_t) reproduces the t-germs", okw, expect=False)
# (4h) the s-composite's own symmetry |c1_2| = |c1_3| (sphere exchange), needed for C4c at punctures 2,3
okh = all(abs(abs(germs(s_composite_maps(q_of_zs(np.array([Z]))[0])[1])[0]) -
              abs(germs(s_composite_maps(q_of_zs(np.array([Z]))[0])[2])[0])) < 1e-9 for Z in seam_pts)
check("C4h  s-composite: |F_2'(0)| = |F_3'(0)| and |F_1'(0)| = |F_4'(0)| on the seam (sphere-exchange symmetry)",
      okh and all(abs(abs(germs(s_composite_maps(q_of_zs(np.array([Z]))[0])[0])[0]) -
                      abs(germs(s_composite_maps(q_of_zs(np.array([Z]))[0])[3])[0])) < 1e-9 for Z in seam_pts))
# (4k) second order / disc image: the mismatch is O(1) on the S_3 seam, at Z=2 included
DK = np.array([d[2] for d in D]); HS = np.array([d[3] for d in D])
print(f"   S_3 seam: |Delta kappa_i| per puncture, min over pts {abs(DK).min(axis=0)}, max {abs(DK).max(axis=0)}")
print(f"   S_3 seam: relative Hausdorff disc mismatch per puncture, min {HS.min(axis=0)}, max {HS.max(axis=0)}")
_, _, dk2, hs2 = seam_data(2.0 + 0j)
print(f"   Z=2: |Delta kappa| = {abs(dk2)}, Hausdorff/r_s = {hs2}")
check("C4k  second-order mismatch |Delta kappa| > 0.05 at every S_3-seam point and every puncture", abs(DK).min() > 0.05)
check("C4k2 disc-image (Hausdorff/r_s) mismatch > 0.05 at every S_3-seam point and every puncture", HS.min() > 0.05)
check("C4f  at the g_t-fixed seam point Z=2 the discs still differ (Hausdorff/r_s > 0.05)", hs2.min() > 0.05)
_, _, dk0, hs0 = seam_data(seam_pts[5], same_side=True)
check("C4k-break s-composite vs itself shows a second-order/disc mismatch > 0.05", abs(dk0).min() > 0.05 and hs0.min() > 0.05, expect=False)
# (4d) ray scan: along each s-channel ray theta = const, sigma in [0.2,1.2]: the first-order (moduli) mismatch
#      has a zero on the seam; the phase-invariant full mismatch (moduli + kappa) never does.
sig_scan = np.linspace(0.2, 1.2, 201)
th_scan = np.linspace(0.05, np.pi - 0.05, 19)
rows = []
for t in th_scan:
    Zr = Zs(np.exp(sig_scan + 1j * t))
    keep = (abs(Zr - 1) < 1.6) & (abs(Zr - 1) > 0.6) & (Zr.real > 0.5)
    if keep.sum() < 5: continue
    Zr, sg = Zr[keep], sig_scan[keep]
    S = [seam_data(Z) for Z in Zr]
    n1 = np.array([np.linalg.norm(s_[0]) for s_ in S]); nfull = np.array([np.linalg.norm(np.concatenate([s_[0], s_[2].real, s_[2].imag])) for s_ in S])
    k = n1.argmin()
    rows.append((t, sg[k], n1.min(), n1.max(), nfull.min(), abs(abs(Zr[k] - 1) - 1)))
print("   ray theta | sigma at min|Re m| | min|Re m| | max|Re m| | min|(Re m, Dkappa)| | dist of argmin to seam")
for r in rows: print(f"   {r[0]:.3f} | {r[1]:.3f} | {r[2]:.2e} | {r[3]:.3f} | {r[4]:.3f} | {r[5]:.3f}")
check("C4d  first-order (moduli) conditions are solvable on every ray (min_sigma |Re m| < 0.01, at the S_3 seam)",
      max(r[2] for r in rows) < 0.01 and max(r[5] for r in rows) < 0.02)
check("C4d2 but not vacuous: |Re m| reaches > 0.1 on every ray away from the seam", min(r[3] for r in rows) > 0.1)
check("C4d3 the full phase-invariant mismatch (moduli + kappa) has no zero on any ray (min > 0.05)", min(r[4] for r in rows) > 0.05)


if __name__ == "__main__":
    n_fail = RESULTS.count(False)
    print(f"summary: {len(RESULTS) - n_fail}/{len(RESULTS)} checks passed")
    sys.exit(1 if n_fail else 0)
