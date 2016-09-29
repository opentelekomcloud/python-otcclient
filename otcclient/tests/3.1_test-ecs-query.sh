source ./otcclient/tests/otcfunc.sh 

apitest otc ecs describe-instances
# this could change 
apitest otc ecs describe-instances --instance-ids b6c602b1-06d0-4bdb-b764-5d43b47abc14 
apitest otc ecs describe-instances --instance-name myvm

apitest otc ecs describe-images
apitest otc ecs describe-flavors
apitest otc ecs describe-key-pairs
apitest otc ecs describe-quotas