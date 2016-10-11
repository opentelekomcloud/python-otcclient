source ./otcclient/tests/otcfunc.sh 

apitest otc ecs describe-subnets
apitest otc ecs create-subnet --subnet-name mysubnet --cidr 10.0.0.0/8 --gateway-ip 10.0.0.2 --primary-dns 8.8.8.8 --secondary-dns 8.8.4.4 --availability-zone eu-de-01 --vpc-name myvpc
apitest otc ecs describe-subnets
apitest otc ecs delete-subnet --subnet-name mysubnet