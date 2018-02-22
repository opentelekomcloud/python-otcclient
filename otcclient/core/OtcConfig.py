#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of OTC Tool released under MIT license.
# Copyright (C) 2016 T-systems Kurt Garloff, Zsolt Nagy

import os

class OtcConfig(object):

    instance_ = None

    #  for singleton instances
    def __init__(self):
        pass

    @classmethod
    def getInstance(cls):
        if cls.instance_ == None:
            cls.instance_ = OtcConfig()
        return cls.instance_

    from os.path import expanduser
    os.environ
    home = expanduser("~")
    OTC_USER_DIR = home + "/.otc"
    OTC_USER_FILE = OTC_USER_DIR + "/config"
    OTC_PROXY_FILE = OTC_USER_DIR + "/common"

    DEBUG = None

    #  replace real AK
    ak = None

    #  replace real SK
    sk = None

    #  default region definition
    region = "eu-de"

    #  replace real service name
    serviceName = "serviceName"
    PROJECT_ID = None
    PROJECT_NAME = "eu-de"

    # public static String SERVER_ID;
    USERNAME = str()
    PASSWORD = str()
    DOMAIN = str()
    ECSTASKID = str()
    SECUGROUPNAME = None
    REGION = None
    VPCNAME = None
    SUBNETNAME = None
    IMAGENAME = None

    IMAGE_URL = None
    TAG_LIST = None
    PROTECTED = None
    OS_VERSION = None
    MIN_RAM = None
    MIN_DISK = None
    IMAGE_VISIBILITY = None
    DISK_FORMAT = None
    CONTAINTER_FORMAT = None
    CONTAINTER_FORMAT
    
    NUMCOUNT = "1"
    INSTANCE_TYPE = None
    INSTANCE_TYPE_NAME = None
    INSTANCE_NAME = None
    INSTANCE_ID = None
    TAG_PAIR = None
    DBTYPE = None
    DBVERSION = None
    DATASTORE_ID = None
    FLAVORID = None

    LOADBALANCER_NAME = None
    LOADBALANCER_ID = None

    LISTENER_NAME = None
    LISTENER_ID = None
    
    ALARM_NAME = None 
    ALARM_ID = None 

    SCALINGGROUP_NAME = None
    SCALINGGROUP_ID = None

            
    ADMINPASS = None
    CREATE_ECS_WITH_PUBLIC_IP = False
    ECSACTIONTYPE = "HARD"
    WAIT_CREATE = False
    KEYNAME = None
    PUBLICKEY = ""
    VOLUME_SIZE = int()
    VOLUME_TYPE = str()
    VOLUME_NAME = None
    DATA_VOLUMES = None
    VOLUME_ID = None
    ATTACHMENT_ID = str()
    EVS_DEVICE = str()
    VOLREP_NAME = None
    VOLREP_PRI = None
    VOLUME_ID1 = None
    VOLUME_ID2 = None
    REPLICATION_ID = None

    # main commands
    MAINCOM = None
    SUBCOM = None
    SUBCOM_P1 = None
    SUBCOM_P2 = None
    ECSACTION = None
    DEFAULT_HOST = "46.29.103.37"
    DEFAULT_OBS_HOST = "obs.otc.t-systems.com"
    
    S3_HOSTNAME = str()
    USER_DATA = None
    USER_DATA_PATH = None
    FILE1 = None
    FILE2 = None
    FILE3 = None
    FILE4 = None
    FILE5 = None
    GWIP = str()
    PRIMARYDNS = str()
    SECDNS = str()
    AZ = "eu-de-01"
    VPCID = None
    CIDR = None
    DIRECTION = str()
    PORTMIN = None
    ETHERTYPE = str()
    PORTMAX = None
    PROTOCOL = str()
    SECUGROUP = None
    IMAGE_ID = str()
    SUBNETID = None
    NETWORKINTERFACEID = str()
    ECSCREATEJOBSTATUS = str()
    TOKEN = str()
    #  proxy settings
    PROXY_URL = str()
    PROXY_PORT = int()
    #  S3 settings 
    S3BUCKET = str()
    S3OBJECT = str()
    S3RECURSIVE = False
    OUTPUT_FORMAT = "table"
    #  backups 
    SNAPSHOTID = "null"
    DESCRIPTION = str()
    PRIVATEIPID = None
    PUBLICIPID = None
    PUBLICIP = None
    DELETE_PUBLICIP = "true"
    DELETE_VOLUME = "true"
    QUERY = None
    SOURCE_GROUP_ID = None
    SOURCE_GROUP = None

    CLUSTER_ID = None
    CLUSTER = None

    NAMESPACE_ID = None
    NAMESPACE = None
    POD = None
    CONTAINER_NAME = None    
    SERVICE_NAME = None
    ENDPOINT_NAME = None
    SECRET_NAME = None
    RC_NAME = None
    
    CLIINPUTJSONFILE = None


    #hodigy
    #add_backend_member.template
    #delete_backend_member.template
    #SERVER_ID = None  ## INSTANCE_ID
    ADDRESS = None
    #apply_private_ip_address.template
    #SUBNETID
    IP_ADDRESS = None
    #create_as_configuration.template
    #SCALINGGROUP_NAME
    #FLAVOR_REF = None
    IMAGE_REF = None
    DISK_SIZE = None
    #VOLUME_TYPE
    DISK_TYPE = None
    #KEYNAME
    #create_as_group.template
    SCALING_CONFIGURATION_ID = None
    DESIRE_INSTANCE_NUMBER = None
    MIN_INSTANCE_NUMBER = None
    MAX_INSTANCE_NUMBER = None
    COOL_DOWN_TIME = None
    HEALTH_PERIODIC_AUDIT_METHOD = None
    HEALTH_PERIODIC_AUDIT_TIME = None
    INSTANCE_TERMINATE_POLICY = None
    #VPCID
    NETWORKS_ID = None
    NOTIFICATIONS = None
    SECURITY_GROUPS_ID = None
    #creating_health_check_task.template
    HEALTHCHECK_CONNECT_PORT = None
    HEALTHCHECK_INTERVAL = None
    HEALTHCHECK_PROTOCOL = None
    HEALTHCHECK_TIMEOUT = None
    HEALTHCHECK_URI = None
    HEALTHY_THREAHOLD = None
    #LISTENER_ID
    UNHEALTHY_THRESHOLD = None

    #disable_enable_as_group.template
    ACTION_DISABLE_ENABLE_AS_GROUP = None
    #modify_as_group.template
    #modify_information_health_check_task.template
    HEALTHCHECK_ID = None
    #modify_information_listener.template
    LISTENER_NAME = None
    LISTENER_DESCRIPTION = None
    LISTENER_PORT = None
    BACKEND_PORT = None
    LB_ALGORITHM = None
    #modify_load_balancer.template
    BANDWIDTH = None
    ADMIN_STATE_UP = None
    #query_as_configuration_details.template

    SCALING_CONFIGURATION_NAME = None
    #ADMINPASS
    PERSONALITY = None
    #INSTANCE_NAME
    #INSTANCE_ID
    #PUBLICIP
    #USER_DATA
    CREATE_TIME = None
    #query_as_group_details.template
    DETAIL = None
    #SCALINGGROUP_ID
    SCALING_GROUP_STATUS = None
    CURRENT_INSTANCE_NUMBER = None
    #LB_LISTENER_ID = None
    IS_SCALING = None
    #DELETE_PUBLICIP
    #update_bandwidth_information.template
    BANDWIDTH_SIZE = None
    #update_elastic_ip_address_information.template
    PUBLICIP_PORT_ID = None
    #update_subnet_information.template
    #SUBNETNAME
    DHCP_ENABLE = None
    #PRIMARYDNS
    #SECDNS
    #update_vpc_information.template
    #VPCNAME
    #CIDR
    #add_nics_ecs_batches.template
    SECURITY_GROUP_ID = None
    #batch_remove_add_instance.template
    INSTANCE_ACTION_ADD_REMOVE_BATCH = None
    INSTANCE_ID_1 = None
    INSTANCE_ID_2 = None
    INSTANCE_DELETE = None
    #create_as_policy.template
    RECURRENCE_VALUE = None
    START_TIME = None
    LAUNCH_TIME = None
    END_TIME = None
    RECURRENCE_TYPE = None
    SCALING_POLICY_TYPE = None
    INSTANCE_NUMBER = None
    OPERATION_AS_POLICY = None


    SCALING_POLICY_NAME = None
    SCALING_POLICY_ID = None
    #delete_nics_ecs_batches.template
    #NETWORKINTERFACEID
    #execute_enable_disable_as_policy.template
    AS_POLICY_ACTION = None
    #expand_capacity_on_evs_disk.template
    EVS_NEW_SIZE = None
    #modify_as_policy.template
    #modify_spec_ecs.template
    #restore_disk_vbs_backup.template
    #VOLUME_ID
    #update_evs_info.template
    #VOLUME_NAME
    #DESCRIPTION
    #create_listener.template
    SESSION_STICKY = None
    STICKY_SESSION_TYPE = None
    COOKIE_TIMEOUT = None


    
    @classmethod
    def isdefined(self, value):
        try:
            if(value != None):
                return value
        except NameError:
            return None
    
    @classmethod
    def copyfromparser(self, parser):
        self.DEBUG = parser.DEBUG                                               if parser.DEBUG else None
        
        self.SECUGROUPNAME = parser.SECUGROUPNAME                               if parser.SECUGROUPNAME else None
        self.REGION = parser.REGION                                             if parser.REGION else None
        self.VPCNAME = parser.VPCNAME                                           if parser.VPCNAME else None
        self.SUBNETNAME = parser.SUBNETNAME                                     if parser.SUBNETNAME else None
        self.IMAGENAME = parser.IMAGENAME                                       if parser.IMAGENAME else None
        self.IMAGE_URL = parser.IMAGE_URL                                       if parser.IMAGE_URL else None
                
        self.TAG_LIST = parser.TAG_LIST                                         if parser.TAG_LIST else None
        self.PROTECTED = parser.PROTECTED                                       if parser.PROTECTED else None
        self.OS_VERSION = parser.OS_VERSION                                     if parser.OS_VERSION else None
        self.MIN_RAM = parser.MIN_RAM                                           if parser.MIN_RAM else None
        self.MIN_DISK = parser.MIN_DISK                                         if parser.MIN_DISK else None
        self.IMAGE_VISIBILITY = parser.IMAGE_VISIBILITY                         if parser.IMAGE_VISIBILITY else None
        self.DISK_FORMAT = parser.DISK_FORMAT                                   if parser.DISK_FORMAT else None
        self.CONTAINTER_FORMAT = parser.CONTAINTER_FORMAT                       if parser.CONTAINTER_FORMAT else None
        
        
        
        self.NUMCOUNT = parser.NUMCOUNT                                         if parser.NUMCOUNT else str()
        # self.INSTANCE_TYPE_ = parser.INSTANCE_TYPE                               if parser.INSTANCE_TYPE else str()
        self.INSTANCE_TYPE_NAME = parser.INSTANCE_TYPE_NAME                     if parser.INSTANCE_TYPE_NAME else str()
        self.INSTANCE_NAME = parser.INSTANCE_NAME                               if parser.INSTANCE_NAME else None
        self.INSTANCE_ID = parser.INSTANCE_ID                                   if parser.INSTANCE_ID else None
        self.TAG_PAIR = parser.TAG_PAIR                                         if parser.TAG_PAIR else None
        self.DBTYPE = parser.DBTYPE                                             if parser.DBTYPE else None
        self.DBVERSION = parser.DBVERSION                                       if parser.DBVERSION else None
        self.DATASTORE_ID = parser.DATASTORE_ID                                 if parser.DATASTORE_ID else None
        self.FLAVORID = parser.FLAVORID                                         if parser.FLAVORID else None
        self.LOADBALANCER_NAME = parser.LOADBALANCER_NAME                               if parser.LOADBALANCER_NAME else None
        self.LOADBALANCER_ID = parser.LOADBALANCER_ID                                   if parser.LOADBALANCER_ID else None
        self.LISTENER_NAME = parser.LISTENER_NAME                               if parser.LISTENER_NAME else None
        self.LISTENER_ID = parser.LISTENER_ID                                   if parser.LISTENER_ID else None
        
        self.ALARM_NAME = parser.ALARM_NAME                               if parser.ALARM_NAME else None
        self.ALARM_ID = parser.ALARM_ID                                   if parser.ALARM_ID else None

        self.SCALINGGROUP_NAME = parser.SCALINGGROUP_NAME                 if parser.SCALINGGROUP_NAME else None
        self.SCALINGGROUP_ID = parser.SCALINGGROUP_ID                     if parser.SCALINGGROUP_ID else None

        self.CLUSTER = parser.CLUSTER                 if parser.CLUSTER else None
        self.CLUSTER_ID = parser.CLUSTER_ID                     if parser.CLUSTER_ID else None
        self.NAMESPACE = parser.NAMESPACE                 if parser.NAMESPACE else None
        self.POD = parser.POD                             if parser.POD else None
        self.CONTAINER_NAME = parser.CONTAINER_NAME                             if parser.CONTAINER_NAME else None
        self.SERVICE_NAME = parser.SERVICE_NAME                                 if parser.SERVICE_NAME else None
        self.ENDPOINT_NAME = parser.ENDPOINT_NAME                                 if parser.ENDPOINT_NAME else None
        self.SECRET_NAME = parser.SECRET_NAME                                 if parser.SECRET_NAME else None
        self.RC_NAME = parser.RC_NAME                                 if parser.RC_NAME else None
        
                
        self.ADMINPASS = parser.ADMINPASS                                        if parser.ADMINPASS else str()
        self.CREATE_ECS_WITH_PUBLIC_IP = parser.CREATE_ECS_WITH_PUBLIC_IP        if parser.CREATE_ECS_WITH_PUBLIC_IP else str()
        # self.ECSACTIONTYPE = parser.ECSACTIONTYPE                               if parser.ECSACTIONTYPE else str()
        self.WAIT_CREATE = parser.WAIT_CREATE                                   if parser.WAIT_CREATE else False
        self.KEYNAME = parser.KEYNAME                                            if parser.KEYNAME else str()
        self.PUBLICKEY = parser.PUBLICKEY                                       if parser.PUBLICKEY else str()
        self.VOLUME_SIZE = parser.VOLUME_SIZE                                   if parser.VOLUME_SIZE else str()
        self.VOLUME_TYPE = parser.VOLUME_TYPE                                   if parser.VOLUME_TYPE else None
        self.VOLUME_NAME = parser.VOLUME_NAME                                   if parser.VOLUME_NAME else None
        self.DATA_VOLUMES = parser.DATA_VOLUMES                                   if parser.DATA_VOLUMES else None
        
        self.VOLUME_ID = parser.VOLUME_ID                                       if parser.VOLUME_ID else None
        self.ATTACHMENT_ID = parser.ATTACHMENT_ID                               if parser.ATTACHMENT_ID else str()
        self.EVS_DEVICE = parser.EVS_DEVICE                                     if parser.EVS_DEVICE else str()
        self.VOLREP_NAME = parser.VOLREP_NAME                                   if parser.VOLREP_NAME else None
        self.VOLREP_PRI = parser.VOLREP_PRI                                     if parser.VOLREP_PRI else None
        self.VOLUME_ID1 = parser.VOLUME_ID1                                     if parser.VOLUME_ID1 else None
        self.VOLUME_ID2 = parser.VOLUME_ID2                                     if parser.VOLUME_ID2 else None
        self.REPLICATION_ID = parser.REPLICATION_ID                             if parser.REPLICATION_ID else None
        self.MAINCOM = parser.MAINCOM                                           if parser.MAINCOM else None
        self.SUBCOM = parser.SUBCOM                                              if parser.SUBCOM else None
        self.SUBCOM_P1 = parser.SUBCOM_P1                                        if parser.SUBCOM_P1 else None
        self.SUBCOM_P2 = parser.SUBCOM_P2                                        if parser.SUBCOM_P2 else None        
        # self.ECSACTION= parser.ECSACTION                                        if parser.ECSACTION else str()
        self.USER_DATA_PATH = parser.USER_DATA_PATH                              if parser.USER_DATA_PATH else None
        self.FILE1 = parser.FILE1                                                if parser.FILE1 else None
        self.FILE2 = parser.FILE2                                                if parser.FILE2 else None
        self.FILE3 = parser.FILE3                                                if parser.FILE3 else None
        self.FILE4 = parser.FILE4                                                if parser.FILE4 else None
        self.FILE5 = parser.FILE5                                                if parser.FILE5 else None
        self.GWIP = parser.GWIP                                                 if parser.GWIP else str()
        self.PRIMARYDNS = parser.PRIMARYDNS                                     if parser.PRIMARYDNS else str()
        self.SECDNS = parser.SECDNS                                             if parser.SECDNS else str()
        self.AZ = parser.AZ                                                     if parser.AZ else self.AZ
        self.VPCID = parser.VPCID                                               if parser.VPCID else None
        self.CIDR = parser.CIDR                                                  if parser.CIDR else str()
        self.DIRECTION = parser.DIRECTION                                       if parser.DIRECTION else str()
        self.PORTMIN = parser.PORTMIN                                           if parser.PORTMIN else None
        self.ETHERTYPE = parser.ETHERTYPE                                       if parser.ETHERTYPE else str()
        self.PORTMAX = parser.PORTMAX                                           if parser.PORTMAX else None
        self.PROTOCOL = parser.PROTOCOL                                         if parser.PROTOCOL else str()
        self.SECUGROUP = parser.SECUGROUP                                       if parser.SECUGROUP else None
        self.IMAGE_ID = parser.IMAGE_ID                                         if parser.IMAGE_ID else str()
        self.SUBNETID = parser.SUBNETID                                         if parser.SUBNETID else None
        self.NETWORKINTERFACEID = parser.NETWORKINTERFACEID                     if parser.NETWORKINTERFACEID else str()
        self.S3BUCKET = parser.S3BUCKET                                         if parser.S3BUCKET else str()
        self.S3OBJECT = parser.S3OBJECT                                         if parser.S3OBJECT else str()
        self.S3RECURSIVE = parser.S3RECURSIVE                                   if parser.S3RECURSIVE else False
        self.OUTPUT_FORMAT = parser.OUTPUT_FORMAT                               if parser.OUTPUT_FORMAT else self.OUTPUT_FORMAT 
        self.SNAPSHOTID = parser.SNAPSHOTID                                     if parser.SNAPSHOTID else "null"
        self.DESCRIPTION = parser.DESCRIPTION                                   if parser.DESCRIPTION else str()
        self.PUBLICIPID = parser.PUBLICIPID                                     if parser.PUBLICIPID else None
        self.PRIVATEIPID= parser.PRIVATEIPID                                    if parser.PRIVATEIPID else None
        self.PUBLICIP = parser.PUBLICIP                                         if parser.PUBLICIP else None
        # self.DELETE_PUBLICIP = parser.DELETE_PUBLICIP                           if parser.DELETE_PUBLICIP else str()
        # self.DELETE_VOLUME = parser.DELETE_VOLUME                               if parser.DELETE_VOLUME else str()
        self.QUERY = parser.QUERY                                               if parser.QUERY else None
        self.SOURCE_GROUP = parser.SOURCE_GROUP                                  if parser.SOURCE_GROUP else None
        self.SOURCE_GROUP_ID = parser.SOURCE_GROUP_ID                           if parser.SOURCE_GROUP_ID else None
        self.CLIINPUTJSONFILE = parser.CLIINPUTJSONFILE                           if parser.CLIINPUTJSONFILE else None
        
        
        
        
        #hodigy
        #add_backend_member.template
        #self.SERVER_ID = parser.SERVER_ID                                           if parser.SERVER_ID else None
        self.ADDRESS = parser.ADDRESS                                           if parser.ADDRESS else None
        #apply_private_ip_address.template
        #SUBNETID
        self.IP_ADDRESS = parser.IP_ADDRESS                                           if parser.IP_ADDRESS else None
        #create_as_configuration.template
        #SCALINGGROUP_NAME
        #self.FLAVOR_REF = parser.FLAVOR_REF                                           if parser.FLAVOR_REF else None
        self.IMAGE_REF = parser.IMAGE_REF                                           if parser.IMAGE_REF else None
        self.DISK_SIZE = parser.DISK_SIZE                                           if parser.DISK_SIZE else None
        #VOLUME_TYPE
        self.DISK_TYPE = parser.DISK_TYPE                                           if parser.DISK_TYPE else None
        #KEYNAME
        #create_as_group.template
        self.SCALING_CONFIGURATION_ID = parser.SCALING_CONFIGURATION_ID                                           if parser.SCALING_CONFIGURATION_ID else None
        self.DESIRE_INSTANCE_NUMBER = parser.DESIRE_INSTANCE_NUMBER                                           if parser.DESIRE_INSTANCE_NUMBER else None
        self.MIN_INSTANCE_NUMBER = parser.MIN_INSTANCE_NUMBER                                           if parser.MIN_INSTANCE_NUMBER else None
        self.MAX_INSTANCE_NUMBER = parser.MAX_INSTANCE_NUMBER                                           if parser.MAX_INSTANCE_NUMBER else None
        self.COOL_DOWN_TIME = parser.COOL_DOWN_TIME                                           if parser.COOL_DOWN_TIME else None
        self.HEALTH_PERIODIC_AUDIT_METHOD = parser.HEALTH_PERIODIC_AUDIT_METHOD                                           if parser.HEALTH_PERIODIC_AUDIT_METHOD else None
        self.HEALTH_PERIODIC_AUDIT_TIME = parser.HEALTH_PERIODIC_AUDIT_TIME                                           if parser.HEALTH_PERIODIC_AUDIT_TIME else None
        self.INSTANCE_TERMINATE_POLICY = parser.INSTANCE_TERMINATE_POLICY                                           if parser.INSTANCE_TERMINATE_POLICY else None
        #VPCID
        self.NETWORKS_ID = parser.NETWORKS_ID                                           if parser.NETWORKS_ID else None
        self.NOTIFICATIONS = parser.NOTIFICATIONS                                           if parser.NOTIFICATIONS else None
        self.SECURITY_GROUPS_ID = parser.SECURITY_GROUPS_ID                                           if parser.SECURITY_GROUPS_ID else None
        #creating_health_check_task.template
        self.HEALTHCHECK_CONNECT_PORT = parser.HEALTHCHECK_CONNECT_PORT                                           if parser.HEALTHCHECK_CONNECT_PORT else None
        self.HEALTHCHECK_INTERVAL = parser.HEALTHCHECK_INTERVAL                                           if parser.HEALTHCHECK_INTERVAL else None
        self.HEALTHCHECK_PROTOCOL = parser.HEALTHCHECK_PROTOCOL                                           if parser.HEALTHCHECK_PROTOCOL else None
        self.HEALTHCHECK_TIMEOUT = parser.HEALTHCHECK_TIMEOUT                                           if parser.HEALTHCHECK_TIMEOUT else None
        self.HEALTHCHECK_URI = parser.HEALTHCHECK_URI                                           if parser.HEALTHCHECK_URI else None
        self.HEALTHY_THREAHOLD = parser.HEALTHY_THREAHOLD                                           if parser.HEALTHY_THREAHOLD else None
        #LISTENER_ID
        self.UNHEALTHY_THRESHOLD = parser.UNHEALTHY_THRESHOLD                                           if parser.UNHEALTHY_THRESHOLD else None
        #delete_backend_member.template
        #self.REMOVE_MEMBER_ID = parser.REMOVE_MEMBER_ID                                           if parser.REMOVE_MEMBER_ID else None
        #disable_enable_as_group.template
        self.ACTION_DISABLE_ENABLE_AS_GROUP = parser.ACTION_DISABLE_ENABLE_AS_GROUP                                           if parser.ACTION_DISABLE_ENABLE_AS_GROUP else None
        #modify_as_group.template
        #modify_information_health_check_task.template
        self.HEALTHCHECK_ID = parser.HEALTHCHECK_ID                                           if parser.HEALTHCHECK_ID else None


        #modify_information_listener.template
        self.LISTENER_NAME = parser.LISTENER_NAME                                           if parser.LISTENER_NAME else None
        self.LISTENER_DESCRIPTION = parser.LISTENER_DESCRIPTION                                           if parser.LISTENER_DESCRIPTION else None
        self.LISTENER_PORT = parser.LISTENER_PORT                                           if parser.LISTENER_PORT else None
        self.BACKEND_PORT = parser.BACKEND_PORT                                           if parser.BACKEND_PORT else None
        self.LB_ALGORITHM = parser.LB_ALGORITHM                                           if parser.LB_ALGORITHM else None
        #modify_load_balancer.template
        self.BANDWIDTH = parser.BANDWIDTH                                           if parser.BANDWIDTH else None
        self.ADMIN_STATE_UP = parser.ADMIN_STATE_UP                                           if parser.ADMIN_STATE_UP else None
        #query_as_configuration_details.template
        self.TENANT = parser.TENANT                                           if parser.TENANT else None
        self.SCALING_CONFIGURATION_NAME = parser.SCALING_CONFIGURATION_NAME                                           if parser.SCALING_CONFIGURATION_NAME else None
        #ADMINPASS
        self.PERSONALITY = parser.PERSONALITY                                           if parser.PERSONALITY else None
        #INSTANCE_NAME
        #INSTANCE_ID
        #PUBLICIP
        #USER_DATA
        self.CREATE_TIME = parser.CREATE_TIME                                           if parser.CREATE_TIME else None
        #query_as_group_details.template
        self.DETAIL = parser.DETAIL                                           if parser.DETAIL else None
        #SCALINGGROUP_ID
        self.SCALING_GROUP_STATUS = parser.SCALING_GROUP_STATUS                                           if parser.SCALING_GROUP_STATUS else None
        self.CURRENT_INSTANCE_NUMBER = parser.CURRENT_INSTANCE_NUMBER                                           if parser.CURRENT_INSTANCE_NUMBER else None
        #self.LB_LISTENER_ID = parser.LB_LISTENER_ID                                           if parser.LB_LISTENER_ID else None
        self.IS_SCALING = parser.IS_SCALING                                           if parser.IS_SCALING else None
        #DELETE_PUBLICIP
        #update_bandwidth_information.template
        self.BANDWIDTH_SIZE = parser.BANDWIDTH_SIZE                                           if parser.BANDWIDTH_SIZE else None
        #update_elastic_ip_address_information.template
        self.PUBLICIP_PORT_ID = parser.PUBLICIP_PORT_ID                                           if parser.PUBLICIP_PORT_ID else None
        #update_subnet_information.template
        #SUBNETNAME
        self.DHCP_ENABLE = parser.DHCP_ENABLE                                           if parser.DHCP_ENABLE else None
        #PRIMARYDNS
        #SECDNS
        #update_vpc_information.template
        #VPCNAME
        #CIDR
        #add_nics_ecs_batches.template
        self.SECURITY_GROUP_ID = parser.SECURITY_GROUP_ID                                           if parser.SECURITY_GROUP_ID else None
        #batch_remove_add_instance.template
        self.INSTANCE_ACTION_ADD_REMOVE_BATCH = parser.INSTANCE_ACTION_ADD_REMOVE_BATCH                                           if parser.INSTANCE_ACTION_ADD_REMOVE_BATCH else None
        self.INSTANCE_ID_1 = parser.INSTANCE_ID_1                                           if parser.INSTANCE_ID_1 else None
        self.INSTANCE_ID_2 = parser.INSTANCE_ID_2                                           if parser.INSTANCE_ID_2 else None
        self.INSTANCE_DELETE = parser.INSTANCE_DELETE                                           if parser.INSTANCE_DELETE else None
        #create_as_policy.template
        self.RECURRENCE_VALUE = parser.RECURRENCE_VALUE                                           if parser.RECURRENCE_VALUE else None
        self.START_TIME = parser.START_TIME                                           if parser.START_TIME else None
        self.LAUNCH_TIME = parser.LAUNCH_TIME                                           if parser.LAUNCH_TIME else None
        self.END_TIME = parser.END_TIME                                           if parser.END_TIME else None
        self.RECURRENCE_TYPE = parser.RECURRENCE_TYPE                                           if parser.RECURRENCE_TYPE else None
        self.SCALING_POLICY_TYPE = parser.SCALING_POLICY_TYPE                                           if parser.SCALING_POLICY_TYPE else None
        self.INSTANCE_NUMBER = parser.INSTANCE_NUMBER                                           if parser.INSTANCE_NUMBER else None
        self.OPERATION_AS_POLICY = parser.OPERATION_AS_POLICY                                           if parser.OPERATION_AS_POLICY else None
        self.SCALING_POLICY_NAME = parser.SCALING_POLICY_NAME                                           if parser.SCALING_POLICY_NAME else None
        self.SCALING_POLICY_ID = parser.SCALING_POLICY_ID                                           if parser.SCALING_POLICY_ID else None
        #delete_nics_ecs_batches.template
        #NETWORKINTERFACEID
        #execute_enable_disable_as_policy.template
        self.AS_POLICY_ACTION = parser.AS_POLICY_ACTION                                           if parser.AS_POLICY_ACTION else None
        #expand_capacity_on_evs_disk.template
        self.EVS_NEW_SIZE = parser.EVS_NEW_SIZE                                           if parser.EVS_NEW_SIZE else None
        #modify_as_policy.template
        #modify_spec_ecs.template
        #restore_disk_vbs_backup.template
        #VOLUME_ID
        #update_evs_info.template
        #VOLUME_NAME
        #DESCRIPTION        

        #create_listener.template
        self.SESSION_STICKY = parser.SESSION_STICKY                                           if parser.SESSION_STICKY else None
        self.STICKY_SESSION_TYPE = parser.STICKY_SESSION_TYPE                                           if parser.STICKY_SESSION_TYPE else None
        self.COOKIE_TIMEOUT = parser.COOKIE_TIMEOUT                                           if parser.COOKIE_TIMEOUT else None
        self.PROJECT_NAME = parser.PROJECT_NAME                                           if parser.PROJECT_NAME else OtcConfig.PROJECT_NAME
        
