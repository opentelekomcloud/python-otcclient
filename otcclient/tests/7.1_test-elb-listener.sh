#!/bin/bash

source ./otcclient/tests/otcfunc.sh 

apitest otc elb create_listener --load-balancer-name apitestelb --listener-name listener-apitest --listener-description test --protocol HTTP --portmin 8888 --lb-algorithm roundrobin --backend-port 1888 --session-sticky false --sticky-session-type insert 

apitest otc elb describe-listeners --load-balancer-name apitestelb 
#--listener-name listener-apitest

apitest otc elb modify-listeners --load-balancer-name apitestelb --listener-name listener-apitest --listener-description test
apitest otc elb describe-listeners --load-balancer-name apitestelb --listener-name listener-apitest

apitest otc elb create-backend-member --load-balancer-name apitestelb  --listener-name listener-apitest --instance-name testinstance-public  --address 100.64.27.96
apitest otc elb describe-members --load-balancer-name apitestelb --listener-name listener-apitest

exit

apitest otc elb create-health-check --listener-name listener-apitest
apitest otc elb describe-health-check --listener-name listener-apitest
apitest otc elb modify-health-check --listener-name listener-apitest
apitest otc elb describe-health-check --listener-name listener-apitest

apitest otc elb delete-backend-member --listener-name listener-c67k --instance-name testinstance-public 
apitest otc elb delete-health-check --listener-name listener-c67k

apitest otc elb delete-listener --listener-name listener-apitest