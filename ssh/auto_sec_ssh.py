# SSH atacks
from .auto_sec_ssh_brute_force import hydra


def brute_force(target):
    return hydra(target)


 