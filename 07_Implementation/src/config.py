"""
ScholarCamp - Placement Readiness Intelligence Engine (PRIE)
Global Application Configuration & Architectural Constants

Centralizes file system paths, persistence endpoints, mathematical weights,
interpretation tiers, feature taxonomies, and environment credentials.
"""

from __future__ import annotations

import logging
import os
import sys
from pathlib import Path
from typing import Dict, List, Tuple

# Load environment variables from local .env file if available
try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

# =============================================================================
# 1. Base Paths & Directory Layout
# =============================================================================
BASE_DIR: Path = Path(__file__).resolve().parent

# Database Persistence Path
DATABASE_PATH: Path = BASE_DIR / "prie_database.db"
DATABASE_URL: str = os.getenv(
    "DATABASE_URL", f"sqlite:///{DATABASE_PATH.as_posix()}"
)
DB_TIMEOUT: int = int(os.getenv("DB_TIMEOUT", "30"))

# File Storage & Uploads
UPLOAD_DIR: Path = BASE_DIR / "uploads" / "resumes"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
AUDIO_UPLOAD_DIR: Path = BASE_DIR / "uploads" / "audio"
AUDIO_UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
MAX_UPLOAD_SIZE_MB: int = int(os.getenv("MAX_UPLOAD_SIZE_MB", "5"))
MAX_UPLOAD_SIZE_BYTES: int = (
    MAX_UPLOAD_SIZE_MB * 1024 * 1024
)  # 5,242,880 Bytes

# Serialized Machine Learning Artifacts
MODELS_DIR: Path = BASE_DIR / "models"
MODELS_DIR.mkdir(parents=True, exist_ok=True)
XGB_MODEL_PATH: Path = MODELS_DIR / "xgb_model.pkl"
SCALER_PATH: Path = MODELS_DIR / "scaler.pkl"
FEATURE_NAMES_PATH: Path = MODELS_DIR / "feature_names.json"
JD_EMBEDDINGS_PATH: Path = MODELS_DIR / "jd_embeddings.npy"
JD_METADATA_PATH: Path = MODELS_DIR / "jd_metadata.json"
SENTENCE_TRANSFORMER_MODEL: str = os.getenv(
    "SENTENCE_TRANSFORMER_MODEL", "all-MiniLM-L6-v2"
)

# Static Reference Data & Taxonomies
DATA_DIR: Path = BASE_DIR / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)
SKILL_TAXONOMY_PATH: Path = DATA_DIR / "skill_taxonomy.json"
COMPANIES_PATH: Path = DATA_DIR / "companies.json"
QUESTION_BANK_PATH: Path = DATA_DIR / "question_bank.json"
RESOURCE_LIBRARY_PATH: Path = DATA_DIR / "resource_library.json"
INTERVIEW_SCENARIOS_PATH: Path = DATA_DIR / "interview_scenarios.json"

# Mock Interview Prosody & Speech Configuration
WHISPER_MODEL_SIZE: str = os.getenv("WHISPER_MODEL_SIZE", "base")
TEMPO_MIN_OPTIMAL: float = 100.0
TEMPO_MAX_OPTIMAL: float = 165.0
HESITATION_MAX_OPTIMAL: float = 0.20
FILLER_DENSITY_MAX_OPTIMAL: float = 0.05
# Roadmap & Recommendation Configuration
ROADMAP_WEEKS: int = int(os.getenv("ROADMAP_WEEKS", "8"))
MAX_TOPICS_PER_WEEK: int = int(os.getenv("MAX_TOPICS_PER_WEEK", "2"))
RECOMMENDATION_TOP_N: int = int(os.getenv("RECOMMENDATION_TOP_N", "5"))
LEARNING_STYLE_BOOST: float = float(os.getenv("LEARNING_STYLE_BOOST", "1.20"))
REVIEW_WEEKS: List[int] = [4, 8]

# =============================================================================
# 2. Application Runtime & Security
# =============================================================================
APP_ENV: str = os.getenv("APP_ENV", "development").lower()
APP_DEBUG: bool = os.getenv("APP_DEBUG", "True").lower() in (
    "true",
    "1",
    "yes",
)
PORT: int = int(os.getenv("PORT", "8501"))
SECRET_KEY: str = os.getenv(
    "SECRET_KEY", "scholarcamp-super-secret-key-32-bytes-minimum!"
)
GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")

# Bcrypt salt rounds
BCRYPT_ROUNDS: int = 12

# =============================================================================
# 3. Placement Readiness Score (PRS) Mathematical Weights
# Formula: PRS = sum(w_i * S_i) where sum(w_i) == 1.00
# =============================================================================
PRS_WEIGHTS: Dict[str, float] = {
    "w_pred": 0.25,        # S_pred: XGBoost calibrated probability
    "w_skill": 0.20,       # S_skill: Skill taxonomy coverage
    "w_resume": 0.15,      # S_resume: ATS match & SBERT cosine
    "w_behavior": 0.15,    # S_behavior: Learning velocity & activity
    "w_consistency": 0.10,  # S_consistency: Weekly session streak
    "w_company": 0.10,     # S_company: Target company alignment
    "w_assessment": 0.05,  # S_assessment: Adaptive quiz accuracy
}

# Verify weights sum exactly to 1.0 (with floating-point tolerance)
_WEIGHT_SUM: float = sum(PRS_WEIGHTS.values())
if abs(_WEIGHT_SUM - 1.0) > 1e-6:
    raise ValueError(
        f"CRITICAL CONFIG ERROR: PRS_WEIGHTS must sum to 1.00, "
        f"got {_WEIGHT_SUM:.4f}"
    )

# =============================================================================
# 4. Placement Readiness Score (PRS) Categorical Tiers
# =============================================================================
PRS_TIERS: Dict[str, Tuple[int, int]] = {
    "Critical": (0, 30),
    "Low": (30, 50),
    "Moderate": (50, 65),
    "Good": (65, 80),
    "High": (80, 90),
    "Excellent": (90, 100),
}

# Adaptive Roadmap Refresh Sensitivity
# Trigger complete weekly schedule re-generation if skill gap changes by > 15%
GAP_DELTA_THRESHOLD: float = float(os.getenv("GAP_DELTA_THRESHOLD", "0.15"))

# =============================================================================
# 5. 22-Dimensional Student Profile Vector (SPV) Canonical Feature Names
# =============================================================================
FEATURE_NAMES: List[str] = [
    "cgpa",
    "backlogs",
    "internship_months",
    "skill_count",
    "certification_count",
    "project_count",
    "aptitude_score",
    "dsa_score",
    "dbms_score",
    "cn_score",
    "programming_score",
    "resume_ats_score",
    "cosine_similarity",
    "gap_score",
    "consistency_score",
    "has_internship",
    "branch_encoded",
    "target_role_encoded",
    "assessment_attempts",
    "behavior_score",
    "engagement_score",
    "roadmap_completion_rate",
]

# Total feature dimensionality
SPV_DIMENSION: int = len(FEATURE_NAMES)
assert SPV_DIMENSION == 22, (
    f"SPV must have exactly 22 dimensions, got {SPV_DIMENSION}"
)

# Bootstrap Confidence Interval Configuration
BOOTSTRAP_ITERATIONS: int = int(os.getenv("BOOTSTRAP_ITERATIONS", "200"))
BOOTSTRAP_NOISE_STD: float = float(os.getenv("BOOTSTRAP_NOISE_STD", "0.05"))


# =============================================================================
# 6. Global Logging Configuration
# =============================================================================
def setup_logging(level: int = logging.INFO) -> logging.Logger:
    """Configures structured logging for ScholarCamp PRIE modules."""
    log_format = "%(asctime)s [%(levelname)s] [%(name)s]: %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"

    logging.basicConfig(
        level=level,
        format=log_format,
        datefmt=date_format,
        handlers=[logging.StreamHandler(sys.stdout)],
    )
    logger_instance = logging.getLogger("PRIE")
    return logger_instance


logger = setup_logging(logging.DEBUG if APP_DEBUG else logging.INFO)
