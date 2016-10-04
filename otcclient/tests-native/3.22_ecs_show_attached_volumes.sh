#!/bin/sh
source ./otcfunc.sh

apitest cinder --insecure list 2>/dev/null

