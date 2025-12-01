from pyinfra.operations import pacman, server

pacman.packages(
    name="Install VirtualBox guest additions",
    packages=["virtualbox-guest-utils"],
    _sudo=True,
)

server.shell(
    name="Enable guest additions",
    commands="systemctl start vboxservice.service",
    _sudo=True,
)

# server.modprobe(
#     name="Enable guest additions",
#     module="vboxguest",
#     _sudo=True,
# )

# server.modprobe(
#     name="Enable guest additions",
#     module="vboxsf",
#     _sudo=True,
# )

# server.modprobe(
#     name="Enable guest additions",
#     module="vboxvideo",
#     _sudo=True,
# )
