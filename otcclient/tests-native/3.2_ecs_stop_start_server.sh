#!/bin/sh

source ./otcfunc.sh

#checking test server if exists

check_test_server ()
{
TEST_SERVER=`nova --insecure list 2>/dev/null | grep TEST_SERVER | awk -F '|' '{print $3}'`


if [ "$TEST_SERVER" = ""  ]; then
        echo "Test Server does not exists.. creating.."
        echo "Executing 3.1_ecs_create_server.sh"
        ./3.1_ecs_create_server.sh
	
        else
        echo "Test Server" $TEST_SERVER "already exists"
fi
}

check_test_server

#waiting for test server to start running

TEST_SERVER=`nova --insecure list 2>/dev/null | grep TEST_SERVER | awk -F '|' '{print $3}'`

RUNNING=`nova --insecure list 2>/dev/null | grep TEST_SERVER | awk -F '|' '{print $6}'|tr -d '[:space:]'`
CR=0

	while [  "$RUNNING" != "Running" ]; do
		RUNNING=`nova --insecure list 2>/dev/null | grep TEST_SERVER | awk -F '|' '{print $6}'|tr -d '[:space:]'`
        	echo "Waiting for Test server to start running..." 
		echo $RUNNING
		sleep 5
		let CR=CR+1
		echo $CR
			if [ $CR -gt 30 ]; then
			echo "Looks like Server is not created or is unable to start running to perform Stop Test. Exiting Test..."
				exit
			fi
	done

#stopping test server
apitest nova --insecure stop $TEST_SERVER 2>/dev/null

CS=0
	while [  "$RUNNING" != "Shutdown" ]; do
                RUNNING=`nova --insecure list 2>/dev/null | grep TEST_SERVER | awk -F '|' '{print $6}'|tr -d '[:space:]'`
                echo "Waiting for Test server to shutdown..." 
                echo $RUNNING
                sleep 5
		let CS=CS+1
		echo $CS
			if [ $CS -gt 30 ]; then
				echo "Looks like Server is unable to stop to perform Start Test. Exiting..."
				exit
			fi
        done

#running test server back
apitest nova --insecure start $TEST_SERVER 2>/dev/null

RUNNING=`nova --insecure list 2>/dev/null | grep TEST_SERVER | awk -F '|' '{print $6}'|tr -d '[:space:]'`
CR=0
while [  $RUNNING != "Running" ]; do
                RUNNING=`nova --insecure list 2>/dev/null | grep TEST_SERVER | awk -F '|' '{print $6}'`
                echo "Waiting for Test server to start running..." 
                echo $RUNNING
                sleep 5
                let CR=CR+1
                echo $CR
                        if [ $CR -gt 30 ]; then
                        echo "Looks like Server is unable to start running to finish Start-Stop Test. Exiting Test..."
                                exit
                        fi
        done

