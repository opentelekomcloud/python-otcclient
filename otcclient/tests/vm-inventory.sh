#!/bin/bash

vm_filter="$1"

subnet_detail=$(otc ecs describe-subnets --output text)
vpc_detail=$(otc ecs describe-vpcs --output text)
publicip_detail=$(otc ecs describe-addresses --output text)
flavor_detail=$(otc ecs describe-flavors --output text)

echo 'tenantid,vm,id,"networks([VPC;Subnet;EIP[bandwith];Private IP])",status,flavor_id,secgroup,keyname,az,flavor,cpu,mem,image_name,os_version,size'
 
for vm in $(otc ecs describe-instances --query "servers[*].name")
do 
 temp_string=$vm
 
 if [ -n "$vm_filter" ] ; then 
  if test "${temp_string#*$vm_filter}" == "$temp_string" ; then
   continue;
  fi
 fi

 instance_detail=$(otc ecs describe-instances --instance-name $(echo $vm) --output text)
 
 tenantid=$(echo "$instance_detail"  |awk '$1 ~ /^.tenant_id$/ { print $2 }')
 id=$(echo "$instance_detail"  |awk '$1 ~ /^.id*$/ { print $2 }')
 ip_addr=$(echo "$instance_detail"  |awk '$1 ~ /\.addr$/ { print $2 }' | tr '\n' ';')
 status=$(echo "$instance_detail"  |awk '$1 ~ /\.status$/ { print $2 }')
 flavor_id=$(echo "$instance_detail"  |awk '$1 ~ /\.flavor.id$/ { print $2 }')
 secgroup=$(echo "$instance_detail"  |awk '$1 ~ /\.security_groups.name$/ { print $2 }'| tr '\n' ';')
 keyname=$(echo "$instance_detail"  |awk '$1 ~ /\.key_name$/ { print $2 }')
 az=$(echo "$instance_detail"  |awk '$1 ~ /\:availability_zone$/ { print $2 }')
 flavor=$(echo "$instance_detail" |awk '$1 ~ /\.flavor.id$/ { print $2 }')
 disk_id=$(echo "$instance_detail" |awk '$1 ~ /volumes_attached.id$/ { print $2 }')

 image_name=$(otc ecs describe-volumes --query  "volumes[?id == '$(echo $disk_id)'].volume_image_metadata.image_name")
 os_version=$(otc ecs describe-volumes --query  "volumes[?id == '$(echo $disk_id)'].volume_image_metadata.__os_version")
 size=$(otc ecs describe-volumes --query  "volumes[?id == '$(echo $disk_id)'].size")
 
 mem=$(echo "$flavor_detail" | grep $flavor |awk '{ print $2 }')
 cpu=$(echo "$flavor_detail" | grep $flavor |awk '{ print$3 }')
 
 networkinterface_detail=$(otc ecs describe_network_interfaces --instance-name $(echo $vm) --output text)
 
 otcnetinfo=""
 IFS=';';ary=($ip_addr)
 
 for ip in "${ary[@]}"; do 
  subnetid=$(echo "$networkinterface_detail" | grep -w $ip | awk 'NF>1{print $NF}')  
  subnetname=$(echo "$subnet_detail" | grep $subnetid |awk '{ print $2 }')
  vpcid=$(echo "$subnet_detail" | grep $subnetid |awk '{ print $6 }')
  vpc=$(echo "$vpc_detail" | grep $vpcid |awk '{ print $3 }')
  
  publicip=$(echo "$publicip_detail" | grep -w $ip |awk '{ print $2 }')
  bandwith=$(echo "$publicip_detail" | grep -w $ip |awk '{ print $8 }')
  
  
  publicip_bandwith=""
  if [ -n $publicip ] ; then 
	publicip_bandwith="$publicip[$bandwith]"    
  fi
  otcnetinfo="$otcnetinfo$vpc;$subnetname;$publicip_bandwith;$ip|"   
 done
 
 echo "$tenantid,$(echo $vm),$id,$otcnetinfo,$status,$flavor_id,$secgroup,$keyname,$az,$flavor,$cpu,$mem,$image_name,$os_version,$size"
 echo "$tenantid,$(echo $vm),$id,\"$otcnetinfo\",$status,$flavor_id,$secgroup,$keyname,$az,$flavor,$cpu,$mem,$image_name,$os_version,$size"
  
done 