#!/bin/sh

source ./nativefunc.sh 

apitest neutron --insecure net-list
apitest neutron --insecure net-create apitestnet
apitest neutron --insecure subnet-list
apitest neutron failtest-example
apitest neutron --insecure subnet-create apitestnet 192.168.2.0/24 --name apitestsubnet1
apitest neutron --insecure subnet-show  apitestsubnet1


apitest neutron --insecure router-list
apitest neutron --insecure router-create apitestrouter
apitest neutron --insecure router-create apitestrouter2
apitest neutron --insecure router-show apitestrouter 
apitest neutron --insecure router-list
apitest neutron --insecure router-interface-add apitestrouter apitestsubnet1
apitest neutron --insecure router-show apitestrouter 
apitest neutron --insecure router-update  apitestrouter2 --name apitestrouter3
apitest neutron --insecure router-delete apitestrouter
apitest neutron --insecure router-delete apitestrouter3


apitest neutron --insecure floatingip-list
apitest neutron floatingip-show --insecure `neutron floatingip-list --quiet --insecure -c id --format csv|tail -1| tr -d '"'`

apitest neutron --insecure security-group-list
apitest neutron --insecure security-group-create apitestsecgroup
apitest neutron --insecure security-group-create apitestsecgroup2
apitest neutron --insecure security-group-rule-create apitestsecgroup --protocol tcp --port-range-min 23 --port-range-max 23 --remote-ip-prefix 172.31.0.224/28
apitest neutron --insecure security-group-show apitestsecgroup
apitest neutron --insecure security-group-update apitestsecgroup2 --name apitestsecgroup3
apitest neutron --insecure security-group-list
apitest neutron --insecure security-group-delete apitestsecgroup3
apitest neutron --insecure security-group-delete apitestsecgroup
apitest neutron --insecure security-group-list
apitest nova --insecure keypair-list

apitest neutron port-create apitestsubnet1 --name apitestport

apitest nova --insecure boot --image Standard_CentOS_7.2_latest --flavor c1.medium apitestinstance --nic net-id=`neutron net-list --quiet --insecure  --format csv|grep apitestnet| tr -d '"' | awk -F',' '{print $1}'`

apitest nova --insecure delete apitestinstance
apitest nova --insecure rename apitestinstance apitestinstance2

apitest neutron --insecure subnet-delete apitestsubnet1
apitest neutron --insecure net-delete apitestnet
