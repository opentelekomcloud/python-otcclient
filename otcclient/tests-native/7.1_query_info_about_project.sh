#!/bin/sh

source otcfunc.sh
source otcconf.sh

apitest keystone --insecure tenant-list 2>/dev/null
