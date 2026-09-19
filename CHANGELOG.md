# Changelog — PRIE Research Repository

All notable changes, version updates, and academic asset additions to the PRIE research repository are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), adhering to academic versioning standards.

---

## [0.1.0] - 2026-09-11

### Added
- **Repository Architecture**: Initialized 12-phase research repository structure (`01_Research_Foundation` through `12_Submission`).
- **Research Foundation**:
  - Consolidated `References.bib` containing all 48 peer-reviewed citations from the literature survey.
  - Generated 48 individual BibTeX files in `01_Research_Foundation/Papers/BibTeX/`.
  - Mirrored comprehensive `Research-Knowledge-Base` containing 10 functional domain folders and 9 cross-paper synthesis documents.
- **Implementation Assets**:
  - Preserved `ScholarCamp_PRIE_Google_Colab.ipynb` prototype in `07_Implementation/notebooks/`.
  - Preserved production model artifacts (`xgb_model.pkl`, `scaler.pkl`, `feature_names.json`, `jd_embeddings.npy`, `jd_metadata.json`) in `07_Implementation/models/`.
  - Linked source code modules in `07_Implementation/src/` and pinned dependencies in `requirements.txt`.
- **Governance & Planning**:
  - Established root `README.md`, `ROADMAP.md`, `TODO.md`, `CHANGELOG.md`, and academic `LICENSE`.
  - Formalized research integrity gate: zero hallucinated citations, strict verification of 22-dimensional Student Profile Vector (SPV) features.
