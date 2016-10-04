#!/bin/sh
source ./otcfunc.sh

TEST_SERVER=`nova --insecure list 2>/dev/null | grep TEST_SERVER | awk -F '|' '{print $3}'`

apitest nova --insecure lock $TEST_SERVER 2>/dev/null
sleep 5 
