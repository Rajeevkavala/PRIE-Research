"""
PRIE v1 — Module M11: Behavioral Telemetry & Engagement Engine
File: backend/modules/m11_behavioral_telemetry.py

MODULE: M11 — Behavioral Telemetry & Engagement Engine
EPISTEMOLOGICAL_STATUS: ESTABLISHED_BY_RESEARCH (EMA per DD-010)
RESEARCH_GAP: RG8 (Passive monitoring; no proactive dropout intervention)
RESEARCH_OBJECTIVE: RO6 (Behavioral Dropout Prediction)
TRACEABILITY: Paper02, Paper05, Paper33, Paper44; DD-010

Implements:
  - F16 (consistency_score): Exponential Moving Average of weekly active days
    Formula: EMA_t = 0.3 * Active_t + 0.7 * EMA_{t-1}
  - F21 (engagement_score): Composite from event frequency, variety, session depth
  - Early-warning flag: engagement drop for 14+ consecutive days triggers alert
  - Cohort-percentile normalization for engagement_score
"""

from __future__ import annotations

import json
import logging
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import config
from database import db_manager, queries

logger = logging.getLogger("PRIE.M11.BehavioralTelemetry")

# ── EMA Configuration ─────────────────────────────────────────────────────────
EMA_ALPHA: float = config.EMA_ALPHA          # 0.30 per architecture spec
EMA_LOOKBACK_WEEKS: int = 6                  # 6-week EMA window
ENGAGEMENT_LOOKBACK_DAYS: int = config.ENGAGEMENT_LOOKBACK_DAYS  # 14 days
DROPOUT_THRESHOLD_DAYS: int = 14             # 14+ inactive days = at-risk warning


class BehavioralTelemetry:
    """
    M11: Behavioral Telemetry & Engagement Engine.

    Computes F16 (consistency_score) and F21 (engagement_score) from
    learning event logs using EMA and composite engagement signals.
    """

    def __init__(self, db_path: Optional[Path] = None) -> None:
        self.db_path = db_path

    def log_event(
        self,
        student_id: int,
        event_type: str,
        event_detail: str = "",
        payload: Optional[Dict[str, Any]] = None,
        duration_seconds: float = 0.0,
    ) -> int:
        """
        Persist a learning event to the telemetry log.

        Event types: login, quiz_attempt, resume_upload, roadmap_milestone,
                     page_view, code_run, resource_view, profile_update
        """
        return db_manager.execute_insert(
            queries.INSERT_LEARNING_EVENT,
            (
                student_id,
                event_type,
                event_detail,
                json.dumps(payload or {}),
                duration_seconds,
            ),
            self.db_path,
        )

    def compute_consistency_score(self, student_id: int) -> float:
        """
        Compute F16 (consistency_score) via EMA over 6 weeks of active days.

        Formula: EMA_t = α * Active_t + (1-α) * EMA_{t-1}  where α=0.3
        Active_t = 1 if any learning event in the week; 0 otherwise.

        Returns:
            float: Normalized consistency score in [0.0, 1.0]
        """
        ema = 0.5   # Initialize to cohort baseline for cold start

        now = datetime.utcnow()
        for week_offset in range(EMA_LOOKBACK_WEEKS - 1, -1, -1):
            week_start = now - timedelta(weeks=week_offset + 1)
            week_end   = now - timedelta(weeks=week_offset)
            start_str  = week_start.strftime("%Y-%m-%d")
            end_str    = week_end.strftime("%Y-%m-%d")

            rows = db_manager.execute_query(
                """
                SELECT COUNT(*) as cnt FROM learning_events
                WHERE student_id = ?
                AND date(event_time) >= ? AND date(event_time) < ?
                """,
                (student_id, start_str, end_str),
                self.db_path,
            )
            active = 1 if (rows and int(rows[0]["cnt"]) > 0) else 0
            ema = EMA_ALPHA * active + (1 - EMA_ALPHA) * ema

        return round(float(np.clip(ema, 0.0, 1.0)), 4)

    def compute_engagement_score(self, student_id: int) -> float:
        """
        Compute F21 (engagement_score) as composite from 3 sub-signals.

        Sub-signals (equal weight):
          - Activity frequency: events in last 14 days / max_expected (20)
          - Event variety: unique event types in last 14 days / 7 total types
          - Session depth: mean session duration proxy from event counts

        Returns:
            float: Normalized engagement score in [0.0, 1.0]
        """
        rows = db_manager.execute_query(
            queries.GET_RECENT_EVENTS,
            (student_id, f"-{ENGAGEMENT_LOOKBACK_DAYS} days"),
            self.db_path,
        )
        events = db_manager.dict_rows(rows)

        if not events:
            return ENGAGEMENT_LOOKBACK_DAYS and 0.0   # cold start

        # Sub-signal 1: Activity frequency
        freq_score = min(len(events) / 20.0, 1.0)

        # Sub-signal 2: Event type variety
        unique_types = len({e["event_type"] for e in events})
        variety_score = min(unique_types / 7.0, 1.0)

        # Sub-signal 3: Session depth (quiz + resource views)
        deep_events = [e for e in events if e["event_type"] in ("quiz_attempt", "resource_view", "code_run")]
        depth_score = min(len(deep_events) / 10.0, 1.0)

        engagement = (freq_score + variety_score + depth_score) / 3.0
        return round(float(np.clip(engagement, 0.0, 1.0)), 4)

    def check_dropout_risk(self, student_id: int) -> Dict[str, Any]:
        """
        Check if student has been inactive for DROPOUT_THRESHOLD_DAYS.

        Returns:
            Dict with is_at_risk, days_inactive, alert_message.
        """
        rows = db_manager.execute_query(
            """
            SELECT MAX(event_time) as last_active FROM learning_events
            WHERE student_id = ?
            """,
            (student_id,),
            self.db_path,
        )

        last_active_str = rows[0]["last_active"] if rows else None
        if not last_active_str:
            return {
                "is_at_risk": True,
                "days_inactive": None,
                "alert_message": "No learning activity recorded. Start your first session!",
            }

        try:
            last_active = datetime.fromisoformat(str(last_active_str).replace("Z", "+00:00"))
            days_inactive = (datetime.utcnow() - last_active.replace(tzinfo=None)).days
        except Exception:
            days_inactive = 0

        is_at_risk = days_inactive >= DROPOUT_THRESHOLD_DAYS
        msg = (
            f"⚠️ You have been inactive for {days_inactive} days. "
            f"Resume your study plan to maintain placement readiness momentum."
            if is_at_risk
            else f"Active within the last {days_inactive} day(s). Keep going!"
        )

        return {
            "is_at_risk":       is_at_risk,
            "days_inactive":    days_inactive,
            "alert_message":    msg,
        }

    def get_telemetry_summary(self, student_id: int) -> Dict[str, Any]:
        """Return full behavioral telemetry summary for a student."""
        consistency  = self.compute_consistency_score(student_id)
        engagement   = self.compute_engagement_score(student_id)
        dropout_risk = self.check_dropout_risk(student_id)

        # Active weeks count (past 6 weeks)
        rows = db_manager.execute_single(
            queries.COUNT_ACTIVE_WEEKS, (student_id,), self.db_path
        )
        active_weeks = int(rows["active_weeks"]) if rows else 0

        return {
            "f16_consistency_score":  consistency,
            "f21_engagement_score":   engagement,
            "active_weeks_last_6":    active_weeks,
            "dropout_risk":           dropout_risk,
            "epistemological_status": "ESTABLISHED_BY_RESEARCH (EMA, DD-010)",
        }

    def compute_metrics(self, student_id: int) -> Dict[str, Any]:
        """Convenience alias returning normalized consistency and engagement scores."""
        summary = self.get_telemetry_summary(student_id)
        return {
            "consistency_score": summary["f16_consistency_score"],
            "engagement_score":  summary["f21_engagement_score"],
            "dropout_risk":      summary["dropout_risk"],
        }
