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

 
    
class ecs(otcpluginbase):
    ar = {}    
    
    @staticmethod
    def otcOutputHandler(): 
        return getplugin(OtcConfig.OUTPUT_FORMAT)
 
    def otctype(self):
        return "func" 

    @staticmethod 
    @otcfunc(plugin_name=__name__,
             desc="Describe instances",
             examples=[
                       {'Describe instances":"otc ecs describe_instances'},
                       {'Detailed information of specific VM instance (JSON): otc ecs describe_instances --instance-ids 097da903-ab95-44f3-bb5d-5fc08dfb6cc3 --output json     '}
                       ],
             args = [ 
                       arg(    '--instance-name',     dest='INSTANCE_NAME',     help='Instance name of the VM'),
                       arg(    '--instance-id',     dest='INSTANCE_ID',     help='Instance ID of the VM')

                ])    
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
    @otcfunc(plugin_name=__name__,
             desc="List VPCs",
             examples=[
                       {'List VPCs":"otc ecs describe_vpcs'}
                       ]
             )
    def describe_vpcs():
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/vpcs"
        ret = utils_http.get(url)
        ecs.otcOutputHandler().print_output(ret, mainkey = "vpcs", listkey={"id", "name", "status", "cidr"})
        return ret


    @staticmethod   
    @otcfunc(plugin_name=__name__,
             desc="List addresses",
             examples=[
                       {'List addresses":"otc ecs describe_addresses'}
                       ]
             )
    def describe_addresses():
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/publicips"        
        ret = utils_http.get(url)
        ecs.otcOutputHandler().print_output(ret, mainkey="publicips", listkey={"id", "status", "public_ip_address", "private_ip_address", "type", "create_time", "bandwidth_size"})
        return ret

    @staticmethod   
    @otcfunc(plugin_name=__name__,
             desc="List bandwiths",
             examples=[
                       {'List bandwiths":"otc ecs describe_bandwiths'}
                       ])
    def describe_bandwiths():
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/bandwidths"        
        ret = utils_http.get(url)
        ecs.otcOutputHandler().print_output(ret, mainkey="bandwidths", listkey={"id", "name", "publicip_info", "size"})
        return ret

    @staticmethod   
    @otcfunc(plugin_name=__name__,
             desc="List private addresses",
             examples=[
                       {'List private addresses":"otc ecs describe_private_addresses --vpc-name myvpc --subnet-name subnettest'}
                       ],
             args = [
                    arg(    '--vpc-id',    dest='VPCID',     help='Id of the VPC will use during VM creation'),    
                    arg(    '--vpc-name',    dest='VPCNAME',     help='Name of the VPC reference will use during VM creation'),
                    arg('--subnet-name',    dest='SUBNETNAME',     help='Name of the subnet reference will use during VM creation'),
                    arg(  '--subnet-id',    dest='SUBNETID',     help='Id of the subnet will use during VM creation')
                    ])
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
    @otcfunc(plugin_name=__name__,
             desc="List VPCs",
             examples=[
                       {'List security groups":"otc ecs describe_security_groups'},
                       {'List security groups":"otc ecs describe_security_groups --group-names test2'}
                       ],
             args = [
                    arg(    '--group-names',    dest='SECUGROUPNAME',     help='Name of the security group'),
                    arg(    '--security-group-ids',    dest='SECUGROUP',     help='Id of the security group')             ]) 
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
    @otcfunc(plugin_name=__name__,
             desc="List subnets",
             examples=[
                       {'List subnets":"otc ecs describe_subnets'}
                       ])
    def describe_subnets():
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/subnets"
        ret = utils_http.get(url)
        ecs.otcOutputHandler().print_output(ret, mainkey="subnets", listkey={"id", "name", "cidr", "status", "vpc_id", "gateway_ip", "primary_dns", "availability_zone"})
        return ret

    @staticmethod 
    @otcfunc(plugin_name=__name__,
             desc="Describe network interfaces",
             examples=[
                       {'Describe network interfaces":"otc ecs describe_network_interfaces --instance-name testinstance'}
                       ],
             args = [ 
                       arg(    '--instance-name',     dest='INSTANCE_NAME',     help='Instance name of the VM'),

                ])    
    def describe_network_interfaces(): 
        if not OtcConfig.INSTANCE_NAME is None:
            ecs.convertINSTANCENameToId() 
        
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v2/" + OtcConfig.PROJECT_ID + "/servers/" + OtcConfig.INSTANCE_ID + "/os-interface"
        
        ret = utils_http.get(url)
#        print (ret)
        ecs.otcOutputHandler().print_output(ret, mainkey="interfaceAttachments", listkey={"port_state", "fixed_ips", "port_id", "net_id", "mac_addr"})
        return ret




    @staticmethod    
    @otcfunc(plugin_name=__name__,
             desc="List images",
             examples=[
                       {'List images":"otc ecs describe_images'}
                       ])      
    def describe_images():
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v2/cloudimages"
        ret = utils_http.get(url)
        ecs.otcOutputHandler().print_output(ret, mainkey="images", listkey={"id", "name", "__os_type", "updated_at", "deleted"})
        return ret


    @staticmethod     
    @otcfunc(plugin_name=__name__,
             desc="List flavors",
             examples=[
                       {'List flavors":"otc ecs describe_flavors'}
                       ])  
    def describe_flavors():
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/cloudservers/flavors"
        ret = utils_http.get(url)
        ecs.otcOutputHandler().print_output(ret, mainkey="flavors", listkey= {"id", "name", "vcpus", "ram", "disk", "swap"})
        return ret

    @staticmethod     
    @otcfunc(plugin_name=__name__,
             desc="List key-pairs",
             examples=[
                       {'List key-pairs":"otc ecs describe_key_pairs'}
                       ])  
    def describe_key_pairs():
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v2/" + OtcConfig.PROJECT_ID + "/os-keypairs"
        ret = utils_http.get( url )    
        ecs.otcOutputHandler().print_output(ret, mainkey="keypairs", subkey="keypair", listkey={"name", "fingerprint", "public_key"})        
        return ret


    @staticmethod 
    @otcfunc(plugin_name=__name__,
             desc="Create key-pairs",
             examples=[
                       {"Create key-pairs":"otc dms create_key_pair --key-name testkey --public-key 1234"}                       
                       ],
             args = [ 
                    arg(    '--key-name',     dest='KEYNAME',     help='SSH key name| S3 Object key'),
                    arg(    '--public-key',     dest='PUBLICKEY',     help='Import public key for SSH keypairs')             
                ]                
            )        
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
    @otcfunc(plugin_name=__name__,
             desc="Allocate address",
             examples=[
                       {'Allocate address ":"otc ecs allocate-address'}
                       ],
             args = [])   
    def allocate_address():
        REQ_CREATE_PUBLICIP = "{\"publicip\":{\"type\":\"5_bgp\"},\"bandwidth\":{\"name\":\"apiTest\",\"size\":5,\"share_type\":\"PER\",\"charge_mode\":\"traffic\"}}"
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/publicips"
        ret = utils_http.post(url, REQ_CREATE_PUBLICIP)
        # print( ret )
        maindata = json.loads(ret)
        if "code" in  maindata:            
            print("Can not create:" +maindata["message"])  
            os._exit( 1 )             
                            
        ecs.otcOutputHandler().print_output(ret, mainkey="publicip")
        return ret

    @staticmethod   
    @otcfunc(plugin_name=__name__,
             desc="Release address",
             examples=[
                       {'Release address ":"otc ecs release-address'}
                       ],
             args = [
                    arg(    '--public-ip',    dest='PUBLICIP',     help='Public IP for association')
                  ])         
    def release_address():
        if not (OtcConfig.PUBLICIP is None):
            ecs.convertPublicIpNameToId()            
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/publicips" + \
        "/" + OtcConfig.PUBLICIPID
        ret = utils_http.delete(url)
        print(ret)
        return ret

    @staticmethod     
    @otcfunc(plugin_name=__name__,
             desc="Release private address",
             examples=[
                       {'Release private address ":"otc ecs release-private-address --private-ip-id 097da903-ab95-44f3-bb5d-5fc08dfb6cc3'}
                       ],
             args = [
                    arg(    '--private-ip-id',    dest='PRIVATEIPID',     help='Private IP Id')
                  ])       
    def release_private_address():
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/privateips" + OtcConfig.PRIVATEIPID
        ret = utils_http.delete(url)
        print(ret)
        return ret


    @staticmethod    
    @otcfunc(plugin_name=__name__,
             desc="Associate address",
             examples=[
                       {'Associate address ":"otc ecs associate-address'}
                       ])
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
    @otcfunc(plugin_name=__name__,
             desc="Resize instance",
             examples=[
                       {'Resize instance":"otc ecs resize-instance --instance-ids 097da903-ab95-44f3-bb5d-5fc08dfb6cc3 --instance-type testinstancetype'},
                        {'Resize instance":"otc ecs resize-instance --instance-name testinstance --instance-type testinstancetype'}
                       ],
             args = [ 
                       arg(    '--instance-ids',     dest='INSTANCE_ID',     help='Instance Id of the VM'),
                       arg(    '--instance-name',     dest='INSTANCE_NAME',     help='Instance name of the VM'),
                       arg(    '--instance-type',    dest='INSTANCE_TYPE_NAME',     help='Flavor type of the VM')
                ])    
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
    @otcfunc(plugin_name=__name__,
             desc="Delete key-pairs",
             examples=[
                       {"Delete key-pairs":"otc dms delete-key-pair --key-name testkey"}                       
                       ],
             args = [ 
                    arg(    '--key-name',     dest='KEYNAME',     help='SSH key name| S3 Object key')]
                    )   
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
        if OtcConfig.DEBUG:
            print ret
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
    @otcfunc(plugin_name=__name__,
             desc="Start VM instances",
             examples=[
                       {'Start VM instance":"otc ecs start-instances --instance-name testinstance '}
                       ],
             args = [ 
                       arg(    '--instance-name',     dest='INSTANCE_NAME',     help='Instance name of the VM'),
                       arg(    '--instance-ids',     dest='INSTANCE_ID',     help='Instance Id of the VM')
                ])
    def start_instances():
        OtcConfig.ECSACTION = "os-start"
        ecs.ECSAction()

    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="Stop VM instances",
             examples=[
                       {'Stop VM instance":"otc ecs stop-instances --instance-name testinstance '}
                       ],
             args = [ 
                       arg(    '--instance-name',     dest='INSTANCE_NAME',     help='Instance name of the VM'),
                       arg(    '--instance-ids',     dest='INSTANCE_ID',     help='Instance Id of the VM')
					   ])
    def stop_instances():
        OtcConfig.ECSACTION = "os-stop"
        ecs.ECSAction()

    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="Delete VM instance (public ip + EVS also)",
             examples=[
                       {'Delete VM instance (public ip + EVS also)":"otc ecs delete-instances --instance-name testinstance'}
                       ],
             args = [ 
                       arg(    '--instance-name',     dest='INSTANCE_NAME',     help='Instance name of the VM')
                ])       
    ### DELETE_PUBLICIP
    ### DELETE_VOLUME
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
    @otcfunc(plugin_name=__name__,
             desc="Create VPC",
             examples=[
                       {'Create VPC": "otc ecs create-vpc --vpc-name testvpc'}
                       ],
             args = [ 
                arg(    '--vpc-name',    dest='VPCNAME',     help='Name of the VPC reference will use during VM creation'),
                arg(    '--cidr',    dest='CIDR',     help='CIDR of the subnet will use during subnet creation')]
                )
    def create_vpc():
        REQ_CREATE_VPC = "{ \"vpc\": { \"name\": \"" + OtcConfig.VPCNAME + "\", \"cidr\": \"" + OtcConfig.CIDR + "\" } }"
        
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/vpcs"
        ret = utils_http.post(url, REQ_CREATE_VPC)
        print(ret)
        return ret

    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="Delete VPC",
             examples=[
                       {'Delete VPC":"otc ecs delete-vpc --vpc-name testvpc'}
                       ],
             args = [ 
                arg(    '--vpc-name',    dest='VPCNAME',     help='Name of the VPC reference will use during VM creation'),
                arg(    '--vpc-id',    dest='VPCID',     help='Id of the VPC will use during VM creation')
                ]
                )
    def delete_vpc():
        if not (OtcConfig.VPCNAME is None):
            ecs.convertVPCNameToId()

        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/vpcs/" + OtcConfig.VPCID    
        ret = utils_http.delete(url)
        print(ret)
        return ret

    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="Create new subnet for VPC",
             examples=[
                       {'Create new subnet for VPC":"otc ecs create-subnet --subnet-name subnettest --cidr 192.168.1.0/16 --gateway-ip 192.168.1.2 --primary-dns 8.8.8.8 --secondary-dns 8.8.4.4 --availability-zone eu-de-01 --vpc-name default-vpc '}
                       ],
             args = [ 
                    arg(    '--subnet-name',    dest='SUBNETNAME',     help='Name of the subnet reference will use during VM creation'),
                    arg(    '--cidr',    dest='CIDR',     help='CIDR of the subnet will use during subnet creation'),
                    arg('--vpc-name',dest='VPCNAME',     help='Name of the VPC reference will use during VM creation'),
                    arg(      '--vpc-id',    dest='VPCID',     help='Id of the VPC will use during VM creation'),
                    arg(    '--gateway-ip',    dest='GWIP',     help='Gateway Ip of the subnet'),
                    arg(    '--primary-dns',    dest='PRIMARYDNS',     help='Primary dns of the subnet'),
                    arg(    '--secondary-dns',    dest='SECDNS',     help='Secondary dns of the subnet'),
                    arg(    '--availability-zone',    dest='AZ',     help='Availability-zone definition')

                    ]
                )
    def create_subnet():
        if not (OtcConfig.VPCNAME is None):
            ecs.convertVPCNameToId()
            
        #REQ_CREATE_SUBNET = "{ \"subnet\": { \"name\": \"" + OtcConfig.SUBNETNAME + "\", \"cidr\": \"" + OtcConfig.CIDR + "\", \"gateway_ip\": \"" + OtcConfig.GWIP + "\", \"dhcp_enable\": \"true\", \"primary_dns\": \"" + OtcConfig.PRIMARYDNS + "\", \"secondary_dns\": \"" + OtcConfig.SECDNS + "\", \"availability_zone\":\"" + OtcConfig.AZ + "\", \"vpc_id\":\"" + OtcConfig.VPCID + "\" } }"
        req = utils_templates.create_request("create_subnet")
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/subnets"        
        ret = utils_http.post(url, req)
        print(ret)
        return ret

    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="Delete subnet",
             examples=[
                       {'Delete subnet":"otc ecs delete-subnet --subnet-name testsubnet'}
                       ],
             args = [ 
                    arg(    '--subnet-name',    dest='SUBNETNAME',     help='Name of the subnet reference will use during VM creation'),
                    arg(    '--subnet-id',    dest='SUBNETID',     help='Id of the subnet will use during VM creation'),

                ]
                )
    def delete_subnet():
        if OtcConfig.SUBNETNAME:
            ecs.convertSUBNETNameToId()
        
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/subnets" + OtcConfig.SUBNETID
        ret = utils_http.delete(url)
        return ret



    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="Create new network interface",
             examples=[
                       ],
             args = [ 
                    arg(    '--instance-name',     dest='INSTANCE_NAME',     help='Instance name of the VM'),
                    arg(    '--instance-ids',     dest='INSTANCE_ID',     help='Instance Id of the VM'),
                    arg(    '--subnet-name',    dest='SUBNETNAME',     help='Name of the subnet reference will use during VM creation'),
                    arg(    '--subnet-id',    dest='SUBNETID',     help='Id of the subnet will use during VM creation'),
                    arg(    '--group-names',    dest='SECUGROUPNAME',     help='Name of the security group'),
                    arg(    '--security-group-ids',    dest='SECUGROUP',     help='Id of the security group')
                    ])
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
    @otcfunc(plugin_name=__name__,
             desc="Create new security group",
             examples=[
                       {'Create new security group":"otc ecs create-security-group --group-names test2 --vpc-name default-vpc'}
                       ],             
             args = [ 
                    arg(    '--vpc-name',    dest='VPCNAME',     help='Name of the VPC reference will use during VM creation'),
                    arg(      '--vpc-id',    dest='VPCID',     help='Id of the VPC will use during VM creation'),
                    arg(    '--group-names',    dest='SECUGROUPNAME',     help='Name of the security group')
                    ])    
    def create_security_group():
        if not (OtcConfig.VPCNAME is None):
            ecs.convertVPCNameToId()
        
        req = utils_templates.create_request("add_sg")
      
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v2/" + OtcConfig.PROJECT_ID + "/os-security-groups"
        ret = utils_http.post(url, req)
        return ret

    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="Delete security group",
             examples=[
                       {'Delete security group":"otc ecs delete-security-group --group-names test2 --vpc-name default-vpc'}
                       ],
             args = [ 
                    arg(    '--vpc-name',    dest='VPCNAME',     help='Name of the VPC reference will use during VM creation'),
                    arg(      '--vpc-id',    dest='VPCID',     help='Id of the VPC will use during VM creation'),
                    arg(    '--group-names',    dest='SECUGROUPNAME',     help='Name of the security group'),
                    arg(    '--security-group-ids',    dest='SECUGROUP',     help='Id of the security group')
                    ])
    def delete_security_group():
        if not (OtcConfig.VPCNAME is None):
            ecs.convertVPCNameToId()

        if not (OtcConfig.SECUGROUPNAME is None):
            ecs.convertSECUGROUPNameToId()
        
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v2.0/security-groups" + "/"+ OtcConfig.SECUGROUP
        ret = utils_http.delete(url)
        return ret


    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="Add new incomming rule to security-group",
             examples=[
                       {'Add new incomming rule to security-group":"otc ecs authorize-security-group-ingress --group-name test2 --vpc-name default-vpc --protocol tcp --ethertype IPv4 --portmin 22 --portmax 25      '}
                       ], 
             args = [ 
                    arg(    '--vpc-name',    dest='VPCNAME',     help='Name of the VPC reference will use during VM creation'),
                    arg(      '--vpc-id',    dest='VPCID',     help='Id of the VPC will use during VM creation'),
                    arg(    '--group-names',    dest='SECUGROUPNAME',     help='Name of the security group'),
                    arg(    '--security-group-ids',    dest='SECUGROUP',     help='Id of the security group'),
                    arg(    '--direction',    dest='DIRECTION',     help='Direction of the security group rule'),
                    arg(    '--portmin',    dest='PORTMIN',     help='Lower por of the specific security group rule'),
                    arg(    '--portmax',    dest='PORTMAX',     help='Upper  port of the specific security group rule'),
                    arg(    '--protocol',    dest='PROTOCOL',     help='Protocol of the specific security group rule'),
                    arg(    '--ethertype',    dest='ETHERTYPE',     help='Ethertype of the specific security group rule'),
                    arg(    '--cidr',    dest='CIDR',     help='CIDR of the subnet will use during subnet creation'),
                    arg(    '--source-group-id',    dest='SOURCE_GROUP_ID',     help='Id of Source security group'),
                    arg(    '--source-group',    dest='SOURCE_GROUP',     help='Name of Source security group')
                    ])
    def authorize_security_group_ingress():
        OtcConfig.DIRECTION = "ingress"
        ecs._secgrouprulecreate()

    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="Add new outcomming rule to security-group",
             examples=[
                       {'Add new outcomming rule to security-group":"otc ecs authorize-security-group-ingress --group-name test2 --vpc-name default-vpc --protocol tcp --ethertype IPv4 --portmin 22 --portmax 25      '}
                       ], 
             args = [ 
                    arg(    '--vpc-name',    dest='VPCNAME',     help='Name of the VPC reference will use during VM creation'),
                    arg(      '--vpc-id',    dest='VPCID',     help='Id of the VPC will use during VM creation'),
                    arg(    '--group-names',    dest='SECUGROUPNAME',     help='Name of the security group'),
                    arg(    '--security-group-ids',    dest='SECUGROUP',     help='Id of the security group'),
                    arg(    '--direction',    dest='DIRECTION',     help='Direction of the security group rule'),
                    arg(    '--portmin',    dest='PORTMIN',     help='Lower por of the specific security group rule'),
                    arg(    '--portmax',    dest='PORTMAX',     help='Upper  port of the specific security group rule'),
                    arg(    '--protocol',    dest='PROTOCOL',     help='Protocol of the specific security group rule'),
                    arg(    '--ethertype',    dest='ETHERTYPE',     help='Ethertype of the specific security group rule'),
                    arg(    '--cidr',    dest='CIDR',     help='CIDR of the subnet will use during subnet creation'),
                    arg(    '--source-group-id',    dest='SOURCE_GROUP_ID',     help='Id of Source security group'),
                    arg(    '--source-group',    dest='SOURCE_GROUP',     help='Name of Source security group')
                    ])
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
    @otcfunc(plugin_name=__name__,
             desc="Create new VM instance with injected SSH keypair, with public ip, additional file injection, wait instance created and running",
             examples=[
                       {'Create new VM instance with injected SSH keypair, with public ip, additional file injection, wait instance created and running":"otc ecs run-instances --count 1  --admin-pass yourpass123! --instance-type c1.medium --instance-name instancename --image-name Standard_CentOS_6.7_latest --subnet-name testsubnet --vpc-name testvpc --group-name testsecgroup  --key-name testsshkeypair --file1 /otc/a=/otc/a --associate-public-ip-address  --wait-instance-running'}
                       ], 
             args = [ 
                    arg(    '--vpc-name',    dest='VPCNAME',     help='Name of the VPC reference will use during VM creation'),
                    arg(      '--vpc-id',    dest='VPCID',     help='Id of the VPC will use during VM creation'),
                    arg(    '--group-names',    dest='SECUGROUPNAME',     help='Name of the security group'),
                    arg(    '--security-group-ids',    dest='SECUGROUP',     help='Id of the security group'),
                    
                    arg(    '--subnet-name',    dest='SUBNETNAME',     help='Name of the subnet reference will use during VM creation'),
                    arg(    '--availability-zone',    dest='AZ',     help='Availability-zone definition'),
                    arg(    '--size',    dest='VOLUME_SIZE',     help='Size of the EVS disk'),
                    arg(    '--volume-type',    dest='VOLUME_TYPE',     help='Volume type of the EVS disk [SSD SAS SATA]'),
                    arg(    '--data-volumes',    dest='DATA_VOLUMES',     help='Attach data volumes while creating ECS(eg: SSD:10,SATA:20)'),
                    arg(    '--user-data',    dest='USER_DATA_PATH',     help='Path to user-data file which will be used for cloud-init'),
                    arg( '--instance-type',    dest='INSTANCE_TYPE_NAME',     help='Flavor type of the VM'),
                    arg( '--image-name',    dest='IMAGENAME',     help='Name of the image reference will used during VM creation'),
                    arg( '--image-id',    dest='IMAGE_ID',     help='Id of the image reference will use during VM creation'),
                    arg(    '--instance-name',     dest='INSTANCE_NAME',     help='Instance name of the VM'),
                    arg(    '--file1',     dest='FILE1',     help='Name of the #1 file to be injected to VM. Format: target=source'),
                    arg(    '--file2',     dest='FILE2',     help='Name of the #2 file to be injected to VM. Format: target=source'),
                    arg(    '--file3',    dest='FILE3',     help='Name of the #3 file to be injected to VM. Format: target=source'),
                    arg(    '--file4',    dest='FILE4',     help='Name of the #4 file to be injected to VM. Format: target=source'),
                    arg(    '--file5',    dest='FILE5',     help='Name of the #5 file to be injected to VM. Format: target=source'),
                    arg(  '--subnet-name',    dest='SUBNETNAME',     help='Name of the subnet reference will use during VM creation'),
                    arg(  '--subnet-id',    dest='SUBNETID',     help='Id of the subnet will use during VM creation'),


                    arg(    '--admin-pass',     dest='ADMINPASS',     help='Admin password of the started VM'),
                    arg('--count',    dest='NUMCOUNT',     help='Number of VM will be created'), 
                    arg(    '--key-name',     dest='KEYNAME',     help='SSH key name| S3 Object key'),
                    arg(    '--wait-instance-running',     dest='WAIT_CREATE',     help='Wait instance running (only for run-instance command)')
                    ])
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
        
        if OtcConfig.DATA_VOLUMES is not None:
            DATA_VOLUMES = OtcConfig.DATA_VOLUMES
            volumes = DATA_VOLUMES.split(',')
            DATA_VOLUMES = []
            if len(volumes):
                for v in volumes:
                    data = v.split(':')
                    if len(data):
                        DATA_VOLUMES.append("{\"volumetype\":\"%s\",\"size\":%s}" % (data[0], data[1]))
            if len(DATA_VOLUMES):
                DATA_VOLUMES = ','.join(DATA_VOLUMES)
            else:
                DATA_VOLUMES = ''
            OtcConfig.DATA_VOLUMES = DATA_VOLUMES

        REQ_CREATE_VM=utils_templates.create_request("create_vm")        
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/cloudservers"
        
        #print REQ_CREATE_VM
        ret = utils_http.post(url, REQ_CREATE_VM)       
        #print (ret)  
        if OtcConfig.DEBUG:
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
#        if OtcConfig.PROJECT_NAME != None: 
#            project = "\"name\": \"" + OtcConfig.PROJECT_NAME + "\" " 
#
#        else:
#            project = "\"id\": \"" + OtcConfig.PROJECT_ID + "\""
            
        #REQ_IAM = "    {" + "        \"auth\": {       " + "        \"identity\": {   " + "            \"methods\": [" + "                \"password\"                             " + "            ],            " + "            \"password\": {                              " + "                \"user\": {                              " + "                    \"name\": \"" + OtcConfig.USERNAME + "\",    " + "                    \"password\": \"" + OtcConfig.PASSWORD + "\"," + "                    \"domain\": {                        " + "                        \"name\": \"" + OtcConfig.DOMAIN + "\"            " + "                    }     " + "                }         " + "            }             " + "        },                " + "        \"scope\": {      " + "            \"project\": {" + project + "            }             " + "        }                 " + "        }                 " + "    }"
        REQ_IAM = utils_templates.create_request("iam_token")
        
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
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v2/cloudimages"
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
    @otcfunc(plugin_name=__name__,
             desc="Describe volumes",
             examples=[
                       {'Describe volumes":"otc ecs describe_volumes'}
                       ],
             args = [ 
                ])   
    def describe_volumes():
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v2/" + OtcConfig.PROJECT_ID + "/cloudvolumes"+ "/detail"
        ret = utils_http.get( url )
        ecs.otcOutputHandler().print_output(ret,  mainkey = "volumes", listkey= {"id", "name", "volume_type", "size", "status", "bootable", "availability_zone", "limit", "attachments", "source_volid", "snapshot_id", "description", "created_at"})
        return ret

    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="List volumes",
             examples=[
                       {'List volumes":"otc ecs list_volumes --instance-name testinstace'}
                       ],
             args = [ 
                       arg(    '--instance-name',     dest='INSTANCE_NAME',     help='Instance name of the VM'),

                ]) 
    def list_volumes():
        if not OtcConfig.INSTANCE_NAME is None:
            ecs.convertINSTANCENameToId() 

        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v2/" + OtcConfig.PROJECT_ID + "/servers/"+ OtcConfig.INSTANCE_ID + "/os-volume_attachments"
        ret = utils_http.get( url )
        print (ret)
        # TODO: output fix need  
        #ecs.otcOutputHandler().print_output(ret,  mainkey = "volumes", listkey= {"id", "name", "volume_type", "size", "status", "bootable", "availability_zone", "limit", "attachments", "source_volid", "snapshot_id", "description", "created_at"})
        return ret


    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="Create volume",
             examples=[
                       {'Create volume from snapshot":"otc ecs create-volume   --volume-id b197b8af-fe63-465f-97b6-5e5b89exxx --snapshot-id 0c942ff7-454e-xxxx'},
                        {'Create volume":"otc ecs create-volume   --count 1 --volume-name myvolume  --size 100 --volume-type SATA      Create new Volume [type: SSD,SAS,SATA]'}
                       ],
             args = [ 
                    arg(    '--snapshot-id',    dest='SNAPSHOTID',     help='Snapshot id of the backup'),
                    arg('--count',    dest='NUMCOUNT',     help='Number of VM will be created'), 
                    arg(    '--availability-zone',    dest='AZ',     help='Availability-zone definition'),
                    arg(    '--size',    dest='VOLUME_SIZE',     help='Size of the EVS disk'),
                    arg(    '--volume-type',    dest='VOLUME_TYPE',     help='Volume type of the EVS disk [SSD SAS SATA]'),
                    arg(    '--volume-name',    dest='VOLUME_NAME',     help='Volume name of the EVS disk')
                ]) 
    def create_volume():        
        REQ_CREATE_CLOUDVOLUMES = "{ \"volume\": { \"backup_id\": " + OtcConfig.SNAPSHOTID + ", " + "\"count\": " + OtcConfig.NUMCOUNT + ", \"availability_zone\": \"" + OtcConfig.AZ + "\",\"description\": \"" + OtcConfig.VOLUME_NAME + "\", \"size\": " + OtcConfig.VOLUME_SIZE + ", \"name\": \"" + OtcConfig.VOLUME_NAME + "\", \"imageRef\": " + "null" + ", \"volume_type\": \"" + OtcConfig.VOLUME_TYPE + "\" } }"
        #print REQ_CREATE_CLOUDVOLUMES
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v2/" + OtcConfig.PROJECT_ID + "/cloudvolumes"
        ret = utils_http.post(url, REQ_CREATE_CLOUDVOLUMES)
        print(ret)
        return ret


    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="Attach volume",
             examples=[
                       {'Attach volume":"otc ecs attach-volume   --instance-ids f344b625-6f73-44f8-ad56-9fcb05a523c4 --volume-id 8c0de9a7-9f61-4613-a68a-21f456cb7298'}
                       ],
             args = [ 
                    arg(    '--volume-id',     dest='VOLUME_ID',     help='Volume Id of the EVS volume'),
                    arg(    '--device',     dest='EVS_DEVICE',     help='Device of the EVS volume')
                ]) 
    def attach_volume():
        """ generated source for method AttachVolume """        
        REQ_ATTACH_CLOUDVOLUMES = "{ \"volumeAttachment\": { \"volumeId\": \"" + OtcConfig.VOLUME_ID + "\", \"device\": \"" + OtcConfig.EVS_DEVICE + "\" } }"
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/cloudservers/" + OtcConfig.INSTANCE_ID + "/attachvolume"
        ret = utils_http.post(url, REQ_ATTACH_CLOUDVOLUMES)
        print(ret)
        return ret


    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="Detach volume",
             examples=[
                       {'Detach volume":"otc ecs detach-volume   --instance-ids f344b625-6f73-44f8-ad56-9fcb05a523c4 --volume-id 8c0de9a7-9f61-4613-a68a-21f456cb7298'}
                       ],
             args = [ 
                    arg(    '--volume-id',     dest='VOLUME_ID',     help='Volume Id of the EVS volume'),
                    arg(    '--instance-name',     dest='INSTANCE_NAME',     help='Instance name of the VM'),
                    arg(    '--instance-ids',     dest='INSTANCE_ID',     help='Instance Id of the VM')
                ]) 
    def detach_volume():
        """ generated source for method DetachVolume """
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/cloudservers/" + OtcConfig.INSTANCE_ID + "/detachvolume/" + OtcConfig.VOLUME_ID
        ret = utils_http.delete(url)
        print(ret)
        return ret

    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="Delete volume",
             examples=[
                       {'Delete volume":"otc ecs delete-volume --volume-id 8c0de9a7-9f61-4613-a68a-21f456cb7298'}
                       ],
             args = [ 
                    arg(    '--volume-id',     dest='VOLUME_ID',     help='Volume Id of the EVS volume')
                    ])
    def delete_volume():
        if not OtcConfig.VOLUME_NAME is None:
            ecs.convertVOLUMENameToId() 
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v2/" + OtcConfig.PROJECT_ID + "/cloudvolumes" + "/" + OtcConfig.VOLUME_ID    
        ret = utils_http.delete(url)
        print(ret)
        return ret


    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="Describe quotas",
             examples=[
                       {'Describe quotas":"otc ecs describe-quotas'}
                       ],
             args = [ 
                    ])
    def describe_quotas():
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v1/" + OtcConfig.PROJECT_ID + "/cloudservers/limits"
        ret = utils_http.get(url)
        ecs.otcOutputHandler().print_output(ret, mainkey="absolute")
        return ret

 
    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="Describe snapshots",
             examples=[
                       {'Describe snapshots":"otc ecs describe-snapshots'}
                       ],
             args = [ 
                    ])
    def describe_snapshots():    
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v2/" + OtcConfig.PROJECT_ID + "/backups/detail"
        ret = utils_http.get(url)               
        ecs.otcOutputHandler().print_output(ret, mainkey = "backups", listkey={"name","id","size","status","description","created_at", "created_at"} )
        return ret


    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="Restore snapshots",
             examples=[
                       {'Restore snapshots":"otc ecs restore-snapshot --volume-id b197b8af-fe63-465f-97b6-5e5b89exxx --snapshot-id 0c942ff7-454e-xxxx'}
                       ],
             args = [ 
                    arg(    '--snapshot-id',    dest='SNAPSHOTID',     help='Snapshot id of the  backup'),
                    arg(    '--volume-id',     dest='VOLUME_ID',     help='Volume Id of the EVS volume'),
                    arg(    '--volume-name',    dest='VOLUME_NAME',     help='Volume name of the EVS disk')

                    ])
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
    @otcfunc(plugin_name=__name__,
             desc="Delete snapshot",
             examples=[
                       {'Delete snapshot":"otc ecs delete-snapshot --snapshot-id 0c942ff7-454e-xxxx'}
                       ],
             args = [ 
                    arg(    '--snapshot-id',    dest='SNAPSHOTID',     help='Snapshot id of the  backup')
                    ])
    def delete_snapshot():        
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v2/" + OtcConfig.PROJECT_ID + "/cloudbackups"+ "/" + OtcConfig.SNAPSHOTID
        ret = utils_http.post( url , "")
        print(ret)
        return ret


    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="Create snapshot of volume",
             examples=[
                       {'Create snapshots of volume":"otc ecs create-snapshot --volume-id b197b8af-fe63-465f-97b6-5e5b89exxx --snapshot-id 0c942ff7-454e-xxxx'}
                       ],
             args = [ 
                    arg(    '--snapshot-id',    dest='SNAPSHOTID',     help='Snapshot id of the  backup'),
                    arg(    '--volume-id',     dest='VOLUME_ID',     help='Volume Id of the EVS volume'),
                    arg(    '--volume-name',    dest='VOLUME_NAME',     help='Volume name of the EVS disk'),
                    arg(    '--description',    dest='DESCRIPTION',     help='Description definition ( eg: backups)')
                    ])
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

    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="Describe Availability-zones",
             examples=[
                       {'Describe Availability-zones":"otc ecs describe_az'}
                       ],
             args = []) 
    def describe_az():         
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v2/" + OtcConfig.PROJECT_ID + "/os-availability-zone/detail"        
        ret = utils_http.get(url)
        print (ret)
        ecs.otcOutputHandler().print_output(ret, mainkey="availabilityZoneInfo", listkey={"zoneState", "zoneName"})
        return ret


    @staticmethod 
    @otcfunc(plugin_name=__name__,
             desc="List types",
             examples=[
                       {'List types":"otc ecs types'}
                       ])
    def types():         
        url = "https://" + OtcConfig.DEFAULT_HOST+ "/v2/" + OtcConfig.PROJECT_ID + "/types"        
        ret = utils_http.get(url)
        print (ret)
    