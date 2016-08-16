#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of OTC Tool released under MIT license.
# Copyright (C) 2016 T-systems Kurt Garloff, Zsolt Nagy


from otcclient.core.OtcConfig import OtcConfig 
from otcclient.utils import utils_http

from otcclient.core.otcpluginbase import otcpluginbase
from otcclient.core.pluginmanager import getplugin

import json
from otcclient.plugins.ecs import ecs

    
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
            ecs.convertIMAGENameToId()
        ims.create_image_metadata()

    @staticmethod
    def create_image_metadata():
                
        # image id filled until now 
        url = ims.baseurl + "/v2/images" 
        REQ_CREATE_META_IMAGE = "{    \"__os_version\": \"" + OtcConfig.OS_VERSION + "\",\"container_format\": \"" + OtcConfig.CONTAINTER_FORMAT +  "\",\"disk_format\": \"" + OtcConfig.DISK_FORMAT + "\",    \"min_disk\": " +  OtcConfig.MIN_DISK + ",\"min_ram\": " + OtcConfig.MIN_RAM + ",\"name\": \"" + OtcConfig.IMAGENAME + "\",\"tags\": [\"" + OtcConfig.TAG_LIST + "\",\"image\"],\"visibility\": \"" + OtcConfig.IMAGE_VISIBILITY + "\",\"protected\": " + OtcConfig.PROTECTED + "}"    
        ret = utils_http.post(url, REQ_CREATE_META_IMAGE)        
        ims.otcOutputHandler().print_output(ret, mainkey="") 

        OtcConfig.IMAGE_ID = json.loads(ret)["id"]
        
        if OtcConfig.IMAGE_ID is None: 
            raise RuntimeError("Image not created! " + ret)

        return ret

    @staticmethod
    def register_image():
        if not (OtcConfig.IMAGENAME is None):
            ecs.convertIMAGENameToId()
        
        if OtcConfig.IMAGE_ID is None:
            # error handling 
            raise RuntimeError("Please define image id!")
        
        # image id filled until now 
        url = ims.baseurl + "/v2/images/" + OtcConfig.IMAGE_ID + "/file"
        REQ_REG_IMAGE = "{\"image_url\":\"" + OtcConfig.IMAGE_URL + "\" }"
        ret = utils_http.put(url, REQ_REG_IMAGE)
        if len(ret) != 0: 
            print ("Image registration error!" + ret) 
        return ret

    @staticmethod
    def get_image():
        if not (OtcConfig.IMAGENAME is None):
            ecs.convertIMAGENameToId()
        
        if OtcConfig.IMAGE_ID is None:
            # error handling 
            raise RuntimeError("Please define image id!")
         
        # image id filled until now 
        url = ims.baseurl + "/v2/images/" + OtcConfig.IMAGE_ID + "/file"
        REQ_REG_IMAGE = "{\"image_url\":\"" + OtcConfig.IMAGE_URL + "\" }"
        ret = utils_http.post(url, REQ_REG_IMAGE)
        if len(ret) != 0: 
            print ("Image registration error!" + ret) 
        return ret


    @staticmethod
    def create_image():        
        ims.create_image_metadata()        
        ret = ims.register_image()        
        return ret
