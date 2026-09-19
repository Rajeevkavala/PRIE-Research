"""
ScholarCamp - Placement Readiness Intelligence Engine (PRIE)
Module 7: Learning Behavior Telemetry Analyzer
File: modules/behavior_analyzer.py

Tracks passive learner clickstream and session telemetry, quantifying study
discipline, engagement velocity, and recency of effort over a rolling 30-day window.
Computes behavioral signals as leading indicators of placement readiness.
"""

from __future__ import annotations

import json
import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

from database import queries
from database.db_manager import execute_insert, execute_query

logger = logging.getLogger("PRIE.BehaviorAnalyzer")


class LearningBehaviorAnalyzer:
    """Intelligence processing engine modeling student engagement and consistency."""

    def __init__(self, db_path: Optional[Union[str, Path]] = None) -> None:
        """Initialize the Learning Behavior Analyzer.

        Args:
            db_path: Optional explicit database path for isolated environments.
        """
        self.db_path = db_path

    def log_event(
        self,
        student_id: int,
        event_type: str,
        payload: Optional[Dict[str, Any]] = None,
        detail: str = "",
        duration_minutes: int = 0,
    ) -> int:
        """Log a new learning telemetry event to the persistence layer.

        Args:
            student_id: Primary key of student.
            event_type: Event category string (e.g. 'login', 'quiz_completed', 'roadmap_task_completed').
            payload: Optional dictionary payload.
            detail: Optional human-readable event description.
            duration_minutes: Active session or task duration in minutes.

        Returns:
            int: Primary key ID of created event row.
        """
        payload_str = json.dumps(payload or {})
        event_id = execute_insert(
            queries.INSERT_LEARNING_EVENT,
            (student_id, event_type, payload_str, detail, int(duration_minutes)),
            db_path=self.db_path,
        )
        return event_id

    def analyze_behavior(
        self,
        student_id: int,
        reference_time: Optional[datetime] = None,
    ) -> Tuple[float, float]:
        """Compute behavioral consistency and engagement velocity from event logs.

        Evaluates events over a rolling 30-day temporal window:
        1. Weekly Consistency (C_norm): Number of distinct active weeks / 4.0
        2. Engagement Velocity (E): Action count / 20.0 capped at 1.0
        3. Recency of Effort (R): Linear decay when inactive > 14 days, bounded at [0.2, 1.0]
        4. Composite Score: S_behavior = 0.40 * C_norm + 0.35 * E + 0.25 * R

        Args:
            student_id: Primary key of student.
            reference_time: Optional datetime reference (defaults to current timestamp).

        Returns:
            Tuple[float, float]: (s_behavior, consistency_score) in range [0.0, 1.0].
                                 Returns calibrated priors (0.50, 0.50) if no events exist.
        """
        events_rows = execute_query(
            queries.GET_STUDENT_EVENTS,
            (student_id, 1000),
            db_path=self.db_path,
        )

        if not events_rows:
            # Cold-start prior for newly onboarded students
            return 0.50, 0.50

        events = [dict(ev) for ev in events_rows]
        now = reference_time or datetime.now()
        thirty_days_ago = now - timedelta(days=30)

        # Parse event timestamps and filter to 30-day window
        recent_events: List[Dict[str, Any]] = []
        parsed_dates: List[datetime] = []

        for ev in events:
            time_raw = ev.get("event_time")
            if not time_raw:
                continue
            try:
                # Handle ISO format and SQLite standard datetime formats
                if isinstance(time_raw, str):
                    clean_time = time_raw.replace(" ", "T")
                    ev_time = datetime.fromisoformat(clean_time)
                elif isinstance(time_raw, datetime):
                    ev_time = time_raw
                else:
                    continue
            except Exception:
                continue

            parsed_dates.append(ev_time)
            if ev_time >= thirty_days_ago:
                recent_events.append({"event": ev, "time": ev_time})

        if not parsed_dates:
            return 0.50, 0.50

        # 1. Weekly Consistency (C_norm)
        active_weeks = set()
        for item in recent_events:
            ev_time = item["time"]
            # Map into week buckets (0 = this week, 1 = 1 week ago, 2 = 2 weeks ago, 3 = 3 weeks ago)
            days_ago = max(0, (now - ev_time).days)
            week_bucket = min(3, days_ago // 7)
            active_weeks.add(week_bucket)

        consistency_score = min(1.0, len(active_weeks) / 4.0)

        # 2. Engagement Velocity (E)
        recent_event_count = len(recent_events)
        engagement_velocity = min(1.0, recent_event_count / 20.0)

        # 3. Recency of Effort (R)
        latest_event_time = max(parsed_dates)
        days_inactive = max(0, (now - latest_event_time).days)
        recency_factor = max(0.20, 1.0 - (days_inactive / 14.0))

        # 4. Composite Behavioral Score (S_behavior)
        s_behavior = (
            (0.40 * consistency_score)
            + (0.35 * engagement_velocity)
            + (0.25 * recency_factor)
        )

        return round(float(s_behavior), 4), round(float(consistency_score), 4)

    def get_behavior_summary(
        self,
        student_id: int,
        reference_time: Optional[datetime] = None,
    ) -> Dict[str, Any]:
        """Compute detailed behavioral diagnostic breakdown.

        Args:
            student_id: Primary key of student.
            reference_time: Optional reference datetime.

        Returns:
            Dict[str, Any]: Detailed metrics including active weeks, velocity, and days inactive.
        """
        s_behavior, consistency_score = self.analyze_behavior(student_id, reference_time)

        events_rows = execute_query(
            queries.GET_STUDENT_EVENTS,
            (student_id, 1000),
            db_path=self.db_path,
        )
        total_events = len(events_rows)

        now = reference_time or datetime.now()
        thirty_days_ago = now - timedelta(days=30)
        recent_count = 0
        latest_date = None

        for row in events_rows:
            time_raw = row["event_time"]
            if not time_raw:
                continue
            try:
                if isinstance(time_raw, str):
                    clean_time = time_raw.replace(" ", "T")
                    ev_time = datetime.fromisoformat(clean_time)
                else:
                    ev_time = time_raw
            except Exception:
                continue

            if latest_date is None or ev_time > latest_date:
                latest_date = ev_time

            if ev_time >= thirty_days_ago:
                recent_count += 1

        days_inactive = (now - latest_date).days if latest_date else 999

        return {
            "student_id": student_id,
            "s_behavior": s_behavior,
            "consistency_score": consistency_score,
            "engagement_velocity": min(1.0, recent_count / 20.0),
            "recent_events_count": recent_count,
            "total_events_count": total_events,
            "days_inactive": days_inactive,
            "is_cold_start": total_events == 0,
        }
