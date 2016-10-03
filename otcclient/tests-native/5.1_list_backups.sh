#!/bin/sh

source otcfunc.sh


apitest cinder --insecure backup-list 2>/dev/null
