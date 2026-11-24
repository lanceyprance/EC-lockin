"""Recompute every number in the topics, homeworks and past papers.

Usage: python3 tools/check_numbers.py      (needs numpy)
Each line: OK / FAIL, label, computed value, the value written in the repo.
"official" = the value printed in an official UCD solution. Everything else is my own answer.
All homework Greek-letter offsets (alpha, gamma, ...) are set to 0.
"""
import cmath, math, sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(__file__))
from mna import solve, par

pi = math.pi
fails = 0
VERBOSE = '-v' in sys.argv


def check(label, got, want, rtol=0.006, atol=1e-12):
    global fails
    if want is None:
        print(f'  ??   {label}: {got!r}'); return
    if isinstance(got, complex) or isinstance(want, complex):
        ok = abs(got - want) <= rtol * abs(want) + atol
    else:
        ok = abs(got - want) <= rtol * abs(want) + atol
    if not ok: fails += 1
    if VERBOSE or not ok:
        print(f"{'OK  ' if ok else 'FAIL'} {label}: got {got:.6g} want {want:.6g}")


def deg(z): return math.degrees(cmath.phase(z))


def rc_step(v0, vinf, t, tau): return vinf + (v0 - vinf) * math.exp(-t / tau)


def simulate(f_rhs, y0, T, n_per, periods):
    """Simple RK4 for one-state circuits. Returns (t, y) over the last period."""
    dt = T / n_per; y = y0; t = 0.0; ts = []; ys = []
    for k in range(periods * n_per):
        k1 = f_rhs(t, y); k2 = f_rhs(t + dt / 2, y + dt / 2 * k1)
        k3 = f_rhs(t + dt / 2, y + dt / 2 * k2); k4 = f_rhs(t + dt, y + dt * k3)
        y += dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4); t += dt
        if k >= (periods - 1) * n_per: ts.append(t); ys.append(y)
    return np.array(ts), np.array(ys)


print('=== Homework 0 (official answers exist) ===')
check('H0-1a V12', 3 * 1200 / 3400, 1.06, 0.01)
check('H0-1b I(R3)', 9 / (par(1000, 2200) + par(3300, 4700)) * 4700 / 8000, 2.01e-3, 0.01)
check('H0-1c V', -1e-3 * 1200, -1.2)
check('H0-1d R', par(1000, 2200) + par(3300, 4700), 2626, 0.002)
v, _ = solve([('V', 'A', 0, 9), ('R', 'A', 'B', 1000), ('R', 'B', 0, 2200), ('R', 'B', 0, 3300),
              ('R', 'A', 'C', 3300), ('R', 'C', 0, 2200), ('R', 'C', 0, 1000)])
check('H0-2 VCA', (v['C'] - v['A']).real, -7.448, 0.001)
check('H0-2 P(R1)', abs(v['A'] - v['B']) ** 2 / 1000, 15.05e-3, 0.002)

print('=== Homework 1 (2026 sheet: my answers) ===')
# 1a: Is into top node T, R1 T-X, R2 X-0, R3 X-0
check('H1-1a I(R2)', 1e-3 * 3300 / 5500, 0.6e-3)
# 1b
Rt, Rb = par(1000, 3300), par(2200, 4700)
VT = 3 * Rt / (Rt + Rb)
check('H1-1b I(R1)', VT / 1000, 1.016e-3, 0.004)
# 1c superposition
def h1c(Is, Vs):
    v, _ = solve([('I', 0, 'P', Is), ('R', 'P', 0, 1200), ('R', 'P', 'Q', 2200), ('R', 'Q', 0, 3300),
                  ('R', 'Q', 'S', 4700), ('V', 'S', 'W', Vs), ('R', 0, 'W', 5600)])
    return (0 - v['W']).real / 5600   # I(R5) arrow from the ground node to W
check('H1-1c (i)', h1c(1e-3, 0), -49.36e-6, 0.004)
check('H1-1c (ii)', h1c(0, 9), 0.7516e-3, 0.004)
check('H1-1c (iii)', h1c(1e-3, 9), 0.7022e-3, 0.004)
# 1d Norton
Vth = 12 * 3300 / 4300 * 3600 / (3600 + 1200 + par(1000, 3300))
Rn = par(3600, 1200 + par(1000, 3300))
check('H1-1d Rn', Rn, 1272.2, 0.002)
check('H1-1d In', Vth / Rn, 4.681e-3, 0.004)
check('H1-1d I(1k)', Vth / (Rn + 1000), 2.621e-3, 0.004)
# Q2 VCVS amplifier
def h1q2(RL):
    els = [('V', 1, 0, 0.1), ('R', 1, 'in', 50), ('R', 'in', 0, 10e3), ('VCVS', 'o', 0, 'in', 2, 1e5),
           ('R', 'o', 'out', 75), ('R', 'out', 2, 10e3), ('R', 2, 0, 2200)]
    if RL is not None: els.append(('R', 'out', 0, RL))
    return solve(els)
v, _ = h1q2(None)
check('H1-2 Voc', v['out'].real, 0.5518, 0.004)
v, _ = h1q2(1e-9)
check('H1-2 Isc', (v['out'] / 1e-9).real, 132.7, 0.05)
v, _ = h1q2(32)
check('H1-2 Vout', v['out'].real, 0.5517, 0.004)
check('H1-2 P(Vs)', (0.1 * (0.1 - v['in']) / 50).real, 0.1 ** 2 / 10050, 0.004)
check('H1-2 P(RL)', abs(v['out']) ** 2 / 32, 9.511e-3, 0.004)

print('=== Homework 1 2025 version (official) ===')
G = 1 / 1000 + 1 / 2200 + 1 / 3300
check('H1-25 1a', -1e-3 * (1 / 2200) / G, -259e-6, 0.005)
VM = 9 * par(2200, 4700) / (par(1000, 3300) + par(2200, 4700))
check('H1-25 1b', VM / 4700, 1.266e-3, 0.004)
def h125c(Is, Vs):
    v, _ = solve([('I', 0, 'P', Is), ('R', 'P', 0, 1200), ('R', 'P', 'Q', 2200), ('R', 'Q', 0, 3300),
                  ('R', 'Q', 'S', 4700), ('V', 'S', 0, Vs)])
    return ((v['Q'] - v['S']) / 4700).real
check('H1-25 1c i', h125c(1e-3, 0), 92.7e-6, 0.005)
check('H1-25 1c ii', h125c(0, 9), -1.41e-3, 0.005)
check('H1-25 1c iii', h125c(1e-3, 9), -1.32e-3, 0.006)
Vth = 12 * 3300 / 4300 - 12 * 3600 / 4800; Rn = par(1000, 3300) + par(1200, 3600)
check('H1-25 1d In', Vth / Rn, 125e-6, 0.006)
check('H1-25 1d Rn', Rn, 1667, 0.002)
check('H1-25 1d I1k', Vth / (Rn + 1000), 78.5e-6, 0.005)
Vin = 0.1 * 10e3 / 10050; A = 1e5; R1, R2 = 18e3, 2200
Vout = A * (R1 + R2) / (R1 + R2 + A * R2) * Vin
check('H1-25 2 Vout', Vout, 913.5e-3, 0.002)
check('H1-25 2 P(Vs)', 0.1 * 0.1 / 10050, 995e-9, 0.002)
check('H1-25 2 P(R1)', (Vout * R1 / (R1 + R2)) ** 2 / R1, 36.8e-6, 0.005)
check('H1-25 2 P(R2)', (Vout * R2 / (R1 + R2)) ** 2 / R2, 4.5e-6, 0.01)

print('=== Homework 2 (2026 sheet: my answers) ===')
cs = lambda *c: 1 / sum(1 / x for x in c)
check('H2-1a CAB', cs(1000e-12, 2000e-12, 3000e-12), 545.45e-12, 0.001)
v, _ = solve([('V', 1, 0, 1), ('R', 1, 2, 1000), ('R', 2, 'o', 10e3), ('VCCS', 'o', 0, 2, 0, 2.2e-3),
              ('R', 'o', 0, 100e3), ('R', 'o', 0, 5600)])
G1b = v['o'].real
check('H2-1b gain', G1b, -3.982, 0.003)
check('H2-1b max', abs(G1b) * 0.25, 0.9954, 0.003)
check('H2-1c Rth', par(100e3, 10100 / 200), 50.47, 0.002)
check('H2-1d Vc', rc_step(9, 5, 250e-6, 220e-6), 6.284, 0.002)
R1, R2, R3, R4, RL, Vs = 10e3, 10e3, 12e3, 12e3, 1000, 10
v, _ = solve([('V', 1, 0, Vs), ('R', 1, 2, R1), ('R', 0, 3, R2), ('R', 3, 4, R3), ('R', 4, 2, R4),
              ('R', 2, 0, RL), ('OPAMP', 2, 3, 4)])
check('H2-2 I(RL)', (v[2] / RL).real, 1e-3)
check('H2-2 e2', v[2].real, 1.0)
check('H2-2 e4', v[4].real, 2.2)

print('=== Homework 2 2025 version (official) ===')
check('H2-25 1a', cs(2e-9, 1e-9 + cs(2e-9, 2e-9)), 1e-9)
check('H2-25 1b', 2.2e-3 * par(50e3, 4700) * 0.5, 4.72, 0.003)
v, cur = solve([('V', 1, 0, 0), ('R', 1, 2, 50), ('V', 2, 'x', 0, 'Vb'), ('R', 'x', 4, 10e3),
                ('CCCS', 3, 4, 'Vb', 150), ('R', 3, 4, 80e3), ('R', 4, 0, 470), ('I', 0, 3, 1.0)])
check('H2-25 1c Rth', v[3].real, 616e3, 0.003)
check('H2-25 1d Rs', 32 * (100 / 40 - 1), 48)
check('H2-25 2 e3', (110e3 * 100e3 / (10e3 * 110e3)) * 1 - 10 * 0.5, 5.0, 0.01)

print('=== Homework 3 (2026 sheet: my answers) ===')
def zrep(label, Z, mag, ang):
    check(label + ' |Z|', abs(Z), mag, 0.002); check(label + ' angle', deg(Z), ang, 0.003)
w = 2 * pi * 50e3; Z = 1800 + 1 / (1j * w * 2200e-12)
zrep('H3-1a', Z, 2309.4, -38.79)
w = 2 * pi * 25e3; Z = par(1500, 1 / (1j * w * 3300e-12))
zrep('H3-1b', Z, 1184.2, -37.87)
w = 2 * pi * 30e3; Z = 1200 + par(2200, 1 / (1j * w * 3300e-12)) + 1 / (1j * w * 4700e-12)
zrep('H3-1c', Z, 2933.0, -47.92)
w = 2 * pi * 10e3; Zl = 1 / (1j * w * 3300e-12) + 4700
I = 0.5 / (1200 + 1j * w * 2200e-12 + Zl)
check('H3-1d avg P', 0.5 * abs(I) ** 2 * 4700, 10.12e-6, 0.004)
Vl = I * Zl
check('H3-1d peak P', (abs(Vl) * abs(I) / 2) * (1 + math.cos(cmath.phase(Zl))), 24.61e-6, 0.004)
w = 2 * pi * 25e3; Z1, Z2, Z3, Z4 = 1200, 2200, 1 / (1j * w * 3300e-12), 1 / (1j * w * 4700e-12)
H = Z4 / (Z1 + par(Z2, Z3) + Z4)
check('H3-2 |H|', abs(H), 0.4155, 0.003)
check('H3-2 angle deg', deg(H), -41.41, 0.003)

print('=== Homework 3 2025 version (official) ===')
Z = 1200 + 1j * 2 * pi * 250e3 * 1800e-6
check('H3-25 1a |Z|', abs(Z), 3071.5, 0.001); check('H3-25 1a ang', deg(Z), 67.0, 0.003)
Z = par(8200, 1 / (1j * 2 * pi * 500 * 100e-9))
check('H3-25 1b |Z|', abs(Z), 2967, 0.002); check('H3-25 1b ang', deg(Z), -68.8, 0.003)
tau = 18e-3 / 1200
check('H3-25 1c VL', math.exp(-20e-6 / tau), 0.264, 0.005)
check('H3-25 1c IL', (1 / 1200) * (1 - math.exp(-20e-6 / tau)), 614e-6, 0.003)
check('H3-25 1d Vc', 5 * (1 - math.exp(-100e-6 / 120e-6)), 2.83, 0.003)
check('H3-25 2 tau', 2200 * 330e-9, 726e-6)
check('H3-25 2 Vout1ms', -2.2 * (1 - math.exp(-1e-3 / 726e-6)), -1.64, 0.005)

print('=== Homework 4 (2026 sheet: my answers) ===')
w = 2 * pi * 12.75e3
check('H4-1a Cs', 1 / (25 * w ** 2 * 1e-6), 6.234e-6, 0.003)
check('H4-1a Pmax', 1 / (8 * 1000), 125e-6)
check('H4-1b IRS', (5 - 3.7) / 1000, 1.3e-3)
w = 2 * pi * 75e3
v, _ = solve([('V', 1, 0, 0.5), ('R', 1, 2, 2200), ('C', 2, 0, 2200e-12), ('R', 2, 3, 1000), ('C', 3, 0, 1000e-12)], w)
Ic2 = v[3] * 1j * w * 1000e-12
check('H4-1c |IC2|', abs(Ic2), 62.18e-6, 0.003)
check('H4-1c phase', deg(Ic2), -1.131, 0.004)
# 1d half-wave peak detector, piecewise-linear diode Vth 0.7, Ron = 0 -> track the source while it rises
def peak_det(A, f, Vth, RC):
    T = 1 / f; vmax = A - Vth
    # after the peak at T/4 the capacitor discharges until the rising sine (minus Vth) catches it
    best = None
    for k in range(1, 200001):
        t = T / 4 + k * T / 200000
        vc = vmax * math.exp(-(t - T / 4) / RC)
        if A * math.sin(2 * pi * f * t) - Vth >= vc and t > T: best = vc; break
    return vmax, best
mx, mn = peak_det(5, 1e3, 0.7, 1e-3)
check('H4-1d max', mx, 4.3)
check('H4-1d min', mn, 1.864, 0.004)
R1, L2, R3, C4 = 1200, 1200e-9, 2200, 2200e-12
H = lambda f: -(par(R3, 1 / (1j * 2 * pi * f * C4))) / (R1 + 1j * 2 * pi * f * L2)
check('H4-2 |H(1k)|', abs(H(1e3)), 1.8333, 0.002)
f3 = 1 / (2 * pi * R3 * C4)
check('H4-2 f3dB', f3, 32.88e3, 0.002)
check('H4-2 |H(f3)|', abs(H(f3)), 1.2964, 0.002)
check('H4-2 phase(f3)', deg(H(f3)), 134.99, 0.002)

print('=== Final 2025 (official) ===')
v, _ = solve([('V', 'T', 0, 9), ('R', 'T', 'A', 1200), ('R', 'A', 0, 2200), ('R', 'T', 'B', 3300), ('R', 'B', 0, 4700), ('R', 'A', 'B', 5600)])
check('F2025-1a', ((v['A'] - v['B']) / 5600).real, 64.46e-6, 0.002)
v, _ = solve([('V', 's', 0, 0), ('R', 's', 'm', 50), ('V', 'm', 'x', 0, 'Vp'), ('R', 'x', 'A', 5600), ('CCCS', 0, 'A', 'Vp', 200), ('R', 'A', 0, 100e3), ('I', 0, 'A', 1.0)])
check('F2025-1b Rth', v['A'].real, 28.1, 0.003)
check('F2025-1c n', math.sqrt(50 / 32), 1.25)
w = 2 * pi * 1e3; Z = 6 + 1j * w * 430e-6 + par(137, 1 / (1j * w * 252e-6))
check('F2025-1d |Z|', abs(Z), 6.35, 0.003); check('F2025-1d ang', deg(Z), 19.0, 0.005)
check('F2025-1e', 230 / 23 - 1.4, 8.6)
RC = 10e3 * 470e-12
for f, A, wantA, wantP in ((1e3, 5, 4.998, -0.0295), (1e6, 10, 0.3384, -1.537)):
    H = 1 / (1 + 1j * 2 * pi * f * RC)
    check(f'F2025-2 amp {f:g}', A * abs(H), wantA, 0.002); check(f'F2025-2 phase {f:g}', cmath.phase(H), wantP, 0.003)
# full circuit check of the Q2 simplification
R, C = 10e3, 470e-12
for f in (1e3, 1e6):
    w = 2 * pi * f
    v, _ = solve([('V', 'i', 0, 1), ('R', 'i', 'p', R), ('R', 'p', 0, R), ('C', 'p', 0, C), ('OPAMP', 'p', 'n', 'o'),
                  ('R', 'n', 0, R), ('R', 'n', 'o', R), ('C', 'n', 'o', C)], w)
    check(f'F2025-2 circuit = 1/(1+jwCR) at {f:g}', v['o'], 1 / (1 + 1j * w * C * R), 1e-9)
tau = 10e3 * 22e-9; x = math.exp(-100e-6 / tau)
check('F2025-3 Vmax', 8 / (1 + x), 4.894, 0.001); check('F2025-3 Vmin', 8 * x / (1 + x), 3.106, 0.001)

print('=== Final 2024 (my answers) ===')
def e2_2024(t, A1=5, A2=2):
    G = 1 / 1200 + 1 / 2200 + 1 / 3300
    return (A1 * math.sin(2000 * pi * t) / 1200 + A2 * math.cos(5000 * pi * t) / 3300) / G
check('F2024-1a k1', (1 / 1200) / (1 / 1200 + 1 / 2200 + 1 / 3300), 0.5238, 0.002)
check('F2024-1a e2(1.25ms)', e2_2024(1.25e-3), 2.888, 0.002)
tau = 0.1 / 1215; i100 = 5 / 1215 * (1 - math.exp(-100e-6 / tau))
check('F2024-1b |I(200us)|', i100 * math.exp(-100e-6 / tau), 0.8587e-3, 0.003)
check('F2024-1d Cs', 1 / ((2 * pi * 10e3) ** 2 * 1e-3), 253.3e-9, 0.002)
check('F2024-1e (i)', 0.25 + 0.5, 0.75)
R, C = 10e3, 1e-9
f0 = 1 / (3 * pi * R * C)
check('F2024-2 f0', f0, 10.61e3, 0.002)
v, _ = solve([('V', 'i', 0, 1), ('R', 'i', 1, R), ('R', 1, 2, R), ('OPAMP', 0, 2, 3), ('R', 2, 3, 2 * R), ('C', 1, 3, C)], 2 * pi * f0)
check('F2024-2 |H(f0)|', abs(v[3]), 0.7071, 0.001); check('F2024-2 phase', deg(v[3]), 135.0, 0.001)
w = 2 * pi * 1e3; Zl = par(10 + 1j * w * 0.22, 1 / (1j * w * 100e-9))
check('F2024-3 Re', Zl.real, 577.2, 0.003); check('F2024-3 Im', Zl.imag, 10486, 0.004)
n = 10; Zp = n * n * Zl; e2 = 1 * Zp / (100 + Zp)
check('F2024-3 |e3| (n=10 assumed)', abs(e2) / n, 0.09996, 0.003)

print('=== Final 2023 (my answers) ===')
w = 2 * pi * 50; Z = 100 + 1j * w * 0.5; V2 = 325 / 65
check('F2023-1a P', 0.5 * V2 ** 2 * 100 / abs(Z) ** 2, 36.05e-3, 0.003)
v, _ = solve([('R', 1, 'a', 2000), ('V', 'a', 0, 1), ('R', 1, 2, 1000), ('R', 2, 'b', 2000), ('V', 'b', 0, 1), ('R', 2, 0, 2000)])
check('F2023-1b e1', v[1].real, 0.75, 0.002); check('R2024-1b e2', v[2].real, 0.625, 0.002)
tau = 0.1 / 2200
check('F2023-1c e3', 1200 * (2 - 1 * math.exp(-50e-6 / tau)) / 2200, 0.9093, 0.002)
check('F2023-1e f3dB', 1 / (2 * pi * 100e3 * 10e-12), 159.15e3, 0.002)
check('F2023-3 gm', 10 / (10e3 - 10 * 500), 2e-3)
v, _ = solve([('V', 's', 0, 1), ('R', 's', 'g', 1000), ('VCCS', 'd', 'S', 'g', 'S', 2e-3), ('R', 'S', 0, 500), ('R', 'd', 0, 10e3)])
check('F2023-3 H with gm', v['d'].real, -10, 1e-6)

print('=== Final 2022 (my answers) ===')
w = 2 * pi * 50
check('F2022-1a P', 0.5 * 325 ** 2 * 100 / (110 ** 2 + (w * 0.5) ** 2), 143.6, 0.003)
v, _ = solve([('V', 1, 4, 1), ('R', 1, 2, 2000), ('R', 2, 4, 3000), ('R', 3, 4, 5000), ('I', 3, 2, 0.5e-3), ('R', 4, 0, 1e9)])
check('F2022-1b V24', (v[2] - v[4]).real, 1.2, 0.001); check('R2023-1b V12', (v[1] - v[2]).real, -0.2, 0.001)
check('F2022-1c e2', 2 - math.exp(-1e-3 / (2200 * 470e-9)), 1.6198, 0.002)
Z = 40 + 1j * 2 * pi * 1e3 * 18e-3
check('F2022-1d |Z|', abs(Z), 119.97, 0.002); check('F2022-1d ang', deg(Z), 70.52, 0.002)
H = -33 / (1 + 1j * 2 * pi * 50e3 * 330e3 * 10e-12)
check('F2022-1e amp', 0.05 * abs(H), 1.1455, 0.002); check('F2022-1e phase', deg(H), 133.97, 0.002)
w = 2 * pi * 7e3
e1 = 1j * w * 100e-6 * 10e3 / (1 + 1j * w * 100e-6 * 10e3)
Z45 = par(10e3, 1 / (1j * w * 1e-9))
Vo = e1 * (1 + Z45 / 1e3)
check('F2022-2 amp', abs(Vo), 10.077, 0.003); check('F2022-2 phase', deg(Vo), -21.6, 0.01)

print('=== Final 2021 (my answers) ===')
check('F2021-1a P', (0.5) ** 2 / (2 * 1000), 125e-6)
v, _ = solve([('V', 1, 0, 1), ('R', 1, 2, 2000), ('R', 2, 0, 3000), ('V', 2, 3, 4), ('R', 3, 0, 5000)])
check('F2021-1b e2', v[2].real, 1.2581, 0.002)
check('F2021-1c i4', 0.25e-3 * (1 - math.exp(-1e-6 / 0.75e-6)), 184.1e-6, 0.002)
w = 2 * pi * 1e3; Z = 1300 + 1j * w * 18e-3 + 1 / (1j * w * 100e-9)
check('F2021-1d |Z|', abs(Z), 1968.7, 0.002); check('F2021-1d ang', deg(Z), -48.67, 0.002)
H = -4 / (1 + 1j * 2 * pi * 30e3 * 4000 * 2000e-12)
check('F2021-1e amp', abs(H), 2.2105, 0.002); check('F2021-1e phase', deg(H), 123.55, 0.002)
w = 2 * pi * 10e3; Zf = par(10e3, 1 / (1j * w * 1e-9)); H2 = Zf / 1e3
check('F2021-2 amp', abs(H2) * (2 - 1), 8.467, 0.002); check('F2021-2 phase', deg(H2), -32.14, 0.003)
v, _ = solve([('V', 'a', 0, 1), ('R', 'a', 'n', 1e3), ('R', 'n', 'o', 10e3), ('C', 'n', 'o', 1e-9),
              ('V', 'b', 0, 2), ('R', 'b', 'p', 1e3), ('R', 'p', 0, 10e3), ('C', 'p', 0, 1e-9), ('OPAMP', 'p', 'n', 'o')], w)
check('F2021-2 circuit', v['o'], H2 * 1, 1e-9)
# Q3 peak detector with Rs: ideal diode, A=5, Rs=10, RL=1k, C=100u, 50 Hz
def pd(t, vc, A=5, f=50, Rs=10, RL=1000, C=100e-6):
    vs = A * math.sin(2 * pi * f * t)
    i = max(0.0, (vs - vc) / Rs)
    return (i - vc / RL) / C
ts, ys = simulate(pd, 0.0, 1 / 50, 4000, 40)
check('F2021-3 max', ys.max(), 4.793, 0.004)
check('F2021-3 min', ys.min(), 4.038, 0.006)

print('=== Resit 2025 (my answers) ===')
G = 1 / 1200 + 1 / 2200 + 1 / 3300
e2 = lambda t: (2 * math.sin(2000 * pi * t) / 1200 + 5 * math.cos(5000 * pi * t) / 3300) / G
check('R2025-1a i1(1ms)', (2 * math.sin(2 * pi) - e2(1e-3)) / 1200, 0.7937e-3, 0.003)
tau = 0.1 / 1215; i50 = 2 / 1215 * (1 - math.exp(-50e-6 / tau)); i100 = i50 * math.exp(-50e-6 / tau)
check('R2025-1b e2(100us)', 0 - 1200 * i100, -0.4899, 0.004)
w = 2 * pi * 10e3
check('R2025-1d Cs', 1 / (w ** 2 * 18e-3), 14.07e-9, 0.002); check('R2025-1d Pmax', 4 / (8 * 50), 10e-3)
check('R2025-1e (i)', 0.35 + 0.65, 1.0)
R, C = 10e3, 4e-9; f0 = 3 / (10 * pi * R * C)
check('R2025-2 f0', f0, 2387.3, 0.002)
v, _ = solve([('V', 'i', 0, 1), ('R', 'i', 1, R), ('R', 1, 2, 2 * R), ('OPAMP', 0, 2, 3), ('R', 2, 3, 3 * R), ('C', 1, 3, C)], 2 * pi * f0)
check('R2025-2 |H|', abs(v[3]), 0.7071, 0.001); check('R2025-2 phase', deg(v[3]), 135, 0.001)
w = 2 * pi * 1e3; Zl = par(15 + 1j * w * 0.18, 1 / (1j * w * 120e-9))
check('R2025-3 Re', Zl.real, 687.6, 0.003); check('R2025-3 Im', Zl.imag, 7627, 0.004)
Zp = 100 * Zl; check('R2025-3 |e3|', abs(Zp / (100 + Zp)) / 10, 0.09996, 0.003)

print('=== Resit 2024 (my answers) ===')
w = 2 * pi * 50; Z = 200 + 1j * w * 1.0
check('R2024-1a P', 0.5 * 25 * 200 / abs(Z) ** 2, 18.03e-3, 0.003)
tau = 0.1 / 2500
check('R2024-1c I(R4)', (2 / 2500) * (1 - math.exp(-50e-6 / tau)), 0.5708e-3, 0.003)
check('R2024-1e gain dB', 20 * math.log10(180 / 22), 18.26, 0.002)
check('R2024-1e f3dB', 1 / (2 * pi * 180e3 * 100e-12), 8842, 0.002)
R, C = 10e3, 1e-9; f0 = 1 / (2 * pi * R * C)
check('R2024-2 f0', f0, 15.915e3, 0.002)
w = pi * f0; H = 1 / (1 + 1j * w * C * 2 * R - w * w * R * R * C * C)
check('R2024-2 amp at f0/2', abs(H), 0.8, 0.002); check('R2024-2 phase', deg(H), -53.13, 0.002)
v, _ = solve([('V', 'i', 0, 1), ('R', 'i', 1, R), ('R', 1, 2, R), ('C', 2, 0, C), ('C', 1, 3, C), ('OPAMP', 2, 3, 3)], w)
check('R2024-2 circuit', v[3], H, 1e-9)
g = 10 ** 1.5
check('R2024-3 gm', g / (22e3 - g * 470), 4.430e-3, 0.003)

print('=== Resit 2023 (my answers) ===')
w = 2 * pi * 50; Zl = par(100, 1 / (1j * w * 220e-6)); VA = 325 * Zl / (10 + Zl)
check('R2023-1a P', 0.5 * abs(VA) ** 2 / 100, 312.9, 0.003)
check('R2023-1c e2', math.exp(-0.5e-3 / (1800 * 560e-9)), 0.6089, 0.002)
f = 40 / (2 * pi * 18e-3)
check('R2023-1d f', f, 353.68, 0.002); check('R2023-1d |Z|', 40 * math.sqrt(2), 56.57, 0.002)
H = -(33 / 4.7) / (1 + 1j * 2 * pi * 400e3 * 33e3 * 12e-12)
check('R2023-1e amp', 0.1 * abs(H), 0.4977, 0.003); check('R2023-1e phase', deg(H), 135.14, 0.003)
for f, wa, wp in ((1e3, 20.47, -14.91), (10e3, 11.25, -56.27)):
    w = 2 * pi * f; H = 1 + par(10e3, 1 / (1j * w * 4.7e-9)) / 1e3
    check(f'R2023-2 dB {f:g}', 20 * math.log10(abs(H)), wa, 0.003); check(f'R2023-2 phase {f:g}', deg(H), wp, 0.01)

print('=== Resit 2022 (my answers) ===')
v, _ = solve([('V', 1, 0, 5), ('R', 1, 2, 4000), ('R', 2, 0, 3000), ('V', 2, 3, 2), ('R', 3, 0, 5000)])
check('R2022-1b e3', v[3].real, 0.1064, 0.004)
check('R2022-1c e3', 1 - math.exp(-2), 0.8647, 0.001)
w = 2 * pi * 4000; Z = 40 + 1j * w * 18e-3 + 1 / (1j * w * 82e-9)
check('R2022-1d |Z| value', abs(Z), 51.75, 0.003); check('R2022-1d ang', deg(Z), -39.39, 0.003)
H = -(8200 / 3300) / (1 + 1j * 2 * pi * 10e3 * 8200 * 2200e-12)
check('R2022-1e amp', 2 * abs(H), 3.288, 0.003); check('R2022-1e phase', deg(H), 131.6, 0.003)
check('R2022-2 Vout', 5 * (1.2 - (-0.8)), 10)
check('R2022-3 Imax', 1 / 5010, 199.6e-6, 0.002)

print('=== Resit 2021 (my answers) ===')
check('R2021-1a P', 3 * 1e-3, 3e-3)
v, _ = solve([('V', 1, 0, 1), ('R', 1, 2, 2000), ('R', 2, 0, 3000), ('I', 0, 2, 4e-3)])
check('R2021-1b I(R2)', ((v[1] - v[2]) / 2000).real, -2.2e-3, 0.001)
check('R2021-1c I(L4)', 0.5e-3 * (1 - math.exp(-5e-6 / (4e-3 / 1200))), 388.4e-6, 0.002)
w = 2 * pi * 200e3; Y = 1 / (4700 + 1j * w * 10e-3 + 1 / (1j * w * 100e-12))
check('R2021-1d |Y|', abs(Y), 151.9e-6, 0.004); check('R2021-1d ang', deg(Y), -44.44, 0.003)
w = 2 * pi * 10e3; H = (1j * w * 2000e-12 * 3000) / (1 + 1j * w * 2000e-12 * 3000) * (1 + 5000 / 4000)
check('R2021-1e amp', abs(H), 0.7937, 0.003); check('R2021-1e phase', deg(H), 69.34, 0.003)
w = 1e6; Zp = par(1j * w * 1e-3, 1000); H = Zp / (1000 + 1 / (1j * w * 1000e-12) + Zp)
check('R2021-2 Vm', abs(H), 0.4472, 0.002); check('R2021-2 phi(cos form, deg)', deg(H) - 90, -26.57, 0.002, atol=1e-6)

print('=== Topic notes extras (my answers) ===')
check('T3 H0-2 P(R2) at 9V', (9 * 1320 / 2320) ** 2 / 2200, 11.92e-3, 0.003)
check('T3 E6-2 20ohm', 5 * 20 / 40, 2.5); check('T3 E6-2 200ohm', 5 * 200 / 220, 4.545, 0.002)
v, _ = solve([('V', 1, 0, 3), ('R', 1, 2, 1e3), ('R', 2, 0, 10e3), ('R', 2, 3, 1e3), ('R', 3, 0, 2e3), ('R', 3, 4, 2e3), ('R', 4, 0, 4e3)])
check('T3 E6-3 e3', v[3].real, 1.2); check('T3 E6-3 e4', v[4].real, 0.8)
check('T3 H0-1b total I', 9 / 2626.25, 3.427e-3, 0.001)
check('T4 bridge Thevenin I', 9 * (2200 / 3400 - 4700 / 8000) / (par(1200, 2200) + par(3300, 4700) + 5600), 64.46e-6, 0.002)
check('T4 R2025-1a coeff', 2 * (1 - (1 / 1200) / (1 / 1200 + 1 / 2200 + 1 / 3300)) / 1200, 0.7937e-3, 0.002)
check('T4 E8-4 i', 12 * (1000 / 1900 - 0.5) / (par(900, 1000) + 500 + 10e3), 28.78e-6, 0.003)
check('T5 F2021-1b e3', 39 / 31 - 4, -2.742, 0.002)
check('T5 M2', 10 / 2.5, 4.0)
v, _ = solve([('I', 0, 1, 2e-3), ('R', 1, 0, 1e3), ('R', 1, 2, 2e3), ('R', 2, 0, 2e3)])
check('T5 M3 e1', v[1].real, 1.6); check('T5 M3 e2', v[2].real, 0.8)
check('T6 HX2-1c formula', 80e3 * (1 + 150 * 470 / (470 + 10050)) + par(470, 10050), 616e3, 0.002)
check('T6 E10-4 vL/vs', (1e4 / 10100) * 1000 * 4 / 12, 330, 0.002)
check('T6 E10-4 Pmax', (1000 * 0.02 * 1e4 / 10100) ** 2 / 32, 12.25, 0.003)
check('T6 E10-4 dB', 20 * math.log10((1e4 / 10100) * 1000 * 0.5), 53.9, 0.002)
check('T6 M3', 0.9 * 50 * 0.9, 40.5)
v, _ = solve([('V', 'i', 0, 0.2), ('OPAMP', 'i', 'n', 'o'), ('R', 'n', 0, 1e3), ('R', 'n', 'o', 9e3)])
check('T7 M3 vo', v['o'].real, 2.0)
A = 2e5; Ri, Ro, R1, Rf = 2e6, 75, 10e3, 50e3
check('T7 E14-2', Ri * (Ro - A * Rf) / ((R1 + Ri) * (Ro + Rf) + (1 + A) * R1 * Ri), -4.99985, 1e-5)
v, _ = solve([('V', 'a', 0, -0.8), ('R', 'a', 'n', 1e3), ('R', 'n', 'o', 5e3), ('V', 'b', 0, 1.2), ('R', 'b', 'p', 1e3), ('R', 'p', 0, 5e3), ('OPAMP', 'p', 'n', 'o')])
check('T7 R2022-2 Vout circuit', v['o'].real, 10.0)
check('T8 H2-1a', 6000e-12 / 11, 545.5e-12, 0.001)
check('T8 E15-5', cs(2, 3), 1.2); check('T8 E16-3', 2 + par(2, 2 + par(1, 1)), 28 / 9)
check('T8 M3 L', 0.5 * 0.1 * 0.02 ** 2, 20e-6); check('T8 M3 C', 0.5 * 470e-9 * 100, 23.5e-6)
check('T9 F2023-1c i', 2 / 2200 - (1 / 2200) * math.exp(-50 / 45.4545), 0.7578e-3, 0.002)
check('T9 R2025-1b i50', 2 / 1215 * (1 - math.exp(-50e-6 / (0.1 / 1215))), 0.750e-3, 0.003)
check('T9 R2023-1c', math.exp(-0.5 / 1.008), 0.609, 0.002)
check('T9 M2', 5 * (1 - math.exp(-1)), 3.16, 0.002); check('T9 M3', 2e-3 * math.exp(-2), 0.271e-3, 0.002)
check('T9 R2021-1c Thevenin', 0.6 / 1200, 0.5e-3)
w = 2 * pi * 1e3; C1, R2c, C2 = 1e-9, 1e3, 2e-9
Zf = (1 + 1j * w * R2c * C2) / (1j * w * (C1 + C2) - w * w * R2c * C1 * C2)
check('T11 Z12 formula vs direct', Zf, par(1 / (1j * w * C1), R2c + 1 / (1j * w * C2)), 1e-9)
check('T11 Y12 formula', 1j * w * C1 + 1j * w * C2 / (1 + 1j * w * R2c * C2), 1 / Zf, 1e-9)
check('T11 R2023-1d f', 40 / (2 * pi * 0.018), 353.7, 0.001)
check('T11 HX3-1b wRC', 2 * pi * 500 * 8200 * 100e-9, 2.576, 0.001)
check('T11 M3 I', 10 / abs(1000 + 1 / (1j * 2 * pi * 1e3 * 159e-9)), 7.07e-3, 0.003)
check('T10 E20-2 Vo', -par(1e3, 1 / (1j * 1000 * 2e-6)) / 500 * 5, -2 + 4j, 1e-6)
check('T10 E20-1 phase', cmath.phase(5 / (1 + 20j)), -1.52, 0.003)
w = 2 * pi * 10e3; Z = 1200 + 1j * w * 2200e-12 + 1 / (1j * w * 3300e-12) + 4700; I = 0.5 / Z
check('T12 H3-1d |I|', abs(I), 65.6e-6, 0.002)
check('T12 R2025-1d Pmax direct', 0.5 * (2 / 100) ** 2 * 50, 10e-3)
check('T12 M2', 100 / 400, 0.25)
w = 2 * pi * 1e3; Z = 100 + 1j * w * 0.01
check('T12 M3 P', 0.5 * (10 / abs(Z)) ** 2 * 100, 0.359, 0.003); check('T12 M3 pf', 100 / abs(Z), 0.847, 0.002)
I1 = 80 / (30 + 20j + 9 * (5 - 8j)); check('T13 E22-3 Vc', 3 * abs(I1) * 8, 21.04, 0.002)
check('T13 E22-3 phase rad', math.radians(math.degrees(cmath.phase(I1)) - 90), -0.965, 0.003)
check('T13 F2024 f0', 1 / (2 * pi * math.sqrt(0.22 * 100e-9)), 1073, 0.002)
check('T13 R2025 f0', 1 / (2 * pi * math.sqrt(0.18 * 120e-9)), 1083, 0.002)
check('T13 R2022 f0', 1 / (2 * pi * math.sqrt(18e-3 * 82e-9)), 4144, 0.002)
check('T13 H4-1a reflected X', 25 * 2 * pi * 12.75e3 * 1e-6, 2.003, 0.002)
check('T13 M2', math.sqrt(75), 8.66, 0.001); check('T13 M3 f0', 1 / (2 * pi * math.sqrt(1e-8)), 1592, 0.001)
# Topic 14/15 extra checks
w = 1e6; L, C, Rs, RL = 1e-3, 1e-9, 1e3, 1e3
Hf = -w * w * L * C * RL / (RL - w * w * L * C * (Rs + RL) + 1j * w * (L + C * Rs * RL))
check('T14 R2021-2 formula', Hf, par(1j * w * L, RL) / (Rs + 1 / (1j * w * C) + par(1j * w * L, RL)), 1e-9)
check('T14 E24-1 f0', 1 / (2 * pi * math.sqrt(25.33e-6 * 1e-9)), 1.000e6, 0.002)
check('T14 E24-1 BW', 1 / (2 * pi * 2387 * 1e-9), 66.67e3, 0.002)
check('T14 M2', 1 / (2 * pi * 1e-4), 1592, 0.001); check('T14 M3', 2 * abs(1 / (1 + 1j * 5000 / 1591.5)), 0.607, 0.003)
for a, b in ((1, 2), (2, 3), (1.5, 4)):
    R, C, w = 10e3, 1e-9, 2 * pi * 7e3
    v, _ = solve([('V', 'i', 0, 1), ('R', 'i', 1, R), ('R', 1, 2, a * R), ('OPAMP', 0, 2, 3), ('R', 2, 3, b * R), ('C', 1, 3, C)], w)
    check(f'T15 Eq75 a={a} b={b}', v[3], -(b / (1 + a)) / (1 + 1j * w * C * R * (a + b) / (1 + a)), 1e-9)
R1, R2, C3, C4, w = 4e3, 7e3, 2e-9, 3e-9, 2 * pi * 9e3
Z1, Z2, Z3, Z4 = R1, R2, 1 / (1j * w * C3), 1 / (1j * w * C4)
v, _ = solve([('V', 'i', 0, 1), ('R', 'i', 1, R1), ('R', 1, 2, R2), ('C', 2, 0, C4), ('C', 1, 3, C3), ('OPAMP', 2, 3, 3)], w)
check('T15 Sallen-Key Z form', v[3], Z3 * Z4 / (Z1 * Z2 + Z3 * (Z1 + Z2) + Z3 * Z4), 1e-9)
check('T15 Sallen-Key RC form', v[3], 1 / (1 - w * w * R1 * R2 * C3 * C4 + 1j * w * C4 * (R1 + R2)), 1e-9)
check('T15 F2023-1e f3', 1 / (2 * pi * 100e3 * 10e-12), 159.2e3, 0.001)
check('T15 R2024-1e f3', 1 / (2 * pi * 180e3 * 100e-12), 8842, 0.002)
check('T15 M2 f3', 1 / (2 * pi * 50e3 * 100e-12), 31.8e3, 0.002)
# Topics 16-18
check('T16 R2025-1e current', (5 - 1.0) / 20e3, 0.2e-3)
check('T16 E26-2 (i)', 0.5 / 2, 0.25)
check('T16 M2', (9 - 0.7) / 1e3, 8.3e-3)
f_ = lambda t: 5 * math.sin(2 * pi * 1e3 * t) - 0.7 - 4.3 * math.exp(-(t - 0.25e-3) / 1e-3)
lo, hi = 1.0e-3, 1.25e-3
for _ in range(60):
    mid = (lo + hi) / 2; lo, hi = (mid, hi) if f_(mid) < 0 else (lo, mid)
check('T17 H4-1d crossing t', lo, 1.086e-3, 0.002); check('T17 H4-1d min exact', 4.3 * math.exp(-(lo - 0.25e-3) / 1e-3), 1.864, 0.003)
check('T17 F2021-3 min est', 4.79 * math.exp(-0.017 / 0.1), 4.04, 0.003)
check('T17 M3', 6 * math.exp(-0.2), 4.91, 0.002)
check('T18 E25-2 res', 10 / 255, 0.0392, 0.002); check('T18 E25-2 err%', 100 * 10 / 255 / 2 / 10, 0.196, 0.002)

print()
print('FAILS:', fails)
sys.exit(1 if fails else 0)
