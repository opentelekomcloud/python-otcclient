#!/bin/sh
VER=1.1

apitest ()
{
    "$@"
    local status=$?
    if [ $status -ne 0 ]; then
        echo "error with $1" >&2
        echo "$@ => NOT OK " >>"hcp_test_result_$VER.txt"
    else
        echo "$@ => OK " >>"hcp_test_result_$VER.txt"
    fi
    return $status

}

echo "HCP TEST $VER" >"hcp_test_result_$VER.txt"
