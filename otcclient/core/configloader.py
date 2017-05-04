#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of OTC Tool released under MIT license.
# Copyright (C) 2016 T-systems Kurt Garloff, Zsolt Nagy

import sys
if sys.version_info >= (3, 0):
    import configparser as ConfigParser
    from configparser import NoSectionError 
else:    
    import ConfigParser
    from ConfigParser import NoSectionError
    
from  otcclient.core.OtcConfig import OtcConfig
import os

from otcclient.core.pluginmanager import getplugin
#from urlparse import urlparse

if (sys.version_info > (3, 0)):
     # Python 3 code in this block
     from urllib.parse import urlparse
else:
     # Python 2 code in this block
     from urlparse import urlparse

 
class configloader(object):
    """
    Utility class to load / persist configuration properties
    """

    @staticmethod
    def _checkOtcUserDir():
        if not os.path.exists(OtcConfig.OTC_USER_DIR):
            try:
                os.makedirs(OtcConfig.OTC_USER_DIR)
            except:
                raise

    @staticmethod
    def loadOtcConfig(jsonFileName):
        Config = ConfigParser.ConfigParser()
        Config.read(jsonFileName)
        return Config

    @staticmethod
    def readProxyValues():
        try:            
            Config = ConfigParser.ConfigParser()
            Config.read(OtcConfig.OTC_PROXY_FILE)
                        
            OtcConfig.PROXY_URL = Config.get("otc", "proxy_host")
            temp = OtcConfig.PROXY_URL = Config.get("otc", "proxy_port")
            OtcConfig.PROXY_PORT = int(temp)
        except NoSectionError:
            """ No proxy defined"""
 
    @staticmethod
    def readUserValues():                
        OtcConfig.USERNAME = os.getenv("OS_USERNAME", None)
        OtcConfig.PASSWORD = os.getenv("OS_PASSWORD", None)
        OtcConfig.DOMAIN = os.getenv("OS_USER_DOMAIN_NAME", None)
        OtcConfig.ak = os.getenv("S3_ACCESS_KEY_ID", None)
        OtcConfig.sk = os.getenv("S3_SECRET_ACCESS_KEY", None)
        OtcConfig.PROJECT_ID = os.getenv("PROJECT_ID", None)
        host = os.getenv("OS_AUTH_URL", None)
        
        if( host ):
            p = urlparse(host)
            host = p.hostname
            OtcConfig.DEFAULT_HOST = host
        

        Config = ConfigParser.ConfigParser()
        
        Config.read(OtcConfig.OTC_USER_FILE) 
                 
        if( Config.has_option("otc", "host") ):
            OtcConfig.DEFAULT_HOST = Config.get("otc", "host", "")

        if( Config.has_option("otc", "obs_host") ):
            OtcConfig.DEFAULT_OBS_HOST = Config.get("otc", "obs_host", "")

        
        if(OtcConfig.USERNAME is None):
            OtcConfig.USERNAME = Config.get("otc", "username") 

        if(OtcConfig.PASSWORD is None):
            OtcConfig.PASSWORD = Config.get("otc", "apikey") 

        if(OtcConfig.ak  is None and Config.has_option("otc", "otc_access_key_id")):
            OtcConfig.ak = Config.get("otc", "otc_access_key_id") 
        if(OtcConfig.sk  is None and Config.has_option("otc", "otc_secret_access_key")):
            OtcConfig.sk = Config.get("otc", "otc_secret_access_key") 

        if(OtcConfig.PROJECT_ID  is None and Config.has_option("otc", "project_id")):
            OtcConfig.PROJECT_ID = Config.get("otc", "project_id", "") 
        else:
            OtcConfig.PROJECT_ID = str()

         
        if(OtcConfig.DOMAIN is None and Config.has_option("otc", "domain")):
            OtcConfig.DOMAIN = Config.get("otc", "domain")                                    
        
        
        if(OtcConfig.DOMAIN is None):
            OtcConfig.DOMAIN = str(OtcConfig.USERNAME).split(' ')[1]                                    

            

    @staticmethod
    def persistProxyValues():
        configloader._checkOtcUserDir()
        Config = ConfigParser.ConfigParser()
        # add the settings to the structure of the file, and lets write it out...
        Config.add_section('otc')
        Config.set('otc', 'proxy_host', OtcConfig.PROXY_URL)
        Config.set('otc', 'proxy_port', OtcConfig.PROXY_PORT)
        oldmask = os.umask(0o600);        
        with open(OtcConfig.OTC_PROXY_FILE, 'w') as cfgfile:
            try:
                Config.write(cfgfile)
            except Exception as e:
                print("Error during save keys/date pairs", e)
        os.umask(oldmask)
        
    @staticmethod
    def persistUserValues():
        configloader._checkOtcUserDir()
        Config = ConfigParser.ConfigParser()
        # add the settings to the structure of the file, and lets write it out...
        Config.add_section('otc')
        Config.set('otc', "otc_access_key_id", OtcConfig.ak)
        Config.set('otc', "otc_secret_access_key", OtcConfig.sk)
        Config.set('otc', "username", OtcConfig.USERNAME)
        Config.set('otc', "apikey", OtcConfig.PASSWORD)
        Config.set('otc', "domain", OtcConfig.DOMAIN)
        oldmask = os.umask(0o600);
        with open(OtcConfig.OTC_USER_FILE, 'w+') as cfgfile:
            try:
                Config.write(cfgfile)
            except Exception as e:
                print("Error during save keys/date pairs", e)
        os.umask(oldmask)
                
    @staticmethod
    def validateConfig():        
        #if OtcConfig.USERNAME != None and len(OtcConfig.USERNAME) == 32 and OtcConfig.PASSWORD != None and len(OtcConfig.PASSWORD) == 32 and OtcConfig.DOMAIN != None and len(OtcConfig.DOMAIN) == 23:
        if OtcConfig.USERNAME != None and OtcConfig.PASSWORD != None and OtcConfig.DOMAIN != None:            
            getplugin("ecs").getIamToken()
            #cls.otcServiceCalls.getIamToken()
        elif OtcConfig.ak != None and len(OtcConfig.ak) == 32 and OtcConfig.sk != None and len(OtcConfig.sk) == 32:
            raise RuntimeError("TODO: ERROR NOT IMPLEMENTED !!!")
        else:
            raise ValueError()

