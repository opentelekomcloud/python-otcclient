#!/bin/sh
source ./otcfunc.sh


for i in `neutron --insecure port-list 2>/dev/null | awk '/ip_address/ {print $2}'`; do apitest neutron --insecure port-show $i 2>/dev/null; done;

