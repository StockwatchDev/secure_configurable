"""Module for loading and retrieving parameters for configuration and settings."""

from importlib.metadata import version

from secure_configurable_config.config import SecureConfigSection, CSPConfigSection

__version__ = version("secure_configurable_config")

__all__ = [
    "CSPConfigSection",
    "SecureConfigSection",
]
