#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of OTC Tool released under MIT license.
# Copyright (C) 2016 T-systems Kurt Garloff, Zsolt Nagy

from otcclient.core.OtcConfig import OtcConfig 
import requests
requests.packages.urllib3.disable_warnings()  # @UndefinedVariable

def delete( requestUrl):        
    try:
        response = httpcall(requestUrl,delete=True)                               
        ret = response.text
    except Exception as e:
        print (str(e))
    finally:
        pass        
    return ret

def get( requestUrl):
    ret = None
    try:
        response = httpcall(requestUrl)                       
        token = response.headers.get('X-Subject-Token')   
        if  token != None and len( response.headers.get('X-Subject-Token')) > 0:
            OtcConfig.TOKEN = response.headers.get("X-Subject-Token")            
        ret = response.text
    except Exception as e:
        print (str(e))
    finally:
        pass
    return ret

def post( requestUrl, postbody):
    ret = None
    try:
        response = httpcall(requestUrl, datastr=str(postbody))                          
        token = response.headers.get('X-Subject-Token')   
        if  token != None and len( response.headers.get('X-Subject-Token')) > 0:
            OtcConfig.TOKEN = response.headers.get("X-Subject-Token")            
        ret = response.text
    except Exception as e:
        print (str(e))
    finally:
        pass
    return ret

def put( requestUrl, postbody):
    ret = None
    try:
        response = httpcall(requestUrl, datastr=str(postbody), put=True)                          
        token = response.headers.get('X-Subject-Token')   
        if  token != None and len( response.headers.get('X-Subject-Token')) > 0:
            OtcConfig.TOKEN = response.headers.get("X-Subject-Token")            
        ret = response.text
    except Exception as e:
        print (str(e))
    finally:
        pass
    return ret


def httpcall( url, datastr=None, delete=None, put=None):            
    s = requests.session()        
    headers = {'Content-Type': 'application/json',  'Accept': 'application/json' }
    
    if len(OtcConfig.TOKEN) > 0:
        headers['X-Auth-Token'] = OtcConfig.TOKEN

    if OtcConfig.CLUSTER_ID:
        headers['X-Cluster-Uuid'] = OtcConfig.CLUSTER_ID


    if put:
        data = datastr        
        response=s.put(url, data, headers=headers, verify=False)
    elif datastr:
        data = datastr        
        response=s.post(url, data, headers=headers, verify=False)        
    elif delete:
        response=s.delete(url,headers=headers, verify=False)
    else:
        response=s.get(url, headers=headers, verify=False)
    return response