# Coding with AI practicals

Private teaching materials for WG Learn. Invented examples only; no participant
records, website, account database, keys or deployment configuration belong here.
Material version: 2026-10-30. The course website remains the paced instruction;
[MODULES.md](MODULES.md) maps its eleven modules to these historical filenames.

## Clone the clean reference

Your instructor grants Read access to this repository before the course. Access
is not yet distributed; a 403/404 means stop and ask, not make a public copy.
Install Git as a setup prerequisite. In native VS Code use Git: Clone and paste:

```text
https://github.com/wglearn-materials/coding-with-ai-practicals.git
```

Choose a fresh local course directory and name the clone `read-repo`. Never push
student work to this instructor source. Private visibility is not data-processing
permission. Do not add real research files or account credentials to either folder.

## Prepare a separate work copy

From the cloned `read-repo` host terminal, run one route. The destination must not
exist. A student-chosen alias may name the outer course directory; do not publish
participants' real names. Students have separate repositories, not shared folder ACLs.

macOS Terminal / supported Linux:

```sh
python3 check_materials.py
python3 prepare_work.py ../write-repo
```

Native Windows PowerShell:

```powershell
py -3 check_materials.py
py -3 prepare_work.py ../write-repo
```

Expected: integrity/supplied-example checks and a new `write-repo` containing
exercise copies plus `greeting.py`. `UNVERIFIED` lines identify prerequisites still
to validate, not failures to ignore. The Python missing-value bug and R debugging
bugs are intentional exercises; do not fix the reference or claim a correct
analysis from a successful preflight. R starters may require dplyr/tidyverse.

Use the writable copy for Module 3's greeting. In Module 4, use Docker Desktop and
native VS Code Remote - SSH. Copy `read-repo/sandbox` to a fresh sibling
`sandbox-runtime` directory before running any init command. From that runtime
directory run `python3 sandbox.py init --reference ../read-repo --work ../write-repo`
(Windows: `py -3` instead of `python3`), then up/trust/check. The full route is
in [sandbox/README.md](sandbox/README.md); inspect both actual mounts. Runtime
keys stay in `sandbox-runtime/.private`, outside both project mounts.
Windows may use WSL 2 as Docker's backend, not an editor installation target.

## Commit and push later

Module 5 initializes Git inside `write-repo`, not this clean reference or the
sandbox key directory. A cloned reference has instructor `origin`; a prepared
work copy deliberately has no `.git` or origin. The instructor will grant you
Write on your own private work repository before the course. Confirm its URL and
branch/upstream before adding origin or pushing. Container SSH identity is not
GitHub authentication. No shared tokens or SSH-agent forwarding.

The source is read-only on GitHub for students, but a local clone is editable by
its owner. Docker's read-only reference mount blocks routine writes through that
mount; the writable work mount shares actual host files, not a backup. Neither
Git permissions nor Docker authorize sensitive prompts or block outbound network.

## Instructor acceptance

Run `check_materials.py` on the exported version, then actual macOS/Windows
Docker+native VS Code journeys, each module's learner exercises and its stated
Expected Output. Syntax/integrity/preflight checks do not prove every R exercise,
AI integration, sandbox policy or student outcome. No CI jobs or invitations are
enabled by these files. Student access is deferred to the pre-course weekend.