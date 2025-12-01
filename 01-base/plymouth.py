from pyinfra import config, host
from pyinfra.facts import files
from pyinfra.operations import pacman, server

config.SUDO = True

pacman.packages(
    name="Plymouth - Install plymouth",
    packages=["plymouth"],
)

if not host.get_fact(files.File, "/boot/loader/entries/arch.conf"):
    server.shell(
        name="Plymouth - Set file name",
        commands=[
            "mv /boot/loader/entries/*linux-zen.conf /boot/loader/entries/arch.conf",
            "mv /boot/loader/entries/*linux-zen-fallback.conf /boot/loader/entries/arch-fallback.conf",
        ],
    )

if not host.get_fact(
    files.FindInFile, "/boot/loader/entries/arch.conf", "quiet splash"
):
    server.shell(
        name="Plymouth - Set boot parameters",
        commands="sed -i 's/options root=.*$/& quiet splash/' /boot/loader/entries/arch.conf",
    )

if not host.get_fact(files.FindInFile, "/etc/mkinitcpio.conf", "plymouth"):
    server.shell(
        name="Plymouth - Set mkinitcpio",
        commands="sed -i 's/^HOOKS=([a-z ]*/& plymouth/' /etc/mkinitcpio.conf",
    )

packages = [
    "plymouth-theme-catppuccin-mocha-git",
]

server.shell(
    name="Plymouth - Install theme",
    commands=f"paru -S --noconfirm {', '.join(packages)}",
    _su_user="aur_builder",
)

server.shell(
    name="Plymouth - Set theme",
    commands="plymouth-set-default-theme -R catppuccin-mocha",
)

# server.shell(
#     name="Plymouth - Regenerate mkinitcpio",
#     commands="mkinitcpio -p linux-zen",
# )
