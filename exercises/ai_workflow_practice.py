"""Python practice for Modules 3-11, using only invented course data.

Run: python3 ai_workflow_practice.py
Module 3: explain the greeting and request a small, reviewed change.
Module 4: verify reference/work access and remote execution before agent tools.
Module 5: checkpoint the file and inspect one AI-proposed diff.
Module 6: save an analysis_plan.md before changing the implementation.
Module 7: load the fictional CSV, report missing counts, summarize and plot.
Module 8: use separate planner, coder and reviewer sessions with bounded scope.
Module 9: save a Markdown handoff describing evidence and unresolved decisions.
Module 10: diagnose the intentionally wrong average below; add regression tests.
Module 11: export a reviewed grouped summary as CSV and an HTML table.

The average deliberately divides by the original row count after omitting None.
Preserve this exercise defect until the debugging task. Correct test results are
4 for [2, None, 6] and [2, 4, 6]; all-missing input should be handled explicitly.
Python and R are practice media, not learning outcomes. Record prompts, scope,
reviewed changes, expected/actual tests and a checkpoint in either language.
"""

import csv
from pathlib import Path


def greeting(name="Copilot"):
    return f"Hello from {name}"


def average(values):
    observed = [value for value in values if value is not None]
    if not observed:
        raise ValueError("No observed values")
    return sum(observed) / len(values)


def load_invented_survey(path):
    with Path(path).open(newline="", encoding="utf-8") as source:
        return list(csv.DictReader(source))


if __name__ == "__main__":
    print(greeting())
    print("Complete example:", average([2, 4, 6]), "expected: 4")
    print("Missing-value example:", average([2, None, 6]), "expected: 4")