#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of OTC Tool released under MIT license.
# Copyright (C) 2016 T-systems Kurt Garloff, Zsolt Nagy 

from otcclient.core.otcpluginbase import otcpluginbase

from otcclient.utils import utils_s3
from otcclient.core.OtcConfig import OtcConfig
from otcclient.core.pluginmanager import getplugin

class s3(otcpluginbase):
    ar = {}
    @staticmethod
    def otcOutputHandler(): 
        return getplugin(OtcConfig.OUTPUT_FORMAT)

    def otctype(self):
        return "func"
     
    @staticmethod
    def parse_bucket_uri(s3path):
        val = str(s3path).replace('s3://', '').split('/', 1)
        s3bucket = val[0]
        if len(val) > 1:
            s3dir = val[1]
        else:
            s3dir = ""
        return s3bucket, s3dir
    
    @staticmethod
    def ls():        
        if OtcConfig.SUBCOM_P1 is None:   
            buckets = utils_s3.ls_buckets()            
            s3.otcOutputHandler().print_output(buckets, mainkey = "", listkey={"Name","CreationDate"})     
        else:            
            s3bucket, s3dir = s3.parse_bucket_uri(OtcConfig.SUBCOM_P1)            
            buckets=utils_s3.ls_bucket(Bucket=s3bucket,Prefix=s3dir)        
            s3.otcOutputHandler().print_output(buckets, mainkey = "", listkey={"Key","Size","LastModified"})
                
    @staticmethod
    def mb():
        s3bucket= s3.parse_bucket_uri(OtcConfig.SUBCOM_P1)[0]
        utils_s3.create_bucket(Bucket=s3bucket)

    @staticmethod
    def rb():
        s3bucket = s3.parse_bucket_uri(OtcConfig.SUBCOM_P1)[0]
        utils_s3.delete_bucket(Bucket=s3bucket) 

    @staticmethod
    def rm():
        s3bucket, s3dir = s3.parse_bucket_uri(OtcConfig.SUBCOM_P1)
        utils_s3.delete_object(Bucket=s3bucket,Prefix=s3dir) 


    @staticmethod
    def get_bucket_versioning():
        s3bucket, s3dir = s3.parse_bucket_uri(OtcConfig.SUBCOM_P1)            # @UnusedVariable
        ver = utils_s3.get_bucket_versioning(Bucket=s3bucket,Prefix=s3dir)
        #print(ver) #debug
        s3.otcOutputHandler().print_output(ver, mainkey = "", listkey={"Key","Size","LastModified"}) 

    @staticmethod
    def list_object_versions():
        s3bucket, s3dir = s3.parse_bucket_uri(OtcConfig.SUBCOM_P1)            # @UnusedVariable
        ver = utils_s3.list_object_versions(Bucket=s3bucket,Prefix=s3dir)
        s3.otcOutputHandler().print_output(ver, mainkey = "", listkey={"Key","Size","LastModified"}) 

    @staticmethod
    def cp():        
        if( OtcConfig.SUBCOM_P1 is None or OtcConfig.SUBCOM_P2 is None):         
            raise RuntimeError("S3 Copy error. Please add s3 params correctly.")
        elif( str(OtcConfig.SUBCOM_P1).startswith("s3://") and OtcConfig.S3RECURSIVE):
            # directory download
            s3bucket, s3dir = s3.parse_bucket_uri(OtcConfig.SUBCOM_P1)            
            utils_s3.download_file(Bucket=s3bucket, Prefix=s3dir, File=OtcConfig.SUBCOM_P2)
        elif( str(OtcConfig.SUBCOM_P2).startswith("s3://") and OtcConfig.S3RECURSIVE):
            # directory upload
            s3bucket, s3dir = s3.parse_bucket_uri(OtcConfig.SUBCOM_P2)                        
            utils_s3.upload_dir(Local=OtcConfig.SUBCOM_P1,Bucket=s3bucket, Prefix=s3dir )         
        elif( str(OtcConfig.SUBCOM_P1).startswith("s3://") ):
            # file upload 
            s3bucket, s3dir = s3.parse_bucket_uri(OtcConfig.SUBCOM_P1)            
            utils_s3.download_file(Bucket=s3bucket, Prefix=s3dir, File=OtcConfig.SUBCOM_P2)
        elif( str(OtcConfig.SUBCOM_P2).startswith("s3://") ):
            # file download
            s3bucket, s3dir = s3.parse_bucket_uri(OtcConfig.SUBCOM_P2)            
            utils_s3.upload_file(File=OtcConfig.SUBCOM_P1,Bucket=s3bucket, Prefix=s3dir )
