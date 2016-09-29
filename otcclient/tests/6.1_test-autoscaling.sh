source ./otcclient/tests/otcfunc.sh 

# get avaliable as groups 
apitest otc autoscaling describe-auto-scaling-groups 
apitest otc autoscaling describe-auto-scaling-configuration
apitest otc autoscaling describe-auto-scaling-instances --auto-scaling-group-name test
apitest otc autoscaling describe-policies --auto-scaling-group-name test
apitest otc autoscaling describe-activitylog --auto-scaling-group-name test
apitest otc autoscaling describe-quotas
