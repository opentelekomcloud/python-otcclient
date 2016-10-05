#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is part of OTC Tool released under MIT license.
# Copyright (C) 2016 T-systems Kurt Garloff, Zsolt Nagy

import os
from jinja2 import Environment, FileSystemLoader
from otcclient.core.OtcConfig import OtcConfig

templateFolder = os.path.join( os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) , "templates")
 
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(templateFolder), #
    trim_blocks=False)


def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)


def create_request(template):
    template_file_name = template+ '.template'
    if OtcConfig.CLIINPUTJSONFILE: 
        with open(OtcConfig.CLIINPUTJSONFILE, "rb") as _file:
            req= _file.read()        
        #req = render_template(OtcConfig.CLIINPUTJSONFILE, OtcConfig.__dict__)
    else:        
        req = render_template(template_file_name, OtcConfig.__dict__)
    return req

