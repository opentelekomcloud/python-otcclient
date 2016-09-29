source ./otcclient/tests/otcfunc.sh 

apitest otc ecs describe-vpcs
apitest ecs create-vpc --vpc-name testvpc --cidr 10.0.0.0/10
apitest otc ecs describe-vpcs