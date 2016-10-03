#!/bin/sh

source otcfunc.sh

apitest keystone --insecure tenant-list 2>/dev/null
