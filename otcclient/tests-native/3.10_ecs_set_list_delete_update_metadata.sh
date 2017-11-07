#!/bin/sh

source ./otcfunc.sh

TEST_SERVER=`nova --insecure list 2>/dev/null | grep TEST_SERVER | awk -F '|' '{print $3}'`


apitest nova --insecure meta $TEST_SERVER set newmeta='Update meta data test' 2>/dev/null
apitest nova --insecure show $TEST_SERVER 2>/dev/null
#apitest nova --insecure meta $TEST_SERVER delete newmeta  2>/dev/null

