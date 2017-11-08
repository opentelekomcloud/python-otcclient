#!/bin/bash

apitest otc ecs describe-instances

ID=$(otc ecs describe-instances --query "servers[?name == 'testinstance'].id")
apitest otc ecs describe-instances --instance-ids $ID
apitest otc ecs describe-instances --instance-name testinstance

apitest otc ecs describe-images
apitest otc ecs describe-flavors
apitest otc ecs describe-key-pairs
apitest otc ecs describe-quotas

