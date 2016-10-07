source ./otcclient/tests/otcfunc.sh 

apitest otc cce describe-clusters 
apitest otc cce list-clusters 
apitest otc cce describe-clusters --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].name"`


apitest otc cce list-services  --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].name"`  

apitest otc cce list-container-instances  --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].name"`  


