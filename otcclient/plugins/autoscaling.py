#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of OTC Tool released under MIT license.
# Copyright (C) 2016 T-systems Kurt Garloff, Zsolt Nagy


from otcclient.core.OtcConfig import OtcConfig 
from otcclient.utils import utils_http

from otcclient.core.otcpluginbase import otcpluginbase
from otcclient.core.pluginmanager import getplugin
import base64
from time import sleep
import sys
import json
    
class autoscaling(otcpluginbase):
    ar = {}    
    
    @staticmethod
    def otcOutputHandler(): 
        return getplugin(OtcConfig.OUTPUT_FORMAT)
 
    def otctype(self):
        return "func" 

    @staticmethod
    def delete_launch_configuration():
        raise RuntimeError("NOT IMPLEMENTED!")
        if not (OtcConfig.PUBLICIP is None):
            autoscaling.convertPublicIpNameToId()            
        url = autoscaling.baseurl+ "/v1/" + OtcConfig.PROJECT_ID + "/publicips" + \
        "/" + OtcConfig.PUBLICIPID
        ret = utils_http.delete(url)
        print(ret)
    
              
    @staticmethod
    def create_launch_configuration():
        raise RuntimeError("NOT IMPLEMENTED!")

    @staticmethod
    def attach_instances():
        raise RuntimeError("NOT IMPLEMENTED!")



    @staticmethod
    def create_auto_scaling_group():
        raise RuntimeError("NOT IMPLEMENTED!")

    @staticmethod
    def delete_auto_scaling_group():
        raise RuntimeError("NOT IMPLEMENTED!")

