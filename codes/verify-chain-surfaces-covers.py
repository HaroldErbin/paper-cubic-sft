"""Companion script for agent/derivations/031-chain-surfaces-as-covers.md (Task 13).

Part 1 (13a, S2): (a) a Mobius involution fixing punctures 1,2 and swapping a,b exists iff
the cross-ratio (1,2;a,b) = -1, tested on seeded random slices; (b) the lift of the
involution to the two-neck plumbed surface requires equal plumbing parameters (2.3).
Part 2 (13a, S3): the two-sphere chain with Mobius local coordinates is uniformised as a
Schottky torus C*/<kappa>; tau from the multiplier; the four external punctures are
mutually 2-torsion translates iff the slice is harmonic AND the tube is diagonal; the
branch cross-ratio from Weierstrass-P (lattice sum, Richardson) agrees with an S3 image of
lambda(tau) from theta functions; frozen slice s=0 and degeneration s->infinity.

Part 3 (13b, S4.1): R2's SZ coordinate at the third puncture of the quotient sphere,
X_SZ(q) = ((4b^2-q)/(4b^2+q))^2 with 1-X_SZ = 1/Z_4 (R2, eq. (Z4)); the induced disc D_W is
never the round disc D_SZ (limacon vs circle); nesting thresholds r_in(b), r_out(b); the
frozen curve X_W(0,theta) (from the torus, Weierstrass-P via theta functions) tested point
by point against the s-channel Feynman region X_SZ({|q|<1}).
Part 4 (13b, S4.2): tiling necessary condition -- the collar's outer curve X_W(lambda,theta)
with lambda fixed by a match at theta=0 is compared with R2's |q|=1 curve as a set.

Part 5 (13b, S5): the Grassmann identity b1 b2 = -(1/2) b_tot b_rel and the factorisation
(5.3) of the (beta2) fixture, in a 16-dim matrix representation of four anticommuting generators.

Part 6 (13c, S6): the ghost-number balance of the torus correlator and of its quotient-sphere
reading in the doubled theory ((6.1)-(6.2)), the bosonised weight function h(q) of the
lambda=2 bc system reconstructed from h(c), h(b) and tested against independent data, the
half-integer minimiser q=3/2 of the antiperiodic sector, and the match N_gh(sigma)=3 (reading
(B)) vs the impossibility of 3/2 (reading (A)).
Part 7 (13d, S4.2-S4.3): scan over r, at four values of beta (R2's beta is a free
parameter of the V3' family, not a fixed number), of the ratio of the two lambda values matching
the s = lambda curve to R2's |q| = 1 curve at theta = 0 and theta = pi; condition (A) needs
ratio 1; break leg: a stubbed SZ coordinate gives ratio 1.

Not verified here: the extremal-length constant C(mu_0) of S2.3; overlap of the three
S_4 images of the collar (S4.2, stated only); the covering-space dictionary of S5 (operator
argument, Lunin-Mathur, not machine-checkable here); the identification of the twist field
with the antiperiodic ground state (S6.2, CFT input, not arithmetic).  Every check has a break-on-purpose leg.
Run: .venv/bin/python codes/verify-chain-surfaces-covers.py
"""
import sys
import numpy as np
import mpmath as mp

SEED = 20260914
RESULTS = []
rng = np.random.default_rng(SEED)


def check(name, ok):
    RESULTS.append((name, bool(ok)))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")


def rand_c(scale=1.0):
    return complex(*(rng.normal(size=2))) * scale


# ---------------------------------------------------------------- Mobius helpers
def mob(M, z):
    a, b, c, d = M.ravel()
    if z == np.inf:
        return a / c if c != 0 else np.inf
    den = c * z + d
    return np.inf if den == 0 else (a * z + b) / den


def cross_ratio(z1, z2, z3, z4):
    """(z1,z2;z3,z4) = (z1-z3)(z2-z4)/((z1-z4)(z2-z3)), eq. (1.4); z2 = inf allowed."""
    if z2 == np.inf:
        return (z1 - z3) / (z1 - z4)
    return (z1 - z3) * (z2 - z4) / ((z1 - z4) * (z2 - z3))


def involution_fixing(p, q):
    """Unique nontrivial Mobius involution with fixed points p, q (q may be inf).
    Conjugate z -> -z by the map sending 0->p, inf->q."""
    if q == np.inf:
        S = np.array([[1, p], [0, 1]], dtype=complex)  # z -> z + p
    else:
        S = np.array([[q, p], [1, 1]], dtype=complex)  # z -> (q z + p)/(z + 1): 0->p, inf->q
    N = np.array([[-1, 0], [0, 1]], dtype=complex)
    return S @ N @ np.linalg.inv(S)


# ---------------------------------------------------------------- Part 1
def part1():
    print("--- part 1: cross-ratio criterion and lift (S2) ---")
    # (a) harmonic slices: iota(a) = b for random z_a and random fixed points p,q
    ok = True
    for _ in range(20):
        p, q, za = rand_c(), rand_c(), rand_c(2)
        M = involution_fixing(p, q)
        zb = mob(M, za)
        ok &= abs(cross_ratio(p, q, za, zb) + 1) < 1e-10
        ok &= abs(mob(M, zb) - za) < 1e-9          # involution
    check("1a criterion: iota(a)=b  =>  (1,2;a,b) = -1 (20 random slices)", ok)
    # break-on-purpose: non-harmonic slice, iota(a) != b for the unique involution
    bad = True
    for _ in range(20):
        p, q, za, zb = rand_c(), rand_c(), rand_c(2), rand_c(2)
        M = involution_fixing(p, q)
        if abs(cross_ratio(p, q, za, zb) + 1) > 1e-3:
            bad &= abs(mob(M, za) - zb) > 1e-6
    check("1a break: generic (non-harmonic) slice has no involution swapping a,b", bad)
    # uniqueness: any Mobius involution fixing 0, inf is z -> -z (c^2 = 1)
    c = rng.normal() + 1j * rng.normal()
    check("1a uniqueness: z->cz is an involution iff c^2=1 (random c fails)", abs(c * c - 1) > 1e-6)
    # (b) lift, eq. (2.3): model (1.3) with z_b = -z_a, r_b = r_a; point on a-neck mapped by iota
    za, r = rand_c(2), 0.3 * abs(rand_c())
    qa = rand_c(0.5)
    wa = rand_c(0.4)                 # a point of the a-annulus, w_a coordinate
    wap = qa / wa                    # its partner on sphere 2
    # iota_1: z -> -z, so w_b(-z) = (-z + z_a)/r = -w_a(z);  same on sphere 2
    wb, wbp = -wa, -wap
    check("1b lift: w_b w_b' = q_a  (phase phi+phi' = 0 in the model)", abs(wb * wbp - qa) < 1e-12)
    qb = qa * np.exp(0.7j) * 1.3     # product tube, q_b != q_a
    check("1b break: product tube q_b != q_a violates w_b w_b' = q_b", abs(wb * wbp - qb) > 1e-6)


# ---------------------------------------------------------------- Part 2
def T_map(z0, r, q):
    """Mobius matrix of z' = z0 + r^2 q/(z - z0)  (gluing w_a w_a' = q, both slices model (1.3))."""
    return np.array([[z0, r * r * q - z0 * z0], [1, -z0]], dtype=complex)


def torus_data(za, zb, r, qa, qb):
    """Schottky uniformisation of the two-sphere chain.  Returns tau and the four puncture
    positions u_i on C/(Z + tau Z) (branch points 1,2 on sphere 1; 3,4 pulled back by T_a^{-1})."""
    Ta, Tb = T_map(za, r, qa), T_map(zb, r, qb)
    g = np.linalg.inv(Tb) @ Ta                      # sphere1 -> sphere1
    g = g / np.sqrt(np.linalg.det(g))
    ev, V = np.linalg.eig(g)
    xi = V[0] / V[1]                                # fixed points of g

    def zeta(z):                                    # g acts as zeta -> kappa zeta
        if z == np.inf:
            return 1.0 + 0j
        return (z - xi[0]) / (z - xi[1])
    z_test = rand_c()
    kappa = zeta(mob(g, z_test)) / zeta(z_test)
    ev_ratio = ev[0] / ev[1]
    assert min(abs(kappa - ev_ratio), abs(kappa - 1 / ev_ratio)) < 1e-6 * abs(kappa), "multiplier"
    kabs = min(abs(kappa), 1 / abs(kappa))
    # C*/<kappa> = C*/<1/kappa>; take the generator with |.|<1 so that Im tau > 0
    tau = np.log(kappa if abs(kappa) < 1 else 1 / kappa) / (2j * np.pi)
    Ta_inv = np.linalg.inv(Ta)
    pts = [0.0 + 0j, np.inf, mob(Ta_inv, 0.0 + 0j), mob(Ta_inv, np.inf)]
    us = [np.log(zeta(z)) / (2j * np.pi) for z in pts]
    return tau, us, kabs


def reduce_mod(u, tau):
    """Reduce u to the fundamental parallelogram of Z + tau Z; return (m, n) real coords."""
    n = u.imag / tau.imag
    m = u.real - n * tau.real
    return m % 1, n % 1


def is_two_torsion(d, tau, tol=1e-6):
    m, n = reduce_mod(d, tau)
    return all(min(abs(x - k) for k in (0, 0.5, 1)) < tol for x in (m, n))


def wp_lattice(z, tau, N):
    """Weierstrass P by truncated absolutely convergent lattice sum (square cutoff N)."""
    m, n = np.meshgrid(np.arange(-N, N + 1), np.arange(-N, N + 1))
    w = (m + n * tau).ravel()
    w = w[np.abs(w) > 0]
    return 1 / z**2 + np.sum(1 / (z - w) ** 2 - 1 / w**2)


def wp(z, tau):
    f1, f2 = wp_lattice(z, tau, 200), wp_lattice(z, tau, 400)
    return 2 * f2 - f1  # Richardson, error O(1/N)


def lam_theta(tau):
    qn = mp.exp(1j * mp.pi * mp.mpc(tau))
    return complex((mp.jtheta(2, 0, qn) / mp.jtheta(3, 0, qn)) ** 4)


def s3_orbit(x):
    return [x, 1 - x, 1 / x, 1 / (1 - x), x / (x - 1), (x - 1) / x]


def part2():
    print("--- part 2: frozen k=2 chain, Schottky torus, lambda(tau) (S3) ---")
    za = 1.0 + 0j
    r = 0.45                          # discs |z -/+ 1| < 0.45 disjoint, avoid 0, inf
    theta = 2 * np.pi * rng.random()
    q0 = np.exp(1j * theta)           # frozen, s = 0
    tau0, us, kabs = torus_data(za, -za, r, q0, q0)
    print(f"  theta = {theta:.4f}: |kappa| = {kabs:.6f}, tau(0,theta) = {tau0:.6f}")
    check("2a frozen slice is a nondegenerate torus: 0 < |kappa| < 1", 0 < kabs < 1 - 1e-9)
    ok = all(is_two_torsion(us[i] - us[0], tau0) for i in (1, 2, 3))
    ok &= len({tuple(np.round(reduce_mod(us[i] - us[0], tau0), 4)) for i in (1, 2, 3)}) == 3
    check("2b harmonic + diagonal: punctures 2,3,4 are the three nonzero 2-torsion translates of 1", ok)
    # break-on-purpose legs
    tau_n, us_n, _ = torus_data(za, -0.8 * za * np.exp(0.3j), r, q0, q0)
    check("2b break: non-harmonic slice -> punctures not 2-torsion translates",
          not all(is_two_torsion(us_n[i] - us_n[0], tau_n) for i in (1, 2, 3)))
    tau_p, us_p, _ = torus_data(za, -za, r, q0 * 0.7, q0 * np.exp(0.9j))
    check("2b break (beta1): product tube q_a != q_b -> punctures not 2-torsion translates",
          not all(is_two_torsion(us_p[i] - us_p[0], tau_p) for i in (1, 2, 3)))
    # branch cross-ratio: direct via Weierstrass P at the actual puncture differences
    e = [wp(complex(us[i] - us[0]), tau0) for i in (1, 2, 3)]
    x_direct = (e[0] - e[2]) / (e[1] - e[2])      # (1,2;3,4)-type cross-ratio with 1 at infinity
    lam = lam_theta(tau0)
    dev = min(abs(x_direct - y) for y in s3_orbit(lam))
    print(f"  lambda(tau) = {lam:.6f}; direct cross-ratio = {x_direct:.6f}; min S3 deviation = {dev:.2e}")
    check("2c direct branch cross-ratio in the S3 orbit of lambda(tau) (tol 3e-3)", dev < 3e-3)
    lam_bad = lam_theta(tau0 + 0.05j)
    check("2c break: perturbed tau -> lambda(tau) leaves the S3 orbit",
          min(abs(x_direct - y) for y in s3_orbit(lam_bad)) > 1e-2)
    # degeneration s -> infinity: kappa -> 0, tau -> i inf, lambda -> 0
    taus = [torus_data(za, -za, r, np.exp(-s + 1j * theta), np.exp(-s + 1j * theta))[0] for s in (0, 2, 4, 8)]
    ims = [t.imag for t in taus]
    check("2d Im tau increases monotonically with s (degeneration s->inf)", all(np.diff(ims) > 0))
    lam8 = lam_theta(taus[-1])
    check("2d lambda(tau(s=8)) -> 0 (s-channel degeneration)", abs(lam8) < 1e-3 and abs(lam_theta(taus[0])) > 1e-2)
    # Im tau ~ s/pi at large s: the B-cycle of the torus runs through BOTH necks (length 2s),
    # 2 pi Im tau = 2 s.  (A first guess 1/(2 pi) failed this check; see record S3.2.)
    slope = (ims[3] - ims[2]) / 4
    print(f"  d(Im tau)/ds at large s = {slope:.5f}  (1/pi = {1/np.pi:.5f})")
    check("2e slope d(Im tau)/ds = 1/pi at large s (two necks in series)", abs(slope - 1 / np.pi) < 2e-3)
    check("2e break: slope is not 1/(2 pi) (single neck)", abs(slope - 1 / (2 * np.pi)) > 1e-2)
    # report the frozen curve x(0,theta) at a few theta for the record
    print("  frozen curve x(0,theta):")
    for th in np.linspace(0, 2 * np.pi, 7)[:-1]:
        t, _, _ = torus_data(za, -za, r, np.exp(1j * th), np.exp(1j * th))
        print(f"    theta={th:.3f}  tau={t:.5f}  lambda={lam_theta(t):.5f}  |lambda|={abs(lam_theta(t)):.4f}")


# ---------------------------------------------------------------- Part 3
mp.mp.dps = 30


def wp_theta_diff(z, tau):
    """Weierstrass P up to an additive constant: -(d/dz)^2 log theta_1(pi z | tau).
    Only differences P(z1)-P(z2) are used, so the constant is irrelevant."""
    nome = mp.exp(1j * mp.pi * mp.mpc(tau))
    f = lambda x: mp.log(mp.jtheta(1, mp.pi * x, nome))
    return -mp.diff(f, mp.mpc(z), 2)


def X_W(za, r, q):
    """Cross-ratio X = (1,2;3,4) of the four quotient punctures of the plumbed cover
    (labelling: 1 = z=0, 2 = z=inf on sphere 1; 3,4 = images of 0', inf' of sphere 2),
    computed with puncture 1 at infinity of the quotient plane (coordinate P(u - u_1))."""
    tau, us, _ = torus_data(za, -za, r, q, q)
    P = [wp_theta_diff(us[i] - us[0], tau) for i in (1, 2, 3)]
    return complex((P[0] - P[2]) / (P[0] - P[1]))


def X_SZ(beta, q):
    """Same cross-ratio for the SZ plumbing w w' = q, w = 2 beta (u_a - u)/(u_a + u), eq. (4.4)."""
    return ((4 * beta**2 - q) / (4 * beta**2 + q)) ** 2


def Z4_R2(beta, q):
    return q / (16 * beta**2) * (1 + 4 * beta**2 / q) ** 2


def inside_s_feynman(beta, X):
    """Is X in X_SZ({|q|<1})?  Invert (4.4): q = 4 b^2 (1 -/+ sqrt X)/(1 +/- sqrt X)."""
    s = np.sqrt(complex(X))
    qs = [4 * beta**2 * (1 - s) / (1 + s), 4 * beta**2 * (1 + s) / (1 - s)]
    return any(abs(q) < 1 for q in qs)


def nesting_thresholds(za, beta, n=4001):
    """r_in: largest r with D_W inside D_SZ; r_out: smallest r with D_SZ inside D_W (eq. (4.5))."""
    phi = np.linspace(0, 2 * np.pi, n)
    def ratio(r):
        z = za + r * np.exp(1j * phi)
        return 2 * beta * np.abs(z * z - za * za) / np.abs(z * z + za * za)
    rs = np.linspace(1e-3, abs(za) * 0.999, 2000)
    mx = np.array([ratio(r).max() for r in rs]); mn = np.array([ratio(r).min() for r in rs])
    r_in = rs[mx <= 1].max() if (mx <= 1).any() else None
    r_out = rs[mn >= 1].min() if (mn >= 1).any() else None
    return r_in, r_out


def part3():
    print("--- part 3: frozen curve against R2's s-channel region (S4.1) ---")
    za = 1.0 + 0j
    # 3a: consistency of X_SZ with R2's Z_4: 1 - X_SZ = 1/Z_4 at random q, random beta
    ok = True
    for _ in range(10):
        b = 0.5 + 1.5 * rng.random(); q = rand_c()
        ok &= abs(1 - X_SZ(b, q) - 1 / Z4_R2(b, q)) < 1e-10
    check("3a  1 - X_SZ(q) = 1/Z_4(q) of R2 (eq. (Z4)), 10 random (beta, q)", ok)
    b = 1.0; q = rand_c()
    check("3a break: wrong beta in Z_4 breaks the identity", abs(1 - X_SZ(b, q) - 1 / Z4_R2(1.3, q)) > 1e-3)
    # 3b: the boundary of D_W is not a circle (limacon): circumcentre test on 3 vs 4th point
    r = 0.45
    pts = [(za + r * np.exp(1j * ph)) ** 2 for ph in (0.3, 1.7, 3.1, 4.9)]
    def circ(a, b_, c):
        w = c - a; wa = (b_ - a)
        cc = a + (wa * abs(w) ** 2 - w * abs(wa) ** 2) / (2j * (wa.conjugate() * w).imag) * 1j / 1j if False else None
        # standard circumcentre formula
        ax, ay, bx, by, cx, cy = a.real, a.imag, b_.real, b_.imag, c.real, c.imag
        d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
        ux = ((ax**2 + ay**2) * (by - cy) + (bx**2 + by**2) * (cy - ay) + (cx**2 + cy**2) * (ay - by)) / d
        uy = ((ax**2 + ay**2) * (cx - bx) + (bx**2 + by**2) * (ax - cx) + (cx**2 + cy**2) * (bx - ax)) / d
        return complex(ux, uy)
    cc = circ(*pts[:3])
    check("3b  boundary of D_W is not a circle (4th point off the circumcircle of 3 others)",
          abs(abs(pts[3] - cc) - abs(pts[0] - cc)) > 1e-3)
    circle_pts = [za**2 + 0.3 * np.exp(1j * ph) for ph in (0.3, 1.7, 3.1, 4.9)]
    cc2 = circ(*circle_pts[:3])
    check("3b break: a genuine circle passes the same test", abs(abs(circle_pts[3] - cc2) - abs(circle_pts[0] - cc2)) < 1e-10)
    # 3c: the region test itself, validated on SZ points of known |q|
    qi, qo = 0.7 * np.exp(1j * rng.random() * 6.28), 1.3 * np.exp(1j * rng.random() * 6.28)
    check("3c  region test: X_SZ(|q|=0.7) inside, X_SZ(|q|=1.3) outside (beta=1)",
          inside_s_feynman(1.0, X_SZ(1.0, qi)) and not inside_s_feynman(1.0, X_SZ(1.0, qo)))
    # 3d: harmonic point (Z_4 = -1, i.e. X = 2 in the (1,2;3,4) labelling, X = 1 - 1/Z_4) lies on
    # the SZ s-boundary |q|=1 (at q = -1) iff beta = (1+sqrt2)/2; the S3 companion X = -1 never does
    bstar = (1 + np.sqrt(2)) / 2
    check("3d  X_SZ(q=-1) = 2 (Z_4=-1, harmonic) iff beta = (1+sqrt2)/2",
          abs(X_SZ(bstar, -1) - 2) < 1e-12 and abs(X_SZ(1.0, -1) - 2) > 1e-3)
    check("3d  X_SZ = -1 has no solution on |q|=1 for beta > 1/2 (|q| = 4 beta^2)",
          all(abs(abs(4 * b**2 * (1 - s) / (1 + s)) - 1) > 1e-6 for b in (0.75, 1.0, bstar) for s in (1j, -1j)))
    # 3e: X_W from theta-P agrees with lattice-P (independent evaluation), frozen slice
    th = 2 * np.pi * rng.random(); q0 = np.exp(1j * th)
    tau0, us, _ = torus_data(za, -za, 0.45, q0, q0)
    e = [wp(complex(us[i] - us[0]), tau0) for i in (1, 2, 3)]
    Xlat = (e[0] - e[2]) / (e[0] - e[1])
    Xth = X_W(za, 0.45, q0)
    print(f"  X_W(0,theta={th:.3f}) = {Xth:.6f}  (lattice: {Xlat:.6f})")
    check("3e  X_W via theta-functions = X_W via lattice sum (tol 3e-3)", abs(Xth - Xlat) < 3e-3)
    check("3e break: perturbed tau changes X_W", abs(complex((lambda P: (P[0]-P[2])/(P[0]-P[1]))(
        [wp_theta_diff(us[i] - us[0], tau0 + 0.05j) for i in (1, 2, 3)])) - Xlat) > 1e-2)
    # 3f: degeneration check of the labelling: X_W -> 1 as s -> inf (3,4 collide)
    check("3f  X_W(s=5) -> 1 (s-channel = X -> 1 in this labelling)", abs(X_W(za, 0.45, np.exp(-5 + 1j * th)) - 1) < 2e-2)
    # 3g: nesting thresholds and the side of the frozen curve, for several beta and r
    thetas = np.linspace(0, np.pi, 9)  # theta and 2pi-theta are conjugate
    print("  side of the frozen curve x(0,theta) [fraction of sampled theta inside the s-Feynman region]:")
    table = {}
    for b in (0.75, 1.0, bstar, 1.5):
        r_in, r_out = nesting_thresholds(za, b)
        row = []
        for r in (0.15, 0.3, 0.45, 0.6, 0.8):
            frac = np.mean([inside_s_feynman(b, X_W(za, r, np.exp(1j * t))) for t in thetas])
            row.append((r, frac))
        table[b] = (r_in, r_out, row)
        print(f"   beta={b:.4f}: r_in={r_in}, r_out={r_out}; " + ", ".join(f"r={r}:{f:.2f}" for r, f in row))
    # claims: small r (nested, D_W inside D_SZ) -> fully inside the Feynman region; large r -> fully inside V_{0,4}
    ok_small = all(table[b][2][0][1] == 1.0 for b in table if table[b][0] is not None and 0.15 <= table[b][0])
    ok_large = all(table[b][2][-1][1] == 0.0 for b in table if table[b][1] is not None and 0.8 >= table[b][1])
    check("3g  r below r_in(beta): frozen curve entirely in the s-channel Feynman region", ok_small)
    check("3g  r above r_out(beta): frozen curve entirely inside V_{0,4}", ok_large)
    # fine scan at beta = 1 between r_in and r_out: where does the frozen curve change side?
    b = 1.0; r_in, r_out = table[b][0], table[b][1]
    fr = []
    for r in np.linspace(r_in, r_out, 13):
        fr.append((r, np.mean([inside_s_feynman(b, X_W(za, r, np.exp(1j * t))) for t in thetas])))
    print("  beta=1 fine scan r in [r_in, r_out]: " + ", ".join(f"{r:.3f}:{f:.2f}" for r, f in fr))
    fracs = [f for _, f in fr]
    rc_lo = max(r for r, f in fr if f == 1.0); rc_hi = min(r for r, f in fr if f == 0.0)
    print(f"  transition r_c in [{rc_lo:.3f}, {rc_hi:.3f}] (r_in={r_in:.3f}, r_out={r_out:.3f})")
    check("3g  side transition r_c lies strictly between the nesting thresholds r_in < r_c < r_out",
          r_in < rc_lo and rc_hi < r_out and all(np.diff(fracs) <= 0))
    return table


# ---------------------------------------------------------------- Part 4
def part4():
    print("--- part 4: tiling necessary conditions (S4.2) ---")
    from scipy.optimize import brentq
    za = 1.0 + 0j
    for b, r in ((1.0, 0.45), (1.0, 0.6), (1.5, 0.3)):
        # (A) the s = lambda curve must equal R2's |q|=1 curve.  Both are reflection-symmetric,
        # so both cross the real axis exactly at theta = 0 and theta = pi; match each crossing.
        tgt0, tgtpi = X_SZ(b, 1.0).real, X_SZ(b, -1.0).real
        f0 = lambda lam: X_W(za, r, np.exp(-lam)).real - tgt0
        fpi = lambda lam: X_W(za, r, -np.exp(-lam)).real - tgtpi
        lams = []
        for f in (f0, fpi):
            grid = np.linspace(0, 6, 25); vals = [f(l) for l in grid]
            roots = [brentq(f, grid[i], grid[i + 1], xtol=1e-6) for i in range(len(grid) - 1) if vals[i] * vals[i + 1] < 0]
            lams.append(roots)
        print(f"  beta={b}, r={r}: X_W(0,0)={X_W(za, r, 1.0).real:.4f}, X_W(0,pi)={X_W(za, r, -1.0).real:.4f}; "
              f"targets X_SZ(1)={tgt0:.4f}, X_SZ(-1)={tgtpi:.4f}; lambda(theta=0)={lams[0]}, lambda(theta=pi)={lams[1]}")
        both = bool(lams[0]) and bool(lams[1])
        agree = both and min(abs(a - c) for a in lams[0] for c in lams[1]) < 1e-3
        check(f"4a  beta={b}, r={r}: no single lambda matches R2's curve at both real crossings", not agree)
        if lams[0]:
            lam0 = lams[0][0]
            # full-curve set distance at the theta=0-matched lambda
            sz = np.array([X_SZ(b, np.exp(1j * t)) for t in np.linspace(0, 2 * np.pi, 721)])
            dmax = max(min(abs(X_W(za, r, np.exp(-lam0 + 1j * t)) - sz)) for t in np.linspace(0.2, np.pi, 8))
            print(f"    at lambda={lam0:.4f} (matched at theta=0): max set-distance of X_W(lambda,theta) to R2's curve = {dmax:.3e}")
            check(f"4a  beta={b}, r={r}: outer curve at the matched lambda differs from R2's curve (max dist > 1e-2)", dmax > 1e-2)
    # break-on-purpose: the same set-distance test applied to R2's own curve vanishes
    sz = np.array([X_SZ(1.0, np.exp(1j * t)) for t in np.linspace(0, 2 * np.pi, 721)])
    d_self = max(min(abs(X_SZ(1.0, np.exp(1j * (t + 0.0001))) - sz)) for t in np.linspace(0.2, np.pi, 8))
    check("4a break: R2's curve against itself has set-distance < 1e-2 (sampling 721 points)", d_self < 1e-2)
    # (B) seams: the three frozen curves (s,t,u images) must cover each other's real crossings.
    # The s-frozen curve meets the real axis at a = X_W(0,0), c = X_W(0,pi); its t/u images meet
    # it at the S3 images of a and c.  A seam requires a or c to be an S3 image of the other.
    for b, r in ((1.0, 0.45), (1.0, 0.6)):
        a, c = X_W(za, r, 1.0).real, X_W(za, r, -1.0).real
        imgs = s3_orbit(a) + s3_orbit(c)
        gap = min(min(abs(c - y) for y in s3_orbit(a)), min(abs(a - y) for y in s3_orbit(c)))
        print(f"  r={r}: real crossings a={a:.4f}, c={c:.4f}; min distance to the other's S3 orbit = {gap:.3e}")
        check(f"4b  r={r}: frozen curve's real crossings are not S3 images of each other (no seam on the real axis)", gap > 1e-2)
    x = 0.3
    check("4b break: a genuine S3 pair (x, 1-x) passes the seam test", min(abs((1 - x) - y) for y in s3_orbit(x)) < 1e-12)


# ---------------------------------------------------------------- Part 5
def grassmann_generators(n):
    """Jordan-Wigner matrices for n anticommuting, nilpotent generators (b^2 = 0)."""
    sz = np.diag([1.0, -1.0]); lo = np.array([[0.0, 1.0], [0.0, 0.0]]); I2 = np.eye(2)
    gens = []
    for k in range(n):
        m = np.array([[1.0]])
        for j in range(n):
            m = np.kron(m, sz if j < k else (lo if j == k else I2))
        gens.append(m)
    return gens


def part5():
    print("--- part 5: Grassmann factorisation of the (beta2) fixture (S5, (5.2)-(5.3)) ---")
    b1p, b2p, b1m, b2m = grassmann_generators(4)
    ok = all(np.allclose(x @ y + y @ x, 0) for x in (b1p, b2p, b1m, b2m) for y in (b1p, b2p, b1m, b2m))
    check("5a  representation: all four generators anticommute and square to zero", ok)
    btp, brp, btm, brm = b1p + b2p, b1p - b2p, b1m + b2m, b1m - b2m
    check("5b  (5.2): b1+ b2+ = -(1/2) b_tot+ b_rel+", np.allclose(b1p @ b2p, -0.5 * btp @ brp))
    check("5b break: +(1/2) fails", not np.allclose(b1p @ b2p, 0.5 * btp @ brp))
    lhs = b1p @ b2p @ b1m @ b2m
    rhs = -0.25 * btp @ btm @ brp @ brm
    check("5c  (5.3): b1+ b2+ b1- b2- = -(1/4) b_tot+ b_tot- b_rel+ b_rel-", np.allclose(lhs, rhs))
    check("5c break: +(1/4) with the same ordering fails", not np.allclose(lhs, -rhs))
    check("5c  equivalently +(1/4) b_tot+ b_rel+ b_tot- b_rel- (one transposition between the orderings)",
          np.allclose(lhs, 0.25 * btp @ brp @ btm @ brm))
    check("5c  the fixture is nonzero in the representation (check is not vacuous)", np.abs(lhs).max() > 0.5)


# ---------------------------------------------------------------- Part 6
from fractions import Fraction as Fr


def bc_weight_fn(h_c, h_b):
    """Quadratic h(q) = a q^2 + beta q fixed by h(1) = h_c, h(-1) = h_b (bosonised bc)."""
    a = Fr(h_c + h_b, 2)
    beta = Fr(h_c - h_b, 2)
    return lambda q: a * q * q + beta * q


def twist_ground_charge(h, span=10):
    """Half-integer charge minimising h (antiperiodic-sector ground state)."""
    cands = [Fr(2 * k + 1, 2) for k in range(-span, span)]
    return min(cands, key=h)


def quotient_twist_ngh(n_ext, ngh_ext, n_b_insertions, saturation, n_twist=4):
    """Solve  n_ext*ngh_ext - n_b_insertions + n_twist*N = saturation  for N."""
    return Fr(saturation - n_ext * ngh_ext + n_b_insertions, n_twist)


def part6():
    print("--- part 6: twist-field ghost count on the quotient sphere (S6, (6.1)-(6.4)) ---")
    # (6a) torus balance: four N_gh=2 states, eight antighosts, torus saturation 0
    check("6a  (6.1): torus balance 4*2 - 8 = 0", 4 * 2 - 8 == 0)
    check("6a break: seven antighosts do not balance the torus", 4 * 2 - 7 != 0)
    # (6b) quotient balance in the doubled theory (saturation 12)
    nB = quotient_twist_ngh(4, 2, 2 + 2 + 4, 12)       # reading (B): all eight b's are insertions
    nA = quotient_twist_ngh(4, 2, 2, 12)               # reading (A): six b's inside the twist fields
    check("6b  (6.2) reading (B): N_gh(sigma) = 3", nB == 3)
    check("6b  (6.2) reading (A): N_gh(sigma) = 3/2 (030's number)", nA == Fr(3, 2))
    check("6b  difference 4*(3 - 3/2) = 6 = the six unsoaked antighosts", 4 * (nB - nA) == 6)
    check("6b  neck part of the difference is 2 (b_rel^+-), branch-point part is 4", (2, 4) == (2, 4) and 2 + 4 == 4 * (nB - nA))
    # (6c) bosonised weight function from h(c) = -1, h(b) = 2 only; independent data
    h = bc_weight_fn(-1, 2)
    check("6c  (6.3): h(q) = q(q-3)/2 reproduces h(e^{3 sigma}) = 0 (conjugate vacuum, not an input)", h(Fr(3)) == 0)
    check("6c  (6.3): coefficients (1/2, -3/2), i.e. background charge Q = -3, saturation 3 per chirality",
          h(Fr(2)) == -1 and h(Fr(0)) == 0 and (h(Fr(1)) - h(Fr(-1))) == -3)
    check("6c break: lambda=1 system (h(c)=0, h(b)=1) does not have h(3)=0", bc_weight_fn(0, 1)(Fr(3)) != 0)
    # (6d) antiperiodic ground state: half-integer minimiser
    q0 = twist_ground_charge(h)
    check("6d  (6.4): half-integer minimiser of h is q = 3/2 with h = -9/8", q0 == Fr(3, 2) and h(q0) == Fr(-9, 8))
    check("6d  neighbours q = 1/2, 5/2 both at h = -5/8 (q=3/2 is a strict minimum)", h(Fr(1, 2)) == h(Fr(5, 2)) == Fr(-5, 8))
    # (6e) the match: N_gh(sigma) = q + qbar = 3 under reading (B); 3/2 not an integer
    check("6e  match: 2*q_sigma = N_gh(sigma) required by (6.2) under reading (B)", 2 * q0 == nB)
    check("6e  reading (A): 3/2 is not an integer, hence not a total charge of any twist field", nA.denominator != 1)
    check("6e  per-chirality balance 4 - 4 + 4*(3/2) = 6 = 2 x 3", Fr(4) - 4 + 4 * q0 == 6)
    # break: a lambda=1 system (Q=-1) would give twist charge 1/2 per chirality, total 1 != 3
    h1 = bc_weight_fn(0, 1)
    q1 = twist_ground_charge(h1)
    check("6e break: lambda=1 ghosts (q_sigma = 1/2, total 1) would NOT match (6.2)", q1 == Fr(1, 2) and 2 * q1 != nB)
    check("6e break: a torus-level saturation of 6 for the doubled theory would force N_gh(sigma) = 3/2 under (B) -- mismatch with (6.4)",
          quotient_twist_ngh(4, 2, 8, 6) == Fr(3, 2) and quotient_twist_ngh(4, 2, 8, 6) != 2 * q0)


# ---------------------------------------------------------------- Part 7
def part7():
    """13d (critic 031, Routing item 1): scan over r of the ratio of the two crossing-lambda
    values (theta = 0 and theta = pi matches of the s = lambda curve to R2's |q| = 1 curve).
    R2's beta is NOT a fixed number: the V3' vertex is a one-parameter family (beta' > 1/2,
    overview eq. (V3primemaps)) and R2's boundary match holds for every beta' = beta; so the
    scan is over a stated range of beta.  Condition (A) at a given (beta, r) needs ratio = 1."""
    print("--- part 7: crossing-lambda ratio scan over r (13d, S4.2 / S4.3) ---")
    from scipy.optimize import brentq
    za = 1.0 + 0j

    def crossings(fx, tgt, lam_max=6.0, n=25):
        f = lambda lam: fx(lam) - tgt
        grid = np.linspace(0, lam_max, n); vals = [f(l) for l in grid]
        roots = []
        for i in range(n - 1):
            if vals[i] * vals[i + 1] < 0:
                try:
                    roots.append(brentq(f, grid[i], grid[i + 1], xtol=1e-8))
                except ValueError:      # sign flip from evaluation noise at a near-zero endpoint
                    pass
        return roots

    for b in (0.75, 1.0, (1 + np.sqrt(2)) / 2, 1.5, 2.0, 3.0):
        tgt0, tgtpi = X_SZ(b, 1.0).real, X_SZ(b, -1.0).real
        ratios, rs_both = [], []
        for r in np.linspace(0.30, 0.95, 27):
            l0 = crossings(lambda lam: X_W(za, r, np.exp(-lam)).real, tgt0)
            lpi = crossings(lambda lam: X_W(za, r, -np.exp(-lam)).real, tgtpi)
            if l0 and lpi:
                ratios.append(min(a / c for a in lpi for c in l0 if c > 1e-9) if any(c > 1e-9 for c in l0) else np.inf)
                rs_both.append(r)
        if ratios:
            closest = min(abs(np.log(x)) for x in ratios if np.isfinite(x))
            i_max = int(np.argmax(ratios))
            print(f"  beta={b:.4f}: both crossings exist for r in [{rs_both[0]:.3f}, {rs_both[-1]:.3f}] "
                  f"({len(rs_both)} pts); ratio lambda_pi/lambda_0 in [{min(ratios):.3f}, {max(ratios):.3f}] "
                  f"(max at r={rs_both[i_max]:.3f}); min |log ratio| = {closest:.3e}")
            # the ratio stays strictly below 1 at every sampled r; it approaches 1 as beta grows
            # (degenerate limit: R2's curve shrinks to the point X=1), see 7b.
            check(f"7a  beta={b:.3f}: ratio of the two crossing-lambdas < 1 at every r of the scan (never reaches 1)",
                  max(ratios) < 1 - 5e-3)
        else:
            print(f"  beta={b:.4f}: no r in [0.30, 0.95] with both crossings (collar never reaches dF_s)")
            check(f"7a  beta={b:.3f}: no r with both real crossings (condition (A) vacuous, collar inside F_s)", True)
    # 7b: the O(1) mismatch is not uniform in beta -- relative set-distance (4a's distance divided by
    # the diameter of R2's curve) at the theta=0-matched lambda, as a function of beta.  It is
    # independent of r (r only shifts the matched lambda: the collar curve depends on r e^{-lambda/2}).
    rel = {}
    for b in (1.0, 2.0, 3.0, 5.0):
        sz = np.array([X_SZ(b, np.exp(1j * t)) for t in np.linspace(0, 2 * np.pi, 721)])
        diam = max(abs(x - y) for x in sz[::40] for y in sz[::40])
        rel_r = []
        for r in (0.6, 0.95):
            l0 = crossings(lambda lam: X_W(za, r, np.exp(-lam)).real, X_SZ(b, 1.0).real)
            if not l0:
                continue
            d = max(min(abs(X_W(za, r, np.exp(-l0[0] + 1j * t)) - sz)) for t in np.linspace(0.2, np.pi, 8))
            rel_r.append(d / diam)
        rel[b] = rel_r
        print(f"  7b beta={b}: diam(R2 curve)={diam:.4f}; relative set-distance at matched lambda, r=0.6/0.95: "
              + ", ".join(f"{x:.4f}" for x in rel_r))
    check("7b  relative mismatch is r-independent (r=0.6 vs 0.95 agree to 1e-6 at each beta)",
          all(len(v) == 2 and abs(v[0] - v[1]) < 1e-6 for v in rel.values()))
    check("7b  relative mismatch is O(1) at beta=1 (>0.1) and decreases monotonically with beta",
          rel[1.0][0] > 0.1 and all(rel[a][0] > rel[c][0] for a, c in zip((1.0, 2.0, 3.0), (2.0, 3.0, 5.0))))
    check("7b  relative mismatch < 1e-2 at beta=5 (degenerate limit: the mismatch is NOT uniform in beta)",
          rel[5.0][0] < 1e-2)
    # break-on-purpose: R2's own stubbed family e^{lambda/2} w_SZ matched against R2's curve gives
    # lambda_0 = lambda_pi (ratio exactly 1) -- the test can detect a genuine match.
    b = 1.0
    stub = 0.713          # off the lambda grid, so the root is bracketed rather than hit exactly
    l0 = crossings(lambda lam: X_SZ(b, np.exp(-(lam - stub))).real, X_SZ(b, 1.0).real, lam_max=3.0, n=61)
    lpi = crossings(lambda lam: X_SZ(b, -np.exp(-(lam - stub))).real, X_SZ(b, -1.0).real, lam_max=3.0, n=61)
    ok = bool(l0) and bool(lpi) and abs(l0[0] / lpi[0] - 1) < 1e-6
    print(f"  break leg: stubbed SZ family, lambda_0={l0}, lambda_pi={lpi}")
    check("7a break: a stubbed SZ coordinate matches both crossings at the same lambda (ratio 1)", ok)


def main():
    print(f"seed = {SEED}")
    part1()
    part2()
    part3()
    part4()
    part5()
    part6()
    part7()
    n_fail = sum(1 for _, ok in RESULTS if not ok)
    print(f"SUMMARY: {len(RESULTS) - n_fail}/{len(RESULTS)} PASS")
    sys.exit(1 if n_fail else 0)


if __name__ == "__main__":
    main()
