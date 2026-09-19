"""
PRIE v1 — Database Seeder
File: backend/database/seed_data.py

Populates initial seed data:
  1. Question Bank with IRT item parameters (DSA, DBMS, OS, CN, Programming, Aptitude)
  2. Company Benchmarks across MAANG, Tier-1 Product, Tier-2 Product, and Service
  3. Canonical Skill Taxonomy
  4. Demo Student with initialized profile
"""

from __future__ import annotations

import hashlib
import json
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import config
from database.db_manager import execute_insert, execute_query, initialize_schema
from database.queries import (
    INSERT_COMPANY,
    INSERT_QUESTION,
    INSERT_STUDENT,
)

logger = logging.getLogger("PRIE.SeedData")
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s]: %(message)s")


def _hash_pw(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


# ── Question Bank Seed ────────────────────────────────────────────────────────
QUESTIONS = [
    # DSA
    (
        "dsa", "Easy",
        "What is the average time complexity of searching in a balanced Binary Search Tree (BST)?",
        json.dumps(["O(1)", "O(log n)", "O(n)", "O(n log n)"]),
        "O(log n)",
        "In a balanced BST like AVL or Red-Black tree, the height is bounded by O(log n), so search takes O(log n) time.",
        0.30, 0.45, "DSA-TREE-01", "confuses_bst_with_linear_search"
    ),
    (
        "dsa", "Easy",
        "Which data structure operates on a Last In First Out (LIFO) basis?",
        json.dumps(["Queue", "Stack", "Priority Queue", "Deque"]),
        "Stack",
        "A Stack processes elements in LIFO order using push and pop operations.",
        0.20, 0.40, "DSA-STACK-01", None
    ),
    (
        "dsa", "Medium",
        "Which algorithm is used to find the shortest path from a single source vertex to all other vertices in a weighted graph with non-negative weights?",
        json.dumps(["Bellman-Ford", "Dijkstra's Algorithm", "Floyd-Warshall", "Prim's Algorithm"]),
        "Dijkstra's Algorithm",
        "Dijkstra solves single-source shortest paths on non-negative edge graphs in O((V + E) log V) with a min-heap.",
        0.55, 0.65, "DSA-GRAPH-01", "selects_bellman_ford_for_positive_weights"
    ),
    (
        "dsa", "Medium",
        "What is the amortized time complexity of inserting an element into a dynamic array (like std::vector or Python list)?",
        json.dumps(["O(1)", "O(log n)", "O(n)", "O(n^2)"]),
        "O(1)",
        "Although array resizing takes O(n), geometric doubling ensures the amortized cost per append is O(1).",
        0.50, 0.55, "DSA-ARRAY-02", "confuses_worst_case_with_amortized"
    ),
    (
        "dsa", "Hard",
        "In dynamic programming, what is the key difference between the 0/1 Knapsack problem and the Fractional Knapsack problem?",
        json.dumps([
            "0/1 Knapsack can be solved with a greedy approach, while Fractional cannot",
            "Fractional Knapsack requires DP, while 0/1 Knapsack requires Divide and Conquer",
            "0/1 Knapsack cannot be solved greedily and requires DP, while Fractional is solvable greedily",
            "Both require 2D dynamic programming matrices"
        ]),
        "0/1 Knapsack cannot be solved greedily and requires DP, while Fractional is solvable greedily",
        "Fractional items can be sorted by value/weight ratio and greedily chosen, while discrete 0/1 choice requires checking overlapping subproblems.",
        0.75, 0.70, "DSA-DP-01", "believes_greedy_works_on_01_knapsack"
    ),
    # DBMS
    (
        "dbms", "Easy",
        "Which SQL command is used to remove all records from a table without logging individual row deletions?",
        json.dumps(["DELETE", "DROP", "TRUNCATE", "REMOVE"]),
        "TRUNCATE",
        "TRUNCATE is a DDL command that deallocates data pages and is faster than DELETE without logging individual row deletions.",
        0.35, 0.40, "DBMS-SQL-01", "confuses_truncate_with_drop"
    ),
    (
        "dbms", "Medium",
        "Which normal form eliminates partial functional dependency on the candidate key?",
        json.dumps(["1NF", "2NF", "3NF", "BCNF"]),
        "2NF",
        "A relation is in 2NF if it is in 1NF and no non-prime attribute is partially dependent on any candidate key.",
        0.55, 0.60, "DBMS-NORM-01", "confuses_2nf_and_3nf"
    ),
    (
        "dbms", "Medium",
        "What does the 'I' in ACID properties of relational transactions stand for?",
        json.dumps(["Integrity", "Isolation", "Immutability", "Indexing"]),
        "Isolation",
        "Isolation ensures that concurrent transactions execute without interfering with one another.",
        0.40, 0.50, "DBMS-TX-01", "confuses_isolation_with_integrity"
    ),
    (
        "dbms", "Hard",
        "Which transaction isolation level prevents Dirty Reads and Non-Repeatable Reads, but may still allow Phantom Reads in ANSI SQL?",
        json.dumps(["Read Uncommitted", "Read Committed", "Repeatable Read", "Serializable"]),
        "Repeatable Read",
        "Repeatable Read locks rows read, preventing dirty and non-repeatable reads, but may allow phantom inserts unless range locking is used.",
        0.78, 0.68, "DBMS-ISO-01", "confuses_serializable_and_repeatable_read"
    ),
    # OS
    (
        "os", "Easy",
        "Which CPU scheduling algorithm gives minimal average waiting time for a given set of processes?",
        json.dumps(["FCFS", "Round Robin", "Shortest Job First (SJF)", "Priority Scheduling"]),
        "Shortest Job First (SJF)",
        "SJF is provably optimal for minimizing average waiting time, though burst times are rarely known in advance.",
        0.38, 0.45, "OS-SCHED-01", "selects_round_robin_for_minimal_waiting"
    ),
    (
        "os", "Medium",
        "Which of the following is NOT one of the four necessary conditions for a deadlock (Coffman conditions)?",
        json.dumps(["Mutual Exclusion", "Hold and Wait", "Preemption allowed", "Circular Wait"]),
        "Preemption allowed",
        "The condition is 'No Preemption'. If preemption is allowed, deadlocks can be broken.",
        0.52, 0.58, "OS-DEADLOCK-01", "misses_negation_in_preemption"
    ),
    (
        "os", "Hard",
        "What is Belady's Anomaly in operating system virtual memory management?",
        json.dumps([
            "Thrashing occurs when too many pages are allocated to a process",
            "In FIFO page replacement, increasing the number of page frames can result in an increased number of page faults",
            "LRU page replacement degenerates to O(n) search time when memory is tight",
            "Dirty pages cannot be written to disk if page faults exceed 100/sec"
        ]),
        "In FIFO page replacement, increasing the number of page frames can result in an increased number of page faults",
        "Belady's Anomaly describes the counterintuitive behavior of FIFO where more page frames cause more page faults on certain reference strings.",
        0.72, 0.65, "OS-VM-01", "confuses_beladys_anomaly_with_thrashing"
    ),
    # Computer Networks
    (
        "cn", "Easy",
        "Which layer of the OSI model is responsible for end-to-end reliable data delivery?",
        json.dumps(["Network Layer", "Transport Layer", "Data Link Layer", "Session Layer"]),
        "Transport Layer",
        "The Transport Layer (e.g., TCP) provides end-to-end communication services for applications.",
        0.30, 0.40, "CN-OSI-01", "confuses_network_and_transport"
    ),
    (
        "cn", "Medium",
        "In the TCP 3-way handshake, what is the exact sequence of flags transmitted to establish a connection?",
        json.dumps(["SYN -> ACK -> SYN-ACK", "SYN -> SYN-ACK -> ACK", "ACK -> SYN -> SYN-ACK", "SYN-ACK -> SYN -> ACK"]),
        "SYN -> SYN-ACK -> ACK",
        "Client sends SYN, server replies with SYN-ACK, client acknowledges with ACK.",
        0.48, 0.55, "CN-TCP-01", "inverts_handshake_order"
    ),
    (
        "cn", "Hard",
        "What is the primary mechanism of TCP Tahoe and Reno when a triple-duplicate ACK is received?",
        json.dumps([
            "Full Timeout: cwnd is set to 1 MSS immediately and slow start begins",
            "Fast Retransmit: segment is retransmitted before the retransmission timer expires, and cwnd drops to ssthresh + 3 MSS in Reno",
            "Exponential Backoff: double RTO without retransmitting",
            "Nagle's algorithm halts packet transmission until window slides"
        ]),
        "Fast Retransmit: segment is retransmitted before the retransmission timer expires, and cwnd drops to ssthresh + 3 MSS in Reno",
        "Triple duplicate ACKs indicate a single missing packet has slipped through; Fast Retransmit / Fast Recovery circumvents slow start.",
        0.76, 0.68, "CN-CONG-01", "confuses_fast_retransmit_with_timeout"
    ),
    # Programming
    (
        "programming", "Easy",
        "In Python, what is the output of `type([])`?",
        json.dumps(["<class 'array'>", "<class 'list'>", "<class 'tuple'>", "<class 'dict'>"]),
        "<class 'list'>",
        "`[]` denotes a built-in Python list object.",
        0.15, 0.35, "PROG-PY-01", None
    ),
    (
        "programming", "Medium",
        "What is the difference between shallow copy and deep copy in object-oriented languages?",
        json.dumps([
            "Shallow copy creates new objects for all nested elements, while deep copy copies references",
            "Shallow copy constructs a new compound object and inserts references to the original child objects; deep copy recursively copies child objects",
            "Deep copy is only available in Java, while shallow copy is Python-specific",
            "Shallow copy cannot copy primitive types"
        ]),
        "Shallow copy constructs a new compound object and inserts references to the original child objects; deep copy recursively copies child objects",
        "A shallow copy duplicates the container; a deep copy recursively duplicates both the container and all nested objects.",
        0.50, 0.58, "PROG-OOP-01", "inverts_shallow_and_deep_definitions"
    ),
    # Aptitude
    (
        "aptitude", "Easy",
        "If a train running at 72 km/h crosses a 200m platform in 20 seconds, what is the length of the train?",
        json.dumps(["150 m", "200 m", "250 m", "300 m"]),
        "200 m",
        "Speed = 72 * (5/18) = 20 m/s. Total distance = speed * time = 20 * 20 = 400 m. Train length = 400 - 200 = 200 m.",
        0.45, 0.50, "APT-SPEED-01", "forgets_platform_length_deduction"
    ),
    (
        "aptitude", "Medium",
        "A sum of money doubles itself in 5 years at simple interest. In how many years will it become 4 times itself?",
        json.dumps(["10 years", "12 years", "15 years", "20 years"]),
        "15 years",
        "Simple interest: Doubling means interest = P in 5 years (rate = 20%). To become 4 times, interest = 3P. Time = 3 * 5 = 15 years.",
        0.58, 0.62, "APT-SI-01", "applies_compound_interest_formula"
    ),
]


# ── Company Benchmarks Seed ───────────────────────────────────────────────────
COMPANIES = [
    (
        "Google", "MAANG", 8.0, 0,
        json.dumps(["DSA", "System Design", "Python", "Go", "C++", "Distributed Systems"]),
        json.dumps(["Kubernetes", "Borg", "Spanner", "TensorFlow", "gRPC"]),
        0.82,
        json.dumps({
            "roles": ["Software Engineer L3", "Associate Product Manager"],
            "focus_areas": ["Advanced Graph Algorithms", "Dynamic Programming", "Concurrency"]
        }),
        "Global technology leader in search, cloud, AI, and advertising infrastructure."
    ),
    (
        "Microsoft", "MAANG", 7.5, 0,
        json.dumps(["DSA", "C#", "C++", "Azure", "Cloud Computing", "OOP"]),
        json.dumps([".NET", "Azure", "TypeScript", "React", "CosmosDB"]),
        0.78,
        json.dumps({
            "roles": ["Software Engineer", "Support Engineer", "Program Manager"],
            "focus_areas": ["Tree/Graph Traversal", "System Design", "Object Oriented Design"]
        }),
        "Global software and cloud enterprise leader."
    ),
    (
        "Amazon", "MAANG", 7.0, 0,
        json.dumps(["DSA", "Java", "AWS", "Leadership Principles", "System Design"]),
        json.dumps(["DynamoDB", "AWS Lambda", "EC2", "Spring Boot", "Java"]),
        0.75,
        json.dumps({
            "roles": ["Software Development Engineer I"],
            "focus_areas": ["LP Behavioral Questions", "Heaps", "DP", "Low-Level Design"]
        }),
        "E-commerce and cloud hyperscaler."
    ),
    (
        "Razorpay", "Tier-1 Product", 7.0, 0,
        json.dumps(["DSA", "Python", "Golang", "DBMS", "Microservices", "Kafka"]),
        json.dumps(["Go", "PHP", "MySQL", "Kafka", "Redis", "Docker"]),
        0.72,
        json.dumps({
            "roles": ["Backend Engineer I", "Frontend Engineer I"],
            "focus_areas": ["Database ACID & Indexing", "Concurrency", "API Design"]
        }),
        "Leading Indian fintech payments gateway unicorns."
    ),
    (
        "CRED", "Tier-1 Product", 7.5, 0,
        json.dumps(["DSA", "Java", "Distributed Systems", "SQL", "High Scale Architecture"]),
        json.dumps(["Kotlin", "Java", "PostgreSQL", "Kafka", "Redis"]),
        0.76,
        json.dumps({
            "roles": ["Software Engineer (Backend)", "Mobile Engineer"],
            "focus_areas": ["Fast Algorithms", "Clean Code Architecture", "Problem Solving"]
        }),
        "High-trust credit score and premium rewards platform."
    ),
    (
        "Flipkart", "Tier-1 Product", 7.0, 0,
        json.dumps(["DSA", "Java", "Multithreading", "Spring Boot", "Kafka"]),
        json.dumps(["Java", "HBase", "Kafka", "MySQL", "Storm"]),
        0.70,
        json.dumps({
            "roles": ["Software Development Engineer 1"],
            "focus_areas": ["Machine Coding Round", "DSA Hard", "LLD"]
        }),
        "Leading Indian e-commerce marketplace."
    ),
    (
        "Zoho", "Tier-2 Product", 6.5, 1,
        json.dumps(["C", "Java", "OOP", "DBMS", "Problem Solving"]),
        json.dumps(["Java", "C++", "MySQL", "JavaScript"]),
        0.62,
        json.dumps({
            "roles": ["Software Developer"],
            "focus_areas": ["Language Fundamentals", "Basic Data Structures", "Application Development"]
        }),
        "Global SaaS business applications suite provider."
    ),
    (
        "TCS Digital", "Service-Based", 6.5, 0,
        json.dumps(["Java", "Python", "SQL", "Aptitude", "DSA Basics"]),
        json.dumps(["Java", "Angular", "Spring", "Oracle SQL"]),
        0.60,
        json.dumps({
            "roles": ["Digital Cadre Engineer"],
            "focus_areas": ["Advanced Coding", "Quantitative Aptitude", "Verbal Ability"]
        }),
        "TCS premium digital cadre hiring track."
    ),
    (
        "Infosys DSE", "Service-Based", 6.5, 0,
        json.dumps(["Python", "Java", "DSA", "DBMS", "Aptitude"]),
        json.dumps(["Python", "React", "PostgreSQL"]),
        0.60,
        json.dumps({
            "roles": ["Digital Specialist Engineer"],
            "focus_areas": ["HackWithInfy Coding", "Greedy & Graphs", "DBMS Queries"]
        }),
        "Infosys specialized digital roles track."
    ),
]


# ── Canonical Skill Taxonomy Seed ─────────────────────────────────────────────
SKILLS = [
    ("Data Structures & Algorithms", "Technical", "advanced", 0.90, json.dumps(["DSA", "Algorithms", "Data Structures"]), json.dumps(["Arrays", "Trees", "Graphs", "DP"])),
    ("Object-Oriented Programming", "Technical", "intermediate", 0.75, json.dumps(["OOP", "OOPs", "Object Oriented"]), json.dumps(["Inheritance", "Polymorphism", "Encapsulation"])),
    ("Database Management Systems", "Technical", "intermediate", 0.70, json.dumps(["DBMS", "SQL", "RDBMS", "Relational Database"]), json.dumps(["ACID", "Normalization", "Indexing"])),
    ("Operating Systems", "Technical", "intermediate", 0.65, json.dumps(["OS", "Operating System"]), json.dumps(["Processes", "Threads", "Memory Management", "Deadlocks"])),
    ("Computer Networks", "Technical", "intermediate", 0.65, json.dumps(["CN", "Networking", "Computer Network"]), json.dumps(["TCP/IP", "OSI Model", "HTTP", "DNS"])),
    ("Python", "Programming", "intermediate", 0.70, json.dumps(["Python3", "Py"]), json.dumps(["FastAPI", "Pandas", "NumPy", "Django"])),
    ("Java", "Programming", "intermediate", 0.75, json.dumps(["Core Java", "J2EE"]), json.dumps(["Spring Boot", "JVM", "Collections Framework"])),
    ("C++", "Programming", "intermediate", 0.70, json.dumps(["CPP", "Modern C++"]), json.dumps(["STL", "Pointers", "Memory Management"])),
    ("JavaScript", "Programming", "intermediate", 0.65, json.dumps(["JS", "ECMAScript"]), json.dumps(["DOM", "Async/Await", "ES6", "Node.js"])),
    ("Git & Version Control", "Tools", "beginner", 0.60, json.dumps(["Git", "GitHub", "GitLab"]), json.dumps(["Branching", "Pull Requests", "Merge Conflicts"])),
    ("Docker & Containers", "Tools", "intermediate", 0.55, json.dumps(["Docker", "Containerization"]), json.dumps(["Dockerfile", "Compose", "Images"])),
    ("System Design (LLD)", "Architecture", "advanced", 0.80, json.dumps(["Low Level Design", "Object Oriented Design"]), json.dumps(["Design Patterns", "SOLID Principles", "UML"])),
    ("Quantitative Aptitude", "Aptitude", "intermediate", 0.60, json.dumps(["Quant", "Math", "Aptitude"]), json.dumps(["Percentages", "Time & Work", "Probability"])),
    ("Verbal Ability", "Aptitude", "intermediate", 0.50, json.dumps(["English", "Verbal", "Communication"]), json.dumps(["Reading Comprehension", "Grammar"])),
]


def seed_database(db_path: Path | None = None) -> None:
    """Run all seed procedures."""
    logger.info("Initializing database schema...")
    initialize_schema(db_path)

    # 1. Questions
    logger.info("Seeding Question Bank...")
    q_count = 0
    for q in QUESTIONS:
        try:
            execute_insert(INSERT_QUESTION, q, db_path)
            q_count += 1
        except Exception as e:
            logger.debug(f"Question insert note: {e}")
    logger.info(f"Seeded {q_count} questions.")

    # 2. Companies
    logger.info("Seeding Companies...")
    c_count = 0
    for c in COMPANIES:
        try:
            execute_insert(INSERT_COMPANY, c, db_path)
            c_count += 1
        except Exception as e:
            logger.debug(f"Company insert note: {e}")
    logger.info(f"Seeded {c_count} company benchmarks.")

    # 3. Skills
    logger.info("Seeding Skill Taxonomy...")
    insert_skill = """
    INSERT OR IGNORE INTO skill_map
      (skill_name, category, level, baseline_weight, synonyms_json, related_topics_json)
    VALUES (?, ?, ?, ?, ?, ?)
    """
    s_count = 0
    for s in SKILLS:
        try:
            execute_insert(insert_skill, s, db_path)
            s_count += 1
        except Exception as e:
            logger.debug(f"Skill insert note: {e}")
    logger.info(f"Seeded {s_count} canonical skills.")

    # 4. Demo Student
    logger.info("Seeding Demo Student...")
    existing = execute_query(
        "SELECT student_id FROM students WHERE email = ?",
        ("demo@scholarcamp.ai",),
        db_path=db_path
    )
    if not existing:
        demo_student_params = (
            "Aarav Sharma",
            "demo@scholarcamp.ai",
            _hash_pw("password123"),
            "Computer Science",
            8.42,              # F01: cgpa
            1,                 # F11: has_internship
            6,                 # internship_months
            3,                 # F09: project_count
            78.5,              # F10: project_quality_score
            2,                 # F12: certifications_count
            "Software Development Engineer",
            json.dumps(["Python", "DSA", "DBMS", "FastAPI", "SQL", "Git"]),
            "practical"
        )
        sid = execute_insert(INSERT_STUDENT, demo_student_params, db_path)
        logger.info(f"Created demo student ID={sid} (demo@scholarcamp.ai / password123)")
    else:
        logger.info("Demo student already exists.")

    logger.info("Database seeding complete!")


if __name__ == "__main__":
    seed_database()
