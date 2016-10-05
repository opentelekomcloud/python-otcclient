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

    LOADBALANCER_NAME = None
    LOADBALANCER_ID = None
    HEALTCHECK_ID = None

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
    VOLUME_ID = None
    ATTACHMENT_ID = str()
    EVS_DEVICE = str()
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
    CLIINPUTJSONFILE = None

    
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
        
                
        self.ADMINPASS = parser.ADMINPASS                                        if parser.ADMINPASS else str()
        self.CREATE_ECS_WITH_PUBLIC_IP = parser.CREATE_ECS_WITH_PUBLIC_IP        if parser.CREATE_ECS_WITH_PUBLIC_IP else str()
        # self.ECSACTIONTYPE = parser.ECSACTIONTYPE                               if parser.ECSACTIONTYPE else str()
        self.WAIT_CREATE = parser.WAIT_CREATE                                   if parser.WAIT_CREATE else False
        self.KEYNAME = parser.KEYNAME                                            if parser.KEYNAME else str()
        self.PUBLICKEY = parser.PUBLICKEY                                       if parser.PUBLICKEY else str()
        self.VOLUME_SIZE = parser.VOLUME_SIZE                                   if parser.VOLUME_SIZE else str()
        self.VOLUME_TYPE = parser.VOLUME_TYPE                                   if parser.VOLUME_TYPE else str()
        self.VOLUME_NAME = parser.VOLUME_NAME                                   if parser.VOLUME_NAME else None
        self.VOLUME_ID = parser.VOLUME_ID                                       if parser.VOLUME_ID else None
        self.ATTACHMENT_ID = parser.ATTACHMENT_ID                               if parser.ATTACHMENT_ID else str()
        self.EVS_DEVICE = parser.EVS_DEVICE                                     if parser.EVS_DEVICE else str()
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
        self.PUBLICIP = parser.PUBLICIP                                         if parser.PUBLICIP else None
        # self.DELETE_PUBLICIP = parser.DELETE_PUBLICIP                           if parser.DELETE_PUBLICIP else str()
        # self.DELETE_VOLUME = parser.DELETE_VOLUME                               if parser.DELETE_VOLUME else str()
        self.QUERY = parser.QUERY                                               if parser.QUERY else None
        self.SOURCE_GROUP = parser.SOURCE_GROUP                                  if parser.SOURCE_GROUP else None
        self.SOURCE_GROUP_ID = parser.SOURCE_GROUP_ID                           if parser.SOURCE_GROUP_ID else None
        self.CLIINPUTJSONFILE = parser.CLIINPUTJSONFILE                           if parser.CLIINPUTJSONFILE else None
        
        
