# Model Selection Methodology: Subsystem Portfolios, Candidate Baselines & Selection Taxonomies

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/Model_Selection.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative Model Selection Specification  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. Epistemological Model Selection Taxonomy

To maintain scientific integrity and prevent circular logic, PRIE enforces an explicit three-tiered model classification:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           MODEL SELECTION TAXONOMY                              │
├─────────────────────────────────────────────────────────────────────────────────┤
│  TIER 1: CANDIDATE MODEL                                                        │
│  • Scientifically viable models identified from Phase 01/02 literature.         │
│  • Evaluated during exploratory and preliminary benchmarking.                   │
│                                                                                 │
│  TIER 2: SELECTED FOR EXPERIMENT                                                │
│  • The specific architectural models designated in Phase 04 Design Decisions   │
│    (DD-002, DD-004, DD-005, DD-007, DD-008, DD-009) to test hypotheses H1–H6. │
│                                                                                 │
│  TIER 3: BEST AFTER EXPERIMENT                                                  │
│  • The empirically victorious model determined post-experimentation in Phase 08.│
│  • REQUIRES EMPIRICAL RESULTS. STRICTLY EXCLUDED FROM PHASE 06.                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Subsystem Model Selection Matrix

Every core PRIE intelligence subsystem defines its candidates, selected model, comparative baselines, and literature rationale:

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                          SUBSYSTEM MODEL SELECTION PORTFOLIO                                            │
├──────┬────────────────────────┬──────────────────────┬──────────────────────┬────────────────────┬──────────────────────┤
│ Mod  │ Functional Subsystem   │ Candidate Models     │ Selected Model       │ Baseline Model     │ Literature Grounding │
├──────┼────────────────────────┼──────────────────────┼──────────────────────┼────────────────────┼──────────────────────┤
│ M06  │ Static Predictor       │ XGBoost, LightGBM,   │ XGBoost (DD-002)     │ Logistic Regr, RF, │ Paper01, Paper06,    │
│      │                        │ CatBoost, MLP        │                      │ Decision Tree      │ Paper22, Paper24     │
├──────┼────────────────────────┼──────────────────────┼──────────────────────┼────────────────────┼──────────────────────┤
│ M06  │ Dynamic Sequence Model │ TFT, LSTM, GRU,      │ Temporal Fusion      │ Static XGBoost,    │ Paper02, Paper05,    │
│      │                        │ Informer             │ Transformer (DD-002) │ Standard LSTM      │ Paper33, Paper44     │
├──────┼────────────────────────┼──────────────────────┼──────────────────────┼────────────────────┼──────────────────────┤
│ M02  │ ATS Spatial Parser     │ LayoutLMv3, Donut,   │ LayoutLMv3 (DD-004)  │ spaCy NER, BERT,   │ Paper11, Paper12,    │
│      │                        │ OCR-Regex, LayoutXLM │                      │ Rule-based Regex   │ Paper17, Paper42     │
├──────┼────────────────────────┼──────────────────────┼──────────────────────┼────────────────────┼──────────────────────┤
│ M02  │ Resume-JD Semantic     │ Sentence-BERT, TFIDF,│ all-MiniLM-L6-v2     │ TF-IDF Cosine,     │ Paper11, Paper17,    │
│      │ Matching               │ OpenAI text-embed    │ (DD-004)             │ Word2Vec Averaging │ Paper36, Paper37     │
├──────┼────────────────────────┼──────────────────────┼──────────────────────┼────────────────────┼──────────────────────┤
│ M05  │ Mock Interview STT     │ Whisper, Conformer,  │ Chunked Whisper-base │ Cloud Whisper API  │ Paper03, Paper14,    │
│      │                        │ Vosk, Google STT API │ (DD-005)             │ (Batch)            │ Paper15, Paper28     │
├──────┼────────────────────────┼──────────────────────┼──────────────────────┼────────────────────┼──────────────────────┤
│ M05  │ Mock Interview Vision  │ MediaPipe FaceMesh,  │ Wasm MediaPipe       │ OpenFace, Python   │ Paper03, Paper14,    │
│      │                        │ OpenFace, Dlib       │ FaceMesh (DD-005)    │ Server Processing  │ Paper29, Paper30     │
├──────┼────────────────────────┼──────────────────────┼──────────────────────┼────────────────────┼──────────────────────┤
│ M07  │ Descriptive XAI        │ TreeSHAP, LIME,      │ Fast TreeSHAP        │ Permutation        │ Paper18, Paper19,    │
│      │                        │ Anchors              │ (DD-003)             │ Importance         │ Paper22, Paper34     │
├──────┼────────────────────────┼──────────────────────┼──────────────────────┼────────────────────┼──────────────────────┤
│ M07  │ Prescriptive Recourse  │ DiCE, Watcher,       │ DiCE Counterfactuals │ Standard SHAP      │ Paper02, Paper18,    │
│      │                        │ GeCo, Nearest-CF     │ (DD-003)             │ Feature Delta      │ Paper19, Paper32     │
├──────┼────────────────────────┼──────────────────────┼──────────────────────┼────────────────────┼──────────────────────┤
│ M08  │ Recommendation Engine  │ Topological A*, Collab│ A* Graph Search      │ Matrix Factorization│ Paper04, Paper13,    │
│      │                        │ Filtering, PageRank  │ on Concept DAG(DD-008│ Item-based CF      │ Paper16, Paper35     │
├──────┼────────────────────────┼──────────────────────┼──────────────────────┼────────────────────┼──────────────────────┤
│ M09  │ Curriculum RAG         │ ChromaDB + Cross-Enc,│ Two-Stage RAG        │ BM25 Keyword,      │ Paper20, Paper21,    │
│      │                        │ FAISS, Single Dense  │ with Triad (DD-007)  │ Single Dense Retr. │ Paper23, Paper39     │
├──────┼────────────────────────┼──────────────────────┼──────────────────────┼────────────────────┼──────────────────────┤
│ M10  │ Automated Question Gen │ Causal Concept DAG,  │ Causal DAG Chain-of- │ Zero-Shot LLM,     │ Paper25, Paper26,    │
│      │                        │ Zero-Shot, Few-Shot  │ Thought (DD-009)     │ Template AQG       │ Paper39, Paper40     │
└──────┴────────────────────────┴──────────────────────┴──────────────────────┴────────────────────┴──────────────────────┘
```

---

## 3. Detailed Selection Rationale by Subsystem

### 3.1 Static Predictor Selection (XGBoost vs LightGBM vs CatBoost)
- **Literature Evidence**: Across `Paper01`, `Paper06`, `Paper22`, and `Paper24`, gradient-boosted decision trees consistently outperformed deep multi-layer perceptrons (MLPs) and linear models on tabular educational records ($F_1$ deltas $+0.12$ to $+0.18$).
- **Engineering Rationale**: XGBoost provides native exact tree traversal algorithms required for millisecond TreeSHAP explainer execution (`M07`), direct handling of sparse missing values, and robust scale-invariant split finding.
- **Selection**: `XGBoost` is selected as the authoritative static classification baseline (`DD-002`).

### 3.2 Longitudinal Sequence Forecaster Selection (TFT vs LSTM vs Informer)
- **Literature Evidence**: Standard LSTMs operate as black-box recurrent processors that fail to provide multi-horizon uncertainty intervals or self-attention over specific historical weeks (`Paper02`, `Paper05`, `Paper33`).
- **Engineering Rationale**: Temporal Fusion Transformers (TFT) integrate Gated Residual Networks (GRN), Variable Selection Networks (VSN), and Multi-Head Self-Attention, enabling interpretable quantile forecasting ($q_{0.1}, q_{0.5}, q_{0.9}$) across multi-month horizons.
- **Selection**: `TFT` is selected for dynamic longitudinal forecasting (`DD-002`, `EXP-3`).

### 3.3 ATS Vision-Language Selection (LayoutLMv3 vs Flat-Text NER)
- **Literature Evidence**: 60% of modern undergraduate technical resumes use two-column or multi-column visual layouts. Flat-text OCR interleaves horizontal text lines, destroying semantic coherence (`Paper11`, `Paper17`, `Paper36`).
- **Engineering Rationale**: LayoutLMv3 unifies word embeddings with 2D spatial bounding boxes $[x_0, y_0, x_1, y_1]$ and visual patch embeddings, recognizing layout columns as independent spatial blocks.
- **Selection**: `LayoutLMv3` is selected as the core document intelligence model (`DD-004`, `EXP-1`).
