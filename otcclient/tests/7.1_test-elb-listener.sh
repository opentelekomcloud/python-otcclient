source ./otcclient/tests/otcfunc.sh 

apitest otc elb describe-listeners --load-balancer-name elb-myot
apitest otc elb describe-health-check --load-balancer-name elb-myot
apitest otc elb describe-listeners --load-balancer-name elb-myot
apitest otc elb describe-members --listener-name listener-c67k
