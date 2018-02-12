#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of OTC Tool released under MIT license.
# Copyright (C) 2016 T-systems Kurt Garloff, Zsolt Nagy
# NOT used currently (later could change the autentication and plugin tech base on this)

import os
from argparse import ArgumentParser, RawTextHelpFormatter
from otcclient.core.OtcConfig import OtcConfig
import pprint

parser = ArgumentParser(prog='otc' ,  formatter_class=RawTextHelpFormatter ) #RawDescriptionHelpFormatter ,description=program_license
parserall = ArgumentParser(prog='otc' ,  formatter_class=RawTextHelpFormatter ) #RawDescriptionHelpFormatter ,description=program_license

funclist = {}

    
def arg(*args, **kwargs):
    return args, kwargs

def otcfunc(*args, **kwargs):
    """Decorator for CLI args.

    Example:

    >>> @arg("name", help="Name of the new entity")
    ... def entity_create(args):
    ...     pass
    """
    def _decorator(func):        
        add_otc_func(func, *args, **kwargs)
        return func
    return _decorator


def env(*args, **kwargs):
    """Returns the first environment variable set.

    If all are empty, defaults to '' or keyword arg `default`.
    """
    for arg in args:
        value = os.environ.get(arg)
        if value:
            return value
    return kwargs.get('default', '')
        
def add_otc_func(func, *args, **kwargs):
    if type( func ).__name__ == 'staticmethod':
        return;

    args_temp = dict( kwargs )
    args_temp["func_name"] = func.__name__
    key = kwargs.get("plugin_name") + "-" + func.__name__ 
    if key not in funclist:
        funclist[key] = args_temp      

# 
# add_to_parser( parser, "mrs-describe_clusters" )
# add_to_parser( parserall  )
def add_to_parser( myparser, key ='*' ):    
    for fkey, fval in funclist.items():
        if fkey ==  key or fkey == '*':
            print(fval) 
            for myarg,mykwargs in fval["args"]:         
                myparser.add_argument(  *myarg,**mykwargs  )

    if OtcConfig.DEBUG: 
        pprint(funclist)

def get_help_iter():
    return  list(funclist.values())

