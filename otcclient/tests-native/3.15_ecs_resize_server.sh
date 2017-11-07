#!/bin/sh
source ./otcfunc.sh

TEST_SERVER=`nova --insecure list 2>/dev/null | grep TEST_SERVER | awk -F '|' '{print $3}'`

#list server flavor
ACT_FLAVOR=`nova --insecure show $TEST_SERVER 2>/dev/null | grep flavor | awk -F '|' '{print $3}' | awk -F '(' '{print $1}'`

NEW_FLAVOR=`nova --insecure flavor-list 2>/dev/null| grep True | awk -F '|' '{print $3}' | sort --random-sort | head -n 1`

echo "........." $TEST_SERVER $ACT_FLAVOR "..............."

check_flavor()
{
	if [ "$ACT_FLAVOR" = $NEW_FLAVOR ];then
	NEW_FLAVOR=`nova --insecure flavor-list 2>/dev/null| grep True | awk -F '|' '{print $3}' | sort --random-sort | head -n 1`
	check_flavor
	fi
}


apitest nova --insecure list 2>/dev/null
echo "Resizing from " $ACT_FLAVOR "to " $NEW_FLAVOR
apitest nova --insecure resize $TEST_SERVER $NEW_FLAVOR 2>/dev/null
apitest nova --insecure list 2>/dev/null

 
