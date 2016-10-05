source ./otcclient/tests/otcfunc.sh 

apitest otc elb describe_quotas
apitest otc elb describe-load-balancers 
apitest otc elb create-load-balancers --load-balancer-name apitestelb --vpc-name testvpc

apitest otc elb describe-load-balancers --load-balancer-name apitestelb

apitest otc elb modify-load-balancers --load-balancer-name apitestelb --listener-description test --bandwith 20

apitest otc elb delete-load-balancers --load-balancer-name apitestelb

