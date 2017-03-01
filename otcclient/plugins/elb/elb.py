#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of OTC Tool released under MIT license.
# Copyright (C) 2016 T-systems Kurt Garloff, Zsolt Nagy

from otcclient.core.OtcConfig import OtcConfig 
from otcclient.utils import utils_http
from otcclient.utils import utils_templates

from otcclient.core.otcpluginbase import otcpluginbase
from otcclient.core.pluginmanager import getplugin
import json
import os
from otcclient.core.argmanager import arg, otcfunc 
    
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
    @otcfunc(plugin_name=__name__,
         desc="Delete loadbalancers",
         args = [
            arg(    '--load-balancer-name',     dest='LOADBALANCER_NAME',     help='Loadbalancer name of the VM'),
            arg(    '--load-balancer-id',     dest='LOADBALANCER_ID',     help='Loadbalancer Id of the VM') ]
         ) 
    def delete_load_balancers():        
        if not (OtcConfig.LOADBALANCER_NAME is None):
            elb.convertELBNameToId()            
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1.0/" + OtcConfig.PROJECT_ID + "/elbaas/loadbalancers" + "/" + OtcConfig.LOADBALANCER_ID

        ret = utils_http.delete(url)
        print(ret)
        return ret

    @staticmethod
    @otcfunc(plugin_name=__name__,
         desc="Describe listeners",
         args = [
            arg(    '--load-balancer-name',     dest='LOADBALANCER_NAME',     help='Loadbalancer name of the VM'),
            arg(    '--load-balancer-id',     dest='LOADBALANCER_ID',     help='Loadbalancer Id of the VM') ]
         )
    def describe_listeners():
        if not (OtcConfig.LOADBALANCER_NAME is None):
            elb.convertELBNameToId()
    
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1.0/" + OtcConfig.PROJECT_ID + "/elbaas/listeners" + "?loadbalancer_id=" + OtcConfig.LOADBALANCER_ID
        ret = utils_http.get(url)
        #mod =  ret.replace("[","").replace("]","")        
        print (json.dumps(json.loads(ret), indent=4, sort_keys=True))
        #elb.otcOutputHandler().print_output(ret,mainkey="")
        return ret

    @staticmethod
    @otcfunc(plugin_name=__name__,
         desc="Describe listeners",
         args = [
            arg(    '--load-balancer-name',     dest='LOADBALANCER_NAME',     help='Loadbalancer name of the VM'),
            arg(    '--load-balancer-id',     dest='LOADBALANCER_ID',     help='Loadbalancer Id of the VM') ]
         )
    def describe_members():
        if not (OtcConfig.LISTENER_NAME is None):
            elb.convertLISTENERNameToId()

        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1.0/" + OtcConfig.PROJECT_ID + "/elbaas/listeners/" + OtcConfig.LISTENER_ID + "/members"       
               
        ret = utils_http.get(url)
        mod =  "{ \"members\": " + ret + " }" 
    
        
        elb.otcOutputHandler().print_output(mod, mainkey="members", listkey={"server_address","server_id","server_name","update_time","create_time","id","name","status","health_status","address" } )
        return ret


    @staticmethod
    @otcfunc(plugin_name=__name__,
         desc="Describe health check",
         args = [
            arg(    '--healthcheck-id',     dest='HEALTHCHECK_ID',     help='healthcheck-id'),
            arg(    '--load-balancer-name',     dest='LOADBALANCER_NAME',     help='Loadbalancer name of the VM'),
            arg(    '--load-balancer-id',     dest='LOADBALANCER_ID',     help='Loadbalancer Id of the VM') ]
         )
    def describe_health_check():
        if not (OtcConfig.LOADBALANCER_NAME is None):
            elb.convertELBNameToId()
        
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1.0/" + OtcConfig.PROJECT_ID + "/elbaas/healthcheck/" + OtcConfig.HEALTHCHECK_ID        
               
        ret = utils_http.get(url)
        
        elb.otcOutputHandler().print_output(ret,mainkey="")
        return ret



    @staticmethod
    @otcfunc(plugin_name=__name__,
         desc="Describe health check",
         args = [
            arg(    '--load-balancer-name',     dest='LOADBALANCER_NAME',     help='Loadbalancer name of the VM'),
            arg(    '--load-balancer-id',     dest='LOADBALANCER_ID',     help='Loadbalancer Id of the VM') ]
         )
    def describe_load_balancers():
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1.0/" + OtcConfig.PROJECT_ID + "/elbaas/loadbalancers"        
        if not (OtcConfig.LOADBALANCER_NAME is None):
            elb.convertELBNameToId()
        
        if OtcConfig.LOADBALANCER_ID:
            url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1.0/" + OtcConfig.PROJECT_ID + "/elbaas/loadbalancers" + "/" + OtcConfig.LOADBALANCER_ID
            ret = utils_http.get(url)                       
            elb.otcOutputHandler().print_output(ret,mainkey="")
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
    def convertLISTENERIdToHealthCheckId():
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1.0/" + OtcConfig.PROJECT_ID + "/elbaas/listeners/" + OtcConfig.LISTENER_ID
    
        JSON = utils_http.get(url)
        parsed  = json.loads(JSON)
        OtcConfig.HEALTHCHECK_ID = parsed["healthcheck_id"]
        ret = OtcConfig.HEALTHCHECK_ID
        return ret   

    @staticmethod
    @otcfunc(plugin_name=__name__,
         desc="Create load balancers",
         args = [
            arg(    '--vpc-name',    dest='VPCNAME',     help='Name of the VPC reference will use during VM creation'),
            arg(    '--vpc-id',    dest='VPCID',     help='Id of the VPC will use during VM creation'),
            arg(    '--description',    dest='DESCRIPTION',     help='Description definition ( eg: backups)'),
            arg('--bandwidth', dest='BANDWIDTH', help='bandwidth'),      
            arg(    '--healthcheck-id',     dest='HEALTHCHECK_ID',     help='healthcheck-id'),
            arg(    '--load-balancer-name',     dest='LOADBALANCER_NAME',     help='Loadbalancer name of the VM')
            ]
         ) 
    def create_load_balancers():
        if not (OtcConfig.LOADBALANCER_NAME is None):
            elb.convertELBNameToId()
        if not (OtcConfig.VPCNAME is None):
            getplugin("ecs").convertVPCNameToId()        
        REQ_CREATE_ELB=utils_templates.create_request("create_loadbalancer")
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1.0/" + OtcConfig.PROJECT_ID + "/elbaas/loadbalancers"
        ret = utils_http.post(url, REQ_CREATE_ELB)
                 
        maindata = json.loads(ret)
        if "code" in  maindata:            
            print("Can not create:" +maindata["message"])  
            os._exit( 1 )             
        print("created")        
        return ret



    @staticmethod  
    @otcfunc(plugin_name=__name__,
         desc="Create listener",
         args = [
                    arg(    '--listener-name',     dest='LISTENER_NAME',     help='Listener name of the VM'),
					arg('--listener-description',     dest='LISTENER_DESCRIPTION',     help='listener-description'),
                    arg('--listener-port',     dest='LISTENER_PORT',     help='listener-port'),
                    arg('--backend-port',     dest='BACKEND_PORT',     help='backend-port'),
                    arg(    '--lb-algorithm',     dest='LB_ALGORITHM',     help='lb-algorithm'),               
                    arg(    '--protocol',    dest='PROTOCOL',     help='Protocol of the specific security group rule'),
                    arg(    '--portmin',    dest='PORTMIN',     help='Lower por of the specific security group rule'),
                    arg( '--listener-description', dest='LISTENER_DESCRIPTION', help='listener-description'),
                    arg( '--session-sticky', dest='SESSION_STICKY', help='Specifies whether to enable the session persistence function.The value is true or false. The session persistence function is enabled when the value is true, and is disabled when the value is false.'),
                    arg( '--sticky-session-type', dest='STICKY_SESSION_TYPE', help='Specifies the cookie processing method. The value is insert.insert indicates that the cookie is inserted by the load balancer. This parameter is valid when protocol is set to HTTP, and session_sticky to true. The default value is insert. This parameter is invalid when protocol is set to TCP. That means the parameter is empty.'),
                    arg( '--cookie-timeout', dest='COOKIE_TIMEOUT', help='Specifies the cookie timeout period (s).The value ranges from 1 to 86,400. This parameter is valid when protocol is set to HTTP, session_sticky to true, and sticky_session_type to insert. This parameter is invalid when protocol is set to TCP.')   
                    ]
         )
    def create_listener():
        
        if not (OtcConfig.LOADBALANCER_NAME is None):
            elb.convertELBNameToId()
        if not (OtcConfig.VPCNAME is None):
            getplugin("ecs").convertVPCNameToId()                
        
        REQ_CREATE_LISTENER=utils_templates.create_request("create_listener")        
        print (REQ_CREATE_LISTENER)       
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1.0/" + OtcConfig.PROJECT_ID + "/elbaas/listeners"
        ret = utils_http.post(url, REQ_CREATE_LISTENER)        
        maindata = json.loads(ret)
        if "code" in  maindata:            
            print("Can not create:" +maindata["message"])  
            os._exit( 1 )             
        elb.otcOutputHandler().print_output(ret,mainkey="")
        print( ret )
        #ecs.otcOutputHandler().print_output(ret, mainkey="loadbalancer")
        return ret

    @staticmethod 
    @otcfunc(plugin_name=__name__,
             desc="Describe quotas",
             examples=[ ],
             args = [ ])  
    def describe_quotas():
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1.0/" + OtcConfig.PROJECT_ID + "/elbaas/quotas"                           
        ret = utils_http.get(url)
        print( ret )
        elb.otcOutputHandler().print_output(ret,mainkey="")
        return ret

#     @staticmethod
#     def describe_members():
#         if not (OtcConfig.LISTENER_NAME is None):
#             elb.convertLISTENERNameToId()
# 
#         url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1.0/" + OtcConfig.PROJECT_ID + "/elbaas/listeners/" + OtcConfig.LISTENER_ID + "/members"       
#                
#         ret = utils_http.get(url)
#         mod =  "{ \"members\": " + ret + " }" 
#     
#         
#         elb.otcOutputHandler().print_output(mod, mainkey="members", listkey={"server_address","server_id","server_name","update_time","create_time","id","name","status","health_status","address" } )
#         return ret

    @staticmethod 
    @otcfunc(plugin_name=__name__,
             desc="Create backend member",
             examples=[ ],
             args = [ 
                       arg(    '--instance-name',     dest='INSTANCE_NAME',     help='Instance name of the VM'),
                       arg(    '--listener-name',     dest='LISTENER_NAME',     help='Listener name of the VM'),
                       arg(    '--address',     dest='ADDRESS',     help='Specifies the private IP address of the backend member')
                ])    
    def create_backend_member():
        if not (OtcConfig.LISTENER_NAME is None):
            elb.convertLISTENERNameToId()
        if not OtcConfig.INSTANCE_NAME is None:
            getplugin("ecs").convertINSTANCENameToId() 
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1.0/" + OtcConfig.PROJECT_ID + "/elbaas/listeners/" + OtcConfig.LISTENER_ID + "/members"       
        REQ_CREATE_BACKEND_MEMBER = utils_templates.create_request("add_backend_member")           
        ret = utils_http.post(url, REQ_CREATE_BACKEND_MEMBER)    
        print(ret)
        return ret        
    
    @staticmethod 
    @otcfunc(plugin_name=__name__,
             desc="Delete backend member",
             examples=[],
             args = [ 
                       arg(    '--instance-name',     dest='INSTANCE_NAME',     help='Instance name of the VM'),
                       arg(    '--listener-name',     dest='LISTENER_NAME',     help='Listener name of the VM')
                ])    
    def delete_backend_member():
        if not (OtcConfig.LISTENER_NAME is None):
            elb.convertLISTENERNameToId()
        if not OtcConfig.INSTANCE_NAME is None:
            getplugin("ecs").convertINSTANCENameToId() 


        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1.0/" + OtcConfig.PROJECT_ID + "/elbaas/listeners/" + OtcConfig.LISTENER_ID + "/members/action"       

        REQ_DELETE_BACKEND_MEMBER=utils_templates.create_request("delete_backend_member")        
   
        ret = utils_http.post(url, REQ_DELETE_BACKEND_MEMBER)

        print(ret)
        return ret            

    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="Create health check",
             examples=[],
             args = [ 
                        arg(    '--listener-name',     dest='LISTENER_NAME',     help='Listener name of the VM'),
                        arg('--healthcheck-connect-port',dest='HEALTHCHECK_CONNECT_PORT',help='Specifies the port for health check'),
                        arg(    '--healthcheck-interval',     dest='HEALTHCHECK_INTERVAL',     help='Specifies the maximum interval for health check.The value ranges from 1 to 5(s)'),
                        arg(    '--healthcheck-protocol',     dest='HEALTHCHECK_PROTOCOL',     help='Specifies the health check protocol.The value can be HTTP or TCP (case-insensitive)'),
                        arg(    '--healthcheck-timeout',     dest='HEALTHCHECK_TIMEOUT',     help='Specifies the maximum timeout duration for health check. The value ranges from 1 to 50 (s)'),
                        arg(    '--healthcheck-uri',     dest='HEALTHCHECK_URI',     help='Specifies the URI for health check. The value is a string of 1 to 80 characters that contain only letters'),
                        arg(    '--healthy-threahold',     dest='HEALTHY_THREAHOLD',     help='Specifies the number of consecutive successful health checks for the health check result changing from fail to success. The value ranges from 1 to 10.'),        
                        arg(    '--unhealthy-threshold',     dest='UNHEALTHY_THRESHOLD',     help='Specifies the number of consecutive successful health checks for the health check result changing from success to fail. The value ranges from 1 to 10.')             
                ])      
    def create_health_check():
        if not (OtcConfig.LISTENER_NAME is None):
            elb.convertLISTENERNameToId()
        
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1.0/" + OtcConfig.PROJECT_ID + "/elbaas/healthcheck"       

        REQ_CREATE_HEALTH_CHECK=utils_templates.create_request("creating_health_check_task")        
   
        ret = utils_http.post(url, REQ_CREATE_HEALTH_CHECK)
        return ret


    @staticmethod    
    @otcfunc(plugin_name=__name__,
             desc="Create health check",
             examples=[],
             args = [ 
                        arg(    '--listener-name',     dest='LISTENER_NAME',     help='Listener name of the VM'),
                        arg(    '--healthcheck-connect-port',     dest='HEALTHCHECK_CONNECT_PORT',     help='Specifies the port for health check'),
                        arg(    '--healthcheck-interval',     dest='HEALTHCHECK_INTERVAL',     help='Specifies the maximum interval for health check.The value ranges from 1 to 5(s)'),
                        arg(    '--healthcheck-protocol',     dest='HEALTHCHECK_PROTOCOL',     help='Specifies the health check protocol.The value can be HTTP or TCP (case-insensitive)'),
                        arg(    '--healthcheck-timeout',     dest='HEALTHCHECK_TIMEOUT',     help='Specifies the maximum timeout duration for health check. The value ranges from 1 to 50 (s)'),
                        arg(    '--healthcheck-uri',     dest='HEALTHCHECK_URI',     help='Specifies the URI for health check. The value is a string of 1 to 80 characters that contain only letters'),
                        arg(    '--healthy-threahold',     dest='HEALTHY_THREAHOLD',     help='Specifies the number of consecutive successful health checks for the health check result changing from fail to success. The value ranges from 1 to 10.'),        
                        arg(    '--unhealthy-threshold',     dest='UNHEALTHY_THRESHOLD',     help='Specifies the number of consecutive successful health checks for the health check result changing from success to fail. The value ranges from 1 to 10.')             
                ])
    def modify_health_check():
        if not (OtcConfig.LOADBALANCER_NAME is None):
            elb.convertELBNameToId()
        if not (OtcConfig.HEALTHCHECK_ID is None):
            elb.convertLISTENERIdToHealthCheckId()
        
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1.0/" + OtcConfig.PROJECT_ID + "/elbaas/healthcheck/"  + OtcConfig.HEALTHCHECK_ID              

        REQ_MODIFY_HEALTH_CHECK=utils_templates.create_request("modify_information_health_check_task")        
   
        ret = utils_http.put(url, REQ_MODIFY_HEALTH_CHECK)
        print(ret)
        return ret

    @staticmethod
    @otcfunc(plugin_name=__name__,
         desc="Modify load balancers",
         args = [
            arg(    '--vpc-name',    dest='VPCNAME',     help='Name of the VPC reference will use during VM creation'),
            arg(    '--vpc-id',    dest='VPCID',     help='Id of the VPC will use during VM creation'),
            arg('--bandwidth', dest='BANDWIDTH', help='bandwidth'),      
            arg(    '--listener-description',     dest='LISTENER_DESCRIPTION',     help='listener-description'),
            arg(    '--load-balancer-name',     dest='LOADBALANCER_NAME',     help='Loadbalancer name of the VM')
            ]
         )
    def modify_load_balancers():
        if not (OtcConfig.LOADBALANCER_NAME is None):
            elb.convertELBNameToId()
        if not (OtcConfig.VPCNAME is None):
            getplugin("ecs").convertVPCNameToId()        
                 
        REQ_MODIFY_ELB=utils_templates.create_request("modify_load_balancer")        
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1.0/" + OtcConfig.PROJECT_ID + "/elbaas/loadbalancers/" + OtcConfig.LOADBALANCER_ID
        print (REQ_MODIFY_ELB)
        ret = utils_http.put(url, REQ_MODIFY_ELB)
        print(ret)         
        maindata = json.loads(ret)
        if "code" in  maindata:            
            print("Can not modify:" +maindata["message"])  
            os._exit( 1 )             
        print("created")        
        return ret

    @staticmethod 
    @otcfunc(plugin_name=__name__,
         desc="Modify listener",
         args = [
                    arg(    '--listener-name',     dest='LISTENER_NAME',     help='Listener name of the VM'),
                    arg('--listener-description',     dest='LISTENER_DESCRIPTION',     help='listener-description'),
                    arg('--listener-port',     dest='LISTENER_PORT',     help='listener-port'),
                    arg('--backend-port',     dest='BACKEND_PORT',     help='backend-port'),
                    arg(    '--lb-algorithm',     dest='LB_ALGORITHM',     help='lb-algorithm')                   ]
         )
    def modify_listeners():
        #if not (OtcConfig.LOADBALANCER_NAME is None):
        #    elb.convertELBNameToId()
        #if not (OtcConfig.VPCNAME is None):
        #    getplugin("ecs").convertVPCNameToId()                
        if not (OtcConfig.LISTENER_NAME is None):
            elb.convertLISTENERNameToId()
        
        #REQ_CREATE_LISTENER = "{ \"name\":\"listener1\", \"description\":\"\", \"loadbalancer_id\":\"0b07acf06d243925bc24a0ac7445267a\", \"protocol\":\"HTTP\", \"port\":88, \"backend_protocol\":\"HTTP\", \"backend_port\":80, \"lb_algorithm\":\"roundrobin\", \"session_sticky\":true, \"sticky_session_type\":\"insert\", \"cookie_timeout\":100 }"         
        REQ_MODIFY_LISTENER=utils_templates.create_request("modify_information_listener")               
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1.0/" + OtcConfig.PROJECT_ID + "/elbaas/listeners/"+ OtcConfig.LISTENER_ID
        ret = utils_http.put(url, REQ_MODIFY_LISTENER)
        print( ret )
        maindata = json.loads(ret)
        if "code" in  maindata:            
            print("Can not create:" +maindata["message"])  
            os._exit( 1 )              
        
        print( ret )
        #ecs.otcOutputHandler().print_output(ret, mainkey="loadbalancer")
        return ret        

    @staticmethod
    @otcfunc(plugin_name=__name__,
         desc="Delete listener",
         args = [
                    arg(    '--listener-name',     dest='LISTENER_NAME',     help='Listener name of the VM')
                   ]
         )
    def delete_listener():
        if not (OtcConfig.LISTENER_NAME is None):
            elb.convertLISTENERNameToId()
    
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1.0/" + OtcConfig.PROJECT_ID + "/elbaas/listeners/" + OtcConfig.LISTENER_ID
        ret = utils_http.delete(url)

        print(ret)
        return ret

    @staticmethod
    @otcfunc(plugin_name=__name__,
         desc="Delete health check",
         args = [
            arg(    '--healthcheck-id',     dest='HEALTHCHECK_ID',     help='healthcheck-id'),
            arg(    '--load-balancer-name',     dest='LOADBALANCER_NAME',     help='Loadbalancer name of the VM'),
            arg(    '--load-balancer-id',     dest='LOADBALANCER_ID',     help='Loadbalancer Id of the VM') ]
         )
    def delete_health_check():
        if not (OtcConfig.LOADBALANCER_NAME is None):
            elb.convertELBNameToId()
        if not (OtcConfig.HEALTHCHECK_ID is None):
            elb.convertLISTENERIdToHealthCheckId()

        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1.0/" + OtcConfig.PROJECT_ID + "/elbaas/healthcheck/" + OtcConfig.HEALTHCHECK_ID        
        ret = utils_http.delete(url)

        print(ret)
        return ret
