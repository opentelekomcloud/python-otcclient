#!/bin/sh

source otcfunc.sh


VOLUME_NAME=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 10 | head -n 1)_VOLUME
SNAPSHOT_NAME=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 10 | head -n 1)_SNAPSHOT

apitest cinder --insecure create --name ${VOLUME_NAME} 5 2>/dev/null
sleep 10
apitest cinder --insecure show ${VOLUME_NAME} 2>/dev/null
apitest cinder --insecure snapshot-create ${VOLUME_NAME} --name ${SNAPSHOT_NAME} 2>/dev/null
sleep 20
apitest cinder --insecure snapshot-show ${SNAPSHOT_NAME} 2>/dev/null
sleep 10
apitest cinder --insecure snapshot-delete ${SNAPSHOT_NAME} 2>/dev/null
sleep 10
apitest cinder --insecure delete ${VOLUME_NAME} 2>/dev/null
