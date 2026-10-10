# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: =CS-Lib= The single source of the facts of this host's Unbound (local resolver) set-up.
#+end_org """

""" #+begin_org
* [[elisp:(org-cycle)][| ~Description~ |]] :: Unbound is BISOS's local resolver (decision of 2026-10-10,
bisos-pip/pals/palsWithBcm README.org <<1.2>>). It replaces sending every lookup to the
network's (ISP's) resolver:
** Full recursion by default, with DNSSEC validation and QNAME minimisation: no single party
   keeps a log of the names looked up. Forwarding over DNS-over-TLS to chosen upstreams is the
   alternative mode (the ISP then sees no DNS at all; the chosen provider sees all of it).
** The zones Knot serves for the site (intra.) are stub zones pointing at Knot.
   here. is deliberately NOT stubbed: .here names are loopback addresses, meaningful only on
   this platform, and stay in /etc/hosts.
** Company/VPN domains: a NetworkManager dispatcher script forwards the search domains a
   connection brings to that connection's own DNS servers, and removes them when it goes down.
** Browsers: Firefox and Chrome/Chromium policies turn their DNS-over-HTTPS off, so they use
   this resolver; Mozilla's canary domain is answered NXDOMAIN for unmanaged Firefoxes.
** What is generated: /etc/unbound/unbound.conf.d/bisos.conf (Debian's own unbound.conf.d
   files --- remote-control at /run/unbound.ctl, the root trust anchor --- are left alone),
   /etc/resolv.conf, a NetworkManager conf.d file (dns=none), the dispatcher script and
   the browser policy files.
** Pure: importing this module has no side effects and touches no host state.
** Status: Starting point. Not run on any host yet.
** /[[elisp:(org-cycle)][| Planned Improvements |]]/ :
*** TODO A local DNS-over-HTTPS endpoint (needs the platform CA, palsWithBcm 1.4), so Firefox keeps ECH.
*** TODO Listen on the site LAN too, when this platform is a site's resolver.
#+end_org """

####+BEGIN: b:prog:file/proclamations :outLevel 1
""" #+begin_org
* *[[elisp:(org-cycle)][| Proclamations |]]* :: Libre-Halaal Software --- Part Of BISOS ---  Poly-COMEEGA Format.
** This is Libre-Halaal Software. © Neda Communications, Inc. Subject to AGPL.
** It is part of BISOS (ByStar Internet Services OS)
** Best read and edited  with Blee in Poly-COMEEGA (Polymode Colaborative Org-Mode Enhance Emacs Generalized Authorship)
#+end_org """
####+END:

####+BEGIN: b:prog:file/particulars :authors ("./inserts/authors-mb.org")
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars |]]* :: Authors, version
** This File: /bisos/git/bxRepos/bisos-pip/dnsCap/py3/bisos/dnsCap/unboundInfo.py
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

import dataclasses
import enum
import json
import pathlib

from bisos.dnsCap.knotInfo import knotInfo


@enum.unique
class ResolverMode(enum.Enum):
    recursive = "recursive"       # ask the authoritative servers directly
    forwardTls = "forwardTls"     # forward everything over DNS-over-TLS to forwardTlsUpstreams


@dataclasses.dataclass(frozen=True)
class UnboundInfo:
    """The facts of this host's Unbound set-up. Built once, as unboundInfo below."""

    mode: ResolverMode = ResolverMode.recursive

    # Used only in forwardTls mode: "address@port#tls-auth-name", Unbound's notation.
    forwardTlsUpstreams: tuple[str, ...] = (
        "9.9.9.9@853#dns.quad9.net",
        "149.112.112.112@853#dns.quad9.net",
    )

    listenAddrs: tuple[str, ...] = ("127.0.0.1", "::1")

    # The zones Knot serves that this resolver sends to Knot. Not here. --- see Description.
    stubZones: tuple[str, ...] = ("intra",)

    # Mozilla's canary: NXDOMAIN tells Firefox not to switch DNS-over-HTTPS on by default.
    firefoxCanary: str = "use-application-dns.net"

    confFile: pathlib.Path = pathlib.Path("/etc/unbound/unbound.conf.d/bisos.conf")
    resolvConf: pathlib.Path = pathlib.Path("/etc/resolv.conf")
    resolvConfOrig: pathlib.Path = pathlib.Path("/etc/resolv.conf.bisos-orig")
    nmConfFile: pathlib.Path = pathlib.Path("/etc/NetworkManager/conf.d/90-bisos-dns.conf")
    nmDispatcherFile: pathlib.Path = pathlib.Path("/etc/NetworkManager/dispatcher.d/90-bisos-unbound-forward")
    controlSocket: pathlib.Path = pathlib.Path("/run/unbound.ctl")   # Debian's remote-control.conf

    firefoxPolicies: pathlib.Path = pathlib.Path("/etc/firefox/policies/policies.json")
    chromePolicyFiles: tuple[pathlib.Path, ...] = (
        pathlib.Path("/etc/opt/chrome/policies/managed/bisos-dns.json"),   # Google Chrome
        pathlib.Path("/etc/chromium/policies/managed/bisos-dns.json"),     # Debian's Chromium
    )

    # knot-dnsutils for kdig, the health check before /etc/resolv.conf is switched.
    debPkgs: tuple[str, ...] = ("unbound", "knot-dnsutils")

    # A name that must resolve before this host's resolv.conf is pointed at Unbound.
    healthCheckName: str = "debian.org"


# A Singleton
unboundInfo = UnboundInfo()


def unboundConfContent(info: UnboundInfo = unboundInfo) -> str:
    """The content of /etc/unbound/unbound.conf.d/bisos.conf. Regenerated, not hand-edited."""
    interfaces = "".join(f"    interface: {addr}\n" for addr in info.listenAddrs)
    stubs = "".join(
        f'    domain-insecure: "{zone}."\n'   # the signed root proves these TLDs do not exist
        f'    private-domain: "{zone}."\n'    # their answers may be private addresses
        for zone in info.stubZones
    )
    out = (
        "# Generated by bisos.dnsCap from bisos.dnsCap.unboundInfo. Do not edit: regenerate.\n"
        "# Debian's unbound.conf.d files (remote-control, root trust anchor) are left alone.\n"
        "server:\n"
        f"{interfaces}"
        "    access-control: 127.0.0.0/8 allow\n"
        "    access-control: ::1/128 allow\n"
        "    qname-minimisation: yes\n"
        "    harden-glue: yes\n"
        "    harden-dnssec-stripped: yes\n"
        "    aggressive-nsec: yes\n"
        "    prefetch: yes\n"
        "    hide-identity: yes\n"
        "    hide-version: yes\n"
        "    # Stub zones point at Knot on a 127.x address, which Unbound refuses by default.\n"
        "    do-not-query-localhost: no\n"
        f"{stubs}"
        f'    local-zone: "{info.firefoxCanary}." always_nxdomain\n'
    )
    if info.mode is ResolverMode.forwardTls:
        out += "    tls-cert-bundle: /etc/ssl/certs/ca-certificates.crt\n"
    for zone in info.stubZones:
        out += (
            "\nstub-zone:\n"
            f'    name: "{zone}."\n'
            f"    stub-addr: {knotInfo.listenAddr}\n"
        )
    if info.mode is ResolverMode.forwardTls:
        out += '\nforward-zone:\n    name: "."\n    forward-tls-upstream: yes\n'
        out += "".join(f"    forward-addr: {upstream}\n" for upstream in info.forwardTlsUpstreams)
    return out


def resolvConfContent(info: UnboundInfo = unboundInfo) -> str:
    """/etc/resolv.conf once this host uses Unbound. NetworkManager no longer writes it (dns=none)."""
    return (
        "# Generated by bisos.dnsCap from bisos.dnsCap.unboundInfo. Do not edit: regenerate.\n"
        "# The original is kept as /etc/resolv.conf.bisos-orig (unboundDns.cs -i resolverRevert).\n"
        "nameserver 127.0.0.1\n"
        "options edns0 trust-ad\n"
    )


def nmConfContent() -> str:
    """NetworkManager conf.d: stop writing /etc/resolv.conf."""
    return (
        "# Generated by bisos.dnsCap. NetworkManager must not overwrite /etc/resolv.conf:\n"
        "# this host resolves through its local Unbound.\n"
        "[main]\n"
        "dns=none\n"
    )


def nmDispatcherContent(info: UnboundInfo = unboundInfo) -> str:
    """NetworkManager dispatcher: forward a connection's own domains to its own DNS servers.

    On up / vpn-up: every search domain the connection brings (IP4_DOMAINS, VPN_IP4_DOMAINS)
    becomes an Unbound forward zone to that connection's name servers. +i marks it insecure:
    such internal zones are typically unsigned below a signed parent, and validation would
    reject them. On down / vpn-down: the zones recorded for that interface are removed.
    """
    return f"""#!/bin/sh
# Generated by bisos.dnsCap from bisos.dnsCap.unboundInfo. Do not edit: regenerate.
# Forward a connection's own (company/VPN) domains to its own DNS servers via Unbound.
iface="$1"; action="$2"
stateDir=/run/bisos-unbound
ctl="unbound-control -s {info.controlSocket}"
[ -S {info.controlSocket} ] || exit 0
mkdir -p "$stateDir"
stateFile="$stateDir/$iface.zones"

case "$action" in
    up|dhcp4-change)   domains="$IP4_DOMAINS";     servers="$IP4_NAMESERVERS" ;;
    vpn-up)            domains="$VPN_IP4_DOMAINS"; servers="$VPN_IP4_NAMESERVERS" ;;
    down|vpn-down)
        [ -f "$stateFile" ] || exit 0
        while read -r zone ; do
            $ctl forward_remove +i "$zone" >/dev/null 2>&1
            $ctl flush_zone "$zone" >/dev/null 2>&1
        done < "$stateFile"
        rm -f "$stateFile"
        exit 0 ;;
    *) exit 0 ;;
esac

[ -n "$domains" ] && [ -n "$servers" ] || exit 0
for zone in $domains ; do
    $ctl forward_add +i "$zone" $servers >/dev/null 2>&1 && echo "$zone" >> "$stateFile"
    $ctl flush_zone "$zone" >/dev/null 2>&1
done
exit 0
"""


def firefoxPoliciesMerged(existingText: str | None) -> str:
    """policies.json with DNS-over-HTTPS off and locked, merged into whatever policies exist.

    Firefox reads a single policies.json, so BISOS adds its key rather than owning the file.
    """
    data = json.loads(existingText) if existingText and existingText.strip() else {}
    data.setdefault("policies", {})["DNSOverHTTPS"] = {"Enabled": False, "Locked": True}
    return json.dumps(data, indent=2) + "\n"


def chromePolicyContent() -> str:
    """A managed-policy file of its own: Chrome/Chromium merge every file in the directory."""
    return json.dumps({"DnsOverHttpsMode": "off"}, indent=2) + "\n"


####+BEGIN: b:py3:cs:framework/endOfFile :basedOn "classification"
""" #+begin_org
* [[elisp:(org-cycle)][| *End-Of-Editable-Text* |]] :: emacs and org variables and control parameters
#+end_org """

#+STARTUP: showall

### local variables:
### no-byte-compile: t
### end:
####+END:
