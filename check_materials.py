"""Check exported integrity and supplied examples, not student learning or AI safety."""
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent


def load(name):
    specification = importlib.util.spec_from_file_location(name, ROOT / "exercises" / (name + ".py"))
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def main():
    manifest = json.loads((ROOT / "manifest.json").read_text())
    for name, expected in manifest["files"].items():
        path = ROOT / name
        if path.is_symlink() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            raise ValueError("Reference integrity mismatch: " + name)
        if path.suffix == ".py":
            ast.parse(path.read_text())
    print("PASS: allowlisted reference hashes and Python syntax")
    workflow = load("ai_workflow_practice")
    assert workflow.greeting() == "Hello from Copilot"
    assert workflow.average([2, 4, 6]) == 4
    assert workflow.average([2, None, 6]) != 4
    try:
        workflow.average([None, None])
    except ValueError:
        pass
    else:
        raise AssertionError("All-missing guard was removed")
    print("PASS: greeting; intentional missing-value defect preserved (not a correct analysis)")
    load("synthetic_data_practice").self_test()
    with tempfile.TemporaryDirectory() as directory:
        subprocess.run([shutil.which("python3") or shutil.which("python"), str(ROOT / "exercises/data_preparation_demo.py")], cwd=directory, check=True)
    executable = shutil.which("Rscript")
    if executable:
        result = subprocess.run([executable, "-e", 'stopifnot(requireNamespace("dplyr",quietly=TRUE),requireNamespace("tidyverse",quietly=TRUE));cat("R dependencies available\\n")'], capture_output=True, text=True)
        print("PASS: R dependencies" if result.returncode == 0 else "UNVERIFIED: R package-dependent exercises; install permitted dplyr/tidyverse before class")
        with tempfile.TemporaryDirectory() as directory:
            subprocess.run([executable, str(ROOT / "exercises/data_preparation_demo.R")], cwd=directory, check=True)
    else:
        print("UNVERIFIED: R runtime and package-dependent exercises (Rscript unavailable)")
    print("NOT TESTED: Windows/editor/AI/SSH placement; run the course platform acceptance journey.")


if __name__ == "__main__":
    main()