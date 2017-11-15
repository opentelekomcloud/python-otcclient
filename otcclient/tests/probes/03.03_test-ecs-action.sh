#!/bin/bash

apitest otc ecs stop-instances --instance-name testinstance
sleep 30
apitest otc ecs start-instances --instance-name testinstance
sleep 30
apitest otc ecs reboot-instances --instance-name testinstance
sleep 30
