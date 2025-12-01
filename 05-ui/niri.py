from pyinfra.operations import pacman, server


pacman.packages(
    name="Niri - Install dependencies",
    packages=[
        "alacritty",
        "fuzzel",
        "mako",
        "niri",
        "sddm",
        "swaylock",
        "xdg-desktop-portal-gnome",
        "xdg-desktop-portal-gtk",
        "xwayland-satellite",
    ],
    present=True,
    update=True,
    _sudo=True,
)

packages = [
    "dms-shell-bin",
    "matugen",
    "wl-clipboard",
    "cliphist",
    "cava",
    "qt6-multimedia-ffmpeg",
]

server.shell(
    name="Niri - Install paru dependencies",
    commands=f"paru -S --noconfirm {' '.join(packages)}",
    _su_user="aur_builder",
    _sudo=True,
)

server.shell(
    name="Niri - Add dms to systemctl",
    commands=[
        "systemctl --user add-wants niri.service dms",
        "systemctl --user add-wants niri.service mako.service",
    ],
)

server.shell(
    name="Niri - Enable sddm",
    commands="systemctl enable sddm.service",
    _sudo=True,
)
