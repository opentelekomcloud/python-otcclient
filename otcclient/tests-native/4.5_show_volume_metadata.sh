#!/bin/sh

source otcfunc.sh


VOLUME_NAME=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 10 | head -n 1)_VOLUME

apitest cinder --insecure create --name ${VOLUME_NAME} 5 2>/dev/null
sleep 10
apitest cinder --insecure metadata-show ${VOLUME_NAME} 2>/dev/null
sleep 10
apitest cinder --insecure delete ${VOLUME_NAME} 2>/dev/null
