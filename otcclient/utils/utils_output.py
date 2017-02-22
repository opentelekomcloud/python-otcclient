#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is part of OTC Tool released under MIT
# Copyright (C) 2016 T-systems Kurt Garloff, Zsolt Nagy

import json
import prettytable
import jmespath
import sys
from otcclient.core.argmanager import get_help_iter
 
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
        print (json.dumps(parsed, indent=4, sort_keys=True)) 
    else: 
        if(outformat.startswith("text")) :                        
            p.set_style(prettytable.PLAIN_COLUMNS)    
        mainId = respjson
        if mainkey and len(mainkey) > 0:
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
        print (p.get_string())

def handleQuery(result, query):
    if isinstance(result, (str, unicode)):
        parsed = json.loads(result)
    else:
        parsed = result
                
    sr = jmespath.search(query, parsed)    
    if isinstance(sr, list):
        for object_ in sr:
            print (object_)
    else:        
        print (sr)
    
    

def printJsonTableTransverse(jsonval, outformat, mainkey):    
    parsed = json.loads(jsonval)
    if(outformat.startswith("json")) :            
        print (json.dumps(parsed, indent=4, sort_keys=True)) 
    else: 
        if(outformat.startswith("text")) :                        
            x.set_style(prettytable.PLAIN_COLUMNS)    
        if mainkey:
            id_generator(parsed[mainkey], "")
        else:
            id_generator(parsed, "")
        print (x.get_string())

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



# Print iterations progress
def printProgress (iteration, total, prefix = '', suffix = '', decimals = 1, barLength = 100, fill = '#'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        barLength   - Optional  : character length of bar (Int)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(barLength * iteration // total)
    bar = fill * filledLength + '-' * (barLength - filledLength)
    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percent, '%', suffix)),
    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()


def printShortHelp():
    print("usage: otc [-h] [-V] [-d] [--configure [{user,proxy}]] <plugin name> <command>")
    print("Available plugin commands:")
    
    for i in get_help_iter():
        print("    "+ i["plugin_name"] + " " + i["func_name"])
    
    indent = len("otc") * " "
    sys.stderr.write("otc" + ": " + "\n")
    sys.stderr.write(indent + "  for help use --help\n")
        
    print("More information: ")        
    print("    otc --help")