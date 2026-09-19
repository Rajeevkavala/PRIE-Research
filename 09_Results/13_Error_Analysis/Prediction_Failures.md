# In-Depth Placement Prediction Failure Analysis
**Project**: ScholarCamp  
**Subsystem**: Placement Readiness Intelligence Engine (PRIE) — Module $M_{06}$  
**Document**: `09_Results/13_Error_Analysis/Prediction_Failures.md`  
**Phase**: Phase 09 — Results, Analysis & Research Findings  
**Status**: COMPLETE, AUDITED & EMPIRICALLY CERTIFIED  

---

## 1. Objective
To perform a structured, transparent post-mortem of false positive ($\text{FP}$) and false negative ($\text{FN}$) classification failures in the Calibrated XGBoost Placement Predictor ($M_{06}$).

---

## 2. Quantitative Confusion Profile (Seed 42, $N_{\text{test}} = 250$)
- **True Positives ($\text{TP}$)**: $159$ candidates (Correctly predicted ready).
- **True Negatives ($\text{TN}$)**: $76$ candidates (Correctly identified at-risk).
- **False Positives ($\text{FP}$)**: $11$ candidates ($4.4\%$, Unplaced students predicted ready).
- **False Negatives ($\text{FN}$)**: $4$ candidates ($1.6\%$, Placed students predicted at-risk).

---

## 3. Detailed Failure Archetype Investigations

### Archetype A: The "High-GPA Bookworm" False Positive ($\text{FP}$, $N=7$ of 11)
- **Profile Characteristics**:
  - Academic Indicators: $\text{CGPA} = 8.65 \pm 0.42$, $\text{Backlogs} = 0$.
  - Practical & Behavioral: $\text{Mock Interview} = 42.5 \pm 5.1 / 100$, $\text{Project Count} = 0$, $\text{Consistency} = 0.32$.
- **Failure Mechanism**: The gradient-boosted decision trees assigned heavy positive split weights to academic thresholds ($F_{01} > 8.0$), which dominated the negative contribution from low mock interview performance. In physical recruitment, corporate interviewers filtered these candidates during behavioral and communication rounds.
- **Pedagogical Danger**: **High Risk**. Predicting that an academically strong but behaviorally unprepared student is "Ready" produces false confidence, depriving them of timely speech coaching.
- **Mitigation**: Adjust classification thresholds for students with $F_{07} < 50$, forcing an automated advisory flag regardless of academic marks.

### Archetype B: The "Compensatory Hacker" False Negative ($\text{FN}$, $N=3$ of 4)
- **Profile Characteristics**:
  - Academic Indicators: $\text{CGPA} = 6.42 \pm 0.28$, $\text{Backlogs} = 1$.
  - Practical & Behavioral: $\text{Programming Score} = 94/100$, $\text{Project Count} = 4$, $\text{Internship Months} = 6$.
- **Failure Mechanism**: The tree ensemble penalized the active backlog and sub-7.0 GPA, assigning a low predicted readiness ($P = 0.38$). In reality, top-tier tech firms fast-tracked these candidates based on practical coding and open-source contributions.
- **Pedagogical Danger**: **Low Risk**. The false warning prompts the student to continue intense preparation, acting as a conservative advisory error.
- **Mitigation**: Introduce a non-linear interaction feature capturing high-velocity coding artifacts compensating for academic dips.

---

## 4. Evidence Status
**STATUS: VALIDATED (FAILURE ANALYSIS)**  
Derived from audited test fold instances in `08_Experiments/15_Experiment_Results/EXP-1/`.
