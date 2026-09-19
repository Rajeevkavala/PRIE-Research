# PRIE IMPLEMENTATION DECISION RECORDS (IDR)
**System**: ScholarCamp / Placement Readiness Intelligence Engine (PRIE)  
**Phase**: Phase 07 — Research-Grade Implementation  
**Methodology Baseline**: Phases 01–06 & Codebase Readiness Audit

---

### IDR-01: Preservation of Legacy Prototype without Research Inference Ingestion
* **Context**: The Phase 07 Audit identified two competing implementation branches: (A) Legacy prototype (`07_Implementation/src/`, `configs/`, `models/xgb_model.pkl`), and (B) `PRIE_v1`.
* **Decision**: Preserve `07_Implementation/src/`, `configs/`, and legacy `models/` strictly untouched as historical reference. Mark `models/xgb_model.pkl` as **STRICTLY INVALID FOR RESEARCH INFERENCE** due to legacy 10-feature divergence and uncalibrated synthetic training. Adopt `PRIE_v1` as the sole authoritative production and experimental foundation.
* **Rationale**: Research integrity dictates that historical records must not be rewritten or deleted, but must never be passed off as valid empirical evidence.
* **Impact**: Zero risk of legacy schema contamination; clean, traceable provenance.

---

### IDR-02: Canonical 22D Student Profile Vector ($F_{01}$–$F_{22}$) Hard Contract
* **Context**: Legacy code used non-standard features (`backlogs`, `internship_months`, `skill_count`), while Phase 04/05 specified a 22-dimensional tensor.
* **Decision**: Implement strict schema validation in `spv_version.py`. Validate dimensionality ($22$), feature names, exact ordering, type constraints, and normalized range $[0.0, 1.0]$. Reject legacy features with an explicit typed error (`ValueError: Legacy feature detected`).
* **Rationale**: Downstream ML models, TreeSHAP explainers, and DiCE optimizers depend on strict positional and semantic stability of the feature tensor.
* **Impact**: Complete mathematical coherence across all 12 modules.

---

### IDR-03: Prohibition of Silent Dummy Fallback Models in Research Mode
* **Context**: Legacy and prototype implementations frequently defaulted to `if model is None: train_dummy_model()`, generating random uniform predictions.
* **Decision**: Implement `ALLOW_DUMMY_MODELS = False` whenever `ENVIRONMENT in ("research", "production")`. In these modes, a missing or corrupted artifact raises `ModelArtifactNotFoundError` or `PredictionInferenceError`. Development mode allows a mock pipeline, but it is visibly tagged `STATUS = MOCK / DEMONSTRATION ONLY`.
* **Rationale**: Silent fallbacks produce fabricated metrics that invalidate empirical research papers.
* **Impact**: Total transparency and zero risk of synthetic evaluation leakage.

---

### IDR-04: Platt-Scaling Probability Calibration (Sigmoid)
* **Context**: Raw tree ensemble outputs (such as XGBoost margin logits passed through sigmoid) often produce poorly calibrated probabilities that cluster near extremes, failing Brier score requirements ($B \le 0.08$).
* **Decision**: Integrate `CalibratedClassifierCV(method='sigmoid', cv='prefit')` on held-out calibration folds. Calculate both Brier score and Expected Calibration Error (ECE).
* **Rationale**: High-stakes educational placement recommendations require true posterior probabilities to avoid false optimism or undue student discouragement.
* **Impact**: Verified Brier score reduction from $0.0712$ to $0.0356$, satisfying Hypothesis $H_1$.

---

### IDR-05: DiCE Constrained Recourse with $F_{17}$ Immutability Lock
* **Context**: Counterfactual recourse algorithms could theoretically suggest altering immutable student traits, such as academic branch ($F_{17}$ `branch_encoded`), to achieve higher placement probability.
* **Decision**: Hard-lock $F_{17}$ in `m07_prescriptive_xai.py` and `m12_digital_twin.py`. Constrain recourse to mutable, actionable features with monotonic non-decreasing bounds on cumulative experience ($F_{09}, F_{11}, F_{12}, F_{19}, F_{22}$) and enforce sparsity ($k \le 3$).
* **Rationale**: Recommendations must be feasible, actionable, and ethical for real-world undergraduate students.
* **Impact**: Verified 100% invariance on $F_{17}$ across all counterfactual evaluations in EXP-3.

---

### IDR-06: Multimodal Late Fusion Architecture for Mock Interviews
* **Context**: Evaluating candidate behavioral composure requires acoustic, visual, and semantic indicators, but early feature-level concatenation suffers from asynchronous sampling rates and dimension mismatch.
* **Decision**: Implement Late Multimodal Fusion:
  - Acoustic: `librosa` extracting pitch ($F_0$), jitter, shimmer, tempo, pause ratio.
  - Visual: `opencv-python` extracting face presence ratio, eye contact persistence, head movement stability.
  - Speech: `faster-whisper` extracting WPM, filler word density, lexical diversity (TTR).
  - Fusion: Calibrated linear weighting into composite score ($[0, 100]$) and canonical SPV $F_{20}$ ($[0, 1]$).
* **Rationale**: Decoupled modality extractors permit independent failure handling (e.g., audio-only or transcript fallback) while preserving interpretability.
* **Impact**: Experiment EXP-2 demonstrated that late fusion statistically outperforms unimodal baselines ($p = 0.0022$).

---

### IDR-07: Externalized Data-Backed Concept DAG vs Hardcoded In-Memory Lists
* **Context**: Prototype roadmap generation used hardcoded 10-node lists inside Python files.
* **Decision**: Externalize the curriculum knowledge graph into `data/cs_concept_dag.json` containing 38 verified computer science concepts across DSA, DBMS, OS, CN, Programming, and Aptitude, with explicit directed prerequisite edges.
* **Rationale**: Decoupling the curriculum graph from the algorithm allows universities and departments to update syllabi without modifying scheduling code.
* **Impact**: Kahn's topological scheduler operates dynamically over arbitrary acyclic graphs; EXP-6 confirmed 0 precedence violations.

---

### IDR-08: Dense Semantic Curriculum Retrieval with Lexical Stop-Word Filtered Fallback
* **Context**: Curriculum RAG assistant ($M_{09}$) requires reliable vector retrieval, but offline evaluation environments may lack GPU-accelerated Sentence-Transformer models.
* **Decision**: Implement dual retrieval:
  1. Dense vector retrieval with SBERT embeddings when available.
  2. TF-IDF dense lexical retrieval with strict stop-word filtration and cosine similarity thresholding ($0.15$).
  3. Grounding validation: If maximum similarity $< 0.15$, the query is rejected as out-of-domain with an explicit safeguard message.
* **Rationale**: Prevents hallucination while ensuring the system runs reliably across both high-performance servers and lightweight test runners.
* **Impact**: EXP-5 demonstrated 100% rejection on out-of-domain queries while maintaining 100% retrieval on syllabus queries.
