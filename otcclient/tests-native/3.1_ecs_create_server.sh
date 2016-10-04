#!/bin/sh
source ./otcfunc.sh

SERVER_NAME=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 10 | head -n 1)_TEST_SERVER
TEST_SERVER=`nova --insecure list 2>/dev/null | grep TEST_SERVER | awk -F '|' '{print $3}'`


if [ "$TEST_SERVER" = ""  ]; then
	echo "Test Server does not exists.. creating.."
apitest nova --insecure boot --flavor c1.medium --image 4bc34621-0b50-42cd-a8e8-ab6ac9a2cadf $SERVER_NAME 2>/dev/null
	else
	echo "Test Server" $TEST_SERVER "already exists"
fi
