#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is part of OTC Tool released under MIT license.
# Copyright (C) 2016 T-systems Kurt Garloff, Zsolt Nagy

import os
from jinja2 import Environment, FileSystemLoader
from otcclient.core.OtcConfig import OtcConfig
import inspect

# -------------------------------
#templateFolder = os.path.join( os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) , "templates")
# -------------------------------

# plugins/<plugin direcory>/templates/<template_name>.template
templateFolder = os.path.join(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)), "plugins")

TEMPLATE_ENVIRONMENT = Environment(autoescape = False,
                                   loader = FileSystemLoader(templateFolder),
                                   trim_blocks = False)

def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)

def create_plugin_request(pluginname, template):    
    template_file_name = pluginname + "/templates/" + template + '.template'
    # -----------------------------------------------------------
    # plugin arch
    #template_file_name = template+ '.template'
    # -----------------------------------------------------------
    
    if OtcConfig.CLIINPUTJSONFILE: 
        with open(OtcConfig.CLIINPUTJSONFILE, "rb") as _file:
            req = _file.read()        
    else:        
        req = render_template(template_file_name, OtcConfig.__dict__)
    return req

def automodule():
    # frame = inspect.stack()[2]
    # module = inspect.getmodule(frame[0])
    # module.__name__.split(".")[-1]
    fname = str(inspect.stack()[2][1])
    return os.path.basename(fname).split(".")[0] 

def create_request(template):
    modulename =  automodule()        
    req = create_plugin_request(modulename, template)
    return req
