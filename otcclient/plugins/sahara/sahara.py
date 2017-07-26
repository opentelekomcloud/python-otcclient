#aws emr create-cluster --name "Add Spark Step Cluster" --release-label emr-5.5.0 --applications Name=Spark \
#--ec2-attributes KeyName=myKey --instance-type m3.xlarge --instance-count 3 \
#--steps Type=Spark,Name="Spark Program",ActionOnFailure=CONTINUE,Args=[--class,org.apache.spark.examples.SparkPi,/usr/lib/spark/lib/spark-examples.jar,10] --use-default-roles


#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of OTC Tool released under MIT license.
# Copyright (C) 2016 T-systems Kurt Garloff, Zsolt Nagy


from otcclient.core.OtcConfig import OtcConfig 
from otcclient.utils import utils_http

from otcclient.core.otcpluginbase import otcpluginbase
from otcclient.core.pluginmanager import getplugin

import json
from otcclient.core.argmanager import arg, otcfunc
from otcclient.utils import utils_templates 
 
    
class sahara(otcpluginbase):
    ar = {}    
    
    @staticmethod
    def otcOutputHandler(): 
        return getplugin(OtcConfig.OUTPUT_FORMAT)
 
    def otctype(self):
        return "func" 

    @staticmethod
    def create_datasource():        
        REQ_ADD_NODE=utils_templates.create_request("create_datasource")                       
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.1/"+ OtcConfig.PROJECT_ID +"/data-sources"
        ret = utils_http.post(url, REQ_ADD_NODE)
        
        print (url)
        print (ret)        
        sahara.otcOutputHandler().print_output(ret, mainkey = "") 


    @staticmethod
    def update_datasource():
                       
        if not (OtcConfig.DATASOURCE_ID is None):
            getplugin("sahara").convertDATASOURCENameToId()
        
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.1/"+ OtcConfig.PROJECT_ID +"/data-sources/" + OtcConfig.DATASOURCE_ID
          
        
        REQ_UPDADTE_DATASORCE=utils_templates.create_request("update_datasource")

        ret = utils_http.put(url, REQ_UPDADTE_DATASORCE)
        print REQ_UPDADTE_DATASORCE
        print (url)
        print (ret)        
        sahara.otcOutputHandler().print_output(ret, mainkey = "") 



    @staticmethod
    def convertDATASOURCENameToId():
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.1/"+ OtcConfig.PROJECT_ID +"/data-sources" 
        JSON = utils_http.get(url)        
        parsed  = json.loads(JSON)
        servers = parsed["data_sources"]                
        ret = None
        for server in servers:
            if server.get("name") == OtcConfig.DATASOURCE:
                ret = server["id"]
        OtcConfig.DATASOURCE_ID = ret  
        
    @staticmethod
    def describe_datasources():        
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.1/"+ OtcConfig.PROJECT_ID +"/data-sources"    
        
        if not (OtcConfig.DATASOURCE_ID is None):
            getplugin("sahara").convertDATASOURCENameToId()

        if OtcConfig.DATASOURCE_ID is None: 
            ret = utils_http.get(url)        
            sahara.otcOutputHandler().print_output(ret, mainkey = "")
        else:            
            ret = utils_http.get(url + '/' + OtcConfig.SOURCE_GROUP_ID )        
            maindata = json.loads(ret)
            if "itemNotFound" in  maindata:
                raise RuntimeError("Not found!")                      
            sahara.otcOutputHandler().print_output(ret, mainkey = "") 
        return ret



    
    @staticmethod
    def delete_datasource():
        if not (OtcConfig.DATASOURCE is None):
            getplugin("sahara").convertDATASOURCENameToId()
        
        if OtcConfig.DATASOURCE_ID is  None:
            raise RuntimeError("Not found!")                      
        
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.1/"+ OtcConfig.PROJECT_ID +"/data-sources/" + OtcConfig.DATASOURCE_ID
        ret = utils_http.delete(url)
        sahara.otcOutputHandler().print_output(ret, mainkey = "") 
        return ret
    
# ----------------------------------------------------------------------    
# CLUSTER MANAGMENT INTERFACE     
# ----------------------------------------------------------------------

    @staticmethod
    def create_cluster():               
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.1/"+ OtcConfig.PROJECT_ID +"/run-job-flow"
        #vpc_id
        if not (OtcConfig.VPCNAME is None):
            getplugin("ecs").convertVPCNameToId()
          
        #network_id
        if not OtcConfig.SUBNETNAME is None:
            getplugin("ecs").convertSUBNETNameToId()

        
        REQ_CREATE_CLUSTER=utils_templates.create_request("create_cluster_with_job")

        ret = utils_http.post(url, REQ_CREATE_CLUSTER)
        print REQ_CREATE_CLUSTER
        print (url)
        print (ret)        
        sahara.otcOutputHandler().print_output(ret, mainkey = "") 


    @staticmethod
    def add_nodes():
        REQ_ADD_NODE=utils_templates.create_request("add_node")               
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.1/"+ OtcConfig.PROJECT_ID +"/cluster_infos/" + OtcConfig.CLUSTER_ID 
        ret = utils_http.post(url, REQ_ADD_NODE)
        print (url)
        print (ret)        
        sahara.otcOutputHandler().print_output(ret, mainkey = "") 
    



    @staticmethod
    def describe_clusters():
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.1/"+ OtcConfig.PROJECT_ID +"/cluster_infos/" + OtcConfig.CLUSTER_ID
        
        if OtcConfig.CLUSTER_ID is None: 
            ret = utils_http.get(url)
            print (url)
            print (ret)        
            #sahara.otcOutputHandler().print_output(ret, mainkey = "clusters", listkey={"id", "name"})
            sahara.otcOutputHandler().print_output(ret, mainkey = "") 
        else:            
            ret = utils_http.get(url + '/' + OtcConfig.CLUSTER_ID)        
            maindata = json.loads(ret)
            if "itemNotFound" in  maindata:
                raise RuntimeError("Not found!")                      
            sahara.otcOutputHandler().print_output(ret, mainkey = "") 
            #sahara.otcOutputHandler().print_output(ret,mainkey="server") 
        return ret



    @staticmethod    
    def delete_cluster():
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.1/"+ OtcConfig.PROJECT_ID +"/clusters/" + OtcConfig.CLUSTER_ID        
        ret = utils_http.delete(url)
        print (url)
        print (ret)        
        sahara.otcOutputHandler().print_output(ret, mainkey = "") 
        return ret

# ----------------------------------------------------------------------    
# JOB BINARY OBJECT INTERFACE     
# ----------------------------------------------------------------------
    @staticmethod
    def create_jobbinary():
        REQ_ADD_JOBBIN=utils_templates.create_request("create_jobbinary")               
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.1/"+ OtcConfig.PROJECT_ID +"/job-binaries"
        ret = utils_http.post(url, REQ_ADD_JOBBIN)
        print (url)
        print (ret)        
        sahara.otcOutputHandler().print_output(ret, mainkey = "") 



    @staticmethod
    def update_jobbinary():               
        if not (OtcConfig.JOBBINARY is None):
            getplugin("sahara").convertJOBBINARYNameToId()

        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.1/"+ OtcConfig.PROJECT_ID +"/job-binaries/" + OtcConfig.JOBBINARY_ID
                  
        REQ_UPDADTE_JOBBINARY=utils_templates.create_request("update_jobbinary")
        ret = utils_http.put(url, REQ_UPDADTE_JOBBINARY)
        print (url)
        print (ret)        
        sahara.otcOutputHandler().print_output(ret, mainkey = "") 



    @staticmethod
    def convertJOBBINARYNameToId():
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.1/"+ OtcConfig.PROJECT_ID +"/job-binaries"
        JSON = utils_http.get(url)
        parsed  = json.loads(JSON)
        servers = parsed["binaries"]

        ret = None
        for server in servers:
            if server.get("name") == OtcConfig.JOBBINARY:
                ret = server["id"]
        if ret:
            OtcConfig.JOBBINARY_ID = ret  


    @staticmethod
    def describe_jobbinaries():        
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.1/"+ OtcConfig.PROJECT_ID +"/job-binaries"    
        
        if not (OtcConfig.JOBBINARY is None):
            getplugin("sahara").convertJOBBINARYNameToId()

        if OtcConfig.JOBBINARY_ID is None:  # list  
            ret = utils_http.get(url)        
            sahara.otcOutputHandler().print_output(ret, mainkey = "")
        else:             # details
            ret = utils_http.get(url + '/' + OtcConfig.JOBBINARY_ID )        
            maindata = json.loads(ret)
            if "itemNotFound" in  maindata:
                raise RuntimeError("Not found!")                      
            sahara.otcOutputHandler().print_output(ret, mainkey = "") 
        return ret


    @staticmethod
    def delete_jobbinary():
        if not (OtcConfig.JOBBINARY is None):
            getplugin("sahara").convertJOBBINARYNameToId()

        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.1/"+ OtcConfig.PROJECT_ID +"/job-binaries/" + OtcConfig.JOBBINARY_ID
        ret = utils_http.delete(url)
        sahara.otcOutputHandler().print_output(ret, mainkey = "") 
        return ret


# ----------------------------------------------------------------------    
# JOB OBJECT INTERFACE     
# ----------------------------------------------------------------------

    @staticmethod
    def add_job():
        REQ_ADD_JOB=utils_templates.create_request("add_job")               
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.1/"+ OtcConfig.PROJECT_ID +"/jobs/submit-job"
        ret = utils_http.post(url, REQ_ADD_JOB)
        print (url)
        print (ret)        
        sahara.otcOutputHandler().print_output(ret, mainkey = "") 


    @staticmethod
    def create_jobobject():
        REQ_ADD_JOB=utils_templates.create_request("create_jobobject")               
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.1/"+ OtcConfig.PROJECT_ID +"/jobs"
        ret = utils_http.post(url, REQ_ADD_JOB)
        if OtcConfig.DEBUG:
            print REQ_ADD_JOB
        #print (url)
        #print (ret)        
        sahara.otcOutputHandler().print_output(ret, mainkey = "") 


        
    @staticmethod
    def update_jobobject():               
        if not (OtcConfig.JOB is None):
            getplugin("sahara").convertJOBNameToId()

        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.1/"+ OtcConfig.PROJECT_ID +"/jobs/" + OtcConfig.JOB_ID               
        REQ_UPDADTE_JOBOBJECT=utils_templates.create_request("update_jobobject")
        ret = utils_http.patch(url, REQ_UPDADTE_JOBOBJECT)
        sahara.otcOutputHandler().print_output(ret, mainkey = "") 
        

    
    @staticmethod
    def convertJOBNameToId():
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.1/"+ OtcConfig.PROJECT_ID +"/jobs"
        JSON = utils_http.get(url)
        parsed  = json.loads(JSON)
        servers = parsed["jobs"]

        ret = None
        for server in servers:
            if server.get("name") == OtcConfig.JOB:
                ret = server["id"]
        if ret:
            OtcConfig.JOB_ID = ret      
    
    @staticmethod
    def describe_jobs():
        if not (OtcConfig.JOB is None):
            getplugin("sahara").convertJOBNameToId()
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.1/"+ OtcConfig.PROJECT_ID +"/jobs"        
        
        if OtcConfig.JOB_ID is None: 
            ret = utils_http.get(url)
            sahara.otcOutputHandler().print_output(ret, mainkey = "")
        else:            
            ret = utils_http.get(url + '/' + OtcConfig.JOB_ID )        
            maindata = json.loads(ret)
            if "itemNotFound" in  maindata:
                raise RuntimeError("Not found!")                      
            sahara.otcOutputHandler().print_output(ret, mainkey = "") 
        return ret

    @staticmethod
    def delete_jobobject():
        if not (OtcConfig.JOB is None):
            getplugin("sahara").convertJOBNameToId()
        
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.1/"+ OtcConfig.PROJECT_ID +"/jobs/" + OtcConfig.JOB_ID        
        ret = utils_http.delete(url)
        print (url)
        print (ret)        
        sahara.otcOutputHandler().print_output(ret, mainkey = "") 
        return ret


    @staticmethod
    def execute_jobobject():

        if not (OtcConfig.JOB is None):
            getplugin("sahara").convertJOBNameToId()
        REQ_EXECUTE=utils_templates.create_request("execute_jobobject")                       
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.1/"+ OtcConfig.PROJECT_ID +"/jobs/" + OtcConfig.JOB_ID +"/execute"
        ret = utils_http.post(url, REQ_EXECUTE)
        if OtcConfig.DEBUG:        
            print REQ_EXECUTE
            print (url)
            print (ret)        
        sahara.otcOutputHandler().print_output(ret, mainkey = "")     
        return ret


    @staticmethod
    def describe_jobexec_hua():
        url = "https://" + OtcConfig.DEFAULT_HOST +  "/v1.1/" + OtcConfig.PROJECT_ID + "/job-exes"
        
        if OtcConfig.JOBEXEC_ID is None: 
            ret = utils_http.get(url)        
            sahara.otcOutputHandler().print_output(ret, mainkey = "")
        else:            
            ret = utils_http.get(url + '/' + OtcConfig.JOBEXEC_ID )        
            maindata = json.loads(ret)
            if "itemNotFound" in  maindata:
                raise RuntimeError("Not found!")                      
        sahara.otcOutputHandler().print_output(ret, mainkey = "") 
        return ret




    @staticmethod
    def describe_jobexec():
        url = "https://" + OtcConfig.DEFAULT_HOST +  "/v1.1/" + OtcConfig.PROJECT_ID + "/job-executions"
        
        if OtcConfig.JOBEXEC_ID is None: 
            ret = utils_http.get(url)            
            sahara.otcOutputHandler().print_output(ret, mainkey = "") 
        else:            
            ret = utils_http.get(url + '/' + OtcConfig.JOBEXEC_ID )        
            maindata = json.loads(ret)
            if "itemNotFound" in  maindata:
                raise RuntimeError("Not found!")                      
            sahara.otcOutputHandler().print_output(ret, mainkey = "") 
        return ret


    @staticmethod
    def terminate_job():
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.1/"+ OtcConfig.PROJECT_ID +"/job-executions/" + OtcConfig.JOBEXEC_ID + "/cancel"        
        ret = utils_http.get(url)
        print (url)
        print (ret)        
        sahara.otcOutputHandler().print_output(ret, mainkey = "") 
        return ret


    @staticmethod
    def delete_jobexec():
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.1/"+ OtcConfig.PROJECT_ID +"/job-executions/" + OtcConfig.JOBEXEC_ID         
        ret = utils_http.delete(url)
        print (url)
        print (ret)        
        sahara.otcOutputHandler().print_output(ret, mainkey = "") 
        return ret
