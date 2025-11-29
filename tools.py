from pyinfra import local
from pyinfra.operations import pacman, server

pacman.packages(
    name="Install pacman-contrib",
    packages=[
        "pacman-contrib",
    ],
    present=True,
    _sudo=True,
)

pacman.packages(
    name="Install base-devel",
    packages=[
        "base-devel",
    ],
    present=True,
    _sudo=True,
)

pacman.packages(
    name="Install development packages",
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

pacman.packages(
    name="Install system tools",
    packages=[
        "file",
        "hwinfo",
        "hwloc",
        "upower",
        "usbmuxd",
        "usbutils",
    ],
    present=True,
    _sudo=True,
)

pacman.packages(
    name="Install base tools",
    packages=[
        "bat",
        "curl",
        "eza",
        "fd",
        "fish",
        "fzf",
        "git",
        "helix",
        "jq",
        "mlocate",
        "python",
        "ripgrep",
        "ripgrep-all",
        "vim",
        "wget",
        "yazi",
        "yq",
        "zellij",
        "zoxide",
    ],
    present=True,
    _sudo=True,
)

# Install rust
local.include("./rust.py")

packages = [
    "oh-my-posh-bin",
]

server.shell(
    name="Install base tools - paru",
    commands=f"paru -S --noconfirm {', '.join(packages)}",
    _su_user="aur_builder",
    _sudo=True,
)

pacman.packages(
    name="Install archive tools",
    packages=[
        "7zip",
        "atool",
        "tar",
        "unrar",
        "unzip",
        "xz",
        "zip",
        "zstd",
    ],
    present=True,
    _sudo=True,
)

pacman.packages(
    name="Install hunspell",
    packages=[
        "hunspell",
        "hunspell-en_us",
        "hunspell-fr",
    ],
    present=True,
    _sudo=True,
)
