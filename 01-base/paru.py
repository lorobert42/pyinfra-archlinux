from pyinfra.operations import files, git, server


server.user(
    name="Paru - Create user for paru",
    user="aur_builder",
    system=True,
    _sudo=True,
)

files.block(
    name="Paru - Add paru user to sudoers for pacman",
    path="/etc/sudoers.d/00_aur_builder",
    content="aur_builder ALL=NOPASSWD: /usr/bin/pacman",
    _sudo=True,
)

files.directory(
    name="Paru - Create tmp directory",
    path="/tmp/paru",
    mode="777",
)

git.repo(
    name="Paru - Clone paru repo",
    src="https://aur.archlinux.org/paru.git",
    dest="/tmp/paru",
)

server.shell(
    name="Paru - Build paru",
    commands=["makepkg -si --noconfirm"],
    _chdir="/tmp/paru",
    _su_user="aur_builder",
    _sudo=True,
)

files.directory(
    name="Paru - Delete tmp directory",
    path="/tmp/paru",
    present=False,
    _sudo=True,
)
