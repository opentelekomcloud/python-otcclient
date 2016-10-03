#!/bin/sh

source otcfunc.sh


apitest cinder --insecure snapshot-list  2>/dev/null
