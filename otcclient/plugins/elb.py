#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of OTC Tool released under MIT license.
# Copyright (C) 2016 T-systems Kurt Garloff, Zsolt Nagy

from otcclient.core.OtcConfig import OtcConfig 
from otcclient.utils import utils_http

from otcclient.core.otcpluginbase import otcpluginbase
from otcclient.core.pluginmanager import getplugin
import json
from otcclient.plugins.ecs import ecs
import os
    
class elb(otcpluginbase):
    ar = {}    
    
    @staticmethod
    def otcOutputHandler(): 
        return getplugin(OtcConfig.OUTPUT_FORMAT)
 
    def otctype(self):
        return "func" 

    @staticmethod
    def attach_load_balancers():
        pass
              
    @staticmethod
    def create_launch_configuration():
        raise RuntimeError("NOT IMPLEMENTED!")

    @staticmethod
    def delete_load_balancers():        
        if not (OtcConfig.LOADBALANCER_NAME is None):
            elb.convertELBNameToId()            
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1.0/" + OtcConfig.PROJECT_ID + "/elbaas/loadbalancers" + "/" + OtcConfig.LOADBALANCER_ID

        ret = utils_http.delete(url)
        print(ret)
        return ret

    @staticmethod
    def describe_listeners():
        if not (OtcConfig.LOADBALANCER_NAME is None):
            elb.convertELBNameToId()

        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1.0/" + OtcConfig.PROJECT_ID + "/elbaas/listeners" + "?loadbalancer_id=" + OtcConfig.LOADBALANCER_ID       
               
        ret = utils_http.get(url)
        mod =  ret.replace("[","").replace("]","")        
        ecs.otcOutputHandler().print_output(mod,mainkey="")
        return ret

    @staticmethod
    def describe_members():
        if not (OtcConfig.LISTENER_NAME is None):
            elb.convertLISTENERNameToId()

        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1.0/" + OtcConfig.PROJECT_ID + "/elbaas/listeners/" + OtcConfig.LISTENER_ID + "/members"       
               
        ret = utils_http.get(url)
        mod =  "{ \"members\": " + ret + " }" 
    
        
        elb.otcOutputHandler().print_output(mod, mainkey="members", listkey={"server_address","server_id","server_name","update_time","create_time","id","name","status","health_status","address" } )
        return ret


    @staticmethod
    def describe_health_check():
        if not (OtcConfig.LOADBALANCER_NAME is None):
            elb.convertELBNameToId()
        
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1.0/" + OtcConfig.PROJECT_ID + "/elbaas/healthcheck/" + OtcConfig.HEALTCHECK_ID        
               
        ret = utils_http.get(url)
        
        ecs.otcOutputHandler().print_output(ret,mainkey="")
        return ret



    @staticmethod
    def describe_load_balancers():
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1.0/" + OtcConfig.PROJECT_ID + "/elbaas/loadbalancers"        
        if not (OtcConfig.LOADBALANCER_NAME is None):
            elb.convertELBNameToId()
        
        if OtcConfig.LOADBALANCER_ID:
            url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1.0/" + OtcConfig.PROJECT_ID + "/elbaas/loadbalancers" + "/" + OtcConfig.LOADBALANCER_ID
            ret = utils_http.get(url)                       
            ecs.otcOutputHandler().print_output(ret,mainkey="")
        else:
            url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1.0/" + OtcConfig.PROJECT_ID + "/elbaas/loadbalancers"
            ret = utils_http.get(url) 
            elb.otcOutputHandler().print_output(ret, mainkey="loadbalancers", listkey={"vip_address","update_time","create_time","id","name","status","bandwidth","admin_state_up","type","description" } )
                         
        return ret


    @staticmethod
    def convertELBNameToId():
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1.0/" + OtcConfig.PROJECT_ID + "/elbaas/loadbalancers"        
        JSON = utils_http.get(url)        
        parsed  = json.loads(JSON)
        loadbalancers = parsed["loadbalancers"]        
        ret = None
        for loadbalancer in loadbalancers:
            if loadbalancer.get("name") == OtcConfig.LOADBALANCER_NAME: # and ( loadbalancer.get("vpc_id") == OtcConfig.VPCID or OtcConfig.VPCID is None ) :
                OtcConfig.LOADBALANCER_ID = loadbalancer["id"]
                ret = OtcConfig.LOADBALANCER_ID
        return ret               

    @staticmethod
    def convertLISTENERNameToId():
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1.0/" + OtcConfig.PROJECT_ID + "/elbaas/listeners"        
        JSON = utils_http.get(url)        
        
        parsed  = json.loads(JSON)
        listeners = parsed        
        ret = None
        for listener in listeners:
            if listener.get("name") == OtcConfig.LISTENER_NAME: # and ( loadbalancer.get("vpc_id") == OtcConfig.VPCID or OtcConfig.VPCID is None ) :
                OtcConfig.LISTENER_ID = listener["id"]
                ret = OtcConfig.LISTENER_ID
        return ret               


    @staticmethod 
    def create_load_balancers():
        if not (OtcConfig.LOADBALANCER_NAME is None):
            elb.convertELBNameToId()
        if not (OtcConfig.VPCNAME is None):
            ecs.convertVPCNameToId()        
         
        REQ_CREATE_ELB = "{ \"name\": \"" + OtcConfig.LOADBALANCER_NAME + "\", \"description\": \"" + OtcConfig.LOADBALANCER_NAME+ "\", \"vpc_id\": \"" + OtcConfig.VPCID +"\", \"bandwidth\": 10, \"type\": \"External\", \"admin_state_up\": true }" 
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1.0/" + OtcConfig.PROJECT_ID + "/elbaas/loadbalancers"
        ret = utils_http.post(url, REQ_CREATE_ELB)
        print(ret)         
        maindata = json.loads(ret)
        if "code" in  maindata:            
            print("Can not create:" +maindata["message"])  
            os._exit( 1 )             
        print("created")        
        return ret



    @staticmethod 
    def create_listeners():
        raise RuntimeError('NOT TESTED YET!!!!')
        if not (OtcConfig.LOADBALANCER_NAME is None):
            elb.convertELBNameToId()
        if not (OtcConfig.VPCNAME is None):
            ecs.convertVPCNameToId()                
         
        #REQ_CREATE_ELB = "{ \"name\": \"" + OtcConfig.LOADBALANCER_NAME + "\", \"description\": \"" + OtcConfig.LOADBALANCER_NAME+ "\", \"vpc_id\": \"" + OtcConfig.VPCID +"\", \"bandwidth\": 10, \"type\": \"External\", \"admin_state_up\": true }"
        REQ_CREATE_LISTENER = "{ \"name\":\"listener1\", \"description\":\"\", \"loadbalancer_id\":\"0b07acf06d243925bc24a0ac7445267a\", \"protocol\":\"HTTP\", \"port\":88, \"backend_protocol\":\"HTTP\", \"backend_port\":80, \"lb_algorithm\":\"roundrobin\", \"session_sticky\":true, \"sticky_session_type\":\"insert\", \"cookie_timeout\":100 }"         
        #print( REQ_CREATE_ELB )        
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1.0/" + OtcConfig.PROJECT_ID + "/elbaas/listeners"
        ret = utils_http.post(url, REQ_CREATE_LISTENER)
        print( ret )
        maindata = json.loads(ret)
        if "code" in  maindata:            
            print("Can not create:" +maindata["message"])  
            os._exit( 1 )             
        
        print( ret )
        #ecs.otcOutputHandler().print_output(ret, mainkey="loadbalancer")
        return ret

    @staticmethod
    def describe_quotas():
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1.0/" + OtcConfig.PROJECT_ID + "/elbaas/quotas"                           
        ret = utils_http.get(url)
        print( ret )
        ecs.otcOutputHandler().print_output(ret,mainkey="")
        return ret
