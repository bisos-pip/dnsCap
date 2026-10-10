#!/bin/bash -i
#

# Safety check: must run from a directory named "tests"
if [[ "$(basename "$PWD")" != "tests" ]]; then
    echo "ERROR: verify.sh must be run from a directory named 'tests'." >&2
    echo "  Current PWD: $PWD" >&2
    exit 1
fi

lpDo ../bin/dnsCap_seed.cs
lpDo ../bin/airflow-here-dns.pcs

# ensureHostsDblock -- add-path against a scratch file (real /etc/hosts is left untouched)
printf '127.0.0.1\tlocalhost\n' > /tmp/dnsCap-hosts-test
lpDo ../bin/airflow-here-dns.pcs -i dnsCap_ensureHostsDblock /tmp/dnsCap-hosts-test
lpDo cat /tmp/dnsCap-hosts-test
# ensureHostsDblock -- idempotent second run detects the dblock and no-ops
lpDo ../bin/airflow-here-dns.pcs -i dnsCap_ensureHostsDblock /tmp/dnsCap-hosts-test
# ensureHostsDblock -- present-path against real /etc/hosts (dblock already there)
lpDo ../bin/airflow-here-dns.pcs -i dnsCap_ensureHostsDblock

lpDo ../bin/airflow-here-dns.pcs -i dnsCap_verify
lpDo ../bin/airflow-here-dns.pcs -i dnsCap_update
lpDo cat /etc/hosts
lpDo ../bin/airflow-here-dns.pcs -i dnsCap_resolve  airflow.here
lpDo ../bin/airflow-here-dns.pcs -i dnsCap_fqdnPing  airflow.here
lpDo ping -c 3 airflow.here


# --- Knot DNS (authoritative): read-only generation; nothing installed or started ---
lpDo ../bin/knotDns.cs
lpDo ../bin/knotDns.cs -i knotConfStdout
lpDo ../bin/knotDns.cs -i knotZoneStdout here
lpDo ../bin/knot-sbom.pcs -i readme
lpDo python3 -c "
import dns.zone
from bisos.dnsCap import knotInfo as k
zone = dns.zone.from_text(k.zoneFileContent(k.zoneSpecOf('here')), origin='here.', relativize=False)
from bisos.banna import tcpPorts
missing = [n for ip, n, _ in tcpPorts.hereEntries()
           if str(zone.find_rdataset(n + '.here.', 'A')[0]) != ip]
print('here. zone agrees with banna hereEntries' if not missing else f'MISMATCH: {missing}')
"

# --- Unbound (local resolver): read-only generation; nothing installed or switched ---
lpDo ../bin/unboundDns.cs
lpDo ../bin/unboundDns.cs -i unboundConfStdout
lpDo ../bin/unboundDns.cs -i resolvConfStdout
lpDo ../bin/unboundDns.cs -i nmDispatcherStdout
lpDo ../bin/unboundDns.cs -i browserPoliciesStdout
lpDo ../bin/unbound-sbom.pcs -i readme
lpDo ../bin/knotDns.cs -i knotZoneStdout intra
