# Question Generation Methodology: Causal Concept DAGs, Distractor Mechanics & Psychometric Calibration

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/Question_Generation_Methodology.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative AQG Protocol  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. The Trivial Distractor Crisis in LLM Assessment (`RG6`)

Automatic Question Generation using unconstrained zero-shot LLM prompts (`Paper25`, `Paper26`, `Paper39`) yields multiple-choice questions with superficial, implausible distractors (e.g., syntax-error options easily eliminated by students without understanding the core concept). This results in near-zero psychometric discrimination, rendering diagnostic tests useless for identifying true misconceptions.

PRIE introduces **Causal Concept DAG-Guided Chain-of-Thought AQG** (`DD-009`, `M10`, `EXP-5`), where distractors are explicitly derived from documented student conceptual error paths:

```
[Target CS Concept: e.g., Quicksort Worst-Case Complexity]
                              │
                              ▼
        Identify Documented Student Misconceptions
        Misconception A: Confusing Quicksort with Mergesort (O(n log n))
        Misconception B: Forgetting unbalanced partition recursion depth (O(n))
        Misconception C: Confusing best-case with average-case
                              │
                              ▼
        Construct Misconception-Grounded Multiple Choice Options
        • Key (Correct): O(n^2) - Arises when pivot is smallest/largest
        • Distractor 1: O(n log n) - Derived from Misconception A
        • Distractor 2: O(n) - Derived from Misconception B
        • Distractor 3: O(log n) - Derived from Misconception C
                              │
                              ▼
        Psychometric Calibration (Item Difficulty P, Discrimination DI, DPI)
```

---

## 2. Psychometric Calibration Framework (Classical Test Theory & IRT)

To evaluate question quality rigorously in `EXP-5`:

### 2.1 Item Difficulty Index ($P$-value)
The proportion of students answering the item correctly:
$$P = \frac{R}{N} \in [0.0, 1.0]$$
Target calibration zone for effective diagnostic gating: $0.35 \le P \le 0.75$.

### 2.2 Item Discrimination Index ($DI$)
The ability of the question to distinguish between top-performing ($U$) and bottom-performing ($L$) student quartiles:
$$DI = \frac{R_U - R_L}{N/2} \in [-1.0, +1.0]$$
A question is psychometrically acceptable if $DI \ge 0.35$. Items with $DI < 0.20$ are purged from the test bank.

### 2.3 Distractor Plausibility Index ($DPI$)
Measures whether distractors genuinely attract lower-performing students:
$$DPI(d) = \frac{N_{\text{chosen}}(d, L)}{N_L}$$
A distractor is functional if $DPI(d) \ge 0.05$. If a distractor receives zero student selections across 100 attempts, it is flagged as a Non-Functional Distractor ($NFD$).
