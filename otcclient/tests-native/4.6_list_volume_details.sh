#!/bin/sh

source otcfunc.sh
source otcconf.sh

apitest cinder --insecure list 2>/dev/null
