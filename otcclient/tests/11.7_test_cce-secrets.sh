source ./otcclient/tests/otcfunc.sh 



apitest otc cce describe-secrets   --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].name"`  --namespace apitestnamespace

apitest otc cce create-secrets   --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].name"`  --namespace apitestnamespace --secret-name apitestsecret --portmin 8765 --portmax 9376


apitest otc cce delete-secrets --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].name"`  --namespace apitestnamespace --secret-name apitestsecret