from pyinfra.operations import pacman, server

pacman.packages(
    name="Fonts - Install fontconfig",
    packages=[
        "fontconfig",
    ],
    present=True,
    _sudo=True,
)

pacman.packages(
    name="Fonts - Install fonts",
    packages=[
        "adobe-source-code-pro-fonts",
        "cantarell-fonts",
        "gnu-free-fonts",
        "noto-fonts",
        "noto-fonts-cjk",
        "noto-fonts-emoji",
        "noto-fonts-extra",
        "otf-font-awesome",
        "ttf-bitstream-vera",
        "ttf-croscore",
        "ttf-dejavu",
        "ttf-droid",
        "ttf-fira-code",
        "ttf-fira-mono",
        "ttf-fira-sans",
        "ttf-hack",
        "ttf-ibm-plex",
        "ttf-jetbrains-mono",
        "ttf-jetbrains-mono-nerd",
        "ttf-liberation",
        "ttf-nerd-fonts-symbols",
        "ttf-nerd-fonts-symbols-common",
        "ttf-nerd-fonts-symbols-mono",
        "ttf-opensans",
        "ttf-roboto",
        "ttf-roboto-mono",
        "ttf-ubuntu-font-family",
    ],
    present=True,
    _sudo=True,
)

server.shell(
    name="Fonts - Generate fc-cache",
    commands=[
        "fc-cache -f -v",
    ],
    _sudo=True,
)
