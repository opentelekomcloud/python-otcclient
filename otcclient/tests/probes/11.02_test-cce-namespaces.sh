#!/bin/bash

CLUSTER_NAME=$(otc cce describe-clusters --query "[0].[metadata][*].name")

apitest otc cce describe-namespaces \
	--cluster-name $CLUSTER_NAME \
	--debug

apitest otc cce describe-namespaces \
	--cluster-name $CLUSTER_NAME \
	--namespace apitestnamespace 

apitest otc cce create-namespace \
	--cluster-name $CLUSTER_NAME \
	--namespace apitestnamespace 

apitest otc cce create-namespace \
	--cluster-name $CLUSTER_NAME \
	--namespace apitestnamespace2 

apitest otc cce rename-namespace apitestnamespace2 \
	--cluster-name $CLUSTER_NAME \
	--namespace apitestnamespace3 

apitest otc cce describe-namespaces \
	--cluster-name $CLUSTER_NAME 

apitest otc cce delete-namespace \
	--cluster-name $CLUSTER_NAME \
	--namespace apitestnamespace

apitest otc cce delete-namespace \
	--cluster-name $CLUSTER_NAME \
	--namespace apitestnamespace3
