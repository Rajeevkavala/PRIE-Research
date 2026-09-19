"""
Unit tests for SPV schema & invariant dimensionality (v1).
"""

import sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from spv_version import SPV_VERSION, SPV_DIMENSION, SPV_FEATURES, SPV_FEATURE_NAMES, IMMUTABLE_FEATURES


def test_spv_dimension():
    """Verify invariant 22-dimensional specification."""
    assert SPV_DIMENSION == 22
    assert len(SPV_FEATURES) == 22
    assert len(SPV_FEATURE_NAMES) == 22


def test_spv_version():
    """Verify version protocol tag."""
    assert SPV_VERSION == "v1"


def test_immutable_features():
    """Verify ethical constraint locking F17 branch_encoded."""
    assert "branch_encoded" in IMMUTABLE_FEATURES


def test_feature_ids_sequential():
    """Verify F01 through F22 sequential IDs."""
    for idx, f in enumerate(SPV_FEATURES, start=1):
        expected_id = f"F{idx:02d}"
        assert f.id == expected_id, f"Expected {expected_id}, got {f.id}"
