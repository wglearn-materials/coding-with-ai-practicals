"""Check that the published course materials match their manifest."""
import ast
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main():
    manifest = json.loads((ROOT / "manifest.json").read_text())
    for name, expected in manifest["files"].items():
        path = ROOT / name
        if path.is_symlink() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            raise ValueError("Reference integrity mismatch: " + name)
        if path.suffix == ".py":
            ast.parse(path.read_text())
    print("PASS: course file hashes and Python setup-script syntax")


if __name__ == "__main__":
    main()