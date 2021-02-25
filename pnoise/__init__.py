from .pnoise import Noise


def _get_version() -> str:
    import pkg_resources

    return pkg_resources.get_distribution("pnoise").version


__version__ = _get_version()
