/* 
 * Copyright (c) 2016 T-Systems GmbH
 * Germany
 * All rights reserved.
 * 
 * Name: ParamFactory.java
 * Author: zsonagy
 * Datum: 08.03.2016
 */

package com.tsystems.otc;

import java.io.IOException;
import java.net.MalformedURLException;
import java.util.Date;
import java.util.concurrent.TimeoutException;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import com.fasterxml.jackson.core.JsonParseException;
import com.fasterxml.jackson.databind.JsonMappingException;
import com.tsystems.otc.aws.S3;
import com.tsystems.otc.config.ConfigLoader;
import com.tsystems.otc.config.OtcConfig;
import com.tsystems.otc.imp.DefaultOtcServiceCalls;
import com.tsystems.otc.interfaces.IOtcServiceCalls;
import com.tsystems.otc.params.ParamFactory;

/***
 * Otc Command line client Main application
 * 
 * @author zsonagy
 *
 */
 
public class OtcMain {

	static final Logger log = LogManager.getLogger(OtcMain.class.getName());
	IOtcServiceCalls otcServiceCalls = (IOtcServiceCalls) new DefaultOtcServiceCalls();
	S3 s3 = new S3();
	OtcConfig tempconfig = OtcConfig.getInstance();

	
	public static void main(String[] args) {
		try {
			OtcMain otcMain = new OtcMain();
			otcMain.doMain(args);
		} catch (Exception e) {
			e.printStackTrace();
			log.error(e);
		}
	}

	private void doMain(String[] args) throws JsonParseException,
			JsonMappingException, IOException, Exception, TimeoutException,
			InterruptedException {
		log.info("Starting OTC ...");
		Date start = new Date();
		log.info("----------------------------------------------------------------");
		log.info("LOAD OTC GLOBAL CONFIG ...");


		ParamFactory.parseOtcOptions(args, tempconfig);

		if (OtcConfig.MAINCOM.equalsIgnoreCase("configure")) {
			ConfigLoader.reSetUserValues();
			System.exit(0);
		}

		if (OtcConfig.MAINCOM.equalsIgnoreCase("configure-proxy")) {
			ConfigLoader.reSetProxyValues();
			System.exit(0);
		}

		if (OtcConfig.MAINCOM.equalsIgnoreCase("version")) {
			ConfigLoader.printVersion();
			System.exit(0);
		}

		try {
			ConfigLoader.readUserValues();			
			ConfigLoader.readProxyValues();
			ConfigLoader.validateConfig();
		} catch (Exception e) {
			log.error("LOAD OTC GLOBAL CONFIG ...", e);
			System.out
					.println("Configuration file error. \nPlease run following command: \n	otc configure ");
			System.exit(1);
		}

		handleCommands(args);

		log.info("----------------------------------------------------------------");
		Date end = new Date();
		log.info("OTC Cli DONE! (" + ((end.getTime() - start.getTime()) / 1000)
				+ " s)");
	}

	private void handleCommands(String[] args) throws MalformedURLException,
			IOException, InterruptedException, Exception {
		if (OtcConfig.MAINCOM.equalsIgnoreCase("s3")
				&& OtcConfig.SUBCOM.equalsIgnoreCase("ls") && args.length > 2
				&& !args[2].startsWith("--")) {
			s3.listBucketContent(args[2]);
		} else if (OtcConfig.MAINCOM.equalsIgnoreCase("s3")
				&& OtcConfig.SUBCOM.equalsIgnoreCase("ls")) {
			s3.listBuckets();
		} else if (OtcConfig.MAINCOM.equalsIgnoreCase("s3")
				&& OtcConfig.SUBCOM.equalsIgnoreCase("cp")) {
			s3.fileCopy(args[2], args[3]);
		} else if (OtcConfig.MAINCOM.equalsIgnoreCase("s3")
				&& OtcConfig.SUBCOM.equalsIgnoreCase("rm")) {
			s3.remove(args[2]);
		} else if (OtcConfig.MAINCOM.equalsIgnoreCase("ecs")
				&& OtcConfig.SUBCOM.equalsIgnoreCase("create-snapshot")) {
			otcServiceCalls.CreateBackup();
		} else if (OtcConfig.MAINCOM.equalsIgnoreCase("ecs")
				&& OtcConfig.SUBCOM.equalsIgnoreCase("delete-snapshot")) {
			otcServiceCalls.DeleteBackup();
/*NO RESTORE BACKUP becasue this part of the create volume
 * 		} else if (OtcConfig.MAINCOM.equalsIgnoreCase("ecs")
				&& OtcConfig.SUBCOM.equalsIgnoreCase("restore-snapshot")) {
			OtcServiceCalls.RestoreBackupDisk();
*/		
			} else if (OtcConfig.MAINCOM.equalsIgnoreCase("ecs")
				&& OtcConfig.SUBCOM.equalsIgnoreCase("describe-snapshots")) {
			otcServiceCalls.getBackupList();
		}

		else if (OtcConfig.MAINCOM.equalsIgnoreCase("autoscaling")
				&& OtcConfig.SUBCOM
						.equalsIgnoreCase("create-launch-configuration")) {
			otcServiceCalls.CreateLaunchConfiguration();
		} else if (OtcConfig.MAINCOM.equalsIgnoreCase("autoscaling")
				&& OtcConfig.SUBCOM
						.equalsIgnoreCase("delete-launch-configuration")) {
			otcServiceCalls.DeleteLaunchConfiguration();
		}

		else if (OtcConfig.MAINCOM.equalsIgnoreCase("autoscaling")
				&& OtcConfig.SUBCOM.equalsIgnoreCase("attach-instances")) {
			otcServiceCalls.AttachInstances();
		} else if (OtcConfig.MAINCOM.equalsIgnoreCase("autoscaling")
				&& OtcConfig.SUBCOM.equalsIgnoreCase("attach-load-balancers")) {
			otcServiceCalls.AttachLoadBalancers();
		} else if (OtcConfig.MAINCOM.equalsIgnoreCase("autoscaling")
				&& OtcConfig.SUBCOM.equalsIgnoreCase("attach-load-balancers")) {
			otcServiceCalls.AttachLoadBalancers();
		} else if (OtcConfig.MAINCOM.equalsIgnoreCase("autoscaling")
				&& OtcConfig.SUBCOM.equalsIgnoreCase("attach-load-balancers")) {
			otcServiceCalls.AttachLoadBalancers();
		}

		else if (OtcConfig.MAINCOM.equalsIgnoreCase("autoscaling")
				&& OtcConfig.SUBCOM
						.equalsIgnoreCase("create-auto-scaling-group")) {
			otcServiceCalls.CreateAutoScalingGroup();
		}

		else if (OtcConfig.MAINCOM.equalsIgnoreCase("autoscaling")
				&& OtcConfig.SUBCOM
						.equalsIgnoreCase("delete-auto-scaling-group")) {
			otcServiceCalls.DeleteAutoScalingGroup();
		}

		else if (OtcConfig.MAINCOM.equalsIgnoreCase("s3api")
				&& OtcConfig.SUBCOM.equalsIgnoreCase("create-bucket")) {
			s3.createBucket();
		} else if (OtcConfig.MAINCOM.equalsIgnoreCase("s3api")
				&& OtcConfig.SUBCOM.equalsIgnoreCase("get-object")) {
			s3.getObject();
		} else if (OtcConfig.MAINCOM.equalsIgnoreCase("ecs")
				&& OtcConfig.SUBCOM.equalsIgnoreCase("describe-instances")
				&& args.length > 2 && !args[2].startsWith("--")) {

			
			otcServiceCalls.getECSVM(args[2]);
		} else if (
				( OtcConfig.MAINCOM.equalsIgnoreCase("ecs") && OtcConfig.SUBCOM.equalsIgnoreCase("describe-instances" ) ) || 
						( OtcConfig.MAINCOM.equalsIgnoreCase("ecs") && OtcConfig.SUBCOM.equalsIgnoreCase("ls" ) )
						
						
						) {
			
			otcServiceCalls.getECSList();
		} else if (OtcConfig.MAINCOM.equalsIgnoreCase("ecs")
				&& OtcConfig.SUBCOM.equalsIgnoreCase("list-detail")) {
			
			otcServiceCalls.getECSDetail();
		} else if (OtcConfig.MAINCOM.equalsIgnoreCase("ecs")
				&& OtcConfig.SUBCOM.equalsIgnoreCase("run-instances")) {
			

			if (OtcConfig.VPCNAME != null) {
				otcServiceCalls.convertVPCNameToId();
			}

			if (OtcConfig.SUBNETNAME != null) {
				otcServiceCalls.convertSUBNETNameToId();
			}

			if (OtcConfig.IMAGENAME != null) {
				otcServiceCalls.convertIMAGENameToId();
			}

			if (OtcConfig.SECUGROUPNAME != null) {
				otcServiceCalls.convertSECUGROUPNameToId();
			}

			if (OtcConfig.INSTANCE_TYPE_NAME != null) {
				otcServiceCalls.convertFlavorNameToId();
			}

			otcServiceCalls.ECSCreate();

			// wait implementation after create
			// call ecs jobs interface in every 5 sec and until "RUNNING" or
			// "INIT" state
			if (OtcConfig.WAIT_CREATE.equalsIgnoreCase("true")) {

				OtcConfig.resetUrlVars();
				
				otcServiceCalls.getECSJOBList();
				System.out.print("#");
				while ("RUNNING".equalsIgnoreCase(OtcConfig.ECSCREATEJOBSTATUS)
						|| "INIT"
								.equalsIgnoreCase(OtcConfig.ECSCREATEJOBSTATUS)) {
					Thread.sleep(5000);
					otcServiceCalls.getECSJOBList();
					System.out.print("#");
				}
				System.out.println("ECS Creation status: "
						+ OtcConfig.ECSCREATEJOBSTATUS);
			}

			if ("SUCCESS".equalsIgnoreCase(OtcConfig.ECSCREATEJOBSTATUS)) {
				System.exit(1);
			}
		} else if (OtcConfig.MAINCOM.equalsIgnoreCase("ecs")
				&& OtcConfig.SUBCOM.equalsIgnoreCase("reboot-instances")) {
			OtcConfig.ECSACTION = "reboot";

			if (OtcConfig.INSTANCE_ID == null || OtcConfig.INSTANCE_ID.equalsIgnoreCase("")) {
				System.out.println("Error. Must be specify the Instance ID!");
				ParamFactory.printHelp();
				System.exit(1);
			}

			
			otcServiceCalls.ECSAction();
		} else if (OtcConfig.MAINCOM.equalsIgnoreCase("ecs")
				&& OtcConfig.SUBCOM.equalsIgnoreCase("start-instances")) {
			OtcConfig.ECSACTION = "os-start";

			if (OtcConfig.INSTANCE_ID == null || OtcConfig.INSTANCE_ID.equalsIgnoreCase("")) {
				System.out.println("Error. Must be specify the Instance ID!");
				ParamFactory.printHelp();
				System.exit(1);
			}

			
			otcServiceCalls.ECSAction();
		} else if (OtcConfig.MAINCOM.equalsIgnoreCase("ecs")
				&& OtcConfig.SUBCOM.equalsIgnoreCase("stop-instances")) {
			OtcConfig.ECSACTION = "os-stop";

			if (OtcConfig.INSTANCE_ID == null || OtcConfig.INSTANCE_ID.equalsIgnoreCase("")) {
				System.out.println("Error. Must be specify the Instance ID!");
				ParamFactory.printHelp();
				System.exit(1);
			}
			
			otcServiceCalls.ECSAction();

		} else if (OtcConfig.MAINCOM.equalsIgnoreCase("ecs")
				&& OtcConfig.SUBCOM.equalsIgnoreCase("delete-instances")) {


			if (OtcConfig.INSTANCE_ID.equalsIgnoreCase("")) {
				System.out.println("Error. Must be specify the Instance ID!");
				ParamFactory.printHelp();
				System.exit(1);
			}
			otcServiceCalls.ECSDelete();
		
		
		} else if (OtcConfig.MAINCOM.equalsIgnoreCase("ecs")
				&& OtcConfig.SUBCOM.equalsIgnoreCase("job")) {
			OtcConfig.ECSTASKID = args[3];
			OtcConfig.AUTH_URL_ECS_JOB = "https://ecs.eu-de.otc.t-systems.com/v1/"
					+ OtcConfig.PROJECT_ID + "/jobs/$ECSTASKID";

			
			otcServiceCalls.getECSJOBList();
		} else if (OtcConfig.MAINCOM.equalsIgnoreCase("ecs")
				&& OtcConfig.SUBCOM.equalsIgnoreCase("describe-vpcs")) {
			otcServiceCalls.getIamToken();
			otcServiceCalls.getVPCList();
		} else if (OtcConfig.MAINCOM.equalsIgnoreCase("ecs")
				&& OtcConfig.SUBCOM.equalsIgnoreCase("create-vpc")) {
			
			otcServiceCalls.VPCCreate();
		} else if (OtcConfig.MAINCOM.equalsIgnoreCase("ecs")
				&& OtcConfig.SUBCOM.equalsIgnoreCase("describe-addresses")) {
			
			otcServiceCalls.getPUBLICIPSList();

		} else if (OtcConfig.MAINCOM.equalsIgnoreCase("ecs")
				&& OtcConfig.SUBCOM.equalsIgnoreCase("allocate-address")) {
			otcServiceCalls.PUBLICIPSAllocate();
		} else if (OtcConfig.MAINCOM.equalsIgnoreCase("ecs")
				&& OtcConfig.SUBCOM.equalsIgnoreCase("associate-address")) {

			if (OtcConfig.PUBLICIP != null) {
				otcServiceCalls.convertPublicIpNameToId();
			}

			otcServiceCalls.PUBLICIPSAssociate();
		}

		else if (OtcConfig.MAINCOM.equalsIgnoreCase("ecs")
				&& OtcConfig.SUBCOM.equalsIgnoreCase("describe-subnets")) {
			
			otcServiceCalls.getSUBNETList();
		} else if (OtcConfig.MAINCOM.equalsIgnoreCase("ecs")
				&& OtcConfig.SUBCOM.equalsIgnoreCase("create-subnet")) {
			

			if (OtcConfig.VPCNAME != null) {
				otcServiceCalls.convertVPCNameToId();
			}
			otcServiceCalls.SUBNETCreate();
		} else if (OtcConfig.MAINCOM.equalsIgnoreCase("ecs")
				&& OtcConfig.SUBCOM
						.equalsIgnoreCase("describe-security-groups")) {
			
			// OtcConfig.VPCNAME = args[3];
			if (OtcConfig.VPCNAME != null) {
				otcServiceCalls.convertVPCNameToId();
			}

			otcServiceCalls.getSECGROUPList();
		} else if (OtcConfig.MAINCOM.equalsIgnoreCase("ecs")
				&& OtcConfig.SUBCOM.equalsIgnoreCase("create-security-group")) {
			

			if (OtcConfig.VPCNAME != null) {
				otcServiceCalls.convertVPCNameToId();
			}

			otcServiceCalls.SECGROUPCreate();

		} else if (OtcConfig.MAINCOM.equalsIgnoreCase("security-group-rules")
				&& OtcConfig.SUBCOM.equalsIgnoreCase("list")) {					

			if (args.length < 3) {
				System.out
						.println("Error. Must be specify the Security Rule Group ID!");
				ParamFactory.printHelp();
				System.exit(1);
			}
			OtcConfig.SECUGROUP = args[3];

			OtcConfig.AUTH_URL_SEC_GROUP_RULE = "https://vpc.eu-de.otc.t-systems.com/v1/"
					+ OtcConfig.PROJECT_ID
					+ "/security-group-rules/"
					+ OtcConfig.SECUGROUP;
			otcServiceCalls.getSECGROUPRULESList();

		} else if (OtcConfig.MAINCOM.equalsIgnoreCase("ecs")
				&& (OtcConfig.SUBCOM
						.equalsIgnoreCase("authorize-security-group-ingress") || OtcConfig.SUBCOM
						.equalsIgnoreCase("authorize-security-group-egress"))) {

			if (OtcConfig.SUBCOM
					.equalsIgnoreCase("authorize-security-group-ingress")) {
				OtcConfig.DIRECTION = "ingress";
			} else {
				OtcConfig.DIRECTION = "egress";
			}

			if (OtcConfig.VPCNAME != null) {
				otcServiceCalls.convertVPCNameToId();
			}

			if (OtcConfig.SECUGROUPNAME != null) {
				otcServiceCalls.convertSECUGROUPNameToId();
			}

			otcServiceCalls.SECGROUPRULECreate();

		} else if (OtcConfig.MAINCOM.equalsIgnoreCase("ecs")
				&& OtcConfig.SUBCOM.equalsIgnoreCase("describe-images")) {
			
			otcServiceCalls.getIMAGEList();
		} else if (OtcConfig.MAINCOM.equalsIgnoreCase("ecs")
				&& OtcConfig.SUBCOM.equalsIgnoreCase("describe-flavors")) {
			
			otcServiceCalls.getFLAVORList();
		} else if (OtcConfig.MAINCOM.equalsIgnoreCase("ecs")
				&& OtcConfig.SUBCOM.equalsIgnoreCase("describe-key-pairs")) {
			
			otcServiceCalls.getKEYPAIRList();
		} else if (OtcConfig.MAINCOM.equalsIgnoreCase("ecs")
				&& OtcConfig.SUBCOM.equalsIgnoreCase("create-key-pair")) {
			
			otcServiceCalls.KEYPAIRCreate();
		} else if (OtcConfig.MAINCOM.equalsIgnoreCase("ecs")
				&& OtcConfig.SUBCOM.equalsIgnoreCase("delete-key-pair")) {
			
			otcServiceCalls.KEYPAIRDelete();
		} else if (OtcConfig.MAINCOM.equalsIgnoreCase("ecs")
				&& OtcConfig.SUBCOM.equalsIgnoreCase("create-volume")) {
			
				
			if( OtcConfig.VOLUME_NAME == null || OtcConfig.VOLUME_NAME.length() == 0 )
			{
				otcServiceCalls.RestoreBackupDisk();
			}			
			else
			{
				otcServiceCalls.CreateVolume();
			}
		}
		else if (OtcConfig.MAINCOM.equalsIgnoreCase("ecs")
				&& OtcConfig.SUBCOM.equalsIgnoreCase("describe-volumes")) {
			otcServiceCalls.getVolumeList();
		}
		else if (OtcConfig.MAINCOM.equalsIgnoreCase("ecs")
				&& OtcConfig.SUBCOM.equalsIgnoreCase("attach-volume")) {
			otcServiceCalls.AttachVolume();
		}

		else if (OtcConfig.MAINCOM.equalsIgnoreCase("ecs")
				&& OtcConfig.SUBCOM.equalsIgnoreCase("detach-volume")) {

			otcServiceCalls.DetachVolume();
		}

		else if (OtcConfig.MAINCOM.equalsIgnoreCase("ecs")
				&& OtcConfig.SUBCOM.equalsIgnoreCase("delete-volume")) {

			otcServiceCalls.DeleteVolume();
		}
		
		
		else if (OtcConfig.MAINCOM.equalsIgnoreCase("ecs")
				&& OtcConfig.SUBCOM.equalsIgnoreCase("describe-quotas")) {
			
			otcServiceCalls.DescribeQuotas();
		}

		else if (OtcConfig.MAINCOM.equalsIgnoreCase("iam")
				&& OtcConfig.SUBCOM.equalsIgnoreCase("token")) {
			otcServiceCalls.getIamToken();
			System.out.println(OtcConfig.TOKEN);
		} else {
			ParamFactory.printHelp();
		}
	}

}