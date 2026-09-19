"""
ScholarCamp - Placement Readiness Intelligence Engine (PRIE)
Database Initialization & Seed Data Ingestion Script
File: database/db_init.py

Executes DDL schema creation, B-tree index compilation, and idempotent seeding
of benchmark companies, 500+ classified skills, administrative and student
credentials, diagnostic assessment questions, and curated learning resources.
"""

from __future__ import annotations

import argparse
import json
import logging
import os
from pathlib import Path
from typing import Optional, Union
import bcrypt

import config
from database.db_manager import get_db_connection

logger = logging.getLogger("PRIE.DatabaseInit")


def hash_password(password: str) -> str:
    """Hashes a plaintext password using bcrypt with salt rounds defined in config.

    Args:
        password: Plaintext password string.

    Returns:
        str: Salted bcrypt hash string.
    """
    rounds = getattr(config, "BCRYPT_ROUNDS", 12)
    salt = bcrypt.gensalt(rounds=rounds)
    return bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")


def initialize_database(
    db_path: Optional[Union[str, Path]] = None,
    force_recreate: bool = False,
) -> None:
    """Initializes schema, builds indexes, and ingests seed data idempotently.

    Args:
        db_path: Optional database path. Defaults to config.DATABASE_PATH.
        force_recreate: If True, removes existing database file before building.
    """
    target_path = Path(db_path) if db_path is not None else config.DATABASE_PATH

    if force_recreate and str(target_path) != ":memory:" and target_path.exists():
        logger.warning("Force recreate requested. Removing existing database at: %s", target_path)
        try:
            target_path.unlink()
        except Exception as err:
            logger.error("Failed to remove old database: %s", err)

    logger.info("Initializing PRIE Database at: %s", target_path)
    base_dir = Path(__file__).resolve().parent

    schema_file = base_dir / "schema.sql"
    index_file = base_dir / "indexes.sql"

    with get_db_connection(target_path) as conn:
        cursor = conn.cursor()

        # 1. Execute DDL Schema
        if schema_file.exists():
            logger.info("Executing DDL schema from %s", schema_file.name)
            with open(schema_file, "r", encoding="utf-8") as f:
                cursor.executescript(f.read())
        else:
            raise FileNotFoundError(f"Missing schema file: {schema_file}")

        # 2. Execute High-Performance Indexes
        if index_file.exists():
            logger.info("Building B-Tree indexes from %s", index_file.name)
            with open(index_file, "r", encoding="utf-8") as f:
                cursor.executescript(f.read())
        else:
            raise FileNotFoundError(f"Missing index file: {index_file}")

        # 3. Seed Companies
        companies_json_path = getattr(config, "COMPANIES_PATH", config.DATA_DIR / "companies.json")
        if companies_json_path.exists():
            with open(companies_json_path, "r", encoding="utf-8") as f:
                companies_data = json.load(f)
                for comp in companies_data:
                    req_skills = json.dumps(comp.get("required_skills", []))
                    tech_stack = json.dumps(comp.get("tech_stack", []))
                    role_profiles = json.dumps(comp.get("role_profiles", {}))
                    cursor.execute(
                        """
                        INSERT OR IGNORE INTO companies (
                            company_name, tier, min_cgpa, max_backlogs,
                            required_skills_json, tech_stack_json, prs_threshold,
                            role_profiles_json, description
                        )
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """,
                        (
                            comp["company_name"],
                            comp["tier"],
                            comp.get("min_cgpa", 6.0),
                            comp.get("max_backlogs", 0),
                            req_skills,
                            tech_stack,
                            comp.get("prs_threshold", 0.65),
                            role_profiles,
                            comp.get("description", ""),
                        ),
                    )
            logger.info("Companies seeded successfully from %s", companies_json_path.name)

        # 4. Seed Administrative User
        admin_email = "admin@scholarcamp.edu"
        cursor.execute("SELECT student_id FROM students WHERE email = ?", (admin_email,))
        if not cursor.fetchone():
            admin_pwd = hash_password("Admin@ScholarCamp2026")
            cursor.execute(
                """
                INSERT INTO students (
                    name, email, password_hash, branch, cgpa, backlogs,
                    skills_json, target_role, profile_completeness, is_admin
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    "System Administrator",
                    admin_email,
                    admin_pwd,
                    "Administration",
                    10.0,
                    0,
                    json.dumps(["Administration", "Security", "System Design"]),
                    "Platform Administrator",
                    100.0,
                    1,
                ),
            )
            logger.info("Created system administrator: %s", admin_email)

        # 5. Seed Benchmark Student (Aryan Verma)
        student_email = "aryan@scholarcamp.edu"
        cursor.execute("SELECT student_id FROM students WHERE email = ?", (student_email,))
        student_row = cursor.fetchone()
        student_id: int
        if not student_row:
            student_pwd = hash_password("Student@123")
            # Lookup Google as target company
            cursor.execute("SELECT company_id FROM companies WHERE company_name = 'Google'")
            google_row = cursor.fetchone()
            google_id = google_row["company_id"] if google_row else 1

            cursor.execute(
                """
                INSERT INTO students (
                    name, email, password_hash, branch, cgpa, backlogs,
                    skills_json, target_role, target_company_id, learning_style,
                    profile_completeness, is_admin
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    "Aryan Verma",
                    student_email,
                    student_pwd,
                    "CSE",
                    7.8,
                    0,
                    json.dumps(["Python", "Java", "SQL", "Data Structures", "HTML5"]),
                    "Software Development Engineer",
                    google_id,
                    "practical",
                    75.0,
                    0,
                ),
            )
            student_id = cursor.lastrowid
            logger.info("Created baseline student: %s (id: %d)", student_email, student_id)
        else:
            student_id = student_row["student_id"]

        # 6. Seed 500+ Skills into skill_map
        skills_json_path = getattr(config, "SKILL_TAXONOMY_PATH", config.DATA_DIR / "skill_taxonomy.json")
        if skills_json_path.exists():
            with open(skills_json_path, "r", encoding="utf-8") as f:
                skills_data = json.load(f)
                for item in skills_data:
                    synonyms_str = json.dumps(item.get("synonyms", []))
                    aliases_str = json.dumps(item.get("aliases", []))
                    related_str = json.dumps(item.get("related_topics", []))
                    cursor.execute(
                        """
                        INSERT OR IGNORE INTO skill_map (
                            skill_name, category, level, baseline_weight,
                            synonyms_json, aliases_json, related_topics_json
                        )
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                        """,
                        (
                            item["skill_name"],
                            item["category"],
                            item.get("level", "intermediate"),
                            item.get("baseline_weight", 0.50),
                            synonyms_str,
                            aliases_str,
                            related_str,
                        ),
                    )
            logger.info("Skill taxonomy ingested from %s", skills_json_path.name)

        # 7. Seed Question Bank
        qbank_json_path = getattr(config, "QUESTION_BANK_PATH", config.DATA_DIR / "question_bank.json")
        if qbank_json_path.exists():
            with open(qbank_json_path, "r", encoding="utf-8") as f:
                qbank_data = json.load(f)
                for q in qbank_data:
                    opts_str = json.dumps(q.get("options", []))
                    cursor.execute(
                        """
                        INSERT OR IGNORE INTO question_bank (
                            topic, difficulty, question_text, options_json,
                            correct_option, explanation, created_by
                        )
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                        """,
                        (
                            q["topic"],
                            q["difficulty"],
                            q["question_text"],
                            opts_str,
                            q["correct_option"],
                            q.get("explanation", ""),
                            student_id,
                        ),
                    )
            logger.info("Diagnostic questions seeded from %s", qbank_json_path.name)

        # 8. Seed Initial Recommendations for Sample Student
        res_lib_path = getattr(config, "RESOURCE_LIBRARY_PATH", config.DATA_DIR / "resource_library.json")
        if res_lib_path.exists():
            with open(res_lib_path, "r", encoding="utf-8") as f:
                res_data = json.load(f)
                for res in res_data:
                    cursor.execute(
                        """
                        INSERT OR IGNORE INTO recommendations (
                            student_id, title, topic, resource_type, url,
                            difficulty, platform, relevance_score, reason, is_completed
                        )
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 0)
                        """,
                        (
                            student_id,
                            res["title"],
                            res["topic"],
                            res["resource_type"],
                            res["url"],
                            res.get("difficulty", "intermediate"),
                            res.get("platform", "Web"),
                            res.get("relevance_score", 0.85),
                            res.get("reason", "Curated roadmap preparation asset."),
                        ),
                    )
            logger.info("Recommendations initialized from %s", res_lib_path.name)

        # Verification & Row Counts
        tables = [
            "students", "companies", "resumes", "question_bank", "assessments",
            "prs_history", "roadmaps", "recommendations", "learning_events", "skill_map"
        ]
        counts = {}
        for table in tables:
            cursor.execute(f"SELECT COUNT(*) AS total FROM {table}")
            row = cursor.fetchone()
            counts[table] = row["total"] if row else 0

        logger.info("=== Database Initialization Complete ===")
        for tbl, cnt in counts.items():
            logger.info("  Table %-18s: %4d records", tbl, cnt)

    return counts


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ScholarCamp PRIE Database Initializer")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Recreate database from scratch, removing existing database file.",
    )
    args = parser.parse_args()

    # Configure root logger for CLI feedback
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

    initialize_database(force_recreate=args.force)
