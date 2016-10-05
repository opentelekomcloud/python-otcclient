#!/bin/sh

source otcfunc.sh

SECURITY_GROUP_NAME=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 10 | head -n 1)_SECNAME


apitest neutron --insecure security-group-list 2>/dev/null

apitest neutron --insecure security-group-create ${SECURITY_GROUP_NAME} 2>/dev/null

apitest neutron --insecure security-group-rule-create --protocol tcp --port-range-min 23 --port-range-max 23 --remote-ip-prefix 172.31.0.224/28  ${SECURITY_GROUP_NAME}  2>/dev/null
apitest neutron --insecure security-group-rule-create  --protocol icmp --direction ingress ${SECURITY_GROUP_NAME} 2>/dev/null
apitest neutron --insecure security-group-rule-create  --protocol tcp --port-range-min 22 --port-range-max 22 --direction ingress ${SECURITY_GROUP_NAME}  2>/dev/null


apitest neutron --insecure security-group-rule-list 2>/dev/null
SECURITY_RULE_ID_TO_DELETE=`neutron --insecure security-group-show ${SECURITY_GROUP_NAME} 2>/dev/null|awk -F "|" '{print $3}'|grep 172.31|tr -s "," '\n'|grep "\"id\":"|awk -F ":" '{print $2}'|tr -d '"'|tr -d  '}'`

apitest neutron --insecure security-group-show ${SECURITY_GROUP_NAME} 2>/dev/null
apitest neutron --insecure security-group-list 2>/dev/null
apitest neutron --insecure security-group-rule-delete ${SECURITY_RULE_ID_TO_DELETE} #2>/dev/null

apitest neutron --insecure security-group-delete ${SECURITY_GROUP_NAME} 2>/dev/null
