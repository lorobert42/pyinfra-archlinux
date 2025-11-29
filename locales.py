from pyinfra.operations import server

server.shell(
    name="Locale - Generate en_US and fr_CH locales",
    commands=[
        'echo "en_US.UTF-8 UTF-8" > /etc/locale.gen',
        'echo "fr_CH.UTF-8 UTF-8" >> /etc/locale.gen',
        "locale-gen",
    ],
    _sudo=True,
)
