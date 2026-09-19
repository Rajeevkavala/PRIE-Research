"""
PRIE v1 — Roadmap API Routes
File: backend/api/v1_roadmap.py
"""

from __future__ import annotations
import sys
from pathlib import Path
from typing import Optional
from fastapi import APIRouter, HTTPException, Depends, Body

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from api.v1_auth import get_current_student
from modules.m01_spv_aggregator import SPVAggregator
from modules.m04_skill_gap_engine import SkillGapEngine
from modules.m08_roadmap_generator import RoadmapGenerator
from database import db_manager, queries

router = APIRouter()


@router.get("/active")
def get_roadmap(student_id: int = Depends(get_current_student)):
    """GET /api/v1/roadmap/active — Returns current roadmap milestones."""
    gen = RoadmapGenerator()
    weeks = gen.get_roadmap(student_id)
    return {"weeks": weeks, "total_weeks": len(weeks)}


@router.post("/generate")
def generate_roadmap(student_id: int = Depends(get_current_student)):
    """POST /api/v1/roadmap/generate — Regenerates roadmap from current SPV."""
    try:
        agg = SPVAggregator()
        spv, _, _ = agg.assemble(student_id)

        row = db_manager.dict_row(db_manager.execute_single(queries.GET_STUDENT_BY_ID, (student_id,)))
        target_role    = (row or {}).get("target_role", "Software Development Engineer")
        learning_style = (row or {}).get("learning_style", "practical")

        gap_engine = SkillGapEngine()
        _, deficit_list, _ = gap_engine.compute_gap(spv, target_role)

        gen = RoadmapGenerator()
        # Clear existing roadmap
        db_manager.execute_update(queries.DELETE_STUDENT_ROADMAP, (student_id,))
        weeks = gen.generate(student_id, deficit_list, target_role, learning_style)

        return {"weeks": weeks, "total_weeks": len(weeks), "generated": True}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/complete/{week_number}")
def complete_week(week_number: int, student_id: int = Depends(get_current_student)):
    gen = RoadmapGenerator()
    ok = gen.mark_week_complete(student_id, week_number)
    return {"status": "completed" if ok else "not_found", "week": week_number}
