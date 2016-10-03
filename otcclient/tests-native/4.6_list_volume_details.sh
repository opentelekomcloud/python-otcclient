#!/bin/sh

source otcfunc.sh


VOLUME_NAME=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 10 | head -n 1)_VOLUME

apitest cinder --insecure list 2>/dev/null
