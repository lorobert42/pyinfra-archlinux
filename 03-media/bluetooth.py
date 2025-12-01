from pyinfra.operations import pacman, systemd

pacman.packages(
    name="Bluetooth - Install bluez",
    packages=[
        "blueman",
        "bluez",
        "bluez-utils",
    ],
    present=True,
    _sudo=True,
)

systemd.service(
    name="Bluetooth - Enable the bluetooth service",
    service="bluetooth.service",
    running=True,
    enabled=True,
    _sudo=True,
)
