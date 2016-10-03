#!/bin/sh

source otcfunc.sh

ROUTER_NAME=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 10 | head -n 1)_ROUTER
SUBNET_NAME=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 10 | head -n 1)_SUBNET
ROUTER_INTERFACE_NAME=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 10 | head -n 1)_INTERFACE

NETWORK_NAME=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 10 | head -n 1)_NETWORK


apitest neutron --insecure net-create ${NETWORK_NAME} 2>/dev/null

NETWORK_ID=`neutron --insecure net-list 2>/dev/null|grep ${NETWORK_NAME}|awk '{print $2}'`

apitest neutron --insecure subnet-create ${NETWORK_NAME} 192.168.2.0/24 --name ${SUBNET_NAME}  2>/dev/null



apitest neutron --insecure router-create ${ROUTER_NAME} 2>/dev/null

apitest neutron --insecure router-interface-add ${ROUTER_NAME} ${SUBNET_NAME}  2>/dev/null

#apitest neutron --insecure router-show ${ROUTER_NAME} 2>/dev/null

apitest neutron --insecure router-interface-delete ${ROUTER_NAME} ${SUBNET_NAME} 2>/dev/null


apitest neutron --insecure router-delete ${ROUTER_NAME} 2>/dev/null

apitest neutron --insecure subnet-delete  ${SUBNET_NAME} 2>/dev/null
apitest neutron --insecure net-delete ${NETWORK_NAME}  2>/dev/null
