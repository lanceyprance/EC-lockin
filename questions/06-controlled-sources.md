# Topic 6: End-of-topic test

Try each question first.
Then click to check.

Each answer says which notes section (§) it comes from.

Homework Greek-letter offsets are set to 0.

---

## Part A: Homework and past-final questions

### F2025-1b (Final 2025 Q1b)

![Fig 1(b)](../img/papers/f2025-1b.png)

Calculate the Thévenin resistance to the left of A and B. I(F) = β I(Rpi).

Vs = 9 sin(2000πt) V, Rs = 50 Ω, Rpi = 5600 Ω, β = 200, Ro = 100 kΩ.

<details><summary>Answer</summary>

Turn off Vs, keep F. Test voltage v_t at A: I(Rpi) = −v_t/5650.

i_t = v_t/Ro + v_t/5650 + 200 v_t/5650.

Rth = 100 k ∥ (5650/201) = 100 k ∥ 28.11 = **28.1 Ω** (official answer).

From: worked example, Rule 27, Equation 29

</details>

---

### F2023-3 (Final 2023 Q3)

![Fig 3](../img/papers/f2023-3.png)

(a) Find H = Vo/Vs in terms of Rs, R1, R2 and g_m. (b) Rs = 1 kΩ, R1 = 500 Ω, R2 = 10 kΩ. What g_m gives H = 20 dB?

<details><summary>Answer</summary>

**(a)** No gate current, so the gate is at Vs. v_gs = Vs − g_m v_gs R1 → v_gs = Vs/(1 + g_m R1). Vo = −g_m v_gs R2.

**H = −g_m R2 / (1 + g_m R1)** (Rs drops out.)

**(b)** |H| = 10: 10 000 g_m = 10 (1 + 500 g_m) → 5000 g_m = 10 → **g_m = 2 mS**.

From: worked example, Equation 30, Equation 31

</details>

---

### R2024-3 (Resit 2024 Q3)

![Fig 3](../img/papers/r2024-3.png)

Same circuit. Rs = 1 kΩ, R1 = 470 Ω, R2 = 22 kΩ. What g_m gives H = 30 dB?

<details><summary>Answer</summary>

|H| = 10^(30/20) = 31.62.

g_m × 22 000 = 31.62 (1 + 470 g_m) → g_m (22 000 − 14 862) = 31.62.

**g_m = 4.43 mS**

From: Equation 30, Equation 31

</details>

---

### H1-2 (Homework 1 Q2)

![Fig 2](../img/hw/h1-2.png)

The VCVS gives vo = A vd, with vd = V(Input) − e2. R4 is in series with its output. R1 and R2 feed back from Output to node 2.

(a) Write Vo/c (RL open). (b) Write Is/c (RL shorted). Then with Vs = 100 mV, Rs = 50 Ω, R3 = 10 kΩ, R4 = 75 Ω, A = 100 kV/V, R1 = 10 kΩ, R2 = 2.2 kΩ, RL = 32 Ω find (c) Vout, (d) the power supplied by Vs, (e) the power in RL.

<details><summary>Answer</summary>

Input divider: Vin = Vs R3/(Rs + R3) (no current into the VCVS input).

**(a)** RL open: one current through R4, R1, R2. e2 = vo R2/(R4 + R1 + R2), and vo = A(Vin − e2):

**Vo/c = A Vin (R1 + R2) / (R4 + R1 + R2 + A R2)**, with Vin = Vs R3/(Rs + R3).

**(b)** RL shorted: Output = 0, so e2 = 0 and vo = A Vin:

**Is/c = A Vin / R4 = A Vs R3 / (R4 (Rs + R3))**

**(c)** Vin = 99.50 mV. With A this big the gain is almost exactly 1 + R1/R2 = 5.545:

**Vout = 0.552 V** (the 32 Ω load barely changes it: the feedback makes the output resistance tiny).

**(d)** P(Vs) = Vs²/(Rs + R3) = 0.01/10 050 = **995 nW**.

**(e)** P(RL) = 0.5517²/32 = **9.51 mW**.

(Is/c works out at 133 A: a "theoretical" number. A real amplifier would saturate long before that.)

From: §2, §3, Equation 28

</details>

---

### HX1-2 (Homework 1 (2025) Q2)

![Fig 2, 2025](../img/hw/hx1-2.png)

Last year's version, no R4 and no RL. Vs = 100 mV, Rs = 50 Ω, R3 = 10 kΩ, A = 100 kV/V, R1 = 18 kΩ, R2 = 2.2 kΩ. Find Vout, P(Vs), P(R1), P(R2).

<details><summary>Answer</summary>

Vin = Vs R3/(Rs + R3). Vout = A (R1 + R2) Vin / (R1 + R2 + A R2).

**Vout = 913.5 mV**, **P(Vs) = 995 nW**, **P(R1) = 36.8 μW**, **P(R2) = 4.5 μW** (all official).

Note: P(R1) + P(R2) ≫ P(Vs). The extra power comes from the VCVS (an active element).

From: §2, Equation 28

</details>

---

### H2-1b (Homework 2 Q1b)

![Fig 1(b)](../img/hw/h2-1b.png)

Find the maximum positive value of Vout. Vin = 250 sin(4000πt) mV, Rg = 1 kΩ, Rf = 10 kΩ, g_m = 2.2 mS, Ro = 100 kΩ, RL = 5.6 kΩ. The VCCS current g_m v_gs flows from the output node to ground.

<details><summary>Answer</summary>

Let R' = Ro ∥ RL = 5303 Ω.

KCL at the output: (vo − e2)/Rf + g_m e2 + vo/R' = 0 → vo = −7.277 e2.

KCL at the gate: (e2 − vin)/Rg + (e2 − vo)/Rf = 0 → 1.1 e2 + 0.7277 e2 = vin (in mS) → e2 = 0.5471 vin.

Gain = −3.982. The output is an inverted sine of amplitude 3.982 × 0.25.

**Maximum positive Vout = 0.995 V** (when Vin is at its negative peak).

From: §1 Rule 26, Topic 5 Rule 23

</details>

---

### HX2-1b (Homework 2 (2025) Q1b)

![Fig 1(b), 2025](../img/hw/hx2-1b.png)

No Rf. Vin = 500 sin(2000πt) mV, Rg = 1 kΩ, G_m = 2.2 mS, Ro = 50 kΩ, RL = 4.7 kΩ. Find Vout and its maximum positive value.

<details><summary>Answer</summary>

No gate current, so v_gs = Vin. The VCCS current flows into Ro ∥ RL:

**Vout = −G_m (Ro ∥ RL) Vin** = −9.45 Vin

Maximum positive value: 9.45 × 0.5 = **4.72 V** (official).

From: §2

</details>

---

### H2-1c (Homework 2 Q1c)

![Fig 1(c)](../img/hw/h2-1c.png)

Find Rth to the left of A and B, and the RL for maximum power. Rs = 100 Ω, Rpi = 10 kΩ, β = 199, Ro = 100 kΩ.

<details><summary>Answer</summary>

Same structure as Final 2025 Q1b (Equation 29):

Rth = Ro ∥ (Rs + Rpi)/(β + 1) = 100 k ∥ (10 100/200) = 100 k ∥ 50.5 = **50.47 Ω**

Maximum power: **RL = 50.47 Ω**.

From: Equation 29, Topic 4 Equation 22

</details>

---

### HX2-1c (Homework 2 (2025) Q1c)

![Fig 1(c), 2025](../img/hw/hx2-1c.png)

Now the CCCS (β = 150) and Ro = 80 kΩ both sit between node 3 and node 4, with RE = 470 Ω from node 4 to ground. Rs = 50 Ω, Rpi = 10 kΩ. Find Rth between A (node 3) and B (ground).

<details><summary>Answer</summary>

Test source at node 3. Here Equation 29 does **not** fit: use the full test-source method.

The result is

Rth = Ro [1 + β RE/(RE + Rs + Rpi)] + RE ∥ (Rs + Rpi) = 80 k × 7.70 + 449 = **616 kΩ** (official).

The emitter resistor RE multiplies the output resistance. Opposite to Final 2025 Q1b.

From: §3 Rule 27

</details>

---

### E10-4 (Lecture 10, Example 10.4)

Amplifier: A = 1000, Rs = 100 Ω, Ri = 10 kΩ, Ro = 8 Ω. (i) vs = 20 mV, RL = 4 Ω: find the load power. (ii) What RL maximises the load power, and what is it? (iii) What is the gain then, in dB?

<details><summary>Answer</summary>

**(i)** vL = (10 000/10 100) × 1000 × (4/12) vs = 330 vs = 6.6 V. P = 6.6²/4 = **10.89 W**.

**(ii)** Rth = Ro = 8 Ω, so **RL = 8 Ω**. vth = 990 × 0.02 = 19.8 V. P = 19.8²/(4 × 8) = **12.25 W**.

**(iii)** Gain = 990 × 8/16 = 495 → 20 log 495 = **53.9 dB**.

From: §2 Equation 28, §3, Equation 31

</details>

---

## Part B: Exam-style questions

### M1: True or false

1. A CCCS produces a current controlled by a current.
2. When finding Rth, you replace a VCVS by a short circuit.
3. A good voltage amplifier has a small input resistance.
4. A gain of 100 is 40 dB.
5. In Equation 30, if g_m R1 ≫ 1 the gain is about −R2/R1.

<details><summary>Answer</summary>

1. **True.** Rule 26.
2. **False.** Controlled sources stay on (Rule 27).
3. **False.** Large Ri, so it doesn't load the source (§2).
4. **True.** 20 log 100 = 40 dB (Equation 31).
5. **True.** The 1 becomes negligible (worked example).

</details>

---

### M2: Multiple choice

A VCCS has g_m = 5 mS and drives a 2 kΩ load. Its controlling voltage is 0.1 V. What is the load voltage (magnitude)?

- A. 0.5 V
- B. 1 V
- C. 10 V
- D. 0.25 V

<details><summary>Answer</summary>

**B.** i = 5 mS × 0.1 = 0.5 mA. v = 0.5 mA × 2 kΩ = 1 V.

From: §1 Rule 26

</details>

---

### M3: Calculate

A source vs with Rs = 1 kΩ drives an amplifier with Ri = 9 kΩ, A = 50, Ro = 100 Ω, into RL = 900 Ω. Find vL/vs.

<details><summary>Answer</summary>

(9/10) × 50 × (900/1000) = **40.5**

From: Equation 28

</details>

---

### M4: Explain

Why can't you find Rth of a circuit with a controlled source just by combining resistors?

<details><summary>Answer</summary>

The controlled source stays on and pushes a current (or voltage) that depends on what you apply. It changes the ratio v/i. You must apply a test source and compute v_t / i_t with the controlled source included.

From: §3 Rule 27

</details>
