#!/bin/sh
source ./otcfunc.sh

apitest nova --insecure flavor-show c1.medium 2>/dev/null
