# Mock Final 3

Same layout as the real EEEN20020 final: **2 hours, answer all three questions. Q1 is 100 marks (five parts of 20%), Q2 and Q3 are 50 marks each.**

Open book: your notes and the [exam sheet](../formula-sheet.md). Calculator. No laptop.

There are no figures. Each circuit is described in words: **draw it first**, then solve.

The answers are mine, every number checked in Python (`tools/check_mocks.py`).

---

## Questions

### Q1. Five short circuits — 100 marks

**(a)** An amplifier model: vin → R1 = 1 kΩ → node X. R2 = 9 kΩ from X to ground. A VCCS draws gm vX (gm = 10 mS) from node O to ground. Ro = 20 kΩ from O to ground. Rf = 100 kΩ feeds back from O to X. Find the open-circuit gain vO/vin and the Thévenin resistance seen at O. (20%)

**(b)** C1 = 10 nF, then (C2 = 4.7 nF in parallel with C3 = 2.2 nF), then C4 = 22 nF, all in series across a 12 V supply. Find the equivalent capacitance, the charge on it, and the stored energy. (20%)

**(c)** A source steps from +2 V to −1 V at t = 0 (it had been at +2 V for a long time). It drives R1 = 1 kΩ, L = 50 mH and R2 = 1.5 kΩ in series. Find the current at t = 30 μs, and when it crosses zero. (20%)

**(d)** A source at 10 kHz has E = 5 V peak and internal impedance ZS = 100 + j200 Ω. You may use a resistor and a capacitor in series as the load. Choose them for maximum load power, and find that power. (20%)

**(e)** V1 = 3 cos(1000 t) V through R1 = 1 kΩ and V2 = 2 V dc through R3 = 2 kΩ both feed node 2. R2 = 2 kΩ goes from node 2 to ground. Find e2(t), and its maximum and minimum. (20%)

---

### Q2. Band-pass by two stages — 50 marks

Vin → C1 = 10 nF → the + input, with R2 = 10 kΩ from the + input to ground. − input: R3 = 2 kΩ to ground, and R4 = 18 kΩ in parallel with C5 = 1 nF to the output.

(a) Find H(ω) = Vout/Vin. (30%)

(b) What is the gain at dc, and at very high frequency? What kind of filter is it overall? (20%)

(c) Find |H| and the phase at fc = 1/(2πC1R2). (30%)

(d) Find Vout(t) when Vin = 0.1 cos(2π fc t) V. (20%)

---

### Q3. DC power supply — 50 marks

The mains (325 V peak, 50 Hz) feeds an ideal 15:1 transformer. A bridge rectifier (each diode ideal with Vth = 0.7 V) charges C = 470 μF. A load RL = 100 Ω is across C.

(a) Sketch the output voltage in steady state, with the rectified sine dashed. (40%)

(b) Find the peak output voltage and the ripple period. (20%)

(c) Find the minimum output voltage and the peak-to-peak ripple. (40%)

---

## Answers

<details><summary>Q1 answers</summary>

**(a)** Nodal analysis, keeping the VCCS on (Topic 6 Rule 27). With vin = 1 V and O open:

**vO/vin = −59.8**

Test source at O with vin = 0:

**Rth = 6.71 kΩ**

(Rf feeds O back into X, and the VCCS reacts to vX: the test-source method is the only safe way.)

From: Topic 6 §3, Topic 5

<br>

**(b)** C2 ∥ C3 = 6.9 nF. Series: 1/C = 1/10 + 1/6.9 + 1/22 (per nF).

**C = 3.44 nF. Q = CV = 41.3 nC. W = ½CV² = 248 nJ.**

From: Topic 8 Equation 40, Equation 39

<br>

**(c)** i(0) = 2/2500 = 0.8 mA (continuous). i(∞) = −1/2500 = −0.4 mA. τ = 50 mH/2.5 kΩ = 20 μs.

**i(30 μs) = −0.4 + 1.2 e^(−1.5) = −0.132 mA**

Zero when 1.2 e^(−t/τ) = 0.4: **t = τ ln 3 = 22.0 μs**

From: Topic 9 Equation 45

<br>

**(d)** ZL = ZS* = 100 − j200: **R = 100 Ω, C = 1/(ω × 200) = 79.6 nF.**

**Pmax = 5²/(8 × 100) = 31.3 mW**

From: Topic 12 Equation 60

<br>

**(e)** Superposition: dc and ac separately. G = 1/1k + 1/2k + 1/2k = 2 mS.

dc: 2 V/2k = 1 mA → 0.5 V. ac: 3/1k = 3 mA → 1.5 V.

**e2(t) = 0.5 + 1.5 cos(1000 t) V. Max 2 V, min −1 V.**

From: Topic 4 Rule 18 (Millman)

</details>

<details><summary>Q2 answers</summary>

**(a) H = [jωC1R2/(1 + jωC1R2)] × [1 + R4/(R3(1 + jωR4C5))]**

**(b)** dc: the high-pass blocks: **H = 0**. Very high f: high-pass passes (1) but C5 shorts R4, so the gain stage → 1: **H → 1**. In between the gain rises to about 8.5. Overall a **band-pass** (with gain).

**(c)** fc = 1591.5 Hz. High-pass part: 0.7071∠45°. Gain part: 1 + Z45/R3 = 9.844∠−9.2°.

**|H| = 6.96, phase 35.8°**

**(d) Vout(t) = 0.696 cos(2π 1591.5 t + 0.625) V**

From: Topic 15 §5 Equation 76

</details>

<details><summary>Q3 answers</summary>

**(a)** Full-wave humps (dashed). The output follows each hump to its peak, then decays slowly until the next hump catches it. Ripple repeats every 10 ms.

**(b)** Secondary peak 325/15 = 21.67 V. Two diodes: **peak = 21.67 − 1.4 = 20.27 V.** Ripple period = **10 ms** (full-wave: half the 20 ms mains period).

**(c)** τ = RL C = 47 ms. Decay from the peak until the next hump catches it (solve |sin| − 1.4 = decay):

**Vmin ≈ 17.0 V. Ripple ≈ 3.26 V peak-to-peak.**

From: Topic 17 Rule 83, Rule 84, Topic 13 Equation 62

</details>
