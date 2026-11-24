# Exam sheet (print this and bring it)

The EEEN20020 final is **open book**: any printed notes, no laptop or phone, calculator allowed.

So this page is not for learning by heart. It is the sheet to **print and bring in**: every 📐 box in the repo on one page, in exam order.

Box numbers match the 📐 boxes in the notes (1 to 91). Each section links to its topic.

Still: know the ⭐ items cold. Looking things up costs minutes, and you have 2 hours for 200 marks (36 seconds a mark).

---

## Time plan for the exam

| Question | Marks | Time |
|---|---|---|
| Q1 (five parts a–e) | 100 | 55 min (11 each) |
| Q2 (frequency response) | 50 | 30 min |
| Q3 (diodes / amplifier / transformer) | 50 | 30 min |
| Check | | 5 min |

Do the part you're surest of first. Write units on every answer. Three significant figures.

---

## Signs, power, Kirchhoff ([Topics 1](notes/01-current-voltage-power.md), [2](notes/02-elements-kirchhoff.md))

| # | Box |
|---|---|
| 1 | i = dq/dt (1 A = 1 C/s) |
| 2 | v = dw/dq (1 V = 1 J/C) |
| 3 ⭐ | Standard convention: current arrow **into the +** terminal |
| 4 ⭐ | p = vi. With Rule 3: p > 0 absorbs, p < 0 supplies |
| 5 | Sum of all powers = 0 |
| 6 ⭐ | KCL: currents leaving a node sum to 0 |
| 7 ⭐ | KVL: voltages round a loop sum to 0 |
| 8 ⭐ | Ohm: v = Ri, i = Gv. Only the voltage **across** the resistor |
| 9 | Voltage source: fixed v, any current |
| 10 | Current source: fixed i, any voltage |
| 11 | Branch voltage v = e_A − e_B |

## Resistive networks ([Topics 3](notes/03-series-parallel-division.md), [4](notes/04-superposition-thevenin-norton.md), [5](notes/05-node-voltage.md))

| # | Box |
|---|---|
| 12 ⭐ | Series: R1 + R2 |
| 13 ⭐ | Parallel: R1R2/(R1 + R2). Conductances add |
| 14 | Voltage sources in series add. Current sources in parallel add. Anything ∥ a V source sees that V |
| 15 ⭐ | Voltage division: v1 = V R1/(R1 + R2) (same current only!) |
| 16 ⭐ | Current division: i1 = I R2/(R1 + R2) (the **other** R on top) |
| 17 | Real source: Vs with Rs. vL = Vs RL/(Rs + RL) |
| 18 ⭐ | Superposition: one source at a time. **V off = short, I off = open**. Add |
| 19 | Source transform: E series R ⇔ E/R parallel R |
| 20 ⭐ | Thévenin: Vth = open-circuit V. Norton: In = short-circuit I. Rth = Rn = Vth/In = R with sources off |
| 21 | Bridge: Vth = Vs(R3/(R1 + R3) − R4/(R2 + R4)). Rth = R1∥R3 + R2∥R4 |
| 22 | dc max power: RL = Rs, Pmax = Vs²/(4Rs) |
| 23 ⭐ | Nodal: ground, KCL at each node with (e_this − e_other)/R, solve |
| 24 | By inspection: diagonal = sum of G at node, off-diagonal = −G between, RHS = source currents in |
| 25 | V source to ground: node known. Floating V source: e_a − e_b = V, KCL round both nodes |

**Millman (one node fed through resistors):** e = (Σ Vk/Rk)/(Σ 1/Rk).

## Amplifiers and op amps ([Topics 6](notes/06-controlled-sources.md), [7](notes/07-op-amps.md))

| # | Box |
|---|---|
| 26 | VCVS (E): v = A vx · CCCS (F): i = β ix · CCVS (H): v = r ix · VCCS (G): i = gm vx |
| 27 ⭐ | **Never turn off a controlled source.** Rth by a test source: Rth = vt/it |
| 28 | vL/vs = [Ri/(Rs + Ri)] · A · [RL/(Ro + RL)] |
| 29 | CCCS pushing into the output node: Rth = Ro ∥ (Rs + rπ)/(β + 1) (Final 2025 Q1b: 28.1 Ω) |
| 30 | FET with source resistor R1, drain resistor R2: H = −gm R2/(1 + gm R1) |
| 31 ⭐ | dB = 20 log10\|gain\|. Undo: \|gain\| = 10^(dB/20). 20 dB = ×10, 30 dB = ×31.62 |
| 32 ⭐ | Ideal op amp with negative feedback: **i+ = i− = 0, v+ = v−** |
| 33 ⭐ | Inverting: −Rf/R1 (−Zf/Z1) |
| 34 ⭐ | Non-inverting: 1 + Rf/R1 (1 + Zf/Z1) |
| 35 | Buffer: vo = vin |
| 36 | Summing: vo = −Rf(v1/R1 + v2/R2 + …) |
| 37 | Difference: vo = (R2/R1)(v2 − v1). General: (R1 + R2)R4/(R1(R3 + R4)) v2 − (R2/R1) v1 |

**Howland current source (HW2 Q2):** R0 = R1R2R4/(R2R4 − R1R3). Balanced → R0 = ∞, I = Vs/R1.

## Capacitors, inductors, transients ([Topics 8](notes/08-capacitors-inductors.md), [9](notes/09-transients.md))

| # | Box |
|---|---|
| 38 ⭐ | i = C dv/dt. **vC can't jump** |
| 39 | wC = ½Cv², wL = ½Li² |
| 40 ⭐ | C in parallel add. C in series: 1/C = 1/C1 + 1/C2 |
| 41 ⭐ | v = L di/dt. **iL can't jump** |
| 42 | L combine like R |
| 43 | Integrator vo = −(1/RC)∫vin. Differentiator vo = −RC dvin/dt |
| 44 ⭐ | dc steady state: **C open, L short** |
| 45 ⭐ | **X(t) = X(∞) + [X(t0) − X(∞)] e^(−(t − t0)/τ)** |
| 46 ⭐ | τ = Rth C or L/Rth (sources off) |
| 47 | Continuity: vC and iL same just after a switch |
| 48 | Square wave 0/V into RC, x = e^(−T/(2τ)): Vmax = V/(1 + x), Vmin = Vx/(1 + x) |

Units: kΩ × nF = μs · kΩ × μF = ms · mH/kΩ = μs. e^(−1) = 0.368, 1 − e^(−1) = 0.632, e^(−5) < 1%.

**Pulse:** two stages. The end of stage 1 is the start of stage 2.

**Lossy integrator (R1 in, R2 ∥ C fb) with a step V:** vo(0) = 0, vo(∞) = −(R2/R1)V, τ = R2C.

## Phasors and impedance ([Topics 10](notes/10-sinusoids-phasors.md), [11](notes/11-impedance.md))

| # | Box |
|---|---|
| 49 | A cos(ωt + φ), ω = 2πf, T = 1/f |
| 50 ⭐ | sin x = cos(x − 90°) |
| 51 ⭐ | a + jb = r∠θ: r = √(a² + b²), θ = atan(b/a) **+180° if a < 0** |
| 52 ⭐ | A cos(ωt + φ) ↔ A∠φ. Back: r∠θ → r cos(ωt + θ) |
| 53 ⭐ | ZR = R, ZL = jωL, ZC = 1/(jωC) = −j/(ωC) |
| 54 ⭐ | Every resistive rule works with Z |
| 55 | Y = 1/Z = G + jB. \|Y\| = 1/\|Z\|, ∠Y = −∠Z. Admittances in parallel add |
| 56 | Transform → solve → transform back. Never mix |

Multiply: sizes ×, angles +. Divide: sizes ÷, angles −. R ∥ C = R/(1 + jωRC).

**Phasor transform handout:** (1) write x(t) = Xm cos(ωt + φ); (2) x(t) = Re{Xm e^(j(ωt + φ))}; (3) drop Re; (4) drop e^(jωt): X = Xm∠φ. Back: reverse the steps.

## AC power, transformers, resonance ([Topics 12](notes/12-ac-power.md), [13](notes/13-transformer-resonance.md))

| # | Box |
|---|---|
| 57 ⭐ | P = ½ Vm Im cos(φv − φi) (peak values!) |
| 58 ⭐ | P = ½\|I\|² Re(Z). Series load: ½\|I\|²R. Parallel load: ½\|V\|²/R |
| 59 | Vrms = Vm/√2. P = Vrms Irms cos θ. 230 V rms = 325 V peak |
| 60 ⭐ | Max power: **ZL = ZS\***. Pmax = \|E\|²/(8RS) (E peak). Only one part adjustable: make total X = 0 |
| 61 | p(t) = ½VmIm[cos θ + cos(2ωt + φv + φi)]. Peak = ½VmIm(1 + cos θ) |
| 62 ⭐ | V1/V2 = n1/n2, I2 = −(n1/n2) I1. Lossless |
| 63 ⭐ | Zin = (n1/n2)² ZL |
| 64 ⭐ | Match: n1/n2 = √(Rs/RL) |
| 65 | ω0 = 1/√(LC). Series LC = short at ω0. Parallel LC = open at ω0 |

**R + jωL in parallel with C:** Z = (R + jωL)/(1 − ω²LC + jωRC).

## Frequency response and op-amp filters ([Topics 14](notes/14-frequency-response.md), [15](notes/15-op-amp-filters.md)) = Q2

| # | Box |
|---|---|
| 66 | H(ω) = Vout/Vin |
| 67 ⭐ | A cos(ωt + θ) in → A\|H\| cos(ωt + θ + ∠H) out |
| 68 ⭐ | 3 dB point: \|H\| = \|H\|max/√2 (−3 dB) |
| 69 ⭐ | Low-pass 1/(1 + jω/ω0), high-pass (jω/ω0)/(1 + jω/ω0). At ω0: 0.707, ∓45° |
| 70 ⭐ | Type by inspection: ω→0: C open, L short. ω→∞: C short, L open |
| 71 | RLC band-pass: ω0 = 1/√(LC), BW = 1/(RC), Q = R√(C/L) |
| 72 ⭐ | Op-amp filters: R → Z in Topic 7's formulas |
| 73 ⭐ | Inverting LP (R2 in, R4∥C3 fb): H = −(R4/R2)/(1 + jωR4C3). f3dB = 1/(2πR4C3) |
| 74 ⭐ | Sallen–Key LP: H = 1/(1 − ω²R1R2C3C4 + jωC4(R1 + R2)). −90° at ω0 = 1/√(R1R2C3C4). In Z's: Z3Z4/(Z1Z2 + Z3(Z1 + Z2) + Z3Z4) |
| 75 | R, aR, bR, C inverting: H = −[b/(1 + a)]/[1 + jωCR(a + b)/(1 + a)]. (1, 2): −1/(1 + 1.5jωRC). (2, 3): −1/(1 + (5/3)jωRC) |
| 76 | RC high-pass then non-inverting: H = [jωCR/(1 + jωCR)](1 + Zf/R1) |

Inverting filter phase = 180° − (low-pass lag). At its corner: 135°.

**Final 2025 Q2 circuit** (R∥C both sides, all equal): H = 1/(1 + jωCR).

**Read the input frequency twice:** cos(πf0 t) is f0/2.

## Diodes ([Topics 16](notes/16-diodes.md), [17](notes/17-rectifiers-clippers.md), [18](notes/18-other-nonlinear.md)) = Q3

| # | Box |
|---|---|
| 77 | Nonlinear: no superposition, no phasors through the diode |
| 78 | i = Is(e^(v/VT) − 1), VT ≈ 25 mV |
| 79 ⭐ | Ideal diode: ON = short (i ≥ 0), OFF = open (v ≤ 0) |
| 80 ⭐ | PWL: ideal + Vth (0.7 V unless told). ON: v = Vth |
| 81 ⭐ | Guess ON/OFF, solve, check the direction. Wrong → swap |
| 82 ⭐ | Half-wave: vo = vi − Vth when vi > Vth, else 0. Period T |
| 83 | Full-wave: \|vi\| − Vth (centre-tap) or \|vi\| − 2Vth (bridge). Period T/2 |
| 84 ⭐ | Peak detector: charges to A − Vth, decays with τ = RL C until the input catches it |
| 85 ⭐ | Clipper: clamps at the battery level (+Vth). Between levels vout = vin |
| 86 | Clamper: series C + diode shifts the wave; peak sits at the diode's level |
| 87 | All diodes OFF and no load: Rs drops nothing |
| 88 | Op amp saturates at ±Esat |
| 89 | Comparator: +Esat if v+ > v−, else −Esat |
| 90 | Flash ADC: ladder references + one comparator each |
| 91 | Resolution = V/(2ⁿ − 1). Max error = half |

### Sketch checklists (Q3 is often 25 to 50% sketch)
- **Always:** draw the input faintly (dashed), mark its amplitude and period, then draw the output bold on the same axes.
- **Clipper:** dashed lines at each clip level. The sine, flat wherever it crosses a line.
- **Half-wave:** positive humps (minus Vth), zero between. **Full-wave:** humps every T/2.
- **Peak detector:** follow up to the peak, slow exponential fall, catch up near the next peak. Mark Vmax, Vmin, T.
- **Clamper:** same shape, shifted so the peak sits at the diode level.
- **RC square wave:** rising curves (concave down) in high halves, falling (concave up) in low halves, between Vmin and Vmax.
- Label axes and units. Mark max, min and the period with numbers.
