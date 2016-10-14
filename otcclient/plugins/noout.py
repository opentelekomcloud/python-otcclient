#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of OTC Tool released under MIT license.
# Copyright (C) 2016 T-systems Kurt Garloff, Zsolt Nagy 

from otcclient.core.OtcConfig import OtcConfig 
from otcclient.core.otcpluginbase import otcpluginbase
from otcclient.utils import utils_output 

class noout(otcpluginbase):
    
    def otctype(self):
        return "utils_output" 
    
    @staticmethod
    def handleQuery(result):
        utils_output.handleQuery(result, OtcConfig.QUERY)
                
    @staticmethod
    def print_output(respjson, **kwargs):
	pass

