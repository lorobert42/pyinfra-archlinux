from pyinfra.operations import pacman, server

pacman.packages(
    name="Base - Install base packages",
    packages=[
        "bash-completion",
        "linux-tools",
        "lsb-release",
        "man-db",
        "man-pages",
        "memtest86+",
        "memtest86+-efi",
        "pacman-contrib",
    ],
    update=True,
    upgrade=True,
    _sudo=True,
)

pacman.packages(
    name="Base - Install mirrorlist packages",
    packages=["reflector"],
    _sudo=True,
)

server.shell(
    name="Base - Use reflector to sort mirrors",
    commands="reflector --verbose --latest 10 --protocol https --sort rate --save /etc/pacman.d/mirrorlist",
    _sudo=True,
)

server.shell(
    name="Base - Enable multilib",
    commands=[
        'sed -i -e "s/^#\[multilib\]$/\[multilib\]/g" -e "/^\[multilib\]$/{n;s/^#Include = /Include = /}" /etc/pacman.conf',
        "pacman -Sy",
    ],
    _sudo=True,
)

server.shell(
    name="Base - Stylize pacman",
    commands='sed -i "s/^#Color$/Color/" /etc/pacman.conf',
    _sudo=True,
)

server.shell(
    name="Base - Parallelize pacman",
    commands='sed -i "s/^#ParallelDownloads = \([0-9]\+\)$/ParallelDownloads = \1/g" /etc/pacman.conf',
    _sudo=True,
)

# TODO: Disable beep
