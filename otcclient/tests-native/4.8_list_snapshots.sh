#!/bin/sh

source otcfunc.sh
source otcconf.sh

apitest cinder --insecure snapshot-list  2>/dev/null
