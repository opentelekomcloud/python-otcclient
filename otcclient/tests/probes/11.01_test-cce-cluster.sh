#!/bin/bash

apitest otc cce describe-clusters 
apitest otc cce list-clusters 

CLUSTER_NAME=$(otc cce describe-clusters --query "[0].[metadata][*].name")

apitest otc cce describe-clusters \
	--cluster-name $CLUSTER_NAME

apitest otc cce list-services \
	--cluster-name $CLUSTER_NAME

apitest otc cce list-container-instances \
	--cluster-name $CLUSTER_NAME

TEST_CLUSTER_NAME="testccecluster"
TEST_VPC_NAME="testvpc"
TEST_SUBNET_NAME="testsubnet"

apitest otc cce create-cluster \
	--cluster-name "$TEST_CLUSTER_NAME" \
	--subnet-name "$TEST_SUBNET_NAME" \
	--vpc-name "$TEST_VPC_NAME" \
	--description "test cce cluster"
