#!/bin/sh
source ./otcfunc.sh

TEST_SEC_GROUP=TEST_SEC_GROUP_$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 10 | head -n 1)

apitest nova --insecure secgroup-create $TEST_SEC_GROUP "test sec group" 2>/dev/null 

apitest nova --insecure secgroup-list-rules $TEST_SEC_GROUP 2>/dev/null

