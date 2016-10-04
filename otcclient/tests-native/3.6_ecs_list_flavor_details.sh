#!/bin/sh
source ./otcfunc.sh

apitest nova --insecure flavor-list 2>/dev/null
