#!/bin/bash

source ./otcclient/tests/otcfunc.sh 

# todo this have to change with query to handle automatically 
apitest otc ecs attach-volume  --instance-ids 94fe497d-90c2-4311-8b0e-10ed759089d3 --volume-id b21845e8-fc1e-45fa-a947-e378a08b1765   --device /dev/sdb

apitest otc ecs describe-volumes

# todo this have to change with query to handle automatically 
apitest otc ecs detach-volume  --instance-ids f344b625-6f73-44f8-ad56-9fcb05a523c4 --volume-id 8c0de9a7-9f61-4613-a68a-21f456cb7298
apitest otc ecs describe-volumes

apitest otc ecs describe-instances --instance-name myvm

