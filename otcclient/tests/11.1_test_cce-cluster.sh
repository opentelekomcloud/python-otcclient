source ./otcclient/tests/otcfunc.sh 

apitest otc cce describe-clusters 
apitest otc cce list-clusters 
apitest otc cce describe-clusters --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].uuid"`


apitest otc cce list-services --cluster-name --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].uuid"`  

apitest otc cce list-container-instances --cluster-name --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].uuid"`  


apitest otc cce describe-namespaces --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].uuid"` 
apitest otc cce describe-namespaces --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].uuid"`  --namespace apitestnamespace 
apitest otc cce create-namespace --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].uuid"`  --namespace apitestnamespace 
apitest otc cce create-namespace  --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].uuid"`  --namespace apitestnamespace2 


apitest otc cce rename-namespace apitestnamespace2  --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].uuid"`  --namespace apitestnamespace3 

apitest otc cce describe-pods --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].uuid"` 
apitest otc cce describe-pods --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].uuid"`  --namespace apitestnamespace


apitest otc cce create-pod  --cluster-name test-bed-node1  --namespace apitestnamespace --container-name testpod-nginx --pod testpod --image-name nginx --debug
apitest otc cce create-pod-template  --cluster-name test-bed-node1  --namespace apitestnamespace --container-name testpod-nginx --pod testpod --image-name nginx --portmin 80 --debug
apitest otc cce describe-pod-templates  --cluster-name test-bed-node1  --namespace apitestnamespace --pod testpod
apitest otc cce describe-pod-templates  --cluster-name test-bed-node1  --namespace apitestnamespace
apitest otc cce delete-pod-templates  --cluster-name test-bed-node1  --namespace apitestnamespace --pod testpod


apitest otc cce describe-endpoints  --cluster-name test-bed-node1  --namespace apitestnamespace --endpoint-name servce-test01
apitest otc cce describe-endpoints  --cluster-name test-bed-node1  --namespace apitestnamespace
apitest otc cce describe-endpoints  --cluster-name test-bed-node1  

apitest otc cce create-endpoint  --cluster-name test-bed-node1 --namespace apitestnamespace --endpoint-name servce-test02 --public-ip 10.240.106.152 --portmin 80
apitest otc cce delete-endpoint  --cluster-name test-bed-node1 --namespace apitestnamespace --endpoint-name servce-test02


#cce rename-namespace  nzsnamespace --cluster-name test-bed-node1  --namespace nzsnamespace2 --debug

apitest otc cce delete-namespace --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].uuid"`  --namespace apitestnamespace
apitest otc cce delete-namespace --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].uuid"`  --namespace apitestnamespace3

