source ./otcclient/tests/otcfunc.sh 

apitest otc ecs describe-instances
# this could change 
# normal vm crreation
apitest otc ecs run-instances --count 1  --admin-pass yourpass123! --instance-type c1.medium --instance-name testinstance --image-name Standard_CentOS_6.7_latest --subnet-name testsubnet --vpc-name testvpc --group-name testsecgroup  --key-name testsshkeypair --file1 /otc/a=/otc/a 

apitest otc ecs describe-instances

# create with public IP 
apitest otc ecs run-instances --count 1  --admin-pass yourpass123! --instance-type c1.medium --instance-name testinstance-public --image-name Standard_CentOS_6.7_latest --subnet-name testsubnet --vpc-name testvpc --group-name testsecgroup  --key-name testsshkeypair --file1 /otc/a=/otc/a --associate-public-ip-address --wait-instance-running

apitest otc ecs describe-instances

# create with public IP wait the creation 
apitest otc ecs run-instances --count 1  --instance-type c1.medium --instance-name testinstance-publicw --image-name Standard_CentOS_6.7_latest --subnet-name mysubnet --vpc-name myvpc --group-name mytest  --key-name hadoop --file1 /otc/a=/otc/a  --wait-instance-running 

apitest otc ecs describe-instances

apitest otc ecs resize-instance --instance-type c2.medium --instance-name instancename-public