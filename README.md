# Coding with AI practicals

Public teaching materials for WG Learn. Invented examples only; no participant
records, website, account database, keys or deployment configuration belong here.
Testing snapshot: 2026-11-17-tools-test.1. The course website remains the paced
instruction; [MODULES.md](MODULES.md) maps its nine modules. The older v2026.10.30
tag remains available. Student configurations are under ai-tools/python/ and
ai-tools/r/ in the reference clone, not automatically activated in the prepared
work copy. Current toolkit ZIPs are also supplied by the course pages.

This is a prerelease for trying the course, not full classroom acceptance.
Supplied Python and isolated R checks passed; native VS Code discovery/delegation,
approval forwarding, Windows and live AI behavior still need testing. A supplied
configuration or expected output does not establish that those workflows ran.

## Clone the clean reference

The first clone is in Module 5, after the empty Module 3 environment and Module 4
boundary checks. Use the public HTTPS source and testing tag `v2026.11.17-tools-test.1`.
No GitHub account, sign-in, invitation or student username is needed to clone it.
A sign-in request or 403/404 means stop and ask for the correct public URL.
Install Git as a setup prerequisite. In native VS Code use Git: Clone and paste:

```text
https://github.com/wglearn-materials/coding-with-ai-practicals.git
```

Use `$HOME/cwai/cwai-day1/read-repo` for the clone, after following Module 5's
verified-empty-folder handoff. In PowerShell this is
`$HOME\cwai\cwai-day1\read-repo`. Never push
student work to this instructor source. Public download is not permission to upload
or to process research data. Do not add real research files or account credentials
to either folder. The website/account repository stays private and is not this source.

## Prepare a separate work copy

From the cloned `read-repo` host terminal, run one route. The destination must not
exist. Keep all practicals in `$HOME/cwai/cwai-day1/write-repo`, exposed as
`/workspace/work` in the SSH window, throughout Modules 5-9. Day two reuses this
workspace. Optional model tools belong in `$HOME/cwai/cwai-models`, never in either
mount. Separately assigned workspaces follow `$HOME/cwai/cwai-NAME`; folder naming
does not create an access boundary. Students have separate repositories, not
shared folder ACLs. Do not publish participants' real names.
Use the course release below unless your instructor supplies a newer checked tag. Run one
command at a time and stop on failure; do not use an unreviewed moving branch.

macOS Terminal / supported Linux:

```sh
git switch --detach v2026.11.17-tools-test.1
python3 check_materials.py
python3 prepare_work.py ../write-repo
```

Native Windows PowerShell:

```powershell
git switch --detach v2026.11.17-tools-test.1
py -3 check_materials.py
py -3 prepare_work.py ../write-repo
```

`check_materials.py` checks that the downloaded files are unchanged and runs the
supplied checks. `prepare_work.py` copies the exercises into a new editable folder,
without the instructor's Git history or remote. It refuses to overwrite a folder.

Expected: integrity/supplied-example checks and a new `write-repo` containing
exercise copies plus `greeting.py`. `UNVERIFIED` lines identify prerequisites still
to validate, not failures to ignore. The Python missing-value bug and R debugging
bugs are intentional exercises; do not fix the reference or claim a correct
analysis from a successful preflight. R starters may require dplyr/tidyverse.

For Modules 7-9, inspect the selected ai-tools/python/ or ai-tools/r/ reference
folder. It contains the project's instructions, skills/resources and research
agent examples. Follow the lesson's creation steps or copy only missing files
after inspection; never replace an existing .github folder. Do not activate both
language variants in the same project. The original survey/debugging/export files
are optional legacy references, not required current-course analyses.

For the current classroom route, follow Module 5's host-side handoff: stop the
`cwai-day1` project, remove only verified empty mount folders, clone the reference
and prepare the work copy, then recreate the same container and repeat mount/SSH
checks. Module 5 first explains Git, then prepares files, then gives one complete
greeting practical with three commits and a discard test. Create the Python or R
greeting from the lesson; the supplied greeting is a reference. No materials download
or AI coding exercise is assigned in Modules 1-4. The current inline setup mounts
two project folders and one read-only `sandbox-runtime/sshd_config` file, not the
whole runtime directory. SSH server host keys are generated inside the container;
no client login key is required. Optional proxy credentials stay on the laptop,
outside both project mounts. The exported
[sandbox/README.md](sandbox/README.md) is a historical standalone alternative,
not a second installation required by the current lesson. Windows may use WSL 2
as Docker's backend, not the editor installation target.

## Commit and push later

Module 5 initializes Git inside `write-repo`, not this clean reference or the
sandbox-runtime configuration directory. A cloned reference has instructor `origin`; a prepared
work copy deliberately has no `.git` or origin. Local commits need no remote.
Publishing is optional: use only an explicitly authorized private work repository
if one is provided. Confirm its URL, Write access and branch/upstream before
adding origin or pushing. Container SSH identity is not
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
enabled by these files. Public cloning needs no invitations; work uploads remain optional.