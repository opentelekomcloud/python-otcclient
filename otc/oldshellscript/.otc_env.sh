#!/bin/sh
# == Module: Open Telekom Cloud Cli Interface Configuration 0.2
#
# Store OTC Command Line Configuration
#
# === Parameters 
# 
#export OS_PROJECT_NAME=eu-de
#export OS_USERNAME="NUMBER OTC000....."
#export OS_CACERT=/path/to/cacrt.pem
#export PASSWORD="your generated API key"
#export S3_ACCESS_KEY_ID=S3 KEY
#export S3_SECRET_ACCESS_KEY=S3 SECRET

# === Variables
#
# === Examples
# 
# === Authors
# 
# Zsolt Nagy <Z.Nagy@t-systems.com>
#
# === Copyright
#
# Copyright 2016 T-Systems International GmbH
#

# USER SPECIFIC SETTINGS #################################################################

# HAVE TO CHANGE! ######

# NEEDED FOR TOKEN AUTH
test -e ~/novarc && source ~/novarc
test -e ~/.ostackrc && source ~/.ostackrc
# These variables are in openstack environment format ...
export OS_PROJECT_NAME=eu-de
export OS_USERNAME="$OS_USERNAME"
export OS_PASSWORD="$OS_PASSWORD"
#export S3_ACCESS_KEY_ID=XXXXXXXXXXXXXXXXXXXX
#export S3_SECRET_ACCESS_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# export S3_HOSTNAME=obs.otc.t-systems.com
# Optionally use a proxy for s3 and curl
#export HTTPS_PROXY=
#export OS_CACERT=/path/to/cacrt.pem
export OS_USER_DOMAIN_NAME="${OS_USERNAME##* }"

# HAVE TO CHANGE END ######

# Defaults ( override from command line )

export SECUGROUPNAME="default"
export VPCNAME="default-vpc-MGr"
export SUBNETNAME="default-subnet"
export IMAGENAME="Standard_openSUSE_42.1_JeOS_100_latest"                
export NUMCOUNT=1
export INSTANCE_TYPE="computev1-1"
export INSTANCE_NAME="otcVM-$$"

# Password to inject (only works with some images)
export VOLUMETYPE="SATA"
export ADMINPASS="start"`date +%m%d`"!"
export CREATE_ECS_WITH_PUBLIC_IP="false"

export ECSACTIONTYPE="HARD"
export WAIT_CREATE="true"
##########################################################################################

