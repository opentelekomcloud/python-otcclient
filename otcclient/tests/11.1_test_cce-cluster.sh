#!/bin/bash

source ./otcclient/tests/otcfunc.sh 

apitest otc cce describe-clusters 
apitest otc cce list-clusters 

apitest otc cce describe-clusters --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].name"`


apitest otc cce list-services  --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].name"`  

apitest otc cce list-container-instances  --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].name"`  

TEST_CLUSTER_NAME="testccecluster"
TEST_VPC_NAME="testvpc"
TEST_SUBNET_NAME="testsubnet"

apitest otc cce create-cluster  --cluster-name "$TEST_CLUSTER_NAME" --subnet-name "$TEST_SUBNET_NAME" --vpc-name "$TEST_VPC_NAME"  --description "test cce cluster"
 


