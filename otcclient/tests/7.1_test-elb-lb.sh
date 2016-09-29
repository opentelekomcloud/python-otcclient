source ./otcclient/tests/otcfunc.sh 

apitest otc elb describe_quotas
apitest otc elb describe-load-balancers 
apitest otc elb describe-load-balancers --load-balancer-name myelb
apitest otc elb create-load-balancers --load-balancer-name myelb2 --vpc-name myvpc
apitest otc elb delete-load-balancers --load-balancer-name myelb2

