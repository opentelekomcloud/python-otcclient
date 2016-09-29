source ./otcclient/tests/otcfunc.sh 

apitest otc ecs stop-instances --instance-name testinstance
sleep 180 
apitest otc ecs start-instances --instance-name testinstance
sleep 180 
apitest otc ecs reboot-instances --instance-name testinstance
sleep 180 