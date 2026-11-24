# Topic 10: End-of-topic test

Try each question first.
Then click to check.

Each answer says which notes section (§) it comes from.

Use your calculator's polar/rectangular functions. Practise them now.

---

## Part A: Homework and past-final questions

### HX3-1a (Homework 3 (2025) Q1a)

Calculate the magnitude and phase of Z = R + jωL, with R = 1200 Ω, L = 1800 μH, f = 250 kHz.

<details><summary>Answer</summary>

ωL = 2π × 250 000 × 0.0018 = 2827.4 Ω.

Z = 1200 + j2827.4.

|Z| = √(1200² + 2827.4²) = **3071.5 Ω** (official)

∠Z = tan⁻¹(2827.4/1200) = **67.0° (1.17 rad)** (official)

From: §2 Equation 51

</details>

---

### HX3-1b (Homework 3 (2025) Q1b)

Calculate the magnitude and phase of Z = Z1Z2/(Z1 + Z2), with Z1 = R = 8200 Ω, Z2 = 1/(jωC), C = 100 nF, f = 500 Hz.

<details><summary>Answer</summary>

Z = R/(1 + jωRC). ωRC = 2π × 500 × 8200 × 100 n = 2.576.

|Z| = 8200/√(1 + 2.576²) = **2967 Ω** (official)

∠Z = −tan⁻¹(2.576) = **−68.8° (−1.2 rad)** (official)

From: §2, divide in polar

</details>

---

### E18-2 (Lecture 18, Example 18.2)

Convert −3 − j4 to polar form.

<details><summary>Answer</summary>

r = 5. tan⁻¹(4/3) = 53.1°, but a < 0 and b < 0: third quadrant.

**−3 − j4 = 5∠−126.9° = 5 e^(−j2.214)** (or 5∠233.1°).

From: §2, the quadrant trap

</details>

---

### E18-4 (Lecture 18, Self test 18.1)

z1 = 2 + j3, z2 = j5. Find z1 + z2, z1 z2 and z1/z2 in rectangular and polar form.

<details><summary>Answer</summary>

**z1 + z2 = 2 + j8 = 8.246∠1.326 rad**

**z1 z2 = −15 + j10 = 18.03∠2.554 rad**

**z1 / z2 = 0.6 − j0.4 = 0.721∠−0.588 rad**

From: §2

</details>

---

### E19-1 (Lecture 19, Example 19.1)

Convert to phasors: (i) 12 cos 1000t, (ii) 2 sin(100πt − 45°).

<details><summary>Answer</summary>

(i) **12∠0**

(ii) sin(100πt − 45°) = cos(100πt − 135°): **2∠−135° = −1.414 − j1.414**

From: §3 Rule 52, Rule 50

</details>

---

### E19-2 (Lecture 19, Example 19.2)

At f = 1000 Hz, convert to time functions: (i) −j, (ii) 3 + j4.

<details><summary>Answer</summary>

(i) −j = 1∠−90° → cos(2000πt − 90°) = **sin(2000πt)**

(ii) 3 + j4 = 5∠0.927 rad → **5 cos(2000πt + 0.927)**

From: §3 Rule 52

</details>

---

## Part B: Exam-style questions

### M1: True or false

1. A phasor contains the frequency of the sinusoid.
2. sin(ωt) = cos(ωt − 90°).
3. To multiply two complex numbers in polar form, multiply the sizes and add the angles.
4. tan⁻¹(b/a) always gives the right angle.
5. v(t) = 3 + j4 V is a valid time-domain answer.

<details><summary>Answer</summary>

1. **False.** Only amplitude and phase. ω is kept separately (§3).
2. **True.** Rule 50.
3. **True.** §2.
4. **False.** Add 180° when a < 0 (§2).
5. **False.** Time functions are real. Convert to r cos(ωt + θ) (§3).

</details>

---

### M2: Multiple choice

What is the phasor of 4 sin(ωt + 30°)?

- A. 4∠30°
- B. 4∠120°
- C. 4∠−60°
- D. 4∠−30°

<details><summary>Answer</summary>

**C.** sin(ωt + 30°) = cos(ωt + 30° − 90°) = cos(ωt − 60°).

From: Rule 50, Rule 52

</details>

---

### M3: Calculate

A phasor output is Vo = −2 + j4 at ω = 1000 rad/s. Write vo(t).

<details><summary>Answer</summary>

|Vo| = √20 = 4.472. Angle: a < 0, second quadrant: 180° − 63.43° = 116.6° (2.034 rad).

**vo(t) = 4.472 cos(1000t + 2.034) V**

(This is Lecture 20 Example 20.2.)

From: §2, §3

</details>

---

### M4: Explain

Why can you add phasors for two sources at 1 kHz, but not for a source at 1 kHz and another at 1 MHz?

<details><summary>Answer</summary>

A phasor stands for A cos(ωt + φ) with the e^(jωt) factor dropped. Adding phasors only makes sense if that dropped factor is the same for both, i.e. the same ω. At different frequencies, find each response separately and add the time functions (Final 2025 Q2b).

From: §3, worked example

</details>
