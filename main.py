from pyinfra import local

# Base
local.include("./01-base/base.py")
local.include("./01-base/utils.py")
local.include("./01-base/firmware.py")
local.include("./01-base/time.py")
local.include("./01-base/network.py")
local.include("./01-base/tools.py")
local.include("./01-base/paru.py")
local.include("./01-base/plymouth.py")

# Locales & Languages
local.include("./02-locales/locales.py")
local.include("./02-locales/fonts.py")

# Media
local.include("./03-media/audio.py")
local.include("./03-media/bluetooth.py")

# Programming
local.include("./04-programming/development.py")
local.include("./04-programming/rust.py")

# UI
local.include("./05-ui/niri.py")
local.include("./05-ui/terminal.py")
local.include("./05-ui/graphical_apps.py")
local.include("./05-ui/virtualbox.py")

# Config
local.include("./06-config/dotfiles.py")
