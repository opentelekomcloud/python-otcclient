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
    def convertClusterNameToId():
        url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/clusters"
        JSON = utils_http.get(url)        
        parsed  = json.loads(JSON)
        clusters = parsed
        ret = None
        for cluster in clusters:
            if cluster.get("metadata").get("name") == OtcConfig.CLUSTER:
                ret = cluster.get("metadata").get("uuid")
        OtcConfig.CLUSTER_ID = ret



    @staticmethod
    def list_clusters():
        url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/clusters"
        ret = utils_http.get(url)
        cce.otcOutputHandler().print_output(json.loads(ret), subkey="metadata", listkey={"name", "uuid", "createAt"})
        #ecs.otcOutputHandler().print_output(json.loads(ret),mainkey="")     
        return ret

    @staticmethod
    def describe_clusters():        
        if OtcConfig.CLUSTER:
            cce.convertClusterNameToId()
                
        if OtcConfig.CLUSTER_ID:
            url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/clusters/" + OtcConfig.CLUSTER_ID            
            ret = utils_http.get(url)
            ecs.otcOutputHandler().print_output(ret,mainkey="")     
        else:
            return cce.list_clusters()     

    @staticmethod
    def list_container_instances():
        if OtcConfig.CLUSTER:
            cce.convertClusterNameToId()

        if OtcConfig.INSTANCE_NAME:
            ecs.convertINSTANCENameToId()
        
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
        if OtcConfig.CLUSTER:
            cce.convertClusterNameToId()
        url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/services"
        ret = utils_http.get(url)
        ecs.otcOutputHandler().print_output(ret,mainkey="")     
        return ret


    @staticmethod
    def create_namespace():
        if OtcConfig.CLUSTER:
            cce.convertClusterNameToId()         
        url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/namespaces"
        req = utils_templates.create_request("create_namespace")
        print req
        print OtcConfig.NAMESPACE
        ret = utils_http.post(url, req)
        print ret
        #ecs.otcOutputHandler().print_output(ret,mainkey="")     
        return ret


    @staticmethod
    def describe_namespaces():
        if OtcConfig.CLUSTER:
            cce.convertClusterNameToId()
            
        if OtcConfig.NAMESPACE:
            url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/namespaces/" + OtcConfig.NAMESPACE
        else:          
            url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/namespaces"    
        ret = utils_http.post(url)        
        ecs.otcOutputHandler().print_output(ret,mainkey="")     
        return ret

    @staticmethod       
    def delete_namespaces():
        if OtcConfig.CLUSTER:
            cce.convertClusterNameToId()
        url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/namespaces/" + OtcConfig.NAMESPACE
        ret = utils_http.delete(url)
        print(ret)
        return ret


