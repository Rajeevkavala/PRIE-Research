"""
PRIE v1 — Feature Schema (ml/feature_schema.py)
Re-exports canonical SPV definitions from spv_version.py for ML pipeline consistency.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from spv_version import (
    SPV_VERSION,
    SPV_DIMENSION,
    SPV_FEATURES,
    SPV_FEATURE_NAMES,
    SPV_ID_TO_NAME,
    SPV_NAME_TO_ID,
    SPVFeature,
    get_feature,
    get_feature_by_id,
    get_literature_sources,
    get_features_by_status,
)

__all__ = [
    "SPV_VERSION",
    "SPV_DIMENSION",
    "SPV_FEATURES",
    "SPV_FEATURE_NAMES",
    "SPV_ID_TO_NAME",
    "SPV_NAME_TO_ID",
    "SPVFeature",
    "get_feature",
    "get_feature_by_id",
    "get_literature_sources",
    "get_features_by_status",
]
