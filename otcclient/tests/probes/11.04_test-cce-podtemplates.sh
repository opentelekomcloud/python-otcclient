#!/bin/bash

CLUSTER_NAME=$(otc cce describe-clusters --query "[0].[metadata][*].name")

apitest otc cce create-namespace --cluster-name $CLUSTER_NAME --namespace apitestnamespace --debug

apitest otc cce describe-pod-templates --cluster-name $CLUSTER_NAME --namespace apitestnamespace
apitest otc cce describe-pod-templates --cluster-name $CLUSTER_NAME --namespace apitestnamespace --pod testpod

apitest otc cce create-pod-template --cluster-name $CLUSTER_NAME --namespace apitestnamespace --container-name testpod-nginx --pod testpod --image-name nginx --portmin 80 --debug
apitest otc cce describe-pod-templates --cluster-name $CLUSTER_NAME --namespace apitestnamespace
apitest otc cce delete-pod-templates --cluster-name test-bed-node1 --namespace apitestnamespace --pod testpod
apitest otc cce describe-pod-templates --cluster-name $CLUSTER_NAME --namespace apitestnamespace

apitest otc cce delete-namespace --cluster-name $CLUSTER_NAME --namespace apitestnamespace
