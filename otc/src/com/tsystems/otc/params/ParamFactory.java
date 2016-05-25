/* 
 * Copyright (c) 2016 T-Systems GmbH
 * Germany
 * All rights reserved.
 * 
 * Name: ParamFactory.java
 * Author: zsonagy
 * Datum: 08.03.2016
 */
package com.tsystems.otc.params;

import java.io.OutputStream;
import java.io.PrintWriter;

import org.apache.commons.cli.BasicParser;
import org.apache.commons.cli.CommandLine;
import org.apache.commons.cli.CommandLineParser;
import org.apache.commons.cli.HelpFormatter;
import org.apache.commons.cli.Options;
import org.apache.commons.cli.ParseException;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import com.tsystems.otc.config.OtcConfig;

/**
 * Parsing command line arguments and storing to OtcConfig
 * @author zsoltn
 *  
 */
public class ParamFactory {
	static final Logger log = LogManager.getLogger(ParamFactory.class.getName());

	static Options options = new Options();

	static {
		options.addOption("k", "key-name", true,
				"SSH key name| S3 Object key");
		options.addOption(null, "public-key", true,
				"Import public key for SSH keypairs");

		options.addOption(null, "admin-pass", true, "Admin password of the started VM");
		options.addOption(null, "instance-name", true, "Instance name of the VM");
		options.addOption(null, "instance-ids", true, "Instance Id of the VM");
		options.addOption(null, "volume-id", true, "Volume Id of the EVS volume");
		options.addOption(null, "attachment-id", true, "Attachment Id of the EVS volume");

		options.addOption(null, "device", true, "Device of the EVS volume");

		
		options.addOption(null, "file1", true,"Name of the #1 file to be injected to VM. Format: target=source");
		options.addOption(null, "file2", true,"Name of the #2 file to be injected to VM. Format: target=source");
		options.addOption(null, "file3", true,"Name of the #3 file to be injected to VM. Format: target=source");
		options.addOption(null, "file4", true,"Name of the #4 file to be injected to VM. Format: target=source");
		options.addOption(null, "file5", true,"Name of the #5 file to be injected to VM. Format: target=source");

		options.addOption(null, "instance-type", true,"Flavor type of the VM");

		
		options.addOption(null, "image-name", true,"Name of the image reference will used during VM creation");
		options.addOption(null, "image-id", true,"Id of the image reference will use during VM creation");

		options.addOption("n", "count", true,"Number of VM will be created");
		options.addOption(null, "subnet-name", true,"Name of the subnet reference will use during VM creation");
		options.addOption(null, "subnet-id", true,"Id of the subnet will use during VM creation");
		options.addOption(null, "network-interface-id", true,"Network interface Id of NIC");
		
		
		options.addOption(null, "vpc-name", true,"Name of the VPC reference will use during VM creation");
		options.addOption(null, "vpc-id", true,"Id of the VPC will use during VM creation");
		
		options.addOption(null, "cidr", true,"CIDR of the subnet will use during subnet creation");
		options.addOption(null, "gateway-ip", true,"Gateway Ip of the subnet ");
		options.addOption(null, "primary-dns", true,"Primary dns of the subnet ");
		options.addOption(null, "secondary-dns", true,"Secondary dns of the subnet ");

		options.addOption(null, "availability-zone", true,"Availability-zone definition");

		options.addOption(null, "region", true,"Region definition");

		options.addOption(null, "group-name", true,"Name of the security group");
		options.addOption(null, "security-group-ids", true,"Id of the security group");
		
		options.addOption("p", "associate-public-ip-address", false,"VM will get EIP public IP");
		
		options.addOption(null, "public-ip", true,"Public IP for association");
		options.addOption(null, "public-ip-id", true,"Public IP ID for association");
		options.addOption(null, "bucket", true,"S3 Bucket");
		options.addOption(null, "key", true,"S3 Object Name");
		
		options.addOption(null, "direction", true,"Direction of the security group rule");
		options.addOption(null, "portmin", true,"Lower por of the specific security group rule");
		options.addOption(null, "portmax", true,"Upper  port of the specific security group rule");
		options.addOption(null, "protocol", true,"Protocol of the specific security group rule");
		options.addOption(null, "ethertype", true,"Ethertype of the specific security group rule ");
		options.addOption(null, "output", true,"Output format");
		options.addOption(null, "query", true,"JSON Path query");
		options.addOption(null, "size", true,"Size of the EVS disk");
		options.addOption(null, "volume-type", true,"Volume type of the EVS disk [SSD,SAS,SATA]");
		options.addOption(null, "volume-name", true,"Volume name of the EVS disk");
		options.addOption(null, "description", true,"Description definition ( eg: backups)");
		options.addOption(null, "snapshot-id", true,"Snapshot id of the  backup");
		options.addOption(null, "wait-instance-running", false,"Wait instance running (only for run-instance command)");
		
		
	}

	// create the command line parser
	private static CommandLineParser parser = new BasicParser();

	
	/**
	 * parse command line arguments and store in global config 
	 * @param args command line arguments 
	 * @param config global config container 
	 */
	public static void parseOtcOptions(String[] args,
			OtcConfig config) {

		//
			
		if(args.length < 1 )
		{
			printHelp();
			System.exit(1);
		}
		OtcConfig.MAINCOM = args[0];
		if( args.length > 1)
		{
		OtcConfig.SUBCOM = args[1];
		}
		
		
		try {
			
			// parse the command line arguments
			CommandLine line = parser.parse(options, args);

			
			// validate that block-size has been set
			if (line.hasOption("key-name")) {
				
				OtcConfig.KEYNAME = line.getOptionValue("key-name");
				log.info( "key-name: " + line.getOptionValue("key-name"));
			}

			if (line.hasOption("public-key")) {
				
				OtcConfig.PUBLICKEY = line.getOptionValue("public-key");
				log.info( "public-key: " + line.getOptionValue("public-key"));
			}
			
			
			if (line.hasOption("admin-pass")) {
				
				OtcConfig.ADMINPASS= line.getOptionValue("admin-pass");
				log.info( "admin-pass: " + line.getOptionValue("admin-pass"));
			}

			if (line.hasOption("instance-name")) {
				
				OtcConfig.INSTANCE_NAME= line.getOptionValue("instance-name");
				log.info( "instance-name: " + line.getOptionValue("instance-name"));
			}

			if (line.hasOption("instance-ids")) {
				
				OtcConfig.INSTANCE_ID= line.getOptionValue("instance-ids");
				log.info( "instance-ids: " + line.getOptionValue("instance-ids"));
			}

			if (line.hasOption("volume-id")) {
				
				OtcConfig.VOLUME_ID= line.getOptionValue("volume-id");
				log.info( "volume-id: " + line.getOptionValue("volume-id"));
			}

			if (line.hasOption("attachment-id")) {
				
				OtcConfig.ATTACHMENT_ID= line.getOptionValue("attachment-id");
				log.info( "attachment-id: " + line.getOptionValue("attachment-id"));
			}
			
			
			if (line.hasOption("file1")) {
				
				OtcConfig.FILE1= line.getOptionValue("file1");
				log.info( "file1: " + line.getOptionValue("file1"));
			}
			if (line.hasOption("file2")) {
				OtcConfig.FILE2= line.getOptionValue("file2");
				log.info( "file2: " + line.getOptionValue("file1"));
			}
			if (line.hasOption("file3")) {
				
				OtcConfig.FILE3= line.getOptionValue("file3");
				log.info( "file3: " + line.getOptionValue("file3"));
			}
			if (line.hasOption("file4")) {
				
				OtcConfig.FILE4= line.getOptionValue("file4");
				log.info( "file4: " + line.getOptionValue("file4"));
			}
			if (line.hasOption("file5")) {
				
				OtcConfig.FILE5= line.getOptionValue("file5");
				log.info( "file5: " + line.getOptionValue("file5"));
			}
			
			if (line.hasOption("instance-type")) {
				
				OtcConfig.INSTANCE_TYPE_NAME= line.getOptionValue("instance-type");
				log.info( "instance-type: " + line.getOptionValue("instance-type"));
			}


			if (line.hasOption("image-name")) {
				
				OtcConfig.IMAGENAME= line.getOptionValue("image-name");
				log.info( "image-name: " + line.getOptionValue("image-name"));
			}

			if (line.hasOption("image-id")) {
				
				OtcConfig.IMAGE_ID= line.getOptionValue("image-id");
				log.info( "image-id: " + line.getOptionValue("image-id"));
			}

			if (line.hasOption("count")) {
				
				OtcConfig.NUMCOUNT= line.getOptionValue("count");
				log.info( "instance-count: " + line.getOptionValue("count"));
			}
			
			if (line.hasOption("subnet-name")) {
				
				OtcConfig.SUBNETNAME= line.getOptionValue("subnet-name");
				log.info( "subnet-name: " + line.getOptionValue("subnet-name"));
			}

			if (line.hasOption("subnet-id")) {
				
				OtcConfig.SUBNETID= line.getOptionValue("subnet-id");
				log.info( "subnet-id: " + line.getOptionValue("subnet-id"));
			}
			
			if (line.hasOption("vpc-name")) {
				
				OtcConfig.VPCNAME= line.getOptionValue("vpc-name");
				log.info( "vpc-name: " + line.getOptionValue("vpc-name"));
			}

			if (line.hasOption("vpc-id")) {
				
				OtcConfig.VPCID= line.getOptionValue("vpc-id");
				log.info( "vpc-id: " + line.getOptionValue("vpc-id"));
			}
			

			if (line.hasOption("cidr")) {
				
				OtcConfig.CIDR= line.getOptionValue("cidr");
				log.info( "cidr: " + line.getOptionValue("cidr"));
			}

			if (line.hasOption("gateway-ip")) {
				
				OtcConfig.GWIP= line.getOptionValue("gateway-ip");
				log.info( "gateway-ip: " + line.getOptionValue("gateway-ip"));
			}


			if (line.hasOption("primary-dns")) {
				
				OtcConfig.PRIMARYDNS= line.getOptionValue("primary-dns");
				log.info( "primary-dns: " + line.getOptionValue("primary-dns"));
			}

			if (line.hasOption("secondary-dns")) {
				
				OtcConfig.SECDNS= line.getOptionValue("secondary-dns");
				log.info( "secondary-dns: " + line.getOptionValue("secondary-dns"));
			}

			if (line.hasOption("availability-zone")) {
				
				OtcConfig.AZ= line.getOptionValue("availability-zone");
				log.info( "availability-zone: " + line.getOptionValue("availability-zone"));
			}

			if (line.hasOption("key")) {
				
				OtcConfig.S3OBJECT= line.getOptionValue("key");
				OtcConfig.KEYNAME= line.getOptionValue("key");				
				log.info( "key: " + line.getOptionValue("key"));
			}
			
			
			if (line.hasOption("region")) {
				
				OtcConfig.region= line.getOptionValue("region");
				log.info( "region: " + line.getOptionValue("region"));
			}
			
			if (line.hasOption("group-name")) {
				
				OtcConfig.SECUGROUPNAME= line.getOptionValue("group-name");
				log.info( "group-name: " + line.getOptionValue("group-name"));
			}

			if (line.hasOption("security-group-id")) {
				
				OtcConfig.SECUGROUP= line.getOptionValue("security-group-id");
				log.info( "security-group-id: " + line.getOptionValue("security-group-id"));
			}

			if (line.hasOption("associate-public-ip-address")) {
				
				OtcConfig.CREATE_ECS_WITH_PUBLIC_IP= "true";
				log.info( "public: " + true);
			}

			
			if (line.hasOption("direction")) {
				
				OtcConfig.DIRECTION= line.getOptionValue("direction");
				log.info( "direction: " + line.getOptionValue("direction"));
			}

			if (line.hasOption("portmin")) {
				
				OtcConfig.PORTMIN= line.getOptionValue("portmin");
				log.info( "portmin: " + line.getOptionValue("portmin"));
			}

			if (line.hasOption("portmax")) {
				
				OtcConfig.PORTMAX= line.getOptionValue("portmax");
				log.info( "portmax: " + line.getOptionValue("portmax"));
			}
			

			if (line.hasOption("protocol")) {
				
				OtcConfig.PROTOCOL= line.getOptionValue("protocol");
				log.info( "v: " + line.getOptionValue("protocol"));
			}
			
			if (line.hasOption("ethertype")) {
				
				OtcConfig.ETHERTYPE= line.getOptionValue("ethertype");
				log.info( "ethertype: " + line.getOptionValue("ethertype"));
			}						
			if (line.hasOption("bucket")) {
				
				OtcConfig.S3BUCKET= line.getOptionValue("bucket");
				log.info( "bucket: " + line.getOptionValue("bucket"));
			}						
			if (line.hasOption("output")) {
				
				OtcConfig.OUTPUT_FORMAT= line.getOptionValue("output");
				log.info( "bucket: " + line.getOptionValue("output"));
			}						


			if (line.hasOption("query")) {
				
				OtcConfig.QUERY= line.getOptionValue("query");
				log.info( "query: " + line.getOptionValue("query"));
			}						
			
			
			if (line.hasOption("size")) {
				 
				OtcConfig.VOLUME_SIZE= Integer.parseInt(line.getOptionValue("size"));
				log.info( "size: " + line.getOptionValue("size"));
			}						

			if (line.hasOption("volume-type")) {
				 
				OtcConfig.VOLUME_TYPE= line.getOptionValue("volume-type");
				log.info( "volume-type: " + line.getOptionValue("volume-type"));
			}						
			
			if (line.hasOption("volume-name")) {				 
				OtcConfig.VOLUME_NAME= line.getOptionValue("volume-name");
				log.info( "volume-name: " + line.getOptionValue("volume-name"));
			}						
			if (line.hasOption("device")) {				 
				OtcConfig.EVS_DEVICE= line.getOptionValue("device");
				log.info( "device: " + line.getOptionValue("device"));
			}						

			if (line.hasOption("description")) {				 
				OtcConfig.DESCRIPTION= line.getOptionValue("description");
				log.info( "description: " + line.getOptionValue("description"));
			}						

			if (line.hasOption("snapshot-id")) {				 
				OtcConfig.SNAPSHOTID= line.getOptionValue("snapshot-id");
				log.info( "snapshot-id: " + line.getOptionValue("snapshot-id"));
			}	

			if (line.hasOption("wait-instance-running")) {				 
				OtcConfig.WAIT_CREATE= "true";
				log.info( "wait-instance-running: " + line.getOptionValue("wait-instance-running"));
			}	
			
			if (line.hasOption("network-interface-id")) {				 
				OtcConfig.NETWORKINTERFACEID= line.getOptionValue("network-interface-id");
				log.info( "network-interface-id: " + line.getOptionValue("network-interface-id"));
			}	

			if (line.hasOption("public-ip")) {				 
				OtcConfig.PUBLICIP= line.getOptionValue("public-ip");
				log.info( "public-ip: " + line.getOptionValue("public-ip"));
			}	
			if (line.hasOption("public-ip-id")) {				 
				OtcConfig.PUBLICIPID= line.getOptionValue("public-ip-id");
				log.info( "public-ip-id: " + line.getOptionValue("public-ip-id"));
			}	
			
				
						
			
			
			
			// 

			
		} catch (ParseException exp) {
			System.out.println("Unexpected exception:" + exp.getMessage() );
			
		}
	}
	
	/**
	 * Print usage information to provided OutputStream.
	 */
	public static void printHelp()
	{
		printHelp(
		            options, 300, getHeader(), getFooter(),
		               3, 5, false, System.out);
	}

	public static String getHeader()
	{
		 String HEADER  = "OTC HELP";
		 return HEADER;
	}	
	
	public static String getFooter()
	{
		 String FOOTER  = 				 
				 "Examples: \n"+
				 "\n"+
				 "OTC Tool Configuration Commands: \n"+
				 "otc configure                                                        Configuring OTC client tool (mandatory in first use)  \n"+
				 "otc configure-proxy                                                  Configureing proxy settings ( ONLY https )\n"+
				 "otc version                                                          Print OTC Client tool version\n"+
				 "\n"+				 
				 "S3 Commands: \n"+
				 "otc s3 ls                                                            List Buckets  \n"+
				 "otc s3 ls mybucket                                                   List Bucket files\n"+
				 "otc s3api create-bucket --bucket mybucket                                      Create New Bucket\n"+
				 "otc.bat s3 cp s3://bucketname/filename.txt /localdir/filename.txt    Download from bucket to local\n"+
				 "otc.bat s3 cp /localdir/filename.txt s3://bucketname/filename.txt    Upload file / directory to bucket   \n"+
				 "\n"+
				 "ECS Flavor & Image Commands:\n"+
				 "otc ecs describe-flavors                                             List avaliable flavors (VM templates)\n"+
				 "otc ecs describe-images                                              List image templates\n"+				 
				 "VPC Commands:\n" +				 
				 "otc ecs create-vpc --vpc-name myvpc --cidr 10.0.0.0/8                Crete new VPC \n"+
				 "otc ecs describe-vpcs                                                List VPCs  \n"+
				 "\n"+
				 "Subnet Commands:\n" +				 
				 "otc ecs create-subnet --subnet-name subnettest --cidr 192.168.1.0/16 --gateway-ip 192.168.1.2 --primary-dns 8.8.8.8 --secondary-dns 8.8.4.4 --availability-zone eu-de-01 --vpc-name default-vpc    Create new subnet for VPC \n"+
				 "otc ecs describe-subnets                                              List Subnets\n"+
				 "\n"+
				 "Security Group Commands:\n" +
				 "otc ecs create-security-group --group-name test2 --vpc-name default-vpc  Create new security group \n"+
				 "otc ecs describe-security-groups                                     List existing security-groups  \n"+
				 "otc ecs authorize-security-group-ingress --group-name test2 --vpc-name default-vpc --protocol tcp --ethertype IPv4 --portmin 22 --portmax 25      Add new incomming rule to security-group\n"+
				 "otc ecs authorize-security-group-egress --group-name test2 --vpc-name default-vpc --protocol tcp --ethertype IPv4 --portmin 7000 --portmax 7001   Add new outcomming rule to security-group\n"+
				 "\n"+
				 "Keypair Commands:\n" +
				 "otc ecs describe-key-pairs                                           List key pairs\n"+
				 "otc ecs create-key-pair --key-name mykeypair \"ssh-rsa AA...\"         Create key pair\n"+
				 "\n"+
				 "Instance Commands:\n" +
				 "otc ecs describe-instances                                           List VM instances\n"+
				 "otc ecs describe-instances  --instance-ids 097da903-ab95-44f3-bb5d-5fc08dfb6cc3 --output json     Detailed information of specific VM instance (JSON)\n"+				 
				 "otc ecs run-instances --count 1  --admin-pass yourpass123! --instance-type c1.medium --instance-name instancename --image-name Standard_CentOS_6.7_latest --subnet-name testsubnet --vpc-name testvpc --group-name testsecgroup     Create new VM instance and START   \n"+
				 "otc ecs run-instances --count 1  --admin-pass yourpass123! --instance-type c1.medium --instance-name instancename --image-name Standard_CentOS_6.7_latest --subnet-name testsubnet --vpc-name testvpc --group-name testsecgroup  --key-name testsshkeypair --file1 /otc/a=/otc/a --associate-public-ip-address  --wait-instance-running    Create new VM instance with injected SSH keypair, with public ip, additional file injection, wait instance created and running \n"+
				 "otc ecs describe-instances                                           List VM instances\n"+
				 "otc ecs stop-instances   --instance-ids b6c602b1-06d0-4bdb-b764-5d43b47abc14        Stop VM instance\n" + 
				 "otc ecs start-instances  --instance-ids b6c602b1-06d0-4bdb-b764-5d43b47abc14        Start VM instance\n" +
				 "otc ecs reboot-instances --instance-ids b6c602b1-06d0-4bdb-b764-5d43b47abc14        Reboot VM instance\n" +
				 "otc ecs delete-instances --instance-ids b6c602b1-06d0-4bdb-b764-5d43b47abc14        Delete VM instance (public ip + EVS also)\n" +
				 "\n"+
				 "Backup Commands:\n" + 
				 "otc ecs create-snapshot  --volume-id b197b8af-fe63-465f-97b6-5e5b89exxxx  Create snapshot of volume\n" +
				 "otc ecs describe-snapshots                                           List backup volumes\n" +
				 "otc ecs delete-snapshot  --snapshot-id 0c942ff7-454e-xxxx            Delete volume backup\n" +
				 "\n"+
				 "Volume Commands:\n" + 
				 "otc ecs describe-volumes                                             List volumes\n" +
				 "otc ecs create-volume   --volume-id b197b8af-fe63-465f-97b6-5e5b89exxx --snapshot-id 0c942ff7-454e-xxxx Create volume from snapshot \n" +
				 "otc ecs create-volume   --count 1 --volume-name myvolume  --size 100 --volume-type SATA      Create new Volume [type: SSD,SAS,SATA] \n" +
				 "otc ecs attach-volume   --instance-ids f344b625-6f73-44f8-ad56-9fcb05a523c4 --volume-id 8c0de9a7-9f61-4613-a68a-21f456cb7298             Attach volume to instance \n" +
				 "otc ecs detach-volume   --instance-ids f344b625-6f73-44f8-ad56-9fcb05a523c4 --volume-id 8c0de9a7-9f61-4613-a68a-21f456cb7298             Detach volume from instance\n" +
				 "otc ecs delete-volume   --volume-id 8c0de9a7-9f61-4613-a68a-21f456cb7298                                                                 Delete volume \n" +
				 "\n"+				 
				 "Public Ip Commands:\n" +
				 "otc otc ecs describe-addresses                                       List public ip adresses\n" +
				 "otc ecs allocate-address                                             Allocate public ip address from public ip pool\n" +				 
				 "otc ecs associate-address --public-ip 46.29.96.246 --network-interface-id b197b8af-fe63-465f-97b6-5e5b89exxx      Assodicate public ip with Network Interface Id\n" + 
				 "Output Commands:\n" +
				 "otc otc ecs describe-addresses  --output json                        List public ip struct in JSON format\n" +
				 "otc otc ecs describe-instances  --output text                        Show instance details in text format \n" +
				 "otc otc ecs describe-instances  --output table                       Show instance details in table format (default)\n" +
				 "otc ecs describe-security-groups --output json --query \".name\"     Show all \"name\" property \n"
				 ;				 
		 
		 return FOOTER;
	}	
	
	/**
	 * Write "help" to the provided OutputStream.
	 */
	public static void printHelp(final Options options,
			final int printedRowWidth, final String header,
			final String footer, final int spacesBeforeOption,
			final int spacesBeforeOptionDescription,
			final boolean displayUsage, final OutputStream out) {
		final String commandLineSyntax = "otc main-command sub-command [params]";
		final PrintWriter writer = new PrintWriter(out);
		final HelpFormatter helpFormatter = new HelpFormatter();
		helpFormatter.printHelp(writer, printedRowWidth, commandLineSyntax,
				header, options, spacesBeforeOption,
				spacesBeforeOptionDescription, footer, displayUsage);
		writer.flush();


		
		//writer.close();
	}

}
