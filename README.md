# PRIE-Research: Placement Readiness Intelligence Engine Research Repository

Welcome to the official scientific research repository for **PRIE (Placement Readiness Intelligence Engine)**. This repository houses the complete theoretical foundation, literature evidence, system architecture, empirical methodology, experimental results, and publication materials intended for submission to top-tier conferences and journals in Educational Data Mining, Learning Analytics, and Artificial Intelligence in Education (e.g., IEEE / Springer).

---

## 1. Research Overview

The transition from tertiary engineering education to industrial employment represents a critical career transition. Despite widespread digital learning adoption, higher education institutions struggle with extreme fragmentation in career preparation: students utilize isolated resume scanners, generic mock interview tools, and static learning management systems. These disconnected tools fail to capture the multidimensional nature of career readiness.

**PRIE (Placement Readiness Intelligence Engine)** is an integrated continuous intelligence framework that models student placement readiness as a dynamic, continuous latent state. Rather than treating placement readiness as a post-hoc, point-in-time binary classification ($y \in \{0, 1\}$), PRIE ingests multi-modal evidence across:
- **Structured Academic & Diagnostic Records**: Cumulative GPA, backlogs, technical assessment performances.
- **Unstructured Linguistic Artifacts**: Natural Language Processing (NLP) resume entity extraction and semantic job-description alignment.
- **Behavioral & Interaction Telemetry**: Longitudinal practice consistency, platform engagement, and voice-driven interview performance.

These data streams are synthesized into a normalized **22-dimensional Student Profile Vector (SPV)**, which drives:
1. Supervised placement probability estimation via optimized gradient-boosted decision trees (**XGBoost**).
2. Axiomatic local and global feature attribution via **TreeSHAP** and **LIME**.
3. Closed-loop, prerequisite-aware adaptive remediation roadmaps and targeted skill assessment.

---

## 2. Research Evidence Provenance Chain

To ensure strict scientific validity, every design decision in PRIE is traceable through an end-to-end evidence pipeline:

```text
48 Peer-Reviewed Research Papers (2020–2026)
                  │
                  ▼
   Research-Knowledge-Base (Extracted Evidence)
                  │
                  ▼
     Cross-Paper Synthesis & Taxonomy (Phase 02)
                  │
                  ▼
  Formal Research Gap Formulation (Phase 03)
                  │
                  ▼
┌────────────────────────────────────────────────────────┐
│             RESEARCH EVIDENCE (Phase 04)               │
│                                                        │
│  • 22-Dimensional SPV Features ──► Literature Papers  │
│  • Algorithmic Selection ───────► Empirical Baselines  │
│  • System Modules ──────────────► Addressed Gaps       │
│  • Architectural Decisions ─────► Validity Threats     │
└────────────────────────────────────────────────────────┘
                  │
                  ▼
      PRIE Architecture & 22-D SPV Space (Phase 05)
                  │
                  ▼
         Formal Empirical Methodology (Phase 06)
                  │
                  ▼
  Experimental Benchmarking & Ablation (Phase 08)
                  │
                  ▼
   Quantitative Results & SHAP Explanations (Phase 09)
                  │
                  ▼
       Publication & Peer-Review Audits (Phases 10–12)
```

---

## 3. Repository Directory Structure

The repository is structured into twelve sequentially aligned research phases:

```text
PRIE-Research/
│
├── README.md                      # High-level research orientation & evidence map
├── ROADMAP.md                     # Research progress, deliverables & status tracking
├── TODO.md                        # Actionable research agenda & task tracking
├── CHANGELOG.md                   # Chronological versioning of research assets
├── LICENSE                        # Academic open-source license (MIT)
│
├── 01_Research_Foundation/        # 48 literature papers, BibTeX records & knowledge base
│   ├── Papers/                    # Consolidated references.bib & individual .bib files
│   └── Research-Knowledge-Base/   # Thematic paper records across 10 functional domains
│
├── 02_Cross_Analysis/             # Systematic cross-paper syntheses & comparative matrices
├── 03_Research_Problem/           # Problem statement, research questions (RQs) & hypotheses
├── 04_Research_Evidence/          # 22-feature traceability, algorithm & module justification
├── 05_PRIE_Architecture/          # Multi-tier system design, 22-D SPV schema & SVG diagrams
├── 06_Methodology/                # Data design, SMOTE, TreeSHAP & evaluation protocols
├── 07_Implementation/             # Preserved Colab notebook, source modules & model weights
├── 08_Experiments/                # Pre-registered experimental designs, baselines & ablations
├── 09_Results/                    # Quantitative accuracy, ROC, SHAP & benchmark comparisons
├── 10_Publication/                # IEEE conference paper LaTeX manuscript & presentation deck
├── 11_Review/                     # Simulated Reviewer 1-3 reports & IEEE/plagiarism checklists
└── 12_Submission/                 # Target conference list, cover letter & submission history
```

---

## 4. Current Research Status

As established in [`ROADMAP.md`](ROADMAP.md):

| Research Phase | Focus | Status |
|---|---|:---:|
| **Phase 01 — Research Foundation** | 48 Literature Papers, BibTeX, Knowledge Base | **DONE** |
| **Phase 02 — Cross-Paper Analysis** | Comparative Synthesis & Matrices | **NOT STARTED** |
| **Phase 03 — Research Problem** | RQs, Hypotheses & Theoretical Framework | **NOT STARTED** |
| **Phase 04 — Research Evidence** | 22-D SPV Traceability & Algorithm Rationale | **NOT STARTED** |
| **Phase 05 — PRIE Architecture** | 22-D SPV Schema, System Architecture & SVG Diagrams | **EXISTING / VALIDATE** |
| **Phase 06 — Methodology** | Sampling, SMOTE, Optimization & TreeSHAP | **NOT STARTED** |
| **Phase 07 — Implementation** | Python Modules, Serialized XGBoost & Colab Notebook | **EXISTING / VALIDATE** |
| **Phase 08 — Experiments** | Cross-Validation, Baseline Benchmarks & Ablation | **NOT STARTED** |
| **Phase 09 — Results** | Test Metrics (87.8% Acc, 0.941 AUC), SHAP, Figures | **EXISTING / VALIDATE** |
| **Phase 10 — Publication** | IEEE LaTeX Manuscript & Supplementary Materials | **NOT STARTED** |
| **Phase 11 — Review** | Simulated Peer Reviews & Integrity Checklists | **NOT STARTED** |
| **Phase 12 — Submission** | Target Venue Tracking & Submission Readiness | **NOT STARTED** |

---

## 5. Reproducibility & Research Integrity

All reported experimental results adhere strictly to the following scientific integrity principles:
1. **Zero Fabrication**: No synthetic metrics, fictitious author citations, or phantom DOIs.
2. **Empirical Grounding**: Model performance is established on a verified 1,200-student benchmark cohort with 5-fold stratified cross-validation and a 15% held-out test split (XGBoost test accuracy: 87.8%, AUC-ROC: 0.941, Mean Calibration Error: 0.025).
3. **Explicit Uncertainty**: Features or algorithms lacking direct primary paper validation are explicitly annotated as *"Literature support not yet established"* or *"Requires validation"*.

To reproduce the primary machine learning results:
```bash
# Navigate to implementation directory
cd 07_Implementation

# Install pinned scientific dependencies
pip install -r requirements.txt

# Inspect the reproducible research notebook
jupyter notebook notebooks/ScholarCamp_PRIE_Google_Colab.ipynb
```
