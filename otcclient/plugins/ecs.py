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
    
class ecs(otcpluginbase):
    ar = {}    
    
    @staticmethod
    def otcOutputHandler(): 
        return getplugin(OtcConfig.OUTPUT_FORMAT)
 
    def otctype(self):
        return "func" 

    @staticmethod 
    def describe_instances():  
        url = "https://" + OtcConfig.DEFAULT_HOST +  "/v2/" + OtcConfig.PROJECT_ID + "/servers"
        
        if not OtcConfig.INSTANCE_NAME is None:
            ecs.convertINSTANCENameToId() 

        if OtcConfig.INSTANCE_ID is None: 
            ret = utils_http.get(url)        
            ecs.otcOutputHandler().print_output(ret, mainkey = "servers", listkey={"id", "name"})
        else:            
            ret = utils_http.get(url + '/' + OtcConfig.INSTANCE_ID )        
            maindata = json.loads(ret)
            if "itemNotFound" in  maindata:
                raise RuntimeError("Not found!")                      
            ecs.otcOutputHandler().print_output(ret,mainkey="server") 
        return ret



    @staticmethod 
    def describe_vpcs():
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/vpcs"
        ret = utils_http.get(url)
        ecs.otcOutputHandler().print_output(ret, mainkey = "vpcs", listkey={"id", "name", "status", "cidr"})
        return ret


    @staticmethod 
    def describe_addresses():
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/publicips"        
        ret = utils_http.get(url)
        ecs.otcOutputHandler().print_output(ret, mainkey="publicips", listkey={"id", "status", "public_ip_address", "private_ip_address", "type", "create_time", "bandwidth_size"})
        return ret

    @staticmethod 
    def describe_bandwiths():
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/bandwidths"        
        ret = utils_http.get(url)
        ecs.otcOutputHandler().print_output(ret, mainkey="bandwidths", listkey={"id", "name", "publicip_info", "size"})
        return ret

    @staticmethod 
    def describe_private_addresses():
        if not (OtcConfig.VPCNAME is None):
            ecs.convertVPCNameToId()
        
        if not OtcConfig.SUBNETNAME is None:
            ecs.convertSUBNETNameToId()

        if OtcConfig.VPCID is None:
            print("VPC definition not Correct ! Check VPCs:")
            print("otc ecs describe-vpcs")
            os._exit(1)
        if OtcConfig.SUBNETID is None:       
            print("Subnet definition not Correct ! Check subnets:")
            print("otc ecs describe-subnets")
            os._exit(1)
            
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/subnets/" + OtcConfig.SUBNETID + "/privateips"          
        ret = utils_http.get(url)        
        ecs.otcOutputHandler().print_output(ret, mainkey="privateips", listkey={"id", "status", "ip_address", "device_owner", "subnet_id"})
        return ret



    @staticmethod 
    def describe_security_groups():
        if (not (OtcConfig.SECUGROUPNAME is None)) or (not (OtcConfig.SECUGROUP is None)):

            if (not (OtcConfig.SECUGROUPNAME is None)):
                ecs.convertSECUGROUPNameToId() 
                
            url = "https://" + OtcConfig.DEFAULT_HOST+ "/v2.0/security-group-rules?security_group_id=" + OtcConfig.SECUGROUP        
            ret = utils_http.get(url)                     
            ecs.otcOutputHandler().print_output(ret, mainkey= "security_group_rules", listkey={"id","direction", "protocol","port_range_min","port_range_max" })
        else:             
            url="https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/security-groups"
            ret = utils_http.get(url)            
            ecs.otcOutputHandler().print_output(ret, mainkey= "security_groups", listkey={"id", "name", "vpc_id" })                    
        return ret

    @staticmethod 
    def describe_subnets():
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/subnets"
        ret = utils_http.get(url)
        ecs.otcOutputHandler().print_output(ret, mainkey="subnets", listkey={"id", "name", "cidr", "status", "vpc_id", "gateway_ip", "primary_dns", "availability_zone"})
        return ret

    @staticmethod 
    def describe_network_interfaces(): 
        if not OtcConfig.INSTANCE_NAME is None:
            ecs.convertINSTANCENameToId() 
        
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v2/" + OtcConfig.PROJECT_ID + "/servers/" + OtcConfig.INSTANCE_ID + "/os-interface"
        
        ret = utils_http.get(url)
#        print ret
        ecs.otcOutputHandler().print_output(ret, mainkey="interfaceAttachments", listkey={"port_state", "fixed_ips", "port_id", "net_id", "mac_addr"})
        return ret




    @staticmethod       
    def describe_images():
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v2/images"
        ret = utils_http.get(url)
        ecs.otcOutputHandler().print_output(ret, mainkey="images", listkey={"id", "name", "__os_type", "updated_at", "deleted"})
        return ret


    @staticmethod 
    def describe_flavors():
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/cloudservers/flavors"
        ret = utils_http.get(url)
        ecs.otcOutputHandler().print_output(ret, mainkey="flavors", listkey= {"id", "name", "vcpus", "ram", "disk", "swap"})
        return ret

    @staticmethod 
    def describe_key_pairs():
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v2/" + OtcConfig.PROJECT_ID + "/os-keypairs"
        ret = utils_http.get( url )    
        ecs.otcOutputHandler().print_output(ret, mainkey="keypairs", subkey="keypair", listkey={"name", "fingerprint", "public_key"})        
        return ret


    @staticmethod 
    def create_key_pair():
        REQ_CREATE_KEYPAIR = "{ \"keypair\": { \"name\": \"" + OtcConfig.KEYNAME + "\", " + "\"public_key\": \"" + OtcConfig.PUBLICKEY + "\" } }"
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v2/" + OtcConfig.PROJECT_ID + "/os-keypairs"
        ret = utils_http.post(url, REQ_CREATE_KEYPAIR)
        parsed = json.loads(ret) 
        if "keypair" not in  parsed:            
            print("Can not create:" +ret)  
            os._exit( 1 )             
  
        ecs.otcOutputHandler().print_output(ret, mainkey="keypair")
        return ret


    @staticmethod 
    def allocate_address():
        REQ_CREATE_PUBLICIP = "{\"publicip\":{\"type\":\"5_bgp\"},\"bandwidth\":{\"name\":\"apiTest\",\"size\":5,\"share_type\":\"PER\",\"charge_mode\":\"traffic\"}}"
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/publicips"
        ret = utils_http.post(url, REQ_CREATE_PUBLICIP)
        print( ret )
        maindata = json.loads(ret)
        if "code" in  maindata:            
            print("Can not create:" +maindata["message"])  
            os._exit( 1 )             
                            
        ecs.otcOutputHandler().print_output(ret, mainkey="publicip")
        return ret

    @staticmethod       
    def release_address():
        if not (OtcConfig.PUBLICIP is None):
            ecs.convertPublicIpNameToId()            
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/publicips" + \
        "/" + OtcConfig.PUBLICIPID
        ret = utils_http.delete(url)
        print(ret)
        return ret

    @staticmethod       
    def release_private_address():
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/privateips" + OtcConfig.PRIVATEIPID
        ret = utils_http.delete(url)
        print(ret)
        return ret


    @staticmethod 
    def associate_address():        
        REQ_ASSOCIATE_PUBLICIP = "{ \"publicip\": { \"port_id\": \"" + OtcConfig.NETWORKINTERFACEID + "\" } }"
        #print REQ_ASSOCIATE_PUBLICIP
        if not (OtcConfig.PUBLICIP is None):
            ecs.convertPublicIpNameToId()

        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/publicips" + "/" + OtcConfig.PUBLICIPID        
        ret = utils_http.put(url, REQ_ASSOCIATE_PUBLICIP)
        print(ret)
        return ret

    @staticmethod 
    def resize_instance():        
        if not OtcConfig.INSTANCE_NAME is None:
            ecs.convertINSTANCENameToId() 
        if not OtcConfig.INSTANCE_TYPE_NAME is None:
            ecs.convertFlavorNameToId()
        
        if OtcConfig.INSTANCE_ID is None :
            raise RuntimeError( "Error. Must be specify the Instance Name or ID!")
     
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/cloudservers/" + OtcConfig.INSTANCE_ID + "/resize"
        req = utils_templates.create_request("ecs_resize")
        ret = utils_http.post(url, req)
        print(ret)
        return ret


    @staticmethod       
    def delete_key_pair():
        """ generated source for method KEYPAIRDelete """
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v2/" + OtcConfig.PROJECT_ID + "/os-keypairs"+ "/" + OtcConfig.KEYNAME
        ret = utils_http.delete(url )        
        return ret

    @staticmethod 
    def getECSJOBList():
        """ generated source for method getECSJOBList """        
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/jobs/" + OtcConfig.ECSTASKID
        ret = utils_http.get(url)
        newstatus = str( json.loads(ret)["status"]).upper()
        if newstatus != OtcConfig.ECSCREATEJOBSTATUS:
            sys.stdout.write( "\n" + newstatus )
        OtcConfig.ECSCREATEJOBSTATUS = newstatus         
        return OtcConfig.ECSCREATEJOBSTATUS

    @staticmethod
    def getFileContentJSON( aSource, aTarget):
        """ generated source for method getFileContentJSON """
        with open(aSource, "rb") as _file:
            FILECONTENT = base64.b64encode(_file.read())        
        FILE_TEMPLATE = "{ \"path\": \"" + aTarget + "\", \"contents\": \"" + FILECONTENT + "\" }"
        return FILE_TEMPLATE

    @staticmethod
    def getUserDataContent(aSource):
        USER_DATA = ""
        with open(aSource, "rb") as _file:
            USER_DATA = base64.b64encode(_file.read())
        return USER_DATA

    @staticmethod
    def getPersonalizationJSON():
        """ generated source for method getPersonalizationJSON """
        FILEJSONITEM = ""    
        if not OtcConfig.FILE1 is None: 
            ar =  str(OtcConfig.FILE1).split("=")
            FILEJSONITEM = ecs.getFileContentJSON(ar[1], ar[0])            
        FILECOLLECTIONJSON = FILEJSONITEM
        FILEJSONITEM = ""        
        if not OtcConfig.FILE2 is None:
            ar =  str(OtcConfig.FILE2).split("=")
            if len(FILECOLLECTIONJSON) > 0:
                FILEJSONITEM = ","                
            FILEJSONITEM = FILEJSONITEM + ecs.getFileContentJSON(ar[1], ar[0])
        FILECOLLECTIONJSON = FILECOLLECTIONJSON + FILEJSONITEM
        FILEJSONITEM = ""
        if not OtcConfig.FILE3 is None:
            ar =  str(OtcConfig.FILE3).split("=")
            if len(FILECOLLECTIONJSON) > 0:
                FILEJSONITEM = ","
            FILEJSONITEM = ecs.getFileContentJSON(ar[1], ar[0])
        FILECOLLECTIONJSON = FILECOLLECTIONJSON + FILEJSONITEM
        FILEJSONITEM = ""
        if not OtcConfig.FILE4 is None:
            ar =  str(OtcConfig.FILE4).split("=")
            if len(FILECOLLECTIONJSON) > 0:
                FILEJSONITEM = ","
            FILEJSONITEM = ecs.getFileContentJSON(ar[1], ar[0])
        FILECOLLECTIONJSON = FILECOLLECTIONJSON + FILEJSONITEM
        FILEJSONITEM = ""
        if not OtcConfig.FILE5 is None:
            ar =  str(OtcConfig.FILE5).split("=")
            if len(FILECOLLECTIONJSON) > 0:
                FILEJSONITEM = ","
            FILEJSONITEM = ecs.getFileContentJSON(ar[1], ar[0])
        FILECOLLECTIONJSON = FILECOLLECTIONJSON + FILEJSONITEM
        PERSONALIZATION = ""
        if len(FILECOLLECTIONJSON) > 0:
            PERSONALIZATION = "\"personality\": [ " + FILECOLLECTIONJSON + "],"
        return PERSONALIZATION

    @staticmethod
    def ECSAction():
        if not OtcConfig.INSTANCE_NAME is None:
            ecs.convertINSTANCENameToId() 
        
        if OtcConfig.INSTANCE_ID is None :
            raise RuntimeError( "Error. Must be specify the Instance Name or ID!")
        
        REQ_ECS_ACTION_VM = "{ " + "    \"" + OtcConfig.ECSACTION + "\": " + "    { " + "     \"type\":\"" + OtcConfig.ECSACTIONTYPE + "\", " + "     \"servers\": [ { \"id\": \"" + OtcConfig.INSTANCE_ID + "\" }] " + "     } " + "}"
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/cloudservers/action"
        ret = utils_http.post(url, REQ_ECS_ACTION_VM)
        print(ret)
        return ret


    @staticmethod
    def start_instances():
        OtcConfig.ECSACTION = "os-start"
        ecs.ECSAction()

    @staticmethod
    def stop_instances():
        OtcConfig.ECSACTION = "os-stop"
        ecs.ECSAction()

    @staticmethod
    def delete_instances():
        if not OtcConfig.INSTANCE_NAME is None:
            ecs.convertINSTANCENameToId() 
        if OtcConfig.INSTANCE_ID is None :
            raise RuntimeError( "Error. Must be specify the Instance ID!")

        REQ_ECS_DELETE_VM = "{ \"servers\": [ { \"id\": \"" + OtcConfig.INSTANCE_ID + "\" } ]," + " \"delete_publicip\": \"" + OtcConfig.DELETE_PUBLICIP + "\", \"delete_volume\": \"" + OtcConfig.DELETE_VOLUME + "\" }"
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/cloudservers" + "/delete"
        ret = utils_http.post(url, REQ_ECS_DELETE_VM)
        print(ret)
        return ret

    @staticmethod
    def create_vpc():
        REQ_CREATE_VPC = "{ \"vpc\": { \"name\": \"" + OtcConfig.VPCNAME + "\", \"cidr\": \"" + OtcConfig.CIDR + "\" } }"
        
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/vpcs"
        ret = utils_http.post(url, REQ_CREATE_VPC)
        print(ret)
        return ret

    @staticmethod
    def delete_vpc():
        if not (OtcConfig.VPCNAME is None):
            ecs.convertVPCNameToId()

        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/vpcs" + OtcConfig.VPCID    
        ret = utils_http.delete(url)
        print(ret)
        return ret

    @staticmethod
    def create_subnet():
        if not (OtcConfig.VPCNAME is None):
            ecs.convertVPCNameToId()
            
        REQ_CREATE_SUBNET = "{ \"subnet\": { \"name\": \"" + OtcConfig.SUBNETNAME + "\", \"cidr\": \"" + OtcConfig.CIDR + "\", \"gateway_ip\": \"" + OtcConfig.GWIP + "\", \"dhcp_enable\": \"true\", \"primary_dns\": \"" + OtcConfig.PRIMARYDNS + "\", \"secondary_dns\": \"" + OtcConfig.SECDNS + "\", \"availability_zone\":\"" + OtcConfig.AZ + "\", \"vpc_id\":\"" + OtcConfig.VPCID + "\" } }"
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/subnets"
        ret = utils_http.post(url, REQ_CREATE_SUBNET)
        print(ret)
        return ret

    @staticmethod
    def delete_subnet():
        if OtcConfig.SUBNETNAME:
            ecs.convertSUBNETNameToId()
        
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/subnets" + OtcConfig.SUBNETID
        ret = utils_http.delete(url)
        return ret



    @staticmethod
    def create_network_interface():
        if not (OtcConfig.VPCNAME is None):
            ecs.convertVPCNameToId()
        if not OtcConfig.SUBNETNAME is None:
            ecs.convertSUBNETNameToId()
        if not OtcConfig.SECUGROUPNAME is None:
            ecs.convertSECUGROUPNameToId()
        if not OtcConfig.INSTANCE_NAME is None:
            ecs.convertINSTANCENameToId() 
              
                    
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/cloudservers/" + OtcConfig.INSTANCE_ID + "/nics"        
        req = utils_templates.create_request("add_nics")
                
        ret = utils_http.post(url, req)
        
        return ret

    @staticmethod
    def create_security_group():
        if not (OtcConfig.VPCNAME is None):
            ecs.convertVPCNameToId()
        
        REQ_CREATE_SECGROUP = "{ \"security_group\": { \"name\":\"" + OtcConfig.SECUGROUPNAME + "\", \"vpc_id\" : \"" + OtcConfig.VPCID + "\" } }"
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/security-groups"
        ret = utils_http.post(url, REQ_CREATE_SECGROUP)
        return ret

    @staticmethod
    def delete_security_group():
        if not (OtcConfig.VPCNAME is None):
            ecs.convertVPCNameToId()

        if not (OtcConfig.SECUGROUPNAME is None):
            ecs.convertSECUGROUPNameToId()
        
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v2.0/" + "/security-groups" + "/"+ OtcConfig.SECUGROUP
        ret = utils_http.delete(url)
        return ret


    @staticmethod
    def authorize_security_group_ingress():
        OtcConfig.DIRECTION = "ingress"
        ecs._secgrouprulecreate()

    @staticmethod
    def authorize_security_group_egress():
        OtcConfig.DIRECTION = "egress"
        ecs._secgrouprulecreate()

    @staticmethod
    def _secgrouprulecreate():
        if not (OtcConfig.VPCNAME is None):
            ecs.convertVPCNameToId()

        if not (OtcConfig.SECUGROUPNAME is None):
            ecs.convertSECUGROUPNameToId()
                    
        sourceIp = ""
        if not OtcConfig.CIDR is None:
            sourceIp = "\", \"remote_ip_prefix\":\"" + OtcConfig.CIDR
        remoteGroup = ""
        if not OtcConfig.SOURCE_GROUP_ID is None:
            remoteGroup =  "\", \"remote_group_id\":\"" + OtcConfig.SOURCE_GROUP_ID    

        portrange = ""
        if not OtcConfig.PORTMIN is None and not OtcConfig.PORTMAX is None:
            portrange = "\", \"port_range_min\":\"" + OtcConfig.PORTMIN  + "\", \"port_range_max\":\"" ''+ OtcConfig.PORTMAX     
        
        REQ_CREATE_SECGROUPRULE = "{\"security_group_rule\":{ \"direction\":\"" + OtcConfig.DIRECTION +  "\",\"ethertype\":\"" + OtcConfig.ETHERTYPE + "\",  \"protocol\":\""+ OtcConfig.PROTOCOL+ portrange +remoteGroup  + sourceIp+ "\"  , \"security_group_id\":\""+ OtcConfig.SECUGROUP + "\" } }"
        #REQ_CREATE_SECGROUPRULE = "{\"security_group_rule\":{ \"direction\":\"" + OtcConfig.DIRECTION + "\", \"port_range_min\":\"" + OtcConfig.PORTMIN  + "\", \"ethertype\":\"" + OtcConfig.ETHERTYPE + "\", \"port_range_max\":\"" ''+ OtcConfig.PORTMAX+ "\", \"protocol\":\""+ OtcConfig.PROTOCOL+ remoteGroup  + sourceIp+ "\"  , \"security_group_id\":\""+ OtcConfig.SECUGROUP + "\" } }"                
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v2.0/security-group-rules" 
        ret = utils_http.post(url, REQ_CREATE_SECGROUPRULE)
        #print REQ_CREATE_SECGROUPRULE 
        print (ret)
        ecs.otcOutputHandler().print_output(ret, mainkey="security_group_rule")
        return ret


    @staticmethod
    def run_instances():
        
        if not OtcConfig.VPCNAME is None:
            ecs.convertVPCNameToId()
        if not OtcConfig.SUBNETNAME is None:
            ecs.convertSUBNETNameToId()
        if not OtcConfig.IMAGENAME is None:
            ecs.convertIMAGENameToId()
        if not OtcConfig.SECUGROUPNAME is None:
            ecs.convertSECUGROUPNameToId()
        if not OtcConfig.INSTANCE_TYPE_NAME is None:
            ecs.convertFlavorNameToId()

        if OtcConfig.IMAGE_ID is None:
            print("Image definition not Correct ! Check images:")
            print("otc ecs describe-images")
            os._exit(1)
        if OtcConfig.INSTANCE_TYPE is None:
            print("Instance Type definition not Correct ! Check flavors:")
            print("otc ecs describe-flavors")
            os._exit(1)
        if OtcConfig.VPCID is None:
            print("VPC definition not Correct ! Check VPCs:")
            print("otc ecs describe-vpcs")
            os._exit(1)
        if OtcConfig.SECUGROUP is None:
            print("Security Group definition not Correct ! Check security groups:")
            print("otc ecs describe-security-groups")
            os._exit(1)
        if OtcConfig.SUBNETID is None:       
            print("Subnet definition not Correct ! Check subnets:")
            print("otc ecs describe-subnets")
            os._exit(1)
                            
        PUBLICIPJSON = ""
#        if OtcConfig.CREATE_ECS_WITH_PUBLIC_IP:
#            PUBLICIPJSON = "\"publicip\": { \"eip\": { \"iptype\": \"5_bgp\", \"bandwidth\": { \"size\": 5, \"sharetype\": \"PER\", \"chargemode\": \"traffic\" } } },"
        PERSONALIZATION = ecs.getPersonalizationJSON()
        if not OtcConfig.USER_DATA_PATH is None:
            USER_DATA = ecs.getUserDataContent(OtcConfig.USER_DATA_PATH)
            OtcConfig.USER_DATA = USER_DATA
        
#        OtcConfig.PUBLICIPJSON = PUBLICIPJSON
        OtcConfig.PERSONALIZATION = PERSONALIZATION
#        REQ_CREATE_VM = "    {                 " + "        \"server\": { " + "        \"availability_zone\": \"" + OtcConfig.AZ + "\",         " + "        \"name\": \"" + OtcConfig.INSTANCE_NAME + "\",            " + "        \"imageRef\": \"" + OtcConfig.IMAGE_ID + "\",             " + "        \"root_volume\": {      " + "            \"volumetype\": \"SATA\"            " + "        }, " + "        \"flavorRef\": \"" + OtcConfig.INSTANCE_TYPE + "\"," + PERSONALIZATION + "        \"vpcid\": \"" + OtcConfig.VPCID + "\",           " + "        \"security_groups\": [         " + "            { " + "                \"id\": \"" + OtcConfig.SECUGROUP + "\"   " + "            }    " + "        ],        " + "        \"nics\": [           " + "            {            " + "                \"subnet_id\": \"" + OtcConfig.SUBNETID + "\"        " + "            }         " + "        ],       " + PUBLICIPJSON + "        \"key_name\": \"" + OtcConfig.KEYNAME + "\",    " + "        \"adminPass\": \"" + OtcConfig.ADMINPASS + "\",   " + "        \"count\": \"" + OtcConfig.NUMCOUNT + "\",   " + "        \"},\": {      " + "            \"__vnc_keymap\": \"de\"    " + "        }   " + "        }   " + "    }       " + "    "
        
        REQ_CREATE_VM=utils_templates.create_request("create_vm")        
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/cloudservers"
        ret = utils_http.post(url, REQ_CREATE_VM)
        print ret 

        OtcConfig.ECSTASKID  = json.loads(ret)["job_id"]

        if OtcConfig.WAIT_CREATE:
            ecs.getECSJOBList()
            while OtcConfig.ECSCREATEJOBSTATUS in ["RUNNING", "INIT"]:
                sleep(10)
                ecs.getECSJOBList()
                sys.stdout.write('.')
                #sys.stdout.flush()
        
        if "SUCCESS" == OtcConfig.ECSCREATEJOBSTATUS:
            return OtcConfig.ECSCREATEJOBSTATUS
            
        print("ECS Creation status: " + OtcConfig.ECSCREATEJOBSTATUS)
        return ret

    @staticmethod
    def getIamToken():
        if OtcConfig.PROJECT_NAME != None: 
            project = "\"name\": \"" + OtcConfig.PROJECT_NAME + "\" " 

        else:
            project = "\"id\": \"" + OtcConfig.PROJECT_ID + "\""
            
        REQ_IAM = "    {" + "        \"auth\": {       " + "        \"identity\": {   " + "            \"methods\": [" + "                \"password\"                             " + "            ],            " + "            \"password\": {                              " + "                \"user\": {                              " + "                    \"name\": \"" + OtcConfig.USERNAME + "\",    " + "                    \"password\": \"" + OtcConfig.PASSWORD + "\"," + "                    \"domain\": {                        " + "                        \"name\": \"" + OtcConfig.DOMAIN + "\"            " + "                    }     " + "                }         " + "            }             " + "        },                " + "        \"scope\": {      " + "            \"project\": {" + project + "            }             " + "        }                 " + "        }                 " + "    }"
        url = "https://" + OtcConfig.DEFAULT_HOST +":443/v3/auth/tokens"
        ret = utils_http.post(url, REQ_IAM)
        maindata = json.loads(ret)
        OtcConfig.PROJECT_ID = maindata['token']['project']['id'] 

        return ret

    @staticmethod
    def getIamTokenAKSK():
        if OtcConfig.PROJECT_NAME != None: 
            project = "\"name\": \"" + OtcConfig.PROJECT_NAME + "\" " 

        else:
            project = "\"id\": \"" + OtcConfig.PROJECT_ID + "\""
            
        REQ_IAM = "    {" + "        \"auth\": {       " + "        \"identity\": {   " + "            \"methods\": [" + "                \"password\"                             " + "            ],            " + "            \"password\": {                              " + "                \"user\": {                              " + "                    \"name\": \"" + OtcConfig.USERNAME + "\",    " + "                    \"password\": \"" + OtcConfig.PASSWORD + "\"," + "                    \"domain\": {                        " + "                        \"name\": \"" + OtcConfig.DOMAIN + "\"            " + "                    }     " + "                }         " + "            }             " + "        },                " + "        \"scope\": {      " + "            \"project\": {" + project + "            }             " + "        }                 " + "        }                 " + "    }"
        url = "https://" + OtcConfig.DEFAULT_HOST +":443/v3/auth/tokens"
        
        ret = utils_http.post(url, REQ_IAM)
        maindata = json.loads(ret)
        OtcConfig.PROJECT_ID = maindata['token']['project']['id'] 

        return ret


    @staticmethod
    def convertFlavorNameToId():
        """ generated source for method convertFlavorNameToId """
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/cloudservers/flavors"
        JSON = utils_http.get(url)        
        parsed  = json.loads(JSON)
        flavors = parsed["flavors"]
        ret = None
        for flavor in flavors:
            if flavor.get("name") == OtcConfig.INSTANCE_TYPE_NAME:
                ret = flavor["id"]
        OtcConfig.INSTANCE_TYPE = ret
    
    @staticmethod
    def convertPublicIpNameToId():
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/publicips"
        JSON = utils_http.get(url)        
        parsed  = json.loads(JSON)
        publicips = parsed["publicips"]
        ret = None
        for publicip in publicips:
            if publicip.get("public_ip_address") == OtcConfig.PUBLICIP:
                ret = publicip["id"]
        OtcConfig.PUBLICIPID = ret

    @staticmethod
    def convertVPCNameToId():
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/vpcs"
        JSON = utils_http.get(url)        
        parsed  = json.loads(JSON)
        vpcs = parsed["vpcs"]
        ret = None
        for vpc in vpcs:
            if vpc.get("name") == OtcConfig.VPCNAME:
                ret = vpc["id"]
        OtcConfig.VPCID = ret

    @staticmethod
    def convertVOLUMENameToId():
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v2/" + OtcConfig.PROJECT_ID + "/cloudvolumes"
        JSON = utils_http.get(url)        
        parsed  = json.loads(JSON)
        #print JSON
        cloudvolumes = parsed["volumes"]
        ret = None
        for cloudvolume in cloudvolumes:
            if cloudvolume.get("name") == OtcConfig.VOLUME_NAME:
                ret = cloudvolume["id"]
        OtcConfig.VOLUME_ID = ret


    @staticmethod
    def convertSUBNETNameToId():
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/subnets"
        ar = []
        print OtcConfig.SUBNETNAME
        ar.append(OtcConfig.SUBNETNAME)
        if "," in OtcConfig.SUBNETNAME:             
            ar=str(OtcConfig.SUBNETNAME).split(",")
                        
        JSON = utils_http.get(url)
        parsed  = json.loads(JSON)
        subnets = parsed["subnets"]        
        ret = ""
        for item in ar: 
            for subnet in subnets:
                if subnet.get("name") == item and subnet.get("vpc_id") == OtcConfig.VPCID:
                    if len(ret) > 0:
                        ret = ret + ","
                    ret = ret + subnet["id"]
        OtcConfig.SUBNETID = ret        

    @staticmethod
    def convertIMAGENameToId():
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v2/images"
        JSON = utils_http.get(url)
        parsed  = json.loads(JSON)
        images = parsed["images"]
        ret = None
        for image in images:
            if image.get("name") == OtcConfig.IMAGENAME:
                ret = image["id"]
        OtcConfig.IMAGE_ID = ret

    @staticmethod
    def convertINSTANCENameToId():
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v2/" + OtcConfig.PROJECT_ID + "/servers"
        JSON = utils_http.get(url)
        parsed  = json.loads(JSON)
        servers = parsed["servers"]

        ret = None
        for server in servers:
            if server.get("name") == OtcConfig.INSTANCE_NAME:
                ret = server["id"]
        OtcConfig.INSTANCE_ID = ret        
        
    @staticmethod
    def convertSECUGROUPNameToId():
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/security-groups"
        JSON = utils_http.get(url)
        parsed  = json.loads(JSON)
        security_groups = parsed["security_groups"]
        
        if not (OtcConfig.VPCNAME is None):
            ecs.convertVPCNameToId()
                
        for security_group in security_groups:
            if security_group.get("name") == OtcConfig.SECUGROUPNAME and ( security_group.get("vpc_id") == OtcConfig.VPCID or OtcConfig.VPCID is None ) :
                OtcConfig.SECUGROUP = security_group["id"]
            if security_group.get("name") == OtcConfig.SOURCE_GROUP and ( security_group.get("vpc_id") == OtcConfig.VPCID or OtcConfig.VPCID is None ) :
                OtcConfig.SOURCE_GROUP_ID = security_group["id"]

        OtcConfig.SECUGROUP = OtcConfig.SECUGROUP
        return OtcConfig.SECUGROUP              

    @staticmethod
    def describe_volumes():
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v2/" + OtcConfig.PROJECT_ID + "/cloudvolumes"+ "/detail"
        ret = utils_http.get( url )
        ecs.otcOutputHandler().print_output(ret,  mainkey = "volumes", listkey= {"id", "name", "volume_type", "size", "status", "bootable", "availability_zone", "limit", "attachments", "source_volid", "snapshot_id", "description", "created_at"})
        return ret

    @staticmethod
    def list_volumes():
        if not OtcConfig.INSTANCE_NAME is None:
            ecs.convertINSTANCENameToId() 

        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v2/" + OtcConfig.PROJECT_ID + "/servers/"+ OtcConfig.INSTANCE_ID + "/os-volume_attachments"
        ret = utils_http.get( url )
        print ret 
        #ecs.otcOutputHandler().print_output(ret,  mainkey = "volumes", listkey= {"id", "name", "volume_type", "size", "status", "bootable", "availability_zone", "limit", "attachments", "source_volid", "snapshot_id", "description", "created_at"})
        return ret


    @staticmethod
    def create_volume():        
        REQ_CREATE_CLOUDVOLUMES = "{ \"volume\": { \"backup_id\": " + OtcConfig.SNAPSHOTID + ", " + "\"count\": " + OtcConfig.NUMCOUNT + ", \"availability_zone\": \"" + OtcConfig.AZ + "\",\"description\": \"" + OtcConfig.VOLUME_NAME + "\", \"size\": " + OtcConfig.VOLUME_SIZE + ", \"name\": \"" + OtcConfig.VOLUME_NAME + "\", \"imageRef\": " + "null" + ", \"volume_type\": \"" + OtcConfig.VOLUME_TYPE + "\" } }"
        #print REQ_CREATE_CLOUDVOLUMES
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v2/" + OtcConfig.PROJECT_ID + "/cloudvolumes"
        ret = utils_http.post(url, REQ_CREATE_CLOUDVOLUMES)
        print(ret)
        return ret


    @staticmethod
    def attach_volume():
        """ generated source for method AttachVolume """        
        REQ_ATTACH_CLOUDVOLUMES = "{ \"volumeAttachment\": { \"volumeId\": \"" + OtcConfig.VOLUME_ID + "\", \"device\": \"" + OtcConfig.EVS_DEVICE + "\" } }"
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/cloudservers/" + OtcConfig.INSTANCE_ID + "/attachvolume"
        ret = utils_http.post(url, REQ_ATTACH_CLOUDVOLUMES)
        print(ret)
        return ret


    @staticmethod
    def detach_volume():
        """ generated source for method DetachVolume """
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/cloudservers/" + OtcConfig.INSTANCE_ID + "/detachvolume/" + OtcConfig.VOLUME_ID
        ret = utils_http.delete(url)
        print(ret)
        return ret

    @staticmethod
    def delete_volume():
        if not OtcConfig.VOLUME_NAME is None:
            ecs.convertVOLUMENameToId() 
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v2/" + OtcConfig.PROJECT_ID + "/cloudvolumes" + "/" + OtcConfig.VOLUME_ID    
        ret = utils_http.delete(url)
        print(ret)
        return ret


    @staticmethod
    def describe_quotas():
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/cloudservers/limits"
        ret = utils_http.get(url)
        ecs.otcOutputHandler().print_output(ret, mainkey="absolute")
        return ret

 
    @staticmethod
    def describe_snapshots():    
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v2/" + OtcConfig.PROJECT_ID + "/backups/detail"
        ret = utils_http.get(url)               
        ecs.otcOutputHandler().print_output(ret, mainkey = "backups", listkey={"name","id","size","status","description","created_at", "created_at"} )
        return ret


    @staticmethod

    def restore_snapshot():
        if not OtcConfig.VOLUME_NAME is None:
            ecs.convertVOLUMENameToId() 

        if OtcConfig.VOLUME_ID is None or OtcConfig.SNAPSHOTID is None:
            print("Image definition not Correct ! Check images:")
            print("otc ecs describe-backups")
            os._exit(1)

        REQ_RESTORE_BACKUP = "{ \"restore\":{ \"volume_id\":\"" + OtcConfig.VOLUME_ID + "\" } }"
        #print REQ_RESTORE_BACKUP
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v2/" + OtcConfig.PROJECT_ID + "/cloudbackups" +"/" + OtcConfig.SNAPSHOTID + "/restore"
        ret = utils_http.post(url, REQ_RESTORE_BACKUP)
        print(ret)
        return ret


    @staticmethod
    def delete_snapshot():        
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v2/" + OtcConfig.PROJECT_ID + "/cloudbackups"+ "/" + OtcConfig.SNAPSHOTID
        ret = utils_http.post( url , "")
        print(ret)
        return ret


    @staticmethod
    def create_snapshot():
        if not OtcConfig.VOLUME_NAME is None:
            ecs.convertVOLUMENameToId() 

        if not OtcConfig.DESCRIPTION is None:
            OtcConfig.DESCRIPTION = OtcConfig.VOLUME_ID
            if not OtcConfig.VOLUME_NAME is None:
                OtcConfig.DESCRIPTION = OtcConfig.VOLUME_NAME
                 
        REQ_CREATE_BACKUP = "{ \"backup\":{ \"" + "volume_id\":\"" + OtcConfig.VOLUME_ID + "\", " + "\"name\":\"" + OtcConfig.DESCRIPTION + "\", \"description\":\"" + OtcConfig.DESCRIPTION + "\" } }"
        #print REQ_CREATE_BACKUP
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v2/" + OtcConfig.PROJECT_ID + "/cloudbackups"
        ret = utils_http.post(url, REQ_CREATE_BACKUP)
        print (ret)
        return ret

