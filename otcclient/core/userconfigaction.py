#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of OTC Tool released under MIT license.
# Copyright (C) 2016 T-systems Kurt Garloff, Zsolt Nagy

import argparse
from configloader import  configloader
from OtcConfig import OtcConfig

class userconfigaction(argparse.Action):
    
    def __init__(self,
                 option_strings,
                 dest,
                 nargs=None,
                 const=None,
                 default=None,
                 type=None,  # @ReservedAssignment
                 choices=None,
                 required=False,
                 help=None,  # @ReservedAssignment
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
        for name,value in sorted(locals().items()):
            if name == 'self' or value is None:
                continue
#            print '  %s = %r' % (name, value)
        return

    def __call__(self, parser, namespace, values, option_string=None):        
        if isinstance(values, list):
            values = [ v.upper() for v in values ]
            print values
        else:
            values = values.lower()
            print values
        OtcConfig.MAINCOM = values
        try:                        
            if OtcConfig.MAINCOM == "user":
                userconfigaction.reSetUserValues()
                print "configure exit"
                exit( 1 )        
                
            if str(OtcConfig.MAINCOM) == "configure-proxy".upper():
                userconfigaction.reSetProxyValues()
                exit(0)

            
        except Exception :
            print "Configuration file error. \nPlease run following command: \n    otc configure "
            raise
            exit(1)        

    @classmethod
    def getProxyKeys(cls):        
        OtcConfig.PROXY_URL = cls.getUserTypedValue("Enter a proxy host:", -1)
        OtcConfig.PROXY_PORT = int(cls.getUserTypedValue("Enter a proxy port:", 4))
        

    @staticmethod
    def getAuthKeys():
        OtcConfig.USERNAME = userconfigaction.getUserTypedValue("Enter a Username:", 32)
        OtcConfig.PASSWORD = userconfigaction.getUserTypedValue("Enter a API Key:", 32)
        OtcConfig.DOMAIN = OtcConfig.USERNAME.split(str=" ")[1]
        #  OtcConfig.PROJECT_ID = getUserTypedValue("Enter a Project ID:", 32);
        OtcConfig.ak = userconfigaction.getUserTypedValue("Enter a Access Key:", -1)
        OtcConfig.sk = userconfigaction.getUserTypedValue("Enter a Secret Key:", -1)
        

    @staticmethod
    def reSetUserValues():
        configloader.readUserValues()
        userconfigaction.getAuthKeys()
        configloader.persistUserValues()
        
    @staticmethod
    def reSetProxyValues():
        configloader.readProxyValues()
        userconfigaction.getProxyKeys()
        configloader.persistProxyValues()        
        
    @classmethod
    def getUserTypedValue(cls, title, length):
        validData = False
        val = None
        while True:        
            try:

                val = input(title)
                #  tries to get data. Goes to catch if
                #  invalid data
                if val != None and len((val) == length or length <= 0):
                    validData = True
                    #  if gets data successfully, sets boolean
                    #  to true
                else:
                    raise ValueError()
            except Exception :
                #  executes when this exception occurs
                print "Input has to be a correct. "
            if not ((validData == False)):
                break
        #  loops until validData is true
        return val

