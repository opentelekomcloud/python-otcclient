source ./otcclient/tests/otcfunc.sh 

# get avaliable addresses EIP address 
apitest otc ecs describe-addresses

#  allocate public ip 
apitest otc ecs allocate-address

# delete public ip 
apitest otc ecs release-address --public-ip 160.44.196.167

# get port information of the VM 
apitest otc ecs describe-network-interfaces --instance-name aaaaaaaaaaaaaa

# assing NIC to publicip 
apitest otc ecs associate-address --public-ip 160.44.196.169 --network-interface-id 0f13a9ea-9436-465a-b798-efc6a89d3b2a

# list subnets
apitest otc ecs describe-subnets

# list private ips of subnet 
apitest otc ecs describe-private-addresses --subnet-name mysubnet --vpc-name myvpc
apitest otc ecs release-private-addresses --private-ip-id 0f13a9ea-9436-465a-b798-efc6a89d3b2a

# list of bandwiths 
apitest otc ecs describe_bandwiths 
