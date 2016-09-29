#!/bin/sh
source ./otcclient/tests/VER
apitest ()
{
    echo "$@"
    "$@"
    local status=$?
    if [ $status -ne 0 ]; then
        echo "error with $1" >&2
        echo "$@ => NOT OK " >>"$TEST-$VER.txt"
    else
        echo "$@ => OK " >>"$TEST-$VER.txt"
    fi
    return $status

}

