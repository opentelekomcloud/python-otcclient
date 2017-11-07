#!/bin/sh
source ./otcfunc.sh

TEST_SERVER=`nova --insecure list 2>/dev/null | grep TEST_SERVER | awk -F '|' '{print $3}'`

for i in `nova --insecure instance-action-list $TEST_SERVER 2>/dev/null | grep req- |  awk -F '|' '{print $3}'`; do apitest nova --insecure instance-action $TEST_SERVER $i 2>/dev/null; done;
 
