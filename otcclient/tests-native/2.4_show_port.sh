#!/bin/sh

source otcfunc.sh
source otcconf.sh


apitest neutron --insecure net-create ${NETWORK_NAME} 2>/dev/null

NETWORK_ID=`neutron --insecure net-list 2>/dev/null|grep ${NETWORK_NAME}|awk '{print $2}'`


apitest neutron --insecure port-create ${NETWORK_NAME} --name ${PORT_NAME} 2>/dev/null
apitest neutron --insecure port-show  ${PORT_NAME} 2>/dev/null

apitest neutron --insecure port-delete ${PORT_NAME} 2>/dev/null


apitest neutron --insecure net-delete ${NETWORK_NAME} 2>/dev/null
