from .pnoise import Noise


def _get_version() -> str:
    try:
        from importlib.metadata import version
    except ModuleNotFoundError:
        from importlib_metadata import version  # type: ignore

    return version(__name__)


__version__ = _get_version()
