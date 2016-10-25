#!/bin/bash

source ./otcclient/tests/otcfunc.sh 

apitest otc ecs describe-instances --output text
apitest otc ecs describe-instances --output table
apitest otc ecs describe-instances --output Json

