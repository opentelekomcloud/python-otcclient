#!/bin/bash

# get avaliable as groups 
apitest otc autoscaling describe-auto-scaling-groups 
apitest otc autoscaling describe-auto-scaling-groups-details --auto-scaling-group-name as-group-og62

apitest otc autoscaling describe-auto-scaling-configuration
# apitest otc autoscaling describe-auto-scaling-instances --auto-scaling-group-name test
# apitest otc autoscaling describe-policies --auto-scaling-group-name test
# apitest otc autoscaling describe-activitylog --auto-scaling-group-name test

apitest otc autoscaling describe-auto-scaling-instances --auto-scaling-group-name as-group-og62
apitest otc autoscaling describe-policies --auto-scaling-group-name as-group-og62
apitest otc autoscaling describe-activitylog --auto-scaling-group-name as-group-og62
apitest otc autoscaling describe-auto-scaling-configuration_details --scaling-configuration-name as-config-aulw
# apitest otc autoscaling describe-policy-details --auto-scaling-group-name as-group-og62

apitest otc autoscaling describe-quotas
apitest otc autoscaling describe-quotas-of-group  --auto-scaling-group-name as-group-og62

apitest otc autoscaling describe-auto-scaling-configuration

# apitest otc autoscaling create-auto-scaling-policy --auto-scaling-group-name test --scaling-policy-name test_policy_sched --scaling-policy-type SCHEDULED --launch-time 2019-12-14T03:34Z
# apitest otc autoscaling create-auto-scaling-policy --auto-scaling-group-name test --scaling-policy-name test_policy_recurr --scaling-policy-type RECURRENCE --launch-time 16:00 --recurrence-type Daily 

# apitest otc autoscaling create-auto-scaling-policy --auto-scaling-group-name as-group-og62 --scaling-policy-name test_policy_sched --scaling-policy-type SCHEDULED --launch-time 2019-12-14T03:34Z
# apitest otc autoscaling create-auto-scaling-policy --auto-scaling-group-name as-group-og62 --scaling-policy-name test_policy_recurr --scaling-policy-type RECURRENCE --launch-time 16:00 --recurrence-type Daily --end-time 2016-12-14T03:34Z

# apitest otc autoscaling create-auto-scaling-group --auto-scaling-group-name apitest --subnet-name mysubnet --vpc-name api-test1 --group-name mytest 
# apitest otc autoscaling create-auto-scaling-group --auto-scaling-group-name apitest --subnet-name apitestsubnet1 --vpc-name apitestrouter2 --group-name mytest
# apitest otc autoscaling create-auto-scaling-group --auto-scaling-group-name apitest --subnet-id 3fb48660-845d-44a6-9b06-02721b8c576e --vpc-name testvpc --security-group-ids 0023fedb-e842-4dcf-8f3f-2f980ab7ef1e
# apitest otc autoscaling create-auto-scaling-group --auto-scaling-group-name apitest --subnet-name testsubnet --vpc-name testvpc --group-name default
# apitest otc autoscaling create-auto-scaling-group --auto-scaling-group-name apitest --subnet-name testsubnet --vpc-name vpc-6c8a --group-name default

apitest otc autoscaling create-auto-scaling-group --auto-scaling-group-name apitest --subnet-name subnet-480d --vpc-name vpc-6c8a --group-name default

apitest otc autoscaling create-auto-scaling-policy --auto-scaling-group-name apitest --scaling-policy-name test_policy_recurr --scaling-policy-type RECURRENCE --launch-time 16:00 --recurrence-type Daily --end-time 2016-12-14T03:34Z
apitest otc autoscaling create-auto-scaling-policy --auto-scaling-group-name apitest  --scaling-policy-name test_policy_sched --scaling-policy-type SCHEDULED --launch-time 2019-12-14T03:34Z
apitest otc autoscaling describe-policies --auto-scaling-group-name apitest
apitest otc autoscaling describe-policy-details --scaling-policy-name test_policy_sched --auto-scaling-group-name apitest
apitest otc autoscaling modify-auto-scaling-policy --auto-scaling-group-name apitest --scaling-policy-name test_policy_sched --scaling-policy-type SCHEDULED --launch-time 2017-12-14T03:34Z --operation-as-policy SET # --count 1

apitest otc autoscaling disable-auto-scaling-policy --scaling-policy-name test_policy_recurr --auto-scaling-group-name apitest
apitest otc autoscaling describe-policies --auto-scaling-group-name apitest

# apitest otc autoscaling enable-auto-scaling-policy --scaling-policy-id 52e1e780-bc8f-48b8-9590-1c9f2b0d510b --auto-scaling-group-name as-group-og62
# apitest otc autoscaling describe-policies --auto-scaling-group-name as-group-og62

apitest otc autoscaling enable-auto-scaling-policy --scaling-policy-name test_policy_recurr --auto-scaling-group-name apitest

# apitest otc autoscaling delete-policies --scaling-policy-id 52e1e780-bc8f-48b8-9590-1c9f2b0d510b --auto-scaling-group-name as-group-og62
apitest otc autoscaling delete-policies --scaling-policy-name test_policy_recurr --auto-scaling-group-name apitest

# apitest otc autoscaling create-auto-scaling-configuration --auto-scaling-group-name apitest --subnet-name mysubnet --vpc-name myvpc --group-name mytest 
apitest otc autoscaling create-auto-scaling-configuration --scaling-configuration-name apitest2 --disk-type SYS --volume-type SATA --size 100 --key-name nzstestbed --image-name Standard_CentOS_7.2_latest --instance-type c1.medium
apitest otc autoscaling describe-auto-scaling-configuration
apitest otc autoscaling create-auto-scaling-configuration --scaling-configuration-name apitest4 --disk-type SYS --volume-type SATA --size 100 --key-name nzstestbed --image-name Standard_CentOS_7.2_latest --instance-type c1.medium
apitest otc autoscaling delete-auto-scaling-configuration --scaling-configuration-name apitest4
apitest otc autoscaling describe-auto-scaling-configuration
apitest otc autoscaling create-auto-scaling-configuration --scaling-configuration-name apitest4 --disk-type SYS --volume-type SATA --size 100 --key-name nzstestbed --image-name Standard_CentOS_7.2_latest --instance-type c1.medium
apitest otc autoscaling delete-auto-scaling-configuration --scaling-configuration-name apitest4
apitest otc autoscaling describe-auto-scaling-configuration
apitest otc autoscaling create-auto-scaling-configuration --scaling-configuration-name apitest4 --disk-type SYS --volume-type SATA --size 100 --key-name nzstestbed --image-name Standard_CentOS_7.2_latest --instance-type c1.medium
apitest otc autoscaling batch_delete-auto-scaling-configuration --scaling-configuration-name apitest4

apitest otc autoscaling describe-auto-scaling-groups
apitest otc autoscaling modify-auto-scaling-group --auto-scaling-group-name apitest --scaling-configuration-name apitest2 --max-instance-number 5
 
# --count 1
apitest otc autoscaling enable-auto-scaling-group --auto-scaling-group-name apitest

apitest otc autoscaling describe-auto-scaling-instances --auto-scaling-group-name apitest
# apitest otc ecs run-instances --count 1  --admin-pass yourpass123! --instance-type c1.medium --instance-name apitestinstance --image-name Standard_CentOS_7.2_latest --vpc-name vpc-6c8a --group-name default --subnet-name subnet-480d  --key-name nzstestbed --file1 /otc/a=/otc/a 
# --subnet-name testsubnet --vpc-name testvpc --group-name testsecgroup 
apitest otc ecs run-instances --count 1 --admin-pass yourpass123! --instance-type c1.medium --instance-name apitestinstance-public --image-name Standard_CentOS_6.8_latest --subnet-name subnet-480d --vpc-name vpc-6c8a --group-name default --key-name nzstestbed --associate-public-ip-address --wait-instance-running

apitest otc autoscaling batch-add-delete-auto-scaling-instances --auto-scaling-group-name apitest --instance-action-add-remove-batch ADD --instance-name apitestinstance-public
apitest otc autoscaling describe-auto-scaling-instances --auto-scaling-group-name apitest
sleep 15
apitest otc autoscaling delete-auto-scaling-instance_from_group --instance-name apitestinstance-public
apitest otc autoscaling describe-auto-scaling-instances --auto-scaling-group-name apitest

apitest otc autoscaling modify-auto-scaling-group --auto-scaling-group-name apitest --scaling-configuration-name apitest2 --max-instance-number 5 --count 0

apitest otc autoscaling execute-auto-scaling-policy --scaling-policy-name test_policy_sched --auto-scaling-group-name apitest

apitest otc autoscaling disable-auto-scaling-group --auto-scaling-group-name apitest
apitest otc autoscaling describe-auto-scaling-groups
sleep 15
apitest otc autoscaling delete-auto-scaling-group --auto-scaling-group-name apitest

apitest otc autoscaling batch_delete-auto-scaling-configuration --scaling-configuration-name apitest2
apitest otc autoscaling delete-policies --scaling-policy-name test_policy_sched --auto-scaling-group-name apitest
apitest otc ecs delete-instances --instance-name apitestinstance-public
# apitest otc ecs delete-instances --instance-name apitestinstance-public2
# apitest otc ecs run-instances --count 1 --admin-pass yourpass123! --instance-type c1.medium --instance-name testinstance-public --image-name Standard_CentOS_6.8_latest --subnet-name testsubnet --vpc-name testvpc --group-name testsecgroup  --key-name nzstestbed --associate-public-ip-address --wait-instance-running
#### TODO
# +Removing Instances from an AS Group

