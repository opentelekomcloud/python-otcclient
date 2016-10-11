#!/bin/sh
source ./otcfunc.sh

TEST_SERVER=`nova --insecure list 2>/dev/null | grep TEST_SERVER | awk -F '|' '{print $3}'`

VOLUME=`nova --insecure volume-list 2>/dev/null | grep available | awk -F "|" '{print $2}' | sort --random-sort | head -n 1`


if [ "$TEST_SERVER" == "" ]; then
        echo "Test Server Does Not Exist"
        exit
fi



echo "Attach Volume"
apitest nova --insecure volume-attach $TEST_SERVER $VOLUME 2</dev/null
sleep 5

echo "Detaching Volume"
apitest nova --insecure volume-detach $TEST_SERVER $VOLUME 2>/dev/null 
sleep 5

echo "List Attached Volumes"
nova --insecure volume-list 2>/dev/null | grep "in-use" | awk -F "|" '{print $2}'

