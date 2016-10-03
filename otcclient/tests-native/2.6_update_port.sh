#!/bin/sh

source otcfunc.sh


NETWORK_NAME=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 10 | head -n 1)_NETWORK
PORT_NAME=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 10 | head -n 1)_PORT
PORT_NAME_NEW=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 10 | head -n 1)_PORT


apitest neutron --insecure net-create ${NETWORK_NAME} 2>/dev/null

NETWORK_ID=`neutron --insecure net-list 2>/dev/null|grep ${NETWORK_NAME}|awk '{print $2}'`


apitest neutron --insecure port-create ${NETWORK_NAME} --name ${PORT_NAME} 2>/dev/null
apitest neutron --insecure port-update ${PORT_NAME} --name ${PORT_NAME_NEW} 2>/dev/null
apitest neutron --insecure port-show  ${PORT_NAME_NEW} 2>/dev/null


apitest neutron --insecure port-delete ${PORT_NAME_NEW} 2>/dev/null


apitest neutron --insecure net-delete ${NETWORK_NAME} 2>/dev/null
