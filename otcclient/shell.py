#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is part of OTC Tool released under MIT license.
# otcclient.otcclient -- Client Tool for Open Telecom Cloud
# Copyright (C) 2016 T-systems Kurt Garloff, Zsolt Nagy

'''
otcclient.otcclient -- Client Tool for Open Telecom Cloud 
@copyright:  2016 T-systems(c). All rights reserved.
@contact:    Z.Nagy@t-systems.com
'''

import sys
import os
from argparse import ArgumentParser, RawTextHelpFormatter

if sys.version_info >= (3, 0):
    from configparser import NoSectionError
else:
    from ConfigParser import NoSectionError

from otcclient.core.userconfigaction import userconfigaction
from otcclient.core.configloader import configloader
from otcclient.core.OtcConfig import OtcConfig
from otcclient.core.pluginmanager import getFunc       

__all__ = []
__version__ = 1.1
__date__ = '2016-08-16'
__updated__ = '2016-08-16'

TESTRUN = 0
PROFILE = 0
parser = ArgumentParser(prog='otc' ,  formatter_class=RawTextHelpFormatter ) 

class CLIError(Exception):
    '''Generic exception to raise and log different fatal errors.'''
    def __init__(self, msg):
        super(CLIError).__init__(type(self))
        self.msg = "E: %s" % msg
    def __str__(self):
        return self.msg
    def __unicode__(self):
        return self.msg

def handleCommands(args):  # @DontTrace
    if args:
        pass
    func = getFunc(command=OtcConfig.MAINCOM, subcommand=OtcConfig.SUBCOM)
    # call the function
    (func)()  

def main(argv=None): # IGNORE:C0111
    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)

    program_name = os.path.basename(sys.argv[0])
    program_version = "v%s" % __version__
    program_build_date = str(__updated__)
    program_version_message = '%%(prog)s %s (%s)' % (program_version, program_build_date)
#    program_shortdesc = __import__('__main__').__doc__.split("\n")[1]
#     program_license = '''%s
# 
#   Created by NZS on %s.
#   Copyright 2016 T-systems(c). All rights reserved.
#   Licensed under the MIT
#   
# USAGE
# ''' % (program_shortdesc, str(__date__))

    try:
        # Setup argument parser        
        parser.add_argument('-V', '--version', action='version', version=program_version_message)        
        parser.add_argument('-d', '--debug', help='Debug mode', dest='DEBUG', action='store_true')
        parser.add_argument('--configure', nargs='?',action=userconfigaction,choices=['user', 'proxy'], default = "user")
        #parser.add_argument('--configure-proxy', nargs='+',action=userconfigaction , required = False)
        parser.add_argument(dest="MAINCOM", help="OTC Component Selector",  nargs='?', default='ecs', metavar="OtcComponent") #choices=['ecs', 's3']s
        parser.add_argument(dest="SUBCOM", help="OTC Command Selector",  nargs='?', default='', metavar="OtcCommand")
        # for S3 commands 
        parser.add_argument(dest="SUBCOM_P1", help="[optional Source/Target OBS directory]",  nargs='?', default='', metavar="Source/Target DIR")
        parser.add_argument(dest="SUBCOM_P2", help="[optional Source/Target OBS directory]",  nargs='?', default='', metavar="Source/Target DIR")                

        parser.add_argument("-k", "--key-name", dest="KEYNAME", help="SSH key name| S3 Object key")
        parser.add_argument( "--public-key", dest="PUBLICKEY", help="Import public key for SSH keypairs")
        parser.add_argument( "--admin-pass", dest="ADMINPASS", help="Admin password of the started VM")
        parser.add_argument( "--instance-name", dest="INSTANCE_NAME", help="Instance name of the VM")
        parser.add_argument( "--instance-ids", dest="INSTANCE_ID", help="Instance Id of the VM")

        parser.add_argument( "--load-balancer-name", dest="LOADBALANCER_NAME", help="Loadbalancer name of the VM")
        parser.add_argument( "--load-balancer-id", dest="LOADBALANCER_ID", help="Loadbalancer Id of the VM")
        parser.add_argument( "--listener-name", dest="LISTENER_NAME", help="Listener name of the VM")
        parser.add_argument( "--listener-id", dest="LISTENER_ID", help="Listener Id of the VM")
        parser.add_argument( "--alarm-name", dest="ALARM_NAME", help="Alarm name")
        parser.add_argument( "--alarm-id", dest="ALARM_ID", help="Alarm Id ")
        
        
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
        parser.add_argument( "--cluster-name",dest="CLUSTER", help="Name of the cluster")
        parser.add_argument( "--cluster-id",dest="CLUSTER_ID", help="Id of the cluster")
        parser.add_argument( "--namespace-id",dest="NAMESPACE_ID", help="Namespace Id of the cluster")
        parser.add_argument( "--pod",dest="POD", help="CCE POD")
        parser.add_argument( "--container-name",dest="CONTAINER_NAME", help="CCE POD container name")
        parser.add_argument( "--service-name",dest="SERVICE_NAME", help="CCE Service name")
        parser.add_argument( "--endpoint-name",dest="ENDPOINT_NAME", help="CCE endpoint name")
        
        
        parser.add_argument( "--cli-input-json",dest="CLIINPUTJSONFILE", help="Input JSON file for every request")
        
        parser.add_argument( "--user-data",dest="USER_DATA_PATH", help="Path to user-data file which will be used for cloud-init")
        
        
        parser.add_argument( "--image-url",dest="IMAGE_URL", help="Url of the image used during Image creation")
        parser.add_argument( "--tags",dest="TAG_LIST", help="Tags of the image will used during Image creation")
        parser.add_argument( "--protected",dest="PROTECTED", help="Protected status of  image used during VM creation")
        parser.add_argument( "--os-version",dest="OS_VERSION", help="Os version of image")
        parser.add_argument( "--min-ram",dest="MIN_RAM", help="Min ram used during image creation")
        parser.add_argument( "--min-disk",dest="MIN_DISK", help="Min ram used during image creation")
        parser.add_argument( "--visibility",dest="IMAGE_VISIBILITY", help="Image visibility used during image creation")
        parser.add_argument( "--disk-format",dest="DISK_FORMAT", help="Disk format used during image creation")
        parser.add_argument( "--container-format",dest="CONTAINTER_FORMAT", help="Container format used during image creation")
                
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
        parser.add_argument( "--group-names",dest="SECUGROUPNAME", help="Name of the security group")
        parser.add_argument( "--security-group-ids",dest="SECUGROUP", help="Id of the security group")
        
        parser.add_argument( "--source-group-id",dest="SOURCE_GROUP_ID", help="Id of Source security group")
        parser.add_argument( "--source-group",dest="SOURCE_GROUP", help="Name of Source security group")

        parser.add_argument( "--auto-scaling-group-name",dest="SCALINGGROUP_NAME", help="Name of Auto Scaling group")
        parser.add_argument( "--auto-scaling-group-id",dest="SCALINGGROUP_ID", help="Id of Auto Scaling group")
        
        parser.add_argument( "--dim",dest="DIM", nargs='*', help="CES Dim definition")
        parser.add_argument( "--metric-name",dest="METRIC-NAME", help="CES Metric Name")
        parser.add_argument( "--namespace",dest="NAMESPACE", help="CES/CCE Namespace")
        parser.add_argument( "--period",dest="PERIOD", help="CES Period")
        parser.add_argument( "--filter",dest="FILTER", help="CES Filter")

        
        parser.add_argument("-p", "--associate-public-ip-address", dest="CREATE_ECS_WITH_PUBLIC_IP", action='store_true',help="VM will get EIP public IP")
        parser.add_argument( "--public-ip",dest="PUBLICIP", help="Public IP for association")
        parser.add_argument( "--allocation-id",dest="PUBLICIPID", help="Public IP ID")
        parser.add_argument( "--bucket",dest="S3BUCKET", help="S3 Bucket")
        parser.add_argument( "--key",dest="S3OBJECT", help="S3 Object Name")
        parser.add_argument( "--recursive",dest="S3RECURSIVE", help="S3 recursive operation")
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
        parser.add_argument( "--wait-instance-running", dest="WAIT_CREATE", action='store_true' , help="Wait instance running (only for run-instance command)")
        # Process arguments
        args = parser.parse_args()
        #args = parser.parse_known_args()
        
        OtcConfig.copyfromparser( args )
        
        configloader.readUserValues() 
        configloader.readProxyValues()
        configloader.validateConfig()

        handleCommands(argv)
        
        return 0
    except KeyboardInterrupt as e:
        print("KeyboardInterrupt" +  str(e))
        ### handle keyboard interrupt ###
        return 1

    except NoSectionError as e:
        print("Configuration error. \nDefine ENV variables or run following command: \n    otc --configure [user | proxy]")
        return 1
    except (KeyError,AttributeError) as e:
        #errno, strerror = e.args
        print("Invalid command:" + str(e))
        parser.print_help()
        if OtcConfig.DEBUG or TESTRUN:        
            raise
        ### handle keyboard interrupt ###
        return 1
    except ( Exception ) as e:
    
        if OtcConfig.DEBUG or TESTRUN:
            raise 
        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " + repr(e) + "\n")
        sys.stderr.write(indent + "  for help use --help")
        return 2
    except :
        print("Other exception"  + "Unexpected error:", sys.exc_info()[0])

if __name__ == "__main__":
    main()

