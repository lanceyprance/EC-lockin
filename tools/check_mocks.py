"""Recompute every number in mock/final-1.md, final-2.md, final-3.md.

Usage: python3 tools/check_mocks.py        (-v to print every value)
"""
import cmath, math, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from mna import solve, par

pi = math.pi
fails = 0
VERBOSE = '-v' in sys.argv


def check(label, got, want, rtol=0.006, atol=1e-12):
    global fails
    ok = abs(got - want) <= rtol * abs(want) + atol
    if not ok: fails += 1
    if VERBOSE or not ok:
        print(f"{'OK  ' if ok else 'FAIL'} {label}: got {got:.6g} want {want:.6g}")


def deg(z): return math.degrees(cmath.phase(z))


def bisect(f, lo, hi, n=80):
    flo = f(lo)
    for _ in range(n):
        mid = (lo + hi) / 2
        if (f(mid) < 0) == (flo < 0): lo, flo = mid, f(mid)
        else: hi = mid
    return (lo + hi) / 2


print('=== Mock 1 ===')
v, _ = solve([('V', 'T', 0, 12), ('R', 'T', 'A', 1e3), ('R', 'A', 0, 2e3), ('R', 'T', 'B', 2e3), ('R', 'B', 0, 1e3), ('R', 'A', 'B', 3e3)])
check('M1-1a I(R5)', ((v['A'] - v['B']) / 3e3).real, 0.9231e-3)
check('M1-1a Vth', 12 * (2 / 3 - 1 / 3), 4.0); check('M1-1a Rth', par(1e3, 2e3) * 2, 1333.3, 0.001)
tau = 2.2e3 * 100e-9
v200 = 3 * (1 - math.exp(-200e-6 / tau))
check('M1-1b v200', v200, 1.791, 0.002); check('M1-1b v300', v200 * math.exp(-100e-6 / tau), 1.135, 0.002)
w = 2 * pi * 2e3; Zp = par(1j * w * 2e-3, 1 / (1j * w * 1e-6)); Z = 50 + Zp
check('M1-1c |Z|', abs(Z), 62.04, 0.002); check('M1-1c ang', deg(Z), 36.30, 0.003)
w = 2 * pi * 50; Zl = 50 + 1 / (1j * w * 100e-6); I = 325 / abs(5 + Zl)
check('M1-1d P', 0.5 * I ** 2 * 50, 653.9, 0.003)
R2, R4, C3 = 4.7e3, 47e3, 3.3e-9
check('M1-1e dB', 20 * math.log10(R4 / R2), 20.0, 0.001); check('M1-1e f3', 1 / (2 * pi * R4 * C3), 1026.2, 0.002)
H = -(R4 / R2) / (1 + 1j * 2 * pi * 1e3 * R4 * C3)
check('M1-1e amp', 0.1 * abs(H), 0.7162, 0.002); check('M1-1e phase', deg(H), 135.74, 0.002)
R1 = R2s = 4.7e3; C3, C4 = 10e-9, 4.7e-9
w0 = 1 / math.sqrt(R1 * R2s * C3 * C4)
check('M1-2 f0', w0 / (2 * pi), 4934, 0.002)
Hs = lambda w: 1 / (1 - w * w * R1 * R2s * C3 * C4 + 1j * w * C4 * (R1 + R2s))
check('M1-2 |H(f0)|', abs(Hs(w0)), 0.7294, 0.002); check('M1-2 phase', deg(Hs(w0)), -90, 0.001)
v, _ = solve([('V', 'i', 0, 1), ('R', 'i', 1, R1), ('R', 1, 2, R2s), ('C', 2, 0, C4), ('C', 1, 3, C3), ('OPAMP', 2, 3, 3)], w0)
check('M1-2 circuit', abs(v[3]), abs(Hs(w0)), 1e-6)
check('M1-2 amp A=2', 2 * abs(Hs(w0)), 1.459, 0.002)
check('M1-2 dB at 10 f0', 20 * math.log10(abs(Hs(10 * w0))), -40.03, 0.003)
check('M1-3 max', 2 + 0.7, 2.7); check('M1-3 min', -(3 + 0.7), -3.7)
check('M1-3 I(Rs) at peak', (6 - 2.7) / 1e3, 3.3e-3)
check('M1-3 clip start angle', math.degrees(math.asin(2.7 / 6)), 26.74, 0.002)

print('=== Mock 2 ===')
v, _ = solve([('V', 1, 0, 6), ('R', 1, 2, 1e3), ('R', 2, 0, 2e3), ('V', 2, 3, 3), ('R', 3, 0, 3e3), ('I', 0, 3, 1e-3)])
check('M2-1a e2', v[2].real, 4.3636, 0.002); check('M2-1a e3', v[3].real, 1.3636, 0.002)
check('M2-1b i', 4e-3 * (1 - math.exp(-1)), 2.528e-3, 0.002)
w = 2 * pi * 1e3; Zl = 4 + 1j * w * 1e-3; Zp = 25 * Zl; I1 = 10 / abs(200 + Zp)
check('M2-1c P', 0.5 * I1 ** 2 * Zp.real, 43.60e-3, 0.003)
check('M2-1c n for match (R only)', math.sqrt(200 / 4), 7.071, 0.001)
w = 1e4; Y = 1 / 100 + 1 / (50 + 1j * w * 5e-3)
check('M2-1d |Y|', abs(Y), 22.36e-3, 0.003); check('M2-1d ang', deg(Y), -26.57, 0.01)
check('M2-1e both low', 0.2 + 0.6, 0.8); check('M2-1e one low', 0.2 + 0.6, 0.8)
check('M2-1e current both low', (5 - 0.8) / 10e3, 0.42e-3)
R, C = 4.7e3, 2.2e-9
f0 = 1 / (2 * pi * 2 * R * C)
check('M2-2 f0', f0, 7695, 0.002)
v, _ = solve([('V', 'i', 0, 1), ('R', 'i', 1, R), ('R', 1, 2, R), ('OPAMP', 0, 2, 3), ('R', 2, 3, 3 * R), ('C', 1, 3, C)], 2 * pi * f0)
check('M2-2 |H(f0)|', abs(v[3]), 1.5 / math.sqrt(2), 0.001); check('M2-2 phase f0', deg(v[3]), 135, 0.001)
v, _ = solve([('V', 'i', 0, 1), ('R', 'i', 1, R), ('R', 1, 2, R), ('OPAMP', 0, 2, 3), ('R', 2, 3, 3 * R), ('C', 1, 3, C)], 2 * pi * 2 * f0)
check('M2-2 amp at 2f0 (A=0.5)', 0.5 * abs(v[3]), 0.3354, 0.002); check('M2-2 phase 2f0', deg(v[3]), 116.57, 0.002)
f = 60; T = 1 / f; A, Vth, RC = 10, 0.7, 500 * 470e-6
vmax = A - Vth
g = lambda t: A * math.sin(2 * pi * f * t) - Vth - vmax * math.exp(-(t - T / 4) / RC)
tc = bisect(g, T, T + T / 4)
check('M2-3 max', vmax, 9.3); check('M2-3 min', vmax * math.exp(-(tc - T / 4) / RC), 8.697, 0.003)
check('M2-3 recharge time', (tc - T) * 1e3, 3.241, 0.01)

print('=== Mock 3 ===')
v, _ = solve([('V', 'i', 0, 0), ('R', 'i', 'X', 1e3), ('R', 'X', 0, 9e3), ('VCCS', 'O', 0, 'X', 0, 10e-3), ('R', 'O', 0, 20e3), ('R', 'O', 'X', 100e3), ('I', 0, 'O', 1.0)])
check('M3-1a Rth', v['O'].real, 6707, 0.003)
v, _ = solve([('V', 'i', 0, 1), ('R', 'i', 'X', 1e3), ('R', 'X', 0, 9e3), ('VCCS', 'O', 0, 'X', 0, 10e-3), ('R', 'O', 0, 20e3), ('R', 'O', 'X', 100e3)])
check('M3-1a Voc gain', v['O'].real, -59.76, 0.003)
cs = lambda *c: 1 / sum(1 / x for x in c)
Ceq = cs(10e-9, 4.7e-9 + 2.2e-9, 22e-9)
check('M3-1b Ceq', Ceq, 3.444e-9, 0.002); check('M3-1b Q', Ceq * 12, 41.32e-9, 0.002)
check('M3-1b energy', 0.5 * Ceq * 144, 247.9e-9, 0.002)
tau = 50e-3 / (1e3 + 1.5e3)
i0, iinf = 2 / 2500, -1 / 2500
check('M3-1c i(30us)', iinf + (i0 - iinf) * math.exp(-30e-6 / tau), -0.1322e-3, 0.004)
check('M3-1c zero crossing', tau * math.log((i0 - iinf) / (0 - iinf)), 21.97e-6, 0.002)
w = 2 * pi * 10e3
check('M3-1d C', 1 / (w * 200), 79.58e-9, 0.002); check('M3-1d Pmax', 25 / 800, 31.25e-3)
G = 1 / 1e3 + 1 / 2e3 + 1 / 2e3
check('M3-1e dc', (2 / 2e3) / G, 0.5); check('M3-1e ac amp', (3 / 1e3) / G, 1.5)
check('M3-1e max', 0.5 + 1.5, 2.0)
C1, R2, R3, R4, C5 = 10e-9, 10e3, 2e3, 18e3, 1e-9
fc = 1 / (2 * pi * C1 * R2)
check('M3-2 fc', fc, 1591.5, 0.001)
def Hm(f):
    w = 2 * pi * f
    return (1j * w * C1 * R2 / (1 + 1j * w * C1 * R2)) * (1 + par(R4, 1 / (1j * w * C5)) / R3)
check('M3-2 |H(fc)|', abs(Hm(fc)), 6.960, 0.002); check('M3-2 phase(fc)', deg(Hm(fc)), 35.83, 0.003)
check('M3-2 high-f gain', abs(Hm(1e9)), 1.0, 0.001)
v, _ = solve([('V', 'i', 0, 1), ('C', 'i', 'p', C1), ('R', 'p', 0, R2), ('OPAMP', 'p', 'n', 'o'), ('R', 'n', 0, R3), ('R', 'n', 'o', R4), ('C', 'n', 'o', C5)], 2 * pi * fc)
check('M3-2 circuit', v['o'], Hm(fc), 1e-6)
check('M3-2 peak gain', max(abs(Hm(f)) for f in [100 * 1.05 ** k for k in range(200)]), 8.48, 0.01)
Vp = 325 / 15 - 1.4; f = 50; T = 1 / f; RC = 100 * 470e-6
g = lambda t: (325 / 15) * abs(math.sin(2 * pi * f * t)) - 1.4 - Vp * math.exp(-(t - T / 4) / RC)
tc = bisect(g, T / 2, T / 2 + T / 4)
check('M3-3 peak', Vp, 20.27, 0.002); check('M3-3 min', Vp * math.exp(-(tc - T / 4) / RC), 17.01, 0.004)
check('M3-3 ripple', Vp * (1 - math.exp(-(tc - T / 4) / RC)), 3.256, 0.01)

print('FAILS:', fails)
sys.exit(1 if fails else 0)
