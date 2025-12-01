from pyinfra.operations import pacman

pacman.packages(
    name="Base - Install base tools",
    packages=[
        "bat",
        "curl",
        "eza",
        "fd",
        "fish",
        "fzf",
        "git",
        "helix",
        "jq",
        "mlocate",
        "polkit",
        "python",
        "ripgrep",
        "ripgrep-all",
        "vim",
        "wget",
        "yazi",
        "yq",
        "zellij",
        "zoxide",
    ],
    present=True,
    _sudo=True,
)
