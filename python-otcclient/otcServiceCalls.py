#!/usr/bin/env python
""" generated source for module DefaultOtcServiceCalls """
#  
#  * Copyright (c) 2016 T-Systems GmbH
#  * Germany
#  * All rights reserved.
#  * 
#  * Author: zsonagy
#  * Datum: 08.03.2016
#  

# 
#  * Function implementation of OTC client tool
#  * ( based on aws commands)  
#  * @author zsonagy
#  *
#

from OtcConfig import OtcConfig
from OtcHttpMethods import OtcHttpMethods
from otcOutputHandler import otcOutputHandler
import json 
  
class otcServiceCalls():
    """ generated source for class DefaultOtcServiceCalls """
#    otcOutputHandler = otcOutputHandler()
    ar = {}


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#getECSVM(java.lang.String)
    # 	 
    @staticmethod 
    def getECSVM(VM):
        """ generated source for method getECSVM """
        ret = None
        ret = OtcHttpMethods.get(OtcConfig.AUTH_URL_ECS + "/" + VM)
        otcOutputHandler.printJsonTableTransverse(ret)
        return ret


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#getECSList()
    # 	
    @staticmethod 
    def getECSList():
        """ generated source for method getECSList """
        ret = None
        ret = OtcHttpMethods.get(OtcConfig.AUTH_URL_ECS)
        otcOutputHandler.printLevel2(ret, "servers", {"id", "name"})
        return ret


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#getECSDetail()
    # 	 
    @staticmethod 
    def getECSDetail():
        """ generated source for method getECSDetail """
        ret = None
        ret = OtcHttpMethods.get(OtcConfig.AUTH_URL_ECS + "/detail")
        otcOutputHandler.printJsonTableTransverse(ret) 
        return ret


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#getVPCList()
    # 	 
    @staticmethod 
    def getVPCList():
        """ generated source for method getVPCList """
        ret = None
        ret = OtcHttpMethods.get(OtcConfig.AUTH_URL_VPCS)
        otcOutputHandler.printLevel2(ret, "vpcs", {"id", "name", "status", "cidr"})
        return ret


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#getPUBLICIPSList()
    # 	 
    @staticmethod 
    def getPUBLICIPSList():
        """ generated source for method getPUBLICIPSList """
        ret = None
        ret = OtcHttpMethods.get(OtcConfig.AUTH_URL_PUBLICIPS)
        # print ret;
        otcOutputHandler.printLevel2(ret, "publicips", {"id", "status", "public_ip_address", "private_ip_address", "type", "create_time", "bandwidth_size"})
        return ret


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#getSECGROUPList()
    # 	 
    @staticmethod 
    def getSECGROUPList():
        """ generated source for method getSECGROUPList """
        ret = None
        ret = OtcHttpMethods.get(OtcConfig.AUTH_URL_SEC_GROUPS)
        # print ret;		
        otcOutputHandler.printLevel2(ret, "security_groups", {"id", "name", "vpc_id", "security_group_rules"})
        return ret


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#getSECGROUPRULESList()
    # 	 
    @staticmethod 
    def getSECGROUPRULESList():
        """ generated source for method getSECGROUPRULESList """
        ret = None
        ret = OtcHttpMethods.get(OtcConfig.AUTH_URL_SEC_GROUP_RULE)
        # print ret;
        otcOutputHandler.printLevel2(ret, "subnets", {"id", "name"})
        return ret


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#getSUBNETList()
    # 	 
    @staticmethod 
    def getSUBNETList():
        """ generated source for method getSUBNETList """
        ret = None
        ret = OtcHttpMethods.get(OtcConfig.AUTH_URL_SUBNETS)
        otcOutputHandler.printLevel2(ret, "subnets", {"id", "name", "cidr", "status", "vpc_id", "gateway_ip", "primary_dns", "availability_zone"})
        return ret


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#getIMAGEList()
    #
    @staticmethod  	 
    def getIMAGEList():
        """ generated source for method getIMAGEList """
        ret = None
        ret = OtcHttpMethods.get(OtcConfig.AUTH_URL_IMAGES)
        otcOutputHandler.printLevel2(ret, "images", {"id", "name", "__os_type", "updated_at", "deleted"})
        return ret


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#getFLAVORList()
    # 	 
    @staticmethod 
    def getFLAVORList():
        """ generated source for method getFLAVORList """
        ret = None
        ret = OtcHttpMethods.get(OtcConfig.AUTH_URL_FLAVORS)
        # print ret;
        otcOutputHandler.printLevel2(ret, "flavors", {"id", "name", "vcpus", "ram", "disk", "swap"})
        return ret


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#getKEYPAIRList()
    # 	 
    @staticmethod 
    def getKEYPAIRList():
        """ generated source for method getKEYPAIRList """
        ret = None
        ret = OtcHttpMethods.get(OtcConfig.AUTH_URL_KEYNAMES)
        otcOutputHandler.printLevel3(ret, "keypairs", "keypair", {"name", "fingerprint", "public_key"})
        return ret


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#KEYPAIRCreate()
    # 	 
    @staticmethod 
    def KEYPAIRCreate():
        """ generated source for method KEYPAIRCreate """
        ret = str()
        REQ_CREATE_KEYPAIR = "{ \"keypair\": { \"name\": \"" + OtcConfig.KEYNAME + "\" " + "" + "} }"
        REQ_CREATE_KEYPAIR2 = "{ \"keypair\": { \"name\": \"" + OtcConfig.KEYNAME + "\", " + "\"public_key\": \"" + OtcConfig.PUBLICKEY + "\" } }"
        REQ_CREATE_KEYPAIR3 = "{ \"keypair\": { \"name\": \"" + OtcConfig.KEYNAME + "\", " + "\"tenantId\": \"" + OtcConfig.PROJECT_ID + "\" } }"
        print REQ_CREATE_KEYPAIR2
        print OtcConfig.AUTH_URL_KEYNAMES
        ret = OtcHttpMethods.post(OtcConfig.AUTH_URL_KEYNAMES, REQ_CREATE_KEYPAIR2)
        print ret
        return ret


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#PUBLICIPSAllocate()
    # 	 
    @staticmethod 
    def PUBLICIPSAllocate():
        """ generated source for method PUBLICIPSAllocate """
        ret = str()
        REQ_CREATE_PUBLICIP = "{\"publicip\":{\"type\":\"5_bgp\"},\"bandwidth\":{\"name\":\"apiTest\",\"size\":111,\"share_type\":\"PER\",\"charge_mode\":\"traffic\"}}"
        ret = OtcHttpMethods.post(OtcConfig.AUTH_URL_PUBLICIPS, REQ_CREATE_PUBLICIP)
        print ret
        return ret


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#PUBLICIPSAssociate()
    # 	 
    @staticmethod 
    def PUBLICIPSAssociate():
        """ generated source for method PUBLICIPSAssociate """
        ret = str()
        REQ_ASSOCIATE_PUBLICIP = "{ \"publicip\": { \"port_id\": \"" + OtcConfig.NETWORKINTERFACEID + "\" } }"
        print REQ_ASSOCIATE_PUBLICIP
        url = OtcConfig.AUTH_URL_PUBLICIPS + "/" + OtcConfig.PUBLICIPID
        print url
        ret = OtcHttpMethods.post(url, REQ_ASSOCIATE_PUBLICIP)
        print ret
        return ret


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#KEYPAIRDelete()
    #
    @staticmethod  	 
    def KEYPAIRDelete():
        """ generated source for method KEYPAIRDelete """
        ret = str()
        ret = OtcHttpMethods.delete(OtcConfig.AUTH_URL_KEYNAMES + "/" + OtcConfig.KEYNAME)
        print ret
        return ret


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#getECSJOBList()
    # 	 
    @staticmethod 
    def getECSJOBList():
        """ generated source for method getECSJOBList """
        ret = None
        ret = OtcHttpMethods.get(OtcConfig.AUTH_URL_ECS_JOB)
        jobmap = otcOutputHandler.parseJsontoTopLevelSimple(ret)
        OtcConfig.ECSCREATEJOBSTATUS = str(jobmap.get("status")) 
        # print ret;
        return ret


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#getFileContentJSON(java.lang.String, java.lang.String)
    # 	 
    
    @staticmethod
    def getFileContentJSON( aSource, aTarget):
        """ generated source for method getFileContentJSON """
        if not open(aSource).exists():
            raise Exception(aSource)
#        fileContent = Files.readAllBytes(File(aSource).toPath())
#        bytesEncoded = DatatypeConverter.printBase64Binary(fileContent).getBytes()
#        FILECONTENT = str(bytesEncoded)
#        FILE_TEMPLATE = "{ \"path\": \"" + aTarget + "\", \"contents\": \"" + FILECONTENT + "\" }"
#        return FILE_TEMPLATE


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#getPersonalizationJSON()
    # 	 
    @staticmethod
    def getPersonalizationJSON():
        """ generated source for method getPersonalizationJSON """
        FILEJSONITEM = ""
        FILECOLLECTIONJSON = ""
        if OtcConfig.FILE1 != None: 
            ar =  str(OtcConfig.FILE1).split("=")
            FILEJSONITEM = otcServiceCalls.getFileContentJSON(ar[1], ar[0])
        FILECOLLECTIONJSON = FILEJSONITEM
        FILEJSONITEM = ""
        if OtcConfig.FILE2 != None:
            ar =  str(OtcConfig.FILE2).split("=")
            if len(FILECOLLECTIONJSON) > 0:
                FILEJSONITEM = ","                
            FILEJSONITEM = FILEJSONITEM + otcServiceCalls.getFileContentJSON(ar[1], ar[0])
        FILECOLLECTIONJSON = FILECOLLECTIONJSON + FILEJSONITEM
        FILEJSONITEM = ""
        if OtcConfig.FILE3 != None:
            ar =  str(OtcConfig.FILE3).split("=")
            if len(FILECOLLECTIONJSON) > 0:
                FILEJSONITEM = ","
            FILEJSONITEM = otcServiceCalls.getFileContentJSON(ar[1], ar[0])
        FILECOLLECTIONJSON = FILECOLLECTIONJSON + FILEJSONITEM
        FILEJSONITEM = ""
        if OtcConfig.FILE4 != None:
            ar =  str(OtcConfig.FILE4).split("=")
            if len(FILECOLLECTIONJSON) > 0:
                FILEJSONITEM = ","
            FILEJSONITEM = otcServiceCalls.getFileContentJSON(ar[1], ar[0])
        FILECOLLECTIONJSON = FILECOLLECTIONJSON + FILEJSONITEM
        FILEJSONITEM = ""
        if OtcConfig.FILE5 != None:
            ar =  str(OtcConfig.FILE5).split("=")
            if len(FILECOLLECTIONJSON) > 0:
                FILEJSONITEM = ","
            FILEJSONITEM = otcServiceCalls.getFileContentJSON(ar[1], ar[0])
        FILECOLLECTIONJSON = FILECOLLECTIONJSON + FILEJSONITEM
        PERSONALIZATION = ""
        if FILECOLLECTIONJSON != None and len(FILECOLLECTIONJSON) > 0:
            PERSONALIZATION = "\"personality\": [ " + FILECOLLECTIONJSON + "],"
        return PERSONALIZATION


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#ECSAction()
    # 	 
    @staticmethod
    def ECSAction():
        """ generated source for method ECSAction """
        ret = str()
        REQ_ECS_ACTION_VM = "{ " + "	\"" + OtcConfig.ECSACTION + "\": " + "	{ " + "	 \"type\":\"" + OtcConfig.ECSACTIONTYPE + "\", " + "	 \"servers\": [ { \"id\": \"" + OtcConfig.INSTANCE_ID + "\" }] " + "	 } " + "}"
        ret = OtcHttpMethods.post(OtcConfig.AUTH_URL_ECS_CLOUD_ACTION, REQ_ECS_ACTION_VM)
        print ret
        return ret


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#ECSDelete()
    # 	 
    @staticmethod
    def ECSDelete():
        """ generated source for method ECSDelete """
        ret = str()
        REQ_ECS_DELETE_VM = "{ \"servers\": [ { \"id\": \"" + OtcConfig.INSTANCE_ID + "\" } ]," + " \"delete_publicip\": \"" + OtcConfig.DELETE_PUBLICIP + "\", \"delete_volume\": \"" + OtcConfig.DELETE_VOLUME + "\" }"
        ret = OtcHttpMethods.post(OtcConfig.AUTH_URL_ECS_CLOUDSERVERS_BASE + "/delete", REQ_ECS_DELETE_VM)
        print ret
        return ret


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#VPCCreate()
    # 	 
    @staticmethod
    def VPCCreate():
        """ generated source for method VPCCreate """
        ret = str()
        REQ_CREATE_VPC = "{ \"vpc\": { \"name\": \"" + OtcConfig.VPCNAME + ", \"cidr\": \"" + OtcConfig.CIDR + "\" } }"
        ret = OtcHttpMethods.post(OtcConfig.AUTH_URL_VPCS, REQ_CREATE_VPC)
        print ret
        return ret


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#SUBNETCreate()
    # 	 
    @staticmethod
    def SUBNETCreate():
        """ generated source for method SUBNETCreate """
        ret = str()
        REQ_CREATE_SUBNET = "{ \"subnet\": { \"name\": \"" + OtcConfig.SUBNETNAME + "\", \"cidr\": \"" + OtcConfig.CIDR + "\", \"gateway_ip\": \"" + OtcConfig.GWIP + "\", \"dhcp_enable\": \"true\", \"primary_dns\": \"" + OtcConfig.PRIMARYDNS + "\", \"secondary_dns\": \"" + OtcConfig.SECDNS + "\", \"availability_zone\":\"" + OtcConfig.AZ + "\", \"vpc_id\":\"" + OtcConfig.VPCID + "\" } }"
        ret = OtcHttpMethods.post(OtcConfig.AUTH_URL_SUBNETS, REQ_CREATE_SUBNET)
        print ret
        return ret


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#SECGROUPCreate()
    # 	 
    @staticmethod
    def SECGROUPCreate():
        """ generated source for method SECGROUPCreate """
        ret = str()
        REQ_CREATE_SECGROUP = "{ \"security_group\": { \"name\":\"" + OtcConfig.SECUGROUPNAME + "\", \"vpc_id\" : \"" + OtcConfig.VPCID + "\" } }"
        ret = OtcHttpMethods.post(OtcConfig.AUTH_URL_SEC_GROUPS, REQ_CREATE_SECGROUP)
        print ret
        return ret


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#SECGROUPRULECreate()
    # 	 
    @staticmethod
    def SECGROUPRULECreate():
        """ generated source for method SECGROUPRULECreate """
        ret = str()
        REQ_CREATE_SECGROUPRULE = "{\"security_group_rule\":{ \"direction\":\"" + OtcConfig.DIRECTION + "\", \"port_range_min\":\"" + OtcConfig.PORTMIN + "\", \"ethertype\":\"" + OtcConfig.ETHERTYPE + "\", \"port_range_max\":\"" + OtcConfig.PORTMAX + "\", \"protocol\":\"" + OtcConfig.PROTOCOL + "\"  , \"security_group_id\":\"" + OtcConfig.SECUGROUP + "\" } }"
        print OtcConfig.AUTH_URL_SEC_GROUP_RULE
        print REQ_CREATE_SECGROUPRULE
        ret = OtcHttpMethods.post(OtcConfig.AUTH_URL_SEC_GROUP_RULE, REQ_CREATE_SECGROUPRULE)
        print ret
        return ret


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#ECSCreate()
    # 	 
    @staticmethod
    def ECSCreate():
        """ generated source for method ECSCreate """
        ret = str()
        PUBLICIPJSON = ""
        if OtcConfig.CREATE_ECS_WITH_PUBLIC_IP == "true":
            PUBLICIPJSON = "\"publicip\": { \"eip\": { \"iptype\": \"5_bgp\", \"bandwidth\": { \"size\": 5, \"sharetype\": \"PER\", \"chargemode\": \"traffic\" } } },"
        PERSONALIZATION = otcServiceCalls.getPersonalizationJSON()
        REQ_CREATE_VM = "	{                 " + "	    \"server\": { " + "		\"availability_zone\": \"" + OtcConfig.AZ + "\",         " + "		\"name\": \"" + OtcConfig.INSTANCE_NAME + "\",            " + "		\"imageRef\": \"" + OtcConfig.IMAGE_ID + "\",             " + "		\"root_volume\": {      " + "		    \"volumetype\": \"SATA\"            " + "		}, " + "		\"flavorRef\": \"" + OtcConfig.INSTANCE_TYPE + "\"," + PERSONALIZATION + "		\"vpcid\": \"" + OtcConfig.VPCID + "\",           " + "		\"security_groups\": [         " + "		    { " + "		        \"id\": \"" + OtcConfig.SECUGROUP + "\"   " + "		    }    " + "		],        " + "		\"nics\": [           " + "		    {            " + "		        \"subnet_id\": \"" + OtcConfig.SUBNETID + "\"        " + "		    }         " + "		],       " + PUBLICIPJSON + "		\"key_name\": \"" + OtcConfig.KEYNAME + "\",    " + "		\"adminPass\": \"" + OtcConfig.ADMINPASS + "\",   " + "		\"count\": \"" + OtcConfig.NUMCOUNT + "\",   " + "		\"},\": {      " + "		    \"__vnc_keymap\": \"de\"    " + "		}   " + "	    }   " + "	}       " + "	"
        if OtcConfig.IMAGE_ID == None:
            print "Image definition not Correct ! Check avaliable images with following command:"
            print "otc images list"
            exit(1)
        if OtcConfig.INSTANCE_TYPE == None:
            print "Instance Type definition not Correct ! Please check avaliable flavors  with following command:"
            print "otc ecs flavor-list"
            exit(1)
        if OtcConfig.VPCID == None:
            print "VPC definition not Correct ! Please check avaliable VPCs  with following command:"
            print "otc vpc list"
            exit(1)
        if OtcConfig.SECUGROUP == None:
            print "Security Group definition not Correct ! Please check avaliable security group with following command:"
            print "otc security-group list"
            exit(1)
        if OtcConfig.SUBNETID == None:
            print "Subnet definition not Correct ! Please check avaliable subnets with following command:"
            print "otc subnet list"
            exit(1)
        print (REQ_CREATE_VM)
        ret = OtcHttpMethods.post(OtcConfig.AUTH_URL_ECS_CLOUD, REQ_CREATE_VM)
        jobmap = otcOutputHandler.parseJsontoTopLevelSimple(ret)
        OtcConfig.ECSTASKID = str(jobmap.get("job_id"))
        print ret
        return ret


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#getIamToken()
    # 	 
    @staticmethod
    def getIamToken():
        """ generated source for method getIamToken """
        ret = None
        if OtcConfig.PROJECT_NAME != None: 
            project = "\"name\": \"" + OtcConfig.PROJECT_NAME + "\" " 

        else:
             project = "\"id\": \"" + OtcConfig.PROJECT_ID + "\""
        REQ_IAM = "	{" + "	    \"auth\": {       " + "		\"identity\": {   " + "		    \"methods\": [" + "		        \"password\"                             " + "		    ],            " + "		    \"password\": {                              " + "		        \"user\": {                              " + "		            \"name\": \"" + OtcConfig.USERNAME + "\",    " + "		            \"password\": \"" + OtcConfig.PASSWORD + "\"," + "		            \"domain\": {                        " + "		                \"name\": \"" + OtcConfig.DOMAIN + "\"            " + "		            }     " + "		        }         " + "		    }             " + "		},                " + "		\"scope\": {      " + "		    \"project\": {" + project + "		    }             " + "		}                 " + "	    }                 " + "	}"
        # otcOutputHandler.jsonPretyPrint(REQ_IAM);
        ret = OtcHttpMethods.post(OtcConfig.IAM_AUTH_URL, REQ_IAM)
        maindata = json.loads(ret)
        OtcConfig.PROJECT_ID = maindata['token']['project']['id'] 
        OtcConfig.resetUrlVars()
        return ret


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#convertFlavorNameToId()
    # 	 
    @staticmethod
    def convertFlavorNameToId():
        """ generated source for method convertFlavorNameToId """
        ret = None
        JSON = OtcHttpMethods.get(OtcConfig.AUTH_URL_FLAVORS)

        #OtcConfig.INSTANCE_TYPE = JSON['flavors']['project']['id'] 

        for hashMap in JSON["flavors"]:
            if hashMap.get("name") == OtcConfig.INSTANCE_TYPE_NAME:
                ret = str(hashMap.get("id"))
        OtcConfig.INSTANCE_TYPE = ret


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#convertPublicIpNameToId()
    # 	 
    @staticmethod
    def convertPublicIpNameToId():
        """ generated source for method convertPublicIpNameToId """
        ret = None
        JSON = OtcHttpMethods.get(OtcConfig.AUTH_URL_PUBLICIPS)
        subnetmap = otcOutputHandler.parseJsontoTopLevelList(JSON, "publicips")
        for hashMap in subnetmap:
            if hashMap.get("public_ip_address") == OtcConfig.PUBLICIP:
                ret = str(hashMap.get("id"))
        OtcConfig.PUBLICIPID = ret


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#convertVPCNameToId()
    # 	 
    @staticmethod
    def convertVPCNameToId():
        """ generated source for method convertVPCNameToId """
        ret = None
        JSON = OtcHttpMethods.get(OtcConfig.AUTH_URL_VPCS)
        
        parsed  = json.loads(JSON)
        vpcs = parsed["vpcs"]

        for vpc in vpcs:
            if vpc.get("name") == OtcConfig.VPCNAME:
                ret = vpc["id"]
        OtcConfig.VPCID = ret


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#convertSUBNETNameToId()
    # 	 
    @staticmethod
    def convertSUBNETNameToId():
        """ generated source for method convertSUBNETNameToId """
        ret = None
        JSON = OtcHttpMethods.get(OtcConfig.AUTH_URL_SUBNETS)
        subnetmap = otcOutputHandler.parseJsontoTopLevelList(JSON, "subnets")
        for hashMap in subnetmap:
            if hashMap.get("name") == OtcConfig.SUBNETNAME and hashMap.get("vpc_id") == OtcConfig.VPCID:
                ret = str(hashMap.get("id"))
        OtcConfig.SUBNETID = ret


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#convertIMAGENameToId()
    # 	 
    @staticmethod
    def convertIMAGENameToId():
        """ generated source for method convertIMAGENameToId """
        ret = None
        JSON = OtcHttpMethods.get(OtcConfig.AUTH_URL_IMAGES)
        subnetmap = otcOutputHandler.parseJsontoTopLevelList(JSON, "images")
        for hashMap in subnetmap:
            if hashMap.get("name") == OtcConfig.IMAGENAME:
                ret = str(hashMap.get("id"))
        OtcConfig.IMAGE_ID = ret

    @staticmethod
    def convertINSTANCENameToId():
        """ generated source for method convertIMAGENameToId """
        ret = None
        print "NOT IMPLEMENTED"
        exit( 1 )
        JSON = OtcHttpMethods.get(OtcConfig.AUTH_URL_IMAGES)
        subnetmap = otcOutputHandler.parseJsontoTopLevelList(JSON, "images")
        for hashMap in subnetmap:
            if hashMap.get("name") == OtcConfig.IMAGENAME:
                ret = str(hashMap.get("id"))
        OtcConfig.IMAGE_ID = ret




    # 	 * @see com.tsystems.otc.IOtcServiceCalls#convertSECUGROUPNameToId()
    # 	 
    @staticmethod
    def convertSECUGROUPNameToId():
        """ generated source for method convertSECUGROUPNameToId """
        ret = None
        JSON = OtcHttpMethods.get(OtcConfig.AUTH_URL_SEC_GROUPS)
        subnetmap = otcOutputHandler.parseJsontoTopLevelList(JSON, "security_groups")
        for hashMap in subnetmap:
            if hashMap.get("name") == OtcConfig.SECUGROUPNAME and hashMap.get("vpc_id") == OtcConfig.VPCID:
                ret = str(hashMap.get("id"))
        OtcConfig.SECUGROUP = ret


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#CreateLaunchConfiguration()
    # 	 
    @staticmethod
    def CreateLaunchConfiguration():
        """ generated source for method CreateLaunchConfiguration """
        print("NOT IMPLEMENTED!")
        exit(-1)


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#AttachInstances()
    # 	 
    @staticmethod
    def AttachInstances():
        """ generated source for method AttachInstances """
        print("NOT IMPLEMENTED!")
        exit(-1)
        #  TODO Auto-generated method stub


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#AttachLoadBalancers()
    # 	 
    @staticmethod
    def AttachLoadBalancers():
        """ generated source for method AttachLoadBalancers """
        print("NOT IMPLEMENTED!")
        exit(-1)
        #  TODO Auto-generated method stub


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#CreateAutoScalingGroup()
    # 	 
    @staticmethod
    def CreateAutoScalingGroup():
        """ generated source for method CreateAutoScalingGroup """
        print("NOT IMPLEMENTED!")
        exit(-1)
        #  TODO Auto-generated method stub


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#DeleteAutoScalingGroup()
    # 	 
    @staticmethod
    def DeleteAutoScalingGroup():
        """ generated source for method DeleteAutoScalingGroup """
        print("NOT IMPLEMENTED!")
        exit(-1)
        #  TODO Auto-generated method stub


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#DeleteLaunchConfiguration()
    # 	 
    @staticmethod
    def DeleteLaunchConfiguration():
        """ generated source for method DeleteLaunchConfiguration """
        print("NOT IMPLEMENTED!")
        exit(-1)


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#getVolumeList()
    # 	 
    @staticmethod
    def getVolumeList():
        """ generated source for method getVolumeList """
        ret = None
        ret = OtcHttpMethods.get(OtcConfig.AUTH_URL_CLOUDVOLUMES + "/detail")
        otcOutputHandler.printLevel2(ret, "volumes", {"id", "name", "volume_type", "size", "status", "bootable", "availability_zone", "limit", "attachments", "source_volid", "snapshot_id", "description", "created_at"})
        return ret


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#CreateVolume()
    # 	 
    @staticmethod
    def CreateVolume():
        """ generated source for method CreateVolume """
        ret = str()
        REQ_CREATE_CLOUDVOLUMES = "{ \"volume\": { \"backup_id\": " + OtcConfig.SNAPSHOTID + ", " + "\"count\": " + OtcConfig.NUMCOUNT + ", \"availability_zone\": \"" + OtcConfig.AZ + "\",\"description\": \"" + OtcConfig.VOLUME_NAME + "\", \"size\": " + OtcConfig.VOLUME_SIZE + ", \"name\": \"" + OtcConfig.VOLUME_NAME + "\", \"imageRef\": " + "null" + ", \"volume_type\": \"" + OtcConfig.VOLUME_TYPE + "\" } }"
        print REQ_CREATE_CLOUDVOLUMES
        ret = OtcHttpMethods.post(OtcConfig.AUTH_URL_CLOUDVOLUMES, REQ_CREATE_CLOUDVOLUMES)
        print ret
        return ret


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#AttachVolume()
    # 	 
    @staticmethod
    def AttachVolume():
        """ generated source for method AttachVolume """
        ret = str()
        REQ_ATTACH_CLOUDVOLUMES = "{ \"volumeAttachment\": { \"volumeId\": \"" + OtcConfig.VOLUME_ID + "\", \"device\": \"" + OtcConfig.EVS_DEVICE + "\" } }"
        print REQ_ATTACH_CLOUDVOLUMES
        ret = OtcHttpMethods.post(OtcConfig.AUTH_URL_ECS_ATTACHVOLUME, REQ_ATTACH_CLOUDVOLUMES)
        print ret
        return ret


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#DetachVolume()
    # 	 
    @staticmethod
    def DetachVolume():
        """ generated source for method DetachVolume """
        ret = str()
        ret = OtcHttpMethods.delete(OtcConfig.AUTH_URL_ECS_DEATTACHVOLUME)
        print ret
        return ret


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#DeleteVolume()
    # 	 
    @staticmethod
    def DeleteVolume():
        """ generated source for method DeleteVolume """
        ret = str()
        ret = OtcHttpMethods.delete(OtcConfig.AUTH_URL_CLOUDVOLUMES + "/" + OtcConfig.VOLUME_ID)
        print ret
        return ret


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#DescribeQuotas()
    # 	 
    @staticmethod
    def DescribeQuotas():
        """ generated source for method DescribeQuotas """
        ret = None
        ret = OtcHttpMethods.get(OtcConfig.AUTH_URL_ECS_QUOTAS)
        otcOutputHandler.printJsonTableTransverse(ret)
        return ret

 
    # 	 * @see com.tsystems.otc.IOtcServiceCalls#getBackupList()
    # 	 
    @staticmethod
    def getBackupList():
        """ generated source for method getBackupList """
        ret = None
        ret = OtcHttpMethods.get(OtcConfig.AUTH_URL_BACKUP_LIST)
        # print ret; 
        otcOutputHandler.printJsonTableTransverse(ret)
        return ret


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#RestoreBackupDisk()
    # 	 
    @staticmethod
    def RestoreBackupDisk():
        """ generated source for method RestoreBackupDisk """
        ret = str()
        REQ_RESTORE_BACKUP = "{ \"restore\":{ \"volume_id\":\"" + OtcConfig.VOLUME_ID + "\" } }"
        print REQ_RESTORE_BACKUP
        ret = OtcHttpMethods.post(OtcConfig.AUTH_URL_BACKUP_ACTION + "/" + OtcConfig.SNAPSHOTID + "/restore", REQ_RESTORE_BACKUP)
        print ret
        return ret


    # 	 * @see com.tsystems.otc.IOtcServiceCalls#DeleteBackup()
    # 	 
    @staticmethod
    def DeleteBackup():
        """ generated source for method DeleteBackup """
        ret = str()
        ret = OtcHttpMethods.post(OtcConfig.AUTH_URL_BACKUP_ACTION + "/" + OtcConfig.SNAPSHOTID, "")
        print ret
        return ret


    @staticmethod
    def CreateBackup():
        """ generated source for method CreateBackup """
        ret = str()
        REQ_CREATE_BACKUP = "{ \"backup\":{ \"" + "volume_id\":\"" + OtcConfig.VOLUME_ID + "\", " + "\"name\":\"" + OtcConfig.DESCRIPTION + "\", \"description\":\"" + OtcConfig.DESCRIPTION + "\" } }"
        print REQ_CREATE_BACKUP
        ret = OtcHttpMethods.post(OtcConfig.AUTH_URL_BACKUP_ACTION, REQ_CREATE_BACKUP)
        print ret
        return ret

