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
 
    
class mrs(otcpluginbase):
    ar = {}    
    
    @staticmethod
    def otcOutputHandler(): 
        return getplugin(OtcConfig.OUTPUT_FORMAT)
 
    def otctype(self):
        return "func" 

    
    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="description of the avaliable clusters",
             examples=[
                       {"List Clusters":"otc mrs describe_clusters"}, 
                       {"Show Cluster Details":"otc mrs describe_clusters mycluster"}
                       ],
             args = [ 
                arg(
                    '--cluster-name',
                    dest='CLUSTER',
                    help='description of the avaliable clusters'
                )
                ,
                arg(
                    '--cluster-id',
                    dest='CLUSTER_ID',
                    metavar='<cluster_id>',
                    default=None,
                    help='description of the avaliable clusters'
                )                                            
                ]                
             )
    def describe_clusters():        
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.1/"+ OtcConfig.PROJECT_ID +"/cluster_infos"
        url = url.replace("iam", "mrs") 
        if OtcConfig.CLUSTER_ID is None:
            print(url) 
            ret = utils_http.get(url)
            mrs.otcOutputHandler().print_output(ret, mainkey = "")
        else:            
            ret = utils_http.get(url + '/' + OtcConfig.CLUSTER_ID )        
            maindata = json.loads(ret)
            if "itemNotFound" in  maindata:
                raise RuntimeError("Not found!")                      
            mrs.otcOutputHandler().print_output(ret,mainkey="") 
        return ret


    @staticmethod
    def convertCLUSTERNameToId():
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.1/"+ OtcConfig.PROJECT_ID +"/    "
        
        url = url.replace("iam", "mrs")        
        JSON = utils_http.get(url)
        #print JSON         
        parsed  = json.loads(JSON)  
              
        servers = parsed["clusters"]

        ret = None
        for server in servers:
            if server.get("clusterName") == OtcConfig.CLUSTER:
                ret = server["clusterId"]
        if ret:
            OtcConfig.CLUSTER_ID = ret  
    
    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="description of the avaliable hosts in specified cluster",
             examples=[
                       {"List Clusters":"otc mrs describe_clusterhosts"}, 
                       {"Show Cluster Details":"otc mrs describe_clusterhosts mycluster"}
                       ],
             args = [ 
                arg(
                    '--cluster-name',
                    dest='CLUSTER',
                    help='description of the avaliable clusters'
                )
                ,
                arg(
                    '--cluster-id',
                    dest='CLUSTER_ID',
                    metavar='<cluster_id>',
                    default=None,
                    help='description of the avaliable clusters'
                )                                            
                ]                
             )
    def describe_clusterhosts():                 
        if not (OtcConfig.CLUSTER is None):
            getplugin("mrs").convertCLUSTERNameToId()
         
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.1/"+ OtcConfig.PROJECT_ID +"/clusters/" + OtcConfig.CLUSTER_ID + "/hosts"        
        url = url.replace("iam", "mrs")
                                     
        ret = utils_http.get( url )
                            
        mrs.otcOutputHandler().print_output(ret,mainkey="") 
        return ret


    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="add new node(s) to cluster",
             examples=[
                       {"add node(s)":"otc mrs add-node MYCLUSTER_ID NUM OF NODE"}
                       ],
             args = [ 
                arg(
                    '--cluster-id',
                    dest='CLUSTER_ID',
                    metavar='<cluster_id>',
                    default=None,
                    help='id of the cluster'
                )                                            
                ]                   
             )
    def add_nodes():
        REQ_ADD_NODE=utils_templates.create_request("add_node")               
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.1/"+ OtcConfig.PROJECT_ID +"/cluster_infos/" + OtcConfig.CLUSTER_ID 
        ret = utils_http.post(url, REQ_ADD_NODE)
        print (url)
        print (ret)        
        mrs.otcOutputHandler().print_output(ret, mainkey = "") 


    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="add new node(s) to cluster",
             examples=[
                       {"add node(s)":"otc mrs add-node MYCLUSTER_ID NUM OF NODE"}
                       ],
             args = [ 
                arg(
                    '--cluster-id',
                    dest='CLUSTER_ID',
                    metavar='<cluster_id>',
                    default=None,
                    help='id of the cluster'
                )                                            
                ]                   
             )
    def add_as():
        if not (OtcConfig.CLUSTER is None):
            getplugin("mrs").convertCLUSTERNameToId()
         
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.1/"+ OtcConfig.PROJECT_ID +"/autoscaling-policy/" + OtcConfig.CLUSTER_ID         
        url = url.replace("iam", "mrs")
                                                
        REQ_ADD_NODE=utils_templates.create_request("add_as")               
         
        ret = utils_http.post(url, REQ_ADD_NODE)
        print (url)
        print (ret)        
        mrs.otcOutputHandler().print_output(ret, mainkey = "") 


    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="create hadoop cluster",
             args = [ 
                arg(
                    '--cluster-name',
                    dest='CLUSTER',
                    help='create cluster'
                )
                ]                
             )
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
        print(REQ_CREATE_CLUSTER)
        print (url)
        print (ret)        
        mrs.otcOutputHandler().print_output(ret, mainkey = "") 

    
    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="description of the cluster",
             examples=[
                       {"List jobs":"otc mrs describe-cluster MYCLUSTER-ID"} 
                       ],
             args = [ 
                arg(
                    '-cluster-id',
                    dest='CLUSTER_ID',
                    metavar='<cluster_id>',
                    default=None,
                    help='id of the cluster'
                )                                            
                ]                   
             )
    def describe_cluster():
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.1/"+ OtcConfig.PROJECT_ID +"/cluster_infos/" + OtcConfig.CLUSTER_ID        
        ret = utils_http.get(url)
        print (url)
        print (ret)        
        mrs.otcOutputHandler().print_output(ret, mainkey = "") 
        return ret
    
    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="delete specific cluster",
             examples=[
                       {"List jobs":"otc mrs delete-cluster --cluster-id MYCLUSTER-ID"} 
                       ],
             args = [ 
                arg(
                    '-cluster-id',
                    dest='CLUSTER_ID',
                    metavar='<cluster_id>',
                    default=None,
                    help='id of the cluster'
                )                                            
                ]                   
             )    

    
    def delete_cluster():
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.1/"+ OtcConfig.PROJECT_ID +"/clusters/" + OtcConfig.CLUSTER_ID        
        ret = utils_http.delete(url)
        print (url)
        print (ret)        
        mrs.otcOutputHandler().print_output(ret, mainkey = "") 
        return ret
    
    
    
    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="add job to cluster",
             examples=[
                       {"add job":"otc mrs add-job !!!!!!!!!"}
                       ],
             args = [ 
                arg(
                    '-cluster-id',
                    dest='CLUSTER_ID',
                    metavar='<cluster_id>',
                    default=None,
                    help='id of the cluster'
                )                                            
                ]                   
             )
    def add_job():
        REQ_ADD_JOB=utils_templates.create_request("add_job")               
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.1/"+ OtcConfig.PROJECT_ID +"/jobs/submit-job"
        ret = utils_http.post(url, REQ_ADD_JOB)
        print (url)
        print (ret)        
        mrs.otcOutputHandler().print_output(ret, mainkey = "") 
    
    
    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="description of the avaliable jobs",
             examples=[
                       {"List jobs":"otc mrs describe-jobs"}, 
                       {"Show Cluster Details":"otc mrs jobs of the cluster"}
                       ]             
             )
    def describe_jobs():
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.1/"+ OtcConfig.PROJECT_ID +"/job-exes"
        
        ret = utils_http.get(url)
        print (url)
        print (ret)        
        mrs.otcOutputHandler().print_output(ret, mainkey = "") 
        return ret


    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="description of the job detail",
             examples=[
                       {"List jobs":"otc mrs describe-job-detail -jobexecid JOB-EXEC-ID"}                        
                       ],
             args = [ 
                arg(
                    '--job-exec-id',
                    dest='JOB_EXEC_ID',
                    help='id of the job'
                )
                ]             
             )
    def describe_job_details():
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.1/"+ OtcConfig.PROJECT_ID +"/job-exes/" + OtcConfig.JOB-EXEC-ID
        ret = utils_http.get(url)
        print (url)
        print (ret)        
        mrs.otcOutputHandler().print_output(ret, mainkey = "") 
        return ret

    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="delete the job ",
             examples=[
                       {"List jobs":"otc mrs delete-job -jobexecid JOB-EXEC-ID"}                        
                       ],
             args = [ 
                arg(
                    '-job-exec-id',
                    dest='JOB_EXEC_ID',
                    help='id of the job'
                )
                ]             
             )
    def delete_job():
        url = "https://" + OtcConfig.DEFAULT_HOST + "/v1.1/"+ OtcConfig.PROJECT_ID +"/job-executions/" + OtcConfig.JOB_EXEC_ID        
        ret = utils_http.delete(url)
        print (url)
        print (ret)        
        mrs.otcOutputHandler().print_output(ret, mainkey = "") 
        return ret
