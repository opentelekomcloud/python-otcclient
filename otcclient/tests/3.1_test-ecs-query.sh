source ./otcclient/tests/otcfunc.sh 

apitest otc ecs describe-instances
# this could change 
apitest otc ecs describe-instances --instance-ids `otc ecs describe-instances --query  "servers[?name == 'testinstance'].id"`
apitest otc ecs describe-instances --instance-name testinstance

apitest otc ecs describe-images
apitest otc ecs describe-flavors
apitest otc ecs describe-key-pairs
apitest otc ecs describe-quotas