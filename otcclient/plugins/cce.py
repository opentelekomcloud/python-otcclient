#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of OTC Tool released under MIT license.
# Copyright (C) 2016 T-systems Kurt Garloff, Zsolt Nagy

from otcclient.core.OtcConfig import OtcConfig 
from otcclient.utils import utils_http, utils_templates

from otcclient.core.otcpluginbase import otcpluginbase
from otcclient.core.pluginmanager import getplugin
import json
from otcclient.plugins.ecs import ecs
import os
    
class cce(otcpluginbase):
    ar = {}    
    
    @staticmethod
    def otcOutputHandler(): 
        return getplugin(OtcConfig.OUTPUT_FORMAT)
 
    def otctype(self):
        return "func" 


#ret = utils_templates.create_request("template_name")
#return ret


    @staticmethod
    def list_clusters():
        url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/clusters"
        ret = utils_http.get(url)
        ecs.otcOutputHandler().print_output(ret,mainkey="")     
        return ret

    @staticmethod
    def describe_clusters():
        if OtcConfig.CLUSTER_ID:
            url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/clusters/" + OtcConfig.CLUSTER_ID
            ret = utils_http.get(url)
            ecs.otcOutputHandler().print_output(ret,mainkey="")     
        else:
            return cce.list_clusters()     

    @staticmethod
    def list_container_instances():
        if OtcConfig.INSTANCE_ID:
            url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/clusters/" + OtcConfig.CLUSTER_ID + "/hosts"
            ret = utils_http.get(url)
            ecs.otcOutputHandler().print_output(ret,mainkey="")     
        else:
            url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/clusters/" + OtcConfig.CLUSTER_ID + "/hosts/" + OtcConfig.INSTANCE_ID 
            ret = utils_http.get(url)
            ecs.otcOutputHandler().print_output(ret,mainkey="")     
        return ret
        
        

    

    @staticmethod
    def list_services():
        url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/clusters"
        ret = utils_http.get(url)
        ecs.otcOutputHandler().print_output(ret,mainkey="")     
        return ret


