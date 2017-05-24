#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of OTC Tool released under MIT license.
# Copyright (C) 2016 T-systems Kurt Garloff, Zsolt Nagy

from otcclient.core.OtcConfig import OtcConfig 
from otcclient.utils import utils_http
from otcclient.utils import utils_http, utils_templates

from otcclient.core.otcpluginbase import otcpluginbase
from otcclient.core.pluginmanager import getplugin
import base64
from time import sleep
import sys
import json
import os
from otcclient.core.argmanager import arg, otcfunc

 
    
class dcs(otcpluginbase):
    ar = {}    
    
    @staticmethod
    def otcOutputHandler(): 
        return getplugin(OtcConfig.OUTPUT_FORMAT)
 
    def otctype(self):
        return "func" 

    # url = "https://" + OtcConfig.DEFAULT_HOST+ "/v2/" + OtcConfig.PROJECT_ID + "/os-availability-zone/detail"

    @staticmethod 
    @otcfunc(plugin_name=__name__,
             desc="List instances",
             examples=[
                       {'List instances":"otc dcs list_instances'},
                       {'Information about all DCS instances (JSON): otc dcs list_instances --output json '}
                       ],
             args = [ 
                ])    
    def list_instances():
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.0/" + OtcConfig.PROJECT_ID +  "/instances"    
        ret = utils_http.get(url)
        #print (url)
        #print (ret)        
        dcs.otcOutputHandler().print_output(ret, mainkey = "instances", listkey={"instance_id", "name", "capacity","ip","port","used_memory","max_memory","resource_spec_code","engine_version","status","created_at"})
        
        return ret

    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="Describe instance",
             examples=[
                       {'Describe instances":"otc dcs describe_instances'},
                       {'Detailed information about a specific DCS instance (JSON): otc dcs describe_instances --instance-ids 097da903-ab95-44f3-bb5d-5fc08dfb6cc3 --output json '}
                       ],
             args = [ 
                       arg(    '--instance-ids',     dest='INSTANCE_ID',     help='Instance ID of the VM')
                ])    
    def describe_instance():
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.0/" + OtcConfig.PROJECT_ID +  "/instances"
        ret = utils_http.get(url + '/' + OtcConfig.INSTANCE_ID )
        #print (url)
        #print (ret)        
        dcs.otcOutputHandler().print_output(ret, mainkey = "")
        
        return ret

    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="Create instance",
             examples=[
                       {'Create instances":"otc dcs create_instance'},
                       {'Create a DCS instance (JSON): otc dcs create_instance --instance-name Test-MS --instance-type OTC_DCS_MS:2 --description Test --admin-pass Test1234 --vpc-name vpc-adc-docker  --group-names DCS --subnet-name subnet-az1-110 '}
                       ],
             args = [ 
                       arg(    '--instance-name',     dest='INSTANCE_NAME',          help='Name of the DCS instance'),
                       arg(    '--instance-type',     dest='INSTANCE_TYPE_NAME',     help='DCS Instance Type:Memory Size'),
                       arg(    '--description',       dest='DESCRIPTION',            help='DCS Instance Description'),
                       arg(    '--admin-pass',        dest='ADMINPASS',              help='DCS Instance Admin Password'),
                       arg(    '--vpc-name',          dest='VPCNAME',                help='VPC name'),
                       arg(    '--group-names',       dest='SECUGROUPNAME',          help='Security Group name'),
                       arg(    '--subnet-name',       dest='SUBNETNAME',             help='Subnet name')
                ])    
    def create_instance():
        if not OtcConfig.VPCNAME is None:
            getplugin("ecs").convertVPCNameToId()
        if not OtcConfig.SUBNETNAME is None:
            getplugin("ecs").convertSUBNETNameToId()
        if not OtcConfig.SECUGROUPNAME is None:
            getplugin("ecs").convertSECUGROUPNameToId()
        if not OtcConfig.AZ is None:
            dcs.convertAZnameToId()
        if OtcConfig.INSTANCE_TYPE_NAME is None:
            OtcConfig.INSTANCE_TYPE_NAME = "OTC_DCS_SINGLE:1"
        if OtcConfig.INSTANCE_NAME is None:
           OtcConfig.INSTANCE_NAME = "dcs"

	(OtcConfig.INSTANCE_DCS_TYPE,OtcConfig.INSTANCE_DCS_SIZE) = OtcConfig.INSTANCE_TYPE_NAME.split(':')
        REQ_CREATE_DCS=utils_templates.create_request("create_instance")
        print (REQ_CREATE_DCS)
        
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.0/" + OtcConfig.PROJECT_ID +  "/instances"
        #print (url)
        ret = utils_http.post(url, REQ_CREATE_DCS )

        print (ret)

        return ret

    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="Delete instance",
             examples=[
                       {'Delete instances":"otc dcs delete_instances'},
                       {'Delete a specific DCS instance: otc dcs delete_instance --instance-ids 097da903-ab95-44f3-bb5d-5fc08dfb6cc3 '}
                       ],
             args = [ 
                       arg(    '--instance-ids',     dest='INSTANCE_ID',     help='Instance ID of the DCS instance')
                ])    
    def delete_instance():
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.0/" + OtcConfig.PROJECT_ID +  "/instances"
        ret = utils_http.delete(url + '/' + OtcConfig.INSTANCE_ID )
        #print (url)
        #print (ret)        
        dcs.otcOutputHandler().print_output(ret, mainkey = "")
        
        return ret

    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="Stop instance",
             examples=[
                       {'Stop instance":"otc dcs stop_instance'},
                       {'Stop a specific DCS instance: otc dcs stop_instance --instance-ids 097da903-ab95-44f3-bb5d-5fc08dfb6cc3 '}
                       ],
             args = [ 
                       arg(    '--instance-ids',     dest='INSTANCE_ID',     help='Instance ID of the DCS instance')
                ])    
    def stop_instance():
        OtcConfig.DCS_ACTION = "stop"
        REQ_UPDATE_DCS=utils_templates.create_request("update_instance")
        #print (REQ_UPDATE_DCS)
        
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.0/" + OtcConfig.PROJECT_ID +  "/instances/status"
        #print (url)
        ret = utils_http.put(url, REQ_UPDATE_DCS )

        #print (ret)

        return ret

    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="Start instance",
             examples=[
                       {'Start instance":"otc dcs start_instance'},
                       {'Start a specific DCS instance: otc dcs start_instance --instance-ids 097da903-ab95-44f3-bb5d-5fc08dfb6cc3 '}
                       ],
             args = [ 
                       arg(    '--instance-ids',     dest='INSTANCE_ID',     help='Instance ID of the DCS instance')
                ])    
    def start_instance():
        OtcConfig.DCS_ACTION = "start"
        REQ_UPDATE_DCS=utils_templates.create_request("update_instance")
        #print (REQ_UPDATE_DCS)
        
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.0/" + OtcConfig.PROJECT_ID +  "/instances/status"
        #print (url)
        ret = utils_http.put(url, REQ_UPDATE_DCS )

        print (ret)

        return ret

    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="Restart instance",
             examples=[
                       {'Restart instance":"otc dcs restart_instance'},
                       {'Restart a specific DCS instance: otc dcs restart_instance --instance-ids 097da903-ab95-44f3-bb5d-5fc08dfb6cc3 '}
                       ],
             args = [ 
                       arg(    '--instance-ids',     dest='INSTANCE_ID',     help='Instance ID of the DCS instance')
                ])    
    def restart_instance():
        OtcConfig.DCS_ACTION = "restart"
        REQ_UPDATE_DCS=utils_templates.create_request("update_instance")
        #print (REQ_UPDATE_DCS)
        
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.0/" + OtcConfig.PROJECT_ID +  "/instances/status"
        #print (url)
        ret = utils_http.put(url, REQ_UPDATE_DCS )

        #print (ret)

        return ret

    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="Describe quotas",
             examples=[
                       {'Describe DCS quotas":"otc dcs describe-quotas'}
                       ],
             args = [ 
                ])    
    def describe_quotas():
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.0/" + OtcConfig.PROJECT_ID + "/quota"
        #print (url)
        ret = utils_http.get(url)

        #print (ret)
        dcs.otcOutputHandler().print_output(ret, mainkey = "")

        return ret

    @staticmethod
    def convertAZnameToId():
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.0/" + "availableZones"
        JSON = utils_http.get(url)
        parsed  = json.loads(JSON)
        azs = parsed["available_zones"]
        ret = None
        for az in azs:
            if az.get("name") == OtcConfig.AZ:
                ret = az["id"]
        OtcConfig.AZID = ret

        return ret

    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="List availability zones",
             examples=[
                       {'Describe DCS quotas":"otc dcs describe-quotas'}
                       ],
             args = [ 
                ])    
    def describe_azs():
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.0/" + "availableZones"
        #print (url)
        ret = utils_http.get(url)

        #print (ret)

        dcs.otcOutputHandler().print_output(ret, mainkey = "")

        return ret

