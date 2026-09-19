# Experiment Configuration: Machine-Readable Schemas & Manifest Specifications

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/Experiment_Configuration.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative Experiment Configuration Specification  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. Declarative Experiment Manifest Architecture

To decouple scientific experimental parameters from software implementation code, all experiments (`EXP-1` to `EXP-6`) are orchestrated via declarative, machine-readable JSON/YAML configuration manifests.

```json
{
  "experiment_manifest_schema_version": "1.0.0",
  "experiment_id": "EXP-1",
  "title": "Multimodal Spatial Layout Intelligence vs Flat-Text Resume Parsing",
  "linked_research_question": "RQ1",
  "linked_hypothesis": "H1",
  "dataset": {
    "dataset_id": "DS-CORPUS-01",
    "split_strategy": "GroupKFold",
    "group_column": "author_uuid",
    "k_folds": 5,
    "test_split_ratio": 0.10
  },
  "model_under_test": {
    "model_id": "LayoutLMv3-Spatial-Base",
    "pretrained_weights": "microsoft/layoutlmv3-base",
    "input_modalities": ["tokens", "bounding_boxes", "image_patches"],
    "max_sequence_length": 512,
    "batch_size": 16,
    "optimizer": "AdamW",
    "learning_rate": 2e-5,
    "epochs": 15
  },
  "comparative_baselines": [
    {"baseline_id": "BL1.1", "name": "Regex-Rule-Based"},
    {"baseline_id": "BL1.2", "name": "spaCy-Trf-NER"},
    {"baseline_id": "BL1.3", "name": "BERT-Base-Flat-Text"}
  ],
  "evaluation_metrics": [
    {"metric": "Boundary-F1", "target_threshold": 0.85},
    {"metric": "Token-Precision", "target_threshold": 0.88},
    {"metric": "Token-Recall", "target_threshold": 0.82}
  ],
  "statistical_test": {
    "test_name": "Wilcoxon Signed-Rank Test",
    "alpha": 0.01,
    "alternative": "greater"
  },
  "reproducibility": {
    "random_seed": 42,
    "deterministic_cuda": true
  }
}
```

---

## 2. Master Experiment Configuration Roster

Declarative execution schemas are authored for each core experiment:
- `configs/exp1_spatial_ats.json`: Vision-language spatial parsing vs flat text (`EXP-1`).
- `configs/exp2_interview_latency.json`: Sub-1.5s speech turnaround & human recruiter panel scoring (`EXP-2`).
- `configs/exp3_tft_forecasting.json`: Longitudinal multi-horizon sequence modeling vs static snapshots (`EXP-3`).
- `configs/exp4_dice_recourse.json`: Actionable counterfactuals vs descriptive TreeSHAP (`EXP-4`).
- `configs/exp5_causal_aqg.json`: Psychometric item discrimination & distractor plausibility (`EXP-5`).
- `configs/exp6_digital_twin.json`: Institutional placement conversion uplift (`EXP-6`, Onboarding schema).
