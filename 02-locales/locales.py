from pyinfra.operations import pacman, server

server.shell(
    name="Locales - Generate en_US and fr_CH locales",
    commands=[
        'echo "en_US.UTF-8 UTF-8" > /etc/locale.gen',
        'echo "fr_CH.UTF-8 UTF-8" >> /etc/locale.gen',
        "locale-gen",
    ],
    _sudo=True,
)

pacman.packages(
    name="Locales - Install hunspell",
    packages=[
        "hunspell",
        "hunspell-en_us",
        "hunspell-fr",
    ],
    present=True,
    _sudo=True,
)
