#!/bin/sh

source otcfunc.sh

VOLUME_NAME=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 10 | head -n 1)_VOLUME

apitest cinder --insecure create --name ${VOLUME_NAME} 5 2>/dev/null
sleep 10
VOLUME_ID=`cinder --insecure list 2>/dev/null|grep ${VOLUME_NAME}|awk '{print $2}'`

otc ecs create-snapshot --volume-name ${VOLUME_NAME}
sleep 15

SNAPSHOT_ID=`cinder --insecure snapshot-list 2>/dev/null|grep ${VOLUME_ID}|grep available|awk '{print $2}'`
i=0
while [ -z "$SNAPSHOT_ID" ] 
do
sleep 10
SNAPSHOT_ID=`cinder --insecure snapshot-list 2>/dev/null|grep ${VOLUME_ID}|grep available|awk '{print $2}'`
i=$((i+1))
if [ $i -eq 5 ];
then
exit
fi
done


BACKUP_ID=`cinder --insecure backup-list 2>/dev/null|grep ${SNAPSHOT_ID}|grep available|awk '{print $2}'`
j=0
while [ -z "$BACKUP_ID" ]
do
sleep 10
BACKUP_ID=`cinder --insecure backup-list 2>/dev/null|grep ${SNAPSHOT_ID}|grep available|awk '{print $2}'`
j=$((j+1))
if [ $j -eq 20 ];
then
exit
fi
done


sleep 5
apitest cinder --insecure backup-show ${BACKUP_ID} 2>/dev/null

sleep 10
apitest cinder --insecure backup-delete ${BACKUP_ID}  2>/dev/null
apitest cinder --insecure snapshot-delete ${SNAPSHOT_ID}  2>/dev/null

SNAP=`cinder --insecure snapshot-list 2>/dev/null|grep ${SNAPSHOT_ID}|awk '{print $2}'`
BACK=`cinder --insecure backup-list 2>/dev/null|grep ${BACKUP_ID}|awk '{print $2}'`
j=0
while [ -n "${SNAP}" ]
do
sleep 10
SNAP=`cinder --insecure snapshot-list 2>/dev/null|grep ${SNAPSHOT_ID}|awk '{print $2}'`
BACK=`cinder --insecure backup-list 2>/dev/null|grep ${BACKUP_ID}|awk '{print $2}'`
j=$((j+1))
if [ $j -eq 60 ];
then
exit
fi
done

apitest cinder --insecure delete ${VOLUME_NAME} 2>/dev/null
