rem get avaliable addresses EIP address 
..\bin\otc ecs describe-addresses

rem  allocate public ip 
..\bin\otc ecs allocate-address

rem delete public ip 
..\bin\otc ecs release-address --public-ip 160.44.196.167

rem get port information of the VM 
..\bin\otc ecs describe-network-interfaces --instance-name aaaaaaaaaaaaaa

rem assing NIC to publicip 
..\bin\otc ecs associate-address --public-ip 160.44.196.169 --network-interface-id 0f13a9ea-9436-465a-b798-efc6a89d3b2a

rem list subnets
..\bin\otc ecs describe-subnets

rem list private ips of subnet 
..\bin\otc ecs describe-private-addresses --subnet-name mysubnet --vpc-name myvpc

rem list of bandwiths 
..\bin\otc ecs describe_bandwiths 
