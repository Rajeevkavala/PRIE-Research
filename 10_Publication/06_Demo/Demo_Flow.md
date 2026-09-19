# PRIE Demonstration Architecture & System Flow

**Document**: `10_Publication/06_Demo/Demo_Flow.md`  
**System**: Placement Readiness Intelligence Engine (PRIE)  
**Phase**: Phase 10 — Publication  

---

## 1. End-to-End Demonstration Data Flow

```
+-----------------------------------------------------------------------------------+
|                            STAGE 1: DATA INGESTION                                |
|  [Student Transcripts (SIS)] + [Resume PDF (PyMuPDF)] + [Diagnostic Quiz (M03)]    |
+------------------------------------------+----------------------------------------+
                                           |
                                           v
+-----------------------------------------------------------------------------------+
|                        STAGE 2: LATENT STATE ASSEMBLY                             |
|          Student Profile Vector Aggregator (M01): x_spv in R^22, Mask m           |
+------------------------------------------+----------------------------------------+
                                           |
                                           v
+-----------------------------------------------------------------------------------+
|                       STAGE 3: PREDICTION & CALIBRATION                           |
|          Cost-Sensitive XGBoost (M06) -> Platt Scaling: P(placed) in [0, 1]       |
+------------------------------------------+----------------------------------------+
                                           |
                     +---------------------+---------------------+
                     |                                           |
                     v                                           v
+---------------------------------------+   +---------------------------------------+
|        STAGE 4A: EXPLAINABILITY       |   |       STAGE 4B: RECOURSE ENGINE       |
|    TreeSHAP (M07) Attribution Matrix  |   |   Constrained DiCE (M07): Sparsity k<=3|
|   Isolates Negative Mutable Drivers   |   |   Locks Protected F17, Delta x* Output|
+--------------------+------------------+   +-------------------+-------------------+
                     |                                           |
                     +---------------------+---------------------+
                                           |
                                           v
+-----------------------------------------------------------------------------------+
|                         STAGE 5: CLOSED-LOOP REMEDIATION                          |
|    Kahn's Topological DAG Scheduler (M08): 38-Node CS Concept DAG (0 Violations)  |
|    Multimodal Mock Interview Coach (M05): Tri-Modal Late Fusion (1.18s Latency)   |
|    Curriculum RAG Assistant (M09): Semantic Cosine Gating (tau = 0.70)            |
+-----------------------------------------------------------------------------------+
```

---

## 2. Component API Interaction Flow
1. `POST /api/v1/profile/assemble`: Ingests raw candidate JSON, returns normalized 22-D vector $\mathbf{x}_{\text{spv}}$.
2. `POST /api/v1/predict`: Executes cost-sensitive XGBoost with Platt sigmoid scaling, returning calibrated probability $\hat{p}$ and confidence interval.
3. `POST /api/v1/explain/shap`: Computes polynomial-time TreeSHAP attributions and returns waterfall plot JSON coordinates.
4. `POST /api/v1/recourse/dice`: Solves constrained counterfactual optimization with $F_{17}$ lock, returning minimal feature shifts $\mathbf{\Delta x}^*$.
5. `POST /api/v1/roadmap/generate`: Invokes Kahn's topological sort over `cs_concept_dag.json`, returning a sequenced multi-week learning schedule with zero prerequisite violations.
6. `POST /api/v1/interview/analyze`: Ingests audio, video telemetry, and Faster-Whisper transcripts, returning tri-modal late fusion scores in $<1.5$s.
