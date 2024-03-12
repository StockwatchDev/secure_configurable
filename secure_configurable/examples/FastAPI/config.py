"""Module that defines the config for the FastAPI example"""

from application_settings import ConfigBase, config_filepath_from_cli, dataclass

from secure_configurable_config import SecureConfigSection


@dataclass(frozen=True)
class FastAPIExampleConfig(ConfigBase):
    """Config for the FastAPI example"""

    secure_config: SecureConfigSection = SecureConfigSection()
    """Config for secure.py"""


config_filepath_from_cli(FastAPIExampleConfig)
FastAPIExampleConfig.load()
