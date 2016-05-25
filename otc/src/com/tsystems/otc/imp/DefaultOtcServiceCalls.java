/* 
 * Copyright (c) 2016 T-Systems GmbH
 * Germany
 * All rights reserved.
 * 
 * Name: ParamFactory.java
 * Author: zsonagy
 * Datum: 08.03.2016
 */

package com.tsystems.otc.imp;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

import javax.xml.bind.DatatypeConverter;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import com.tsystems.otc.config.OtcConfig;
import com.tsystems.otc.huawei.OtcHttpMethods;
import com.tsystems.otc.interfaces.IOtcOutputHandler;
import com.tsystems.otc.interfaces.IOtcServiceCalls;

/**
 * Function implementation of OTC client tool
 * ( based on aws commands)  
 * @author zsonagy
 *
 */
public class DefaultOtcServiceCalls implements IOtcServiceCalls {

	static final Logger log = LogManager.getLogger(DefaultOtcServiceCalls.class
			.getName());

	IOtcOutputHandler otcOutputHandler = new DefaultOtcOutputHandler(); 
	
	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#getECSVM(java.lang.String)
	 */
	@Override
	public String getECSVM(String VM) throws IOException {
		String ret = null;
		ret = OtcHttpMethods.get(OtcConfig.AUTH_URL_ECS + "/" + VM);
		otcOutputHandler.printJsonTableTransverse(ret);
		return ret;
	}

	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#getECSList()
	 */
	@Override
	public String getECSList() throws IOException {
		String ret = null;
		
		ret = OtcHttpMethods.get(OtcConfig.AUTH_URL_ECS);

		otcOutputHandler.printLevel2(ret,"servers",Arrays.asList("id","name"));

		return ret;
	}

	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#getECSDetail()
	 */
	@Override
	public String getECSDetail() throws IOException {
		String ret = null;
		
		ret = OtcHttpMethods.get(OtcConfig.AUTH_URL_ECS + "/detail");
			
		otcOutputHandler.printJsonTableTransverse(ret);
		
		return ret;
	}

	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#getVPCList()
	 */
	@Override
	public String getVPCList() throws IOException {
		String ret = null;
		ret = OtcHttpMethods.get(OtcConfig.AUTH_URL_VPCS);
		otcOutputHandler.printLevel2(ret,"vpcs",Arrays.asList("id","name","status","cidr"));
		return ret;
	}

	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#getPUBLICIPSList()
	 */
	@Override
	public String getPUBLICIPSList() throws IOException {
		String ret = null;
		ret = OtcHttpMethods.get(OtcConfig.AUTH_URL_PUBLICIPS);
		
		//System.out.println(ret);
		otcOutputHandler.printLevel2(ret,"publicips",Arrays.asList("id","status","public_ip_address","private_ip_address","type","create_time", "bandwidth_size"));

		return ret;
	}

	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#getSECGROUPList()
	 */
	@Override
	public String getSECGROUPList() throws IOException {
		String ret = null;
		ret = OtcHttpMethods.get(OtcConfig.AUTH_URL_SEC_GROUPS);
		//System.out.println(ret);		
		otcOutputHandler.printLevel2(ret,"security_groups",Arrays.asList("id","name","vpc_id", "security_group_rules"));

		return ret;
	}

	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#getSECGROUPRULESList()
	 */
	@Override
	public String getSECGROUPRULESList() throws Exception {
		String ret = null;
		ret = OtcHttpMethods.get(OtcConfig.AUTH_URL_SEC_GROUP_RULE);
		//System.out.println(ret);
		otcOutputHandler.printLevel2(ret,"subnets",Arrays.asList("id","name"));
		return ret;
	}

	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#getSUBNETList()
	 */
	@Override
	public String getSUBNETList() throws Exception {
		String ret = null;
		ret = OtcHttpMethods.get(OtcConfig.AUTH_URL_SUBNETS);
		
		otcOutputHandler.printLevel2(ret,"subnets",Arrays.asList("id","name","cidr","status","vpc_id","gateway_ip","primary_dns","availability_zone"));
		return ret;
	}

	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#getIMAGEList()
	 */
	@Override
	public String getIMAGEList() throws Exception {
		String ret = null;
		ret = OtcHttpMethods.get(OtcConfig.AUTH_URL_IMAGES);
		otcOutputHandler.printLevel2(ret,"images",Arrays.asList("id","name","__os_type","updated_at","deleted"));
		return ret;
	}

	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#getFLAVORList()
	 */
	@Override
	public String getFLAVORList() throws IOException {
		String ret = null;
		ret = OtcHttpMethods.get(OtcConfig.AUTH_URL_FLAVORS);
		//System.out.println(ret);
		otcOutputHandler.printLevel2(ret,"flavors",Arrays.asList("id","name","vcpus","ram","disk","swap"));

		return ret;
	}

	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#getKEYPAIRList()
	 */
	@Override
	public String getKEYPAIRList() throws IOException {
		String ret = null;
		ret = OtcHttpMethods.get(OtcConfig.AUTH_URL_KEYNAMES);
	
		otcOutputHandler.printLevel3(ret,"keypairs","keypair",Arrays.asList("name","fingerprint","public_key"));
		return ret;
	}
	
	


	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#KEYPAIRCreate()
	 */
	@Override
	public String KEYPAIRCreate() {
		String ret;
		String REQ_CREATE_KEYPAIR = "{ \"keypair\": { \"name\": \""
				+ OtcConfig.KEYNAME
				+ "\" "
				+ ""
				+ "} }";
		
		String REQ_CREATE_KEYPAIR2 = "{ \"keypair\": { \"name\": \""
				+ OtcConfig.KEYNAME
				+ "\", "
				+ "\"public_key\": \""
				+ OtcConfig.PUBLICKEY
				+ "\" } }";

		
		String REQ_CREATE_KEYPAIR3 = "{ \"keypair\": { \"name\": \""
				+ OtcConfig.KEYNAME
				+ "\", "
				+ "\"tenantId\": \""
				+ OtcConfig.PROJECT_ID
				+ "\" } }";

		
		System.out.println(REQ_CREATE_KEYPAIR2);
		System.out.println(OtcConfig.AUTH_URL_KEYNAMES);
		ret = OtcHttpMethods.post(OtcConfig.AUTH_URL_KEYNAMES, REQ_CREATE_KEYPAIR2);										   
		System.out.println(ret);
		return ret;
	}

	
	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#PUBLICIPSAllocate()
	 */
	@Override
	public String PUBLICIPSAllocate() {
		String ret;
		//String REQ_CREATE_PUBLICIP=" { \"publicip\": { \"eip\": { \"iptype\": \"5_bgp\", \"bandwidth\": { \"size\": 5, \"sharetype\": \"PER\", \"charge_mode\": \"traffic\"  } } }";
//		String REQ_CREATE_PUBLICIP=" { \"publicip\": { \"eip\": { \"iptype\": \"5_bgp\", \"bandwidth\": { \"size\": 5, \"sharetype\": \"PER\", \"charge_mode\": \"traffic\"  } } }";
		
		String REQ_CREATE_PUBLICIP = "{\"publicip\":{\"type\":\"5_bgp\"},\"bandwidth\":{\"name\":\"apiTest\",\"size\":111,\"share_type\":\"PER\",\"charge_mode\":\"traffic\"}}";
				//"{ \"publicip\": { \"type\": \"5_bgp\" }, \"bandwidth\": { \"names\":\"bandwidth126\", \"size\": 10, \"sharetype\": \"PER\" } } ";

//~~~		PUBLICIPJSON = "\"publicip\": { \"eip\": { \"iptype\": \"5_bgp\", \"bandwidth\": { \"size\": 10, \"sharetype\": \"PER\" } } },";

		System.out.println(REQ_CREATE_PUBLICIP);
		
		ret = OtcHttpMethods.post(OtcConfig.AUTH_URL_PUBLICIPS, REQ_CREATE_PUBLICIP);
		System.out.println(ret);
		return ret;
	}
	
	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#PUBLICIPSAssociate()
	 */
	@Override
	public String PUBLICIPSAssociate() {
		String ret;
		String REQ_ASSOCIATE_PUBLICIP = "{ \"publicip\": { \"port_id\": \""
				+ OtcConfig.NETWORKINTERFACEID 
				+ "\" } }";
				
		System.out.println(REQ_ASSOCIATE_PUBLICIP);
		String url = OtcConfig.AUTH_URL_PUBLICIPS + "/" + OtcConfig.PUBLICIPID; 
		System.out.println(url );
		ret = OtcHttpMethods.post(url, REQ_ASSOCIATE_PUBLICIP);
		System.out.println(ret);
		return ret;
	}
	
	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#KEYPAIRDelete()
	 */
	@Override
	public String KEYPAIRDelete() {
		String ret;
		ret = OtcHttpMethods.delete(OtcConfig.AUTH_URL_KEYNAMES + "/" + OtcConfig.KEYNAME);
		System.out.println(ret);
		return ret;
		
	}
	
	
	
	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#getECSJOBList()
	 */
	@Override
	public String getECSJOBList() throws IOException {
		String ret = null;
		ret = OtcHttpMethods.get(OtcConfig.AUTH_URL_ECS_JOB);
		HashMap<String, Object>	jobmap	= otcOutputHandler.parseJsontoTopLevelSimple(ret);

		OtcConfig.ECSCREATEJOBSTATUS = (String) jobmap.get("status");
		//System.out.println(ret);
		return ret;
	}

	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#getFileContentJSON(java.lang.String, java.lang.String)
	 */
	@Override
	public String getFileContentJSON(String aSource, String aTarget)
			throws IOException {

		if (!new File(aSource).exists()) {
			throw new FileNotFoundException(aSource);
		}

		byte[] fileContent = Files.readAllBytes(new File(aSource).toPath());

		
		byte[] bytesEncoded = DatatypeConverter.printBase64Binary(fileContent).getBytes();

		String FILECONTENT = new String(bytesEncoded);

		String FILE_TEMPLATE = "{ \"path\": \"" + aTarget
				+ "\", \"contents\": \"" + FILECONTENT + "\" }";
		return FILE_TEMPLATE;
	}

	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#getPersonalizationJSON()
	 */
	@Override
	public String getPersonalizationJSON() throws IOException {
		String FILEJSONITEM = "";
		String FILECOLLECTIONJSON = "";

	
		if (OtcConfig.FILE1 != null) {
			String[] ar = OtcConfig.FILE1.split("=");
			FILEJSONITEM = getFileContentJSON(ar[1], ar[0]);
		}
		FILECOLLECTIONJSON = FILEJSONITEM;

		FILEJSONITEM="";
		if (OtcConfig.FILE2 != null) {
			String[] ar = OtcConfig.FILE2.split("=");
			if( FILECOLLECTIONJSON.length() > 0 ) FILEJSONITEM=","; 
			FILEJSONITEM = FILEJSONITEM + getFileContentJSON(ar[1], ar[0]);
		}

		FILECOLLECTIONJSON = FILECOLLECTIONJSON + FILEJSONITEM;

		FILEJSONITEM="";
		if (OtcConfig.FILE3 != null) {
			String[] ar = OtcConfig.FILE3.split("=");
			if( FILECOLLECTIONJSON.length() > 0 ) FILEJSONITEM=",";
			FILEJSONITEM = getFileContentJSON(ar[1], ar[0]);
		}

		FILECOLLECTIONJSON = FILECOLLECTIONJSON + FILEJSONITEM;

		FILEJSONITEM="";
		if (OtcConfig.FILE4 != null) {
			String[] ar = OtcConfig.FILE4.split("=");
			if( FILECOLLECTIONJSON.length() > 0 ) FILEJSONITEM=",";
			FILEJSONITEM = getFileContentJSON(ar[1], ar[0]);
		}

		FILECOLLECTIONJSON = FILECOLLECTIONJSON + FILEJSONITEM;

		FILEJSONITEM="";
		if (OtcConfig.FILE5 != null) {
			String[] ar = OtcConfig.FILE5.split("=");
			if( FILECOLLECTIONJSON.length() > 0 ) FILEJSONITEM=",";
			FILEJSONITEM = getFileContentJSON(ar[1], ar[0]);
		}

		FILECOLLECTIONJSON = FILECOLLECTIONJSON + FILEJSONITEM;

		String PERSONALIZATION = "";

		if (FILECOLLECTIONJSON != null && FILECOLLECTIONJSON.length() > 0) {
			PERSONALIZATION = "\"personality\": [ " + FILECOLLECTIONJSON
					+ "],";
		}
		return PERSONALIZATION;
	}

	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#ECSAction()
	 */
	@Override
	public String ECSAction() {
		String ret;
		String REQ_ECS_ACTION_VM = "{ " + "	\"" + OtcConfig.ECSACTION + "\": "
				+ "	{ " + "	 \"type\":\"" + OtcConfig.ECSACTIONTYPE + "\", "
				+ "	 \"servers\": [ { \"id\": \"" + OtcConfig.INSTANCE_ID
				+ "\" }] " + "	 } " + "}";

		ret = OtcHttpMethods.post(OtcConfig.AUTH_URL_ECS_CLOUD_ACTION,
				REQ_ECS_ACTION_VM);

		System.out.println(ret);
		return ret;
	}

	
	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#ECSDelete()
	 */
	@Override
	public String ECSDelete() {
		String ret;
		String REQ_ECS_DELETE_VM = "{ \"servers\": [ { \"id\": \""
				+ OtcConfig.INSTANCE_ID
				+ "\" } ],"
				+ " \"delete_publicip\": \""
				+ OtcConfig.DELETE_PUBLICIP
				+ "\", \"delete_volume\": \""
				+ OtcConfig.DELETE_VOLUME
				+ "\" }";

		ret = OtcHttpMethods.post(OtcConfig.AUTH_URL_ECS_CLOUDSERVERS_BASE + "/delete",
				REQ_ECS_DELETE_VM);

		System.out.println(ret);
		return ret;
	}
	
	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#VPCCreate()
	 */
	@Override
	public String VPCCreate() {
		String ret;
		String REQ_CREATE_VPC = "{ \"vpc\": { \"name\": \"" + OtcConfig.VPCNAME
				+ ", \"cidr\": \"" + OtcConfig.CIDR + "\" } }";

		ret = OtcHttpMethods.post(OtcConfig.AUTH_URL_VPCS, REQ_CREATE_VPC);
		System.out.println(ret);
		return ret;
	}

	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#SUBNETCreate()
	 */
	@Override
	public String SUBNETCreate() {
		String ret;
		String REQ_CREATE_SUBNET = "{ \"subnet\": { \"name\": \""
				+ OtcConfig.SUBNETNAME + "\", \"cidr\": \"" + OtcConfig.CIDR
				+ "\", \"gateway_ip\": \"" + OtcConfig.GWIP
				+ "\", \"dhcp_enable\": \"true\", \"primary_dns\": \""
				+ OtcConfig.PRIMARYDNS + "\", \"secondary_dns\": \""
				+ OtcConfig.SECDNS + "\", \"availability_zone\":\""
				+ OtcConfig.AZ + "\", \"vpc_id\":\"" + OtcConfig.VPCID
				+ "\" } }";

		ret = OtcHttpMethods.post(OtcConfig.AUTH_URL_SUBNETS, REQ_CREATE_SUBNET);
		System.out.println(ret);
		return ret;
	}

	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#SECGROUPCreate()
	 */
	@Override
	public String SECGROUPCreate() {
		String ret;
		String REQ_CREATE_SECGROUP = "{ \"security_group\": { \"name\":\""
				+ OtcConfig.SECUGROUPNAME + "\", \"vpc_id\" : \""
				+ OtcConfig.VPCID + "\" } }";

		ret = OtcHttpMethods.post(OtcConfig.AUTH_URL_SEC_GROUPS,
				REQ_CREATE_SECGROUP);
		System.out.println(ret);
		return ret;
	}

	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#SECGROUPRULECreate()
	 */
	@Override
	public String SECGROUPRULECreate() {
		String ret;
		String REQ_CREATE_SECGROUPRULE = "{\"security_group_rule\":{ \"direction\":\""
				+ OtcConfig.DIRECTION
				+ "\", \"port_range_min\":\""
				+ OtcConfig.PORTMIN
				+ "\", \"ethertype\":\""
				+ OtcConfig.ETHERTYPE
				+ "\", \"port_range_max\":\""
				+ OtcConfig.PORTMAX
				+ "\", \"protocol\":\""
				+ OtcConfig.PROTOCOL
				+ "\"  , \"security_group_id\":\""
				+ OtcConfig.SECUGROUP + "\" } }";
		
	
		System.out.println(OtcConfig.AUTH_URL_SEC_GROUP_RULE);
		System.out.println(REQ_CREATE_SECGROUPRULE);
		
		ret = OtcHttpMethods.post(OtcConfig.AUTH_URL_SEC_GROUP_RULE,
				REQ_CREATE_SECGROUPRULE);
		System.out.println(ret);
		return ret;
	}

	
	 

	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#ECSCreate()
	 */
	@Override
	public String ECSCreate() throws IOException {
		String ret;

		String PUBLICIPJSON = "";
		if (OtcConfig.CREATE_ECS_WITH_PUBLIC_IP == "true") {
			PUBLICIPJSON = "\"publicip\": { \"eip\": { \"iptype\": \"5_bgp\", \"bandwidth\": { \"size\": 5, \"sharetype\": \"PER\", \"chargemode\": \"traffic\" } } },";
		}

		String PERSONALIZATION = getPersonalizationJSON();
		String REQ_CREATE_VM = "	{                                                                     "
				+ "	    \"server\": {                                                     "
				+ "		\"availability_zone\": \""
				+ OtcConfig.AZ
				+ "\",                              "
				+ "		\"name\": \""
				+ OtcConfig.INSTANCE_NAME
				+ "\",                                 "
				+ "		\"imageRef\": \""
				+ OtcConfig.IMAGE_ID
				+ "\",                                  "
				+ "		\"root_volume\": {                           "
				+ "		    \"volumetype\": \"SATA\"            "
				+ "		}, "
				+ "		\"flavorRef\": \""
				+ OtcConfig.INSTANCE_TYPE
				+ "\","
				+ PERSONALIZATION
				+ "		\"vpcid\": \""
				+ OtcConfig.VPCID
				+ "\",           "
				+ "		\"security_groups\": [         "
				+ "		    { "
				+ "		        \"id\": \""
				+ OtcConfig.SECUGROUP
				+ "\"   "
				+ "		    }    "
				+ "		],        "
				+ "		\"nics\": [           "
				+ "		    {            "
				+ "		        \"subnet_id\": \""
				+ OtcConfig.SUBNETID
				+ "\"        "
				+ "		    }         "
				+ "		],       "
				+ PUBLICIPJSON
				+ "		\"key_name\": \""
				+ OtcConfig.KEYNAME
				+ "\",    "
				+ "		\"adminPass\": \""
				+ OtcConfig.ADMINPASS
				+ "\",   "
				+ "		\"count\": \""
				+ OtcConfig.NUMCOUNT
				+ "\",   "
				+ "		\"},\": {      "
				+ "		    \"__vnc_keymap\": \"de\"    "
				+ "		}   "
				+ "	    }   "
				+ "	}       " + "	";

		if (OtcConfig.IMAGE_ID == null) {
			System.out
					.println("Image definition not Correct ! Check avaliable images with following command:");
			System.out.println("otc images list");
			System.exit(1);
		}
		if (OtcConfig.INSTANCE_TYPE == null) {
			System.out
					.println("Instance Type definition not Correct ! Please check avaliable flavors  with following command:");
			System.out.println("otc ecs flavor-list");
			System.exit(1);
		}
		if (OtcConfig.VPCID == null) {
			System.out
					.println("VPC definition not Correct ! Please check avaliable VPCs  with following command:");
			System.out.println("otc vpc list");
			System.exit(1);
		}
		if (OtcConfig.SECUGROUP == null) {
			System.out
					.println("Security Group definition not Correct ! Please check avaliable security group with following command:");
			System.out.println("otc security-group list");
			System.exit(1);
		}
		if (OtcConfig.SUBNETID == null) {
			System.out
					.println("Subnet definition not Correct ! Please check avaliable subnets with following command:");
			System.out.println("otc subnet list");
			System.exit(1);
		}
		
		log.info(REQ_CREATE_VM);
		ret = OtcHttpMethods.post(OtcConfig.AUTH_URL_ECS_CLOUD, REQ_CREATE_VM);
		
		HashMap<String, Object>	jobmap	= otcOutputHandler.parseJsontoTopLevelSimple(ret);
		OtcConfig.ECSTASKID = (String) jobmap.get("job_id");
		System.out.println(ret);
		
		return ret;
	}

	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#getIamToken()
	 */
	@Override
	public String getIamToken() throws IOException {
		String ret = null;
		String project = OtcConfig.PROJECT_NAME != null ? "\"name\": \"" + OtcConfig.PROJECT_NAME + "\" " : "\"id\": \"" + OtcConfig.PROJECT_ID + "\"";
		String REQ_IAM = 
				"	{                                                                         " +
						"	    \"auth\": {                                                           " +
						"		\"identity\": {                                                       " + 
						"		    \"methods\": [                                                    " +
						"		        \"password\"                                                  " +
						"		    ],                                                                " +
						"		    \"password\": {                                                   " +
						"		        \"user\": {                                                   " +
						"		            \"name\": \"" + OtcConfig.USERNAME + "\",                         " +
						"		            \"password\": \"" + OtcConfig.PASSWORD + "\",                     " +
						"		            \"domain\": {                                             " +
						"		                \"name\": \"" + OtcConfig.DOMAIN + "\"            " +
						"		            }                                                         " +
						"		        }                                                             " +
						"		    }                                                                 " +
						"		},                                                                    " +
						"		\"scope\": {                                                          " +
						"		    \"project\": {                                                    " +
						project +
						"		    }                                                                 " +
						"		}                                                                     " +
						"	    }                                                                     " +
						"	}                                                                         "  
						;
		//otcOutputHandler.jsonPretyPrint(REQ_IAM);
		ret = OtcHttpMethods.post(OtcConfig.IAM_AUTH_URL, REQ_IAM);
		HashMap<String, Object>	jobmap	= otcOutputHandler.parseJsontoTopLevelSimple(ret);
		HashMap<String, Object>	structAuth = (HashMap<String, Object>) jobmap.get("token");
		
		HashMap<String, Object> projectmap  = (HashMap<String, Object>) structAuth.get("project");
		HashMap<String, Object> usermap  = (HashMap<String, Object>) structAuth.get("user");
		
		String projectid = (String) projectmap.get("id");
		OtcConfig.PROJECT_ID = projectid;
		
		OtcConfig.resetUrlVars();
		//System.out.println(ret);
		return ret;							
		
	}

	
	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#convertFlavorNameToId()
	 */
	@Override
	public void convertFlavorNameToId() throws IOException {
		String ret = null;
		String JSON = OtcHttpMethods.get(OtcConfig.AUTH_URL_FLAVORS);
				

		List<HashMap<String, Object>> subnetmap = otcOutputHandler.parseJsontoTopLevelList(JSON,"flavors");
		for (HashMap<String, Object> hashMap : subnetmap) {
			if( hashMap.get("name").equals(OtcConfig.INSTANCE_TYPE_NAME) ) 
			{
				ret = (String) hashMap.get("id");
			}
		}
		OtcConfig.INSTANCE_TYPE = ret;		
		
	}

	
	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#convertPublicIpNameToId()
	 */
	@Override
	public void convertPublicIpNameToId() throws IOException {
		String ret = null;
		String JSON = OtcHttpMethods.get(OtcConfig.AUTH_URL_PUBLICIPS);
				
		
		List<HashMap<String, Object>> subnetmap = otcOutputHandler.parseJsontoTopLevelList(JSON,"publicips");
		for (HashMap<String, Object> hashMap : subnetmap) {
			if( hashMap.get("public_ip_address").equals(OtcConfig.PUBLICIP) ) 
			{
				ret = (String) hashMap.get("id");
			}
		}
		OtcConfig.PUBLICIPID = ret;		
		
	}
	
	
	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#convertVPCNameToId()
	 */
	@Override
	public void convertVPCNameToId() throws IOException {
		String ret = null;
		String JSON = OtcHttpMethods.get(OtcConfig.AUTH_URL_VPCS);

		List<HashMap<String, Object>> subnetmap = otcOutputHandler.parseJsontoTopLevelList(JSON,"vpcs");
		for (HashMap<String, Object> hashMap : subnetmap) {
			if( hashMap.get("name").equals(OtcConfig.VPCNAME) ) 
			{
				ret = (String) hashMap.get("id");
			}
		}
		OtcConfig.VPCID = ret;		
		
	}

	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#convertSUBNETNameToId()
	 */
	@Override
	public void convertSUBNETNameToId() throws IOException {
		String ret = null;
		String JSON = OtcHttpMethods.get(OtcConfig.AUTH_URL_SUBNETS);
		List<HashMap<String, Object>> subnetmap = otcOutputHandler.parseJsontoTopLevelList(JSON,"subnets");
		for (HashMap<String, Object> hashMap : subnetmap) {
			if( hashMap.get("name").equals(OtcConfig.SUBNETNAME) && hashMap.get("vpc_id").equals( OtcConfig.VPCID ) ) 
			{
				ret = (String) hashMap.get("id");
			}
		}
		OtcConfig.SUBNETID = ret;
	}

	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#convertIMAGENameToId()
	 */
	@Override
	public void convertIMAGENameToId() throws IOException {
		String ret = null;
		String JSON = OtcHttpMethods.get(OtcConfig.AUTH_URL_IMAGES);
		
		List<HashMap<String, Object>> subnetmap = otcOutputHandler.parseJsontoTopLevelList(JSON,"images");
		for (HashMap<String, Object> hashMap : subnetmap) {
			if( hashMap.get("name").equals(OtcConfig.IMAGENAME) ) 
			{
				ret = (String) hashMap.get("id");
			}
		}
		OtcConfig.IMAGE_ID = ret;
		
	}

	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#convertSECUGROUPNameToId()
	 */
	@Override
	public void convertSECUGROUPNameToId() throws IOException {
		String ret = null;
		String JSON = OtcHttpMethods.get(OtcConfig.AUTH_URL_SEC_GROUPS);

		List<HashMap<String, Object>> subnetmap = otcOutputHandler.parseJsontoTopLevelList(JSON,"security_groups");
		for (HashMap<String, Object> hashMap : subnetmap) {
			if( hashMap.get("name").equals(OtcConfig.SECUGROUPNAME) && hashMap.get("vpc_id").equals( OtcConfig.VPCID ) ) 
			{
				ret = (String) hashMap.get("id");
			}
		}
		OtcConfig.SECUGROUP = ret;
		
	}

	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#CreateLaunchConfiguration()
	 */
	@Override
	public void CreateLaunchConfiguration() {
		System.err.println("NOT IMPLEMENTED!");
		System.exit(-1);
		
	}

	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#AttachInstances()
	 */
	@Override
	public void AttachInstances() {
		System.err.println("NOT IMPLEMENTED!");
		System.exit(-1);

		// TODO Auto-generated method stub
		
	}

	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#AttachLoadBalancers()
	 */
	@Override
	public void AttachLoadBalancers() {
		System.err.println("NOT IMPLEMENTED!");
		System.exit(-1);

		// TODO Auto-generated method stub
		
	}

	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#CreateAutoScalingGroup()
	 */
	@Override
	public void CreateAutoScalingGroup() {
		System.err.println("NOT IMPLEMENTED!");
		System.exit(-1);

		// TODO Auto-generated method stub
		
	}

	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#DeleteAutoScalingGroup()
	 */
	@Override
	public void DeleteAutoScalingGroup() {
		System.err.println("NOT IMPLEMENTED!");
		System.exit(-1);

		// TODO Auto-generated method stub
		
	}

	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#DeleteLaunchConfiguration()
	 */
	@Override
	public void DeleteLaunchConfiguration() {
		System.err.println("NOT IMPLEMENTED!");
		System.exit(-1);		
	}
 
	
	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#getVolumeList()
	 */
	@Override
	public String getVolumeList() throws IOException {
		String ret = null;
		
		ret = OtcHttpMethods.get(OtcConfig.AUTH_URL_CLOUDVOLUMES + "/detail");

		otcOutputHandler.printLevel2(ret,"volumes",Arrays.asList("id","name","volume_type","size","status","bootable", "availability_zone","limit","attachments","source_volid","snapshot_id","description","created_at"));

		return ret;
	}
	
	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#CreateVolume()
	 */
	@Override
	public String CreateVolume() {
		String ret;
		String REQ_CREATE_CLOUDVOLUMES = "{ \"volume\": { \"backup_id\": "
				+ OtcConfig.SNAPSHOTID
				+ ", "
				+ "\"count\": "
				+ OtcConfig.NUMCOUNT				
				+ ", \"availability_zone\": \""
				+ OtcConfig.AZ
				+ "\",\"description\": \""
				+ OtcConfig.VOLUME_NAME
				+ "\", \"size\": "
				+ OtcConfig.VOLUME_SIZE
				+ ", \"name\": \""
			    + OtcConfig.VOLUME_NAME
				+ "\", \"imageRef\": "
				+ "null"
				+ ", \"volume_type\": \""
				+ OtcConfig.VOLUME_TYPE
				+ "\" } }";				

		System.out.println(REQ_CREATE_CLOUDVOLUMES);
		ret = OtcHttpMethods.post(OtcConfig.AUTH_URL_CLOUDVOLUMES, REQ_CREATE_CLOUDVOLUMES);
		System.out.println(ret);
		return ret;
		
	}

	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#AttachVolume()
	 */
	@Override
	public String AttachVolume() {
		String ret;
		String REQ_ATTACH_CLOUDVOLUMES = "{ \"volumeAttachment\": { \"volumeId\": \""
				+ OtcConfig.VOLUME_ID
				+ "\", \"device\": \""
				+ OtcConfig.EVS_DEVICE
				+ "\" } }";				

		System.out.println(REQ_ATTACH_CLOUDVOLUMES);
		ret = OtcHttpMethods.post(OtcConfig.AUTH_URL_ECS_ATTACHVOLUME, REQ_ATTACH_CLOUDVOLUMES);
		System.out.println(ret);
		return ret;
		
	}

	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#DetachVolume()
	 */
	@Override
	public String DetachVolume() {
		String ret;
		ret = OtcHttpMethods.delete(OtcConfig.AUTH_URL_ECS_DEATTACHVOLUME);
		System.out.println(ret);
		return ret;		
	}

	
	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#DeleteVolume()
	 */
	@Override
	public String DeleteVolume() {
		String ret;
		ret = OtcHttpMethods.delete(OtcConfig.AUTH_URL_CLOUDVOLUMES + "/" + OtcConfig.VOLUME_ID );
		System.out.println(ret);
		return ret;		
	}
	
	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#DescribeQuotas()
	 */
	@Override
	public String  DescribeQuotas() throws IOException {
		String ret = null;
		ret = OtcHttpMethods.get(OtcConfig.AUTH_URL_ECS_QUOTAS);
		otcOutputHandler.printJsonTableTransverse(ret);		
		return ret;
	}

	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#getBackupList()
	 */
	@Override
	public String getBackupList() throws IOException {
		String ret = null;
		ret = OtcHttpMethods.get(OtcConfig.AUTH_URL_BACKUP_LIST);
		//System.out.println(ret); 
		otcOutputHandler.printJsonTableTransverse(ret);		
		return ret;
		
	}

	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#RestoreBackupDisk()
	 */
	@Override
	public String RestoreBackupDisk() {
		String ret;
		String REQ_RESTORE_BACKUP = "{ \"restore\":{ \"volume_id\":\""
				+ OtcConfig.VOLUME_ID
				+ "\" } }";

		System.out.println(REQ_RESTORE_BACKUP);
		ret = OtcHttpMethods.post(OtcConfig.AUTH_URL_BACKUP_ACTION + "/"+ OtcConfig.SNAPSHOTID + "/restore", REQ_RESTORE_BACKUP);
		System.out.println(ret);
		return ret;							
	}

	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#DeleteBackup()
	 */
	@Override
	public String DeleteBackup() {
		String ret;
		ret = OtcHttpMethods.post(OtcConfig.AUTH_URL_BACKUP_ACTION + "/"+ OtcConfig.SNAPSHOTID,"");
		System.out.println(ret);
		return ret;
		
	}

	/* (non-Javadoc)
	 * @see com.tsystems.otc.IOtcServiceCalls#CreateBackup()
	 */
	@Override
	public String CreateBackup() {
		String ret;
		String REQ_CREATE_BACKUP = "{ \"backup\":{ \""
				+ "volume_id\":\""
				+ OtcConfig.VOLUME_ID
				+ "\", "
				+ "\"name\":\""
				+ OtcConfig.DESCRIPTION
				+ "\", \"description\":\""
				+ OtcConfig.DESCRIPTION
				+ "\" } }";				

		System.out.println(REQ_CREATE_BACKUP);
		ret = OtcHttpMethods.post(OtcConfig.AUTH_URL_BACKUP_ACTION, REQ_CREATE_BACKUP);
		System.out.println(ret);
		return ret;							
	}

}