#!/bin/sh
source ./otcfunc.sh

TEST_SERVER=`nova --insecure list 2>/dev/null | grep TEST_SERVER | awk -F '|' '{print $3}'`

#list server flavor
ACT_FLAVOR=`nova --insecure show $TEST_SERVER 2>/dev/null | grep flavor | awk -F '|' '{print $3}' | awk -F '(' '{print $1}'`



	if [ $ACT_FLAVOR = "c1.medium" ];then
	NEW_FLAVOR="c2.medium"
		else
	NEW_FLAVOR="c1.medium"
	fi

apitest nova --insecure list 2>/dev/null
echo "Resizing from " $ACT_FLAVOR "to " $NEW_FLAVOR
apitest nova --insecure resize $TEST_SERVER $NEW_FLAVOR 2>/dev/null
apitest nova --insecure list 2>/dev/null

 
