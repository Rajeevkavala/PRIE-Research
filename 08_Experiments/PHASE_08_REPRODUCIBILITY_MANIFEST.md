# SCHOLARCAMP / PRIE: PHASE 08 REPRODUCIBILITY MANIFEST
**Project**: ScholarCamp  
**Core System**: Placement Readiness Intelligence Engine (PRIE)  
**Phase**: Phase 08 — Experiments  
**Document**: `08_Experiments/PHASE_08_REPRODUCIBILITY_MANIFEST.md`  
**Execution CLI**: `python 07_Implementation/PRIE_v1/experiments/run_experiment.py --experiment all --seed 42`  

---

## 1. Cryptographic Provenance Hashes

| Artifact Identifier | Relative Path | File Type | SHA-256 Hex Digest |
|:---|:---|:---:|:---|
| **Certified XGBoost Model** | `07_Implementation/PRIE_v1/models/xgb_model_v1.pkl` | Binary Pickled Model | `b16b47c0507204481b7e289bf65ce085a62e59e19c36d2eb1fbc44654b9d3ff0` |
| **Certified Scaler** | `07_Implementation/PRIE_v1/models/scaler_v1.pkl` | Binary Pickled Scaler | `ce836ebfa8846386d4e5f73977c05fa965f725a3d76e4c0aa0a7905a8f4c40eb` |
| **Model Manifest** | `07_Implementation/PRIE_v1/models/model_manifest.json` | JSON Specification | `41c03e62f3f98bb77a1649646b9a896677f59d4791338dfa1fc2e96030cff6cf` |
| **Simulation Dataset** | `07_Implementation/PRIE_v1/data/ds_synth_01.csv` | CSV Dataset ($N=2,500$) | `25bc432b0c36215357876a6ce46ee88ba46f7c8ec23f85387d85ea751d8b1e4e` |
| **Relational Database** | `07_Implementation/PRIE_v1/data/prie_v1.db` | SQLite Database | `b63a948483f9859f77f5a543884b6f120760f38b006ee70817eaee2a2b005fe4` |
| **CS Concept DAG** | `07_Implementation/PRIE_v1/data/cs_concept_dag.json` | JSON Graph (38 nodes) | `30a6c07e056d888e99824cbf5e5c707d89aa2e70e9a385f09623e595ef49ca71` |

---

## 2. Deterministic Command Runbook

To reproduce all empirical results exactly:
```bash
# 1. Run all experiments with master deterministic seed 42
python 07_Implementation/PRIE_v1/experiments/run_experiment.py --experiment all --seed 42

# 2. Run multi-seed robustness battery across 5 seeds
python C:/Users/rajee/.gemini/antigravity-ide/brain/7e325bcf-fdd9-4da6-9973-083489b19d1b/scratch/run_multiseed.py

# 3. Generate 300-DPI publication figures and LaTeX tables
python 07_Implementation/notebooks/generate_paper_figures.py
```
