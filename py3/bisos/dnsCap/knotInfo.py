# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: =CS-Lib= The single source of the facts of this host's Knot DNS (authoritative) installation.
#+end_org """

""" #+begin_org
* [[elisp:(org-cycle)][| ~Description~ |]] :: Knot DNS is BISOS's authoritative DNS server (decision of
2026-10-10, see bisos-pip/pals/palsWithBcm README.org <<1.2>>). It is run *tinydns-style*:
** BISOS data is the single source. The generators below produce knot.conf and one plain
   RFC 1035 zone file per zone --- as tinydns-data produced data.cdb from the data file.
** kzonecheck validates each generated zone; knotc zone-reload publishes it atomically.
** knot.conf keeps the server stateless: zonefile-load: whole (always the whole file),
   journal-content: none (no journal), zonefile-sync: -1 (never write back to the file).
   Nothing is ever edited in the running server.
** SOA serials are the generation time in seconds (unixtime), as tinydns used the data
   file's mtime.
** Pure: importing this module has no side effects and touches no host state.
** Status: Starting point.
** /[[elisp:(org-cycle)][| Planned Improvements |]]/ :
*** TODO Register listenIp in bisos.banna (an IP registry beside tcpPorts.hereIp).
*** TODO Zones of PALS (first.last.byname.net) as a second ZoneSpec source, beside here.
*** TODO DNSSEC: dnssec-signing + policy, and journal-content: changes, once a public zone exists.
*** TODO DnsSpecMethod.knot in dnsCap_seedInfo, so a -here-dns.pcs updates the here zone.
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
** This File: /bisos/git/bxRepos/bisos-pip/dnsCap/py3/bisos/dnsCap/knotInfo.py
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

import dataclasses
import pathlib
import time
import typing


@dataclasses.dataclass(frozen=True)
class ZoneRecord:
    """One resource record. owner is relative to the zone ("@" for the apex)."""
    owner: str
    rrType: str
    rdata: str
    ttl: int | None = None


@dataclasses.dataclass(frozen=True)
class ZoneSpec:
    """A zone Knot serves: its name and its records (SOA and apex NS are added by zoneFileContent)."""
    domain: str
    records: tuple[ZoneRecord, ...]
    ttl: int = 300


@dataclasses.dataclass(frozen=True)
class KnotInfo:
    """The facts of this host's Knot DNS installation. Built once, as knotInfo below."""

    # Debian's knot package: the knot account, knot.service, /etc/knot/knot.conf.
    acctName: str = "knot"
    confFile: pathlib.Path = pathlib.Path("/etc/knot/knot.conf")
    rundir: pathlib.Path = pathlib.Path("/run/knot")

    # Generated zone files. A BISOS-owned subdirectory, so Debian's examples stay untouched.
    zonesDir: pathlib.Path = pathlib.Path("/var/lib/knot/bisos")

    # Knot listens on its own loopback address, port 53 --- not 127.0.0.1, which the
    # resolver takes (as tinydns and dnscache each had their own address). 127.0.0.53 is
    # systemd-resolved's stub, and 127.0.22.x is banna's .here range.
    listenIp: str = "127.0.53.1"
    listenPort: int = 53

    # The name of this server within each zone it serves (SOA mname, apex NS).
    nsName: str = "ns"
    hostmaster: str = "hostmaster"

    # knot-dnssecutils ships kzonecheck (not knot itself, on Debian 13); knot-dnsutils ships kdig.
    debPkgs: tuple[str, ...] = ("knot", "knot-dnssecutils", "knot-dnsutils")

    @property
    def listenAddr(self) -> str:
        """Knot's addr@port notation."""
        return f"{self.listenIp}@{self.listenPort}"

    def zoneFile(self, domain: str) -> pathlib.Path:
        return self.zonesDir / f"{domain.rstrip('.')}.zone"


# A Singleton
knotInfo = KnotInfo()


def hereZoneSpec() -> ZoneSpec:
    """The here. zone: every banna .here name, at its stored hereIp.

    The same source as the /etc/hosts dblock (bannaInfo.cs -i bannaForEtcHosts), so the
    two can be run side by side during migration and must agree.
    """
    from bisos.banna import tcpPorts
    return ZoneSpec(
        domain="here",
        records=tuple(ZoneRecord(hereName, "A", hereIp) for hereIp, hereName, _ in tcpPorts.hereEntries()),
    )


def intraZoneSpec() -> ZoneSpec:
    """The intra. zone: this site's names, at real (LAN) addresses. Reached via Unbound's stub zone.

    Placeholder: SOA and NS only, so .intra names get an authoritative NXDOMAIN rather than a
    failure. Its data source (site BPO or a banna-like registry of site names) is not decided.
    """
    return ZoneSpec(domain="intra", records=())


# The zones this host serves. Each entry is a function, so the data is read at generation time.
# here. is served too, but only for testing Knot: .here resolves through /etc/hosts (loopback
# names are per-platform), and the resolver does not stub it here.
zoneSpecFuncs: dict[str, typing.Callable[[], ZoneSpec]] = {
    "here": hereZoneSpec,
    "intra": intraZoneSpec,
}


def zoneSpecOf(domain: str) -> ZoneSpec:
    return zoneSpecFuncs[domain.rstrip(".")]()


def zoneFileContent(spec: ZoneSpec, serial: int | None = None, info: KnotInfo = knotInfo) -> str:
    """The zone file of spec, as written to info.zoneFile(spec.domain).

    serial defaults to now (unixtime), like tinydns's data-file mtime: every generation is
    a new version, and secondaries (when there are any) see it as newer.
    """
    serial = int(time.time()) if serial is None else serial
    origin = spec.domain.rstrip(".") + "."
    lines = [
        f"; Generated by bisos.dnsCap from bisos.dnsCap.knotInfo. Do not edit: regenerate.",
        f"$ORIGIN {origin}",
        f"$TTL {spec.ttl}",
        # refresh retry expire minimum(negative-caching TTL)
        f"@ SOA {info.nsName}.{origin} {info.hostmaster}.{origin} {serial} 3600 600 604800 {spec.ttl}",
        f"@ NS {info.nsName}.{origin}",
        f"{info.nsName} A {info.listenIp}",
    ]
    for rec in spec.records:
        ttl = f"{rec.ttl} " if rec.ttl is not None else ""
        lines.append(f"{rec.owner} {ttl}{rec.rrType} {rec.rdata}")
    return "\n".join(lines) + "\n"


def knotConfContent(domains: typing.Iterable[str] | None = None, info: KnotInfo = knotInfo) -> str:
    """The content /etc/knot/knot.conf is generated with. Regenerated, not hand-edited.

    Unlike the app config files of bisos.kafka/bisos.airflow (written only when absent),
    this is a build output of BISOS's DNS data: changes belong in this generator.
    """
    domains = list(zoneSpecFuncs) if domains is None else list(domains)
    zones = "".join(f"  - domain: {d.rstrip('.')}\n" for d in domains)
    return (
        "# Generated by bisos.dnsCap from bisos.dnsCap.knotInfo. Do not edit: regenerate.\n"
        "server:\n"
        f"    rundir: \"{info.rundir}\"\n"
        f"    user: {info.acctName}:{info.acctName}\n"
        f"    listen: [ {info.listenAddr} ]\n"
        "\n"
        "log:\n"
        "  - target: syslog\n"
        "    any: info\n"
        "\n"
        "database:\n"
        f"    storage: \"{info.zonesDir.parent}\"\n"
        "\n"
        "template:\n"
        "  - id: default\n"
        f"    storage: \"{info.zonesDir}\"\n"
        "    file: \"%s.zone\"\n"
        "    # tinydns-style: the zone file is the whole truth, the server keeps no state.\n"
        "    zonefile-load: whole\n"
        "    journal-content: none\n"
        "    zonefile-sync: -1\n"
        "    semantic-checks: on\n"
        "\n"
        "zone:\n"
        f"{zones}"
    )


####+BEGIN: b:py3:cs:framework/endOfFile :basedOn "classification"
""" #+begin_org
* [[elisp:(org-cycle)][| *End-Of-Editable-Text* |]] :: emacs and org variables and control parameters
#+end_org """

#+STARTUP: showall

### local variables:
### no-byte-compile: t
### end:
####+END:
