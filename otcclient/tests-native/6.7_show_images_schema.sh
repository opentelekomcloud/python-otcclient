#!/bin/sh

source otcfunc.sh
source otcconf.sh


apitest glance --insecure image-list 2>/dev/null

