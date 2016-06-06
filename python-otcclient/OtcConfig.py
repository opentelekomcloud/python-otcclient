#!/usr/bin/env python
""" generated source for module OtcConfig """
#  
#  * Copyright (c) 2016 T-Systems GmbH
#  * Germany
#  * All rights reserved.
#  * 
#  * Name: ParamFactory.py
#  * Author: zsonagy
#  * Datum: 08.03.2016
#  
# package: com.tsystems.otc.config

#class Singleton(object):
#  _instances = {}
#  def __new__(class_, *args, **kwargs):
#    if class_ not in class_._instances:
#        class_._instances[class_] = super(Singleton, class_).__new__(class_, *args, **kwargs)
#    return class_._instances[class_]

import os

class OtcConfig(object):
    """ generated source for class OtcConfig """
    instance_ = None

    #  for singleton instances
    def __init__(self):
        """ generated source for method __init__ """

    @classmethod
    def getInstance(cls):
        """ generated source for method getInstance """
        if cls.instance_ == None:
            cls.instance_ = OtcConfig()
        return cls.instance_

    from os.path import expanduser
    os.environ
    home = expanduser("~")
    OTC_USER_DIR = home+ "/.otc"
    OTC_USER_FILE = OTC_USER_DIR + "/config"
    OTC_PROXY_FILE = OTC_USER_DIR + "/common"

    #  replace real AK
    ak = str()

    #  replace real SK
    sk = str()

    #  default region definition
    region = "eu-de"

    #  replace real service name
    serviceName = "serviceName"
    PROJECT_ID = str()
    PROJECT_NAME = "eu-de"

    # public static String SERVER_ID;
    USERNAME = str()
    PASSWORD = str()
    DOMAIN = str()
    ECSTASKID = str()
    SECUGROUPNAME = "default"
    VPCNAME = "default-vpc"
    SUBNETNAME = "default-subnet"
    IMAGENAME = "Community-CentOS-7.0-x86_64-2015-0"
    NUMCOUNT = "1"
    INSTANCE_TYPE = "computev1-1"
    INSTANCE_TYPE_NAME = str()
    INSTANCE_NAME = "default"
    INSTANCE_ID = str()
    ADMINPASS = None
    CREATE_ECS_WITH_PUBLIC_IP = "false"
    ECSACTIONTYPE = "HARD"
    WAIT_CREATE = "false"
    KEYNAME = None
    PUBLICKEY = ""
    VOLUME_SIZE = int()
    VOLUME_TYPE = str()
    VOLUME_NAME = str()
    VOLUME_ID = str()
    ATTACHMENT_ID = str()
    EVS_DEVICE = str()

    #  # fetch main command
    MAINCOM = None
    SUBCOM = None
    ECSACTION = None
    DEFAULT_HOST = "46.29.103.37"
    # TODO:!!!!! THIS has changed 
    #DEFAULT_HOST = "otc.t-systems.com"
    S3_HOSTNAME = str()
    IAM_AUTH_URL = str()
    AUTH_URL_ECS = str()
    AUTH_URL_ECS_JOB = str()
    AUTH_URL_ECS_CLOUD = str()
    AUTH_URL_ECS_CLOUDSERVERS_BASE = str()
    AUTH_URL_ECS_CLOUD_ACTION = str()
    AUTH_URL_VPCS = str()
    AUTH_URL_PUBLICIPS = str()
    AUTH_URL_SEC_GROUPS = str()
    AUTH_URL_SEC_GROUP_RULE = str()
    AUTH_URL_SUBNETS = str()
    AUTH_URL_IMAGES = str()
    AUTH_URL_FLAVORS = str()
    AUTH_URL_KEYNAMES = str()
    AUTH_URL_CLOUDVOLUMES = str()
    AUTH_URL_ECS_ATTACHVOLUME = str()
    AUTH_URL_ECS_DEATTACHVOLUME = str()
    AUTH_URL_ECS_QUOTAS = str()
    AUTH_URL_BACKUP_ACTION = str()
    AUTH_URL_BACKUP_LIST = str()
    FILE1 = None
    FILE2 = None
    FILE3 = None
    FILE4 = None
    FILE5 = None
    GWIP = str()
    PRIMARYDNS = str()
    SECDNS = str()
    AZ = "eu-de-01"
    VPCID = str()
    CIDR = None
    DIRECTION = str()
    PORTMIN = str()
    ETHERTYPE = str()
    PORTMAX = str()
    PROTOCOL = str()
    SECUGROUP = str()
    IMAGE_ID = str()
    SUBNETID = str()
    NETWORKINTERFACEID = str()
    ECSCREATEJOBSTATUS = str()
    TOKEN = str()

    #  proxy settings
    PROXY_URL = str()
    PROXY_PORT = int()

    #  S3 settings 
    S3BUCKET = str()
    S3OBJECT = str()
    S3RECURSIVE = bool()
    OUTPUT_FORMAT = "Table"

    #  backups 
    SNAPSHOTID = str()
    DESCRIPTION = str()
    PUBLICIPID = str()
    PUBLICIP = str()
    DELETE_PUBLICIP = "true"
    DELETE_VOLUME = "true"
    QUERY = str()

    #  reset values 
    @classmethod
    def resetUrlVars(cls):
        """ generated source for method resetUrlVars """
        cls.S3_HOSTNAME = "obs.otc.t-systems.com"
        # DEFAULT_HOST;
        cls.IAM_AUTH_URL = "https://" + cls.DEFAULT_HOST + ":443/v3/auth/tokens"
        cls.AUTH_URL_ECS = "https://" + cls.DEFAULT_HOST + "/v2/" + cls.PROJECT_ID + "/servers"
        # 		AUTH_URL_ECS_JOB = "https://"+ cls.DEFAULT_HOST +"/v2/"
        # 				+ cls.PROJECT_ID + "/jobs/" + ECSTASKID;
        cls.AUTH_URL_ECS_CLOUD = "https://" + cls.DEFAULT_HOST + "/v1/" + cls.PROJECT_ID + "/cloudservers"
        cls.AUTH_URL_ECS_CLOUD_ACTION = "https://" + cls.DEFAULT_HOST + "/v1/" + cls.PROJECT_ID + "/cloudservers/action"
        cls.AUTH_URL_VPCS = "https://" + cls.DEFAULT_HOST + "/v1/" + cls.PROJECT_ID + "/vpcs"
        cls.AUTH_URL_PUBLICIPS = "https://" + cls.DEFAULT_HOST + "/v1/" + cls.PROJECT_ID + "/publicips"
        cls.AUTH_URL_SEC_GROUPS = "https://" + cls.DEFAULT_HOST + "/v1/" + cls.PROJECT_ID + "/security-groups"
        # 		AUTH_URL_SEC_GROUP_RULE = "https://"+ cls.DEFAULT_HOST +"/v2.0/security-group-rules";
        cls.AUTH_URL_SUBNETS = "https://" + cls.DEFAULT_HOST + "/v1/" + cls.PROJECT_ID + "/subnets"
        cls.AUTH_URL_IMAGES = "https://" + cls.DEFAULT_HOST + "/v2/images"
        cls.AUTH_URL_FLAVORS = "https://" + cls.DEFAULT_HOST + "/v1/" + cls.PROJECT_ID + "/cloudservers/flavors"
        cls.AUTH_URL_KEYNAMES = "https://" + cls.DEFAULT_HOST + "/v2/" + cls.PROJECT_ID + "/os-keypairs"
        cls.AUTH_URL_ECS_ATTACHVOLUME = "https://" + cls.DEFAULT_HOST + "/v1/" + cls.PROJECT_ID + "/cloudservers/" + cls.INSTANCE_ID + "/attachvolume"
        cls.AUTH_URL_ECS_DEATTACHVOLUME = "https://" + cls.DEFAULT_HOST + "/v1/" + cls.PROJECT_ID + "/cloudservers/" + cls.INSTANCE_ID + "/detachvolume/" + cls.VOLUME_ID
        cls.AUTH_URL_ECS_QUOTAS = "https://" + cls.DEFAULT_HOST + "/v2/" + cls.PROJECT_ID + "/os-quota-sets/" + cls.PROJECT_ID + "?usage=True"
        cls.AUTH_URL_BACKUP_ACTION = "https://" + cls.DEFAULT_HOST + "/v2/" + cls.PROJECT_ID + "/cloudbackups"
        cls.AUTH_URL_BACKUP_LIST = "https://" + cls.DEFAULT_HOST + "/v2/" + cls.PROJECT_ID + "/backups/detail"
        cls.AUTH_URL_ECS_CLOUDSERVERS_BASE = "https://" + cls.DEFAULT_HOST + "/v1/" + cls.PROJECT_ID + "/cloudservers"
        cls.AUTH_URL_CLOUDVOLUMES = "https://" + cls.DEFAULT_HOST + "/v2/" + cls.PROJECT_ID + "/cloudvolumes"
        cls.AUTH_URL_ECS_JOB = "https://" + cls.DEFAULT_HOST + "/v1/" + cls.PROJECT_ID + "/jobs/" + cls.ECSTASKID
        cls.AUTH_URL_SEC_GROUP_RULE = "https://vpc.eu-de.otc.t-systems.com/v1/" + cls.PROJECT_ID + "/security-group-rules/" + cls.SECUGROUP

    
    @classmethod
    def isdefined( self,value ):
        try:
            if( value != None):
                return value
        except NameError:
            return None
    
    @classmethod
    def copyfromparser( self,parser ):
#        self.ak = parser.ak                                                    if hasattr(parser, 'ak') else str() 
#        self.sk = parser.sk                                                    if hasattr(parser, 'sk') else str() 
#        self.region = parser.region                                            if hasattr(parser, 'region') else str()
#         self.serviceName = parser.serviceName                                 if hasattr(parser, 'serviceName') else str()
#         self.PROJECT_ID = parser.PROJECT_ID                                   if hasattr(parser, 'PROJECT_ID') else str()
#         self.PROJECT_NAME = parser.PROJECT_NAME                               if hasattr(parser, 'PROJECT_NAME') else str()
#         self.USERNAME = parser.USERNAME                                       if hasattr(parser, 'USERNAME') else str()
#         self.PASSWORD = parser.PASSWORD                                       if hasattr(parser, 'PASSWORD') else str()
#         self.DOMAIN = parser.DOMAIN                                           if hasattr(parser, 'DOMAIN') else str()
#         self.ECSTASKID = parser.ECSTASKID                                     if hasattr(parser, 'ECSTASKID') else str()

        self.SECUGROUPNAME = parser.SECUGROUPNAME                               if parser.SECUGROUPNAME else str()
        self.VPCNAME = parser.VPCNAME                                           if parser.VPCNAME else str()
        self.SUBNETNAME = parser.SUBNETNAME                                     if parser.SUBNETNAME else str()
        self.IMAGENAME = parser.IMAGENAME                                       if parser.IMAGENAME else str()
        self.NUMCOUNT = parser.NUMCOUNT                                         if parser.NUMCOUNT else str()
        #self.INSTANCE_TYPE_ = parser.INSTANCE_TYPE                               if parser.INSTANCE_TYPE else str()
        self.INSTANCE_TYPE_NAME = parser.INSTANCE_TYPE_NAME                     if parser.INSTANCE_TYPE_NAME else str()
        self.INSTANCE_NAME = parser.INSTANCE_NAME                               if parser.INSTANCE_NAME else str()
        self.INSTANCE_ID = parser.INSTANCE_ID                                   if parser.INSTANCE_ID else str()
        self.ADMINPASS= parser.ADMINPASS                                        if parser.ADMINPASS else str()
        self.CREATE_ECS_WITH_PUBLIC_IP= parser.CREATE_ECS_WITH_PUBLIC_IP        if parser.CREATE_ECS_WITH_PUBLIC_IP else str()
        #self.ECSACTIONTYPE = parser.ECSACTIONTYPE                               if parser.ECSACTIONTYPE else str()
        self.WAIT_CREATE = parser.WAIT_CREATE                                   if parser.WAIT_CREATE else str()
        self.KEYNAME= parser.KEYNAME                                            if parser.KEYNAME else str()
        self.PUBLICKEY = parser.PUBLICKEY                                       if parser.PUBLICKEY else str()
        self.VOLUME_SIZE = parser.VOLUME_SIZE                                   if parser.VOLUME_SIZE else str()
        self.VOLUME_TYPE = parser.VOLUME_TYPE                                   if parser.VOLUME_TYPE else str()
        self.VOLUME_NAME = parser.VOLUME_NAME                                   if parser.VOLUME_NAME else str()
        self.VOLUME_ID = parser.VOLUME_ID                                       if parser.VOLUME_ID else str()
        self.ATTACHMENT_ID = parser.ATTACHMENT_ID                               if parser.ATTACHMENT_ID else str()
        self.EVS_DEVICE = parser.EVS_DEVICE                                     if parser.EVS_DEVICE else str()
        self.MAINCOM = parser.MAINCOM                                           if parser.MAINCOM else str()
        self.SUBCOM= parser.SUBCOM                                              if parser.SUBCOM else str()
        #self.ECSACTION= parser.ECSACTION                                        if parser.ECSACTION else str()
        self.FILE1= parser.FILE1                                                if parser.FILE1 else str()
        self.FILE2= parser.FILE2                                                if parser.FILE2 else str()
        self.FILE3= parser.FILE3                                                if parser.FILE3 else str()
        self.FILE4= parser.FILE4                                                if parser.FILE4 else str()
        self.FILE5= parser.FILE5                                                if parser.FILE5 else str()
        self.GWIP = parser.GWIP                                                 if parser.GWIP else str()
        self.PRIMARYDNS = parser.PRIMARYDNS                                     if parser.PRIMARYDNS else str()
        self.SECDNS = parser.SECDNS                                             if parser.SECDNS else str()
        self.AZ = parser.AZ                                                     if parser.AZ else str()
        self.VPCID = parser.VPCID                                               if parser.VPCID else str()
        self.CIDR= parser.CIDR                                                  if parser.CIDR else str()
        self.DIRECTION = parser.DIRECTION                                       if parser.DIRECTION else str()
        self.PORTMIN = parser.PORTMIN                                           if parser.PORTMIN else str()
        self.ETHERTYPE = parser.ETHERTYPE                                       if parser.ETHERTYPE else str()
        self.PORTMAX = parser.PORTMAX                                           if parser.PORTMAX else str()
        self.PROTOCOL = parser.PROTOCOL                                         if parser.PROTOCOL else str()
        self.SECUGROUP = parser.SECUGROUP                                       if parser.SECUGROUP else str()
        self.IMAGE_ID = parser.IMAGE_ID                                         if parser.IMAGE_ID else str()
        self.SUBNETID = parser.SUBNETID                                         if parser.SUBNETID else str()
        self.NETWORKINTERFACEID = parser.NETWORKINTERFACEID                     if parser.NETWORKINTERFACEID else str()
        #self.ECSCREATEJOBSTATUS = parser.ECSCREATEJOBSTATUS                     if parser.ECSCREATEJOBSTATUS else str()
        #self.TOKEN = parser.TOKEN                                               if parser.TOKEN else str()
        #self.PROXY_URL = parser.PROXY_URL                                       if parser.PROXY_URL else str()
        #self.PROXY_PORT = parser.PROXY_PORT                                     if parser.PROXY_PORT else str()
        self.S3BUCKET = parser.S3BUCKET                                         if parser.S3BUCKET else str()
        self.S3OBJECT = parser.S3OBJECT                                         if parser.S3OBJECT else str()
        #self.S3RECURSIVE = parser.S3RECURSIVE                                   if parser.S3RECURSIVE else str()
        self.OUTPUT_FORMAT = parser.OUTPUT_FORMAT                               if parser.OUTPUT_FORMAT else self.OUTPUT_FORMAT 
        self.SNAPSHOTID = parser.SNAPSHOTID                                     if parser.SNAPSHOTID else str()
        self.DESCRIPTION = parser.DESCRIPTION                                   if parser.DESCRIPTION else str()
        self.PUBLICIPID = parser.PUBLICIPID                                     if parser.PUBLICIPID else str()
        self.PUBLICIP = parser.PUBLICIP                                         if parser.PUBLICIP else str()
        #self.DELETE_PUBLICIP = parser.DELETE_PUBLICIP                           if parser.DELETE_PUBLICIP else str()
        #self.DELETE_VOLUME = parser.DELETE_VOLUME                               if parser.DELETE_VOLUME else str()
        self.QUERY = parser.QUERY                                               if parser.QUERY else str()

#         self.SECUGROUPNAME = parser.SECUGROUPNAME                               if hasattr(parser, 'SECUGROUPNAME') else str()
#         self.VPCNAME = parser.VPCNAME                                           if hasattr(parser, 'VPCNAME') else str()
#         self.SUBNETNAME = parser.SUBNETNAME                                     if hasattr(parser, 'SUBNETNAME') else str()
#         self.IMAGENAME = parser.IMAGENAME                                       if hasattr(parser, 'IMAGENAME') else str()
#         self.NUMCOUNT = parser.NUMCOUNT                                         if hasattr(parser, 'NUMCOUNT') else str()
#         self.INSTANCE_TYPE = parser.INSTANCE_TYPE                               if hasattr(parser, 'INSTANCE_TYPE') else str()
#         self.INSTANCE_TYPE_NAME = parser.INSTANCE_TYPE_NAME                     if hasattr(parser, 'INSTANCE_TYPE_NAME') else str()
#         self.INSTANCE_NAME = parser.INSTANCE_NAME                               if hasattr(parser, 'INSTANCE_NAME') else str()
#         self.INSTANCE_ID = parser.INSTANCE_ID                                   if hasattr(parser, 'INSTANCE_ID') else str()
#         self.ADMINPASS= parser.ADMINPASS                                        if hasattr(parser, 'ADMINPASS') else str()
#         self.CREATE_ECS_WITH_PUBLIC_IP= parser.CREATE_ECS_WITH_PUBLIC_IP        if hasattr(parser, 'CREATE_ECS_WITH_PUBLIC_IP') else str()
#         self.ECSACTIONTYPE = parser.ECSACTIONTYPE                               if hasattr(parser, 'ECSACTIONTYPE') else str()
#         self.WAIT_CREATE = parser.WAIT_CREATE                                   if hasattr(parser, 'WAIT_CREATE') else str()
#         self.KEYNAME= parser.KEYNAME                                            if hasattr(parser, 'KEYNAME') else str()
#         self.PUBLICKEY = parser.PUBLICKEY                                       if hasattr(parser, 'PUBLICKEY') else str()
#         self.VOLUME_SIZE = parser.VOLUME_SIZE                                   if hasattr(parser, 'VOLUME_SIZE') else str()
#         self.VOLUME_TYPE = parser.VOLUME_TYPE                                   if hasattr(parser, 'VOLUME_TYPE') else str()
#         self.VOLUME_NAME = parser.VOLUME_NAME                                   if hasattr(parser, 'VOLUME_NAME') else str()
#         self.VOLUME_ID = parser.VOLUME_ID                                       if hasattr(parser, 'VOLUME_ID') else str()
#         self.ATTACHMENT_ID = parser.ATTACHMENT_ID                               if hasattr(parser, 'ATTACHMENT_ID') else str()
#         self.EVS_DEVICE = parser.EVS_DEVICE                                     if hasattr(parser, 'EVS_DEVICE') else str()
#         self.MAINCOM = parser.MAINCOM                                           if hasattr(parser, 'MAINCOM') else str()
#         self.SUBCOM= parser.SUBCOM                                              if hasattr(parser, 'SUBCOM') else str()
#         self.ECSACTION= parser.ECSACTION                                        if hasattr(parser, 'ECSACTION') else str()
#         self.FILE1= parser.FILE1                                                if hasattr(parser, 'FILE1') else str()
#         self.FILE2= parser.FILE2                                                if hasattr(parser, 'FILE2') else str()
#         self.FILE3= parser.FILE3                                                if hasattr(parser, 'FILE3') else str()
#         self.FILE4= parser.FILE4                                                if hasattr(parser, 'FILE4') else str()
#         self.FILE5= parser.FILE5                                                if hasattr(parser, 'FILE5') else str()
#         self.GWIP = parser.GWIP                                                 if hasattr(parser, 'GWIP') else str()
#         self.PRIMARYDNS = parser.PRIMARYDNS                                     if hasattr(parser, 'PRIMARYDNS') else str()
#         self.SECDNS = parser.SECDNS                                             if hasattr(parser, 'SECDNS') else str()
#         self.AZ = parser.AZ                                                     if hasattr(parser, 'AZ') else str()
#         self.VPCID = parser.VPCID                                               if hasattr(parser, 'VPCID') else str()
#         self.CIDR= parser.CIDR                                                  if hasattr(parser, 'CIDR') else str()
#         self.DIRECTION = parser.DIRECTION                                       if hasattr(parser, 'DIRECTION') else str()
#         self.PORTMIN = parser.PORTMIN                                           if hasattr(parser, 'PORTMIN') else str()
#         self.ETHERTYPE = parser.ETHERTYPE                                       if hasattr(parser, 'ETHERTYPE') else str()
#         self.PORTMAX = parser.PORTMAX                                           if hasattr(parser, 'PORTMAX') else str()
#         self.PROTOCOL = parser.PROTOCOL                                         if hasattr(parser, 'PROTOCOL') else str()
#         self.SECUGROUP = parser.SECUGROUP                                       if hasattr(parser, 'SECUGROUP') else str()
#         self.IMAGE_ID = parser.IMAGE_ID                                         if hasattr(parser, 'IMAGE_ID') else str()
#         self.SUBNETID = parser.SUBNETID                                         if hasattr(parser, 'SUBNETID') else str()
#         self.NETWORKINTERFACEID = parser.NETWORKINTERFACEID                     if hasattr(parser, 'NETWORKINTERFACEID') else str()
#         self.ECSCREATEJOBSTATUS = parser.ECSCREATEJOBSTATUS                     if hasattr(parser, 'ECSCREATEJOBSTATUS') else str()
#         self.TOKEN = parser.TOKEN                                               if hasattr(parser, 'TOKEN') else str()
#         self.PROXY_URL = parser.PROXY_URL                                       if hasattr(parser, 'PROXY_URL') else str()
#         self.PROXY_PORT = parser.PROXY_PORT                                     if hasattr(parser, 'PROXY_PORT') else str()
#         self.S3BUCKET = parser.S3BUCKET                                         if hasattr(parser, 'S3BUCKET') else str()
#         self.S3OBJECT = parser.S3OBJECT                                         if hasattr(parser, 'S3OBJECT') else str()
#         self.S3RECURSIVE = parser.S3RECURSIVE                                   if hasattr(parser, 'S3RECURSIVE') else str()
#         self.OUTPUT_FORMAT = parser.OUTPUT_FORMAT                               if hasattr(parser, 'OUTPUT_FORMAT') else self.OUTPUT_FORMAT 
#         self.SNAPSHOTID = parser.SNAPSHOTID                                     if hasattr(parser, 'SNAPSHOTID') else str()
#         self.DESCRIPTION = parser.DESCRIPTION                                   if hasattr(parser, 'DESCRIPTION') else str()
#         self.PUBLICIPID = parser.PUBLICIPID                                     if hasattr(parser, 'PUBLICIPID') else str()
#         self.PUBLICIP = parser.PUBLICIP                                         if hasattr(parser, 'PUBLICIP') else str()
#         self.DELETE_PUBLICIP = parser.DELETE_PUBLICIP                           if hasattr(parser, 'DELETE_PUBLICIP') else str()
#         self.DELETE_VOLUME = parser.DELETE_VOLUME                               if hasattr(parser, 'DELETE_VOLUME') else str()
#         self.QUERY = parser.QUERY                                               if hasattr(parser, 'QUERY') else str()
