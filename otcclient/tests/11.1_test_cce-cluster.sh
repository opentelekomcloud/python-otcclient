source ./otcclient/tests/otcfunc.sh 

apitest otc cce describe-clusters 
apitest otc cce describe-clusters --cluster-name `otc cce describe-clusters --query  "[0].[metadata][*].uuid"`