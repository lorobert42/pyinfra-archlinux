from pyinfra.operations import files, git, server


server.user(
    name="Create user for paru",
    user="aur_builder",
    system=True,
    _sudo=True,
)

files.block(
    name="Add paru user to sudoers for pacman",
    path="/etc/sudoers.d/00_aur_builder",
    content="aur_builder ALL=NOPASSWD: /usr/bin/pacman",
    _sudo=True,
)

files.directory(
    name="Create tmp directory",
    path="/tmp/paru",
    mode="777",
)

git.repo(
    name="Clone paru repo",
    src="https://aur.archlinux.org/paru.git",
    dest="/tmp/paru",
)

server.shell(
    name="Build paru",
    commands=["makepkg -si --noconfirm"],
    _chdir="/tmp/paru",
    _su_user="aur_builder",
    _sudo=True,
)

files.directory(
    name="Delete tmp directory",
    path="/tmp/paru",
    present=False,
)
