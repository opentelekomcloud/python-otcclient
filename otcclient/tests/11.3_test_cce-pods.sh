#!/bin/bash

source ./otcclient/tests/otcfunc.sh 

apitest otc cce create-namespace --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].name"`  --namespace apitestnamespace 

apitest otc cce describe-pods --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].name"` 
apitest otc cce describe-pods --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].name"`  --namespace apitestnamespace

apitest otc cce create-pod  --cluster-name test-bed-node1  --namespace apitestnamespace --container-name testpod-nginx --pod testpod --image-name nginx --debug
apitest otc cce describe-pods --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].name"` 

apitest otc cce delete-pod  --cluster-name test-bed-node1  --namespace apitestnamespace --container-name testpod-nginx --pod testpod
apitest otc cce describe-pods --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].name"` 

apitest otc cce delete-namespace --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].name"`  --namespace apitestnamespace 


