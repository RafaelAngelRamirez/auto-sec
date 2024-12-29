from .tools.hydra.auto_sec_hydra import AutoSecHydra


def hydra(target):
    h = AutoSecHydra()
    result = h.ssh().target(target).run()
    return result
