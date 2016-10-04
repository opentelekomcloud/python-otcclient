#!/bin/sh
source ./otcfunc.sh

TEST_SERVER=`nova --insecure list 2>/dev/null | grep TEST_SERVER | awk -F '|' '{print $3}'`

FL=`nova --insecure list 2>/dev/null | grep $TEST_SERVER | grep -E 'resize_finish|VERIFY_RESIZE' | awk -F '|' '{print $2}'`
echo $FL;
if [ "$FL" = '' ]; then
	echo "It looks that server resize is still not finished or resize not started, try again later when server status is in \"resize_finish\""
	echo "For starting Resize test use 3.15_ecs_resize_server.sh"
	echo ""
	nova --insecure list 2>/dev/null | grep $TEST_SERVER
	echo ""
		else
	echo "Resize Reverting..."
	apitest nova --insecure resize-revert $FL 2>/dev/null
 	fi
