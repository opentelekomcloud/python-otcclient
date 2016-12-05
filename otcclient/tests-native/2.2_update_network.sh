#!/bin/sh

source otcfunc.sh
source otcconf.sh


apitest neutron --insecure net-create ${NETWORK_NAME} 2>/dev/null

NETWORK_ID=`neutron --insecure net-list 2>/dev/null|grep ${NETWORK_NAME}|awk '{print $2}'`

apitest neutron --insecure net-update ${NETWORK_NAME} --name ${NETWORK_NAME_NEW} 2>/dev/null
apitest neutron --insecure net-show ${NETWORK_NAME_NEW}  2>/dev/null
apitest neutron --insecure net-delete ${NETWORK_NAME_NEW} 2>/dev/null
