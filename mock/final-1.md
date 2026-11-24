# Mock Final 1

Same layout as the real EEEN20020 final: **2 hours, answer all three questions. Q1 is 100 marks (five parts of 20%), Q2 and Q3 are 50 marks each.**

Open book: your notes and the [exam sheet](../formula-sheet.md). Calculator. No laptop.

There are no figures. Each circuit is described in words: **draw it first**, then solve. Drawing it from words is good practice too.

The answers are mine, every number checked in Python (`tools/check_mocks.py`).

---

## Questions

### Q1. Five short circuits — 100 marks

**(a)** A 12 V source feeds the top of a bridge. R1 = 1 kΩ from the top to node A, R2 = 2 kΩ from A to ground, R3 = 2 kΩ from the top to node B, R4 = 1 kΩ from B to ground. R5 = 3 kΩ joins A to B. Find the current from A to B through R5. Use a Thévenin equivalent. (20%)

**(b)** V1 drives R = 2.2 kΩ in series with C = 100 nF to ground. V1 has been 0 V for a long time. At t = 0 it steps to 3 V. At t = 200 μs it steps back to 0 V. Find the capacitor voltage at t = 300 μs. (20%)

**(c)** Find the magnitude and phase of Z between A and B: R1 = 50 Ω in series with (L = 2 mH in parallel with C = 1 μF), at f = 2 kHz. Is the LC pair inductive or capacitive at this frequency? (20%)

**(d)** Vs = 325 cos(2π 50 t) V with Rs = 5 Ω drives a load of R = 50 Ω in series with C = 100 μF. Find the average power in the load. (20%)

**(e)** An inverting amplifier: R2 = 4.7 kΩ from V1 to the − input, R4 = 47 kΩ in parallel with C3 = 3.3 nF from the − input to the output, + input to ground. Find the dc gain in dB and the 3 dB frequency. Then find Vout(t) for V1 = 0.1 cos(2π 1000 t) V. (20%)

---

### Q2. Sallen–Key low-pass — 50 marks

Vin → R1 → node 1 → R2 → node 2. C4 from node 2 to ground. C3 from node 1 to the output. Node 2 is the + input of an op amp wired as a unity-gain follower (output to − input). R1 = R2 = 4.7 kΩ, C3 = 10 nF, C4 = 4.7 nF.

(a) Find H(ω) in terms of Z1 = R1, Z2 = R2, Z3, Z4. (30%)

(b) Find H(ω) in terms of R1, R2, C3, C4 and ω. (20%)

(c) Find f0 where the phase of H is −90°. (20%)

(d) Find Vout(t) when Vin = 2 cos(2πf0 t) V. (20%)

(e) What is the gain in dB at dc and at 10 f0? (10%)

---

### Q3. Clipper with real diodes — 50 marks

Vac = 6 sin(2π 500 t) V drives Rs = 1 kΩ to the output node. D1: anode at the output, cathode to the + of a 2 V battery (− to ground). D2: anode at ground, cathode to the + of a 3 V battery whose − is at the output. Model each diode as ideal with Vth = 0.7 V in series.

(a) Find the output levels where each diode turns on. (20%)

(b) Sketch Vout(t) for one period, with the input dashed. (40%)

(c) Find the maximum, minimum and period of Vout(t). (25%)

(d) Find the current in Rs at the moment the input reaches its positive peak, and the phase angle (in degrees) at which D1 starts to conduct. (15%)

---

## Answers

<details><summary>Q1 answers</summary>

**(a)** Remove R5. V_A = 12 × 2/3 = 8 V, V_B = 12 × 1/3 = 4 V. Vth = 4 V.

Short the source: Rth = 1k ∥ 2k + 2k ∥ 1k = 1333 Ω.

**I(R5) = 4/(1333 + 3000) = 0.923 mA**

From: Topic 4 §4 Equation 21

<br>

**(b)** τ = 2.2k × 100n = 220 μs. At 200 μs: 3(1 − e^(−200/220)) = 1.791 V. Then decay for 100 μs:

**Vc(300 μs) = 1.791 e^(−100/220) = 1.135 V**

From: Topic 9 Equation 45 (a pulse: two stages)

<br>

**(c)** ω = 12 566. Z_L = j25.13, Z_C = −j79.58. Parallel: (j25.13)(−j79.58)/(j25.13 − j79.58) = j36.73 Ω.

Z = 50 + j36.73. **|Z| = 62.0 Ω, phase 36.3°.** The LC pair is **inductive** (below its resonance at 3.56 kHz, a parallel LC is inductive).

From: Topic 11 Rule 54, Topic 13 Equation 65

<br>

**(d)** Z_C = −j31.83 Ω. Total Z = 55 − j31.83, |Z| = 63.55 Ω. |I| = 5.114 A.

**P = ½ × 5.114² × 50 = 654 W**

From: Topic 12 Equation 58

<br>

**(e)** **dc gain = 20 dB** (×10, inverting). **f3dB = 1/(2π × 47k × 3.3n) = 1026 Hz.**

At 1 kHz: ωR4C3 = 0.975. H = −10/(1 + j0.975) = 7.162∠135.7°.

**Vout(t) = 0.716 cos(2π 1000 t + 135.7°) V**

From: Topic 15 Equation 73

</details>

<details><summary>Q2 answers</summary>

**(a) H = Z3Z4/(Z1Z2 + Z3(Z1 + Z2) + Z3Z4)**

**(b) H = 1/(1 − ω²R1R2C3C4 + jωC4(R1 + R2))**

**(c)** ω0 = 1/√(R1R2C3C4) = 1/√(4700² × 47 × 10⁻¹⁸) = 31 035 rad/s.

**f0 = 4939 Hz**

**(d)** |H(ω0)| = 1/(ω0C4(R1 + R2)) = 0.7293, phase −90°.

**Vout(t) = 1.459 cos(2π 4939 t − 90°) V**

**(e)** dc: H = 1 → **0 dB**. At 10 f0: the ω² term dominates, |H| ≈ 1/100 → **−40 dB** (second order: −40 dB per decade).

From: Topic 15 §3 Equation 74

</details>

<details><summary>Q3 answers</summary>

**(a)** D1 on when Vout > 2 + 0.7 = **2.7 V**. D2 on when Vout + 3 < −0.7, i.e. Vout < **−3.7 V**.

**(b)** The sine (6 V peak) with flat tops at +2.7 V and flat bottoms at −3.7 V. Between the levels Vout = Vac (no current in Rs). Mark 2 ms per period.

**(c) Vmax = 2.7 V, Vmin = −3.7 V, period 2 ms**

**(d)** At the peak: I(Rs) = (6 − 2.7)/1k = **3.3 mA**. D1 starts when 6 sin θ = 2.7: **θ = 26.7°**.

From: Topic 17 Rule 85, Rule 87, Topic 16 Rule 80

</details>
