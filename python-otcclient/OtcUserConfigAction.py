#!/usr/bin/env python
""" generated source for module UserInput """
#  
#  * Copyright (c) 2016 T-Systems GmbH
#  * Germany
#  * All rights reserved.
#  * 
#  * Name: OtcUserConfiguration.py
#  * Author: zsonagy
#  * Datum: 08.03.2016
#  
#  * Handling the following input from console: - User Config ,Proxy Config#  * #  * @author zsonagy
import OtcConfig 
import argparse
from ConfigLoader import ConfigLoader
from OtcConfig import OtcConfig

class OtcUserConfigAction(argparse.Action):
    
    def __init__(self,
                 option_strings,
                 dest,
                 nargs=None,
                 const=None,
                 default=None,
                 type=None,
                 choices=None,
                 required=False,
                 help=None,
                 metavar=None):
        argparse.Action.__init__(self,
                                 option_strings=option_strings,
                                 dest=dest,
                                 nargs=nargs,
                                 const=const,
                                 default=default,
                                 type=type,
                                 choices=choices,
                                 required=required,
                                 help=help,
                                 metavar=metavar,
                                 )
 #       print
 #       print 'Initializing CustomAction'
        for name,value in sorted(locals().items()):
            if name == 'self' or value is None:
                continue
#            print '  %s = %r' % (name, value)
        return

    def __call__(self, parser, namespace, values, option_string=None):
        
        print 'Processing CustomAction for "%s"' % self.dest
        #print '  parser = %s' % id(parser)
        print '  values = %r' % values
        print '  option_string = %r' % option_string
        
        # Do some arbitrary processing of the input values
        if isinstance(values, list):
            values = [ v.upper() for v in values ]
            print values
        else:
            values = values.upper()
            print values
        # Save the results in the namespace using the destination
        # variable given to our constructor.
        OtcConfig.MAINCOM = values
        

        try:
        
            if OtcConfig.MAINCOM == "configure".lower():
                ConfigLoader.reSetUserValues()
                
            if str(OtcConfig.MAINCOM) == "configure-proxy".upper():
                ConfigLoader.reSetProxyValues()
                exit(0)

            
        except Exception as e:
            print "Configuration file error. \nPlease run following command: \n    otc configure "
            exit(1)        

    """ generated source for class UserInput """
    # 	static final Logger log = LogManager.getLogger(UserInput.class.__name__);
    # 	static Scanner scan;
    @classmethod
    def getProxyKeys(cls):
        """ generated source for method getProxyKeys """
        
        OtcConfig.PROXY_URL = cls.getUserTypedValue("Enter a proxy host:", -1)
        OtcConfig.PROXY_PORT = int(cls.getUserTypedValue("Enter a proxy port:", 4))
        

    @classmethod
    def getAuthKeys(cls):
        """ generated source for method getAuthKeys """
        
        OtcConfig.USERNAME = cls.getUserTypedValue("Enter a Username:", 32)
        OtcConfig.PASSWORD = cls.getUserTypedValue("Enter a API Key:", 32)
        OtcConfig.DOMAIN = cls.OtcConfig.USERNAME.split(str=" ")[1]
        #  OtcConfig.PROJECT_ID = getUserTypedValue("Enter a Project ID:", 32);
        OtcConfig.ak = cls.getUserTypedValue("Enter a Access Key:", -1)
        OtcConfig.sk = cls.getUserTypedValue("Enter a Secret Key:", -1)
        

    @classmethod
    def getUserTypedValue(cls, title, len):
        """ generated source for method getUserTypedValue """
        validData = False
        val = None
        while True:        
            try:
                import io
                val = input(title)
                #  tries to get data. Goes to catch if
                #  invalid data
                if val != None and len((val) == len or len <= 0):
                    validData = True
                    #  if gets data successfully, sets boolean
                    #  to true
                else:
                    raise ValueError()
            except Exception as e:
                #  executes when this exception occurs
                #  e.printStackTrace();
                print "Input has to be a correct. "
            if not ((validData == False)):
                break
        #  loops until validData is true
        #  scan.close();
        return val

