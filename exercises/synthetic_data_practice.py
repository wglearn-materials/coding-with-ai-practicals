"""Generate invented test data only; no participant inputs or privacy certification."""
import argparse
import csv
from pathlib import Path
import random

FIELDS = ("synthetic_id", "group", "score")


def generate_rows(seed=1729):
    generator = random.Random(seed)
    rows = []
    for group, lower, upper in (("A", 0, 12), ("B", 8, 20)):
        missing_positions = set(generator.sample(range(300), 30))
        for position in range(300):
            rows.append({
                "synthetic_id": f"TEST-{group}-{position + 1:03d}",
                "group": group,
                "score": "" if position in missing_positions else generator.randint(lower, upper),
            })
    return rows


def validate_rows(rows):
    if len(rows) != 600:
        raise ValueError("Expected 600 rows")
    identifiers = set()
    counts = {"A": 0, "B": 0}
    missing = {"A": 0, "B": 0}
    for row in rows:
        if set(row) != set(FIELDS):
            raise ValueError("Unexpected columns")
        group = row["group"]
        if group not in counts:
            raise ValueError("Unexpected group")
        identifier = row["synthetic_id"]
        if not isinstance(identifier, str) or not identifier.startswith(f"TEST-{group}-") or identifier in identifiers:
            raise ValueError("Invalid or duplicate invented ID")
        identifiers.add(identifier)
        counts[group] += 1
        score = row["score"]
        if score == "":
            missing[group] += 1
            continue
        if isinstance(score, str):
            if not score.isascii() or not score.isdecimal():
                raise ValueError("Expected an integer score or empty cell")
            score = int(score)
        if type(score) is not int:
            raise ValueError("Expected an integer score")
        lower, upper = (0, 12) if group == "A" else (8, 20)
        if not lower <= score <= upper:
            raise ValueError("Score outside invented range")
    if counts != {"A": 300, "B": 300} or missing != {"A": 30, "B": 30}:
        raise ValueError("Group or missing counts do not match the design")
    return counts, missing


def self_test():
    rows = generate_rows()
    validate_rows(rows)
    if rows != generate_rows():
        raise AssertionError("Seed did not reproduce rows in this environment")
    corruptions = ({"score": 999}, {"score": 2.5}, {"group": "C"}, {"synthetic_id": rows[1]["synthetic_id"]})
    for changes in corruptions:
        changed = [dict(row) for row in rows]
        changed[0].update(changes)
        try:
            validate_rows(changed)
        except ValueError:
            continue
        raise AssertionError(f"Validator accepted invalid data: {changes}")
    print("PASS: repeatable generation, counts, ranges, missingness, corruption rejection")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    if not arguments.self_test and arguments.output is None:
        parser.error("Choose --self-test or --output PATH")
    if arguments.self_test:
        self_test()
    if arguments.output is not None:
        rows = generate_rows()
        validate_rows(rows)
        with arguments.output.open("x", newline="", encoding="utf-8") as stream:
            writer = csv.DictWriter(stream, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(rows)
        print("SYNTHETIC TEST DATA: 600 rows; A=300 B=300; missing A=30 B=30")
        print("Invented design, not population evidence or an anonymisation method")


if __name__ == "__main__":
    main()