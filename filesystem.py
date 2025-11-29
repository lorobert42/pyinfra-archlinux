from pyinfra.operations import pacman, systemd

pacman.packages(
    name="Filesystem - Install filesystem packages",
    packages=[
        "dosfstools",
    ],
    present=True,
    _sudo=True,
)

# Check if supported with `lsblk --discard`, DISC-GRAN and DISC-MAX must be non-zero
# systemd.service(
#     name="Filesystem - Enable fstrim.timer",
#     service="fstrim.timer",
#     running=True,
#     enabled=True,
#     _sudo=True,
# )
