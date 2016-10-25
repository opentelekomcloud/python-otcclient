#!/bin/bash

source ./otcclient/tests/otcfunc.sh 

apitest otc ces describe-alarms 
apitest otc ces list-metrics 
apitest otc ces list-favorite-metrics 
apitest otc ces list-metric-data
apitest otc ces describe-quotas
