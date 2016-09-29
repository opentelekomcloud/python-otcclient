source ./otcclient/tests/otcfunc.sh 

apitest otc ecs describe-volumes
# this could change 
apitest otc ecs create-volume  --availability-zone eu-de-01 --count 1 --volume-name myvolume58  --size 100 --volume-type SATA
apitest otc ecs describe-volumes
apitest otc ecs create-volume  --availability-zone eu-de-02 --count 1 --volume-name myvolume59  --size 100 --volume-type SATA
apitest otc ecs describe-volumes


apitest otc ecs delete-volume  --volume-name myvolume58
#otc ecs delete-volume  --volume-id 8c0de9a7-9f61-4613-a68a-21f456cb7298
