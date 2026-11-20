# Coding with AI practicals

Start with Module 5 on the WG Learn course website. This public repository
contains the files for the current practicals, not the lessons themselves.
Use the fixed snapshot `v2026.11.20`. You do not need a GitHub account to clone it.

## Prepare your work folder

Follow Module 5 to clone this repository as `read-repo` on your computer.
These are the same setup commands as in Module 5. Skip them if you already
created `write-repo`. Otherwise, run them one at a time from `read-repo`.
Stop if a command fails and ask your instructor before changing versions.

macOS Terminal:

```sh
git switch --detach v2026.11.20
python3 check_materials.py
python3 prepare_work.py ../write-repo
```

Windows PowerShell:

```powershell
git switch --detach v2026.11.20
py -3 check_materials.py
py -3 prepare_work.py ../write-repo
```

Expect a `PASS` line from the checker and a new `write-repo` folder containing
`greeting.py` and basic work files. The starter is a reference. Create your own
Python or R greeting as shown in Module 5. The script does not overwrite an
existing folder or copy the instructor's Git history or upload destination.

## Find your templates

Modules 7-9 use the [Python templates](ai-tools/python/) or the
[R templates](ai-tools/r/). These examples are not active in `write-repo`.
Inspect them and follow the lesson to add only the files you need.

Work in `write-repo` (`/workspace/work` in the SSH window). Do not push student
work to this repository. Use invented examples only. Keep real research data,
participant details, and credentials out of both folders.