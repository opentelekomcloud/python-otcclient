#!/bin/sh
source ./otcfunc.sh

check_server_running
TEST_SERVER=`nova --insecure list 2>/dev/null | grep TEST_SERVER | awk -F '|' '{print $3}'`
apitest nova --insecure reboot $TEST_SERVER 2>/dev/null
sleep 5
check_server_running
nova --insecure list 2>/dev/null | grep TEST_SERVER | awk -F '|' '{print $6}'
