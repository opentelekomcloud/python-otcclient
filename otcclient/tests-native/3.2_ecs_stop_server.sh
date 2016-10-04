#!/bin/sh
VER=3.2

source ./otcfunc.sh

TEST_SERVER=`nova --insecure list 2>/dev/null | grep TEST_SERVER | awk -F '|' '{print $3}'`

apitest nova --insecure stop $TEST_SERVER 2>/dev/null
