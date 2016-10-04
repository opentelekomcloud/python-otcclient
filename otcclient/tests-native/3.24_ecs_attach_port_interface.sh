#!/bin/sh
source ./otcfunc.sh

PORT_INTERFACE=TEST_PI_$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 10 | head -n 1)

apitest neutron --insecure port-create $PORT_INTERFACE 2>/dev/null

