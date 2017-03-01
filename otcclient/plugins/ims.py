#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of OTC Tool released under MIT license.
# Copyright (C) 2016 T-systems Kurt Garloff, Zsolt Nagy


from otcclient.core.OtcConfig import OtcConfig 
from otcclient.utils import utils_http

from otcclient.core.otcpluginbase import otcpluginbase
from otcclient.core.pluginmanager import getplugin

import json

from otcclient.core.argmanager import arg, otcfunc 
    
class ims(otcpluginbase):
    ar = {}    
    
    @staticmethod
    def otcOutputHandler(): 
        return getplugin(OtcConfig.OUTPUT_FORMAT)
 
    def otctype(self):
        return "func" 

    @staticmethod
    def update_image_metadata():
        if not (OtcConfig.IMAGENAME is None):
            getplugin("ecs").convertIMAGENameToId()
        ims.create_image_metadata()

    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="Creates image metadata",
             examples=[
                       {'Creates image metadata":"otc ims create_image_metadata  --image-name testimagenzs --os-version "Ubuntu 14.04 server 64bit" --container-format bare --disk-format raw --min-disk 1 --min-ram 1024 --tags "test,image" --visibility private --protected false'}
                       ],
             args = [ 
                arg(
                    '--os-version',
                    dest='OS_VERSION',
                    metavar='__os_version',
                    default='Other Linux(64 bit)',
                    help='Specifies the image OS version, if this  is not specified, the value will be set to Other Linux(64 bit)'
                )
                ,
                arg(
                    '--container-format',
                    dest='CONTAINTER_FORMAT',
                    metavar='container_format' ,
                    default=None,
                    help='Container format used during image creation'
                )                                            
                ,
                arg(
                    '--disk_format',
                    dest='DISK_FORMAT',
                    metavar='<disk_format>',
                    default=None,
                    help='Disk format used during image creation'
                )                           ,
                arg(
                    '--min_disk',
                    dest='MIN_DISK',
                    metavar='<min_disk>',
                    default=None,
                    help='Min disk used during image creation'
                )                           ,
                arg(
                    '--min_ram',
                    dest='MIN_RAM',
                    metavar='<min_ram>',
                    default=None,
                    help='Min ram used during image creation'
                )                           ,
                arg(
                    '--image-name',
                    dest='IMAGENAME',
                    metavar='<image-name>',
                    default=None,
                    help='description of the avaliable clusters'
                )                           ,
                arg(
                    '--tags',
                    dest='TAG_LIST',
                    metavar='<tags>',
                    default=None,
                    help='Tags of the image will used during Image creation'
                )                           ,
                arg(
                    '--visibility',
                    dest='IMAGE_VISIBILITY',
                    metavar='<visibility>',
                    default=None,
                    help='Image visibility used during image creation'
                )                           ,
                arg(
                    '--protected   ',
                    dest='PROTECTED',
                    metavar='<protected>',
                    default=None,
                    help='Protected status of  image used during VM creation'
                )
                ]                
             )    
    def create_image_metadata():
                
        # image id filled until now 
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v2/images" 
        REQ_CREATE_META_IMAGE = "{    \"__os_version\": \"" + OtcConfig.OS_VERSION + "\",\"container_format\": \"" + OtcConfig.CONTAINTER_FORMAT +  "\",\"disk_format\": \"" + OtcConfig.DISK_FORMAT + "\",    \"min_disk\": " +  OtcConfig.MIN_DISK + ",\"min_ram\": " + OtcConfig.MIN_RAM + ",\"name\": \"" + OtcConfig.IMAGENAME + "\",\"tags\": [\"" + OtcConfig.TAG_LIST + "\",\"image\"],\"visibility\": \"" + OtcConfig.IMAGE_VISIBILITY + "\",\"protected\": " + OtcConfig.PROTECTED + "}"    
        ret = utils_http.post(url, REQ_CREATE_META_IMAGE)        
        ims.otcOutputHandler().print_output(ret, mainkey="") 

        OtcConfig.IMAGE_ID = json.loads(ret)["id"]
        
        if OtcConfig.IMAGE_ID is None: 
            raise RuntimeError("Image not created! " + ret)

        return ret

    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="Registers image",
             examples=[
                       {'Registers image":"otc ims register_image --image-url testuser:c.qcow2'}
                       ],
             args = [ 
                arg(
                    '--image-url',
                    dest='IMAGE_URL',
                    metavar='image_url',
                    default=None,
                    help='Url of the image used during Image creation'
                ),
                arg(
                    '--image-id',
                    dest='IMAGE_ID',
                    metavar='image_id',
                    default=None,
                    help='Id of the image reference will use during VM creation'
                ),
                arg(
                    '--image-name',
                    dest='IMAGENAME',
                    metavar='<image-name>',
                    default=None,
                    help='description of the avaliable clusters'
                ) ]
                )
    def register_image():
        if not (OtcConfig.IMAGENAME is None):
            getplugin("ecs").convertIMAGENameToId()
        
        if OtcConfig.IMAGE_ID is None:
            # error handling 
            raise RuntimeError("Please define image id!")
        
        # image id filled until now 
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v2/images/" + OtcConfig.IMAGE_ID + "/file"
        REQ_REG_IMAGE = "{\"image_url\":\"" + OtcConfig.IMAGE_URL + "\" }"
        ret = utils_http.put(url, REQ_REG_IMAGE)
        if len(ret) != 0: 
            print ("Image registration error!" + ret) 
        return ret

    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="Gets image data",
             examples=[
                       {'Gets image data":"otc ims get_image --image-url testuser:c.qcow2'}
                       ],
             args = [ 
                arg(
                    '--image-url',
                    dest='IMAGE_URL',
                    metavar='image_url',
                    default=None,
                    help='Url of the image used during Image creation'
                ),
                arg(
                    '--image-id',
                    dest='IMAGE_ID',
                    metavar='image_id',
                    default=None,
                    help='Id of the image reference will use during VM creation'
                ),
                arg(
                    '--image-name',
                    dest='IMAGENAME',
                    metavar='<image-name>',
                    default=None,
                    help='description of the avaliable clusters'
                ) ]
                )
    def get_image():
        if not (OtcConfig.IMAGENAME is None):
            getplugin("ecs").convertIMAGENameToId()
        
        if OtcConfig.IMAGE_ID is None:
            # error handling 
            raise RuntimeError("Please define image id!")
         
        # image id filled until now 
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v2/images/" + OtcConfig.IMAGE_ID + "/file"
        REQ_REG_IMAGE = "{\"image_url\":\"" + OtcConfig.IMAGE_URL + "\" }"
        ret = utils_http.post(url, REQ_REG_IMAGE)
        if len(ret) != 0: 
            print ("Image registration error!" + ret) 
        return ret


    @staticmethod
    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="Creates image",
             examples=[
                       {'Creates image":"otc ims create_image --image-url testuser:c.qcow2 --image-name testimagenzs --os-version "Ubuntu 14.04 server 64bit" --container-format bare --disk-format raw --min-disk 1 --min-ram 1024 --tags "test,image" --visibility private --protected false'}
                       ],
             args = [ 
                arg(
                    '--os-version',
                    dest='OS_VERSION',
                    metavar='__os_version',
                    default='Other Linux(64 bit)',
                    help='Specifies the image OS version, if this  is not specified, the value will be set to Other Linux(64 bit)'
                )
                ,
                arg(
                    '--container-format',
                    dest='CONTAINTER_FORMAT',
                    metavar='container_format' ,
                    default=None,
                    help='Container format used during image creation'
                ),
                arg(
                    '--disk_format',
                    dest='DISK_FORMAT',
                    metavar='<disk_format>',
                    default=None,
                    help='Disk format used during image creation'
                )                           ,
                arg(
                    '--min_disk',
                    dest='MIN_DISK',
                    metavar='<min_disk>',
                    default=None,
                    help='Min disk used during image creation'
                )                           ,
                arg(
                    '--min_ram',
                    dest='MIN_RAM',
                    metavar='<min_ram>',
                    default=None,
                    help='Min ram used during image creation'
                )                           ,
                arg(
                    '--image-name',
                    dest='IMAGENAME',
                    metavar='<image-name>',
                    default=None,
                    help='description of the avaliable clusters'
                )                           ,
                arg(
                    '--tags',
                    dest='TAG_LIST',
                    metavar='<tags>',
                    default=None,
                    help='Tags of the image will used during Image creation'
                )                           ,
                arg(
                    '--visibility',
                    dest='IMAGE_VISIBILITY',
                    metavar='<visibility>',
                    default=None,
                    help='Image visibility used during image creation'
                )                           ,
                arg(
                    '--protected   ',
                    dest='PROTECTED',
                    metavar='<protected>',
                    default=None,
                    help='Protected status of  image used during VM creation'
                ),
                arg(
                    '--image-url',
                    dest='IMAGE_URL',
                    metavar='image_url',
                    default=None,
                    help='Url of the image used during Image creation'
                )]
                )     
    def create_image():        
        ims.create_image_metadata()        
        ret = ims.register_image()        
        return ret
