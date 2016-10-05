#!/bin/sh

source ./otcfunc.sh

apitest neutron --insecure net-list 2>/dev/null
