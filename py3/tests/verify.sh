#!/bin/bash -i
#

# Safety check: must run from a directory named "tests"
if [[ "$(basename "$PWD")" != "tests" ]]; then
    echo "ERROR: verify.sh must be run from a directory named 'tests'." >&2
    echo "  Current PWD: $PWD" >&2
    exit 1
fi

lpDo ../bin/capDns_seed.cs
lpDo ../bin/airflow-here-dns.pcs
lpDo ../bin/airflow-here-dns.pcs -i capDns_verify
lpDo ../bin/airflow-here-dns.pcs -i capDns_update
lpDo cat /etc/hosts
lpDo ../bin/airflow-here-dns.pcs -i capDns_resolve  airflow.here
lpDo ../bin/airflow-here-dns.pcs -i capDns_fqdnPing  airflow.here
lpDo ping -c 3 airflow.here

