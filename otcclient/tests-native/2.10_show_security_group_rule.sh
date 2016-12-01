#!/bin/sh

source otcfunc.sh
source otcconf.sh


apitest neutron --insecure security-group-list 2>/dev/null

apitest neutron --insecure security-group-create ${SECURITY_GROUP_NAME} 2>/dev/null

apitest neutron --insecure security-group-rule-create ${SECURITY_GROUP_NAME} --protocol tcp --port-range-min 23 --port-range-max 23 --remote-ip-prefix 172.31.0.224/28 2>/dev/null

SECURITY_RULE_ID_TO_SHOW=`neutron --insecure security-group-show ${SECURITY_GROUP_NAME} 2>/dev/null|awk -F "|" '{print $3}'|grep 172.31|tr -s "," '\n'|grep "\"id\":"|awk -F ":" '{print $2}'|tr -d '"'|tr -d  '}'`

apitest neutron --insecure security-group-rule-show ${SECURITY_RULE_ID_TO_SHOW} 2>/dev/null


apitest neutron --insecure security-group-show ${SECURITY_GROUP_NAME} 2>/dev/null

apitest neutron --insecure security-group-delete ${SECURITY_GROUP_NAME} 2>/dev/null
