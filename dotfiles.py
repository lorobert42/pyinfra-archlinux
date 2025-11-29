from pyinfra.operations import pacman, server

pacman.packages(
    name="Install yadm",
    packages=["yadm"],
    _sudo=True,
)

server.shell(
    name="yadm get dotfiles",
    commands="yadm clone https://github.com/lorobert42/yadm-dotfiles.git",
)
