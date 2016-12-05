#!/bin/sh

source otcfunc.sh
source otcconf.sh


apitest cinder --insecure create --name ${VOLUME_NAME} 5 2>/dev/null
sleep 10
apitest cinder --insecure metadata-show ${VOLUME_NAME} 2>/dev/null
sleep 10
apitest cinder --insecure delete ${VOLUME_NAME} 2>/dev/null
