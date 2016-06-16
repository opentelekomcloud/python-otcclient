#!/usr/bin/env python
#
""" generated source for module OtcHttpMethods """
#  
#  * Copyright (c) 2016 T-Systems GmbH
#  * Germany
#  * All rights reserved.
#  * 
#  * Name: ParamFactory.java
#  * Author: zsonagy
#  * Datum: 08.03.2016
#  



from OtcConfig import OtcConfig
import requests
requests.packages.urllib3.disable_warnings()

from wsgiref import headers
from OpenSSL.crypto import verify


class OtcHttpMethods(object):
    """ generated source for class OtcHttpMethods """

    url = 'http://www.someserver.com/cgi-bin/register.cgi'
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    values = {'name': 'Michael Foord',
              'location': 'Northampton',
              'language': 'Python' }
    headers = {'User-Agent': user_agent}
    
    @classmethod
    def put(cls, requestUrl, putBody):
        """ generated source for method put """
        ret = ""
        accessService = None
        try:
            print "a"
#            accessService = AccessServiceImpl(OtcConfig.serviceName, OtcConfig.region, OtcConfig.sk, OtcConfig.sk)
#            ret = convertStreamToString(response.getEntity().getContent())
            # getStatusLine().get();

        except Exception as e:
            e.printStackTrace()
        finally:
            accessService.close()
        return ret

    @classmethod
    def patch(cls, requestUrl, putBody):
        """ generated source for method patch """
        ret = None
        accessService = None
        try:
            print "a"
#            accessService = AccessServiceImpl(OtcConfig.serviceName, OtcConfig.region, OtcConfig.ak, OtcConfig.sk)
#            ret = convertStreamToString(response.getEntity().getContent())
        except Exception as e:
            e.printStackTrace()
        finally:
            accessService.close()
        return ret

    @classmethod
    def delete(cls, requestUrl):
        """ generated source for method delete """
        ret = None
        accessService = None 
        try:
            print "a"
#            accessService = AccessServiceImpl(OtcConfig.serviceName, OtcConfig.region, OtcConfig.ak, OtcConfig.sk)
#            ret = convertStreamToString(response.getEntity().getContent())
        except Exception as e:
            e.printStackTrace()
        finally:
            accessService.close()
        return ret

    @classmethod
    def get(cls, requestUrl):
        """ generated source for method post """
        ret = None
#        accessService = AccessServiceImpl(OtcConfig.serviceName, OtcConfig.region, OtcConfig.ak, OtcConfig.sk)
        try:
            response = cls.httpcall(requestUrl)  
                     
            token = response.headers.get('X-Subject-Token')   
            if  token != None and len( response.headers.get('X-Subject-Token')) > 0:
                OtcConfig.TOKEN = response.headers.get("X-Subject-Token")
            
            ret = response.text
        except Exception as e:
            print e
        finally:
            pass
            #print "TODO close"
        return ret


    @classmethod
    def post(cls, requestUrl, postbody):
        """ generated source for method post """
        ret = None
#        accessService = AccessServiceImpl(OtcConfig.serviceName, OtcConfig.region, OtcConfig.ak, OtcConfig.sk)
        try:
            response = cls.httpcall(requestUrl, datastr=str(postbody))  
                        
            token = response.headers.get('X-Subject-Token')   
            if  token != None and len( response.headers.get('X-Subject-Token')) > 0:
                OtcConfig.TOKEN = response.headers.get("X-Subject-Token")            
            ret = response.text
        except Exception as e:
            print e
        finally:
            pass
            #print "TODO close"
        return ret

    
    @classmethod
    def httpcall( cls,url, datastr=None):    
        
        s = requests.session()
        
#After that, continue with your requests as you would:

#logged in! cookies saved for future requests.

        headers = {'Content-Type': 'application/json',  'Accept': 'application/json' }
        
        if len(OtcConfig.TOKEN) > 0:
            headers['X-Auth-Token'] = OtcConfig.TOKEN
        if datastr:
            data = datastr #urllib.urlencode(datastr)
            #print data
            response=s.post(url, data, headers=headers, verify=False)
        else:
            response=s.get(url, headers=headers, verify=False)
        return response
#proxy        
        #proxy_support = urllib2.ProxyHandler({})
        #opener = urllib2.build_opener(proxy_support)
        #urllib2.install_opener(opener)

    @classmethod
    def convertStreamToString(cls, is_):
        """ generated source for method convertStreamToString """
