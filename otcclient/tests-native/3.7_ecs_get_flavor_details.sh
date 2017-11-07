#!/bin/sh
source ./otcfunc.sh

FLAVOR=`nova --insecure flavor-list 2>/dev/null| grep True | awk -F '|' '{print $3}' | sort --random-sort | head -n 1`


apitest nova --insecure flavor-show $FLAVOR 2>/dev/null
