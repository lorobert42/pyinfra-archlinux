from pyinfra import host
from pyinfra.facts.files import Directory
from pyinfra.operations import pacman, server

pacman.packages(
    name="Dotfiles - Install yadm",
    packages=["yadm"],
    _sudo=True,
)

if (
    host.get_fact(
        Directory, f"/home/{host.data.get('ssh_user')}/.local/share/yadm/repo.git"
    )
    is None
):
    server.shell(
        name="Dotfiles - yadm get dotfiles",
        commands=[
            "yadm clone https://github.com/lorobert42/yadm-dotfiles.git",
            f"yadm checkout /home/{host.data.get('ssh_user')}",
        ],
    )
