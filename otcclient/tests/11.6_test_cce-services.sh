source ./otcclient/tests/otcfunc.sh 



apitest otc cce list-services  --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].name"`  

apitest otc cce create-service  --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].name"`  --namespace apitestnamespace --service-name apitestservice --portmin 8765 --portmax 9376

apitest otc cce modify-service  --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].name"`  --namespace apitestnamespace --service-name apitestservice --portmin 8765 --portmax 9999

apitest otc cce list-services  --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].name"`  --namespace apitestnamespace --service-name apitestservice

apitest otc cce delete-service  --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].name"`  --namespace apitestnamespace --service-name apitestservice 


