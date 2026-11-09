"""
Companion checks for record 080 (dressed CKV; `agent/derivations/080-dressed-ckv.md`).

Verified (sympy, exact arithmetic, seeded random points in general position):
  C1-mobius-general-chart  (1.5): push-forward of the dilation CKV v = k (u - u_i)(u - u_j)
                           through a Mobius local map F(w) = u_i + a w / (1 + mu w) equals
                           k (u_i - u_j) w (1 + mu_eff w), mu_eff = mu + a/(u_i - u_j).
  C1-exact-quadratic       the germ is exactly quadratic (v_k = 0, k = 3..6).
  C1-pole-criterion        forward: mu chosen with F(inf) = u_j gives mu_eff = 0; backward: the
                           symbolic identity mu_eff = a (R - u_j) / ((u_i - u_j)(R - u_i)),
                           R = F(inf) = u_i + a/mu, the second form of (1.5).
  C1-jet-uniqueness        (1.8)-(1.9): solving v_k = 0 (k = 2..6) order by order for a general
                           jet F = u_i + a w + g_2 w^2 + ... reproduces the jet of the Mobius map
                           (1.8), so no non-Mobius germ qualifies (to order 6).
  C1-general-map           (1.7) for a general jet, and a cubic map with mu_eff = 0 but v_3 != 0
                           (the second-order criterion is not the full one).
  C1-frame-independence    mu of f_0' in the z-frame equals mu of 078's f_1 in the u-frame.
  C2-mode-content          (2.2): the residue of v~(w) b~(w) is k (b_0 + mu b_1) for a Mobius germ.
  C3-rigid-mu              mu_i = alpha'_v / gamma' at both ordinary punctures of the half.
  setup-transport-poles    setup consistency (not C3.2): the rigid transport u = q / u_B puts the
                           poles of half B's transported maps at each other, at random q (|q| = 1
                           and |q| != 1 alike; nothing in it uses |q| = 1).
  setup-u2-ne-u4           setup consistency (not C3.3): u_2 = -z != u_4 = -q/z at random q with
                           |q| > 1. Does not encode A5 or the relabellings; C3.3 is a hand proof.
  C5-alpha-limit           mu_i -> 0 as alpha'_v -> 0 and the local-frame field is exactly +-w d/dw.
  Engine checks (three-point amplitudes <V_3'| chi (x) A_1 (x) A_2> of `codes/verify-ph31-rank.py`,
  imported, never edited; exact rationals, d_eff = 2, beta = 3/2, gamma' = 3; chi over the
  leg-0 Fock basis at ghost number 3, levels <= 2, all zero-mode sectors):
  C2-law-mu-nonzero        (2.6) at alpha'_v = 1/2 (mu = 1/6) in the leg-0 form: from
                           sum_r oint_r v b = 0 on <V|, with oint_0 v b = -beta (b_{-1} - z^2 b_1),
                           oint_{1,2} v b = +-(b_0 + mu b_1) and chi Grassmann-odd,
                           y_chi(A_1, A_2) := <V|[(b_{-1} - z^2 b_1) - c.c.] chi (x) A_1 (x) A_2>
                             = -(mu/beta) [<V| chi, b_1^- A_1, A_2> - (-1)^{|A_1|} <V| chi, A_1, b_1^- A_2>]
                           on the pair of C4.1 and 12 random ordered pairs of H_0 (level <= 1).
  C4.1-explicit-pair       Phi_2(b_1 A_1, A_2) for A_1 = c_{-1} bbar_{-1} c_1 cbar_1|k_1>,
                           A_2 = c_1 cbar_1|k_2>: b_1 A_1 = -c_1|k_1>, bbar_1 A_1 = 0, and the
                           component of Phi_2(b_1 A_1, A_2) dual to chi = cbar_0 c_1 cbar_1|0>
                           equals 2 z (beta gamma')^3 = 243/4 at alpha'_v = 0 and 1/2 (mode
                           expansion: -c(u_1) c(u_2)|0> = 2 z c_1 c_0|0> + ..., a factor
                           1/F'(0) per c with radii a_1 = -a_2 = 1/(beta gamma'), BPZ pairing
                           <bpz chi| c_1 c_0 cbar_1|0> = +1); the O_b functional of the pair
                           vanishes at alpha'_v = 0 and not at 1/2.
  C4.1-sym-witness         (fix pass 2, R1) on A_1 (.) A_2 (swapped order and leg momenta,
                           summed): O_b Phi_2 has even component (on c_1 c_0 cbar_1|k_1+k_2>) 0
                           and odd component (on c_1 c_0 cbar_0|k_1+k_2>) -2 beta z^2 (mu_1 + mu_2)
                           (beta gamma')^3 = -81/8 at alpha'_v = 1/2, 0 at alpha'_v = 0 (engine
                           BPZ I(w) = 1/w: pairing +1 even, -1 odd); the leg-0 O_b functionals of
                           the symmetrised pair vanish at 0 and not at 1/2 (no use of (2.6)).
  C4.1-primary-dressing    the components of Phi_2(c_1|k_1>, c_1 cbar_1|k_2>) at alpha'_v = 1/2
                           and 0 (same radii, different germs) agree on every chi: primary inputs
                           see the germ only through F'(0).
  C5.2-ghost-ground-b-rule the O_b functionals vanish at alpha'_v = 1/2 on pairs of inputs with
                           ghost part c_1 cbar_1 (matter oscillators), while they do not vanish on
                           ghost-excited pairs (break leg).
  BREAK-*                  each criterion fails when it should; the engine break legs flip the
                           relative sign or the coefficient sign of (2.6), use the non-primary
                           A_1 in place of b_1 A_1, drop the swapped term of the symmetrised pair
                           (C4.1-sym), and use a ghost-excited pair for C5.2.

Not verified: the contour deformation of (2.3) on the output side as such (tested only through
the leg-0 form above); the vertex's R_i(q) on the interior of Q_V (data not available); A5,
C3.2 (argued), C3.3 (hand proof); the L-rule of C5.2; hypothesis H1; the engine's normalisation
of the plane-wave prefactor (dropped, common to both sides of every engine check).
"""

from __future__ import annotations

import importlib.util
import random
import sys
import time
from fractions import Fraction
from pathlib import Path

import sympy as sp

SEED = 20261004
random.seed(SEED)
print(f"seed = {SEED}")

w = sp.symbols("w")
results: list[tuple[str, bool]] = []


def check(name: str, ok: bool) -> None:
    results.append((name, bool(ok)))
    print(f"{'PASS' if ok else 'FAIL'}  {name}")


def rnd() -> sp.Rational:
    """Random non-special rational in general position."""
    return sp.Rational(random.randint(-97, 97), random.randint(2, 23)) + sp.Rational(
        random.randint(1, 13), 29
    )


def pushforward(v_u, F):
    """(1.2): v~(w) = v(F(w)) / F'(w) for a vector field v(u) d/du and local map u = F(w)."""
    u = sp.symbols("u")
    return sp.simplify(v_u.subs(u, F) / sp.diff(F, w))


def germ(vt, order: int = 6) -> list:
    """Taylor coefficients v_1..v_order of v~(w) about w = 0."""
    ser = sp.series(vt, w, 0, order + 1).removeO()
    return [sp.simplify(ser.coeff(w, k)) for k in range(1, order + 1)]


u = sp.symbols("u")

# ---- C1: Mobius local map in a general chart ------------------------------------
ok_general, ok_quad, ok_pole_fwd, ok_pole_bwd = True, True, True, True
for _ in range(5):
    ui, uj, a, mu, k = rnd(), rnd(), rnd(), rnd(), rnd()
    if ui == uj or a == 0 or mu == 0:
        continue
    v_u = k * (u - ui) * (u - uj)
    F = ui + a * w / (1 + mu * w)
    vt = pushforward(v_u, F)
    mu_eff = mu + a / (ui - uj)
    target = k * (ui - uj) * w * (1 + mu_eff * w)
    ok_general &= sp.simplify(vt - target) == 0
    coeffs = germ(vt)
    ok_quad &= all(c == 0 for c in coeffs[2:])
    # pole criterion, forward: choose mu so that F(inf) = u_j, expect mu_eff = 0
    mu_star = a / (uj - ui)
    F_star = ui + a * w / (1 + mu_star * w)
    assert sp.simplify(sp.limit(F_star, w, sp.oo) - uj) == 0
    ok_pole_fwd &= germ(pushforward(v_u, F_star))[1] == 0
    # backward: the second form of (1.5), mu_eff = a (R - u_j) / ((u_i - u_j)(R - u_i))
    R = ui + a / mu
    ok_pole_bwd &= sp.simplify(mu_eff - a * (R - uj) / ((ui - uj) * (R - ui))) == 0
check("C1-mobius-general-chart", ok_general)
check("C1-exact-quadratic", ok_quad)
check("C1-pole-criterion", ok_pole_fwd and ok_pole_bwd)

# ---- C1: general (non-Mobius) map, (1.7) and the insufficiency of second order ----
ui, uj, a, b, c3, k = rnd(), rnd(), rnd(), rnd(), rnd(), rnd()
v_u = k * (u - ui) * (u - uj)
F_gen = ui + a * w + b * w**2 + c3 * w**3
coeffs = germ(pushforward(v_u, F_gen))
mu_17 = a / (ui - uj) - b / a
ok_17 = (
    sp.simplify(coeffs[1] / coeffs[0] - mu_17) == 0
    and sp.simplify(coeffs[0] - k * (ui - uj)) == 0
)
# tune b so that mu_eff = 0; v_3 must still be non-zero for generic c3
b_star = a**2 / (ui - uj)
coeffs_star = germ(pushforward(v_u, F_gen.subs(b, b_star)))
ok_cubic = coeffs_star[1] == 0 and sp.simplify(coeffs_star[2]) != 0
check("C1-general-map", ok_17 and ok_cubic)

# ---- C1: uniqueness (1.8)-(1.9): v_k = 0 order by order fixes the jet to the Mobius one ----
ui, uj, a = rnd(), rnd(), rnd()
gs = sp.symbols("g2:7")
F_jet = ui + a * w + sum(gk * w ** (k + 2) for k, gk in enumerate(gs))
v_u = (u - ui) * (u - uj)
coeffs_jet = germ(pushforward(v_u, F_jet), order=6)
sol_jet: dict = {}
for k in range(2, 7):  # v_k is linear in g_k once g_2..g_{k-1} are fixed
    eq = sp.simplify(coeffs_jet[k - 1].subs(sol_jet))
    sk = sp.solve(eq, gs[k - 2])
    sol_jet[gs[k - 2]] = sk[0] if len(sk) == 1 else sp.nan
C = a / (ui - uj)
F_mob = (ui - uj * C * w) / (1 - C * w)
mob_ser = sp.series(F_mob, w, 0, 7).removeO()
ok_jet = all(
    sp.simplify(sol_jet[gs[k - 2]] - mob_ser.coeff(w, k)) == 0 for k in range(2, 7)
)
check("C1-jet-uniqueness", ok_jet)

# ---- C1: frame independence: z-frame f_0' vs 078's u-frame f_1 -------------------
alpha, gamma, beta = sp.symbols("alpha gamma beta", positive=True)
ok_frame = True
for av in [0, sp.Rational(1, 2), 1, sp.Rational(-3, 7)]:
    g, bt = sp.Integer(3), sp.Rational(3, 2)
    z = 1 / (2 * bt)
    # z-frame: punctures at 0 and infinity, CKV z d/dz
    f0 = w / (av * w + g)
    vt_z = sp.simplify(f0 / sp.diff(f0, w))
    mu_z = germ(vt_z)[1] / germ(vt_z)[0]
    # u-frame: u = phi(zeta) with phi Mobius sending 0 -> z, inf -> -z (078: f_1 = phi o f_0)
    # 078 (4.1) at alpha'_v = 0: f_1(w) = (w + g) / (2 bt (g - w)) = phi(f_0'(w)) with
    # phi(zeta) := (1 + zeta) / (2 bt (1 - zeta)), phi(0) = z, phi(inf) = -z.
    zeta = sp.symbols("zeta")
    phi = (1 + zeta) / (2 * bt * (1 - zeta))
    assert sp.simplify(phi.subs(zeta, w / g) - (w + g) / (2 * bt * (g - w))) == 0
    f1 = sp.simplify(phi.subs(zeta, f0))
    v_u = bt * (u**2 - z**2)
    vt_u = pushforward(v_u, f1)
    cu = germ(vt_u)
    ok_frame &= sp.simplify(cu[0] - 1) == 0 and sp.simplify(cu[1] - mu_z) == 0
    ok_frame &= sp.simplify(mu_z - av / g) == 0
check("C1-frame-independence", ok_frame)

# ---- C2: mode content of the contour integral -------------------------------------
bm = {n: sp.Symbol(f"b_{n}") for n in range(-3, 4)}
btilde = sum(bm[n] * w ** (-n - 2) for n in bm)
kk, mm = sp.symbols("kappa mu")
vt = kk * (w + mm * w**2)
res = sp.residue(sp.expand(vt * btilde), w, 0)
check("C2-mode-content", sp.simplify(res - kk * (bm[0] + mm * bm[1])) == 0)

# ---- C3: rigid halves, boundary consistency, symmetry obstruction ------------------
g, bt = sp.Integer(3), sp.Rational(3, 2)
z = 1 / (2 * bt)
ok_rigid = True
for av in [0, sp.Rational(1, 2), 1]:
    f0 = w / (av * w + g)
    finf = (av * w + g) / w
    # z-frame CKV z d/dz; at infinity use y = 1/z, CKV = -y d/dy
    vt1 = sp.simplify(f0 / sp.diff(f0, w))
    y_of_w = 1 / finf
    vt2 = sp.simplify(-y_of_w / sp.diff(y_of_w, w))
    c1, c2 = germ(vt1), germ(vt2)
    ok_rigid &= c1[0] == 1 and c2[0] == -1
    ok_rigid &= (
        sp.simplify(c1[1] / c1[0] - av / g) == 0
        and sp.simplify(c2[1] / c2[0] - av / g) == 0
    )
check("C3-rigid-mu", ok_rigid)

# setup consistency: half B's punctures in half A's circle frame, u = q / u_B, transported
# rigid maps; random q on and off |q| = 1 (the property does not use |q| = 1, so this is not C3.2)
ok_bdry = True
for rr in (sp.Integer(1), sp.Rational(random.randint(11, 19), 10)):
    th = sp.Rational(random.randint(1, 11), 13) * sp.pi
    q = rr * sp.exp(sp.I * th)
    f1A = (w + g) / (2 * bt * (g - w))  # 078 (4.1), alpha'_v = 0, puncture 1 at u = z
    # puncture 2 (u = -z): f_2 = phi(f_inf') = phi(g / w) = (w + g) / (2 bt (w - g)), pole at +z
    f2A = (w + g) / (2 * bt * (w - g))
    # check f2A(0) = -z, f2A(inf) = +z
    ok_bdry &= (
        sp.simplify(f2A.subs(w, 0) + z) == 0
        and sp.simplify(sp.limit(f2A, w, sp.oo) - z) == 0
    )
    f3 = sp.simplify(q / f1A)  # half B's puncture 1 seen in half A's frame
    f4 = sp.simplify(q / f2A)
    u3, u4 = f3.subs(w, 0), f4.subs(w, 0)
    R3, R4 = sp.limit(f3, w, sp.oo), sp.limit(f4, w, sp.oo)
    ok_bdry &= sp.simplify(R3 - u4) == 0 and sp.simplify(R4 - u3) == 0
    # and the CKV of the pair (3,4) reads +-w d/dw exactly in those frames
    v34 = (u - u3) * (
        u - u4
    )  # the dilation CKV of the pair (3,4); only the germ shape matters
    c3_ = germ(pushforward(v34, f3))
    ok_bdry &= sp.simplify(c3_[1]) == 0 and all(sp.simplify(c) == 0 for c in c3_[2:])
check("setup-transport-poles", ok_bdry)

# setup consistency (not C3.3, which is a hand proof using A5): u_2 = -z and u_4 = -q/z
# differ at random q with |q| > 1; u_2 = u_4 only at q = z^2 = 1/(4 beta^2) < 1
qq = sp.symbols("q")
sol = sp.solve(sp.Eq(-z, -qq / z), qq)
ok_u24 = sol == [z**2] and abs(z**2) < 1
for _ in range(5):
    qr = sp.Rational(random.randint(101, 400), 100) * sp.exp(
        sp.I * sp.pi * sp.Rational(random.randint(0, 40), 41)
    )
    ok_u24 &= sp.simplify(-z - (-qr / z)) != 0
check("setup-u2-ne-u4", ok_u24)

# ---- C5: alpha'_v -> 0 limit ---------------------------------------------------------
av = sp.symbols("alpha_v", real=True)
f0 = w / (av * w + g)
vt1 = sp.simplify(f0 / sp.diff(f0, w))
check(
    "C5-alpha-limit",
    sp.simplify(sp.limit(vt1, av, 0) - w) == 0
    and sp.simplify(vt1 - w - av / g * w**2) == 0,
)

# ---- BREAK legs --------------------------------------------------------------------
ui, uj, a, k = rnd(), rnd(), rnd(), rnd()
v_u = k * (u - ui) * (u - uj)
mu_wrong = a / (uj - ui) + sp.Rational(1, 7)  # pole off the partner
F_wrong = ui + a * w / (1 + mu_wrong * w)
check(
    "BREAK-C1-pole-off-partner-gives-mu-nonzero",
    germ(pushforward(v_u, F_wrong))[1] != 0,
)
res_wrong = sp.residue(sp.expand(kk * (w - mm * w**2) * btilde), w, 0)
check(
    "BREAK-C2-germ-sign",
    sp.simplify(res_wrong - kk * (bm[0] + mm * bm[1])) != 0,
)
# perturb the tested formula: mu_eff with the chart term's sign flipped must fail (1.5)
ui, uj, a, mu, k = rnd(), rnd(), rnd(), rnd(), rnd()
vt_b = pushforward(k * (u - ui) * (u - uj), ui + a * w / (1 + mu * w))
check(
    "BREAK-C1-mu-eff-chart-sign",
    sp.simplify(vt_b - k * (ui - uj) * w * (1 + (mu - a / (ui - uj)) * w)) != 0,
)
check(
    "BREAK-C3-rigid-alpha-half-not-zero",
    sp.simplify(germ(sp.simplify((w / (w / 2 + g)) / sp.diff(w / (w / 2 + g), w)))[1])
    != 0,
)

# ---- engine checks: 078's three-point amplitudes (imported, never edited) --------------
_spec = importlib.util.spec_from_file_location(
    "verify_ph31_rank", Path(__file__).resolve().parent / "verify-ph31-rank.py"
)
E = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(E)
t0 = time.time()
d_eff, BETA, GAMMA = 2, Fraction(3, 2), 3
rng = random.Random(SEED)
l1 = tuple(Fraction(rng.randint(-60, 60), rng.randint(1, 25)) for _ in range(d_eff))
l2 = tuple(Fraction(rng.randint(-60, 60), rng.randint(1, 25)) for _ in range(d_eff))


def ghost_act(op: tuple, S: list) -> list:
    """Apply one ghost mode (chirality, 'b'/'c', n) to a list of (coef, matter, string)."""
    return [(c * s2, m, o) for c, m, g in S for s2, o in E.reduce_on_vacuum((op,) + g)]


def lincomb(*terms) -> list:
    """sum_i cf_i S_i for lists of (coef, matter, ghost string)."""
    return [(cf * c, m, g) for cf, S in terms for c, m, g in S]


def b1m(S: list) -> list:
    """b_1^- = b_1 - bbar_1 on the inputs (mu real)."""
    return lincomb((1, ghost_act((0, "b", 1), S)), (-1, ghost_act((1, "b", 1), S)))


def ob_leg0(S: list, z2: Fraction) -> list:
    """(b_{-1} - z^2 b_1) - c.c. on the leg-0 state (078's y_chi operator)."""
    return lincomb(
        (1, ghost_act((0, "b", -1), S)),
        (-z2, ghost_act((0, "b", 1), S)),
        (-1, ghost_act((1, "b", -1), S)),
        (z2, ghost_act((1, "b", 1), S)),
    )


def amp3(X: list, A: list, B: list, amps) -> Fraction:
    """<V_3'| X (x) A (x) B>, multilinear over the string lists."""
    tot = Fraction(0)
    for cx, mx, gx in X:
        for ca, ma, ga in A:
            for cb, mb, gb in B:
                tot += (
                    cx
                    * ca
                    * cb
                    * amps.amp([(1, mx, gx)], [(1, ma, ga)], [(1, mb, gb)], l1, l2)
                )
    return tot


def state(gh: tuple = (), zero: str = "") -> list:
    return E.state_strings({"N": 0, "Nb": 0, "mat": (), "gh": gh}, zero)


amps_v = {
    av: E.Amplitudes(E.Vertex(BETA, GAMMA, av, 4), d_eff, E.Field(None))
    for av in (Fraction(0), Fraction(1, 2))
}
z2v = Fraction(1, 9)  # z = 1/(2 beta) = 1/3
chis = [
    E.state_strings(s, zz)
    for zz in E.ZPREF
    for s in E.closed_basis(2, d_eff, 1 - len(E.ZPREF[zz]), False)
]
A1 = state(gh=((0, "c", -1), (1, "b", -1)))  # c_{-1} bbar_{-1} c_1 cbar_1 |k_1>
A2 = state()  # c_1 cbar_1 |k_2>

# C4.1-explicit-pair
b1A1 = ghost_act((0, "b", 1), A1)
bb1A1 = ghost_act((1, "b", 1), A1)
chi_c = state(zero="cb0")  # cbar_0 c_1 cbar_1 |0>
target = 2 * Fraction(1, 3) * (BETA * GAMMA) ** 3
vals = {av: amp3(chi_c, b1A1, A2, amps_v[av]) for av in amps_v}
y_pair = {
    av: [amp3(ob_leg0(c, z2v), A1, A2, amps_v[av]) for c in chis] for av in amps_v
}
ok_pair = (
    b1A1 == [(-1, (), ((0, "c", 1),))]
    and bb1A1 == []
    and all(v == target for v in vals.values())
    and all(y == 0 for y in y_pair[Fraction(0)])
    and any(y != 0 for y in y_pair[Fraction(1, 2)])
)
check("C4.1-explicit-pair", ok_pair)
print(f"    component = {vals}, target 2z(beta gamma')^3 = {target}; ", end="")
print(f"O_b(pair) non-zero comps at 1/2: {sum(1 for y in y_pair[Fraction(1, 2)] if y)}")

# C4.1-primary-dressing: same radii, different germs -> identical components
r0 = [amp3(c, b1A1, A2, amps_v[Fraction(0)]) for c in chis]
r1 = [amp3(c, b1A1, A2, amps_v[Fraction(1, 2)]) for c in chis]
nz = sum(1 for x in r0 if x)
check("C4.1-primary-dressing", r0 == r1 and nz > 0)
print(f"    {nz} of {len(chis)} components non-zero, all equal at alpha'_v = 0, 1/2")
# break leg: the ghost-excited (non-primary) input A_1 itself does see the germ
# (leg-0 states at ghost number 2, so that the total ghost number is 6)
chis2 = [
    E.state_strings(s, zz)
    for zz in E.ZPREF
    for s in E.closed_basis(2, d_eff, -len(E.ZPREF[zz]), False)
]
yA0 = [amp3(c, A1, A2, amps_v[Fraction(0)]) for c in chis2]
yA1 = [amp3(c, A1, A2, amps_v[Fraction(1, 2)]) for c in chis2]
check("BREAK-C4.1-nonprimary-sees-germ", yA0 != yA1)


# C4.1-sym-witness (fix pass 2, R1): the image I_q is spanned by symmetrised pairs.
# A_1 (.) A_2 = (A_1 at leg 1, k_1; A_2 at leg 2, k_2) + (A_2 at leg 1, k_2; A_1 at leg 2, k_1)
# (both Grassmann-even). By (2.6), O_b Phi_2(A_1 (.) A_2) = beta mu [Phi_2(b_1 A_1, A_2)
# - Phi_2(A_2, b_1 A_1)], mu_1 = mu_2 = mu = alpha'_v / gamma' (C3.1, frame f_2 = -f_1).
# Engine BPZ is I(w) = 1/w (verify-ph31-rank.py, bpz_op): <bpz chi_e | c_1 c_0 cbar_1> = +1,
# <bpz chi_o | c_1 c_0 cbar_0> = -1, so component = (+1 | -1) x amplitude.
def amp3k(X: list, A: list, B: list, amps, k1: tuple, k2: tuple) -> Fraction:
    """<V_3'| X (x) A (x) B> with leg momenta k1 (leg 1), k2 (leg 2)."""
    tot = Fraction(0)
    for cx, mx, gx in X:
        for ca, ma, ga in A:
            for cb, mb, gb in B:
                tot += (
                    cx
                    * ca
                    * cb
                    * amps.amp([(1, mx, gx)], [(1, ma, ga)], [(1, mb, gb)], k1, k2)
                )
    return tot


chi_o = state(gh=((1, "c", -1),))  # cbar_{-1} c_1 cbar_1|0>, dual to c_1 c_0 cbar_0|0>
pair_sign = {"even": Fraction(1), "odd": Fraction(-1)}
sym_comp, ord_comp = {}, {}
for av in amps_v:
    mu_a = av / GAMMA
    for sec, ch in (("even", chi_c), ("odd", chi_o)):
        o = amp3k(ch, b1A1, A2, amps_v[av], l1, l2)
        sw = amp3k(ch, A2, b1A1, amps_v[av], l2, l1)
        sym_comp[(av, sec)] = pair_sign[sec] * BETA * mu_a * (o - sw)
        ord_comp[(av, sec)] = pair_sign[sec] * BETA * mu_a * o
# direct leg-0 form on the symmetrised pair (no use of (2.6)): non-zero at 1/2, zero at 0
y_sym = {
    av: [
        amp3k(ob_leg0(c, z2v), A1, A2, amps_v[av], l1, l2)
        + amp3k(ob_leg0(c, z2v), A2, A1, amps_v[av], l2, l1)
        for c in chis
    ]
    for av in amps_v
}
half = Fraction(1, 2)
target_odd = -2 * BETA * Fraction(1, 9) * 2 * (half / GAMMA) * (BETA * GAMMA) ** 3
ok_sym = (
    all(sym_comp[(av, "even")] == 0 for av in amps_v)
    and sym_comp[(half, "odd")] == target_odd
    and sym_comp[(Fraction(0), "odd")] == 0
    and all(y == 0 for y in y_sym[Fraction(0)])
    and any(y != 0 for y in y_sym[half])
)
check("C4.1-sym-witness", ok_sym)
print(
    f"    even comp {sym_comp[(half, 'even')]}, odd comp {sym_comp[(half, 'odd')]} "
    f"(target -2 beta z^2 (mu_1 + mu_2)(beta gamma')^3 = {target_odd}) at 1/2; "
    f"O_b(A_1 . A_2) non-zero comps: {sum(1 for y in y_sym[half] if y)} at 1/2, "
    f"{sum(1 for y in y_sym[Fraction(0)] if y)} at 0"
)
# break leg: drop the swapped term -> the even component reappears (ordered pair only)
check("BREAK-C4.1-sym-ordered-only", ord_comp[(half, "even")] != 0)

# C2-law-mu-nonzero (#22): (2.6) at alpha'_v = 1/2, mu = 1/6, leg-0 form
amps = amps_v[Fraction(1, 2)]
mu_v = Fraction(1, 6)
ins = [E.state_strings(s, zz) for s, zz in E.input_basis(1, d_eff)]
pairs = [(A1, A2)] + [
    (ins[rng.randrange(len(ins))], ins[rng.randrange(len(ins))]) for _ in range(12)
]


def law_mismatch(cf: Fraction, rel: int) -> tuple[int, int]:
    bad = nzl = 0
    for P1, P2 in pairs:
        for c in chis:
            lhs = amp3(ob_leg0(c, z2v), P1, P2, amps)
            rhs = cf * (amp3(c, b1m(P1), P2, amps) - rel * amp3(c, P1, b1m(P2), amps))
            bad += lhs != rhs
            nzl += lhs != 0
    return bad, nzl


bad, nzl = law_mismatch(-mu_v / BETA, 1)
check("C2-law-mu-nonzero", bad == 0 and nzl > 0)
print(
    f"    {len(pairs)} pairs x {len(chis)} chi: {bad} mismatches, {nzl} non-zero left sides"
)
bad_rel, _ = law_mismatch(-mu_v / BETA, -1)
bad_mu, _ = law_mismatch(mu_v / BETA, 1)
check("BREAK-C2-law-relative-sign", bad_rel > 0)
check("BREAK-C2-law-coefficient-sign", bad_mu > 0)

# C5.2-ghost-ground-b-rule: inputs with ghost part c_1 cbar_1 (matter oscillators allowed)
gg = [
    E.state_strings(s, "")
    for s, zz in E.input_basis(1, d_eff)
    if not s["gh"] and zz == ""
]
yg = [amp3(ob_leg0(c, z2v), P1, P2, amps) for P1 in gg for P2 in gg for c in chis]
check("C5.2-ghost-ground-b-rule", len(gg) > 1 and all(y == 0 for y in yg))
print(f"    {len(gg)} ghost-ground inputs, {len(yg)} functional values, all zero")
check("BREAK-C5.2-ghost-excited-pair", any(y != 0 for y in y_pair[Fraction(1, 2)]))
print(f"    engine block: {time.time() - t0:.1f} s")

n_fail = sum(1 for _, ok in results if not ok)
print(f"summary: {len(results) - n_fail}/{len(results)} PASS")
sys.exit(1 if n_fail else 0)
