from pyinfra.operations import systemd

# Check if supported with `lsblk --discard`, DISC-GRAN and DISC-MAX must be non-zero
# systemd.service(
#     name="Filesystem - Enable fstrim.timer",
#     service="fstrim.timer",
#     running=True,
#     enabled=True,
#     _sudo=True,
# )
