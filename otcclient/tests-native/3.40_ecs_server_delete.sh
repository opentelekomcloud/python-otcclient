#!/bin/sh
source ./otcfunc.sh

TEST_SERVER=`nova --insecure list 2>/dev/null | grep TEST_SERVER | awk -F '|' '{print $3}'`


if [ "$TEST_SERVER" = ""  ]; then
	echo "Test Server does not exists.. creating.."
	exit
	else
	echo "Deleting" $TEST_SERVER 
	apitest nova --insecure delete $TEST_SERVER 2>/dev/null
fi
