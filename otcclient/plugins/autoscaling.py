#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is part of OTC Tool released under MIT license.
# Copyright (C) 2016 T-systems Kurt Garloff, Zsolt Nagy

from otcclient.core.OtcConfig import OtcConfig 
from otcclient.utils import utils_http

from otcclient.core.otcpluginbase import otcpluginbase
from otcclient.core.pluginmanager import getplugin
import json 
    
class autoscaling(otcpluginbase):
    ar = {}    
    
    @staticmethod
    def otcOutputHandler(): 
        return getplugin(OtcConfig.OUTPUT_FORMAT)
 
    def otctype(self):
        return "func" 

    @staticmethod
    def convertASNameToId():
        url = autoscaling.baseurl + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_group"
        JSON = utils_http.get(url)
        parsed = json.loads(JSON)
        autoscalings = parsed["scaling_groups"]        
        ret = None
        for s in autoscalings:
            if s.get("scaling_group_name") == OtcConfig.SCALINGGROUP_NAME:
                ret = s["scaling_group_id"]
        OtcConfig.SCALINGGROUP_ID = ret        


    @staticmethod
    def create_auto_scaling_group():
        raise RuntimeError("TODO: Not implemented!")
#         if not (OtcConfig.SCALINGGROUP_NAME is None):
#             autoscaling.convertASNameToId()
#             
#         REQ_CREATE_SCG = None
#         url = autoscaling.baseurl+ "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_group"
#         ret = utils_http.post(url, REQ_CREATE_SCG)
#         print(ret)
#         return ret



    @staticmethod
    def delete_auto_scaling_group():
        if not (OtcConfig.SCALINGGROUP_NAME is None):
            autoscaling.convertASNameToId()            
        url = autoscaling.baseurl + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_group/" + OtcConfig.SCALINGGROUP_ID 
        ret = utils_http.delete(url)
        print(ret)
        return ret

    @staticmethod 
    def describe_auto_scaling_groups():
        url = autoscaling.baseurl + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_group"
        ret = utils_http.get(url)    
        autoscaling.otcOutputHandler().print_output(ret, 
                                                    mainkey="scaling_groups",
                                                    listkey={"scaling_group_name",
                                                             "scaling_group_id", 
                                                             "networks",
                                                             "scaling_group_status",
                                                             "scaling_configuration_id",
                                                             "scaling_configuration_name",
                                                             "current_instance_number", 
                                                             "desire_instance_number",
                                                             "min_instance_number", 
                                                             "max_instance_number", 
                                                             "cool_down_time",
                                                             "lb_listener_id", 
                                                             "security_groups", 
                                                             "create_time", 
                                                             "instance_terminate_policy",
                                                             "is_scaling"}) 
        return ret

    @staticmethod     
    def describe_auto_scaling_configuration():
        url = autoscaling.baseurl + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_configuration"
        ret = utils_http.get(url)
        autoscaling.otcOutputHandler().print_output(ret, mainkey="scaling_configurations", listkey={"scaling_configuration_name",
                                                                                                    "scaling_configuration_id",
                                                                                                     "create_time", "instance_config"})
        return ret

    @staticmethod     
    def describe_auto_scaling_instances():
        if not (OtcConfig.SCALINGGROUP_NAME is None):
            autoscaling.convertASNameToId()            
        url = autoscaling.baseurl + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_group_instance/" + OtcConfig.SCALINGGROUP_ID + "/list"  
        ret = utils_http.get(url)
        autoscaling.otcOutputHandler().print_output(ret, mainkey="scaling_group_instances",
                                                    listkey={"instance_id", "scaling_group_name",
                                                              "create_time", "health_status",
                                                              "scaling_configuration_name",
                                                               "scaling_configuration_id",
                                                               "instance_name"})
        return ret

    @staticmethod     
    def describe_policies():
        if not (OtcConfig.SCALINGGROUP_NAME is None):
            autoscaling.convertASNameToId()            
        url = autoscaling.baseurl + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_policy/" + OtcConfig.SCALINGGROUP_ID + "/list"  
        ret = utils_http.get(url)
        autoscaling.otcOutputHandler().print_output(ret, mainkey="scaling_policies",
                                                     listkey={"scaling_policy_id", "scaling_group_id",
                                                               "create_time", "scaling_policy_name",
                                                                "scaling_policy_type", "scheduled_policy",
                                                                 "cool_down_time", "scaling_policy_action",
                                                                  "policy_status"})
        return ret


    @staticmethod     
    def describe_activitylog():
        if not (OtcConfig.SCALINGGROUP_NAME is None):
            autoscaling.convertASNameToId()            
        url = autoscaling.baseurl + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_activity_log/" + OtcConfig.SCALINGGROUP_ID           
        ret = utils_http.get(url)
        
        autoscaling.otcOutputHandler().print_output(ret, mainkey="scaling_activity_log", listkey={"id", "status", "description", "instance_value", "desire_value", "scaling_configuration_name", "scaling_value", "start_time", "end_time", "instance_added_list", "instance_deleted_list", "instance_removed_list"})
        return ret

    @staticmethod     
    def describe_quotas():    
        url = autoscaling.baseurl + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/quotas"            
        ret = utils_http.get(url)    
        parsed = json.loads(ret)
        autoscaling.otcOutputHandler().print_output(parsed["quotas"]["resources"], mainkey="", listkey={"type", "used", "quota", "max"})
        return ret


    @staticmethod
    def create_launch_configuration():
        raise RuntimeError("NOT IMPLEMENTED!")


    @staticmethod
    def delete_launch_configuration():
        raise RuntimeError("NOT IMPLEMENTED!")
#         if not (OtcConfig.PUBLICIP is None):
#             autoscaling.convertPublicIpNameToId()            
#         url = autoscaling.baseurl+ "/v1/" + OtcConfig.PROJECT_ID + "/publicips" + \
#         "/" + OtcConfig.PUBLICIPID
#         ret = utils_http.delete(url)
#         print(ret)
    
              





