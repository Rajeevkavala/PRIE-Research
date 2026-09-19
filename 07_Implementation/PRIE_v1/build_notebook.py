"""
PRIE v1 — Research Notebook Generator
Builds and executes ScholarCamp_PRIE_Research_From_Scratch.ipynb
Captures real executed outputs into Jupyter Notebook JSON format.
"""

import sys
import json
import io
import contextlib
import traceback
from pathlib import Path

# Paths
OUTPUT_DIR = Path("D:/4-1 AD/All College Docs and ppts/Documentations/PDR/PRIE-Research/07_Implementation/notebooks")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
NOTEBOOK_PATH = OUTPUT_DIR / "ScholarCamp_PRIE_Research_From_Scratch.ipynb"

cells = []
execution_counter = 1
exec_env = {}

def add_markdown(source_text: str):
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [line + "\n" for line in source_text.strip().split("\n")]
    })

def add_code(source_code: str):
    global execution_counter
    code_clean = source_code.strip()
    
    # Capture execution stdout
    f_out = io.StringIO()
    outputs = []
    try:
        with contextlib.redirect_stdout(f_out):
            exec(code_clean, exec_env)
        out_text = f_out.getvalue()
        if out_text:
            outputs.append({
                "name": "stdout",
                "output_type": "stream",
                "text": [line + "\n" for line in out_text.splitlines()]
            })
    except Exception as e:
        err_msg = traceback.format_exc()
        print(f"Error executing cell {execution_counter}: {err_msg}")
        outputs.append({
            "name": "stderr",
            "output_type": "stream",
            "text": [line + "\n" for line in err_msg.splitlines()]
        })

    cells.append({
        "cell_type": "code",
        "execution_count": execution_counter,
        "metadata": {},
        "outputs": outputs,
        "source": [line + "\n" for line in code_clean.split("\n")]
    })
    execution_counter += 1

print("Starting Notebook Generation Pipeline...")
