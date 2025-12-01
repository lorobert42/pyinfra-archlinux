from pyinfra.operations import server

packages = [
    "oh-my-posh-bin",
]

server.shell(
    name="Terminal - Install oh-my-posh",
    commands=f"paru -S --noconfirm {', '.join(packages)}",
    _su_user="aur_builder",
    _sudo=True,
)
