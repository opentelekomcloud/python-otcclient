#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of OTC Tool released under MIT license.
# Copyright (C) 2016 T-systems Kurt Garloff, Zsolt Nagy 

from otcclient.core.otcpluginbase import otcpluginbase

from otcclient.utils import utils_s3
from otcclient.core.OtcConfig import OtcConfig
from otcclient.core.pluginmanager import getplugin

from otcclient.core.argmanager import arg, otcfunc 

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
    @otcfunc(plugin_name=__name__,
             desc="Create bucket",
             examples=[
                       {"List Buckets":"otc s3 ls"}, 
                       {"List Bucket files":"otc s3 ls mybucket"}
                       ],     
             args = [ 
                        arg(    '',    dest='SUBCOM_P1',     help='[optional Source/Target OBS directory]',metavar="Source/Target DIR")
                ]                
             )     
    def ls():        
        if OtcConfig.SUBCOM_P1 is None:   
            buckets = utils_s3.ls_buckets()            
            s3.otcOutputHandler().print_output(buckets, mainkey = "", listkey={"Name","CreationDate"})     
        else:            
            s3bucket, s3dir = s3.parse_bucket_uri(OtcConfig.SUBCOM_P1)            
            buckets=utils_s3.ls_bucket(Bucket=s3bucket,Prefix=s3dir)        
            s3.otcOutputHandler().print_output(buckets, mainkey = "", listkey={"Key","Size","LastModified"})
                
    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="Create bucket",
             args = [ 
                        arg(    '',    dest='SUBCOM_P1',     help='[optional Source/Target OBS directory]',metavar="Source/Target DIR")
                ]                
             )      
    def mb():
        s3bucket= s3.parse_bucket_uri(OtcConfig.SUBCOM_P1)[0]
        utils_s3.create_bucket(Bucket=s3bucket)

    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="Delete bucket",
             args = [ 
                        arg(    '',    dest='SUBCOM_P1',     help='[optional Source/Target OBS directory]',metavar="Source/Target DIR")
                ]                
             )      
    def rb():
        s3bucket = s3.parse_bucket_uri(OtcConfig.SUBCOM_P1)[0]
        utils_s3.delete_bucket(Bucket=s3bucket) 

    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="Remove object",
             args = [ 
                        arg(    '',    dest='SUBCOM_P1',     help='[optional Source/Target OBS directory]',metavar="Source/Target DIR")
                ]                
             )  
    def rm():
        s3bucket, s3dir = s3.parse_bucket_uri(OtcConfig.SUBCOM_P1)
        utils_s3.delete_object(Bucket=s3bucket,Prefix=s3dir) 


    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="Get Bucket versions",
             args = [ 
                        arg(    '',    dest='SUBCOM_P1',     help='[optional Source/Target OBS directory]',metavar="Source/Target DIR")
                ]                
             )  
    def get_bucket_versioning():
        s3bucket, s3dir = s3.parse_bucket_uri(OtcConfig.SUBCOM_P1)            # @UnusedVariable
        ver = utils_s3.get_bucket_versioning(Bucket=s3bucket,Prefix=s3dir)
        #print(ver) #debug
        s3.otcOutputHandler().print_output(ver, mainkey = "", listkey={"Key","Size","LastModified"}) 

    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="List Bucket file versions",
             args = [ 
                        arg(    '',    dest='SUBCOM_P1',     help='[optional Source/Target OBS directory]',metavar="Source/Target DIR")
                ]                
             )    
    def list_object_versions():
        s3bucket, s3dir = s3.parse_bucket_uri(OtcConfig.SUBCOM_P1)            # @UnusedVariable
        ver = utils_s3.list_object_versions(Bucket=s3bucket,Prefix=s3dir)
        s3.otcOutputHandler().print_output(ver, mainkey = "", listkey={"Key","Size","LastModified"}) 

    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="Download / Upload file / directory to bucket",
             examples=[
                       {"Download from bucket to local":"otc s3 cp s3://bucketname/filename.txt /localdir/filename.txt"}, 
                       {"Upload file / directory to bucket":"otc s3 cp /localdir/filename.txt s3://bucketname/filename.txt"}
                       ],
             args = [ 
                        arg(    '--recursive',    dest='S3RECURSIVE',     help='S3 recursive operation'),
                        arg(    '--encrypted',    dest='S3ENCRYPTED',     help='S3 enrypting operation'),
                        arg(    '',    dest='SUBCOM_P1',     help='[optional Source/Target OBS directory]',metavar="Source/Target DIR"),    
                        arg(    '',    dest='SUBCOM_P2',     help='[optional Source/Target OBS directory]', metavar="Source/Target DIR")    
                ]                
             )   
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
            utils_s3.upload_dir(Local=OtcConfig.SUBCOM_P1,Bucket=s3bucket, Prefix=s3dir, Encryption=OtcConfig.S3ENCRYPTED)
        elif( str(OtcConfig.SUBCOM_P1).startswith("s3://") ):
            # file download
            s3bucket, s3dir = s3.parse_bucket_uri(OtcConfig.SUBCOM_P1)            
            utils_s3.download_file(Bucket=s3bucket, Prefix=s3dir, File=OtcConfig.SUBCOM_P2)
        elif( str(OtcConfig.SUBCOM_P2).startswith("s3://") ):
            # file upload
            s3bucket, s3dir = s3.parse_bucket_uri(OtcConfig.SUBCOM_P2)            
            utils_s3.upload_file(File=OtcConfig.SUBCOM_P1,Bucket=s3bucket, Prefix=s3dir, Encryption=OtcConfig.S3ENCRYPTED)
