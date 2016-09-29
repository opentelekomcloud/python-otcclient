source ./otcclient/tests/otcfunc.sh 

apitest otc ecs stop-instances --instance-ids b6c602b1-06d0-4bdb-b764-5d43b47abc14
sleep 300 
apitest otc ecs start-instances --instance-ids b6c602b1-06d0-4bdb-b764-5d43b47abc14
sleep 300 
apitest otc ecs reboot-instances --instance-ids b6c602b1-06d0-4bdb-b764-5d43b47abc14
sleep 300 