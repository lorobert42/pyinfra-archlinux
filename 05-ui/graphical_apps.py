from pyinfra.operations import pacman, server

pacman.packages(
    name="Install graphical applications",
    packages=[
        "libreoffice-fresh",
        "libreoffice-fresh-fr",
        "transmission-gtk",
    ],
    present=True,
    _sudo=True,
)

packages = [
    "waterfox-bin",
]

server.shell(
    name="Install graphical applications - paru",
    commands=f"paru -S --noconfirm {', '.join(packages)}",
    _su_user="aur_builder",
    _sudo=True,
)
