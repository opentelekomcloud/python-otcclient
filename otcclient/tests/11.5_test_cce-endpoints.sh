source ./otcclient/tests/otcfunc.sh 

apitest otc cce create-namespace --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].name"`  --namespace apitestnamespace

apitest otc cce describe-endpoints  --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].name"`  --namespace apitestnamespace
apitest otc cce describe-endpoints  --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].name"`  

apitest otc cce create-endpoint  --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].name"` --namespace apitestnamespace --endpoint-name servce-test02 --public-ip 10.240.106.152 --portmin 80

apitest otc cce describe-endpoints  --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].name"`  --namespace apitestnamespace --endpoint-name servce-test02

apitest otc cce delete-endpoint  --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].name"` --namespace apitestnamespace --endpoint-name servce-test02

apitest otc cce delete-namespace --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].name"`  --namespace apitestnamespace

