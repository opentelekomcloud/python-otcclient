#!/bin/sh
source ./otcfunc.sh

apitest nova --insecure secgroup-list 2>/dev/null 

