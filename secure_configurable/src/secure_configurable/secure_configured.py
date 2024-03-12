"""Module for creating a configured secure_header."""

import secure
from secure_configurable_config import (
    CSPConfigSection,
    HSTSConfigSection,
    SecureConfigSection,
)


def _configure_csp(csp_config: CSPConfigSection) -> secure.ContentSecurityPolicy:
    csp = secure.ContentSecurityPolicy()
    if csp_config.base_uri:
        csp.base_uri(*csp_config.base_uri)
    if csp_config.child_src:
        csp.child_src(*csp_config.child_src)
    if csp_config.connect_src:
        csp.connect_src(*csp_config.connect_src)
    if csp_config.default_src:
        csp.default_src(*csp_config.default_src)
    if csp_config.font_src:
        csp.font_src(*csp_config.font_src)
    if csp_config.form_action:
        csp.form_action(*csp_config.form_action)
    if csp_config.frame_ancestors:
        csp.frame_ancestors(*csp_config.frame_ancestors)
    if csp_config.frame_src:
        csp.frame_src(*csp_config.frame_src)
    if csp_config.img_src:
        csp.img_src(*csp_config.img_src)
    if csp_config.manifest_src:
        csp.manifest_src(*csp_config.manifest_src)
    if csp_config.media_src:
        csp.media_src(*csp_config.media_src)
    if csp_config.object_src:
        csp.object_src(*csp_config.object_src)
    if csp_config.report_to.endpoints:
        max_age = csp_config.report_to.max_age
        group = csp_config.report_to.group
        endpoints = {"url": csp_config.report_to.endpoints[0]}
        csp.report_to(secure.ReportTo(max_age, False, group, endpoints))  # type: ignore[arg-type]
    if csp_config.script_src:
        csp.script_src(*csp_config.script_src)
    if csp_config.style_src:
        csp.style_src(*csp_config.style_src)
    if csp_config.worker_src:
        csp.worker_src(*csp_config.worker_src)
    if csp_config.upgrade_insecure_requests:
        csp.upgrade_insecure_requests()

    return csp


def _configure_hsts(hsts_config: HSTSConfigSection) -> secure.StrictTransportSecurity:
    hsts = secure.StrictTransportSecurity()
    if hsts_config.include_subdomains:
        hsts.include_subdomains()
    if hsts_config.max_age:
        hsts.max_age(hsts_config.max_age)
    if hsts_config.preload:
        hsts.preload()
    return hsts


def _configure_referrer(referrer_config: str) -> secure.ReferrerPolicy:
    referrer = secure.ReferrerPolicy()
    for ref_dir in referrer_config.split(","):
        referrer_directive = getattr(referrer, ref_dir.strip(), None)
        if referrer_directive:
            referrer_directive()
    return referrer


def _configure_secure_headers() -> secure.Secure:
    sec_conf = SecureConfigSection.get()
    server = secure.Server().set(sec_conf.server_name)

    csp = _configure_csp(sec_conf.csp_config)
    hsts = _configure_hsts(sec_conf.hsts_config)
    referrer = _configure_referrer(sec_conf.referrer_config)

    return secure.Secure(
        server=server,
        csp=csp,
        hsts=hsts,
        referrer=referrer,
    )


secure_headers = _configure_secure_headers()
