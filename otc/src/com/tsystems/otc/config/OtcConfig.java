/* 
 * Copyright (c) 2016 T-Systems GmbH
 * Germany
 * All rights reserved.
 * 
 * Name: ParamFactory.java
 * Author: zsonagy
 * Datum: 08.03.2016
 */

package com.tsystems.otc.config;

import com.jayway.jsonpath.Configuration;

public class OtcConfig {

	private static OtcConfig instance = null;

	// for singleton instances
	protected OtcConfig() {
	}

	public static OtcConfig getInstance() {
		if (instance == null) {
			instance = new OtcConfig();
		}
		return instance;
	}

	public static String OTC_USER_DIR = System.getProperty("user.home")
			+ "/.otc";
	public static String OTC_USER_FILE = OTC_USER_DIR + "/config";
	public static String OTC_PROXY_FILE = OTC_USER_DIR + "/common";

	// replace real AK
	public static String ak;

	// replace real SK
	public static String sk;

	// default region definition
	public static String region = "eu-de";

	// replace real service name
	public static final String serviceName = "serviceName";
	
	public static String PROJECT_ID;
	public static String PROJECT_NAME="eu-de";
	//public static String SERVER_ID;
	public static String USERNAME ;
	public static String PASSWORD ;
	public static String DOMAIN ;
	public static String ECSTASKID = null;

	public static String SECUGROUPNAME = "default";
	public static String VPCNAME = "default-vpc";
	public static String SUBNETNAME = "default-subnet";
	public static String IMAGENAME = "Community-CentOS-7.0-x86_64-2015-0";
	public static String NUMCOUNT = "1";
	public static String INSTANCE_TYPE = "computev1-1";
	public static String INSTANCE_TYPE_NAME;
	public static String INSTANCE_NAME = "default";
	public static String INSTANCE_ID;

	public static String ADMINPASS = null;
	public static String CREATE_ECS_WITH_PUBLIC_IP = "false";

	public static String ECSACTIONTYPE = "HARD";
	public static String WAIT_CREATE = "false";
	public static String KEYNAME = null;
	public static String PUBLICKEY = "";

	public static int VOLUME_SIZE;
	public static String VOLUME_TYPE;
	public static String VOLUME_NAME;
	public static String VOLUME_ID;
	public static String ATTACHMENT_ID;
	public static String EVS_DEVICE;

	// # fetch main command
	public static String MAINCOM = null;
	public static String SUBCOM = null;
	public static String ECSACTION = null;

	public static String DEFAULT_HOST="46.29.103.37";
	
	public static String S3_HOSTNAME ;
	public static String IAM_AUTH_URL;
	
										 
	public static String AUTH_URL_ECS;
	public static String AUTH_URL_ECS_JOB ;
	public static String AUTH_URL_ECS_CLOUD ;

	public static String AUTH_URL_ECS_CLOUDSERVERS_BASE ;
	
	public static String AUTH_URL_ECS_CLOUD_ACTION ;
	public static String AUTH_URL_VPCS ;
	public static String AUTH_URL_PUBLICIPS ;
	public static String AUTH_URL_SEC_GROUPS ;
	public static String AUTH_URL_SEC_GROUP_RULE ;
	public static String AUTH_URL_SUBNETS ;
	public static String AUTH_URL_IMAGES ;
	public static String AUTH_URL_FLAVORS;
	public static String AUTH_URL_KEYNAMES ;
	public static String AUTH_URL_CLOUDVOLUMES ;
	public static String AUTH_URL_ECS_ATTACHVOLUME ;
	public static String AUTH_URL_ECS_DEATTACHVOLUME ;
	public static String AUTH_URL_ECS_QUOTAS ;
	public static String AUTH_URL_BACKUP_ACTION ;
	public static String AUTH_URL_BACKUP_LIST ;

	
	public static String FILE1 = null;
	public static String FILE2 = null;
	public static String FILE3 = null;
	public static String FILE4 = null;
	public static String FILE5 = null;

	public static String GWIP;

	public static String PRIMARYDNS;

	public static String SECDNS;

	public static String AZ = "eu-de-01";

	public static String VPCID;
	public static String CIDR = null;
	public static String DIRECTION;

	public static String PORTMIN;

	public static String ETHERTYPE;

	public static String PORTMAX;

	public static String PROTOCOL;

	public static String SECUGROUP;

	public static String IMAGE_ID;

	public static String SUBNETID;
	public static String NETWORKINTERFACEID;
	
	public static String ECSCREATEJOBSTATUS;

	public static String TOKEN;

	// proxy settings
	public static String PROXY_URL;
	public static int PROXY_PORT;

	// S3 settings 
	public static String S3BUCKET;
	public static String S3OBJECT;
	public static boolean S3RECURSIVE;
	
	public static String OUTPUT_FORMAT = "Table";

	// backups 
	public static String SNAPSHOTID;
	public static String DESCRIPTION;
	public static String PUBLICIPID;
	public static String PUBLICIP;
	public static String DELETE_PUBLICIP = "true";
	public static String DELETE_VOLUME = "true";
	public static String QUERY;
	

	// reset values 
	public static void resetUrlVars() {
		S3_HOSTNAME = "obs.otc.t-systems.com";//DEFAULT_HOST;
		IAM_AUTH_URL = "https://"+ DEFAULT_HOST +":443/v3/auth/tokens";
		AUTH_URL_ECS = "https://"+ DEFAULT_HOST +"/v2/" + PROJECT_ID
				+ "/servers";
//		AUTH_URL_ECS_JOB = "https://"+ DEFAULT_HOST +"/v2/"
//				+ PROJECT_ID + "/jobs/" + ECSTASKID;
		AUTH_URL_ECS_CLOUD = "https://"+ DEFAULT_HOST +"/v1/"
				+ PROJECT_ID + "/cloudservers";
		AUTH_URL_ECS_CLOUD_ACTION = "https://"+ DEFAULT_HOST +"/v1/"
				+ PROJECT_ID + "/cloudservers/action";
		AUTH_URL_VPCS = "https://"+ DEFAULT_HOST +"/v1/" + PROJECT_ID
				+ "/vpcs";
		AUTH_URL_PUBLICIPS = "https://"+ DEFAULT_HOST +"/v1/"
				+ PROJECT_ID + "/publicips";
		AUTH_URL_SEC_GROUPS = "https://"+ DEFAULT_HOST +"/v1/"
				+ PROJECT_ID + "/security-groups";
//		AUTH_URL_SEC_GROUP_RULE = "https://"+ DEFAULT_HOST +"/v2.0/security-group-rules";
		AUTH_URL_SUBNETS = "https://"+ DEFAULT_HOST +"/v1/"
				+ PROJECT_ID + "/subnets";
		AUTH_URL_IMAGES = "https://"+ DEFAULT_HOST +"/v2/images";
		AUTH_URL_FLAVORS = "https://"+ DEFAULT_HOST +"/v1/"
				+ PROJECT_ID + "/cloudservers/flavors";
		AUTH_URL_KEYNAMES = "https://"+ DEFAULT_HOST +"/v2/"
				+ PROJECT_ID + "/os-keypairs";
		AUTH_URL_ECS_ATTACHVOLUME = "https://"+ DEFAULT_HOST +"/v1/"
				+ PROJECT_ID + "/cloudservers/" + INSTANCE_ID + "/attachvolume";
		AUTH_URL_ECS_DEATTACHVOLUME = "https://"+ DEFAULT_HOST +"/v1/"
				+ PROJECT_ID + "/cloudservers/" + INSTANCE_ID + "/detachvolume/"
				+ VOLUME_ID;
		AUTH_URL_ECS_QUOTAS = "https://"+ DEFAULT_HOST +"/v2/"
				+ PROJECT_ID + "/os-quota-sets/" + PROJECT_ID + "?usage=True";

		AUTH_URL_BACKUP_ACTION =  "https://"+ DEFAULT_HOST +"/v2/"
				+ PROJECT_ID + "/cloudbackups";
		AUTH_URL_BACKUP_LIST =  "https://"+ DEFAULT_HOST +"/v2/"
				+ PROJECT_ID + "/backups/detail";
	
		AUTH_URL_ECS_CLOUDSERVERS_BASE = "https://"+ DEFAULT_HOST +"/v1/"
				+ PROJECT_ID + "/cloudservers";
		
		AUTH_URL_CLOUDVOLUMES = "https://"+ DEFAULT_HOST +"/v2/"
				+ PROJECT_ID + "/cloudvolumes";		
		AUTH_URL_ECS_JOB = "https://"+ DEFAULT_HOST +"/v1/"
				+ PROJECT_ID + "/jobs/" + ECSTASKID;
		
		AUTH_URL_SEC_GROUP_RULE = "https://vpc.eu-de.otc.t-systems.com/v1/"
				+ PROJECT_ID
				+ "/security-group-rules/"
				+ SECUGROUP;		
	}


	
}