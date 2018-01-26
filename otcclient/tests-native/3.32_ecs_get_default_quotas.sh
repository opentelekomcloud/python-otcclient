#!/bin/sh
source ./otcfunc.sh

apitest nova --insecure quota-defaults  2>/dev/null
