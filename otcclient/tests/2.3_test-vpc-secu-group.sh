#!/bin/bash

source ./otcclient/tests/otcfunc.sh 

apitest otc ecs describe-security-groups
apitest otc ecs create-security-group --group-name mytest --vpc-name myvpc
apitest otc ecs describe-security-groups
apitest otc ecs delete-security-group --group-name mytest --vpc-name myvpc
apitest otc ecs describe-security-groups
