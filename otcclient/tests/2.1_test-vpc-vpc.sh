source ./otcclient/tests/otcfunc.sh 

apitest otc ecs describe-vpcs
apitest otc ecs create-vpc --vpc-name testvpc --cidr 10.0.0.0/10
apitest otc ecs describe-vpcs
apitest otc ecs delete-vpc --vpc-name testvpc