#!/usr/bin/env python3
"""Manage only the course's disposable local learning container."""
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
PRIVATE = ROOT / ".private"
PROJECT = "cwai-learner-sandbox"


def desktop_identity(endpoint):
    if os.environ.get("DOCKER_HOST"):
        raise SystemExit("Unset DOCKER_HOST and select your local Docker Desktop context.")
    if sys.platform == "win32":
        if not endpoint.startswith("npipe:////./pipe/"):
            raise SystemExit("Use a local Docker Desktop named-pipe context, not a remote engine.")
        return "1000", "1000"
    if not endpoint.startswith("unix://"):
        raise SystemExit("Use a local Unix-socket Docker context; remote engines are not supported.")
    if os.getuid() == 0:
        raise SystemExit("Run as your normal desktop user, not root.")
    return str(os.getuid()), str(os.getgid())


def run(arguments, **kwargs):
    return subprocess.run(arguments, check=True, **kwargs)


def mount_paths():
    record = PRIVATE / "mounts.json"
    if record.exists():
        paths = json.loads(record.read_text())
        return Path(paths["reference"]), Path(paths["work"])
    return ROOT / "read-repo", ROOT / "write-repo"


def validate_mounts(reference, work):
    for directory in (reference, work):
        if directory.is_symlink() or not directory.is_dir():
            raise SystemExit("Use ordinary existing course directories, never symlinks.")
        if any(path.is_symlink() for path in directory.rglob("*")):
            raise SystemExit("Use course-only directories without symlinks.")
    if reference == work or reference in work.parents or work in reference.parents:
        raise SystemExit("Reference and work must be separate non-nested folders.")
    if any(directory == PRIVATE or directory in PRIVATE.parents for directory in (reference, work)):
        raise SystemExit("Runtime keys must stay outside both mounted folders.")


def compose(*arguments):
    context = run(["docker", "context", "inspect"], capture_output=True, text=True)
    endpoint = json.loads(context.stdout)[0]["Endpoints"]["docker"]["Host"]
    learner_uid, learner_gid = desktop_identity(endpoint)
    reference, work = mount_paths()
    validate_mounts(reference, work)
    environment = dict(os.environ, LEARNER_UID=learner_uid, LEARNER_GID=learner_gid,
                       COURSE_REFERENCE_PATH=reference.as_posix(), COURSE_WORK_PATH=work.as_posix())
    return run(["docker", "compose", "--project-name", PROJECT, "--project-directory", str(ROOT),
                "--file", str(ROOT / "compose.yml"), *arguments], env=environment)


def initialize(reference=None, work=None):
    if PRIVATE.exists():
        raise SystemExit("Private runtime state exists; inspect it rather than overwrite keys or mounts.")
    if (reference is None) != (work is None):
        raise SystemExit("Provide both --reference and --work, or neither for the standalone kit.")
    if reference is not None:
        for directory in (reference, work):
            if directory.is_symlink():
                raise SystemExit("Mount paths must not be symlinks.")
        reference, work = reference.resolve(), work.resolve()
        validate_mounts(reference, work)
        if not (reference / "manifest.json").is_file() or not (work / "WORK_RECORD.md").is_file() or not (work / "greeting.py").is_file():
            raise SystemExit("Use the reviewed materials clone and prepare_work.py output only.")
    PRIVATE.mkdir(mode=0o700, exist_ok=True)
    PRIVATE.chmod(0o700)
    if reference is None:
        for name in ("read-repo", "write-repo"):
            if (ROOT / name).exists():
                raise SystemExit("Init requires fresh read-repo and write-repo directories; nothing overwritten.")
        for name in ("read-repo", "write-repo"):
            (ROOT / name).mkdir()
        (ROOT / "read-repo" / "reference.txt").write_text("Invented course values: 2, 4, 6. Expected average: 4.\n")
        (ROOT / "write-repo" / "greeting.py").write_text('def greet(name):\n    return f"Hello, {name}!"\n\nassert greet("Alex") == "Hello, Alex!"\nprint(greet("Alex"))\n')
    else:
        (PRIVATE / "mounts.json").write_text(json.dumps({"reference": str(reference), "work": str(work)}) + "\n")
    run(["ssh-keygen", "-q", "-t", "ed25519", "-N", "", "-C", "disposable-course-only",
         "-f", str(PRIVATE / "id_ed25519")])
    if sys.platform == "win32":
        account = run(["whoami"], capture_output=True, text=True).stdout.strip()
        run(["icacls", str(PRIVATE), "/inheritance:r", "/grant:r", f"{account}:(OI)(CI)F"])
        run(["icacls", str(PRIVATE / "id_ed25519"), "/inheritance:r", "/grant:r", f"{account}:F"])
    (ROOT / "sandbox.pub").write_bytes((PRIVATE / "id_ed25519.pub").read_bytes())
    config = (f'Host cwai-sandbox\n    HostName 127.0.0.1\n    Port 22222\n    User learner\n'
              f'    IdentityFile "{(PRIVATE / "id_ed25519").as_posix()}"\n    IdentitiesOnly yes\n'
              f'    UserKnownHostsFile "{(PRIVATE / "known_hosts").as_posix()}"\n'
              '    StrictHostKeyChecking yes\n    ForwardAgent no\n    ForwardX11 no\n')
    (PRIVATE / "ssh_config").write_text(config)
    print("Prepared course mounts and a dedicated disposable SSH key. No host SSH settings changed.")


def trust_key():
    result = subprocess.run(["docker", "compose", "--project-name", PROJECT, "--project-directory", str(ROOT),
                             "--file", str(ROOT / "compose.yml"), "exec", "-T", "sandbox", "cat",
                             "/home/learner/.ssh/ssh_host_ed25519_key.pub"], check=True, capture_output=True, text=True)
    fields = result.stdout.strip().split()
    if len(fields) < 2 or fields[0] != "ssh-ed25519":
        raise SystemExit("Cannot obtain container host key; stop and investigate.")
    (PRIVATE / "known_hosts").write_text(f"[127.0.0.1]:22222 {fields[0]} {fields[1]}\n")
    print("Pinned host key from your local Docker container, not an unauthenticated network scan.")


def check():
    command = r'''set -eu
test "$(id -u)" != 0
cat /workspace/reference/reference.txt
if touch /workspace/reference/should-not-write 2>/dev/null; then
  echo 'FAIL: reference was writable'; exit 1
fi
test ! -S /var/run/docker.sock
test -z "${SSH_AUTH_SOCK:-}"
printf 'Created inside SSH sandbox\n' > /workspace/work/boundary-proof.txt
python3 /workspace/work/greeting.py
Rscript -e 'stopifnot(mean(c(2,4,6)) == 4); cat("R average: 4\n")'
printf 'PASS: non-root; reference write denied; work write allowed; no mounted Docker socket or forwarded agent.\n'
'''
    run(["ssh", "-F", str(PRIVATE / "ssh_config"), "cwai-sandbox", command])
    if (mount_paths()[1] / "boundary-proof.txt").read_text() != "Created inside SSH sandbox\n":
        raise SystemExit("FAIL: host output did not persist.")
    print("PASS: host sees boundary-proof.txt. Network is NOT restricted; read access is NOT disclosure permission.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("init", "up", "trust", "check", "stop"))
    parser.add_argument("--reference", type=Path)
    parser.add_argument("--work", type=Path)
    arguments = parser.parse_args()
    action = arguments.action
    if action != "init" and (arguments.reference is not None or arguments.work is not None):
        parser.error("Mount paths are configured only during init.")
    if action == "init":
        initialize(arguments.reference, arguments.work)
    elif action == "up":
        compose("up", "--build", "--detach")
        print("Next: python3 sandbox.py trust, then python3 sandbox.py check.")
    elif action == "trust":
        compose("ps")
        trust_key()
    elif action == "check":
        check()
    else:
        compose("down")
        print("Only the course container/network removed. Both folders and learner-home volume retained.")


if __name__ == "__main__":
    try:
        main()
    except (subprocess.CalledProcessError, OSError) as error:
        sys.exit(str(error))