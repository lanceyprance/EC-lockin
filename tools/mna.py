"""Tiny modified-nodal-analysis solver used by check_numbers.py and check_mocks.py.

Node 0 (or '0' / 'gnd') is ground. Elements:
  ('R', a, b, ohms)        ('C', a, b, farads)      ('L', a, b, henries)
  ('Z', a, b, complex_ohms)
  ('I', a, b, amps)        current flows a -> through the source -> b (so it is pushed INTO b)
  ('V', p, n, volts)       p is the + terminal
  ('VCCS', a, b, cp, cn, gm)   current gm*(v_cp - v_cn) flows a -> through the source -> b
  ('VCVS', p, n, cp, cn, A)    v_p - v_n = A*(v_cp - v_cn)
  ('CCCS', a, b, 'Vname', beta) current beta*I(Vname) flows a -> through -> b; I(Vname) = current
                                 into the + terminal of voltage source Vname (name given as 6th field of 'V')
  ('OPAMP', plus, minus, out)  ideal op amp: v_plus = v_minus, output sources any current
A 'V' element may carry a name as a 5th field: ('V', p, n, volts, 'Vx').
solve(elements, w) returns (v, i): dict node -> voltage, dict Vname -> current (into + terminal, through source to -).
w = angular frequency (0 for dc; then C is open and L is a short).
"""
import numpy as np


def _z(e, w):
    k, a, b, x = e[0], e[1], e[2], e[3]
    if k == 'R': return x
    if k == 'Z': return x
    if k == 'C': return np.inf if w == 0 else 1 / (1j * w * x)
    if k == 'L': return 0 if w == 0 else 1j * w * x


def solve(elements, w=0.0):
    nodes = []
    def nid(n):
        if n in (0, '0', 'gnd'): return None
        if n not in nodes: nodes.append(n)
        return nodes.index(n)
    els = []
    for e in elements:
        k = e[0]
        if k in 'RCLZ' and len(k) == 1:
            z = _z(e, w)
            if z == 0: els.append(('V', e[1], e[2], 0.0, None))   # short
            elif np.isinf(z): continue
            else: els.append(('Y', e[1], e[2], 1 / z))
        else:
            els.append(e)
    for e in els:
        if e[0] in ('Y', 'I', 'V'): nid(e[1]); nid(e[2])
        elif e[0] in ('VCCS', 'VCVS'): [nid(x) for x in e[1:5]]
        elif e[0] == 'CCCS': nid(e[1]); nid(e[2])
        elif e[0] == 'OPAMP': [nid(x) for x in e[1:4]]
    vsrc = [e for e in els if e[0] in ('V', 'VCVS', 'OPAMP')]
    N, M = len(nodes), len(vsrc)
    A = np.zeros((N + M, N + M), complex); rhs = np.zeros(N + M, complex)
    def stamp_y(a, b, y):
        ia, ib = nid(a), nid(b)
        if ia is not None: A[ia, ia] += y
        if ib is not None: A[ib, ib] += y
        if ia is not None and ib is not None: A[ia, ib] -= y; A[ib, ia] -= y
    names = {}
    for j, e in enumerate(vsrc):
        if e[0] == 'V' and len(e) > 4 and e[4]: names[e[4]] = N + j
    for e in els:
        k = e[0]
        if k == 'Y': stamp_y(e[1], e[2], e[3])
        elif k == 'I':
            ia, ib = nid(e[1]), nid(e[2])
            if ia is not None: rhs[ia] -= e[3]
            if ib is not None: rhs[ib] += e[3]
        elif k == 'VCCS':
            ia, ib, cp, cn = (nid(x) for x in e[1:5]); g = e[5]
            for r, s in ((ia, 1), (ib, -1)):
                if r is None: continue
                if cp is not None: A[r, cp] += s * g
                if cn is not None: A[r, cn] -= s * g
        elif k == 'CCCS':
            ia, ib = nid(e[1]), nid(e[2]); col = names[e[3]]; beta = e[4]
            if ia is not None: A[ia, col] += beta
            if ib is not None: A[ib, col] -= beta
    for j, e in enumerate(vsrc):
        r = N + j; k = e[0]
        if k == 'V':
            ip, iN = nid(e[1]), nid(e[2])
            if ip is not None: A[ip, r] += 1; A[r, ip] += 1
            if iN is not None: A[iN, r] -= 1; A[r, iN] -= 1
            rhs[r] = e[3]
        elif k == 'VCVS':
            ip, iN, cp, cn = (nid(x) for x in e[1:5]); g = e[5]
            if ip is not None: A[ip, r] += 1; A[r, ip] += 1
            if iN is not None: A[iN, r] -= 1; A[r, iN] -= 1
            if cp is not None: A[r, cp] -= g
            if cn is not None: A[r, cn] += g
        elif k == 'OPAMP':
            ipl, imi, io = (nid(x) for x in e[1:4])
            if io is not None: A[io, r] += 1          # output current is the unknown
            if ipl is not None: A[r, ipl] += 1
            if imi is not None: A[r, imi] -= 1
    x = np.linalg.solve(A, rhs)
    v = {n: x[i] for i, n in enumerate(nodes)}; v[0] = 0
    cur = {nm: x[c] for nm, c in names.items()}
    return v, cur


def par(*zs):
    return 1 / sum(1 / z for z in zs)
