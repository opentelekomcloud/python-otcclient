#!/bin/sh
source ./otcfunc.sh

for i in `nova --insecure secgroup-list 2>/dev/null | grep TEST_SEC_GROUP* | awk -F '|' '{print $2}'`; do apitest nova --insecure secgroup-delete $i 2>/dev/null; done;

