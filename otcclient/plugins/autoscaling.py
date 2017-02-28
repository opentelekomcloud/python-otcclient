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
#from otcclient.plugins.ecs import ecs
    
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
            
        url = "https://" + OtcConfig.DEFAULT_HOST + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_policy/" + OtcConfig.SCALINGGROUP_ID + "/list?scaling_policy_name="  + OtcConfig.SCALING_POLICY_NAME
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
    @otcfunc(plugin_name=__name__,
             desc="Delete auto scaling group",
             examples=[],
             args = [
                    arg(    '--auto-scaling-group-name',    dest='SCALINGGROUP_NAME',     help='Name of Auto Scaling group'),
                    arg(    '--auto-scaling-group-id',    dest='SCALINGGROUP_ID',     help='Id of Auto Scaling group')
                          ]) 
    def delete_auto_scaling_group():
        if not (OtcConfig.SCALINGGROUP_NAME is None):
            autoscaling.convertASNameToId()            
        url = "https://" + OtcConfig.DEFAULT_HOST + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_group/" + OtcConfig.SCALINGGROUP_ID 
        ret = utils_http.delete(url)
        print(ret)
        return ret

    @staticmethod       
    @otcfunc(plugin_name=__name__,
             desc="Describe auto scaling groups",
             examples=[],
             args = [ ]) 
    def describe_auto_scaling_groups():
        url = "https://" + OtcConfig.DEFAULT_HOST + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_group"
        ret = utils_http.get(url)    
        #print(ret)
        autoscaling.otcOutputHandler().print_output(ret, mainkey="scaling_groups",listkey={"scaling_group_name","scaling_configuration_name","create_time","instance_terminate_policy","is_scaling", "scaling_group_status"}) 
        return ret

    @staticmethod       
    @otcfunc(plugin_name=__name__,
             desc="Describe auto scaling group details",
             examples=[],
             args = [
                    arg(    '--auto-scaling-group-name',    dest='SCALINGGROUP_NAME',     help='Name of Auto Scaling group'),
                    arg(    '--auto-scaling-group-id',    dest='SCALINGGROUP_ID',     help='Id of Auto Scaling group')
                          ]) 
    def describe_auto_scaling_groups_details():
        if not (OtcConfig.SCALINGGROUP_NAME is None):
            autoscaling.convertASNameToId()     
        url = "https://" + OtcConfig.DEFAULT_HOST + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_group/" + OtcConfig.SCALINGGROUP_ID
        ret = utils_http.get(url)    
        autoscaling.otcOutputHandler().print_output(ret, 
                                                    mainkey="scaling_group"#,listkey={"instance_terminate_policy","is_scaling"}
                                                    ) 
        return ret      
        
    @staticmethod         
    @otcfunc(plugin_name=__name__,
             desc="Describe auto scaling configuration details",
             examples=[],   
             args=[])
    def describe_auto_scaling_configuration():
        url = "https://" + OtcConfig.DEFAULT_HOST + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_configuration"
        ret = utils_http.get(url)
        autoscaling.otcOutputHandler().print_output(ret, mainkey="scaling_configurations" #, subkey="instance_config" 
        , listkey={"scaling_configuration_name","scaling_configuration_id","create_time"#, "instance_config"
                }
                )
        return ret

    @staticmethod       
    @otcfunc(plugin_name=__name__,
             desc="Describe auto scaling configuration details",
             examples=[],
             args = [
                    arg(    '--scaling-configuration-id',     dest='SCALING_CONFIGURATION_ID',     help='scaling-configuration-id'),
                    arg(    '--scaling-configuration-name',     dest='SCALING_CONFIGURATION_NAME',     help='scaling-configuration-name')
                          ])     
    def describe_auto_scaling_configuration_details():
        if not (OtcConfig.SCALING_CONFIGURATION_NAME is None):
            autoscaling.convertASConfigurationNameToId()
        url = "https://" + OtcConfig.DEFAULT_HOST + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_configuration/" + OtcConfig.SCALING_CONFIGURATION_ID
        ret = utils_http.get(url)
        #print(ret)
        autoscaling.otcOutputHandler().print_output(ret, mainkey="scaling_configuration" #, subkey="instance_config" 
        )
        #autoscaling.otcOutputHandler().print_output(ret, mainkey="scaling_configuration", listkey={"scaling_configuration_name",
        #                                                                                            "scaling_configuration_id",
        #                                                                                             "create_time", "instance_config"})
        return ret      
        
    @staticmethod      
    @otcfunc(plugin_name=__name__,
             desc="Describe auto scaling instances",
             examples=[],
             args = [
                    arg(    '--auto-scaling-group-name',    dest='SCALINGGROUP_NAME',     help='Name of Auto Scaling group'),
                    arg(    '--auto-scaling-group-id',    dest='SCALINGGROUP_ID',     help='Id of Auto Scaling group')
                          ]) 
    def describe_auto_scaling_instances():
        if not (OtcConfig.SCALINGGROUP_NAME is None):
            autoscaling.convertASNameToId()            
        url = "https://" + OtcConfig.DEFAULT_HOST + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_group_instance/" + OtcConfig.SCALINGGROUP_ID + "/list"
        ret = utils_http.get(url)
        autoscaling.otcOutputHandler().print_output(ret, mainkey="scaling_group_instances",listkey={"instance_name","instance_id", "scaling_group_name", "life_cycle_state"} )
        return ret

    @staticmethod      
    @otcfunc(plugin_name=__name__,
             desc="Describe policies",
             examples=[],
             args = [
                    arg(    '--auto-scaling-group-name',    dest='SCALINGGROUP_NAME',     help='Name of Auto Scaling group'),
                    arg(    '--auto-scaling-group-id',    dest='SCALINGGROUP_ID',     help='Id of Auto Scaling group')
                          ]) 
    def describe_policies():
        if not (OtcConfig.SCALINGGROUP_NAME is None):
            autoscaling.convertASNameToId()            
        url = "https://" + OtcConfig.DEFAULT_HOST + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_policy/" + OtcConfig.SCALINGGROUP_ID + "/list"  
        ret = utils_http.get(url)
        #print(ret)
        autoscaling.otcOutputHandler().print_output(ret, mainkey="scaling_policies",
                                                                 listkey={"cool_down_time", "scaling_policy_action",
                                                                  "policy_status", "scaling_policy_type", "scheduled_policy", "scaling_policy_name", "scaling_policy_id"})
        return ret


    @staticmethod      
    @otcfunc(plugin_name=__name__,
             desc="Describe activitylog",
             examples=[],
             args = [
                    arg(    '--auto-scaling-group-name',    dest='SCALINGGROUP_NAME',     help='Name of Auto Scaling group'),
                    arg(    '--auto-scaling-group-id',    dest='SCALINGGROUP_ID',     help='Id of Auto Scaling group')
                          ]) 
    def describe_activitylog():
        if not (OtcConfig.SCALINGGROUP_NAME is None):
            autoscaling.convertASNameToId()            
        url = "https://" + OtcConfig.DEFAULT_HOST + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_activity_log/" + OtcConfig.SCALINGGROUP_ID           
        ret = utils_http.get(url)
        
        autoscaling.otcOutputHandler().print_output(ret, mainkey="scaling_activity_log", listkey={"id", "status", "description", "instance_value", "desire_value", "scaling_configuration_name", "scaling_value", "start_time", "end_time", "instance_added_list", "instance_deleted_list", "instance_removed_list"})
        return ret

    @staticmethod        
    @otcfunc(plugin_name=__name__,
             desc="Describe quotas",
             examples=[],
             args = [ ])    
    def describe_quotas():    
        url = "https://" + OtcConfig.DEFAULT_HOST + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/quotas"            
        ret = utils_http.get(url)    
        parsed = json.loads(ret)
        autoscaling.otcOutputHandler().print_output(parsed["quotas"]["resources"], mainkey="", listkey={"type", "used", "quota", "max"})
        return ret

    @staticmethod      
    @otcfunc(plugin_name=__name__,
             desc="Describe quotas of group",
             examples=[],
             args = [
                    arg(    '--auto-scaling-group-name',    dest='SCALINGGROUP_NAME',     help='Name of Auto Scaling group'),
                    arg(    '--auto-scaling-group-id',    dest='SCALINGGROUP_ID',     help='Id of Auto Scaling group')
                          ]) 
    def describe_quotas_of_group():    
        if not (OtcConfig.SCALINGGROUP_NAME is None):
            autoscaling.convertASNameToId()
        url = "https://" + OtcConfig.DEFAULT_HOST + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/quotas/" + OtcConfig.SCALINGGROUP_ID
        ret = utils_http.get(url)    
        parsed = json.loads(ret)
        autoscaling.otcOutputHandler().print_output(parsed["quotas"]["resources"], mainkey="", listkey={"type", "used", "quota", "max"})
        return ret      
              
    @staticmethod       
    @otcfunc(plugin_name=__name__,
             desc="Describe policy details",
             examples=[],
             args = [
                    arg(    '--scaling-policy-name',     dest='SCALING_POLICY_NAME',     help='Specifies the AS policy name. The name can contain letters,digits,underscores(_), and hyphens (-) and cannot exceed 64 characters'),
                    arg(     '--scaling-policy-id',     dest='SCALING_POLICY_ID',     help='scaling-policy-id')
                          ])     
    def describe_policy_details():
        if not (OtcConfig.SCALING_POLICY_NAME is None):
            autoscaling.convertASPolicyNameToId()      
                
        print(OtcConfig.SCALING_POLICY_ID)        
        url = "https://" + OtcConfig.DEFAULT_HOST + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_policy/" + OtcConfig.SCALING_POLICY_ID  
        ret = utils_http.get(url)
        #autoscaling.otcOutputHandler().print_output(ret, mainkey="scaling_policy",                                                     listkey={"scaling_policy_id", "scaling_group_id"})
        autoscaling.otcOutputHandler().print_output(ret,mainkey="")
        return ret


    @staticmethod       
    @otcfunc(plugin_name=__name__,
             desc="Create auto scaling policy",
             examples=[],
             args = [
                    arg(    '--auto-scaling-group-name',    dest='SCALINGGROUP_NAME',     help='Name of Auto Scaling group'),
                    arg(    '--scaling-policy-name',     dest='SCALING_POLICY_NAME',     help='Specifies the AS policy name. The name can contain letters,digits,underscores(_), and hyphens (-) and cannot exceed 64 characters'),
                    arg(     '--scaling-policy-id' ,    dest='SCALING_POLICY_ID'  ,   help='scaling-policy-id'),
                    arg(    '--recurrence-value',     dest='RECURRENCE_VALUE',     help='recurrence-value'),    
                    arg(    '--start-time',     dest='START_TIME',     help='start-time'),    
                    arg(    '--launch-time',     dest='LAUNCH_TIME',     help='launch-time'),    
                    arg(    '--end-time',     dest='END_TIME',     help='end-time'),    
                    arg(    '--recurrence-type',     dest='RECURRENCE_TYPE',     help='recurrence-type'),    

                    arg(    '--scaling-policy-type',     dest='SCALING_POLICY_TYPE',     help='Specifies the AS policy type: ALARM/SCHEDULED/RECURRENCE'),
                    arg(    '--operation-as-policy',     dest='OPERATION_AS_POLICY',     help='Specifies the operation to be performed. The default operation is ADD.ADD: adds instances to the AS group.REMOVE: removes instances from the AS group.SET: sets the number of the instances in the AS group'),
                    arg('--count',    dest='NUMCOUNT',     help='Number of VM will be created'),                
                    arg(    '--cool-down-time',     dest='COOL_DOWN_TIME',     help='cool-down-time')
])
    def create_auto_scaling_policy():
        if not (OtcConfig.SCALINGGROUP_NAME is None):
            autoscaling.convertASNameToId()             
        REQ_CREATE_SCP=utils_templates.create_request("create_as_policy")               
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_policy"
        ret = utils_http.post(url, REQ_CREATE_SCP)
        autoscaling.otcOutputHandler().print_output(ret,mainkey="")
        return ret


    @staticmethod       
    @otcfunc(plugin_name=__name__,
             desc="Modify auto scaling policy",
             examples=[],
             args = [
                    arg(    '--auto-scaling-group-name',    dest='SCALINGGROUP_NAME',     help='Name of Auto Scaling group'),
                    arg(    '--scaling-policy-name',     dest='SCALING_POLICY_NAME',     help='Specifies the AS policy name. The name can contain letters,digits,underscores(_), and hyphens (-) and cannot exceed 64 characters'),
                    arg(     '--scaling-policy-id' ,    dest='SCALING_POLICY_ID' ,    help='scaling-policy-id'),
                    arg(    '--recurrence-value',     dest='RECURRENCE_VALUE',     help='recurrence-value'),    
                    arg(    '--start-time',     dest='START_TIME',     help='start-time'),    
                    arg(    '--launch-time',     dest='LAUNCH_TIME',     help='launch-time'),    
                    arg(    '--end-time',     dest='END_TIME',     help='end-time'),    
                    arg(    '--recurrence-type',     dest='RECURRENCE_TYPE',     help='recurrence-type'),    

                    arg(    '--scaling-policy-type',     dest='SCALING_POLICY_TYPE',     help='Specifies the AS policy type: ALARM/SCHEDULED/RECURRENCE'),
                    arg(    '--operation-as-policy',     dest='OPERATION_AS_POLICY',     help='Specifies the operation to be performed. The default operation is ADD.ADD: adds instances to the AS group.REMOVE: removes instances from the AS group.SET: sets the number of the instances in the AS group'),
                    arg('--count',    dest='NUMCOUNT',     help='Number of VM will be created'),                
                    arg(    '--cool-down-time',     dest='COOL_DOWN_TIME',     help='cool-down-time')
                    ])
    def modify_auto_scaling_policy():
        if not (OtcConfig.SCALINGGROUP_NAME is None):
            autoscaling.convertASNameToId()         
        if not (OtcConfig.SCALING_POLICY_NAME is None):
            autoscaling.convertASPolicyNameToId()         
        
        REQ_CREATE_SCP=utils_templates.create_request("modify_as_policy")               
        #print(REQ_CREATE_SCP)

        url = "https://" + OtcConfig.DEFAULT_HOST+ "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_policy/" + OtcConfig.SCALING_POLICY_ID  
        #print(url)
        ret = utils_http.put(url, REQ_CREATE_SCP)
        autoscaling.otcOutputHandler().print_output(ret,mainkey="")
        return ret



    @staticmethod       
    @otcfunc(plugin_name=__name__,
             desc="Create auto scaling group",
             examples=[],
             args = [

                    arg(    '--scaling-policy-name',     dest='SCALING_POLICY_NAME',     help='Specifies the AS policy name. The name can contain letters,digits,underscores(_), and hyphens (-) and cannot exceed 64 characters'),
                    arg(     '--scaling-policy-id' ,    dest='SCALING_POLICY_ID'  ,   help='scaling-policy-id'),
                    arg(    '--auto-scaling-group-name',    dest='SCALINGGROUP_NAME',     help='Name of Auto Scaling group'),
                    arg(    '--scaling-configuration-id',     dest='SCALING_CONFIGURATION_ID',     help='scaling-configuration-id'),
                    arg(    '--scaling-configuration-name',     dest='SCALING_CONFIGURATION_NAME',     help='scaling-configuration-name'),
                    arg('--count',    dest='NUMCOUNT',     help='Number of VM will be created'), 
                                         arg(    '--cool-down-time',     dest='COOL_DOWN_TIME',     help='cool-down-time'),
                    arg(    '--min-instance-number',     dest='MIN_INSTANCE_NUMBER',     help='min-instance-number'),
                    arg(    '--max-instance-number',     dest='MAX_INSTANCE_NUMBER',     help='max-instance-number'),
                    arg(    '--listener-id',     dest='LISTENER_ID',     help='Listener Id of the VM'),
                    arg(    '--health-periodic-audit-method',     dest='HEALTH_PERIODIC_AUDIT_METHOD',     help='health-periodic-audit-method'),
                    arg(    '--health-periodic-audit-time',     dest='HEALTH_PERIODIC_AUDIT_TIME',     help='health-periodic-audit-time'),
                    arg(    '--instance-terminate-policy',     dest='INSTANCE_TERMINATE_POLICY',     help='instance-terminate-policy'),
                    arg(    '--vpc-id',    dest='VPCID',     help='Id of the VPC will use during VM creation'),    
                    arg(    '--vpc-name',    dest='VPCNAME',     help='Name of the VPC reference will use during VM creation'),
                    arg(  '--subnet-name',    dest='SUBNETNAME',     help='Name of the subnet reference will use during VM creation'),
                    arg(  '--subnet-id',    dest='SUBNETID',     help='Id of the subnet will use during VM creation'),
                    arg(    '--notifications',     dest='NOTIFICATIONS',     help='notifications'),
                    arg(    '--group-names',    dest='SECUGROUPNAME',     help='Name of the security group'),
                    arg(    '--security-group-ids',    dest='SECUGROUP',     help='Id of the security group')
                    ])
    def create_auto_scaling_group():
        if not (OtcConfig.SCALINGGROUP_NAME is None):
            autoscaling.convertASNameToId()
        
        #vpc_id
        if not (OtcConfig.VPCNAME is None):
            getplugin("ecs").convertVPCNameToId()
        #scaling_configuration_id
        if not (OtcConfig.SCALING_CONFIGURATION_NAME is None):
            autoscaling.convertASConfigurationNameToId()
          
        #lb_listener_id
        if not (OtcConfig.LISTENER_NAME is None):
            autoscaling.convertLISTENERNameToId()
        #network_id
        if not OtcConfig.SUBNETNAME is None:
            getplugin("ecs").convertSUBNETNameToId()
        #security_group_id
        if not OtcConfig.SECUGROUPNAME is None:
            getplugin("ecs").convertSECUGROUPNameToId()
        print(OtcConfig.SUBNETID)
        print(OtcConfig.SUBNETID)        
        REQ_CREATE_SCG=utils_templates.create_request("create_as_group")               
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_group"
        ret = utils_http.post(url, REQ_CREATE_SCG)
        autoscaling.otcOutputHandler().print_output(ret,mainkey="")
        #print(REQ_CREATE_SCG)        
        return ret 

    @staticmethod       
    @otcfunc(plugin_name=__name__,
             desc="Create auto scaling group",
             examples=[],
             args = [

                    arg(    '--scaling-policy-name',     dest='SCALING_POLICY_NAME',     help='Specifies the AS policy name. The name can contain letters,digits,underscores(_), and hyphens (-) and cannot exceed 64 characters'),
                    arg(     '--scaling-policy-id',     dest='SCALING_POLICY_ID',     help='scaling-policy-id'),
					arg(    '--auto-scaling-group-name',    dest='SCALINGGROUP_NAME',     help='Name of Auto Scaling group'),
                    arg(    '--scaling-configuration-id',     dest='SCALING_CONFIGURATION_ID',     help='scaling-configuration-id'),
                    arg(    '--scaling-configuration-name',     dest='SCALING_CONFIGURATION_NAME',     help='scaling-configuration-name'),
                    arg('--count',    dest='NUMCOUNT',     help='Number of VM will be created'), 
                    arg(    '--cool-down-time',     dest='COOL_DOWN_TIME',     help='cool-down-time'),                    arg(    '--min-instance-number',     dest='MIN_INSTANCE_NUMBER',     help='min-instance-number'),
                    arg(    '--max-instance-number',     dest='MAX_INSTANCE_NUMBER',     help='max-instance-number'),
                    arg(    '--listener-id',     dest='LISTENER_ID',     help='Listener Id of the VM'),
                    arg(    '--health-periodic-audit-method',     dest='HEALTH_PERIODIC_AUDIT_METHOD',     help='health-periodic-audit-method'),
                    arg(    '--health-periodic-audit-time',     dest='HEALTH_PERIODIC_AUDIT_TIME',     help='health-periodic-audit-time'),
                    arg(    '--instance-terminate-policy',     dest='INSTANCE_TERMINATE_POLICY',     help='instance-terminate-policy'),
                    arg(    '--vpc-id',    dest='VPCID',     help='Id of the VPC will use during VM creation'),    
                    arg(    '--vpc-name',    dest='VPCNAME',     help='Name of the VPC reference will use during VM creation'),
                    arg(  '--subnet-name',    dest='SUBNETNAME',     help='Name of the subnet reference will use during VM creation'),
                    arg(  '--subnet-id',    dest='SUBNETID',     help='Id of the subnet will use during VM creation'),
                    arg(    '--notifications',     dest='NOTIFICATIONS',     help='notifications'),
                    arg(    '--group-names',    dest='SECUGROUPNAME',     help='Name of the security group'),
                    arg(    '--security-group-ids',    dest='SECUGROUP',     help='Id of the security group')
                    ])
    def modify_auto_scaling_group():
        if (OtcConfig.SCALINGGROUP_ID is None) and not (OtcConfig.SCALINGGROUP_NAME is None):
            autoscaling.convertASNameToId()
        #print(SCALINGGROUP_NAME)
        #vpc_id
        if not (OtcConfig.VPCNAME is None):
            getplugin("ecs").convertVPCNameToId()
        #scaling_configuration_id
        if not (OtcConfig.SCALING_CONFIGURATION_NAME is None):
            autoscaling.convertASConfigurationNameToId()
          
        #lb_listener_id
        if not (OtcConfig.LISTENER_NAME is None):
            autoscaling.convertLISTENERNameToId()
        #network_id
        if not OtcConfig.SUBNETNAME is None:
            getplugin("ecs").convertSUBNETNameToId()
        #security_group_id
        if not OtcConfig.SECUGROUPNAME is None:
            getplugin("ecs").convertSECUGROUPNameToId()
        #print(OtcConfig.SECUGROUPNAME)
        #print(OtcConfig.SECUGROUP)        
        REQ_CREATE_SCG=utils_templates.create_request("modify_as_group")               
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_group/"+ OtcConfig.SCALINGGROUP_ID
        ret = utils_http.put(url, REQ_CREATE_SCG)
        autoscaling.otcOutputHandler().print_output(ret,mainkey="")
        #print(REQ_CREATE_SCG)        
        return ret 

    @staticmethod       
    @otcfunc(plugin_name=__name__,
             desc="Enable auto scaling policy",
             examples=[],
             args = [

                    arg(    '--scaling-policy-name',     dest='SCALING_POLICY_NAME',     help='Specifies the AS policy name. The name can contain letters,digits,underscores(_), and hyphens (-) and cannot exceed 64 characters'),
                    arg(     '--scaling-policy-id' ,    dest='SCALING_POLICY_ID'   ,  help='scaling-policy-id')
                    ])
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
    @otcfunc(plugin_name=__name__,
             desc="Disable auto scaling policy",
             examples=[],
             args = [

                    arg(    '--scaling-policy-name',     dest='SCALING_POLICY_NAME',     help='Specifies the AS policy name. The name can contain letters,digits,underscores(_), and hyphens (-) and cannot exceed 64 characters'),
                    arg(     '--scaling-policy-id' ,    dest='SCALING_POLICY_ID' ,    help='scaling-policy-id')
                    ])
    def disable_auto_scaling_policy():
        if not (OtcConfig.SCALING_POLICY_NAME is None):
            autoscaling.convertASPolicyNameToId()      
        print(OtcConfig.SCALING_POLICY_ID)    
        OtcConfig.AS_POLICY_ACTION="pause"
        REQ_ACTION_SCP=utils_templates.create_request("execute_enable_disable_as_policy")
        url = "https://" + OtcConfig.DEFAULT_HOST + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_policy/" + OtcConfig.SCALING_POLICY_ID  + "/action" 
        ret = utils_http.post(url, REQ_ACTION_SCP)
        autoscaling.otcOutputHandler().print_output(ret,mainkey="")
        return ret       
    
    @staticmethod       
    @otcfunc(plugin_name=__name__,
             desc="Execute auto scaling policy",
             examples=[],
             args = [

                    arg(    '--scaling-policy-name',     dest='SCALING_POLICY_NAME',     help='Specifies the AS policy name. The name can contain letters,digits,underscores(_), and hyphens (-) and cannot exceed 64 characters'),
                    arg(     '--scaling-policy-id',     dest='SCALING_POLICY_ID' ,    help='scaling-policy-id')
                    ])
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
    @otcfunc(plugin_name=__name__,
             desc="Enable auto scaling group",
             examples=[],
             args = [
                    arg(    '--auto-scaling-group-name',    dest='SCALINGGROUP_NAME',     help='Name of Auto Scaling group'),
                    arg(    '--auto-scaling-group-id',    dest='SCALINGGROUP_ID',     help='Id of Auto Scaling group')
                          ]) 
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
    @otcfunc(plugin_name=__name__,
             desc="Disable auto scaling group",
             examples=[],
             args = [
                    arg(    '--auto-scaling-group-name',    dest='SCALINGGROUP_NAME',     help='Name of Auto Scaling group'),
                    arg(    '--auto-scaling-group-id',    dest='SCALINGGROUP_ID',     help='Id of Auto Scaling group')
                          ]) 
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
    @otcfunc(plugin_name=__name__,
            desc="Deletes auto scaling instance from group",
            examples=[],
            args = [ 
                     arg(    '--instance-name',     dest='INSTANCE_NAME',     help='Instance name of the VM'),
               ])    
    def delete_auto_scaling_instance_from_group():
        if not OtcConfig.INSTANCE_NAME is None:
            getplugin("ecs").convertINSTANCENameToId()            
        url = "https://" + OtcConfig.DEFAULT_HOST + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_group_instance/" + OtcConfig.INSTANCE_ID 
        ret = utils_http.delete(url)
        print(ret)
        return ret

        
    @staticmethod       

    @otcfunc(plugin_name=__name__,
             desc="Batch delete auto scaling configuration",
             examples=[],
             args = [
                    arg(    '--scaling-configuration-id',     dest='SCALING_CONFIGURATION_ID',     help='scaling-configuration-id'),
                    arg(    '--scaling-configuration-name',     dest='SCALING_CONFIGURATION_NAME',     help='scaling-configuration-name')
                    ])
    def batch_delete_auto_scaling_configuration():
        if (OtcConfig.SCALING_CONFIGURATION_ID is None) and not (OtcConfig.SCALING_CONFIGURATION_NAME is None):
            autoscaling.convertASConfigurationNameToId()

        REQ_DELETE_BATCH_SC=utils_templates.create_request("batch_delete_AS_config")                
        url = "https://" + OtcConfig.DEFAULT_HOST + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_configurations"
        ret = utils_http.post(url, REQ_DELETE_BATCH_SC)
        autoscaling.otcOutputHandler().print_output(ret,mainkey="")
        #print(REQ_DELETE_BATCH_SC)
        return ret


    @staticmethod      
    @otcfunc(plugin_name=__name__,
             desc="Batch delete auto scaling instances",
             examples=[],
             args = [
                    arg(    '--auto-scaling-group-name',    dest='SCALINGGROUP_NAME',     help='Name of Auto Scaling group'),
                    arg(    '--auto-scaling-group-id',    dest='SCALINGGROUP_ID',     help='Id of Auto Scaling group'),
                    arg(    '--instance-name',     dest='INSTANCE_NAME',     help='Instance name of the VM'),     
                    arg(    '--instance-action-add-remove-batch',     dest='INSTANCE_ACTION_ADD_REMOVE_BATCH',     help='instance-action-add-remove-batch'),
                    arg(    '--instance-ids',     dest='INSTANCE_ID',     help='Instance Id of the VM'),
                    arg(    '--instance-delete',     dest='INSTANCE_DELETE',     help='instance-delete'),
               ])      
    def batch_add_delete_auto_scaling_instances():
        if not (OtcConfig.SCALINGGROUP_NAME is None):
            autoscaling.convertASNameToId()  
        
        if (OtcConfig.INSTANCE_ID is None) and not OtcConfig.INSTANCE_NAME is None:
            getplugin("ecs").convertINSTANCENameToId()             

        REQ_BATCH_INST=utils_templates.create_request("batch_remove_add_instance")        

        url = "https://" + OtcConfig.DEFAULT_HOST + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_group_instance/"+ OtcConfig.SCALINGGROUP_ID +"/action"
        ret = utils_http.post(url, REQ_BATCH_INST)
        #print(REQ_BATCH_INST)
        autoscaling.otcOutputHandler().print_output(ret,mainkey="")
        return ret          

        
    @staticmethod
    def create_launch_configuration():
        raise RuntimeError("NOT IMPLEMENTED!")

    @staticmethod            
    @otcfunc(plugin_name=__name__,
             desc="Delete policies",
             examples=[],
             args = [

                    arg(    '--scaling-policy-name',     dest='SCALING_POLICY_NAME',     help='Specifies the AS policy name. The name can contain letters,digits,underscores(_), and hyphens (-) and cannot exceed 64 characters'),
                    arg(     '--scaling-policy-id',     dest='SCALING_POLICY_ID' ,    help='scaling-policy-id')
                    ])
    def delete_policies():
        if not (OtcConfig.SCALING_POLICY_NAME is None):
            autoscaling.convertASPolicyNameToId()
        url = "https://" + OtcConfig.DEFAULT_HOST + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_policy/" + OtcConfig.SCALING_POLICY_ID
        ret = utils_http.delete(url)
        print(ret)
        return ret

    @staticmethod            
    @otcfunc(plugin_name=__name__,
             desc="Delete auto scaling configuration",
             examples=[],
             args = [
                    arg(    '--scaling-configuration-id',     dest='SCALING_CONFIGURATION_ID',     help='scaling-configuration-id'),
                    arg(    '--scaling-configuration-name',     dest='SCALING_CONFIGURATION_NAME',     help='scaling-configuration-name')
                    ])
    def delete_auto_scaling_configuration():
        if not (OtcConfig.SCALING_CONFIGURATION_NAME is None):
            autoscaling.convertASConfigurationNameToId()
        url = "https://" + OtcConfig.DEFAULT_HOST + "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_configuration/"+ OtcConfig.SCALING_CONFIGURATION_ID
        ret = utils_http.delete(url)
        print(ret)
        return ret

    @staticmethod            
    @otcfunc(plugin_name=__name__,
             desc="Delete auto scaling configuration",
             examples=[],
             args = [
                    arg(    '--scaling-configuration-id',     dest='SCALING_CONFIGURATION_ID',     help='scaling-configuration-id'),
                    arg(    '--scaling-configuration-name',     dest='SCALING_CONFIGURATION_NAME',     help='scaling-configuration-name'),
                    arg(    '--image-name',    dest='IMAGENAME',     help='Name of the image reference will used during VM creation'),
                    arg(    '--image-id',    dest='IMAGE_ID',     help='Id of the image reference will use during VM creation'),
                    arg(    '--instance-type',    dest='INSTANCE_TYPE_NAME',     help='Flavor type of the VM'),
                    arg(    '--size',    dest='VOLUME_SIZE',     help='Size of the EVS disk'),        
                    arg(    '--volume-type',    dest='VOLUME_TYPE',     help='Volume type of the EVS disk [SSD SAS SATA]'),
                    arg(    '--disk-type',     dest='DISK_TYPE',     help='disk-type'),
                    arg(    '--key-name',     dest='KEYNAME',     help='SSH key name| S3 Object key')
                    ])
    def create_auto_scaling_configuration():
        if not OtcConfig.INSTANCE_TYPE_NAME is None:
            getplugin("ecs").convertFlavorNameToId()
        if not OtcConfig.IMAGENAME is None:
            getplugin("ecs").convertIMAGENameToId()
        REQ_CREATE_SC=utils_templates.create_request("create_as_configuration")     
        #print(REQ_CREATE_SC)
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/autoscaling-api/v1/" + OtcConfig.PROJECT_ID + "/scaling_configuration"
        ret = utils_http.post(url, REQ_CREATE_SC)
        autoscaling.otcOutputHandler().print_output(ret,mainkey="")
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
    
