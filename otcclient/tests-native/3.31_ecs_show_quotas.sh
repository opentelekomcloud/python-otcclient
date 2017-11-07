#!/bin/sh
source ./otcfunc.sh

apitest nova --insecure quota-show  2>/dev/null
