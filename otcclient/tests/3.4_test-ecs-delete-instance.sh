source ./otcclient/tests/otcfunc.sh 

apitest otc ecs delete-instances --instance-name testinstance-publicw
apitest otc ecs delete-instances --instance-name testinstance
apitest otc ecs delete-instances --instance-name testinstance-public