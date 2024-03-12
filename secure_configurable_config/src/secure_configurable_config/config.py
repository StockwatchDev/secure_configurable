"""Configuration parameters for secure.Secure()"""

from dataclasses import field

from application_settings import ConfigSectionBase, dataclass
from attributes_doc import attributes_doc


@attributes_doc
@dataclass(frozen=True)
class ReportToConfigSection(
    ConfigSectionBase
):  # pylint: disable=too-many-instance-attributes
    """Config section for secure.ContentSecurityPolicy.report_to()"""

    group: str = "endpoint_name"
    """Name that identifies the group to report to; defaults to 'endpoint_name'"""

    max_age: int = 604800
    """Time interval in seconds for which the browser should use the given endpoints;
       defaults to 604800, i.e., 1 week"""

    endpoints: tuple[str, ...] = field(default_factory=tuple)
    """Sets valid urls to report to; e.g. https://example.com/csp-reports;
       defaults to empty tuple (meaning no report-to)."""


@attributes_doc
@dataclass(frozen=True)
class CSPConfigSection(
    ConfigSectionBase
):  # pylint: disable=too-many-instance-attributes
    """Config section for secure.ContentSecurityPolicy()

    Keyword values (embed with single quotes in double quotes): 'none', 'self', 'unsafe-inline'
    and 'unsafe-eval'.
    Default settings equal to most basic policy, tightened version as recommended by
    https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html
    This policy allows images, scripts, AJAX, and CSS from the same origin and does not allow any
    other resources to load (e.g., object, frame, media, etc.).
    If you want a more strict setting, consider this: https://web.dev/articles/strict-csp
    """

    report_only: bool = False
    """Whether or not to set Content-Security-Policy header to Content-Security-Policy-Report-Only;
       defaults to False"""

    base_uri: tuple[str, ...] = field(default_factory=tuple)
    """Sets valid origins for `<base>`; defaults to empty tuple (meaning not set)."""

    child_src: tuple[str, ...] = field(default_factory=tuple)
    """Sets valid origins for web workers; defaults to empty tuple (meaning not set)."""

    connect_src: tuple[str, ...] = field(default_factory=lambda: ("'self'",))
    """Sets valid origins for script interfaces; defaults to ("'self'",)."""

    default_src: tuple[str, ...] = field(default_factory=lambda: ("'none'",))
    """Sets fallback valid orgins for directives not set explicitly; defaults to ("'none'",)."""

    font_src: tuple[str, ...] = field(default_factory=tuple)
    """Set valid origins for `@font-face`; defaults to empty tuple (meaning not set)."""

    form_action: tuple[str, ...] = field(default_factory=lambda: ("'self'",))
    """Set valid origins for form submissions; defaults to ("'self'",)."""

    frame_ancestors: tuple[str, ...] = field(default_factory=lambda: ("'self'",))
    """Set valid origins that can embed the resource; defaults to ("'self'",)."""

    frame_src: tuple[str, ...] = field(default_factory=tuple)
    """Set valid origins for frames; defaults to empty tuple (meaning not set)."""

    img_src: tuple[str, ...] = field(default_factory=lambda: ("'self'",))
    """Set valid origins for images; defaults to ("'self'",)."""

    manifest_src: tuple[str, ...] = field(default_factory=tuple)
    """Set valid origins for manifest files; defaults to empty tuple (meaning not set)."""

    media_src: tuple[str, ...] = field(default_factory=tuple)
    """Set valid origins for media; defaults to empty tuple (meaning not set)."""

    object_src: tuple[str, ...] = field(default_factory=tuple)
    """Set valid origins for plugins; defaults to empty tuple (meaning not set)."""

    # plugin_types(types)  - not configurable, deprecated

    report_to: ReportToConfigSection = ReportToConfigSection()
    """Set the endpoints to report violations to; defaults to no endpoints"""

    # report_uri: str = ""  - not configurable, deprecated

    # require_sri_for(values)  - currently not configurable

    # sandbox(values)  - currently not configurable

    script_src: tuple[str, ...] = field(default_factory=lambda: ("'self'",))
    """Set valid origins for JavaScript; defaults to ("'self'"))."""

    style_src: tuple[str, ...] = field(default_factory=lambda: ("'self'",))
    """Set valid origins for styles; defaults to ("'self'",)."""

    upgrade_insecure_requests: bool = False
    """Wheter or not to upgrade HTTP URLs to HTTPS; defaults to False"""

    worker_src: tuple[str, ...] = field(default_factory=tuple)
    """Set valid origins for worker scripts; defaults to empty tuple (meaning not set)."""


@attributes_doc
@dataclass(frozen=True)
class HSTSConfigSection(ConfigSectionBase):
    """Config section for secure.StrictTransportSecurity()"""

    include_subdomains: bool = True
    """Whether or not this rule applies to all of the site's subdomains as well; defaults to True"""

    max_age: int = 63072000
    """The time, in seconds, that the browser should remember that a site is only to be accessed
       using HTTPS; defaults to 63072000, i.e., 2 year"""

    preload: bool = False
    """Whether or not this site should be included in Google's preload service; defaults to False"""


@attributes_doc
@dataclass(frozen=True)
class SecureConfigSection(ConfigSectionBase):
    """Config section for secure.py"""

    server_name: str = "Unidentified"
    """Name to use in the header for the server"""

    csp_config: CSPConfigSection = CSPConfigSection()
    """Config section for secure.ContentSecurityPolicy()"""

    hsts_config: HSTSConfigSection = HSTSConfigSection()
    """Config section for secure.StrictTransportSecurity()"""

    referrer_config: str = "no_referrer, strict_origin_when_cross_origin"
    """Referrer policy - comma-seperated list of: 'no_referrer', 'no_referrer_when_downgrade',
       'origin', 'origin_when_cross_origin', 'same_origin', 'strict_origin',
       'strict_origin_when_cross_origin', 'unsafe_url'; 
       defaults to 'no referrer, strict_origin_when_cross_origin'"""
