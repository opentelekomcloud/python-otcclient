#!/bin/sh

source otcfunc.sh
source otcconf.sh


#curl -O http://download.cirros-cloud.net/0.3.4/cirros-0.3.4-x86_64-disk.img

apitest glance --insecure image-create --name ${IMAGE_NAME} --disk-format qcow2 --container-format ovf --file cirros-0.3.4-x86_64-disk.img 2>/dev/null

IMAGE_ID=`glance --insecure image-list 2>/dev/null|grep ${IMAGE_NAME}|awk '{print $2}'`


apitest glance --insecure image-update ${IMAGE_ID} --property name=${IMAGE_NAME_NEW} 2>/dev/null

sleep 10

apitest glance --insecure image-delete ${IMAGE_ID} 2>/dev/null

