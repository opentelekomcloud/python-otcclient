#!/bin/bash

apitest otc mrs create-cluster \
	--key-name hadoop \
	--subnet-name subnet-automation \
	--vpc-name vpc-automation \
	--cluster-name mrstestcluster \
	--debug
