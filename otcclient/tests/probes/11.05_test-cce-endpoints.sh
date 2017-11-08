#!/bin/bash

CLUSTER_NAME=$(otc cce describe-clusters --query "[0].[metadata][*].name")

apitest otc cce create-namespace --cluster-name $CLUSTER_NAME  --namespace apitestnamespace

apitest otc cce describe-endpoints  --cluster-name $CLUSTER_NAME  --namespace apitestnamespace
apitest otc cce describe-endpoints  --cluster-name $CLUSTER_NAME  

apitest otc cce create-endpoint  --cluster-name $CLUSTER_NAME --namespace apitestnamespace --endpoint-name servce-test02 --public-ip 10.240.106.152 --portmin 80

apitest otc cce describe-endpoints  --cluster-name $CLUSTER_NAME  --namespace apitestnamespace --endpoint-name servce-test02

apitest otc cce delete-endpoint  --cluster-name $CLUSTER_NAME --namespace apitestnamespace --endpoint-name servce-test02

apitest otc cce delete-namespace --cluster-name $CLUSTER_NAME  --namespace apitestnamespace

