#!/bin/sh
source ./otcfunc.sh

TEST_SERVER=`nova --insecure list 2>/dev/null | grep TEST_SERVER | awk -F '|' '{print $3}'`
INTERFC=`nova --insecure interface-list $TEST_SERVER 2>/dev/null | grep ACTIVE | awk -F '|' '{print $4}'| sort --random-sort | head -n 1 `


apitest nova --insecure interface-attach --net-id $INTERFC $TEST_SERVER 2>/dev/null

apitest nova --insecure interface-list $TEST_SERVER 2>/dev/null

apitest nova --insecure interface-detach --net-id $INTERFC $TEST_SERVER 2>/dev/null

