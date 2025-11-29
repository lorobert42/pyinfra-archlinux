from pyinfra.operations import pacman, server

pacman.packages(
    name="Firmware - Install Linux Firmware",
    packages=["linux-firmware"],
    present=True,
    _sudo=True,
)

pacman.packages(
    name="Firmware - Install Intel microcode",
    packages=["intel-ucode"],
    present=True,
    _sudo=True,
)

pacman.packages(
    name="Firmware - Install tool to manipulate Intel® IA-32/X86-64 microcode bundles",
    packages=["iucode-tool"],
    present=True,
    _sudo=True,
)

server.modprobe(
    name="Firmware - Load the cpuid kernel module",
    module="cpuid",
    present=True,
    _sudo=True,
)
