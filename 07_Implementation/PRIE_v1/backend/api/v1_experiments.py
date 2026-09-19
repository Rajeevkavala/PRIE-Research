"""
PRIE v1 — REST API: Research Experiments Dashboard & Artifacts
File: backend/api/v1_experiments.py
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from fastapi import APIRouter, HTTPException

import config
from experiments.run_experiment import RESULTS_DIR, run_exp1, run_exp2, run_exp3, run_exp4, run_exp5, run_exp6

router = APIRouter()


@router.get("/list", response_model=List[Dict[str, Any]])
async def list_experiments():
    """List all research experiment protocols and their execution status."""
    protocols = [
        {"id": "EXP-1", "title": "Predictive Calibration & Baseline Comparison", "rq": "RQ1", "hypothesis": "H1", "target": "Brier <= 0.08, ECE <= 0.05"},
        {"id": "EXP-2", "title": "Multimodal Mock Interview Diagnostic Ablation", "rq": "RQ4", "hypothesis": "H4", "target": "Multimodal variance reduction"},
        {"id": "EXP-3", "title": "Prescriptive Recourse Feasibility & Invariance", "rq": "RQ5", "hypothesis": "H3", "target": "k <= 3, 100% F17 lock"},
        {"id": "EXP-4", "title": "Resume ATS Spatial Extraction Ablation", "rq": "RQ2", "hypothesis": "H2", "target": "Spatial token segmentation"},
        {"id": "EXP-5", "title": "Curriculum RAG Retrieval & Grounding Evaluation", "rq": "RQ6", "hypothesis": "H6", "target": "Precision & hallucination rejection"},
        {"id": "EXP-6", "title": "A* Concept DAG Scheduling Optimization", "rq": "RQ3", "hypothesis": "H5", "target": "0% prerequisite violation rate"},
    ]

    for p in protocols:
        res_dir = RESULTS_DIR / p["id"]
        meta_file = res_dir / "run_metadata.json"
        if meta_file.exists():
            try:
                meta = json.loads(meta_file.read_text(encoding="utf-8"))
                p["status"] = "EXECUTED"
                p["last_run"] = meta.get("timestamp")
                p["runtime_seconds"] = meta.get("runtime_seconds")
            except Exception:
                p["status"] = "EXECUTED (Unparsed)"
        else:
            p["status"] = "NOT EXECUTED"

    return protocols


@router.get("/{exp_id}/results", response_model=Dict[str, Any])
async def get_experiment_results(exp_id: str):
    """Retrieve exported artifacts and metrics for a specific experiment."""
    exp_dir = RESULTS_DIR / exp_id.upper()
    if not exp_dir.exists():
        raise HTTPException(status_code=404, detail=f"No execution results found for {exp_id}. Status: NOT EXECUTED.")

    output = {"experiment_id": exp_id.upper()}
    for fname in ["run_metadata.json", "raw_metrics.json", "statistical_tests.json", "paper_table.tex", "summary.csv"]:
        fpath = exp_dir / fname
        if fpath.exists():
            if fname.endswith(".json"):
                output[fname.replace(".json", "")] = json.loads(fpath.read_text(encoding="utf-8"))
            else:
                output[fname.replace(".", "_")] = fpath.read_text(encoding="utf-8")

    return output


@router.post("/{exp_id}/run", response_model=Dict[str, Any])
async def trigger_experiment_run(exp_id: str, seed: int = 42):
    """Trigger programmatic execution of a research experiment protocol."""
    runners = {
        "EXP-1": run_exp1,
        "EXP-2": run_exp2,
        "EXP-3": run_exp3,
        "EXP-4": run_exp4,
        "EXP-5": run_exp5,
        "EXP-6": run_exp6,
    }
    eid = exp_id.upper()
    if eid not in runners:
        raise HTTPException(status_code=400, detail=f"Unknown experiment ID: {exp_id}")

    try:
        res = runners[eid](seed=seed)
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Experiment execution failed: {e}")
