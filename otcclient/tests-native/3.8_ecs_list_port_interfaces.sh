#!/bin/sh
source ./otcfunc.sh

apitest neutron --insecure port-list 2>/dev/null | awk '/ip_address/ {print $2}'

