#!/bin/sh

source otcfunc.sh


apitest neutron --insecure port-list 2>/dev/null
