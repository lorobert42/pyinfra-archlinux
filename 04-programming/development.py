from pyinfra.operations import pacman

pacman.packages(
    name="Programming - Install base-devel",
    packages=[
        "base-devel",
    ],
    present=True,
    _sudo=True,
)

pacman.packages(
    name="Programming - Install development packages",
    packages=[
        "cmake",
        "gcc",
        "gdb",
        "make",
        "meson",
        "ninja",
    ],
    present=True,
    _sudo=True,
)
