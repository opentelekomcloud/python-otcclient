# get avaliable addresses EIP address 
otc ecs describe-addresses

#  allocate public ip 
otc ecs allocate-address

# delete public ip 
otc ecs release-address --public-ip 160.44.196.167

# get port information of the VM 
otc ecs describe-network-interfaces --instance-name aaaaaaaaaaaaaa

# assing NIC to publicip 
otc ecs associate-address --public-ip 160.44.196.169 --network-interface-id 0f13a9ea-9436-465a-b798-efc6a89d3b2a

# list subnets
otc ecs describe-subnets

# list private ips of subnet 
otc ecs describe-private-addresses --subnet-name mysubnet --vpc-name myvpc

# list of bandwiths 
otc ecs describe_bandwiths 
