#!/bin/sh

source ./otcfunc.sh

check_server_running()
{
        RUNNING=`nova --insecure list 2>/dev/null | grep TEST_SERVER | awk -F '|' '{print $6}'|tr -d '[:space:]'`
CR=0
while [ "$RUNNING" != "Running" ]; do
                RUNNING=`nova --insecure list 2>/dev/null | grep TEST_SERVER | awk -F '|' '{print $6}'|tr -d '[:space:]'`
                echo "Waiting for Test server to start running..." 
                echo $RUNNING
                sleep 5
                let CR=CR+1
                echo $CR
                        if [ $CR -gt 30 ]; then
                        echo "Looks like Server is unable to start running. Exiting Test..."
                                exit
                        fi
        done
}

check_server_running

TEST_SERVER=`nova --insecure list 2>/dev/null | grep TEST_SERVER | awk -F '|' '{print $3}'`

apitest nova --insecure reboot --hard $TEST_SERVER 2>/dev/null

sleep 5

check_server_running
#nova --insecure list 2>/dev/null | grep TEST_SERVER | awk -F '|' '{print $6}'|tr -d '[:space:]'
