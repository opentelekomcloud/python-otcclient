source ./otcclient/tests/otcfunc.sh 


apitest otc cce describe-namespaces --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].uuid"` 
apitest otc cce describe-namespaces --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].uuid"`  --namespace apitestnamespace 

apitest otc cce create-namespace --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].uuid"`  --namespace apitestnamespace 
apitest otc cce create-namespace  --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].uuid"`  --namespace apitestnamespace2 

apitest otc cce rename-namespace apitestnamespace2  --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].uuid"`  --namespace apitestnamespace3 

apitest otc cce describe-namespaces --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].uuid"` 


apitest otc cce delete-namespace --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].uuid"`  --namespace apitestnamespace
apitest otc cce delete-namespace --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].uuid"`  --namespace apitestnamespace3
