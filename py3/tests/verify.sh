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

