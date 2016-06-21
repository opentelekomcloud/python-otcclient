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
        url = ecs.baseurl +  "/v2/" + OtcConfig.PROJECT_ID + "/servers"
        
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
                os._exit( 1 )             
            ecs.otcOutputHandler().print_output(ret,mainkey="server") 
        return ret



    @staticmethod 
    def describe_vpcs():
        url = ecs.baseurl+ "/v1/" + OtcConfig.PROJECT_ID + "/vpcs"
        ret = utils_http.get(url)
        ecs.otcOutputHandler().print_output(ret, mainkey = "vpcs", listkey={"id", "name", "status", "cidr"})
        return ret


    @staticmethod 
    def describe_addresses():
        url = ecs.baseurl+ "/v1/" + OtcConfig.PROJECT_ID + "/publicips"        
        ret = utils_http.get(url)
        ecs.otcOutputHandler().print_output(ret, mainkey="publicips", listkey={"id", "status", "public_ip_address", "private_ip_address", "type", "create_time", "bandwidth_size"})
        return ret


    @staticmethod 
    def describe_security_groups():
        if (not (OtcConfig.SECUGROUPNAME is None)) or (not (OtcConfig.SECUGROUP is None)):

            if (not (OtcConfig.SECUGROUPNAME is None)):
                ecs.convertSECUGROUPNameToId() 
                
            url = ecs.baseurl+ "/v2.0/security-group-rules?security_group_id=" + OtcConfig.SECUGROUP        
            ret = utils_http.get(url)                     
            ecs.otcOutputHandler().print_output(ret, mainkey= "security_group_rules", listkey={"id","direction", "protocol","port_range_min","port_range_max" })
        else:             
            url=ecs.baseurl+ "/v1/" + OtcConfig.PROJECT_ID + "/security-groups"
            ret = utils_http.get(url)            
            ecs.otcOutputHandler().print_output(ret, mainkey= "security_groups", listkey={"id", "name", "vpc_id" })                    
        return ret

    @staticmethod 
    def describe_subnets():
        url = ecs.baseurl+ "/v1/" + OtcConfig.PROJECT_ID + "/subnets"
        ret = utils_http.get(url)
        ecs.otcOutputHandler().print_output(ret, mainkey="subnets", listkey={"id", "name", "cidr", "status", "vpc_id", "gateway_ip", "primary_dns", "availability_zone"})
        return ret

    @staticmethod       
    def describe_images():
        """ generated source for method getIMAGEList """
        url = ecs.baseurl+ "/v2/images"
        ret = utils_http.get(url)
        ecs.otcOutputHandler().print_output(ret, mainkey="images", listkey={"id", "name", "__os_type", "updated_at", "deleted"})
        return ret


    #      * @see com.tsystems.otc.IOtcServiceCalls#getFLAVORList()
    #      
    @staticmethod 
    def describe_flavors():
        """ generated source for method getFLAVORList """        
        url = ecs.baseurl+ "/v1/" + OtcConfig.PROJECT_ID + "/cloudservers/flavors"
        ret = utils_http.get(url)
        ecs.otcOutputHandler().print_output(ret, mainkey="flavors", listkey= {"id", "name", "vcpus", "ram", "disk", "swap"})
        return ret

    @staticmethod 
    def describe_key_pairs():
        """ generated source for method getKEYPAIRList """
        url = ecs.baseurl+ "/v2/" + OtcConfig.PROJECT_ID + "/os-keypairs"
        ret = utils_http.get( url )
        ecs.otcOutputHandler().print_output(ret, mainkey="keypairs", subkey="keypair", listkey={"name", "fingerprint", "public_key"})        
        return ret


    @staticmethod 
    def create_key_pair():
        """ generated source for method KEYPAIRCreate """
        REQ_CREATE_KEYPAIR = "{ \"keypair\": { \"name\": \"" + OtcConfig.KEYNAME + "\", " + "\"public_key\": \"" + OtcConfig.PUBLICKEY + "\" } }"
        url = ecs.baseurl+ "/v2/" + OtcConfig.PROJECT_ID + "/os-keypairs"
        ret = utils_http.post(url, REQ_CREATE_KEYPAIR)        
        ecs.otcOutputHandler().print_output(ret, mainkey="keypair")
        return ret


    @staticmethod 
    def allocate_address():
        """ generated source for method PUBLICIPSAllocate """
        REQ_CREATE_PUBLICIP = "{\"publicip\":{\"type\":\"5_bgp\"},\"bandwidth\":{\"name\":\"apiTest\",\"size\":5,\"share_type\":\"PER\",\"charge_mode\":\"traffic\"}}"
        url = ecs.baseurl+ "/v1/" + OtcConfig.PROJECT_ID + "/publicips"
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
        url = ecs.baseurl+ "/v1/" + OtcConfig.PROJECT_ID + "/publicips" + \
        "/" + OtcConfig.PUBLICIPID
        ret = utils_http.delete(url)
        print(ret)
        return ret


    @staticmethod 
    def associate_address():
        """ generated source for method PUBLICIPSAssociate """
        REQ_ASSOCIATE_PUBLICIP = "{ \"publicip\": { \"port_id\": \"" + OtcConfig.NETWORKINTERFACEID + "\" } }"
        #print REQ_ASSOCIATE_PUBLICIP
        if not (OtcConfig.PUBLICIP is None):
            ecs.convertPublicIpNameToId()

        url = ecs.baseurl+ "/v1/" + OtcConfig.PROJECT_ID + "/publicips" + "/" + OtcConfig.PUBLICIPID        
        ret = utils_http.post(url, REQ_ASSOCIATE_PUBLICIP)
        print(ret)
        return ret


    @staticmethod       
    def delete_key_pair():
        """ generated source for method KEYPAIRDelete """
        url = ecs.baseurl+ "/v2/" + OtcConfig.PROJECT_ID + "/os-keypairs"+ "/" + OtcConfig.KEYNAME
        ret = utils_http.delete(url )        
        return ret

    @staticmethod 
    def getECSJOBList():
        """ generated source for method getECSJOBList """        
        url = ecs.baseurl+ "/v1/" + OtcConfig.PROJECT_ID + "/jobs/" + OtcConfig.ECSTASKID
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
        """ generated source for method ECSAction """        
        REQ_ECS_ACTION_VM = "{ " + "    \"" + OtcConfig.ECSACTION + "\": " + "    { " + "     \"type\":\"" + OtcConfig.ECSACTIONTYPE + "\", " + "     \"servers\": [ { \"id\": \"" + OtcConfig.INSTANCE_ID + "\" }] " + "     } " + "}"
        url = ecs.baseurl+ "/v1/" + OtcConfig.PROJECT_ID + "/cloudservers/action"
        ret = utils_http.post(url, REQ_ECS_ACTION_VM)
        return ret


    @staticmethod
    def start_instances():
        OtcConfig.ECSACTION = "os-stop"
        if OtcConfig.INSTANCE_ID is None :
            raise "Error. Must be specify the Instance ID!"
        ecs.ECSAction()

    @staticmethod
    def stop_instances():
        OtcConfig.ECSACTION = "os-stop"
        if OtcConfig.INSTANCE_ID is None :
            raise "Error. Must be specify the Instance ID!"
        ecs.ECSAction()

    @staticmethod
    def delete_instances():
        if not OtcConfig.INSTANCE_NAME is None:
            ecs.convertINSTANCENameToId() 

        REQ_ECS_DELETE_VM = "{ \"servers\": [ { \"id\": \"" + OtcConfig.INSTANCE_ID + "\" } ]," + " \"delete_publicip\": \"" + OtcConfig.DELETE_PUBLICIP + "\", \"delete_volume\": \"" + OtcConfig.DELETE_VOLUME + "\" }"
        url = ecs.baseurl+ "/v1/" + OtcConfig.PROJECT_ID + "/cloudservers" + "/delete"
        ret = utils_http.post(url, REQ_ECS_DELETE_VM)
        print ret
        return ret

    @staticmethod
    def create_vpc():
        REQ_CREATE_VPC = "{ \"vpc\": { \"name\": \"" + OtcConfig.VPCNAME + "\", \"cidr\": \"" + OtcConfig.CIDR + "\" } }"
        
        url = ecs.baseurl+ "/v1/" + OtcConfig.PROJECT_ID + "/vpcs"
        ret = utils_http.post(url, REQ_CREATE_VPC)
        print(ret)
        return ret

    @staticmethod
    def create_subnet():
        if not (OtcConfig.VPCNAME is None):
            ecs.convertVPCNameToId()
            
        REQ_CREATE_SUBNET = "{ \"subnet\": { \"name\": \"" + OtcConfig.SUBNETNAME + "\", \"cidr\": \"" + OtcConfig.CIDR + "\", \"gateway_ip\": \"" + OtcConfig.GWIP + "\", \"dhcp_enable\": \"true\", \"primary_dns\": \"" + OtcConfig.PRIMARYDNS + "\", \"secondary_dns\": \"" + OtcConfig.SECDNS + "\", \"availability_zone\":\"" + OtcConfig.AZ + "\", \"vpc_id\":\"" + OtcConfig.VPCID + "\" } }"
        url = ecs.baseurl+ "/v1/" + OtcConfig.PROJECT_ID + "/subnets"
        ret = utils_http.post(url, REQ_CREATE_SUBNET)
        print(ret)
        return ret

    @staticmethod
    def create_security_group():
        if not (OtcConfig.VPCNAME is None):
            ecs.convertVPCNameToId()
        
        REQ_CREATE_SECGROUP = "{ \"security_group\": { \"name\":\"" + OtcConfig.SECUGROUPNAME + "\", \"vpc_id\" : \"" + OtcConfig.VPCID + "\" } }"
        url = ecs.baseurl+ "/v1/" + OtcConfig.PROJECT_ID + "/security-groups"
        ret = utils_http.post(url, REQ_CREATE_SECGROUP)
        return ret

    @staticmethod
    def delete_security_group():
        if not (OtcConfig.VPCNAME is None):
            ecs.convertVPCNameToId()

        if not (OtcConfig.SECUGROUPNAME is None):
            ecs.convertSECUGROUPNameToId()
        
        url = ecs.baseurl+ "/v2.0/" + "/security-groups" + "/"+ OtcConfig.SECUGROUP
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
                    
        sourceIp = "";
        if not OtcConfig.CIDR is None:
            sourceIp = "\", \"remote_ip_prefix\":\"" + OtcConfig.CIDR; 
        remoteGroup = "";
        if not OtcConfig.SOURCE_GROUP_ID is None:
            remoteGroup =  "\", \"remote_group_id\":\"" + OtcConfig.SOURCE_GROUP_ID ;     

        portrange = ""
        if not OtcConfig.PORTMIN is None and not OtcConfig.PORTMAX is None:
            portrange = "\", \"port_range_min\":\"" + OtcConfig.PORTMIN  + "\", \"port_range_max\":\"" ''+ OtcConfig.PORTMAX     
        
        REQ_CREATE_SECGROUPRULE = "{\"security_group_rule\":{ \"direction\":\"" + OtcConfig.DIRECTION +  "\",\"ethertype\":\"" + OtcConfig.ETHERTYPE + "\",  \"protocol\":\""+ OtcConfig.PROTOCOL+ portrange +remoteGroup  + sourceIp+ "\"  , \"security_group_id\":\""+ OtcConfig.SECUGROUP + "\" } }"
        #REQ_CREATE_SECGROUPRULE = "{\"security_group_rule\":{ \"direction\":\"" + OtcConfig.DIRECTION + "\", \"port_range_min\":\"" + OtcConfig.PORTMIN  + "\", \"ethertype\":\"" + OtcConfig.ETHERTYPE + "\", \"port_range_max\":\"" ''+ OtcConfig.PORTMAX+ "\", \"protocol\":\""+ OtcConfig.PROTOCOL+ remoteGroup  + sourceIp+ "\"  , \"security_group_id\":\""+ OtcConfig.SECUGROUP + "\" } }"                
        url = ecs.baseurl+ "/v2.0/security-group-rules" 
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
        if OtcConfig.CREATE_ECS_WITH_PUBLIC_IP == "true":
            PUBLICIPJSON = "\"publicip\": { \"eip\": { \"iptype\": \"5_bgp\", \"bandwidth\": { \"size\": 5, \"sharetype\": \"PER\", \"chargemode\": \"traffic\" } } },"
        PERSONALIZATION = ecs.getPersonalizationJSON()
        REQ_CREATE_VM = "    {                 " + "        \"server\": { " + "        \"availability_zone\": \"" + OtcConfig.AZ + "\",         " + "        \"name\": \"" + OtcConfig.INSTANCE_NAME + "\",            " + "        \"imageRef\": \"" + OtcConfig.IMAGE_ID + "\",             " + "        \"root_volume\": {      " + "            \"volumetype\": \"SATA\"            " + "        }, " + "        \"flavorRef\": \"" + OtcConfig.INSTANCE_TYPE + "\"," + PERSONALIZATION + "        \"vpcid\": \"" + OtcConfig.VPCID + "\",           " + "        \"security_groups\": [         " + "            { " + "                \"id\": \"" + OtcConfig.SECUGROUP + "\"   " + "            }    " + "        ],        " + "        \"nics\": [           " + "            {            " + "                \"subnet_id\": \"" + OtcConfig.SUBNETID + "\"        " + "            }         " + "        ],       " + PUBLICIPJSON + "        \"key_name\": \"" + OtcConfig.KEYNAME + "\",    " + "        \"adminPass\": \"" + OtcConfig.ADMINPASS + "\",   " + "        \"count\": \"" + OtcConfig.NUMCOUNT + "\",   " + "        \"},\": {      " + "            \"__vnc_keymap\": \"de\"    " + "        }   " + "        }   " + "    }       " + "    "
        #print (REQ_CREATE_VM)
        url = ecs.baseurl+ "/v1/" + OtcConfig.PROJECT_ID + "/cloudservers"
        ret = utils_http.post(url, REQ_CREATE_VM)
#        ecs.otcOutputHandler().print_output(json.loads(ret),mainkey = "",listkey={"job_id"} )

        OtcConfig.ECSTASKID  = json.loads(ret)["job_id"]

        if OtcConfig.WAIT_CREATE:
            ecs.getECSJOBList()
            while OtcConfig.ECSCREATEJOBSTATUS in ["RUNNING", "INIT"]:
                sleep(10)
                ecs.getECSJOBList()
                sys.stdout.write('.')
                #sys.stdout.flush()
        
        if "SUCCESS" == OtcConfig.ECSCREATEJOBSTATUS:
            os._exit(1)
            
        print("ECS Creation status: " + OtcConfig.ECSCREATEJOBSTATUS)
        return ret

    @staticmethod
    def getIamToken():
        if OtcConfig.PROJECT_NAME != None: 
            project = "\"name\": \"" + OtcConfig.PROJECT_NAME + "\" " 

        else:
            project = "\"id\": \"" + OtcConfig.PROJECT_ID + "\""
            
        REQ_IAM = "    {" + "        \"auth\": {       " + "        \"identity\": {   " + "            \"methods\": [" + "                \"password\"                             " + "            ],            " + "            \"password\": {                              " + "                \"user\": {                              " + "                    \"name\": \"" + OtcConfig.USERNAME + "\",    " + "                    \"password\": \"" + OtcConfig.PASSWORD + "\"," + "                    \"domain\": {                        " + "                        \"name\": \"" + OtcConfig.DOMAIN + "\"            " + "                    }     " + "                }         " + "            }             " + "        },                " + "        \"scope\": {      " + "            \"project\": {" + project + "            }             " + "        }                 " + "        }                 " + "    }"
        url = "https://"+ OtcConfig.DEFAULT_HOST +":443/v3/auth/tokens";
        ret = utils_http.post(url, REQ_IAM)
        maindata = json.loads(ret)
        OtcConfig.PROJECT_ID = maindata['token']['project']['id'] 

        return ret

    @staticmethod
    def convertFlavorNameToId():
        """ generated source for method convertFlavorNameToId """
        url = ecs.baseurl+ "/v1/" + OtcConfig.PROJECT_ID + "/cloudservers/flavors"
        JSON = utils_http.get(url)        
        parsed  = json.loads(JSON)
        flavors = parsed["flavors"]
        for flavor in flavors:
            if flavor.get("name") == OtcConfig.INSTANCE_TYPE_NAME:
                ret = flavor["id"]
        OtcConfig.INSTANCE_TYPE = ret
    
    @staticmethod
    def convertPublicIpNameToId():
        url = ecs.baseurl+ "/v1/" + OtcConfig.PROJECT_ID + "/publicips"
        JSON = utils_http.get(url)        
        parsed  = json.loads(JSON)
        publicips = parsed["publicips"]
        for publicip in publicips:
            if publicip.get("public_ip_address") == OtcConfig.PUBLICIP:
                ret = publicip["id"]
        OtcConfig.PUBLICIPID = ret

    @staticmethod
    def convertVPCNameToId():
        url = ecs.baseurl+ "/v1/" + OtcConfig.PROJECT_ID + "/vpcs"
        JSON = utils_http.get(url)        
        parsed  = json.loads(JSON)
        vpcs = parsed["vpcs"]
        for vpc in vpcs:
            if vpc.get("name") == OtcConfig.VPCNAME:
                ret = vpc["id"]
        OtcConfig.VPCID = ret

    @staticmethod
    def convertSUBNETNameToId():
        url = ecs.baseurl+ "/v1/" + OtcConfig.PROJECT_ID + "/subnets"
        JSON = utils_http.get(url)
        parsed  = json.loads(JSON)
        subnets = parsed["subnets"]        
        ret = None
        for subnet in subnets:
            if subnet.get("name") == OtcConfig.SUBNETNAME and subnet.get("vpc_id") == OtcConfig.VPCID:
                ret = subnet["id"]
        OtcConfig.SUBNETID = ret        

    @staticmethod
    def convertIMAGENameToId():
        url = ecs.baseurl+ "/v2/images"
        JSON = utils_http.get(url)
        parsed  = json.loads(JSON)
        images = parsed["images"]
        for image in images:
            if image.get("name") == OtcConfig.IMAGENAME:
                ret = image["id"]
        OtcConfig.IMAGE_ID = ret

    @staticmethod
    def convertINSTANCENameToId():
        url = ecs.baseurl+ "/v2/" + OtcConfig.PROJECT_ID + "/servers"
        JSON = utils_http.get(url)
        parsed  = json.loads(JSON)
        servers = parsed["servers"]

        for server in servers:
            if server.get("name") == OtcConfig.INSTANCE_NAME:
                ret = server["id"]
        OtcConfig.INSTANCE_ID = ret        
        
    @staticmethod
    def convertSECUGROUPNameToId():
        url = ecs.baseurl+ "/v1/" + OtcConfig.PROJECT_ID + "/security-groups"
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
        """ generated source for method getVolumeList """
        url = ecs.baseurl+ "/v2/" + OtcConfig.PROJECT_ID + "/cloudvolumes"+ "/detail"
        ret = utils_http.get( url )
        ecs.otcOutputHandler().printLevel2(ret, "volumes", {"id", "name", "volume_type", "size", "status", "bootable", "availability_zone", "limit", "attachments", "source_volid", "snapshot_id", "description", "created_at"})
        return ret


    @staticmethod
    def create_volume():
        """ generated source for method CreateVolume """        
        REQ_CREATE_CLOUDVOLUMES = "{ \"volume\": { \"backup_id\": " + OtcConfig.SNAPSHOTID + ", " + "\"count\": " + OtcConfig.NUMCOUNT + ", \"availability_zone\": \"" + OtcConfig.AZ + "\",\"description\": \"" + OtcConfig.VOLUME_NAME + "\", \"size\": " + OtcConfig.VOLUME_SIZE + ", \"name\": \"" + OtcConfig.VOLUME_NAME + "\", \"imageRef\": " + "null" + ", \"volume_type\": \"" + OtcConfig.VOLUME_TYPE + "\" } }"
        #print REQ_CREATE_CLOUDVOLUMES
        url = ecs.baseurl+ "/v2/" + OtcConfig.PROJECT_ID + "/cloudvolumes"
        ret = utils_http.post(url, REQ_CREATE_CLOUDVOLUMES)
        print(ret)
        return ret


    @staticmethod
    def attach_volume():
        """ generated source for method AttachVolume """        
        REQ_ATTACH_CLOUDVOLUMES = "{ \"volumeAttachment\": { \"volumeId\": \"" + OtcConfig.VOLUME_ID + "\", \"device\": \"" + OtcConfig.EVS_DEVICE + "\" } }"
        url = ecs.baseurl+ "/v1/" + OtcConfig.PROJECT_ID + "/cloudservers/" + OtcConfig.INSTANCE_ID + "/attachvolume"
        ret = utils_http.post(url, REQ_ATTACH_CLOUDVOLUMES)
        print(ret)
        return ret


    @staticmethod
    def detach_volume():
        """ generated source for method DetachVolume """
        url = ecs.baseurl+ "/v1/" + OtcConfig.PROJECT_ID + "/cloudservers/" + OtcConfig.INSTANCE_ID + "/detachvolume/" + OtcConfig.VOLUME_ID
        ret = utils_http.delete(url)
        print(ret)
        return ret

    @staticmethod
    def delete_volume():
        url = ecs.baseurl+ "/v2/" + OtcConfig.PROJECT_ID + "/cloudvolumes" + "/" + OtcConfig.VOLUME_ID
        ret = utils_http.delete(url)
        print(ret)
        return ret


    @staticmethod
    def describe_quotas():
        url = ecs.baseurl+ "/v1/" + OtcConfig.PROJECT_ID + "/cloudservers/limits"
        ret = utils_http.get(url)
        ecs.otcOutputHandler().print_output(ret, mainkey="absolute")
        return ret

 
    @staticmethod
    def describe_snapshots():
        """ vm backup list """
        url = ecs.baseurl+ "/v2/" + OtcConfig.PROJECT_ID + "/backups/detail"
        ret = utils_http.get(url)        
        ecs.otcOutputHandler().printJsonTableTransverse(ret)
        return ret


    @staticmethod
    #TODO: restore backup disk this is a create volume action
    def RestoreBackupDisk():
        REQ_RESTORE_BACKUP = "{ \"restore\":{ \"volume_id\":\"" + OtcConfig.VOLUME_ID + "\" } }"
        #print REQ_RESTORE_BACKUP
        url = ecs.baseurl+ "/v2/" + OtcConfig.PROJECT_ID + "/cloudbackups" +"/" + OtcConfig.SNAPSHOTID + "/restore"
        ret = utils_http.post(url + "/" + OtcConfig.SNAPSHOTID + "/restore", REQ_RESTORE_BACKUP)
        print(ret)
        return ret


    @staticmethod
    def delete_snapshot():        
        url = ecs.baseurl+ "/v2/" + OtcConfig.PROJECT_ID + "/cloudbackups"+ "/" + OtcConfig.SNAPSHOTID
        ret = utils_http.post( url , "")
        print(ret)
        return ret


    @staticmethod
    def create_snapshot():
        REQ_CREATE_BACKUP = "{ \"backup\":{ \"" + "volume_id\":\"" + OtcConfig.VOLUME_ID + "\", " + "\"name\":\"" + OtcConfig.DESCRIPTION + "\", \"description\":\"" + OtcConfig.DESCRIPTION + "\" } }"
        #print REQ_CREATE_BACKUP
        url = ecs.baseurl+ "/v2/" + OtcConfig.PROJECT_ID + "/cloudbackups"
        ret = utils_http.post(url, REQ_CREATE_BACKUP)
        print (ret)
        return ret

