#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is part of OTC Tool released under MIT
# Copyright (C) 2016 T-systems Kurt Garloff, Zsolt Nagy

import json
import prettytable
import jmespath
 
#from objectpath import Tree 
#from objectpath.core import generator, chain

 
import sys
import collections

def defaultprettytable( cols ):    
    p = prettytable.PrettyTable(cols)
    p.align = 'l'
    p.sortby = None
    return p    

x=defaultprettytable({"name", "value"})

def printLevel2(respjson, outformat, mainkey, listkey, subkey=None):            
    if mainkey: 
        parsed = json.loads(respjson)
    p=defaultprettytable(listkey)
    if(outformat.startswith("json")) :            
        print json.dumps(parsed, indent=4, sort_keys=True) 
    else: 
        if(outformat.startswith("text")) :                        
            p.set_style(prettytable.PLAIN_COLUMNS)    
        mainId = respjson
        if mainkey:
            mainId = parsed[mainkey]
    
        for n in range(len(mainId)):
            item = mainId[n]
        #for item in mainId:                 
            if not (subkey is None):
                item = item[subkey]
            vals = list()            
            for colkey in listkey:                    
                if colkey in item :
                    vals.append(item[colkey])
                else:
                    vals.append(" ")
            p.add_row(vals)                
        print p.get_string()

def handleQuery(result, query):
    parsed = json.loads(result)
    sr = jmespath.search(query, parsed)    
    if isinstance(sr, list):
        for object_ in sr:
            print object_
    else:        
        print sr
    
    

def printJsonTableTransverse(jsonval, outformat, mainkey):    
    parsed = json.loads(jsonval)
    if(outformat.startswith("json")) :            
        print json.dumps(parsed, indent=4, sort_keys=True) 
    else: 
        if(outformat.startswith("text")) :                        
            x.set_style(prettytable.PLAIN_COLUMNS)    
        id_generator(parsed[mainkey], "")    
        print x.get_string()

def id_generator(parsed, headkey):
    for k, v in parsed.items():
            if isinstance(v, dict):
                id_generator(v, headkey + "." + k)                     
            elif isinstance(v, list):
                for v2 in v:
                    if isinstance(v2, dict):
                        id_generator(v2, headkey + "." + k)
                    else :
                        pass                                     
            else :                    
                if not v : 
                    v = ""                                          
                x.add_row([headkey + "." + k, v ])

