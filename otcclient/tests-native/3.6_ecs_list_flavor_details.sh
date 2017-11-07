#!/bin/sh
source ./otcfunc.sh
source ./otcconf.sh
#check_testserver
apitest nova --insecure flavor-list 2>/dev/null
