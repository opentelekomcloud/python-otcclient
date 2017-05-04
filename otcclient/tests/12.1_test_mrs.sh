#!/bin/bash

#source ./otcclient/tests/otcfunc.sh 

#apitest otc ims create_image_metadata  --image-name testimagenzs --os-version "Ubuntu 14.04 server 64bit" --container-format bare --disk-format raw --min-disk 1 --min-ram 1024 --tags "test,image" --visibility private --protected false
#apitest otc ims register_image --image-url nzs2:c.qcow2  --image-name testimagenzs 
#apitest otc ims create_image --image-url nzs2:c.qcow2 --image-name testimagenzs9 --os-version "Ubuntu 14.04 server 64bit" --container-format bare --disk-format raw --min-disk 1 --min-ram 1024 --tags "test,image" --visibility private --protected false


#20....
otc mrs create-cluster  --key-name hadoop --subnet-name subnet-automation --vpc-name vpc-automation  --cluster-name mrstestcluster --debug