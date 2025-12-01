from pyinfra.operations import pacman

pacman.packages(
    name="Audio - Install Pipewire",
    packages=[
        "pipewire",
        "pipewire-alsa",
        "pipewire-jack",
        "pipewire-pulse",
        "wireplumber",
    ],
    present=True,
    _sudo=True,
)
