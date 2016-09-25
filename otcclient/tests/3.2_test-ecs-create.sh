otc ecs describe-instances
# this could change 
# normal vm crreation
otc ecs run-instances --count 1  --admin-pass yourpass123! --instance-type c1.medium --instance-name instancename --image-name Standard_CentOS_6.7_latest --subnet-name testsubnet --vpc-name testvpc --group-name testsecgroup  --key-name testsshkeypair --file1 /otc/a=/otc/a 

otc ecs describe-instances

# create with public IP 
otc ecs run-instances --count 1  --admin-pass yourpass123! --instance-type c1.medium --instance-name instancename-public --image-name Standard_CentOS_6.7_latest --subnet-name testsubnet --vpc-name testvpc --group-name testsecgroup  --key-name testsshkeypair --file1 /otc/a=/otc/a --associate-public-ip-address --wait-instance-running

otc ecs describe-instances

# create with public IP wait the creation 
otc ecs run-instances --count 1  --instance-type c1.medium --instance-name instancename-public --image-name Standard_CentOS_6.7_latest --subnet-name mysubnet --vpc-name myvpc --group-name mytest  --key-name hadoop --file1 /otc/a=/otc/a  --wait-instance-running 

otc ecs describe-instances

otc ecs resize-instance --instance-type c2.medium --instance-name instancename-public