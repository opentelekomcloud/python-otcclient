#!/usr/local/bin/python2.7
# encoding: utf-8
'''
otcclient.otcclient -- Client Tool for Open Telecom Cloud 

otcclient.otcclient is a description

It defines classes_and_methods

@author:     Zsolt Nagy 

@copyright:  2016 T-systems(c). All rights reserved.

@license:    license

@contact:    Z.Nagy@t-systems.com
@deffield    updated: 2016.05.24
'''

import sys
import os
from s3 import s3


from argparse import ArgumentParser, ArgumentError, ArgumentTypeError,\
    RawTextHelpFormatter
from argparse import RawDescriptionHelpFormatter
import argparse
from warnings import catch_warnings
from django.template.defaultfilters import default
from OtcUserConfigAction import OtcUserConfigAction
from ConfigLoader import ConfigLoader
from OtcConfig import OtcConfig
from otcServiceCalls import otcServiceCalls
#import pdb
#pdb.set_trace()


__all__ = []
__version__ = 0.1
__date__ = '2016-05-24'
__updated__ = '2016-05-24'

DEBUG = 0
TESTRUN = 0
PROFILE = 0

class CLIError(Exception):
    '''Generic exception to raise and log different fatal errors.'''
    def __init__(self, msg):
        super(CLIError).__init__(type(self))
        self.msg = "E: %s" % msg
    def __str__(self):
        return self.msg
    def __unicode__(self):
        return self.msg



def handleCommands(args):
    """ generated source for method handleCommands """
    if str.lower( OtcConfig.MAINCOM ) == "s3".lower() and str.lower( OtcConfig.SUBCOM ) == "ls".lower() and args.length > 3 and not args[3].startswith("--"):
        s3.listBucketContent(args[3])
    elif str.lower( OtcConfig.MAINCOM ) == "s3".lower() and str.lower( OtcConfig.SUBCOM ) == "ls".lower():
        s3.listBuckets()
    elif str.lower( OtcConfig.MAINCOM ) == "s3".lower() and str.lower( OtcConfig.SUBCOM ) == "cp".lower():
        s3.fileCopy(args[3], args[4]) 
    elif str.lower( OtcConfig.MAINCOM ) == "s3".lower() and str.lower( OtcConfig.SUBCOM ) == "rm".lower():
        s3.remove(args[3])
    elif str.lower( OtcConfig.MAINCOM ) == "ecs".lower() and str.lower( OtcConfig.SUBCOM ) == "create-snapshot".lower():
        otcServiceCalls.CreateBackup()
    elif str.lower( OtcConfig.MAINCOM ) == "ecs".lower() and str.lower( OtcConfig.SUBCOM ) == "delete-snapshot".lower():
        otcServiceCalls.DeleteBackup()
    elif str.lower( OtcConfig.MAINCOM ) == "ecs".lower() and str.lower( OtcConfig.SUBCOM ) == "describe-snapshots".lower():
        otcServiceCalls.getBackupList()
    elif str.lower( OtcConfig.MAINCOM ) == "autoscaling".lower() and str.lower( OtcConfig.SUBCOM ) == "create-launch-configuration".lower():
        otcServiceCalls.CreateLaunchConfiguration()
    elif str.lower( OtcConfig.MAINCOM ) == "autoscaling".lower() and str.lower( OtcConfig.SUBCOM ) == "delete-launch-configuration".lower():
        otcServiceCalls.DeleteLaunchConfiguration()
    elif str.lower( OtcConfig.MAINCOM ) == "autoscaling".lower() and str.lower( OtcConfig.SUBCOM ) == "attach-instances".lower():
        otcServiceCalls.AttachInstances()
    elif str.lower( OtcConfig.MAINCOM ) == "autoscaling".lower() and str.lower( OtcConfig.SUBCOM ) == "attach-load-balancers".lower():
        otcServiceCalls.AttachLoadBalancers()
    elif str.lower( OtcConfig.MAINCOM ) == "autoscaling".lower() and str.lower( OtcConfig.SUBCOM ) == "attach-load-balancers".lower():
        otcServiceCalls.AttachLoadBalancers()
    elif str.lower( OtcConfig.MAINCOM ) == "autoscaling".lower() and str.lower( OtcConfig.SUBCOM ) == "attach-load-balancers".lower():
        otcServiceCalls.AttachLoadBalancers()
    elif str.lower( OtcConfig.MAINCOM ) == "autoscaling".lower() and str.lower( OtcConfig.SUBCOM ) == "create-auto-scaling-group".lower():
        otcServiceCalls.CreateAutoScalingGroup()
    elif str.lower( OtcConfig.MAINCOM ) == "autoscaling".lower() and str.lower( OtcConfig.SUBCOM ) == "delete-auto-scaling-group".lower():
        otcServiceCalls.DeleteAutoScalingGroup()
    elif str.lower( OtcConfig.MAINCOM ) == "s3api".lower() and str.lower( OtcConfig.SUBCOM ) == "create-bucket".lower():
        s3.createBucket()
    elif str.lower( OtcConfig.MAINCOM ) == "s3api".lower() and str.lower( OtcConfig.SUBCOM ) == "get-object".lower():
        s3.getObject() 
    elif str.lower( OtcConfig.MAINCOM ) == "ecs".lower() and str.lower( OtcConfig.SUBCOM ) == "describe-instances".lower() and ( OtcConfig.INSTANCE_ID or OtcConfig.INSTANCE_NAME ): #len(args) > 3 and not args[3].startswith("--")
        if OtcConfig.INSTANCE_NAME != None and  len(OtcConfig.INSTANCE_NAME) > 0 :
            otcServiceCalls.convertINSTANCENameToId()
        otcServiceCalls.getECSVM(OtcConfig.INSTANCE_ID)
    elif (str.lower( OtcConfig.MAINCOM ) == "ecs".lower() and str.lower( OtcConfig.SUBCOM ) == "describe-instances".lower()) or (str.lower( OtcConfig.MAINCOM ) == "ecs".lower() and str.lower( OtcConfig.SUBCOM ) == "ls".lower()):
        otcServiceCalls.getECSList()
    elif str.lower( OtcConfig.MAINCOM ) == "ecs".lower() and str.lower( OtcConfig.SUBCOM ) == "list-detail".lower():
        otcServiceCalls.getECSDetail()
    elif str.lower( OtcConfig.MAINCOM ) == "ecs".lower() and str.lower( OtcConfig.SUBCOM ) == "run-instances".lower():
        if OtcConfig.VPCNAME != None:
            otcServiceCalls.convertVPCNameToId()
        if OtcConfig.SUBNETNAME != None:
            otcServiceCalls.convertSUBNETNameToId()
        if OtcConfig.IMAGENAME != None:
            otcServiceCalls.convertIMAGENameToId()
        if OtcConfig.SECUGROUPNAME != None:
            otcServiceCalls.convertSECUGROUPNameToId()
        if OtcConfig.INSTANCE_TYPE_NAME != None:
            otcServiceCalls.convertFlavorNameToId()
        otcServiceCalls.ECSCreate()
        if OtcConfig.WAIT_CREATE.lower() == "true".lower():
            OtcConfig.resetUrlVars()
            otcServiceCalls.getECSJOBList()
            print "#",
            print "ECS Creation status: " + OtcConfig.ECSCREATEJOBSTATUS
        if "SUCCESS".lower() == OtcConfig.ECSCREATEJOBSTATUS.lower():
            exit(1)
    elif str.lower( OtcConfig.MAINCOM ) == "ecs".lower() and str.lower( OtcConfig.SUBCOM ) == "reboot-instances".lower():
        OtcConfig.ECSACTION = "reboot"
        if OtcConfig.INSTANCE_ID == None or OtcConfig.INSTANCE_ID.lower() == "".lower():
            print "Error. Must be specify the Instance ID!"
#            ParamFactory.printHelp()
            exit(1)
        otcServiceCalls.ECSAction()
    elif str.lower( OtcConfig.MAINCOM ) == "ecs".lower() and str.lower( OtcConfig.SUBCOM ) == "start-instances".lower():
        OtcConfig.ECSACTION = "os-start"
        if OtcConfig.INSTANCE_ID == None or OtcConfig.INSTANCE_ID.lower() == "".lower():
            print "Error. Must be specify the Instance ID!"
#            ParamFactory.printHelp()
            exit(1)
        otcServiceCalls.ECSAction()
    elif str.lower( OtcConfig.MAINCOM ) == "ecs".lower() and str.lower( OtcConfig.SUBCOM ) == "stop-instances".lower():
        OtcConfig.ECSACTION = "os-stop"
        if OtcConfig.INSTANCE_ID == None or OtcConfig.INSTANCE_ID.lower() == "".lower():
            print "Error. Must be specify the Instance ID!"
#            ParamFactory.printHelp()
            exit(1)
        otcServiceCalls.ECSAction()
    elif str.lower( OtcConfig.MAINCOM ) == "ecs".lower() and str.lower( OtcConfig.SUBCOM ) == "delete-instances".lower():
        if OtcConfig.INSTANCE_ID.lower() == "".lower():
            print "Error. Must be specify the Instance ID!"
#            ParamFactory.printHelp()
            exit(1)
        otcServiceCalls.ECSDelete()
    elif str.lower( OtcConfig.MAINCOM ) == "ecs".lower() and str.lower( OtcConfig.SUBCOM ) == "job".lower():
        OtcConfig.ECSTASKID = args[3]
        OtcConfig.AUTH_URL_ECS_JOB = "https://ecs.eu-de.otc.t-systems.com/v1/" + OtcConfig.PROJECT_ID + "/jobs/$ECSTASKID"
        otcServiceCalls.getECSJOBList()
    elif str.lower( OtcConfig.MAINCOM ) == "ecs".lower() and str.lower( OtcConfig.SUBCOM ) == "describe-vpcs".lower():
        otcServiceCalls.getIamToken()
        otcServiceCalls.getVPCList()
    elif str.lower( OtcConfig.MAINCOM ) == "ecs".lower() and str.lower( OtcConfig.SUBCOM ) == "create-vpc".lower():
        otcServiceCalls.VPCCreate()
    elif str.lower( OtcConfig.MAINCOM ) == "ecs".lower() and str.lower( OtcConfig.SUBCOM ) == "describe-addresses".lower():
        otcServiceCalls.getPUBLICIPSList()
    elif str.lower( OtcConfig.MAINCOM ) == "ecs".lower() and str.lower( OtcConfig.SUBCOM ) == "allocate-address".lower():
        otcServiceCalls.PUBLICIPSAllocate()
    elif str.lower( OtcConfig.MAINCOM ) == "ecs".lower() and str.lower( OtcConfig.SUBCOM ) == "associate-address".lower():
        if OtcConfig.PUBLICIP != None:
            otcServiceCalls.convertPublicIpNameToId()
        otcServiceCalls.PUBLICIPSAssociate()
    elif str.lower( OtcConfig.MAINCOM ) == "ecs".lower() and str.lower( OtcConfig.SUBCOM ) == "describe-subnets".lower():
        otcServiceCalls.getSUBNETList()
    elif str.lower( OtcConfig.MAINCOM ) == "ecs".lower() and str.lower( OtcConfig.SUBCOM ) == "create-subnet".lower():
        if OtcConfig.VPCNAME != None:
            otcServiceCalls.convertVPCNameToId()
        otcServiceCalls.SUBNETCreate()
    elif str.lower( OtcConfig.MAINCOM ) == "ecs".lower() and str.lower( OtcConfig.SUBCOM ) == "describe-security-groups".lower():
        if OtcConfig.VPCNAME != None:
            otcServiceCalls.convertVPCNameToId()
        otcServiceCalls.getSECGROUPList()
    elif str.lower( OtcConfig.MAINCOM ) == "ecs".lower() and str.lower( OtcConfig.SUBCOM ) == "create-security-group".lower():
        if OtcConfig.VPCNAME != None:
            otcServiceCalls.convertVPCNameToId()
        otcServiceCalls.SECGROUPCreate()
    elif str.lower( OtcConfig.MAINCOM ) == "security-group-rules".lower() and str.lower( OtcConfig.SUBCOM ) == "list".lower():
        if args.length < 3:
            print "Error. Must be specify the Security Rule Group ID!"
#            ParamFactory.printHelp()
            exit(1)
        OtcConfig.SECUGROUP = args[3]
        OtcConfig.AUTH_URL_SEC_GROUP_RULE = "https://vpc.eu-de.otc.t-systems.com/v1/" + OtcConfig.PROJECT_ID + "/security-group-rules/" + OtcConfig.SECUGROUP
        otcServiceCalls.getSECGROUPRULESList()
    elif str.lower( OtcConfig.MAINCOM ) == "ecs".lower() and (str.lower( OtcConfig.SUBCOM ) == "authorize-security-group-ingress".lower() or str.lower( OtcConfig.SUBCOM ) == "authorize-security-group-egress".lower()):
        if str.lower( OtcConfig.SUBCOM ) == "authorize-security-group-ingress".lower():
            OtcConfig.DIRECTION = "ingress"
        else:
            OtcConfig.DIRECTION = "egress"
        if OtcConfig.VPCNAME != None:
            otcServiceCalls.convertVPCNameToId()
        if OtcConfig.SECUGROUPNAME != None:
            otcServiceCalls.convertSECUGROUPNameToId()
        otcServiceCalls.SECGROUPRULECreate()
    elif str.lower( OtcConfig.MAINCOM ) == "ecs".lower() and str.lower( OtcConfig.SUBCOM ) == "describe-images".lower():
        otcServiceCalls.getIMAGEList()
    elif str.lower( OtcConfig.MAINCOM ) == "ecs".lower() and str.lower( OtcConfig.SUBCOM ) == "describe-flavors".lower():
        otcServiceCalls.getFLAVORList()
    elif str.lower( OtcConfig.MAINCOM ) == "ecs".lower() and str.lower( OtcConfig.SUBCOM ) == "describe-key-pairs".lower():
        otcServiceCalls.getKEYPAIRList()
    elif str.lower( OtcConfig.MAINCOM ) == "ecs".lower() and str.lower( OtcConfig.SUBCOM ) == "create-key-pair".lower():
        otcServiceCalls.KEYPAIRCreate()
    elif str.lower( OtcConfig.MAINCOM ) == "ecs".lower() and str.lower( OtcConfig.SUBCOM ) == "delete-key-pair".lower():
        otcServiceCalls.KEYPAIRDelete()
    elif str.lower( OtcConfig.MAINCOM ) == "ecs".lower() and str.lower( OtcConfig.SUBCOM ) == "create-volume".lower():
        if OtcConfig.VOLUME_NAME == None or len(OtcConfig.VOLUME_NAME) == 0:
            otcServiceCalls.RestoreBackupDisk()
        else:
            otcServiceCalls.CreateVolume()
    elif str.lower( OtcConfig.MAINCOM ) == "ecs".lower() and str.lower( OtcConfig.SUBCOM ) == "describe-volumes".lower():
        otcServiceCalls.getVolumeList()
    elif str.lower( OtcConfig.MAINCOM ) == "ecs".lower() and str.lower( OtcConfig.SUBCOM ) == "attach-volume".lower():
        otcServiceCalls.AttachVolume()
    elif str.lower( OtcConfig.MAINCOM ) == "ecs".lower() and str.lower( OtcConfig.SUBCOM ) == "detach-volume".lower():
        otcServiceCalls.DetachVolume()
    elif str.lower( OtcConfig.MAINCOM ) == "ecs".lower() and str.lower( OtcConfig.SUBCOM ) == "delete-volume".lower():
        otcServiceCalls.DeleteVolume()
    elif str.lower( OtcConfig.MAINCOM ) == "ecs".lower() and str.lower( OtcConfig.SUBCOM ) == "describe-quotas".lower():
        otcServiceCalls.DescribeQuotas()
    elif str.lower( OtcConfig.MAINCOM ) == "iam".lower() and str.lower( OtcConfig.SUBCOM ) == "token".lower():
        otcServiceCalls.getIamToken()
        print OtcConfig.TOKEN
    else:
        print "Not valid command"
#        ParamFactory.printHelp()






def main(argv=None): # IGNORE:C0111
    '''Command line options.'''

#    print("nzs!!!!!!!!!!!!!!!!!!!!!!!" )
    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)

    #print sys.argv
    program_name = os.path.basename(sys.argv[0])
    program_version = "v%s" % __version__
    program_build_date = str(__updated__)
    program_version_message = '%%(prog)s %s (%s)' % (program_version, program_build_date)
    program_shortdesc = __import__('__main__').__doc__.split("\n")[1]
    program_license = '''%s

  Created by NZS on %s.
  Copyright 2016 T-systems(c). All rights reserved.

  Licensed under the Apache License 2.0
  http://www.apache.org/licenses/LICENSE-2.0

  Distributed on an "AS IS" basis without warranties
  or conditions of any kind, either express or implied.

USAGE
''' % (program_shortdesc, str(__date__))

    try:
        # Setup argument parser
        parser = ArgumentParser(prog='otc' ,  formatter_class=RawTextHelpFormatter ) #RawDescriptionHelpFormatter ,description=program_license
         
        #parser.add_argument("-r", "--recursive", dest="recurse", action="store_true", help="recurse into subfolders [default: %(default)s]")
        #parser.add_argument("-v", "--verbose", dest="verbose", action="count", help="set verbosity level [default: %(default)s]")
        #parser.add_argument("-i", "--include", dest="include", help="only include paths matching this regex pattern. Note: exclude is given preference over include. [default: %(default)s]", metavar="RE" )
        #parser.add_argument("-e", "--exclude", dest="exclude", help="exclude paths matching this regex pattern. [default: %(default)s]", metavar="RE" )
        parser.add_argument('-V', '--version', action='version', version=program_version_message)
        
        parser.add_argument('--configure', nargs='?',action=OtcUserConfigAction,choices=['user', 'proxy'], default = "user")
        #parser.add_argument('--configure-proxy', nargs='+',action=OtcUserConfigAction , required = False)

        
        
        parser.add_argument(dest="MAINCOM", help="OTC Component Selector",  nargs='?', default='ecs', metavar="OtcComponent") #choices=['ecs', 's3']s
        parser.add_argument(dest="SUBCOM", help="OTC Command Selector",  nargs='?', default='', metavar="OtcCommand")

        parser.add_argument("-k", "--key-name", dest="KEYNAME", help="SSH key name| S3 Object key")
        parser.add_argument( "--public-key", dest="PUBLICKEY", help="Import public key for SSH keypairs")
        parser.add_argument( "--admin-pass", dest="ADMINPASS", help="Admin password of the started VM")
        parser.add_argument( "--instance-name", dest="INSTANCE_NAME", help="Instance name of the VM")
        parser.add_argument( "--instance-ids", dest="INSTANCE_ID", help="Instance Id of the VM")
        parser.add_argument( "--volume-id", dest="VOLUME_ID", help="Volume Id of the EVS volume")
        parser.add_argument( "--attachment-id", dest="ATTACHMENT_ID", help="Attachment Id of the EVS volume")
        parser.add_argument( "--device", dest="EVS_DEVICE", help="Device of the EVS volume")
        parser.add_argument( "--file1", dest="FILE1", help="Name of the #1 file to be injected to VM. Format: target=source")
        parser.add_argument( "--file2", dest="FILE2", help="Name of the #2 file to be injected to VM. Format: target=source")
        parser.add_argument( "--file3",dest="FILE3", help="Name of the #3 file to be injected to VM. Format: target=source")
        parser.add_argument( "--file4",dest="FILE4", help="Name of the #4 file to be injected to VM. Format: target=source")
        parser.add_argument( "--file5",dest="FILE5", help="Name of the #5 file to be injected to VM. Format: target=source")
        parser.add_argument( "--instance-type",dest="INSTANCE_TYPE_NAME", help="Flavor type of the VM")
        parser.add_argument( "--image-name",dest="IMAGENAME", help="Name of the image reference will used during VM creation")
        parser.add_argument( "--image-id",dest="IMAGE_ID", help="Id of the image reference will use during VM creation")
        parser.add_argument("-n", "--count",dest="NUMCOUNT", help="Number of VM will be created")
        parser.add_argument( "--subnet-name",dest="SUBNETNAME", help="Name of the subnet reference will use during VM creation")
        parser.add_argument( "--subnet-id",dest="SUBNETID", help="Id of the subnet will use during VM creation")
        parser.add_argument( "--network-interface-id",dest="NETWORKINTERFACEID", help="Network interface Id of NIC")
        parser.add_argument( "--vpc-name",dest="VPCNAME", help="Name of the VPC reference will use during VM creation")
        parser.add_argument( "--vpc-id",dest="VPCID", help="Id of the VPC will use during VM creation")
        parser.add_argument( "--cidr",dest="CIDR", help="CIDR of the subnet will use during subnet creation")
        parser.add_argument( "--gateway-ip",dest="GWIP", help="Gateway Ip of the subnet ")
        parser.add_argument( "--primary-dns",dest="PRIMARYDNS", help="Primary dns of the subnet ")
        parser.add_argument( "--secondary-dns",dest="SECDNS", help="Secondary dns of the subnet ")
        parser.add_argument( "--availability-zone",dest="AZ", help="Availability-zone definition")
        parser.add_argument( "--region",dest="REGION", help="Region definition")
        parser.add_argument( "--group-name",dest="SECUGROUPNAME", help="Name of the security group")
        parser.add_argument( "--security-group-ids",dest="SECUGROUP", help="Id of the security group")
        parser.add_argument("-p", "--associate-public-ip-address", dest="CREATE_ECS_WITH_PUBLIC_IP", help="VM will get EIP public IP")
        parser.add_argument( "--public-ip",dest="PUBLICIP", help="Public IP for association")
        parser.add_argument( "--public-ip-id",dest="PUBLICIPID", help="Public IP ID for association")
        parser.add_argument( "--bucket",dest="S3BUCKET", help="S3 Bucket")
        parser.add_argument( "--key",dest="S3OBJECT", help="S3 Object Name")
        parser.add_argument( "--direction",dest="DIRECTION", help="Direction of the security group rule")
        parser.add_argument( "--portmin",dest="PORTMIN", help="Lower por of the specific security group rule")
        parser.add_argument( "--portmax",dest="PORTMAX", help="Upper  port of the specific security group rule")
        parser.add_argument( "--protocol",dest="PROTOCOL", help="Protocol of the specific security group rule")
        parser.add_argument( "--ethertype",dest="ETHERTYPE", help="Ethertype of the specific security group rule ")
        parser.add_argument( "--output",dest="OUTPUT_FORMAT", help="Output format")
        parser.add_argument( "--query",dest="QUERY", help="JSON Path query")
        parser.add_argument( "--size",dest="VOLUME_SIZE", help="Size of the EVS disk")
        parser.add_argument( "--volume-type",dest="VOLUME_TYPE", help="Volume type of the EVS disk [SSD,SAS,SATA]")
        parser.add_argument( "--volume-name",dest="VOLUME_NAME", help="Volume name of the EVS disk")
        parser.add_argument( "--description",dest="DESCRIPTION", help="Description definition ( eg: backups)")
        parser.add_argument( "--snapshot-id",dest="SNAPSHOTID", help="Snapshot id of the  backup")
        parser.add_argument( "--wait-instance-running", dest="WAIT_CREATE", help="Wait instance running (only for run-instance command)")

        # Process arguments
        args = parser.parse_args()
        OtcConfig.copyfromparser( args )
        
#        print("my command: " + OtcConfig.MAINCOM)
#        print("my subcommand: " + OtcConfig.SUBCOM)

        ConfigLoader.readUserValues() 
        ConfigLoader.readProxyValues()
        ConfigLoader.validateConfig()


        handleCommands(argv)
        
        return 0
    except KeyboardInterrupt,e:
        print "KeyboardInterrupt" +  str(e)
        ### handle keyboard interrupt ###
        return 0
    except ( Exception ) as e:
    #    sys.exit()    
        raise
    
        if DEBUG or TESTRUN:
            raise(e)
        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " + repr(e) + "\n")
        sys.stderr.write(indent + "  for help use --help")
        return 2
    except :
        print "Other exception"  + "Unexpected error:", sys.exc_info()[0]

if __name__ == "__main__":
    if DEBUG:
        sys.argv.append("-h")
        sys.argv.append("-v")
        sys.argv.append("-r")
    if TESTRUN:
        import doctest
        doctest.testmod()
    if PROFILE:
        import cProfile
        import pstats
        profile_filename = 'otcclient.otcclient_profile.txt'
        cProfile.run('main()', profile_filename)
        statsfile = open("profile_stats.txt", "wb")
        p = pstats.Stats(profile_filename, stream=statsfile)
        stats = p.strip_dirs().sort_stats('cumulative')
        stats.print_stats()
        statsfile.close()
        sys.exit(0)
        
    sys.exit(main())

