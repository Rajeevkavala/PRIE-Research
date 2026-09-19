# Academic Conference Poster Layout Specification

**Document**: `10_Publication/07_Poster/Poster_Layout.md`  
**System**: Placement Readiness Intelligence Engine (PRIE)  
**Phase**: Phase 10 — Publication  
**Standard Dimensions**: Standard A0 (841 mm $\times$ 1189 mm, Landscape or Portrait)  

---

## 3-Column Visual Layout Structure

```
+---------------------------------------------------------------------------------------------------------------+
|                                                HEADER BANNER                                                  |
|  PRIE: An Explainable Placement Readiness Intelligence Engine with Calibrated Predictive Modeling and Recourse|
|  Anonymous Authors | Department of Computer Science & Engineering | Affiliated Engineering Institution        |
+---------------------------------------+---------------------------------------+-------------------------------+
|               COLUMN 1                |               COLUMN 2                |            COLUMN 3           |
|      PROBLEM & ARCHITECTURE           |       METHODOLOGY & RECOURSE          |      EMPIRICAL RESULTS        |
+---------------------------------------+---------------------------------------+-------------------------------+
| 1. The Employability Disconnect       | 4. Platt Probability Calibration      | 7. Predictive Benchmark       |
|    - Educational fragmentation        |    - Sigmoid scaling: ECE <= 0.035    |    - XGBoost vs Baselines     |
|    - Black-box classification void    |    - Reliable risk estimates          |    - Table 1 (Acc 94.6%, AUC) |
|    - Lack of student agency           |    - Reliability curves [Fig 1]       |    - ROC/PR curves [Fig 2]    |
|                                       |                                       |                               |
| 2. The 22-D Student Profile Vector    | 5. Prescriptive Recourse (DiCE)       | 8. Multimodal Interview       |
|    - Academic SIS records             |    - Bounded sparsity: k <= 3         |    - Tri-modal late fusion    |
|    - Diagnostic tests (DSA, OS)       |    - 100% lock on F17 (Branch)        |    - 77.98% variance damping  |
|    - Resume embeddings (SBERT)        |    - Actionable intervention card     |    - Modality ablation [Fig 4]|
|    - Behavioral telemetry & mask      |    - TreeSHAP bee-swarm [Fig 3]       |                               |
|                                       |                                       | 9. Topological Roadmaps       |
| 3. System Microservice Architecture   | 6. 2D Spatial Coordinate ATS Parsing  |    - Kahn's DAG scheduling    |
|    - 4-Tier closed-loop framework     |    - Mitigates column interleaving    |    - 0 Precedence violations  |
|    - Data -> State -> XAI -> Action   |    - Entity Macro-F1 = 0.8421         |    - Concept graph [Fig 5]    |
|    - High-level architecture [Fig 7]  |    - Reading order preservation       |                               |
|                                       |                                       | 10. Summary & Open Trials     |
+---------------------------------------+---------------------------------------+-------------------------------+
|                                                FOOTER BAR                                                     |
|  IEEE / ACM Research Dissemination | Open-Source Code: https://github.com/scholar-camp/prie-core | Contact QR |
+---------------------------------------------------------------------------------------------------------------+
```

---

## Typography & Color Palette
* **Header Font**: Helvetica / Inter Bold (64pt).
* **Section Titles**: Arial / Roboto Bold (36pt), Primary Color: `#1E3A8A` (Deep Navy).
* **Body Text**: Inter / Calibri Regular (24pt), `#222222`.
* **Accent Colors**: Accent Gold `#D97706`, Success Green `#059669`, High-Risk Coral `#DC2626`.
* **Figure Callouts**: Embedded high-resolution PNGs at 300 DPI.
