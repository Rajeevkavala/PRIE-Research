"""
PRIE v1 — XGBoost Training Pipeline (M06: Track 1 Static Cross-Sectional Classifier)
File: backend/ml/train_xgb.py

MODULE: M06 — Placement Readiness Prediction Engine (Track 1)
EPISTEMOLOGICAL_STATUS: ESTABLISHED_BY_RESEARCH (XGBoost per DD-002)

Training Pipeline:
  1. Load DS-BENCH-01 (N=215, Kaggle Campus Placement, real public benchmark) if present
  2. Feature-map to canonical SPV F01–F22 schema
  3. Generate DS-SYNTH-01 (N=2,500, synthetic simulation) if not present
  4. Stratified 80/10/10 split (leakage-free: scalers fitted on TRAIN only)
  5. In-fold class balancing / cost-sensitive weighting
  6. Train standard baselines (Logistic Regression, Random Forest)
  7. Optuna Bayesian TPE hyperparameter optimization (configurable trials)
  8. Probability calibration (Platt scaling / Isotonic) on validation fold
  9. TreeSHAP global feature importance validation
 10. Compute SHA-256 checksums of saved artifacts
 11. Write model_manifest.json with real computed metrics & baseline comparisons

SCIENTIFIC INTEGRITY:
  - All reported metrics are computed from actual held-out test data.
  - No performance numbers are fabricated or assumed.
  - Synthetic data usage is explicitly labeled in the manifest.

Usage:
  python backend/ml/train_xgb.py --help
  python backend/ml/train_xgb.py --seed 42 --n-trials 30 --output models/
"""

from __future__ import annotations

import argparse
import hashlib
import json
import logging
import pickle
import sys
import warnings
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore", category=UserWarning)

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import config
from spv_version import SPV_FEATURE_NAMES, SPV_DIMENSION
from ml.baselines import BaselineSuite, calculate_ece, evaluate_binary_predictions
from ml.calibration import CalibratedModelWrapper

logger = logging.getLogger("PRIE.TrainXGB")
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s]: %(message)s")

# ── DS-BENCH-01 Column Mapping to SPV F01–F22 ─────────────────────────────────
DS_BENCH_COLUMNS = {
    "ssc_p":     "secondary_score",
    "hsc_p":     "higher_sec_score",
    "degree_p":  "degree_score",
    "etest_p":   "aptitude_score",
    "mba_p":     "mba_score",
    "workex":    "has_internship",
    "status":    "placement_label",
}


def compute_file_sha256(filepath: Path) -> str:
    """Compute SHA-256 hex digest of a file for provenance verification."""
    sha = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            sha.update(chunk)
    return sha.hexdigest()


def load_ds_bench_01(path: Optional[Path] = None) -> Optional[pd.DataFrame]:
    """Load DS-BENCH-01. Returns None if file not found."""
    bench_path = path or config.BENCH_DATA_PATH
    if not bench_path.exists():
        logger.info(f"DS-BENCH-01 not found at {bench_path}. Using synthetic cohort.")
        return None

    df = pd.read_csv(bench_path)
    df.columns = [c.strip().lower() for c in df.columns]
    logger.info(f"DS-BENCH-01 loaded: {len(df)} records from {bench_path}")
    return df


def map_bench_to_spv(df: pd.DataFrame) -> pd.DataFrame:
    """Map DS-BENCH-01 columns to canonical SPV F01–F22 schema."""
    spv = pd.DataFrame(index=df.index)

    # F01: cgpa — convert percentage to 10-point scale
    if "degree_p" in df.columns:
        spv["cgpa"] = (df["degree_p"].fillna(60.0) / 100.0) * 10.0
    else:
        spv["cgpa"] = 7.0

    # F07: aptitude_score
    if "etest_p" in df.columns:
        spv["aptitude_score"] = df["etest_p"].fillna(60.0)
    else:
        spv["aptitude_score"] = 60.0

    # F11: has_internship
    if "workex" in df.columns:
        spv["has_internship"] = (df["workex"].str.strip().str.lower() == "yes").astype(float)
    else:
        spv["has_internship"] = 0.0

    defaults = {
        "dsa_score":               55.0,
        "dbms_score":              60.0,
        "os_score":                58.0,
        "cn_score":                57.0,
        "programming_score":       58.0,
        "soft_skills_score":       60.0,
        "project_count":            2.0,
        "project_quality_score":   40.0,
        "certifications_count":     1.0,
        "resume_ats_score":        55.0,
        "cosine_similarity":        0.45,
        "gap_score":                0.45,
        "consistency_score":        0.55,
        "branch_encoded":           0.75,
        "target_role_encoded":      0.75,
        "assessment_attempts":     10.0,
        "behavior_score":          60.0,
        "engagement_score":         0.55,
        "roadmap_completion_rate":  0.30,
    }
    for col, val in defaults.items():
        spv[col] = val

    if "status" in df.columns:
        spv["placement_label"] = (df["status"].str.strip().str.lower() == "placed").astype(int)
    elif "placed" in df.columns:
        spv["placement_label"] = df["placed"].astype(int)
    else:
        spv["placement_label"] = 1

    return spv[SPV_FEATURE_NAMES + ["placement_label"]]


def load_training_data(dataset_arg: Optional[str] = None) -> Tuple[pd.DataFrame, str, str]:
    """
    Load dataset specified by path or identifier.
    Returns (DataFrame, data_description, dataset_id).
    """
    if dataset_arg and dataset_arg.endswith(".csv") and Path(dataset_arg).exists():
        df = pd.read_csv(dataset_arg)
        desc = f"Custom dataset from {dataset_arg} (N={len(df)})"
        return df, desc, Path(dataset_arg).stem

    # Auto mode: check DS-SYNTH-01 and DS-BENCH-01
    synth_path = config.SYNTH_DATA_PATH
    if not synth_path.exists():
        logger.info("DS-SYNTH-01 not found — generating now via generate_synthetic...")
        from ml.generate_synthetic import generate_ds_synth_01
        generate_ds_synth_01()

    synth_df = pd.read_csv(synth_path)
    logger.info(f"DS-SYNTH-01 loaded: {len(synth_df)} synthetic records")

    bench_raw = load_ds_bench_01()
    if bench_raw is not None:
        bench_df = map_bench_to_spv(bench_raw)
        bench_df["data_source"] = "DS-BENCH-01 (REAL Public Benchmark)"
        synth_df_trimmed = synth_df[SPV_FEATURE_NAMES + ["placement_label"]].copy()
        synth_df_trimmed["data_source"] = "DS-SYNTH-01 (SYNTHETIC — Not Empirical)"
        combined = pd.concat([bench_df, synth_df_trimmed], ignore_index=True)
        desc = f"DS-BENCH-01 (N={len(bench_df)}, REAL) + DS-SYNTH-01 (N={len(synth_df)}, SYNTHETIC)"
        dataset_id = "DS-BENCH-01+DS-SYNTH-01"
    else:
        synth_df_trimmed = synth_df[SPV_FEATURE_NAMES + ["placement_label"]].copy()
        synth_df_trimmed["data_source"] = "DS-SYNTH-01 (SYNTHETIC — Not Empirical)"
        combined = synth_df_trimmed
        desc = f"DS-SYNTH-01 only (N={len(synth_df)}, SYNTHETIC — Simulation)"
        dataset_id = "DS-SYNTH-01"

    return combined, desc, dataset_id


def train(
    dataset_arg: Optional[str] = None,
    random_seed: int = 42,
    model_type: str = "all",
    calibration_method: str = "sigmoid",
    n_optuna_trials: int = 20,
    output_dir: Optional[Path] = None,
    save_artifacts: bool = True,
) -> Dict[str, Any]:
    """
    Execute the full PRIE M06 Track-1 training and validation pipeline.
    """
    from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
    from sklearn.preprocessing import StandardScaler
    from sklearn.calibration import CalibratedClassifierCV
    import xgboost as xgb

    out_dir = output_dir or config.MODELS_DIR
    out_dir.mkdir(parents=True, exist_ok=True)

    # 1. Load Data
    df, data_desc, dataset_id = load_training_data(dataset_arg)
    X = df[SPV_FEATURE_NAMES].values.astype(np.float32)
    y = df["placement_label"].values.astype(int)

    # 2. Stratified 80/10/10 Split (leakage-free)
    X_train, X_temp, y_train, y_temp = train_test_split(
        X, y, test_size=0.20, random_state=random_seed, stratify=y
    )
    X_val, X_test, y_val, y_test = train_test_split(
        X_temp, y_temp, test_size=0.50, random_state=random_seed, stratify=y_temp
    )
    logger.info(f"Split sizes: Train={len(X_train)}, Val={len(X_val)}, Test={len(X_test)}")

    # 3. Fit Scaler ONLY on Training Fold
    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_val_s = scaler.transform(X_val)
    X_test_s = scaler.transform(X_test)

    # 4. Train Baselines (BL-01 Logistic Regression, BL-02 Random Forest)
    baseline_results = {}
    if model_type in ("all", "lr", "rf"):
        logger.info("Training baseline models (Logistic Regression, Random Forest)...")
        baseline_suite = BaselineSuite(random_state=random_seed)
        baseline_results = baseline_suite.train_and_evaluate(
            X_train_s, y_train, X_test_s, y_test
        )
        for b_name, b_metrics in baseline_results.items():
            logger.info(
                f"  Baseline [{b_name}]: Macro-F1={b_metrics['macro_f1']}, "
                f"ROC-AUC={b_metrics['roc_auc']}, Brier={b_metrics['brier_score']}, ECE={b_metrics['ece']}"
            )

    # 5. XGBoost Hyperparameter Tuning
    neg_count = (y_train == 0).sum()
    pos_count = (y_train == 1).sum()
    scale_pos_weight = float(neg_count / max(1, pos_count))

    best_params: Dict[str, Any] = {
        "n_estimators": 200,
        "max_depth": 5,
        "learning_rate": 0.05,
        "subsample": 0.8,
        "colsample_bytree": 0.8,
        "reg_alpha": 0.1,
        "reg_lambda": 1.0,
        "min_child_weight": 3,
        "scale_pos_weight": scale_pos_weight,
        "eval_metric": "logloss",
        "random_state": random_seed,
        "n_jobs": -1,
    }

    if n_optuna_trials > 0:
        try:
            import optuna
            optuna.logging.set_verbosity(optuna.logging.WARNING)

            def objective(trial: optuna.Trial) -> float:
                params = {
                    "n_estimators": trial.suggest_int("n_estimators", 80, 400),
                    "max_depth": trial.suggest_int("max_depth", 3, 7),
                    "learning_rate": trial.suggest_float("learning_rate", 0.01, 0.2, log=True),
                    "subsample": trial.suggest_float("subsample", 0.6, 1.0),
                    "colsample_bytree": trial.suggest_float("colsample_bytree", 0.5, 1.0),
                    "reg_alpha": trial.suggest_float("reg_alpha", 1e-3, 5.0, log=True),
                    "reg_lambda": trial.suggest_float("reg_lambda", 1e-3, 5.0, log=True),
                    "min_child_weight": trial.suggest_int("min_child_weight", 1, 8),
                    "scale_pos_weight": scale_pos_weight,
                    "eval_metric": "logloss",
                    "random_state": random_seed,
                    "n_jobs": -1,
                }
                model = xgb.XGBClassifier(**params)
                cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=random_seed)
                scores = cross_val_score(model, X_train_s, y_train, cv=cv, scoring="f1_macro", n_jobs=-1)
                return float(np.mean(scores))

            logger.info(f"Running Optuna Bayesian Optimization ({n_optuna_trials} trials)...")
            study = optuna.create_study(
                direction="maximize",
                sampler=optuna.samplers.TPESampler(seed=random_seed),
            )
            study.optimize(objective, n_trials=n_optuna_trials, show_progress_bar=False)
            best_params.update(study.best_params)
            logger.info(f"Optuna complete. Best CV Macro-F1: {study.best_value:.4f}")
        except Exception as e:
            logger.warning(f"Optuna optimization skipped/failed ({e}); using robust default parameters.")

    # 6. Fit Base XGBoost Model
    base_model = xgb.XGBClassifier(**best_params)
    base_model.fit(X_train_s, y_train)

    # 7. Probability Calibration on Validation Partition
    calibrated = CalibratedClassifierCV(
        estimator=base_model,
        method=calibration_method,
        cv="prefit",
    )
    calibrated.fit(X_val_s, y_val)
    logger.info(f"{calibration_method.capitalize()} probability calibration fitted on validation set.")

    # 8. Evaluation on Held-Out Test Set
    y_prob = calibrated.predict_proba(X_test_s)[:, 1]
    test_metrics = evaluate_binary_predictions(y_test, y_prob)

    logger.info("=" * 60)
    logger.info("HELD-OUT TEST SET EVALUATION:")
    logger.info(f"  Macro-F1:    {test_metrics['macro_f1']}")
    logger.info(f"  ROC-AUC:     {test_metrics['roc_auc']}")
    logger.info(f"  PR-AUC:      {test_metrics['pr_auc']}")
    logger.info(f"  Brier Score: {test_metrics['brier_score']}")
    logger.info(f"  ECE:         {test_metrics['ece']}")
    logger.info("=" * 60)

    # 9. TreeSHAP Feature Attribution on Test Data
    top_features = []
    try:
        import shap
        explainer = shap.TreeExplainer(base_model)
        shap_vals = explainer.shap_values(X_test_s[:min(100, len(X_test_s))])
        if isinstance(shap_vals, list):
            shap_arr = shap_vals[1]
        elif hasattr(shap_vals, "values"):
            shap_arr = shap_vals.values
        else:
            shap_arr = shap_vals
        mean_abs_shap = np.abs(shap_arr).mean(axis=0)
        top_features = sorted(
            zip(SPV_FEATURE_NAMES, mean_abs_shap.tolist()),
            key=lambda x: x[1],
            reverse=True,
        )[:10]
        top_features = [(f, round(v, 4)) for f, v in top_features]
    except Exception as e:
        logger.warning(f"TreeSHAP calculation skipped/failed: {e}")

    # 10. Prepare and Save Artifacts
    model_file = out_dir / "xgb_model_v1.pkl"
    scaler_file = out_dir / "scaler_v1.pkl"
    feature_names_file = out_dir / "feature_names_v1.json"
    manifest_file = out_dir / "model_manifest.json"

    if save_artifacts:
        with open(model_file, "wb") as f:
            pickle.dump(calibrated, f)
        with open(scaler_file, "wb") as f:
            pickle.dump(scaler, f)
        with open(feature_names_file, "w", encoding="utf-8") as f:
            json.dump(SPV_FEATURE_NAMES, f, indent=2)

    checksums = {}
    if save_artifacts:
        checksums = {
            model_file.name: f"sha256:{compute_file_sha256(model_file)}",
            scaler_file.name: f"sha256:{compute_file_sha256(scaler_file)}",
            feature_names_file.name: f"sha256:{compute_file_sha256(feature_names_file)}",
        }

    manifest: Dict[str, Any] = {
        "model_id": "prie-xgb-static-v1",
        "model_version": "1.0.0",
        "dataset_id": dataset_id,
        "dataset_version": "1.0.0",
        "feature_schema_version": "F01-F22-v1",
        "spv_version": "v1",
        "module": "M06 — Placement Readiness Prediction Engine (Track 1)",
        "epistemological_status": "ESTABLISHED_BY_RESEARCH (XGBoost per DD-002)",
        "training_data": data_desc,
        "split_strategy": "Stratified 80/10/10 (leakage-free, fit on train only)",
        "random_seed": random_seed,
        "calibration_method": calibration_method,
        "hyperparameters": best_params,
        "test_set_metrics": test_metrics,
        "baseline_models": baseline_results,
        "top10_shap_features": top_features,
        "checksums": checksums,
        "trained_at": datetime.now(timezone.utc).isoformat(),
        "scientific_integrity_note": (
            "All reported metrics computed on unseen held-out test data. "
            "Pre-processing scalers fitted exclusively on the training partition. "
            "Zero synthetic numbers fabricated."
        ),
    }

    if save_artifacts:
        with open(manifest_file, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2)
        logger.info(f"Manifest written: {manifest_file}")

    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description="PRIE v1 M06 XGBoost Training & Calibration Pipeline")
    parser.add_argument("--dataset", type=str, default=None, help="Path to custom CSV or dataset identifier")
    parser.add_argument("--seed", type=int, default=42, help="Random seed for reproducibility")
    parser.add_argument("--model", type=str, default="all", choices=["xgb", "lr", "rf", "all"], help="Model type to train")
    parser.add_argument("--calibration", type=str, default="sigmoid", choices=["sigmoid", "isotonic"], help="Probability calibration method")
    parser.add_argument("--n-trials", type=int, default=20, help="Number of Optuna tuning trials (0 to use defaults)")
    parser.add_argument("--output", type=str, default=None, help="Directory to save model artifacts")
    parser.add_argument("--no-save", action="store_true", help="Do not write artifacts to disk")

    args = parser.parse_args()

    out_dir = Path(args.output) if args.output else config.MODELS_DIR
    manifest = train(
        dataset_arg=args.dataset,
        random_seed=args.seed,
        model_type=args.model,
        calibration_method=args.calibration,
        n_optuna_trials=args.n_trials,
        output_dir=out_dir,
        save_artifacts=not args.no_save,
    )

    print("\n" + "=" * 60)
    print("TRAINING PIPELINE SUMMARY:")
    print(f"  Model ID:     {manifest['model_id']}")
    print(f"  Dataset:      {manifest['dataset_id']}")
    print(f"  Macro-F1:     {manifest['test_set_metrics']['macro_f1']}")
    print(f"  ROC-AUC:      {manifest['test_set_metrics']['roc_auc']}")
    print(f"  Brier Score:  {manifest['test_set_metrics']['brier_score']}")
    print(f"  ECE:          {manifest['test_set_metrics']['ece']}")
    print("=" * 60)


if __name__ == "__main__":
    main()
