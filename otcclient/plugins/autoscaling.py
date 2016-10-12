#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is part of OTC Tool released under MIT license.
# Copyright (C) 2016 T-systems Kurt Garloff, Zsolt Nagy

from otcclient.core.OtcConfig import OtcConfig 
from otcclient.utils import utils_http

from otcclient.core.otcpluginbase import otcpluginbase
from otcclient.core.pluginmanager import getplugin

import json
from otcclient.utils import utils_templates 
from otcclient.plugins.ecs import ecs
    
class autoscaling(otcpluginbase):
    ar = {}    
    
    @staticmethod
    def otcOutputHandler(): 
        return getplugin(OtcConfig.OUTPUT_FORMAT)
 
    def otctype(self):
        return "func" 

    @staticmethod
    def convertASNameToId():
        url = "https://" + OtcConfig.DEFAULT_HOST + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_group"
        JSON = utils_http.get(url)
        parsed = json.loads(JSON)
        autoscalings = parsed["scaling_groups"]        
        ret = None
        for s in autoscalings:
            if s.get("scaling_group_name") == OtcConfig.SCALINGGROUP_NAME:
                ret = s["scaling_group_id"]
        OtcConfig.SCALINGGROUP_ID = ret        


    @staticmethod     
    def convertASPolicyNameToId():
        if not (OtcConfig.SCALINGGROUP_NAME is None):
            autoscaling.convertASNameToId()         
            
        url = "https://" + OtcConfig.DEFAULT_HOST + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_policy/" + OtcConfig.SCALINGGROUP_ID + "/list?scaling_policy_name="  ++ OtcConfig.SCALING_POLICY_NAME
        JSON = utils_http.get(url)
        parsed = json.loads(JSON)
        as_policy = parsed["scaling_policies"]        
        ret = None
        for s in as_policy:
            if s.get("scaling_policy_name") == OtcConfig.SCALING_POLICY_NAME:
                ret = s["scaling_policy_id"]
        OtcConfig.SCALING_POLICY_ID = ret   

        
    @staticmethod     
    def convertASConfigurationNameToId():
        url = "https://" + OtcConfig.DEFAULT_HOST + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_configuration"
        JSON = utils_http.get(url)
        parsed = json.loads(JSON)
        autoscaleConfs = parsed["scaling_configurations"]        
        ret = None
        for s in autoscaleConfs:
            if s.get("scaling_configuration_name") == OtcConfig.SCALING_CONFIGURATION_NAME:
                ret = s["scaling_configuration_id"]
                
        OtcConfig.SCALING_CONFIGURATION_ID = ret    
        
    @staticmethod
    def delete_auto_scaling_group():
        if not (OtcConfig.SCALINGGROUP_NAME is None):
            autoscaling.convertASNameToId()            
        url = "https://" + OtcConfig.DEFAULT_HOST + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_group/" + OtcConfig.SCALINGGROUP_ID 
        ret = utils_http.delete(url)
        print(ret)
        return ret

    @staticmethod 
    def describe_auto_scaling_groups():
        url = "https://" + OtcConfig.DEFAULT_HOST + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_group"
        ret = utils_http.get(url)    
        autoscaling.otcOutputHandler().print_output(ret, mainkey="scaling_groups",listkey={"instance_terminate_policy","is_scaling"}) 
        return ret

    @staticmethod 
    def describe_auto_scaling_groups_details():
        if not (OtcConfig.SCALINGGROUP_NAME is None):
            autoscaling.convertASNameToId()     
        url = "https://" + OtcConfig.DEFAULT_HOST + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_group" + OtcConfig.SCALINGGROUP_ID
        ret = utils_http.get(url)    
        autoscaling.otcOutputHandler().print_output(ret, 
                                                    mainkey="scaling_group",
                                                             listkey={"instance_terminate_policy",
                                                             "is_scaling"}) 
        return ret      
        
    @staticmethod     
    def describe_auto_scaling_configuration():
        url = "https://" + OtcConfig.DEFAULT_HOST + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_configuration"
        ret = utils_http.get(url)
        autoscaling.otcOutputHandler().print_output(ret, mainkey="scaling_configurations", listkey={"scaling_configuration_name",
                                                                                                    "scaling_configuration_id",
                                                                                                     "create_time", "instance_config"})
        return ret

    @staticmethod     
    def describe_auto_scaling_configuration_details():
        if not (OtcConfig.SCALING_CONFIGURATION_NAME is None):
            autoscaling.convertASConfigurationNameToId()
        url = "https://" + OtcConfig.DEFAULT_HOST + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_configuration/" + OtcConfig.SCALING_CONFIGURATION_ID
        ret = utils_http.get(url)
        autoscaling.otcOutputHandler().print_output(ret, mainkey="scaling_configuration", listkey={"scaling_configuration_name",
                                                                                                    "scaling_configuration_id",
                                                                                                     "create_time", "instance_config"})
        return ret      
        
    @staticmethod     
    def describe_auto_scaling_instances():
        if not (OtcConfig.SCALINGGROUP_NAME is None):
            autoscaling.convertASNameToId()            
        url = "https://" + OtcConfig.DEFAULT_HOST + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_group_instance/" + OtcConfig.SCALINGGROUP_ID + "/list"
        ret = utils_http.get(url)
        autoscaling.otcOutputHandler().print_output(ret, mainkey="scaling_group_instances",listkey={"instance_id", "scaling_group_name"} )
        return ret

    @staticmethod     
    def describe_policies():
        if not (OtcConfig.SCALINGGROUP_NAME is None):
            autoscaling.convertASNameToId()            
        url = "https://" + OtcConfig.DEFAULT_HOST + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_policy/" + OtcConfig.SCALINGGROUP_ID + "/list"  
        ret = utils_http.get(url)
        autoscaling.otcOutputHandler().print_output(ret, mainkey="scaling_policies",
                                                                 listkey={"cool_down_time", "scaling_policy_action",
                                                                  "policy_status"})
        return ret


    @staticmethod     
    def describe_activitylog():
        if not (OtcConfig.SCALINGGROUP_NAME is None):
            autoscaling.convertASNameToId()            
        url = "https://" + OtcConfig.DEFAULT_HOST + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_activity_log/" + OtcConfig.SCALINGGROUP_ID           
        ret = utils_http.get(url)
        
        autoscaling.otcOutputHandler().print_output(ret, mainkey="scaling_activity_log", listkey={"id", "status", "description", "instance_value", "desire_value", "scaling_configuration_name", "scaling_value", "start_time", "end_time", "instance_added_list", "instance_deleted_list", "instance_removed_list"})
        return ret

    @staticmethod     
    def describe_quotas():    
        url = "https://" + OtcConfig.DEFAULT_HOST + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/quotas"            
        ret = utils_http.get(url)    
        parsed = json.loads(ret)
        autoscaling.otcOutputHandler().print_output(parsed["quotas"]["resources"], mainkey="", listkey={"type", "used", "quota", "max"})
        return ret

    @staticmethod     
    def describe_quotas_of_group():    
        if not (OtcConfig.SCALINGGROUP_NAME is None):
            autoscaling.convertASNameToId()
        url = "https://" + OtcConfig.DEFAULT_HOST + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/quotas/" + OtcConfig.SCALINGGROUP_ID
        ret = utils_http.get(url)    
        parsed = json.loads(ret)
        autoscaling.otcOutputHandler().print_output(parsed["quotas"]["resources"], mainkey="", listkey={"type", "used", "quota", "max"})
        return ret      
              
    @staticmethod     
    def describe_policy_details():
        if not (OtcConfig.SCALING_POLICY_NAME is None):
            autoscaling.convertASPolicyNameToId()      
                
                
        url = "https://" + OtcConfig.DEFAULT_HOST + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_policy/" + OtcConfig.SCALING_POLICY_ID  
        ret = utils_http.get(url)
        #autoscaling.otcOutputHandler().print_output(ret, mainkey="scaling_policy",                                                     listkey={"scaling_policy_id", "scaling_group_id"})
        autoscaling.otcOutputHandler().print_output(ret,mainkey="")
        return ret


    @staticmethod
    def create_auto_scaling_policy():
        if not (OtcConfig.SCALINGGROUP_NAME is None):
            autoscaling.convertASNameToId()             
        REQ_CREATE_SCP=utils_templates.create_request("create_as_policy")               
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_policy"
        ret = utils_http.post(url, REQ_CREATE_SCP)
        autoscaling.otcOutputHandler().print_output(ret,mainkey="")
        return ret



    @staticmethod
    def create_auto_scaling_group():
        if not (OtcConfig.SCALINGGROUP_NAME is None):
            autoscaling.convertASNameToId()
        
        #vpc_id
        if not (OtcConfig.VPCNAME is None):
            ecs.convertVPCNameToId()
        #scaling_configuration_id
        if not (OtcConfig.SCALING_CONFIGURATION_NAME is None):
            autoscaling.convertASConfigurationNameToId()
          
        #lb_listener_id
        if not (OtcConfig.LISTENER_NAME is None):
            autoscaling.convertLISTENERNameToId()
        #network_id
        if not OtcConfig.SUBNETNAME is None:
            ecs.convertSUBNETNameToId()
        #security_group_id
        if not OtcConfig.SECUGROUPNAME is None:
            ecs.convertSECUGROUPNameToId()
            
        REQ_CREATE_SCG=utils_templates.create_request("create_as_group")               
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_group"
        ret = utils_http.post(url, REQ_CREATE_SCG)
        autoscaling.otcOutputHandler().print_output(ret,mainkey="")
        return ret 


    @staticmethod
    def enable_auto_scaling_policy():
        if not (OtcConfig.SCALING_POLICY_NAME is None):
            autoscaling.convertASPolicyNameToId()       
        OtcConfig.AS_POLICY_ACTION="resume"
        REQ_ACTION_SCP=utils_templates.create_request("execute_enable_disable_as_policy")
        url = "https://" + OtcConfig.DEFAULT_HOST + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_policy/" + OtcConfig.SCALING_POLICY_ID  + "/action" 
        ret = utils_http.post(url, REQ_ACTION_SCP)
        autoscaling.otcOutputHandler().print_output(ret,mainkey="")
        return ret

         
    @staticmethod
    def disable_auto_scaling_policy():
        if not (OtcConfig.SCALING_POLICY_NAME is None):
            autoscaling.convertASPolicyNameToId()       
        OtcConfig.AS_POLICY_ACTION="pause"
        REQ_ACTION_SCP=utils_templates.create_request("execute_enable_disable_as_policy")
        url = "https://" + OtcConfig.DEFAULT_HOST + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_policy/" + OtcConfig.SCALING_POLICY_ID  + "/action" 
        ret = utils_http.post(url, REQ_ACTION_SCP)
        autoscaling.otcOutputHandler().print_output(ret,mainkey="")
        return ret       
    
    @staticmethod
    def execute_auto_scaling_policy():
        if not (OtcConfig.SCALING_POLICY_NAME is None):
            autoscaling.convertASPolicyNameToId()       
        OtcConfig.AS_POLICY_ACTION="execute"
        REQ_ACTION_SCP=utils_templates.create_request("execute_enable_disable_as_policy")               
        url = "https://" + OtcConfig.DEFAULT_HOST + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_policy/" + OtcConfig.SCALING_POLICY_ID  + "/action" 
        ret = utils_http.post(url, REQ_ACTION_SCP)
        autoscaling.otcOutputHandler().print_output(ret,mainkey="")
        return ret
         

    @staticmethod
    def enable_auto_scaling_group():
        if not (OtcConfig.SCALINGGROUP_NAME is None):
            autoscaling.convertASNameToId()  
         
        OtcConfig.ACTION_DISABLE_ENABLE_AS_GROUP="resume"
        REQ_ACTION_SCG=utils_templates.create_request("disable_enable_as_group")               
        url = "https://" + OtcConfig.DEFAULT_HOST + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_group/" + OtcConfig.SCALINGGROUP_ID + "/action" 
        ret = utils_http.post(url, REQ_ACTION_SCG)
        autoscaling.otcOutputHandler().print_output(ret,mainkey="")
        return ret

    @staticmethod
    def disable_auto_scaling_group():
        if not (OtcConfig.SCALINGGROUP_NAME is None):
            autoscaling.convertASNameToId()  
        OtcConfig.ACTION_DISABLE_ENABLE_AS_GROUP="pause"
        REQ_ACTION_SCG=utils_templates.create_request("disable_enable_as_group")               
        url = "https://" + OtcConfig.DEFAULT_HOST + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_group/" + OtcConfig.SCALINGGROUP_ID + "/action" 
        ret = utils_http.post(url, REQ_ACTION_SCG)
        autoscaling.otcOutputHandler().print_output(ret,mainkey="")
        return ret       

    @staticmethod     
    def delete_auto_scaling_instance_from_group():
        if not OtcConfig.INSTANCE_NAME is None:
            ecs.convertINSTANCENameToId()            
        url = "https://" + OtcConfig.DEFAULT_HOST + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_group_instance/" + OtcConfig.INSTANCE_ID 
        ret = utils_http.delete(url)
        print(ret)
        return ret

        

    @staticmethod     
    def batch_delete_auto_scaling_configuration():
        #if not (OtcConfig.SCALING_CONFIGURATION_NAME is None):
        #    autoscaling.convertASConfigurationNameToId()
        REQ_DELETE_BATCH_SC=utils_templates.create_request("batch_delete_AS_config")                
        url = "https://" + OtcConfig.DEFAULT_HOST + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_configurations"
        ret = utils_http.post(url, REQ_DELETE_BATCH_SC)
        autoscaling.otcOutputHandler().print_output(ret,mainkey="")
        return ret


    @staticmethod     
    def batch_add_delete_auto_scaling_instances():
        if not (OtcConfig.SCALINGGROUP_NAME is None):
            autoscaling.convertASNameToId()  
        REQ_BATCH_INST=utils_templates.create_request("batch_remove_add_instance")        

        url = "https://" + OtcConfig.DEFAULT_HOST + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_group_instance/"+ OtcConfig.SCALINGGROUP_ID +"/action"
        ret = utils_http.post(url, REQ_BATCH_INST)
        autoscaling.otcOutputHandler().print_output(ret,mainkey="")
        return ret          

        
    @staticmethod
    def create_launch_configuration():
        raise RuntimeError("NOT IMPLEMENTED!")

    @staticmethod     
    def delete_policies():
        if not (OtcConfig.SCALING_POLICY_NAME is None):
            autoscaling.convertASPolicyNameToId()
        url = "https://" + OtcConfig.DEFAULT_HOST + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_policy/" + OtcConfig.SCALING_POLICY_ID
        ret = utils_http.delete(url)
        print(ret)
        return ret

    @staticmethod     
    def delete_auto_scaling_configuration():
        if not (OtcConfig.SCALING_POLICY_NAME is None):
            autoscaling.convertASPolicyNameToId()
        url = "https://" + OtcConfig.DEFAULT_HOST + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_configuration/"+ OtcConfig.SCALING_CONFIGURATION_ID
        ret = utils_http.delete(url)
        print(ret)
        return ret

    @staticmethod
    def delete_launch_configuration():
        raise RuntimeError("NOT IMPLEMENTED!")
#         if not (OtcConfig.PUBLICIP is None):
#             autoscaling.convertPublicIpNameToId()            
#         url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/publicips" + \
#         "/" + OtcConfig.PUBLICIPID
#         ret = utils_http.delete(url)
#         print(ret)
    
