#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of OTC Tool released under MIT license.
# Copyright (C) 2016 T-systems Kurt Garloff, Zsolt Nagy

from otcclient.core.OtcConfig import OtcConfig 
from otcclient.utils import utils_http, utils_templates

from otcclient.core.otcpluginbase import otcpluginbase
from otcclient.core.pluginmanager import getplugin
import json
#from otcclient.plugins.ecs import ecs
from otcclient.core.argmanager import arg, otcfunc    
    
class cce(otcpluginbase):
    ar = {}    
    
    @staticmethod
    def otcOutputHandler(): 
        return getplugin(OtcConfig.OUTPUT_FORMAT)
 
    def otctype(self):
        return "func" 


#ret = utils_templates.create_request("template_name")
#return ret

    @staticmethod
    def convertClusterNameToId():
        url = "https://cce.eu-de.otc.t-systems.com" + "/api/v1/clusters"
        JSON = utils_http.get(url)
        # print JSON        
        parsed  = json.loads(JSON)
        clusters = parsed
        ret = None
        for cluster in clusters:
            if cluster.get("metadata").get("name") == OtcConfig.CLUSTER:
                ret = cluster.get("metadata").get("uuid")
        OtcConfig.CLUSTER_ID = ret



    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="List clusters",
             examples=[],
             args = []) 
    def list_clusters():
        url = "https://cce.eu-de.otc.t-systems.com" + "/api/v1/clusters"
        ret = utils_http.get(url)
        #print (ret)
        cce.otcOutputHandler().print_output(json.loads(ret), subkey="metadata", listkey={"name", "uuid", "createAt"})
        #cce.otcOutputHandler().print_output(json.loads(ret),mainkey="")     
        return ret

    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="Describe clusters",
             examples=[],
             args = [ arg(    '--cluster-name',    dest='CLUSTER',     help='Name of the cluster')
                ]) 
    def describe_clusters():        
        if OtcConfig.CLUSTER:
            cce.convertClusterNameToId()
                
        if OtcConfig.CLUSTER_ID:
            url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/clusters/" + OtcConfig.CLUSTER_ID            
            ret = utils_http.get(url)
            cce.otcOutputHandler().print_output(ret,mainkey="")     
        else:
            return cce.list_clusters()     

    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="List container intaces",
             args = [ arg(    '--cluster-name',    dest='CLUSTER',     help='Name of the cluster'),
                       arg(    '--instance-name',     dest='INSTANCE_NAME',     help='Instance name of the VM')
                ])    
    def list_container_instances():
        if OtcConfig.CLUSTER:
            cce.convertClusterNameToId()

        if OtcConfig.INSTANCE_NAME:
            cce.convertINSTANCENameToId()
        
        if OtcConfig.INSTANCE_ID:
            url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/clusters/" + OtcConfig.CLUSTER_ID + "/hosts"
            ret = utils_http.get(url)
            cce.otcOutputHandler().print_output(ret,mainkey="")     
        else:
            url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/clusters/" + OtcConfig.CLUSTER_ID + "/hosts/" + OtcConfig.INSTANCE_ID 
            ret = utils_http.get(url)
            cce.otcOutputHandler().print_output(ret,mainkey="")     
        return ret
            

    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="List services",
             examples=[
                       {'Registers image":"otc ims register_image --image-url testuser:c.qcow2'}
                       ],
             args = [ arg(    '--cluster-name',    dest='CLUSTER',     help='Name of the cluster')
                ]) 
    def list_services():
        if OtcConfig.CLUSTER:
            cce.convertClusterNameToId()
        url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/services"
        ret = utils_http.get(url)
        
        print (ret)
        cce.otcOutputHandler().print_output(ret,mainkey="")     
        return ret


    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="Create services",
             examples=[],
            args = [ arg(    '--cluster-name',    dest='CLUSTER',     help='Name of the cluster'),
            arg(    '--service-name',    dest='SERVICE_NAME',     help='CCE Service name'),
            arg(    '--portmin',    dest='PORTMIN',     help='Lower por of the specific security group rule'),
            arg(    '--portmax',    dest='PORTMAX',     help='Upper  port of the specific security group rule')           
                ]) 
    def create_service():
        if OtcConfig.CLUSTER:
            cce.convertClusterNameToId()
                 
        url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/namespaces/" + OtcConfig.NAMESPACE + "/services"
        req = utils_templates.create_request("cce_create_service")
        ret = utils_http.post(url, req)
        cce.otcOutputHandler().print_output(ret,mainkey="")     
        return ret


    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="Create Clusters",
             examples=[],
            args = [ arg(    '--cluster-name',    dest='CLUSTER',     help='Name of the cluster'),
            arg(    '--service-name',    dest='SERVICE_NAME',     help='CCE Service name'),
            arg(    '--portmin',    dest='PORTMIN',     help='Lower por of the specific security group rule'),
            arg(    '--portmax',    dest='PORTMAX',     help='Upper  port of the specific security group rule')           
                ]) 
    def create_cluster():
        #vpc_id
        if not (OtcConfig.VPCNAME is None):
            getplugin("ecs").convertVPCNameToId()
          
        #network_id
        if not OtcConfig.SUBNETNAME is None:
            getplugin("ecs").convertSUBNETNameToId()
                 
        url = "https://cce.eu-de.otc.t-systems.com" + "/api/v1/clusters"
        req = utils_templates.create_request("cce_create_cluster")
        #print url 
        #print req        
        ret = utils_http.post(url, req)
        cce.otcOutputHandler().print_output(ret,mainkey="")     
        return ret

    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="Create Clusters",
             examples=[],
            args = [ arg(    '--cluster-name',    dest='CLUSTER',     help='Name of the cluster'),
            arg(    '--service-name',    dest='SERVICE_NAME',     help='CCE Service name'),
            arg(    '--portmin',    dest='PORTMIN',     help='Lower por of the specific security group rule'),
            arg(    '--portmax',    dest='PORTMAX',     help='Upper  port of the specific security group rule')           
                ]) 
    def add_node():
        #vpc_id
        if not (OtcConfig.CLUSTER is None):
            getplugin("cce").convertClusterNameToId()
                           
        url = "https://cce.eu-de.otc.t-systems.com" + "/api/v1/clusters/" + OtcConfig.CLUSTER_ID  + "/hosts"
        req = utils_templates.create_request("cce_add_node")
        print url 
        print req        
        ret = utils_http.post(url, req)
        cce.otcOutputHandler().print_output(ret,mainkey="")     
        return ret



    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="Modify services",
             examples=[],
            args = [ arg(    '--cluster-name',    dest='CLUSTER',     help='Name of the cluster'),
            arg(    '--service-name',    dest='SERVICE_NAME',     help='CCE Service name'),
            arg(    '--portmin',    dest='PORTMIN',     help='Lower por of the specific security group rule'),
            arg(    '--portmax',    dest='PORTMAX',     help='Upper  port of the specific security group rule')           
                ]) 
    def modify_service():
        if OtcConfig.CLUSTER:
            cce.convertClusterNameToId()
                 
        url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/namespaces/" + OtcConfig.NAMESPACE + "/services/" + OtcConfig.SERVICE_NAME
        req = utils_templates.create_request("cce_create_service")
        ret = utils_http.put(url, req)
        cce.otcOutputHandler().print_output(ret,mainkey="")     
        return ret


    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="Delete services",
             examples=[],
            args = [ arg(    '--cluster-name',    dest='CLUSTER',     help='Name of the cluster')])
    def delete_service():
        if OtcConfig.CLUSTER:
            cce.convertClusterNameToId()
                 
        url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/namespaces/" + OtcConfig.NAMESPACE + "/services/" + OtcConfig.SERVICE_NAME
        ret = utils_http.delete(url)
        cce.otcOutputHandler().print_output(ret,mainkey="")     
        return ret


    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="Delete services",
             examples=[],
            args = [ arg(    '--cluster-name',    dest='CLUSTER',     help='Name of the cluster')])
    def delete_cluster():
        if OtcConfig.CLUSTER:
            cce.convertClusterNameToId()
                 
        url = "https://cce.eu-de.otc.t-systems.com" + "/api/v1/clusters/" + OtcConfig.CLUSTER_ID
        ret = utils_http.delete(url)
        cce.otcOutputHandler().print_output(ret,mainkey="")     
        return ret


    @staticmethod     
    @otcfunc(plugin_name=__name__,
             desc="Create namespace",
             examples=[],
            args = [ arg(    '--cluster-name',    dest='CLUSTER',     help='Name of the cluster'),
            arg(    '--namespace',    dest='NAMESPACE',     help='CES/CCE Namespace')
            ])
    def create_namespace():
        if OtcConfig.CLUSTER:
            cce.convertClusterNameToId()         
        url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/namespaces"
        req = utils_templates.create_request("create_namespace")
        #print req
        #print OtcConfig.NAMESPACE
        ret = utils_http.post(url, req)
        #print (ret)
        cce.otcOutputHandler().print_output(ret,mainkey="")     
        return ret

    @staticmethod      
    @otcfunc(plugin_name=__name__,
             desc="Rename namespace",
             examples=[],
            args = [ arg(    '--cluster-name',    dest='CLUSTER',     help='Name of the cluster'),
            arg(    '--namespace',    dest='NAMESPACE',     help='CES/CCE Namespace'),
            arg(    '',    dest='SUBCOM_P1',     help='[optional Source/Target OBS directory]',metavar="Source/Target DIR")
            ])
    def rename_namespace():
        if OtcConfig.CLUSTER:
            cce.convertClusterNameToId()         
        url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/namespaces"
        req = utils_templates.create_request("cce_rename_namespace")        
        ret = utils_http.post(url, req)
        cce.otcOutputHandler().print_output(ret,mainkey="")     
        return ret


    @staticmethod      
    @otcfunc(plugin_name=__name__,
             desc="Describe namespace",
             examples=[],
            args = [ arg(    '--cluster-name',    dest='CLUSTER',     help='Name of the cluster'),
            arg(    '--namespace',    dest='NAMESPACE',     help='CES/CCE Namespace'),
            ])
    def describe_namespaces():
        if OtcConfig.CLUSTER:
            cce.convertClusterNameToId()
            
        if OtcConfig.NAMESPACE:
            url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/namespaces/" + OtcConfig.NAMESPACE
        else:          
            url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/namespaces"    
        ret = utils_http.get(url)        
        cce.otcOutputHandler().print_output(ret,mainkey="")     
        return ret

    @staticmethod      
    @otcfunc(plugin_name=__name__,
             desc="Delete namespace",
             examples=[],
            args = [ arg(    '--cluster-name',    dest='CLUSTER',     help='Name of the cluster'),
            arg(    '--namespace',    dest='NAMESPACE',     help='CES/CCE Namespace'),
            ]) 
    def delete_namespace():
        if OtcConfig.CLUSTER:
            cce.convertClusterNameToId()
        url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/namespaces/" + OtcConfig.NAMESPACE
        ret = utils_http.delete(url)
        cce.otcOutputHandler().print_output(ret,mainkey="")        
        return ret


    @staticmethod      
    @otcfunc(plugin_name=__name__,
             desc="Describe pods",
             examples=[],
            args = [ arg(    '--cluster-name',    dest='CLUSTER',     help='Name of the cluster'),
            arg(    '--namespace',    dest='NAMESPACE',     help='CES/CCE Namespace'),
            ]) 
    def describe_pods():
        if OtcConfig.CLUSTER:
            cce.convertClusterNameToId()
            
        if OtcConfig.NAMESPACE:
            if OtcConfig.POD:
                url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/namespaces/" + OtcConfig.NAMESPACE + "/pods/" + OtcConfig.POD 
            else:
                url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/namespaces/" + OtcConfig.NAMESPACE + "/pods"
        else:          
            url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/pods"    
        ret = utils_http.get(url)        
        cce.otcOutputHandler().print_output(ret,mainkey="")     
        return ret


    @staticmethod      
    @otcfunc(plugin_name=__name__,
             desc="Create pod",
             examples=[],
            args = [ arg(    '--cluster-name',    dest='CLUSTER',     help='Name of the cluster'),
            arg(    '--namespace',    dest='NAMESPACE',     help='CES/CCE Namespace'),
            arg(    '--pod',    dest='POD',     help='CCE POD'),
            arg(    '--container-name',    dest='CONTAINER_NAME',     help='CCE POD container name'),
            arg(    '--image-name',    dest='IMAGENAME',     help='Name of the image reference will used during VM creation')
            ]) 
    def create_pod():
        if OtcConfig.CLUSTER:
            cce.convertClusterNameToId()            
        
        url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/namespaces/" + OtcConfig.NAMESPACE + "/pods"
        req = utils_templates.create_request("cce_create_pod")
        print (req)        
        ret = utils_http.post(url, req)
        cce.otcOutputHandler().print_output(ret,mainkey="")    
        return ret

    @staticmethod      
    @otcfunc(plugin_name=__name__,
             desc="Delete pod",
             examples=[],
            args = [ arg(    '--cluster-name',    dest='CLUSTER',     help='Name of the cluster'),
            arg(    '--namespace',    dest='NAMESPACE',     help='CES/CCE Namespace'),
            arg(    '--pod',    dest='POD',     help='CCE POD')
            ]) 
    def delete_pod():
        if OtcConfig.CLUSTER:
            cce.convertClusterNameToId()                    
        url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/namespaces/" + OtcConfig.NAMESPACE + "/pods/" + OtcConfig.POD 
                         
        ret = utils_http.delete(url)
        cce.otcOutputHandler().print_output(ret,mainkey="")     
        return ret

    
    @staticmethod      
    @otcfunc(plugin_name=__name__,
             desc="Create pod template",
             examples=[],
            args = [ 
                arg(    '--cluster-name',    dest='CLUSTER',     help='Name of the cluster'),
                arg(    '--namespace',    dest='NAMESPACE',     help='CES/CCE Namespace'),
                arg(    '--pod',    dest='POD',     help='CCE POD'),
                arg(    '--container-name',    dest='CONTAINER_NAME',     help='CCE POD container name'),
                arg(    '--image-name',    dest='IMAGENAME',     help='Name of the image reference will used during VM creation'),
                arg(    '--portmin',    dest='PORTMIN',     help='Lower por of the specific security group rule')
            ]) 
    def create_pod_template():
        if OtcConfig.CLUSTER:
            cce.convertClusterNameToId()
                 
        url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/namespaces/" + OtcConfig.NAMESPACE + "/podtemplates"
        req = utils_templates.create_request("cce_create_pod_template")
        print (req)
        ret = utils_http.post(url, req)
        cce.otcOutputHandler().print_output(ret,mainkey="")     
        return ret

    @staticmethod      
    @otcfunc(plugin_name=__name__,
             desc="Describe pod templates",
             examples=[],
            args = [ arg(    '--cluster-name',    dest='CLUSTER',     help='Name of the cluster'),
            arg(    '--namespace',    dest='NAMESPACE',     help='CES/CCE Namespace'),
            ]) 
    def describe_pod_templates():
        if OtcConfig.CLUSTER:
            cce.convertClusterNameToId()
                    
        if OtcConfig.POD:
            url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/namespaces/" + OtcConfig.NAMESPACE + "/podtemplates/" + OtcConfig.POD 
        else:
            url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/namespaces/" + OtcConfig.NAMESPACE + "/podtemplates"
                         
        ret = utils_http.get(url)
        cce.otcOutputHandler().print_output(ret,mainkey="")     
        return ret
    
    
    @staticmethod      
    @otcfunc(plugin_name=__name__,
             desc="Delete pod templates",
             examples=[],
             args = [
                arg(    '--cluster-name',    dest='CLUSTER',     help='Name of the cluster'),
                arg(    '--namespace',    dest='NAMESPACE',     help='CES/CCE Namespace'),
                arg(    '--pod',    dest='POD',     help='CCE POD')
            ]) 
    def delete_pod_templates():
        if OtcConfig.CLUSTER:
            cce.convertClusterNameToId()
                    
        if OtcConfig.POD:
            url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/namespaces/" + OtcConfig.NAMESPACE + "/podtemplates/" + OtcConfig.POD 
                         
        ret = utils_http.delete(url)
        cce.otcOutputHandler().print_output(ret,mainkey="")     
        return ret
    
    
    @staticmethod      
    @otcfunc(plugin_name=__name__,
             desc="Describe endpoints",
             examples=[],
             args = [
                arg(    '--cluster-name',    dest='CLUSTER',     help='Name of the cluster'),
                arg(    '--namespace',    dest='NAMESPACE',     help='CES/CCE Namespace'),
                arg(    '--endpoint-name',    dest='ENDPOINT_NAME',     help='CCE endpoint name')
                          ]) 
    def describe_endpoints():
        if OtcConfig.CLUSTER:
            cce.convertClusterNameToId()
            
        if OtcConfig.NAMESPACE:
            if OtcConfig.ENDPOINT_NAME:
                url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/namespaces/" + OtcConfig.NAMESPACE + "/endpoints/" + OtcConfig.ENDPOINT_NAME 
            else:
                url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/namespaces/" + OtcConfig.NAMESPACE + "/endpoints"
        else:          
            url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/endpoints"
        
        ret = utils_http.get(url)        
        cce.otcOutputHandler().print_output(ret,mainkey="")     
        return ret


    @staticmethod      
    @otcfunc(plugin_name=__name__,
             desc="Create endpoints",
             examples=[],
             args = [
                arg(    '--cluster-name',    dest='CLUSTER',     help='Name of the cluster'),
                arg(    '--namespace',    dest='NAMESPACE',     help='CES/CCE Namespace'),
                arg(    '--endpoint-name',    dest='ENDPOINT_NAME',     help='CCE endpoint name'),
                arg(    '--public-ip',    dest='PUBLICIP',     help='Public IP for association'),
                arg(    '--portmin',    dest='PORTMIN',     help='Lower por of the specific security group rule')
            ]) 
    def create_endpoint():
        if OtcConfig.CLUSTER:
            cce.convertClusterNameToId()            
        
        url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/namespaces/" + OtcConfig.NAMESPACE + "/endpoints"
        req = utils_templates.create_request("cce_create_endpoint")
        print (req)        
        ret = utils_http.post(url, req)
        cce.otcOutputHandler().print_output(ret,mainkey="")    
        return ret

    @staticmethod      
    @otcfunc(plugin_name=__name__,
             desc="Describe endpoints",
             examples=[],
             args = [
                arg(    '--cluster-name',    dest='CLUSTER',     help='Name of the cluster'),
                arg(    '--namespace',    dest='NAMESPACE',     help='CES/CCE Namespace'),
                arg(    '--endpoint-name',    dest='ENDPOINT_NAME',     help='CCE endpoint name')
                          ]) 
    def delete_endpoint():
        if OtcConfig.CLUSTER:
            cce.convertClusterNameToId()                    
        url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/namespaces/" + OtcConfig.NAMESPACE + "/endpoints/" + OtcConfig.ENDPOINT_NAME 
                         
        ret = utils_http.delete(url)
        cce.otcOutputHandler().print_output(ret,mainkey="")     
        return ret
    
    
    @staticmethod      
    @otcfunc(plugin_name=__name__,
             desc="Describe secrets",
             examples=[],
             args = [
                arg(    '--cluster-name',    dest='CLUSTER',     help='Name of the cluster'),
                arg(    '--namespace',    dest='NAMESPACE',     help='CES/CCE Namespace'),
                arg(    '--secret-name',    dest='SECRET_NAME',     help='CCE secret name')       
                          ]) 
    def describe_secrets():
        if OtcConfig.CLUSTER:
            cce.convertClusterNameToId()
            
        if OtcConfig.SECRET_NAME:
            url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/namespaces/" + OtcConfig.NAMESPACE + "/secrets/" + OtcConfig.SECRET_NAME 
        else:
            url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/namespaces/" + OtcConfig.NAMESPACE + "/secrets"
        
        ret = utils_http.get(url)        
        print (ret)
        cce.otcOutputHandler().print_output(ret,mainkey="")     
        return ret


    @staticmethod      
    @otcfunc(plugin_name=__name__,
             desc="Describe secrets",
             examples=[],
             args = [
                arg(    '--cluster-name',    dest='CLUSTER',     help='Name of the cluster'),
                arg(    '--namespace',    dest='NAMESPACE',     help='CES/CCE Namespace'),
                arg(    '--secret-name',    dest='SECRET_NAME',     help='CCE secret name'),       
                arg(    '--key-name',     dest='KEYNAME',     help='SSH key name| S3 Object key'),
                arg(    '--admin-pass',     dest='ADMINPASS',     help='Admin password of the started VM')
                    ])
    def create_secret():
        if OtcConfig.CLUSTER:
            cce.convertClusterNameToId()            
        
        url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/namespaces/" + OtcConfig.NAMESPACE + "/secrets"
        req = utils_templates.create_request("cce_create_secret")
        #print req        
        ret = utils_http.post(url, req)
        cce.otcOutputHandler().print_output(ret,mainkey="")    
        return ret

    @staticmethod      
    @otcfunc(plugin_name=__name__,
             desc="Describe secrets",
             examples=[],
             args = [
                arg(    '--cluster-name',    dest='CLUSTER',     help='Name of the cluster'),
                arg(    '--namespace',    dest='NAMESPACE',     help='CES/CCE Namespace'),
                arg(    '--secret-name',    dest='SECRET_NAME',     help='CCE secret name')       
                          ]) 
    def delete_secret():
        if OtcConfig.CLUSTER:
            cce.convertClusterNameToId()                    
        url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/namespaces/" + OtcConfig.NAMESPACE + "/secrets/" + OtcConfig.SECRET_NAME
                         
        ret = utils_http.delete(url)
        cce.otcOutputHandler().print_output(ret,mainkey="")     
        return ret
        
        
    @staticmethod      
    @otcfunc(plugin_name=__name__,
             desc="Describe secrets",
             examples=[],
             args = [
                arg(    '--cluster-name',    dest='CLUSTER',     help='Name of the cluster'),
                arg(    '--namespace',    dest='NAMESPACE',     help='CES/CCE Namespace'),
                arg(    '--rc-name',    dest='RC_NAME',     help='CCE replication controller name')    
                          ]) 
    def describe_rc():
        if OtcConfig.CLUSTER:
            cce.convertClusterNameToId()

        if OtcConfig.NAMESPACE:
            if OtcConfig.RC_NAME:
                url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/namespaces/" + OtcConfig.NAMESPACE + "/replicationcontrollers/" + OtcConfig.RC_NAME  
            else:
                url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/namespaces/" + OtcConfig.NAMESPACE + "/replicationcontrollers"   
        else:
            url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/replicationcontrollers"
        
        
        ret = utils_http.get(url)        
        cce.otcOutputHandler().print_output(ret,mainkey="")     
        return ret


    @staticmethod      
    @otcfunc(plugin_name=__name__,
             desc="Describe secrets",
             examples=[],
             args = [
                    arg(    '--cluster-name',    dest='CLUSTER',     help='Name of the cluster'),
                    arg(    '--namespace',    dest='NAMESPACE',     help='CES/CCE Namespace'),
                    arg(    '--rc-name',    dest='RC_NAME',     help='CCE replication controller name') ,
                    arg(    '--secret-name',    dest='SECRET_NAME',     help='CCE secret name') ,                  
                    arg(    '--container-name',    dest='CONTAINER_NAME',     help='CCE POD container name'),
                    arg(    '--image-name',    dest='IMAGENAME',     help='Name of the image reference will used during VM creation'),
                    arg(    '--portmin',    dest='PORTMIN',     help='Lower por of the specific security group rule'),
                    arg(    '--image-ref',     dest='IMAGE_REF',     help='image-ref')
                    ]) 
    def create_rc():
        if OtcConfig.CLUSTER:
            cce.convertClusterNameToId()            
        
        url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/namespaces/" + OtcConfig.NAMESPACE + "/replicationcontrollers"
        req = utils_templates.create_request("cce_create_rc")
        #print req        
        ret = utils_http.post(url, req)
        cce.otcOutputHandler().print_output(ret,mainkey="")    
        return ret

    @staticmethod      
    @otcfunc(plugin_name=__name__,
             desc="Describe secrets",
             examples=[],
             args = [
                    arg(    '--cluster-name',    dest='CLUSTER',     help='Name of the cluster'),
                    arg(    '--namespace',    dest='NAMESPACE',     help='CES/CCE Namespace'),
                    arg(    '--rc-name',    dest='RC_NAME',     help='CCE replication controller name') ,
                    arg(    '--secret-name',    dest='SECRET_NAME',     help='CCE secret name') ,                  
                    arg(    '--container-name',    dest='CONTAINER_NAME',     help='CCE POD container name'),
                    arg(    '--image-name',    dest='IMAGENAME',     help='Name of the image reference will used during VM creation'),
                    arg(    '--portmin',    dest='PORTMIN',     help='Lower por of the specific security group rule'),
                    arg(    '--image-ref',     dest='IMAGE_REF',     help='image-ref')
                    ]) 
    def modify_rc():
        if OtcConfig.CLUSTER:
            cce.convertClusterNameToId()            
        
        url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/namespaces/" + OtcConfig.NAMESPACE + "/replicationcontrollers/" + OtcConfig.RC_NAME
        req = utils_templates.create_request("cce_create_rc")
        #print req        
        ret = utils_http.put(url, req)
        cce.otcOutputHandler().print_output(ret,mainkey="")    
        return ret


    @staticmethod      
    @otcfunc(plugin_name=__name__,
             desc="Describe secrets",
             examples=[],
             args = [
                arg(    '--cluster-name',    dest='CLUSTER',     help='Name of the cluster'),
                arg(    '--namespace',    dest='NAMESPACE',     help='CES/CCE Namespace'),
                arg(    '--rc-name',    dest='RC_NAME',     help='CCE replication controller name')    
                          ]) 
    def delete_rc():
        if OtcConfig.CLUSTER:
            cce.convertClusterNameToId()                    
        url = "https://" + OtcConfig.DEFAULT_HOST + "/api/v1/namespaces/" + OtcConfig.NAMESPACE + "/replicationcontrollers/" + OtcConfig.RC_NAME
                         
        ret = utils_http.delete(url)
        cce.otcOutputHandler().print_output(ret,mainkey="")     
        return ret
                