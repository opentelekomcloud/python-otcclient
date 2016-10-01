source ./otcclient/tests/otcfunc.sh 

apitest otc cce describe-clusters 
apitest otc cce list-clusters 
apitest otc cce describe-clusters --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].uuid"`


apitest cce list-services --cluster-name --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].uuid"`  

apitest cce list-container-instances --cluster-name --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].uuid"`  


apitest cce describe-namespaces --cluster-name --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].uuid"` 
apitest cce describe-namespaces --cluster-name --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].uuid"`  --namespace apitestnamespace 
apitest cce create-namespace --cluster-name --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].uuid"`  --namespace apitestnamespace 

apitest cce delete-namespace --cluster-name --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].uuid"`  --namespace apitestnamespace