# EC Lock-In: EEEN20020 Electrical and Electronic Circuits (final exam)

Cram notes for **EEEN20020 Electrical and Electronic Circuits** (Prof. Peter Kennedy), final on **Tuesday 15 December**. Built from Lectures 1 to 28, Homeworks 0 to 4, and **ten past papers** (five Autumn finals 2021 to 2025, five Spring resits 2021 to 2025).

**▶ Practice site: https://lanceyprance.github.io/EC-lockin/** (exam drill, check-your-number questions, the ten timed past papers and three mock finals). It reads the `questions/`, `papers/` and `mock/` md files directly, so editing them updates the site.

Start at **[TOPICS.md](TOPICS.md)** (progress tracker). Day-by-day plan to the exam: **[PLAN.md](PLAN.md)**.

- The sheet to **print and bring in** (open-book exam): **[formula-sheet.md](formula-sheet.md)**
- Confusing bits I asked about, plus slips found in the material: **[questions-asked.md](questions-asked.md)**
- Past finals: [2025](papers/2025.md) · [2024](papers/2024.md) · [2023](papers/2023.md) · [2022](papers/2022.md) · [2021](papers/2021.md)
- Past resits: [2025](papers/2025-resit.md) · [2024](papers/2024-resit.md) · [2023](papers/2023-resit.md) · [2022](papers/2022-resit.md) · [2021](papers/2021-resit.md)
- Mock finals: **[Mock 1](mock/final-1.md)** · **[Mock 2](mock/final-2.md)** · **[Mock 3](mock/final-3.md)**

## The exam

- **2 hours. Answer all three questions.** Q1 is 100 marks (five parts of 20%). Q2 and Q3 are 50 marks each. Identical layout in all ten past papers.
- **Open book:** any printed notes. No laptop or phone. Calculator allowed.
- 65% of the module (homeworks 20%, labs 15%).
- Every year:
  - **Q1:** a resistive network, a transient, an impedance, an AC power or transformer part, and an op-amp filter or diode part.
  - **Q2:** frequency response: H(ω), a special frequency, Vout(t).
  - **Q3:** usually a diode waveform (sketch, max, min, period). Sometimes a transistor amplifier, a transformer load or an RC square wave.

## Reading style (dyslexia-friendly)

- One idea per line. Short sentences.
- Big equations on their own line.
- Lots of space between sections.
- Few brackets, little italics, no long bullet points.

## Notation (same as the slides)

| Write | Means |
|---|---|
| e1, e2 | node voltages (relative to ground) |
| V, I (capitals) | phasors (complex) |
| v(t), i(t) | time functions (real) |
| Z, Y | impedance, admittance |
| R1 ∥ R2 | R1 in parallel with R2 |
| r∠θ | polar form: size r, angle θ |
| Z* | complex conjugate |
| ω = 2πf | angular frequency |

## How each topic is built

- `notes/NN-topic.md`: slide diagrams with **"How to read this diagram"** in plain words, and **🧠 check questions** inline (answer before opening).
- **🎯 In the final**: exactly which past-paper parts used this topic.
- **⭐ Learn by heart**: the short list for that topic. All of them are collected on the [exam sheet](formula-sheet.md).
- **📐 boxes** for every rule and equation, numbered 1 to 91 across the whole repo.
- **Worked examples** of past-paper questions, **drawing checklists** for every sketch, and a **method table** at the end: "You're asked for… / Use…".
- `questions/NN-topic.md`: end-of-topic test.
  - Part A: the homework, lecture-example and past-paper questions on that topic.
  - Part B: exam-style questions in other formats (true/false, multiple choice, calculate, explain).
- **Rule:** every answer cites the notes section (§) or box it comes from.

## Answers

- **Final 2025, Homework 0 and the 2025 versions of Homeworks 1 to 3 have official answers.** They are marked "(official)".
- **Everything else is my own working.** Every number in the notes, questions and papers is recomputed in Python with a small circuit solver: `python3 tools/check_numbers.py` and `python3 tools/check_mocks.py` (need numpy). The solver reproduces every official answer.
- Homework values use **all Greek-letter offsets = 0** (α = γ = δ = … = 0). Your own sheets add your student-number digits, so your numbers differ slightly. The method is identical.
- A few papers have slips (missing values, mismatched answer boxes). They're flagged with ⚠️ and listed in [questions-asked.md](questions-asked.md).
- Homework 4 has no solutions. Its answers here are mine, also checked in Python.

## Folders

```
notes/       one file per topic (1–18)
questions/   end-of-topic tests
papers/      ten past papers with worked answers
mock/        three mock finals
img/NN/      slide snippets: Lx-sN.png = Lecture x, slide N
img/papers/  past-paper figures (f = Autumn final, r = Spring resit)
img/hw/      homework figures (h = 2026 sheets, hx = 2025 versions)
site/        the practice site (index.html at the root)
tools/       solver, number checks, link/parse/reference checks, snippet cutters
```

## Checks

```bash
python3 tools/check_numbers.py
```

```bash
python3 tools/check_mocks.py
```

```bash
python3 tools/check_links.py
```

```bash
python3 tools/check_refs.py
```

```bash
node tools/check_site_parse.js .
```
