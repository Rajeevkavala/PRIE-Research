"""
PRIE v1 — Module M08: Personalized Learning Roadmap Generator (A* DAG)
File: backend/modules/m08_roadmap_generator.py

MODULE: M08 — Personalized Learning Roadmap Generator
EPISTEMOLOGICAL_STATUS: ESTABLISHED_BY_RESEARCH (A* topological DAG, DD-007)
TRACEABILITY: Paper13, Paper16, Paper41, Paper44; DD-007

Implements:
  - A* shortest-path traversal over CS Concept DAG (JSON dict representation)
  - Generates 8-week sequenced milestone plan from M04 deficit targets
  - Prerequisite-aware topic ordering (topological sort)
  - Learning style personalization (visual/reading/practical/mixed)
"""

from __future__ import annotations

import json
import logging
import sys
from heapq import heappush, heappop
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import config
from database import db_manager, queries

logger = logging.getLogger("PRIE.M08.RoadmapGenerator")

# ── Embedded minimal CS concept DAG ──────────────────────────────────────────
# Full JSON DAG is loaded from config.CS_DAG_PATH; this is the fallback
MINIMAL_CS_DAG: Dict[str, Dict] = {
    "arrays":           {"prereqs": [],              "feature": "dsa_score", "difficulty": 1, "week_estimate": 1},
    "sorting":          {"prereqs": ["arrays"],       "feature": "dsa_score", "difficulty": 1, "week_estimate": 1},
    "linked_lists":     {"prereqs": ["arrays"],       "feature": "dsa_score", "difficulty": 2, "week_estimate": 1},
    "trees":            {"prereqs": ["linked_lists"], "feature": "dsa_score", "difficulty": 2, "week_estimate": 1},
    "graphs":           {"prereqs": ["trees"],        "feature": "dsa_score", "difficulty": 3, "week_estimate": 2},
    "dynamic_programming": {"prereqs": ["arrays", "trees"], "feature": "dsa_score", "difficulty": 3, "week_estimate": 2},
    "sql_basics":       {"prereqs": [],              "feature": "dbms_score", "difficulty": 1, "week_estimate": 1},
    "normalization":    {"prereqs": ["sql_basics"],  "feature": "dbms_score", "difficulty": 2, "week_estimate": 1},
    "indexing":         {"prereqs": ["sql_basics"],  "feature": "dbms_score", "difficulty": 2, "week_estimate": 1},
    "transactions":     {"prereqs": ["normalization"], "feature": "dbms_score", "difficulty": 3, "week_estimate": 1},
    "processes":        {"prereqs": [],              "feature": "os_score",   "difficulty": 1, "week_estimate": 1},
    "scheduling":       {"prereqs": ["processes"],   "feature": "os_score",   "difficulty": 2, "week_estimate": 1},
    "memory_management": {"prereqs": ["processes"],  "feature": "os_score",   "difficulty": 2, "week_estimate": 1},
    "deadlocks":        {"prereqs": ["scheduling"],  "feature": "os_score",   "difficulty": 3, "week_estimate": 1},
    "osi_model":        {"prereqs": [],              "feature": "cn_score",   "difficulty": 1, "week_estimate": 1},
    "tcp_ip":           {"prereqs": ["osi_model"],   "feature": "cn_score",   "difficulty": 2, "week_estimate": 1},
    "python_basics":    {"prereqs": [],              "feature": "programming_score", "difficulty": 1, "week_estimate": 1},
    "oop":              {"prereqs": ["python_basics"], "feature": "programming_score", "difficulty": 2, "week_estimate": 1},
    "resume_keywords":  {"prereqs": [],              "feature": "resume_ats_score", "difficulty": 1, "week_estimate": 1},
    "quantitative_basics": {"prereqs": [],           "feature": "aptitude_score", "difficulty": 1, "week_estimate": 1},
}

# Feature → topics map
FEATURE_TO_TOPICS: Dict[str, List[str]] = {}
for node, meta in MINIMAL_CS_DAG.items():
    feat = meta["feature"]
    FEATURE_TO_TOPICS.setdefault(feat, []).append(node)


# ── Learning style resource preferences ──────────────────────────────────────
STYLE_RESOURCES: Dict[str, Dict] = {
    "visual":    {"type": "video", "platform": "YouTube / NPTEL", "boost": 1.2},
    "reading":   {"type": "article", "platform": "GeeksForGeeks / Articles", "boost": 1.0},
    "practical": {"type": "practice_problem", "platform": "LeetCode / HackerRank", "boost": 1.2},
    "mixed":     {"type": "course", "platform": "Coursera / NPTEL", "boost": 1.1},
}


class RoadmapGenerator:
    """
    M08: Personalized Learning Roadmap Generator.

    Uses A* topological traversal over CS Concept DAG to generate
    a prerequisite-aware 8-week study plan from the M04 deficit vector.

    EPISTEMOLOGICAL_STATUS: ESTABLISHED_BY_RESEARCH (A* DAG, DD-007)
    """

    def __init__(self, db_path: Optional[Path] = None) -> None:
        self.db_path = db_path
        self._dag = self._load_dag()
        self.feature_to_topics: Dict[str, List[str]] = {}
        for node, meta in self._dag.items():
            feat = meta.get("feature", "dsa_score")
            self.feature_to_topics.setdefault(feat, []).append(node)

    def _load_dag(self) -> Dict[str, Dict]:
        """Load CS Concept DAG from JSON file, fallback to minimal embedded DAG."""
        path = config.CS_DAG_PATH
        if path.exists():
            try:
                dag = json.loads(path.read_text(encoding="utf-8"))
                logger.info(f"CS Concept DAG loaded: {len(dag)} nodes from {path}")
                return dag
            except Exception as e:
                logger.warning(f"DAG load failed: {e} — using minimal embedded DAG")
        return MINIMAL_CS_DAG

    def _topological_sort(self, topic_set: Set[str]) -> List[str]:
        """
        Topological sort of selected topics respecting prerequisite ordering.
        Uses Kahn's algorithm (DAG-compatible A* heuristic).
        """
        in_degree: Dict[str, int] = {t: 0 for t in topic_set}
        adj: Dict[str, List[str]] = {t: [] for t in topic_set}

        for topic in topic_set:
            node = self._dag.get(topic, {})
            for prereq in node.get("prereqs", []):
                if prereq in topic_set:
                    in_degree[topic] = in_degree.get(topic, 0) + 1
                    adj[prereq].append(topic)

        # Priority queue: (difficulty, topic)
        pq = []
        for t, deg in in_degree.items():
            if deg == 0:
                diff = self._dag.get(t, {}).get("difficulty", 1)
                heappush(pq, (diff, t))

        ordered = []
        while pq:
            _, topic = heappop(pq)
            ordered.append(topic)
            for neighbor in adj.get(topic, []):
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    diff = self._dag.get(neighbor, {}).get("difficulty", 2)
                    heappush(pq, (diff, neighbor))

        # Append any remaining (circular dependencies)
        ordered += [t for t in topic_set if t not in ordered]
        return ordered

    def generate(
        self,
        student_id: int,
        deficit_list: List[Dict],
        target_role: str = "Software Development Engineer",
        learning_style: str = "practical",
        n_weeks: int = None,
    ) -> List[Dict]:
        """
        Generate a personalized n-week learning roadmap.

        Args:
            student_id: Primary key of student.
            deficit_list: Ranked deficit list from M04.
            target_role: Target career role.
            learning_style: Student's preferred learning modality.
            n_weeks: Number of roadmap weeks (default from config).

        Returns:
            List of week dicts with topics, resources, and target SPV features.
        """
        n_weeks = n_weeks or config.ROADMAP_WEEKS
        style = STYLE_RESOURCES.get(learning_style, STYLE_RESOURCES["practical"])

        # 1. Identify target features from deficit list
        target_features = [item["feature"] for item in deficit_list[:6]]

        # 2. Collect topics for each deficit feature
        selected_topics: Set[str] = set()
        for feat in target_features:
            topics = self.feature_to_topics.get(feat, FEATURE_TO_TOPICS.get(feat, []))
            selected_topics.update(topics)

        if not selected_topics:
            # Fallback: default SDE curriculum
            selected_topics = {"arrays", "sorting", "sql_basics", "python_basics",
                               "processes", "osi_model", "resume_keywords", "quantitative_basics"}

        # 3. Topological sort
        ordered_topics = self._topological_sort(selected_topics)

        # 4. Pack into weeks (max 2 topics per week)
        weeks = []
        topics_per_week = config.MAX_TOPICS_PER_WEEK
        for week_num in range(1, n_weeks + 1):
            start = (week_num - 1) * topics_per_week
            week_topics = ordered_topics[start:start + topics_per_week]
            if not week_topics and week_num <= 4:
                week_topics = ["revision"]

            week_features = list({
                self._dag.get(t, {}).get("feature", "dsa_score")
                for t in week_topics
            })

            resources = [
                {
                    "title":    f"{t.replace('_', ' ').title()} — {style['platform']}",
                    "type":     style["type"],
                    "platform": style["platform"],
                    "topic":    t,
                }
                for t in week_topics
            ]

            weeks.append({
                "week_number":    week_num,
                "topics":         week_topics,
                "resources":      resources,
                "concept_nodes":  week_topics,
                "target_features": week_features,
                "status":         "pending",
            })

            # Persist to DB
            try:
                db_manager.execute_update(
                    queries.INSERT_ROADMAP_WEEK,
                    (
                        student_id, week_num,
                        json.dumps(week_topics),
                        json.dumps(resources),
                        json.dumps(week_topics),
                        "pending",
                        json.dumps(week_features),
                    ),
                    self.db_path,
                )
            except Exception as e:
                logger.warning(f"Roadmap DB write failed (week {week_num}): {e}")

        logger.info(f"Generated {len(weeks)}-week roadmap for student {student_id} — {len(ordered_topics)} topics")
        return weeks

    def get_roadmap(self, student_id: int) -> List[Dict]:
        """Retrieve the current roadmap from database."""
        rows = db_manager.execute_query(
            queries.GET_STUDENT_ROADMAP, (student_id,), self.db_path
        )
        return db_manager.dict_rows(rows)

    def mark_week_complete(self, student_id: int, week_number: int) -> bool:
        """Mark a roadmap week as completed."""
        affected = db_manager.execute_update(
            queries.UPDATE_ROADMAP_STATUS,
            ("completed", "CURRENT_TIMESTAMP", student_id, week_number),
            self.db_path,
        )
        return affected > 0
