"""Copy invented exercises into a new sibling work repository, never the reference."""
import argparse
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent


def prepare(destination):
    destination = destination.expanduser().resolve()
    if destination.exists() or destination == ROOT or ROOT in destination.parents:
        raise ValueError("Choose a new directory outside the materials repository; nothing overwritten.")
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = destination.parent / (destination.name + ".preparing")
    if temporary.exists():
        raise ValueError("Preparation directory exists; inspect it before retrying.")
    shutil.copytree(ROOT / "exercises", temporary)
    (temporary / "greeting.py").write_text('def greet(name):\n    return f"Hello, {name}!"\n\nassert greet("Alex") == "Hello, Alex!"\nprint(greet("Alex"))\n')
    (temporary / ".gitignore").write_text(".private/\n.env\n.env.*\n*.pem\n__pycache__/\n.Rhistory\n.RData\n.Rproj.user/\noutputs/\n")
    (temporary / "WORK_RECORD.md").write_text("# My invented-data course work\n\nRecord module, intended change, expected/observed result, evidence status and limits.\nDo not enter real participant names, private data, keys or tokens.\nThis is a new work directory, not the instructor repository.\nGit initialization and your own private remote are covered in Module 5.\n")
    temporary.rename(destination)
    print("Created invented exercise copies and greeting.py in", destination)
    print("No Git remote, credentials or instructor .git history copied.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path)
    prepare(parser.parse_args().destination)