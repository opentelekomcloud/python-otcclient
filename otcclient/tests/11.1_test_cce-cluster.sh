source ./otcclient/tests/otcfunc.sh 

apitest otc cce describe-clusters 
apitest otc cce list-clusters 
apitest otc cce describe-clusters --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].uuid"`


apitest otc cce list-services --cluster-name --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].uuid"`  

apitest otc cce list-container-instances --cluster-name --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].uuid"`  


