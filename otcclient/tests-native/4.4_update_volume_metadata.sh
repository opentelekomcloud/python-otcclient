#!/bin/sh

source otcfunc.sh
source otcconf.sh


apitest cinder --insecure create --name ${VOLUME_NAME} 5 2>/dev/null
sleep 10
apitest cinder --insecure metadata-show ${VOLUME_NAME} 2>/dev/null
apitest cinder --insecure metadata ${VOLUME_NAME} set aaa=bbb 2>/dev/null
sleep 5
apitest cinder --insecure metadata-show ${VOLUME_NAME} 2>/dev/null
apitest cinder --insecure delete ${VOLUME_NAME} 2>/dev/null
