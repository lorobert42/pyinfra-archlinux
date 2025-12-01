from pyinfra.operations import pacman, server, systemd

pacman.packages(
    name="Network - Install NetworkManager",
    packages=[
        "networkmanager",
        "wireless-regdb",
        "wpa_supplicant",
    ],
    present=True,
    _sudo=True,
)

systemd.service(
    name="Network - Enable the NetworkManager service",
    service="NetworkManager.service",
    running=True,
    enabled=True,
    _sudo=True,
)

server.shell(
    name="Network - Set regdomain to CH",
    commands=['echo WIRELESS_REGDOM="CH" > /etc/conf.d/wireless-regdom'],
    _sudo=True,
)
