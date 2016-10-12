source ./otcclient/tests/otcfunc.sh 

# get avaliable as groups 
apitest otc autoscaling describe-auto-scaling-groups 
apitest otc autoscaling describe-auto-scaling-configuration
apitest otc autoscaling describe-auto-scaling-instances --auto-scaling-group-name test
apitest otc autoscaling describe-policies --auto-scaling-group-name test
apitest otc autoscaling describe-activitylog --auto-scaling-group-name test
apitest otc autoscaling describe-quotas

apitest otc autoscaling create-auto-scaling-policy --auto-scaling-group-name test --scaling-policy-name test_policy_sched --scaling-policy-type SCHEDULED --launch-time 2019-12-14T03:34Z
apitest otc autoscaling create-auto-scaling-policy --auto-scaling-group-name test --scaling-policy-name test_policy_recurr --scaling-policy-type RECURRENCE --launch-time 16:00 --recurrence-type Daily 


apitest otc autoscaling create-auto-scaling-group --auto-scaling-group-name apitest--subnet-name mysubnet --vpc-name myvpc --group-name mytest 



#### TODO
# +Deleting an AS Configuration
# Deleting an AS Group
# +Deleting an AS Policy
# +Removing Instances from an AS Group
# +Querying AS Configuration Details
# Querying AS Configurations
# +Querying AS Group Details
# Querying AS Groups
# Querying AS Policies
# +Querying AS Policy Details
# Querying Instances in an AS Group
# Querying Quotas for AS Groups and AS Configurations
# +Querying Quotas for AS Instances and AS Policies
# Querying Scaling Action Logs
# Batch Deleting AS Configurations
# Batch Removing or Adding Instances
# +++Creating an AS Configuration
# Creating an AS Group
# +Creating an AS Policy
# +Disabling an AS Group
# +Disabling an AS Policy
# +Enabling an AS Group
# +Enabling an AS Policy
# +Executing an AS Policy
# Modifying an AS Group
# Modifying an AS Policy
