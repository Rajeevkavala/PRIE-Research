"""
Unit tests for Core Intelligence Modules (M01, M04, M08, M11).
"""

import sys
from pathlib import Path
import pytest
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from database import db_manager, queries
from modules.m01_spv_aggregator import SPVAggregator
from modules.m04_skill_gap_engine import SkillGapEngine
from modules.m08_roadmap_generator import RoadmapGenerator
from modules.m11_behavioral_telemetry import BehavioralTelemetry


def test_m01_spv_assembly():
    """Verify M01 assemblies exactly 22 normalized features within [0, 1]."""
    agg = SPVAggregator()
    student = db_manager.dict_row(db_manager.execute_single(queries.GET_STUDENT_BY_EMAIL, ("demo@scholarcamp.ai",)))
    assert student is not None
    sid = student["student_id"]

    spv, mask, comp = agg.assemble(sid)
    assert len(spv) == 22
    assert len(mask) == 22
    assert comp > 0.0
    # Every normalized feature must be in [0.0, 1.0]
    for val in spv:
        assert 0.0 <= val <= 1.0, f"Normalized feature out of bounds: {val}"


def test_m04_skill_gap():
    """Verify M04 computes weighted Euclidean gap score."""
    agg = SPVAggregator()
    student = db_manager.dict_row(db_manager.execute_single(queries.GET_STUDENT_BY_EMAIL, ("demo@scholarcamp.ai",)))
    sid = student["student_id"]
    spv, _, _ = agg.assemble(sid)

    gap_engine = SkillGapEngine()
    gap_score, deficit_list, deficit_vector = gap_engine.compute_gap(spv, "Software Development Engineer")

    assert 0.0 <= gap_score <= 1.0
    assert len(deficit_vector) == 22
    assert isinstance(deficit_list, list)


def test_m08_roadmap_generation():
    """Verify M08 generates topological DAG milestones."""
    agg = SPVAggregator()
    student = db_manager.dict_row(db_manager.execute_single(queries.GET_STUDENT_BY_EMAIL, ("demo@scholarcamp.ai",)))
    sid = student["student_id"]
    spv, _, _ = agg.assemble(sid)

    gap_engine = SkillGapEngine()
    _, deficit_list, _ = gap_engine.compute_gap(spv, "Software Development Engineer")

    gen = RoadmapGenerator()
    weeks = gen.generate(sid, deficit_list, "Software Development Engineer", "practical")
    assert len(weeks) > 0
    assert weeks[0]["week_number"] == 1


def test_m11_behavioral_telemetry():
    """Verify M11 computes EMA consistency and engagement scores."""
    student = db_manager.dict_row(db_manager.execute_single(queries.GET_STUDENT_BY_EMAIL, ("demo@scholarcamp.ai",)))
    sid = student["student_id"]

    telemetry = BehavioralTelemetry()
    metrics = telemetry.compute_metrics(sid)
    assert "consistency_score" in metrics
    assert "engagement_score" in metrics
    assert 0.0 <= metrics["consistency_score"] <= 1.0
    assert 0.0 <= metrics["engagement_score"] <= 1.0
