# Mock Final 2

Same layout as the real EEEN20020 final: **2 hours, answer all three questions. Q1 is 100 marks (five parts of 20%), Q2 and Q3 are 50 marks each.**

Open book: your notes and the [exam sheet](../formula-sheet.md). Calculator. No laptop.

There are no figures. Each circuit is described in words: **draw it first**, then solve.

The answers are mine, every number checked in Python (`tools/check_mocks.py`).

---

## Questions

### Q1. Five short circuits — 100 marks

**(a)** V1 = 6 V at node 1. R1 = 1 kΩ from node 1 to node 2. R2 = 2 kΩ from node 2 to ground. A floating source V2 = 3 V has + at node 2 and − at node 3. R3 = 3 kΩ from node 3 to ground. A 1 mA current source pushes current from ground into node 3. Find e2 and e3. (20%)

**(b)** A 12 V source and a switch feed node 2. R2 = 3 kΩ from node 2 to node 3. R3 = 6 kΩ and L = 20 mH both from node 3 to ground. The inductor current is zero before the switch closes at t = 0. Find the inductor current at t = 10 μs. (20%)

**(c)** Vs = 10 cos(2π 1000 t) V with Rs = 200 Ω drives the primary of an ideal transformer, N1:N2 = 5:1. The secondary load is 4 Ω in series with 1 mH. Find the average power in the load. Which turns ratio would match the resistances? (20%)

**(d)** Find the magnitude and phase of the **admittance** of R1 = 100 Ω in parallel with (R2 = 50 Ω in series with L = 5 mH), at ω = 10⁴ rad/s. (20%)

**(e)** A diode AND gate: VDD = 5 V pulls node 3 up through RL = 10 kΩ. Two diodes have their anodes at node 3. Their cathodes go to sources VA and VB. Each diode drops 0.6 V when on. Find e3 for (i) VA = VB = 0.2 V, (ii) VA = 0.2 V and VB = 4.8 V, (iii) VA = VB = 4.8 V. (20%)

---

### Q2. Inverting active filter — 50 marks

Vin → R → node 1 → R → node 2 (the − input, + input grounded). 3R from node 2 to the output. C from node 1 to the output. R = 4.7 kΩ, C = 2.2 nF.

(a) Find H(ω) in terms of R, C and ω. (40%)

(b) Find the dc gain and the frequency f0 at which the phase of H is 135°. (30%)

(c) Find Vout(t) when Vin = 0.5 cos(2π (2f0) t) V. (30%)

---

### Q3. Peak detector — 50 marks

Vs = 10 sin(2π 60 t) V drives a diode (ideal with Vth = 0.7 V) into C = 470 μF in parallel with RL = 500 Ω.

(a) Sketch Vout(t) in steady state, with the input dashed. (40%)

(b) Find the maximum of Vout and its period. (20%)

(c) Find the minimum of Vout, and how long after the start of each cycle the diode turns on again. (40%)

---

## Answers

<details><summary>Q1 answers</summary>

**(a)** e3 = e2 − 3. KCL round nodes 2 and 3 together (the 1 mA enters):

(e2 − 6)/1k + e2/2k + (e2 − 3)/3k = 1 mA. ×6k: 11 e2 = 48.

**e2 = 4.364 V, e3 = 1.364 V**

From: Topic 5 Rule 25

<br>

**(b)** Thévenin seen by L: Vth = 12 × 6/9 = 8 V, Rth = 3k ∥ 6k = 2 kΩ. i(∞) = 4 mA, τ = 20 mH/2 kΩ = 10 μs.

**i(10 μs) = 4(1 − e^(−1)) = 2.53 mA**

From: Topic 9 Equation 46

<br>

**(c)** Reflect: 25 × (4 + j6.283) = 100 + j157.1 Ω. Total 300 + j157.1, |Z| = 338.6 Ω, |I1| = 29.53 mA.

**P = ½ × 0.02953² × 100 = 43.6 mW** (the same power reaches the 4 Ω).

Match resistances: N1/N2 = √(200/4) = **7.07**.

From: Topic 13 Equation 63, Rule 64

<br>

**(d)** ωL = 50 Ω. Y = 1/100 + 1/(50 + j50) = 0.01 + (0.01 − j0.01) = 0.02 − j0.01 S.

**|Y| = 22.4 mS, ∠Y = −26.6°**

From: Topic 11 Equation 55

<br>

**(e)** The lowest input wins (its diode turns on).

(i) **e3 = 0.8 V** (0.42 mA through RL). (ii) **e3 = 0.8 V** (the 4.8 V diode is reverse-biased). (iii) Both would need 5.4 V > VDD, so both OFF: **e3 = 5 V**.

An AND gate: high only when both inputs are high.

From: Topic 16 Rule 81

</details>

<details><summary>Q2 answers</summary>

**(a)** Equation 75 with a = 1, b = 3:

**H(ω) = −1.5/(1 + 2jωRC)**

**(b)** **dc gain = −1.5** (3.5 dB, inverting). Phase 135° when 2ω0RC = 1:

**f0 = 1/(4πRC) = 7696 Hz**

**(c)** At 2f0: 2ωRC = 2. H = −1.5/(1 + j2) = 0.6708∠116.6°.

**Vout(t) = 0.335 cos(2π 15 392 t + 116.6°) V**

From: Topic 15 §4 Equation 75

</details>

<details><summary>Q3 answers</summary>

**(a)** vo follows the input (minus 0.7 V) up to the peak, then decays slowly (τ = RL C = 0.235 s ≫ T = 16.7 ms), then is caught by the next rising edge. A small ripple near 9 V.

**(b) Max = 10 − 0.7 = 9.3 V. Period = 1/60 s = 16.7 ms.**

**(c)** Decay from t = T/4: vo = 9.3 e^(−(t − T/4)/0.235). Solve 10 sin(2π 60 t) − 0.7 = vo on the next rising edge:

The diode turns on again **3.24 ms** into the next cycle. **Vmin = 8.70 V** (ripple 0.60 V).

From: Topic 17 Rule 84, peak detector checklist

</details>
