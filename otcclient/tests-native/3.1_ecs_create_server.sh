#!/bin/sh
source ./otcfunc.sh

SERVER_NAME=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 10 | head -n 1)_TEST_SERVER
TEST_SERVER=`nova --insecure list 2>/dev/null | grep TEST_SERVER | awk -F '|' '{print $3}'`

FLAVOR=`nova --insecure flavor-list 2>/dev/null| grep True | awk -F '|' '{print $3}' | sort --random-sort | head -n 1`

IMAGE=`nova --insecure image-list 2>/dev/null | grep ACTIVE | awk -F '|' '{print $2}'| sort --random-sort | head -n 1`

if [ "$TEST_SERVER" = ""  ]; then
	echo "Test Server does not exists.. creating.."
apitest nova --insecure boot --flavor $FLAVOR --image $IMAGE $SERVER_NAME 2>/dev/null
	else
	echo "Test Server" $TEST_SERVER "already exists"
	exit
fi
echo $FLAVOR
echo $IMAGE

