from pyinfra.operations import pacman, server

pacman.packages(
    name="Firmware - Install firmware",
    packages=[
        "amd-ucode",
        "intel-ucode",
        "iucode-tool",
        "linux-firmware",
    ],
    _sudo=True,
)

# server.modprobe(
#     name="Firmware - Load the cpuid kernel module",
#     module="cpuid",
#     present=True,
#     _sudo=True,
# )
