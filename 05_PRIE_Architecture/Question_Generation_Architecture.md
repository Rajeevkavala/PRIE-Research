# Question Generation Architecture: Causal Concept DAG-Guided Cognitive Assessment (M10)

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `05_PRIE_Architecture/Question_Generation_Architecture.md`  
**Phase**: 05 — PRIE Architecture  
**Status**: Authoritative Question Generation Architecture Specification  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`)  
**Date**: September 2026  

---

## 1. Research Grounding & The Trivial Distractor Crisis

In higher education automatic question generation (AQG), unconstrained large language model prompting suffers from severe pedagogical deficiencies identified in Phase 02 (`02_Cross_Analysis/Future_Work_Matrix.md`) and validated in Phase 03 (`03_Research_Problem/Gap_Validation.md` — `RG6`):
1. **The Non-Functional Distractor Epidemic**: As established by **Paper26** (Fernandez & Gomez 2025), **78%** of LLM-generated multiple-choice questions (MCQs) feature trivial, absurd, or grammatically mismatched distractors. Examinees easily eliminate them through superficial test-taking heuristics without demonstrating conceptual mastery.
2. **Superficial Recall Bias**: Unconstrained LLMs generate definitions and keyword recall questions (Bloom's Level 1) rather than multi-step cognitive application or debugging items (Bloom's Level 3–4).
3. **Absence of Psychometric Calibration**: Standard LLM questions have uncalibrated difficulty ($p$) and near-zero item discrimination ($DI < 0.20$), failing to differentiate high-ability from low-ability candidates (**Paper39**).

PRIE overcomes these limitations through a **Causal Concept DAG-Guided Chain-of-Thought Question Generation Architecture** (`DD-009`, `M10`), anchoring distractor generation directly in verified Computer Science student misconception pathways.

---

## 2. Causal Concept AQG Subsystem Topology

```
                  ┌────────────────────────────────────────────────────────┐
                  │ 1. TARGET SELECTION & MISCONCEPTION GRAPH MAPPING      │
                  │ • Ingests Target Concept Node v from CS Concept DAG    │
                  │   (e.g., "Virtual Memory Page Replacement: LRU")       │
                  │ • Ingests Documented Misconception Branches:           │
                  │   - Misconception A: Confusing LRU with FIFO           │
                  │   - Misconception B: Inverting Page Fault Counting     │
                  │   - Misconception C: Ignoring Frame Reference Bits     │
                  └───────────────────────────┬────────────────────────────┘
                                              │
                                              ▼
                  ┌────────────────────────────────────────────────────────┐
                  │ 2. CAUSAL CONCEPT-GUIDED CHAIN-OF-THOUGHT PROMPTER     │
                  │ • Enforces 4-Step CoT Prompt Template:                 │
                  │   Step 1: Formulate Scenario / Code Snippet            │
                  │   Step 2: Compute True Correct Key via Ground Truth    │
                  │   Step 3: Deduce Distractor 1 from Misconception A     │
                  │   Step 4: Deduce Distractor 2 from Misconception B     │
                  │   Step 5: Deduce Distractor 3 from Misconception C     │
                  └───────────────────────────┬────────────────────────────┘
                                              │
                                              ▼
                  ┌────────────────────────────────────────────────────────┐
                  │ 3. LOCAL QUANTIZED LLM / SLM INFERENCE WORKER          │
                  │ • Local Llama-3-8B-Instruct (vLLM) / Frontier API      │
                  │ • Output: Structured JSON Item Specification           │
                  └───────────────────────────┬────────────────────────────┘
                                              │
                                              ▼
                  ┌────────────────────────────────────────────────────────┐
                  │ 4. MULTI-STAGE ITEM VALIDATION & PSYCHOMETRIC FILTER   │
                  │ • Syntax & JSON Schema Validation                      │
                  │ • Semantic Deduplication (SBERT Embedding < 0.85)      │
                  │ • Distractor Plausibility Filter (DPI >= 0.70)         │
                  │ • Code Syntax Verification (Docker Sandbox Execution)  │
                  └───────────────────────────┬────────────────────────────┘
                                              │
                                ┌─────────────┴─────────────┐
                                ▼                           ▼
                         [FILTER: PASS]              [FILTER: FAIL]
                                │                           │
                     Persist in Validated        Reject Item & Regenerate
                     Question Bank (M03)         with Adjusted Prompt Seed
```

---

## 3. The 4-Step Causal Distractor Formulation Mechanics

Rather than asking the model to "invent 3 wrong options," PRIE prompts the generative model along verified causal error pathways:

```
[Target Concept: B-Tree Indexing Order-M]
       │
       ├─► Correct Key: "A B-Tree of order M can have at most M-1 keys per node."
       │
       ├─► Causal Error Branch 1 (Off-by-One Confounds):
       │   Distractor 1: "At most M keys per node." (Result of confusing keys with pointers)
       │
       ├─► Causal Error Branch 2 (Binary Search Tree Bleed):
       │   Distractor 2: "At most 2 keys per node regardless of order M." (Over-generalization of BST)
       │
       └─► Causal Error Branch 3 (Leaf Inversion):
           Distractor 3: "Internal nodes hold M-1 keys, but leaf nodes hold unlimited keys."
```

**Diagnostic Benefit**: When an examinee selects Distractor 1 during an assessment (`M03`), PRIE does not merely record "incorrect (-1)"; it updates the Student Profile Vector with the exact diagnostic insight:
$$\text{Insight} = \text{"Student conflates B-tree pointer order } M \text{ with internal key capacity } M-1\text{"}$$
This insight is immediately passed to the Roadmap Generator (`M08`) to schedule targeted prerequisite remediation.

---

## 4. Multi-Stage Safeguards & Verification Filters

### 4.1 Anti-Duplication Filter
- Computes dense Sentence-BERT embeddings of the newly generated question stem.
- Performs cosine nearest-neighbor search against existing question bank items in ChromaDB.
- If $\cos(\mathbf{e}_{\text{new}}, \mathbf{e}_{\text{existing}}) > 0.85$, the item is rejected as a redundant semantic duplicate.

### 4.2 Automated Code Verification
- If the question stem contains a code snippet or requires predicting terminal stdout:
  - The code is executed inside the ephemeral Docker sandbox (`DD-006`).
  - Output stdout is compared against the generated "Correct Key".
  - If sandbox execution throws a syntax error or produces a differing output, the question is discarded immediately.

### 4.3 Psychometric Calibration Targets (Classical Test Theory)
Every item generated by `M10` is tracked dynamically across student test submissions to compute classical psychometric parameters:
1. **Item Difficulty Index ($p$-value)**:
   $$p = \frac{\text{Number of correct examinees}}{\text{Total examinees}} \in [0.30, 0.70]$$
   Items with $p > 0.85$ (too trivial) or $p < 0.20$ (ambiguous/too obscure) are flagged for human review.
2. **Item Discrimination Index ($DI$)**:
   $$DI = p_{\text{upper 27\%}} - p_{\text{lower 27\%}} \ge 0.35$$
   Guarantees that high-performing students consistently answer correctly while struggling students choose diagnostic distractors.
3. **Distractor Plausibility Index ($DPI$)**:
   $$DPI = \frac{\text{Count of non-keyed distractors chosen by } \ge 5\% \text{ of examinees}}{3} \ge 0.70$$
   Mathematically certifies that distractors are functional and realistic rather than obvious throwaways.

---

## 5. Experimental Validation Plan Linkage

The AQG architecture is directly validated under **`EXP-5`** (`Experimental_Decisions.md`):
- **Hypothesis H5**: Automatic question generation guided by causal concept DAGs yields technical multiple-choice questions with statistically higher psychometric Item Discrimination ($DI \ge 0.35$) and Distractor Plausibility ($DPI \ge 0.70$) than unconstrained zero-shot LLM generation.
- **Experimental Protocol**: Administer diagnostic quizzes across 300 engineering students ($300 \times 40$ item matrix); compare Causal DAG AQG vs standard GPT-4o / Llama-3-8B baseline prompting via Kolmogorov-Smirnov test and Fisher's exact test.
