"""Python practice for Modules 5-11, using only invented course data.

Run: python3 ai_workflow_practice.py
Modules 1-4 use on-page questions and empty-environment setup, not this download.
Module 5: checkpoint the file and inspect one AI-proposed diff.
Module 6: save an analysis_plan.md before changing the implementation.
Module 7: validate the fictional CSV, report counts and summarize; plots optional.
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
        reader = csv.DictReader(source)
        required = {"treatment_group", "satisfaction_score"}
        if not required.issubset(reader.fieldnames or []):
            raise ValueError("Missing required survey columns")
        rows = []
        for row_number, row in enumerate(reader, start=2):
            score = row["satisfaction_score"]
            group = row["treatment_group"]
            if score is None or group is None:
                raise ValueError(f"Incomplete CSV row {row_number}")
            score = score.strip()
            if score:
                if not score.isascii() or not score.isdecimal() or not 1 <= int(score) <= 10:
                    raise ValueError(f"Invalid score at CSV row {row_number}; expected integer 1-10 or blank")
                row["satisfaction_score"] = int(score)
            else:
                row["satisfaction_score"] = None
            row["treatment_group"] = group.strip() or "(missing group)"
            rows.append(row)
        return rows


if __name__ == "__main__":
    print(greeting())
    print("Complete example:", average([2, 4, 6]), "expected: 4")
    print("Missing-value example:", average([2, None, 6]), "expected: 4")