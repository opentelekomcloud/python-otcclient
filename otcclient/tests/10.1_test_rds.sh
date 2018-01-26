#!/bin/bash

source ./otcclient/tests/otcfunc.sh 

apitest otc rds describe-db-instances
apitest otc rds create-cluster  --key-name "testkey" --subnet-name "subnet-test" --vpc-name "vpc-test" --group-names "secugroup-test"  --admin-pass "rdspass123!#" --cluster-name "rdstestcluster"