#!/usr/b    wsqin/env python
""" generated source for module ConfigLoader """
#  
#  * Copyright (c) 2016 T-Systems GmbH	
#  * Germany
#  * All rights reserved.
#  * 
#  * Name: ParamFactory.java
#  * Author: zsonagy
#  * Datum: 08.03.2016
#  
import ConfigParser
from _ast import __version__
from OtcConfig import OtcConfig
import os
from _io import FileIO
from test.test_socket import try_address
from ConfigParser import NoSectionError
from otcServiceCalls import otcServiceCalls
# 
#  * Utility class to load / persist configuration properties 
#  * 
#  * @author zsonagy
#  
class ConfigLoader(object):
    
    otcServiceCalls = otcServiceCalls()
    """ generated source for class ConfigLoader """
    # 	static final Logger log = LogManager.getLogger(OtcMain.class.__name__);
    # 
    # 	 * Factory for config from file
    # 	 * @param jsonFileName
    # 	 * @return Config tree according for json file
    # 	 * @throws JsonParseException
    # 	 * @throws JsonMappingException
    # 	 * @throws IOException
    # 	 
    @classmethod
    def loadOtcConfig(cls, jsonFileName):
        """ generated source for method loadOtcConfig """
        Config = ConfigParser.ConfigParser()
        Config.read(jsonFileName)
        return Config



    @classmethod
    def readProxyValues(cls):
        """ generated source for method readProxyValues """
        try:            
            Config = ConfigParser.ConfigParser()
            Config.read(OtcConfig.OTC_PROXY_FILE)
                        
            OtcConfig.PROXY_URL = Config.get("otc", "proxy_host")
            temp = OtcConfig.PROXY_URL = Config.get("otc", "proxy_port")
            OtcConfig.PROXY_PORT = int(temp)
        except NoSectionError:
            """ No proxy defined"""
 
    @classmethod 
    def readUserValues(self):
        """ generated source for method readuservalues """
        OtcConfig.USERNAME = os.getenv("OS_USERNAME", None)
        OtcConfig.PASSWORD = os.getenv("OS_PASSWORD", None)
        OtcConfig.DOMAIN = os.getenv("OS_USER_DOMAIN_NAME", None)
        OtcConfig.ak = os.getenv("S3_ACCESS_KEY_ID", None)
        OtcConfig.sk = os.getenv("S3_SECRET_ACCESS_KEY", None)
        OtcConfig.PROJECT_ID = os.getenv("PROJECT_ID", None)


        Config = ConfigParser.ConfigParser()
        
        Config.read(OtcConfig.OTC_USER_FILE) 
                    

        
        if(OtcConfig.USERNAME is None):
            OtcConfig.USERNAME = Config.get("otc", "username") 

        if(OtcConfig.PASSWORD is None):
            OtcConfig.PASSWORD = Config.get("otc", "apikey") 

        if(OtcConfig.ak  is None):
            OtcConfig.ak = Config.get("otc", "otc_access_key_id") 
        if(OtcConfig.sk  is None):
            OtcConfig.sk = Config.get("otc", "otc_secret_access_key") 

        if(OtcConfig.PROJECT_ID  is None and Config.has_option("otc", "project_id")):
            OtcConfig.PROJECT_ID = Config.get("otc", "project_id", "") 
        else:
            OtcConfig.PROJECT_ID = str()

        
        if(OtcConfig.DOMAIN is None):
            OtcConfig.DOMAIN = str(OtcConfig.USERNAME).split(' ')[1]            
                
        OtcConfig.resetUrlVars()

    @classmethod
    def reSetUserValues(cls):
        """ generated source for method reSetUserValues """
        cls.readUserValues()
        cls.UserInput.getAuthKeys()
        ConfigLoader.persistUserValues()

    @classmethod
    def persistProxyValues(cls):
        """ generated source for method persistProxyValues """
        
        cfgfile = open(cls.OtcConfig.OTC_PROXY_FILE, 'w')
        Config = ConfigParser.ConfigParser()
        # add the settings to the structure of the file, and lets write it out...
        Config.add_section('otc')
        Config.set('otc', 'proxy_host', cls.OtcConfig.PROXY_URL)
        Config.set('otc', 'proxy_port', cls.OtcConfig.proxy_port)
        try:
            os.makedirs(cls.OtcConfig.OTC_USER_DIR)
            Config.write(cfgfile)
        except Exception as e:
            print("Error during save keys/date pairs", e)

        cfgfile.close()
        

    @classmethod
    def persistUserValues(cls):
        """ generated source for method persistUserValues """

        cfgfile = open(cls.OtcConfig.OTC_PROXY_FILE, 'w')
        Config = ConfigParser.ConfigParser()
        # add the settings to the structure of the file, and lets write it out...
        Config.add_section('otc')
        Config.set('otc', "otc_access_key_id", cls.OtcConfig.ak)
        Config.set('otc', "otc_secret_access_key", cls.OtcConfig.sk)
        Config.set('otc', "username", cls.OtcConfig.USERNAME)
        Config.set('otc', "apikey", cls.OtcConfig.PASSWORD)
        try:
            os.makedirs(cls.OtcConfig.OTC_USER_DIR)
            Config.write(cfgfile)
        except Exception as e:
            print("Error during save keys/date pairs", e)
        cfgfile.close()
        
        
    @classmethod
    def reSetProxyValues(cls):
        """ generated source for method reSetProxyValues """
        cls.readProxyValues()
        cls.UserInput.getProxyKeys()
        cls.persistProxyValues()

    @classmethod
    def validateConfig(cls):
        """ generated source for method validateConfig """
        if OtcConfig.USERNAME != None and len(OtcConfig.USERNAME) == 32 and OtcConfig.PASSWORD != None and len(OtcConfig.PASSWORD) == 32 and OtcConfig.DOMAIN != None and len(OtcConfig.DOMAIN) == 23:
            cls.otcServiceCalls.getIamToken()
        elif OtcConfig.ak != None and len(OtcConfig.ak) == 32 and OtcConfig.sk != None and len(OtcConfig.sk) == 32:
            print "TODO: ERROR NOT IMPLEMENTED !!!"
        else:
            raise ValueError()

