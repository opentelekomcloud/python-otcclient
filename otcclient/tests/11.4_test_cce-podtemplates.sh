#!/bin/bash

source ./otcclient/tests/otcfunc.sh 

apitest otc cce create-namespace --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].name"`  --namespace apitestnamespace  --debug

apitest otc cce describe-pod-templates  --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].name"`  --namespace apitestnamespace
apitest otc cce describe-pod-templates  --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].name"`  --namespace apitestnamespace --pod testpod

apitest otc cce create-pod-template  --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].name"`  --namespace apitestnamespace --container-name testpod-nginx --pod testpod --image-name nginx --portmin 80 --debug
apitest otc cce describe-pod-templates  --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].name"`  --namespace apitestnamespace
apitest otc cce delete-pod-templates  --cluster-name test-bed-node1  --namespace apitestnamespace --pod testpod
apitest otc cce describe-pod-templates  --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].name"`  --namespace apitestnamespace

apitest otc cce delete-namespace --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].name"`  --namespace apitestnamespace

