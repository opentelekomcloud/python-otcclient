#!/bin/sh

source ./otcfunc.sh

TEST_SERVER=`nova --insecure list 2>/dev/null | grep TEST_SERVER | awk -F '|' '{print $3}'`

apitest nova --insecure reboot --hard $TEST_SERVER 2>/dev/null
