#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of OTC Tool released under MIT license.
# Copyright (C) 2016 T-systems Kurt Garloff, Zsolt Nagy

import imp
import os
import sys
import inspect

sys.path.append('plugins')

os.path.dirname(os.path.realpath(__file__))
PluginFolder = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) + "/plugins"
plugins = {}


def load_from_file(filepath):
    mod_name,file_ext = os.path.splitext(os.path.split(filepath)[-1])
    if mod_name.startswith("__init__"): 
        return 
    if file_ext.lower() == '.py':
        py_mod = imp.load_source(mod_name, filepath)
    elif file_ext.lower() == '.pyc':
        return None
        py_mod = imp.load_compiled(mod_name, filepath)        
    class_inst = getattr(py_mod, mod_name)()
    return class_inst

def initPlugins():    
    possibleplugins = os.listdir(PluginFolder)
    for i in possibleplugins:
        location = os.path.abspath(os.path.join(PluginFolder, i))
        
        if os.path.isdir(location) :
            continue        
        p = load_from_file(location)
        if p :
            name = os.path.splitext(os.path.split(location)[-1])[0]        
            plugins[name] = p 
    return plugins

def getType(plugintype="func"):
    tempp = list()
    for _,v in plugins:
        if v.otctype == plugintype:
            tempp.append(v)    
    return tempp

def getplugin(pluginname):
    plugin = plugins[pluginname]
    return plugin

def getFunc(command=None,subcommand=None,command2=None,subcommand2=None):    
    plugin = plugins[command.lower()]    
    funcname = subcommand.lower().replace('-','_')
    func = getattr(plugin, funcname)
    return func

global inspect_class  
def acceptMethod(tup):
    #internal function that analyzes the tuples returned by getmembers tup[1] is the 
    #actual member object
    class_only=False
    instance_only=False
    exclude_internal=False
    is_method = inspect.ismethod(tup[1])
    if is_method:
        bound_to = tup[1].im_self
        internal = tup[1].im_func.func_name[:2] == '__' and tup[1].im_func.func_name[-2:] == '__'
        if internal and exclude_internal:
            include = False
        else:
            include = (bound_to == inspect_class and not instance_only) or (bound_to == None and not class_only)
    else:
        include = False
    return include

def classMethods(the_class,class_only=False,instance_only=False,exclude_internal=False):
    inspect_class = the_class    
#uses filter to return results according to internal function and arguments
    return filter(acceptMethod,inspect.getmembers(the_class))

if len(plugins) == 0:
    initPlugins()
