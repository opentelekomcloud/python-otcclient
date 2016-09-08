# get avaliable as groups 
otc autoscaling describe-auto-scaling-groups 
otc autoscaling describe-auto-scaling-configuration
otc autoscaling describe-auto-scaling-instances --auto-scaling-group-name test
otc autoscaling describe-policies --auto-scaling-group-name test
otc autoscaling describe-activitylog --auto-scaling-group-name test
otc autoscaling describe-quotas
