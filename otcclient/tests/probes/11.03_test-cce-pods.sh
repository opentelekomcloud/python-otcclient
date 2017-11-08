#!/bin/bash

CLUSTER_NAME=$(otc cce describe-clusters --query "[0].[metadata][*].name")

apitest otc cce create-namespace \
	--cluster-name $CLUSTER_NAME \
	--namespace apitestnamespace 

apitest otc cce describe-pods \
	--cluster-name $CLUSTER_NAME 

apitest otc cce describe-pods \
	--cluster-name $CLUSTER_NAME \
	--namespace apitestnamespace

apitest otc cce create-pod \
	--cluster-name test-bed-node1 \
	--namespace apitestnamespace \
	--container-name testpod-nginx \
	--pod testpod \
	--image-name nginx \
	--debug

apitest otc cce describe-pods \
	--cluster-name $CLUSTER_NAME 

apitest otc cce delete-pod \
	--cluster-name test-bed-node1 \
	--namespace apitestnamespace \
	--container-name testpod-nginx \
	--pod testpod

apitest otc cce describe-pods \
	--cluster-name $CLUSTER_NAME 

apitest otc cce delete-namespace \
	--cluster-name $CLUSTER_NAME \
	--namespace apitestnamespace
