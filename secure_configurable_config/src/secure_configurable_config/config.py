"""Configuration parameters for secure.Secure()"""

from dataclasses import field

from application_settings import ConfigSectionBase, dataclass
from attributes_doc import attributes_doc


@attributes_doc
@dataclass(frozen=True)
class CSPConfigSection(
    ConfigSectionBase
):  # pylint: disable=too-many-instance-attributes
    """Config section for secure.ContentSecurityPolicy()

    Keyword values (embed with single quotes in double quotes): 'none', 'self', 'unsafe-inline' and 'unsafe-eval'
    """

    configure_csp: bool = False
    """Whether or not to configure a csp; defaults to False"""

    report_only: bool = False
    """Whether or not to set Content-Security-Policy header to Content-Security-Policy-Report-Only; defaults to False"""

    base_uri: tuple[str, ...] = field(default_factory=tuple)
    """Sets valid origins for `<base>`; defaults to empty tuple (meaning not set)."""

    child_src: tuple[str, ...] = field(default_factory=tuple)
    """Sets valid origins for web workers; defaults to empty tuple (meaning not set)."""

    connect_src: tuple[str, ...] = field(default_factory=tuple)
    """Sets valid origins for script interfaces; defaults to empty tuple (meaning not set)."""

    default_src: tuple[str, ...] = field(default_factory=tuple)
    """Sets fallback valid orgins for directives not set explicitly; defaults to empty tuple (meaning not set)."""

    font_src: tuple[str, ...] = field(default_factory=tuple)
    """Set valid origins for `@font-face`; defaults to empty tuple (meaning not set)."""

    form_action: tuple[str, ...] = field(default_factory=tuple)
    """Set valid origins for form submissions; defaults to empty tuple (meaning not set)."""

    frame_ancestors: tuple[str, ...] = field(default_factory=tuple)
    """Set valid origins that can embed the resource; defaults to empty tuple (meaning not set)."""

    frame_src: tuple[str, ...] = field(default_factory=tuple)
    """Set valid origins for frames; defaults to empty tuple (meaning not set)."""

    img_src: tuple[str, ...] = field(default_factory=tuple)
    """Set valid origins for images; defaults to empty tuple (meaning not set)."""

    manifest_src: tuple[str, ...] = field(default_factory=tuple)
    """Set valid origins for manifest files; defaults to empty tuple (meaning not set)."""

    media_src: tuple[str, ...] = field(default_factory=tuple)
    """Set valid origins for media; defaults to empty tuple (meaning not set)."""

    object_src: tuple[str, ...] = field(default_factory=tuple)
    """Set valid origins for plugins; defaults to empty tuple (meaning not set)."""

    # plugin_types(types)  - currently not configurable

    # report_to(json_object)  - currently not configurable

    # report_uri(uri)  - currently not configurable

    # require_sri_for(values)  - currently not configurable

    # sandbox(values)  - currently not configurable

    script_src: tuple[str, ...] = field(default_factory=tuple)
    """Set valid origins for JavaScript; defaults to empty tuple (meaning not set)."""

    style_src: tuple[str, ...] = field(default_factory=tuple)
    """Set valid origins for styles; defaults to empty tuple (meaning not set)."""

    upgrade_insecure_requests: bool = False
    """Wheter or not to upgrade HTTP URLs to HTTPS; defaults to False"""

    worker_src: tuple[str, ...] = field(default_factory=tuple)
    """Set valid origins for worker scripts; defaults to empty tuple (meaning not set)."""


@attributes_doc
@dataclass(frozen=True)
class SecureConfigSection(ConfigSectionBase):
    """Config section for secure.Secure()"""

    field1: float = 0.5
    """Docstring for the first field; defaults to 0.5"""
    field2: int = 2
    """Docstring for the second field; defaults to 2"""
