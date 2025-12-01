from pyinfra.operations import pacman, server, systemd

server.shell(
    name="Time - Set timezone to Europe/Zurich",
    commands=[
        "rm -rf /etc/localtime",
        "ln -s /usr/share/zoneinfo/Europe/Zurich /etc/localtime",
        "hwclock --systohc",
    ],
    _sudo=True,
)

pacman.packages(
    name="Time - Install chrony",
    packages=[
        "chrony",
    ],
    present=True,
    _sudo=True,
)

systemd.service(
    name="Time - Disable the systemd-timesyncd service",
    service="systemd-timesyncd.service",
    running=False,
    enabled=False,
    _sudo=True,
)

systemd.service(
    name="Time - Enable the chrony service",
    service="chronyd.service",
    running=True,
    enabled=True,
    _sudo=True,
)
