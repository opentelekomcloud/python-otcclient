#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of OTC Tool released under MIT license.
# Copyright (C) 2016 T-systems Kurt Garloff, Zsolt Nagy

import imp
import os
import sys

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
        py_mod = imp.load_compiled(mod_name, filepath)        
    else:
        return None
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

def getFunc(command=None,subcommand=None):    
    plugin = plugins[command.lower()]    
    funcname = subcommand.lower().replace('-','_')
    func = getattr(plugin, funcname)
    return func

if len(plugins) == 0:
    initPlugins()
