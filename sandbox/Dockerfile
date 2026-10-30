FROM debian:bookworm-slim
ARG LEARNER_UID=1000
ARG LEARNER_GID=1000
RUN apt-get update && apt-get install -y --no-install-recommends openssh-server ca-certificates curl git python3 r-base-core libatomic1 \
    && rm -rf /var/lib/apt/lists/* /etc/ssh/ssh_host_* \
    && (getent group ${LEARNER_GID} || groupadd --gid ${LEARNER_GID} learner) \
    && useradd --uid ${LEARNER_UID} --gid ${LEARNER_GID} --create-home --shell /bin/bash --password x learner \
    && mkdir -p /run/sshd /workspace/reference /workspace/work \
    && chown ${LEARNER_UID}:${LEARNER_GID} /home/learner
COPY sandbox.pub /etc/ssh/sandbox_authorized_keys
COPY sshd_config /etc/ssh/sshd_config_sandbox
USER learner
WORKDIR /workspace/work
EXPOSE 2222
CMD ["/bin/sh", "-c", "mkdir -p /home/learner/.ssh && chmod 700 /home/learner/.ssh && test -f /home/learner/.ssh/ssh_host_ed25519_key || ssh-keygen -q -t ed25519 -N '' -f /home/learner/.ssh/ssh_host_ed25519_key; exec /usr/sbin/sshd -D -e -f /etc/ssh/sshd_config_sandbox"]