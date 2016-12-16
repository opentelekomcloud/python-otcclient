#!/bin/sh
source ./otcfunc.sh
source ./otcconf.sh

TEST_SERVER=`nova --insecure list 2>/dev/null | grep TEST_SERVER | awk -F '|' '{print $3}'`

if [ "$TEST_SERVER" == "" ]; then
	echo "Test Server Does Not Exist"
	exit
fi

echo "Renaming Server"
apitest nova --insecure rename $TEST_SERVER $RENAME_SERVER 2>/dev/null
echo "Renaming Back"
sleep 5
apitest nova --insecure rename $RENAME_SERVER $TEST_SERVER 2>/dev/null

