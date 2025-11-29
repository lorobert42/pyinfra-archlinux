from pyinfra import local
from pyinfra.operations import pacman

# Locales
local.include("./locales.py")

# Network
local.include("./network.py")

# Time
local.include("./time.py")

# Filesystem
local.include("./filesystem.py")

# Firmware
local.include("./firmware.py")

# Audio
local.include("./audio.py")

# Bluetooth
local.include("./bluetooth.py")

# Polkit
pacman.packages(
    name="Polkit - Install polkit",
    packages=[
        "polkit",
    ],
    present=True,
    _sudo=True,
)

# Fonts
local.include("./fonts.py")

# paru
local.include("./paru.py")

# Tools
local.include("./tools.py")

# Compositor
local.include("./niri.py")
