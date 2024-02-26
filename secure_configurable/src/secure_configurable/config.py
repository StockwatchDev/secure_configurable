"""Configuration parameters for secure.Secure()"""

from application_settings import ConfigSectionBase, dataclass
from attributes_doc import attributes_doc


@attributes_doc
@dataclass(frozen=True)
class SecureConfigSection(ConfigSectionBase):
    """Config section for secure.Secure()"""

    field1: float = 0.5
    """Docstring for the first field; defaults to 0.5"""
    field2: int = 2
    """Docstring for the second field; defaults to 2"""
