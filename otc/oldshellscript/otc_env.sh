#!/bin/sh
# == Module: Open Telekom Cloud Cli Interface Configuration 0.2
#
# Store OTC Command Line Configuration
#
# === Parameters 
# 
#export PROJECT_ID=1c95bf65e2724ebbb504abc8a46b0a03
#export USERNAME=YOUR USERNAME
#export PASSWORD="your password"
#export S3_ACCESS_KEY_ID=S3 KEY
#export S3_SECRET_ACCESS_KEY=S3 ACCESS 

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
# NEED FOR TOKEN AUTH
export PROJECT_ID=1c95bf65e2724ebbb504abc8a46b0a03
export USERNAME=ITSH_PIA
export PASSWORD="PIA12345_"
#NEED FOR S3 ONLY
export S3_ACCESS_KEY_ID=DDTGEXLQVNOMK0UXFHTQ
export S3_SECRET_ACCESS_KEY=0okfrHO4lQ7nNvBf29nmKd0dhOHFpFpdUIzO9YNE
# HAVE TO CHANGE END ######

#NEED FOR ECS DEFAULT ( if not add here have to specify in command line )

export SECUGROUPNAME="default"
export VPCNAME="default-vpc"
export SUBNETNAME="default-subnet"
export IMAGENAME="Community-CentOS-7.0-x86_64-2015-0"                
export NUMCOUNT=1
export INSTANCE_TYPE="computev1-1"
export INSTANCE_NAME="default"

export ADMINPASS="start"`date +%m%d`"!"
export CREATE_ECS_WITH_PUBLIC_IP="false"
export ECSACTIONTYPE="HARD"
export WAIT_CREATE="true"

##########################################################################################

