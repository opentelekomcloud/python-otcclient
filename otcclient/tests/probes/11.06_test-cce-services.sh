#!/bin/bash

CLUSTER_NAME=$(otc cce describe-clusters --query "[0].[metadata][*].name")

apitest otc cce list-services  --cluster-name $CLUSTER_NAME  

apitest otc cce create-service  --cluster-name $CLUSTER_NAME  --namespace apitestnamespace --service-name apitestservice --portmin 8765 --portmax 9376

apitest otc cce modify-service  --cluster-name $CLUSTER_NAME  --namespace apitestnamespace --service-name apitestservice --portmin 8765 --portmax 9999

apitest otc cce list-services  --cluster-name $CLUSTER_NAME  --namespace apitestnamespace --service-name apitestservice

apitest otc cce delete-service  --cluster-name $CLUSTER_NAME  --namespace apitestnamespace --service-name apitestservice 


