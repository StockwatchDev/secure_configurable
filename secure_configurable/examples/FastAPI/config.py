"""Module that defines the config for the FastAPI example"""

from application_settings import ConfigBase, dataclass

from secure_configurable_config import CSPConfigSection


@dataclass(frozen=True)
class FastAPIExampleConfig(ConfigBase):
    """Config for the FastAPI example"""

    csp_config: CSPConfigSection = CSPConfigSection(configure_csp=True)
