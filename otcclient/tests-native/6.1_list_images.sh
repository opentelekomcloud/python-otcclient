#!/bin/sh

source otcfunc.sh
source otcconf.sh


apitest glance --insecure --get-schema image-list 2>/dev/null
