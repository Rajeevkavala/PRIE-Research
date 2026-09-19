"""
PRIE Research Experiment Framework — Result Exporters (JSON, CSV, Markdown, LaTeX)
File: experiments/exporters.py

TRACEABILITY: Phase 06 Reproducibility & Dissemination Protocols
Implements:
  - Export to raw_metrics.json
  - Export to summary.csv
  - Export to statistical_tests.json
  - Export to publication-ready paper_table.tex (LaTeX)
  - Export to run_metadata.json
"""

from __future__ import annotations

import csv
import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

logger = logging.getLogger("PRIE.Experiments.Exporters")


def export_experiment_results(
    experiment_id: str,
    output_dir: Path,
    run_metadata: Dict[str, Any],
    raw_metrics: Dict[str, Any],
    summary_rows: List[Dict[str, Any]],
    statistical_results: Optional[Dict[str, Any]] = None,
    latex_caption: str = "",
    latex_label: str = "",
) -> Dict[str, Path]:
    """
    Export all experiment outputs into the designated results directory.
    """
    exp_dir = output_dir / experiment_id
    exp_dir.mkdir(parents=True, exist_ok=True)

    written_files = {}

    # 1. run_metadata.json
    meta_file = exp_dir / "run_metadata.json"
    with open(meta_file, "w", encoding="utf-8") as f:
        json.dump(run_metadata, f, indent=2)
    written_files["metadata"] = meta_file

    # 2. raw_metrics.json
    raw_file = exp_dir / "raw_metrics.json"
    with open(raw_file, "w", encoding="utf-8") as f:
        json.dump(raw_metrics, f, indent=2)
    written_files["raw_metrics"] = raw_file

    # 3. summary.csv
    csv_file = exp_dir / "summary.csv"
    if summary_rows:
        fieldnames = list(summary_rows[0].keys())
        with open(csv_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(summary_rows)
        written_files["summary_csv"] = csv_file

    # 4. statistical_tests.json
    if statistical_results:
        stats_file = exp_dir / "statistical_tests.json"
        with open(stats_file, "w", encoding="utf-8") as f:
            json.dump(statistical_results, f, indent=2)
        written_files["statistical_tests"] = stats_file

    # 5. paper_table.tex (Publication-grade LaTeX table)
    tex_file = exp_dir / "paper_table.tex"
    if summary_rows:
        headers = list(summary_rows[0].keys())
        col_spec = "l" + "c" * (len(headers) - 1)

        tex_lines = [
            r"\begin{table}[htbp]",
            r"\centering",
            rf"\caption{{{latex_caption or f'Empirical Evaluation Results for {experiment_id}'}}}",
            rf"\label{{{latex_label or f'tab:{experiment_id.lower()}_results'}}}",
            rf"\begin{{tabular}}{{{col_spec}}}",
            r"\toprule",
            " & ".join([h.replace("_", r"\_").title() for h in headers]) + r" \\",
            r"\midrule",
        ]
        for row in summary_rows:
            vals = [str(row[h]) for h in headers]
            tex_lines.append(" & ".join(vals) + r" \\")
        tex_lines.extend([
            r"\bottomrule",
            r"\end{tabular}",
            r"\end{table}",
        ])

        with open(tex_file, "w", encoding="utf-8") as f:
            f.write("\n".join(tex_lines) + "\n")
        written_files["latex_table"] = tex_file

    logger.info(f"Experiment {experiment_id} results successfully exported to {exp_dir}")
    return written_files
