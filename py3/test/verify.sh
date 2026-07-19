#!/bin/bash -i
#

# Safety check: must run from a directory named "test"
if [[ "$(basename "$PWD")" != "test" ]]; then
    echo "ERROR: verify.sh must be run from a directory named 'test'." >&2
    echo "  Current PWD: $PWD" >&2
    exit 1
fi

lpDo ../bin/capDns_seed.cs
lpDo ../bin/exmpl-here-dns.pcs
