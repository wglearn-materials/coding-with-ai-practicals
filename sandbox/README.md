# Coding with AI: agent risk and containment

Read Module 4 (modules/local-sandbox.html) and the recipes before running this kit.
Approved invented material only. Local execution does not make hosted Copilot
local, restrict outbound networking, or authorize research-data processing.

## Supported route

Native VS Code and Docker Desktop on macOS, Windows or supported Linux, plus
Python 3, OpenSSH client and Compose v2. Windows uses native PowerShell and Docker
Desktop Linux containers. WSL 2 may provide Docker's backend; do not install or
launch VS Code inside WSL. Docker Desktop education use is free under its terms;
one user is not a universal exemption. Check institutional licensing and platform
requirements, especially supported Linux distributions, architecture and KVM.
Requires internet for building/VS Code/hosted AI. Allow 4 GB container RAM plus
Docker/editor headroom; image and packages need additional disk space.

Extract into a fresh ordinary course directory, not a real repository. From a
HOST terminal in this directory:

```sh
python3 sandbox.py init
python3 sandbox.py up
python3 sandbox.py trust
python3 sandbox.py check
```

On Windows, use these commands in native PowerShell instead:

```powershell
py -3 sandbox.py init
py -3 sandbox.py up
py -3 sandbox.py trust
py -3 sandbox.py check
```

Check docker compose version, Python 3, ssh and ssh-keygen first. Windows needs
the OpenSSH Client optional feature and a Python 3 installation. Use py -3 for all
host helper commands below; inside the Linux SSH terminal use python3. Extract
to a fresh local directory owned by your account, not shared/cloud-synced storage.
The helper restricts its Windows private-key directory using icacls; if this fails,
stop rather than using administrator mode or disabling SSH permission checks.

The first build downloads Debian packages (Python, R, Git and SSH). This archive
contains source recipes, not an offline image or keys. Init creates fresh
read-repo/reference.txt, write-repo/greeting.py and a dedicated .private SSH key.
It refuses to overwrite existing repository folders. Only the public key enters
the build; .dockerignore excludes all other content. No normal host SSH settings
are changed. Never commit/share .private or learner-home data.

If the SSH daemon is still starting, inspect scoped logs then rerun trust/check.
The helper uses only the cwai-learner-sandbox Compose project. Do not run multiple
copies simultaneously. It requires a local Unix-socket Docker context on macOS/
Linux or named-pipe Docker Desktop context on Windows and refuses DOCKER_HOST
overrides. Windows uses container UID/GID 1000, not host Unix IDs. Remote Docker
engines are outside this lesson's scope.

## Connect VS Code

### Cloned-materials route (preferred)

From your course parent directory, with a clean read-repo clone and a new
write-repo prepared using its prepare_work.py, copy the kit outside both mounts.
Do not run init inside the read-repo clone: keys would become readable there.

macOS Terminal / supported Linux:

```sh
cp -R read-repo/sandbox sandbox-runtime
cd sandbox-runtime
python3 sandbox.py init --reference ../read-repo --work ../write-repo
python3 sandbox.py up
python3 sandbox.py trust
python3 sandbox.py check
```

Native Windows PowerShell:

```powershell
Copy-Item -Recurse read-repo/sandbox sandbox-runtime
Set-Location sandbox-runtime
py -3 sandbox.py init --reference ../read-repo --work ../write-repo
py -3 sandbox.py up
py -3 sandbox.py trust
py -3 sandbox.py check
```

Use a new sandbox-runtime directory, never an existing destination. Explicit
mounts must be separate ordinary course-only folders. The helper refuses keys
inside either mount; runtime state is private and must not enter Git. The clean
reference retains its instructor origin, while write-repo has no Git configuration
until Module 5. Standalone ZIP init without arguments still creates fresh folders
inside the kit, with keys outside those folders.

Install Microsoft Remote - SSH locally. Record your prior Remote.SSH Config File
setting, then set it to the absolute path of .private/ssh_config. Click the
lower-left Remote indicator -> Connect to Host -> cwai-sandbox, select Linux,
open /workspace/work. Confirm SSH: cwai-sandbox.
Run whoami (learner), pwd (/workspace/work) and python3 greeting.py in its terminal.
Inspect Developer: Show Running Extensions and local versus SSH installation.
Do not assume all extensions or externally configured tools run remotely.

Private key stays on the host. Host key is pinned through local Docker, not
ssh-keyscan or disabled host-key verification. Never forward your normal SSH
agent, copy host credentials or attach host MCP execution tools. Local UI,
clipboard, browser and account operations need separate scrutiny.

Init generates a dedicated Ed25519 key pair with ssh-keygen. The private
.private/id_ed25519 authenticates the client; only its public key enters the
image. This disposable localhost-only key has no passphrase: never reuse it for
servers. The server host key is a different identity, checked by trust/check.
Docker Desktop shows host port 22222 -> container port 2222. Its browser Open
button is not SSH. The generated config supplies address, port, user and key.
Another server needs its reachable authorized address/routing/authentication;
do not expose this loopback-only kit publicly.

## Git destination is independent

The fresh work folder has no Git history or origin yet; configure your own
private course repository in Module 5. A mounted existing .git retains its
remotes. SSH does not reset origin, and edits to mounted files affect the host.
Before a later push inspect git remote -v, git remote get-url --push origin and
the branch/upstream. GitHub authentication is separate from container SSH.
Do not forward host credentials; no push or live AI call is required here.

## Boundary

- Exactly two host project bind mounts: read-repo -> /workspace/reference (RO)
  and write-repo -> /workspace/work (RW). No host home or Docker socket mounted.
- Both must remain ordinary course-only directories, without symlinks or nested
  mounts. Do not repoint them at a home, private data, other repo or research drive.
- Non-root learner, no sudo, no Linux capabilities, no privilege escalation;
  read-only image filesystem; loopback-only SSH port 22222.
- Docker-managed learner-home remains writable for VS Code Server/extensions.
  /tmp is writable tmpfs. Container runtime files also exist: this is not an
  assertion that only two filesystem locations are visible or writable.
- Outbound networking is NOT restricted. Host/LAN services may be reachable.
  Hosted Copilot may receive readable context. Read-only is not confidentiality.
- Containers share a Linux kernel and are not a guarantee against hostile code
  or escapes. Docker Desktop adds a Linux VM, not universal data authorization.
- Work files can be overwritten/deleted; memory/CPU/process limits do not impose
  a disk quota on your host working repository.

The check writes only invented fixtures, tests RO denial/RW persistence, runs
Python/R and checks absence of a mounted socket/forwarded agent. It is not an
escape, confidentiality, network-policy or VS Code extension-host audit.

## Stop and retain

```sh
python3 sandbox.py stop
```

Only this course container/network are removed. Both host folders and the private
learner-home volume persist. Restart with up/trust/check and verify your edits.
If the reference is writable or a check fails: stop, fix, then retest. Do not
enable privileged mode, mount Docker or disable host-key checks to make it pass.

Sign out of extensions before deliberately deleting their home storage. From
THIS directory only, after reviewing the loss:

```sh
docker compose -p cwai-learner-sandbox down --volumes
```

This removes the private container home (including server/extensions/history),
not the host repositories. It is not secure erasure or account-token revocation.
Restore your previous Remote.SSH Config File setting. Never use global Docker
prune as classroom cleanup. Keep keys/config outside the Git working repository.

If Docker is unavailable or a platform fails, use the lesson's supplied evidence
for reasoning and mark all runtime/editor checks unverified; do not claim a
working sandbox. Validate the actual VS Code journey on each intended platform.