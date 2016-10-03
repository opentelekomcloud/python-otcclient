#!/bin/sh

source otcfunc.sh


apitest neutron --insecure security-group-list 2>/dev/null
