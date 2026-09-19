"""
PRIE — Global Application Configuration
File: config.py

Centralizes all environment-driven settings, file system paths, ML artifact paths,
PRS weight formulas, SPV constants, and logging configuration.

Traceability: 05_PRIE_Architecture/System_Architecture.md (Layer 6)
"""

from __future__ import annotations

import logging
import os
import sys
from pathlib import Path
from typing import Dict, List, Tuple

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# =============================================================================
# 1. Root Directory Layout
# =============================================================================
BASE_DIR: Path = Path(__file__).resolve().parent          # backend/
ROOT_DIR: Path = BASE_DIR.parent                          # PRIE_v1/
FRONTEND_DIR: Path = ROOT_DIR / "frontend"
MODELS_DIR: Path = ROOT_DIR / "models"
DATA_DIR: Path = ROOT_DIR / "data"
UPLOAD_DIR: Path = ROOT_DIR / "uploads" / "resumes"
LOGS_DIR: Path = ROOT_DIR / "logs"

# Ensure directories exist
for _d in [MODELS_DIR, DATA_DIR, UPLOAD_DIR, LOGS_DIR]:
    _d.mkdir(parents=True, exist_ok=True)

# =============================================================================
# 2. Database
# =============================================================================
DATABASE_PATH: Path = ROOT_DIR / "data" / "prie_v1.db"
DATABASE_URL: str = os.getenv("DATABASE_URL", f"sqlite:///{DATABASE_PATH.as_posix()}")
DB_TIMEOUT: int = int(os.getenv("DB_TIMEOUT", "30"))

# =============================================================================
# 3. ML Artifact Paths (Model Registry — CMP-MDL-XGB)
# =============================================================================
XGB_MODEL_PATH: Path = MODELS_DIR / "xgb_model_v1.pkl"
SCALER_PATH: Path = MODELS_DIR / "scaler_v1.pkl"
FEATURE_NAMES_PATH: Path = MODELS_DIR / "feature_names_v1.json"
MODEL_MANIFEST_PATH: Path = MODELS_DIR / "model_manifest.json"
SYNTH_DATA_PATH: Path = DATA_DIR / "ds_synth_01.csv"
BENCH_DATA_PATH: Path = DATA_DIR / "ds_bench_01.csv"

# NLP / Embedding Models
SBERT_MODEL: str = os.getenv("SBERT_MODEL", "all-MiniLM-L6-v2")
WHISPER_MODEL_SIZE: str = os.getenv("WHISPER_MODEL_SIZE", "base")

# =============================================================================
# 4. Reference Data
# =============================================================================
QUESTION_BANK_PATH: Path = DATA_DIR / "question_bank.json"
SKILL_TAXONOMY_PATH: Path = DATA_DIR / "skill_taxonomy.json"
COMPANIES_PATH: Path = DATA_DIR / "companies.json"
CS_DAG_PATH: Path = DATA_DIR / "cs_concept_dag.json"
RESOURCE_LIBRARY_PATH: Path = DATA_DIR / "resource_library.json"

# =============================================================================
# 5. Application Runtime & Execution Modes
# =============================================================================
EXECUTION_MODE: str = os.getenv("EXECUTION_MODE", os.getenv("APP_ENV", "development")).lower()
if EXECUTION_MODE not in ("development", "testing", "research", "production"):
    EXECUTION_MODE = "development"

APP_ENV: str = EXECUTION_MODE
IS_PRODUCTION: bool = EXECUTION_MODE == "production"
IS_RESEARCH_MODE: bool = EXECUTION_MODE in ("research", "production")
APP_DEBUG: bool = os.getenv("APP_DEBUG", "false" if IS_PRODUCTION else "true").lower() in ("true", "1", "yes")

# Gate for fallback dummy models: strictly disallowed in research and production
ALLOW_DUMMY_MODELS: bool = os.getenv(
    "ALLOW_DUMMY_MODELS",
    "true" if EXECUTION_MODE in ("development", "testing") else "false"
).lower() in ("true", "1", "yes")

PORT: int = int(os.getenv("PORT", "8000"))
FRONTEND_PORT: int = int(os.getenv("FRONTEND_PORT", "8080"))

# Secure Secret Management
_DEFAULT_DEV_SECRET = "prie-v1-dev-secret-change-in-production-32b!"
SECRET_KEY: str = os.getenv("SECRET_KEY", "")
if not SECRET_KEY:
    if IS_PRODUCTION:
        raise ValueError("CRITICAL SECURITY ERROR: SECRET_KEY must be explicitly set via environment in production mode!")
    SECRET_KEY = _DEFAULT_DEV_SECRET

JWT_ALGORITHM: str = "HS256"
JWT_EXPIRE_MINUTES: int = int(os.getenv("JWT_EXPIRE_MINUTES", "480"))
BCRYPT_ROUNDS: int = 12

_raw_cors = os.getenv("CORS_ORIGINS", "http://localhost:8080,http://127.0.0.1:8080,http://localhost:8000")
CORS_ORIGINS: List[str] = [origin.strip() for origin in _raw_cors.split(",") if origin.strip()]

# =============================================================================
# 6. PRS Composite Score Weights (sum MUST equal 1.0 — validated below)
# Formula: PRS = Σ(w_i × S_i)
# Derived from: 05_PRIE_Architecture/Module_Architecture.md → M06
# =============================================================================
PRS_WEIGHTS: Dict[str, float] = {
    "w_pred":        0.25,   # S_pred: XGBoost calibrated probability
    "w_skill":       0.20,   # S_skill: Skill coverage composite
    "w_resume":      0.15,   # S_resume: ATS + SBERT cosine
    "w_behavior":    0.15,   # S_behavior: Interview + engagement
    "w_consistency": 0.10,   # S_consistency: Weekly session EMA
    "w_company":     0.10,   # S_company: Target company alignment
    "w_assessment":  0.05,   # S_assessment: Quiz accuracy
}

_weight_sum = round(sum(PRS_WEIGHTS.values()), 10)
assert abs(_weight_sum - 1.0) < 1e-9, (
    f"CRITICAL: PRS_WEIGHTS must sum to 1.0, got {_weight_sum:.6f}"
)

# =============================================================================
# 7. Readiness Tier Thresholds (M06 output → M12 display)
# Derived from: 05_PRIE_Architecture/Module_Architecture.md → M06 Outputs
# =============================================================================
READINESS_TIERS: Dict[str, Tuple[float, float]] = {
    "Ready":             (0.75, 1.01),
    "Needs Remediation": (0.45, 0.75),
    "At-Risk":           (0.00, 0.45),
}

# PRS percentage tiers (for dashboard display)
PRS_TIERS: Dict[str, Tuple[int, int]] = {
    "Excellent": (90, 101),
    "High":      (80,  90),
    "Good":      (65,  80),
    "Moderate":  (50,  65),
    "Low":       (30,  50),
    "Critical":  ( 0,  30),
}

# =============================================================================
# 8. SPV & ML Constants
# =============================================================================
SPV_DIMENSION: int = 22          # Invariant — never change
BOOTSTRAP_ITERATIONS: int = int(os.getenv("BOOTSTRAP_ITERATIONS", "200"))
BOOTSTRAP_NOISE_STD: float = float(os.getenv("BOOTSTRAP_NOISE_STD", "0.05"))
GAP_DELTA_THRESHOLD: float = float(os.getenv("GAP_DELTA_THRESHOLD", "0.15"))

# Behavioral Telemetry EMA alpha (M11)
EMA_ALPHA: float = 0.30   # F16 formula: EMA_t = 0.3 * Active_t + 0.7 * EMA_{t-1}
ENGAGEMENT_LOOKBACK_DAYS: int = 14  # Early-warning window

# Roadmap
ROADMAP_WEEKS: int = int(os.getenv("ROADMAP_WEEKS", "8"))
MAX_TOPICS_PER_WEEK: int = 2

# =============================================================================
# 9. Logging
# =============================================================================
def setup_logging(level: int = logging.INFO) -> logging.Logger:
    fmt = "%(asctime)s [%(levelname)s] [%(name)s]: %(message)s"
    logging.basicConfig(
        level=level,
        format=fmt,
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[logging.StreamHandler(sys.stdout)],
    )
    return logging.getLogger("PRIE")


logger = setup_logging(logging.DEBUG if APP_DEBUG else logging.INFO)
