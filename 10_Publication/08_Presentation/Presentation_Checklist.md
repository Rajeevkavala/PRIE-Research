# Conference Presentation Rehearsal & AV Checklist

**Document**: `10_Publication/08_Presentation/Presentation_Checklist.md`  
**System**: Placement Readiness Intelligence Engine (PRIE)  
**Phase**: Phase 10 — Publication  

---

## 1. Timing & Structure Verification
- [x] Total slide count: Exactly 16 slides.
- [x] Target duration: 15 minutes presentation (~55 seconds per slide) + 5 minutes Q&A.
- [x] Section balance: Motivation (Slides 1–4), Method & Arch (Slides 5–8), Empirical Results (Slides 9–14), Limitations & Conclusion (Slides 15–16).

## 2. Visual & Diagram Verification
- [x] Embedded high-resolution diagrams: Fig 1 (Calibration), Fig 2 (ROC/PR), Fig 3 (TreeSHAP), Fig 4 (Multimodal Ablation), Fig 5 (Concept DAG), Fig 6 (Persona Radar), and High-Level Architecture.
- [x] Slide typography compliant: High-contrast fonts, no walls of unformatted text, key metrics emphasized in bold.

## 3. Anticipated Reviewer Q&A Talking Points
- **Q: Why did Logistic Regression achieve a higher F1-score (0.9892) than XGBoost on synthetic data?**  
  *A: The synthetic generator relies on linear and piecewise-linear combinations, making synthetic data linearly separable. In real-world data, feature interactions and non-linear thresholds dominate. Furthermore, XGBoost provides polynomial-time TreeSHAP feature attributions, which are essential for our closed-loop DiCE recourse.*
- **Q: How can you be certain that DiCE never suggests changing demographic major ($F_{17}$)?**  
  *A: We enforce a hard mathematical constraint in the DiCE optimization objective, locking $c_{17} = x_{17}$. In our empirical test on 30 profiles, the $F_{17}$ lock retention was exactly 100.0%.*
- **Q: Has this system been tested on real students in live hiring drives?**  
  *A: No; we explicitly disclose that longitudinal placement rate uplift ($H_{\text{uplift}}$) and recruiter panel correlations ($H_{\text{recruiter}}$) are marked as `DATA COLLECTION REQUIRED` for live institutional trials under institutional IRB oversight.*
