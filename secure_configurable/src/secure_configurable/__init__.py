"""Module for loading and retrieving parameters for configuration and settings."""

from importlib.metadata import version
from secure import Secure

from secure_configurable.secure_configured import secure_headers

__version__ = version("secure_configurable_config")

__all__ = [
    "Secure",
    "secure_headers",
]
