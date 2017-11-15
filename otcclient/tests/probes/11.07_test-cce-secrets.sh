#!/bin/bash

CLUSTER_NAME=$(otc cce describe-clusters --query "[0].[metadata][*].name")

apitest otc cce create-secret  --cluster-name $CLUSTER_NAME  --namespace apitestnamespace --secret-name apitestsecret --key-name "YWRtaW4=" --admin-pass MWYyZDFlMmU2N2Rm --secret-name apitestsecret --debug

apitest otc cce describe-secrets   --cluster-name $CLUSTER_NAME  --namespace apitestnamespace --secret-name apitestsecret --debug 

apitest otc cce delete-secret --cluster-name $CLUSTER_NAME  --namespace apitestnamespace --secret-name apitestsecret
