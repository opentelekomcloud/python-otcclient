source ./otcclient/tests/otcfunc.sh 

apitest otc elb describe-listeners --load-balancer-name apitestelb --vpc-name testvpc --debug
apitest otc elb describe-health-check --healthcheck-id 134e5ea962327c6a574b83e6e7f31f35
apitest otc elb describe-listeners --load-balancer-name elb-myot
#apitest otc elb describe-members --listener-name listener-c67k
#apitest otc elb describe-members --listener-name listener-c67k
#apitest otc elb create-backend-member --listener-name listener-c67k --instance-name testinstance-public  --address 100.64.27.96
#apitest otc elb delete-backend-member --listener-name listener-c67k --instance-name testinstance-public 
#apitest otc elb create-health-check --listener-name listener-c67k
#apitest otc elb modify-health-check --healthcheck-id 134e5ea962327c6a574b83e6e7f31f35
#apitest otc elb modify-listeners --listener-name listener-c67k --listener-description test