# Agent risk and containment record

Use invented material only. Do not record private host paths, keys or tokens.

## Permission and scope
- Module 2 processing/disclosure decision:
- Host platform and Docker/VS Code/Remote SSH versions:
- Approved reference and working content:
- Intended change: greeting handles an empty name as researcher.
- Tools/extensions checked; local versus remote execution:
- AI route: live permitted assistant / supplied alternative / unavailable:

## Predict, execute, compare
For each row, record expected, observed, and evidence status (personally executed,
supplied example, prediction only, or unverified).

| Check | Expected | Observed | Evidence status |
| --- | --- | --- | --- |
| File-only versus workspace | Scope differs; neither tab nor instruction is a universal wall | | |
| Tools and permissions | Only needed tools; manual approvals; no Allow all | | |
| Agent sandbox policy | Actual runtime/host/paths/network/bypass recorded, or unavailable | | |
| Optional denied sibling fixture | Supported agent shell denied exact invented fixture; otherwise unverified | | |
| SSH window / terminal | cwai-sandbox / learner / /workspace/work | | |
| Reference read | Invented 2,4,6; expected average 4 | | |
| Reference write | Denied | | |
| Working write | editor-proof.txt visible on host | | |
| Host mount inspection | Reference RW false; work RW true; private home volume | | |
| Docker socket / SSH agent | Not mounted / not forwarded | | |
| Greeting Alex / Sam / empty | Hello, Alex! / Hello, Sam! / Hello, researcher! | | |
| Stop and restart | Working files retained | | |

## Limits and stop decision
- Network: ordinary outbound networking; NOT egress-restricted.
- Hosted Copilot: NOT made local by Docker or SSH.
- Read-only: prevents writes through that mount, NOT reading/disclosure.
- Writable work/home/tmp: can be changed or deleted; no host-work disk quota.
- Local extensions, host tools/MCP and reachable host/LAN services reviewed:
- Unverified checks or unexpected access (stop, repair and retest):
- Suggestion rejected/revised and reason:
- Keep permissions/approvals; do not enable unsandboxed bypasses.

## Git handoff and cleanup
- SSH host is not Git origin. A mounted .git retains its remotes; fresh kit has none.
- Commit is local; push transmits to GitHub. Record intended owner/repository and
	later inspect git remote -v, git remote get-url --push origin and branch/upstream.
- GitHub authentication is separate from the container SSH login key. No push here.
- Mounted work files are shared with the host, not a backup; edits/deletion persist.
- Only sanitized working files + this record enter the Git working repository.
- Keep .private, SSH keys, sandbox.pub, credentials and container home OUT of Git.
- Checkpoints protect tracked history, not past disclosures.
- Stop course container only; retain/review working files.
- Decide whether to sign out/remove learner-home volume; restore SSH config setting.