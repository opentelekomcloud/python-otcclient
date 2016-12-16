#!/bin/sh
source ./otcfunc.sh
source ./otcconf.sh

apitest nova --insecure secgroup-create $TEST_SEC_GROUP "test sec group" 2>/dev/null 

apitest nova --insecure secgroup-list-rules $TEST_SEC_GROUP 2>/dev/null

