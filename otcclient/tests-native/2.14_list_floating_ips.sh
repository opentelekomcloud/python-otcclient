#!/bin/sh

source otcfunc.sh

apitest neutron --insecure floatingip-list 2>/dev/null


