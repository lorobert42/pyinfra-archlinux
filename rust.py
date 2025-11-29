from pyinfra.operations import server

server.shell(
    name="Install rustup",
    commands="curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y",
)
