from OtcConfig import OtcConfig
import json
import prettytable 
from objectpath import Tree 
import os

class otcOutputHandler(object):
    """ generated source for class OtcConfig """
    instance_ = None

    #  for singleton instances
    def __init__(self):
        """ generated source for method __init__ """

    @classmethod
    def getInstance(cls):
        """ generated source for method getInstance """
        if cls.instance_ == None:
            cls.instance_ = otcOutputHandler()
        return cls.instance_

    
    @staticmethod
    def printLevel2(respjson,mainkey,subkey ):
        """ generated source for method getInstance """
        
        parsed = json.loads(respjson)
        if( str.lower( OtcConfig.OUTPUT_FORMAT) == "json" ) :            
            print json.dumps(parsed, indent=4, sort_keys=True) 
        elif( str.lower( OtcConfig.OUTPUT_FORMAT) == "table" ) :            
            x=prettytable.PrettyTable(subkey)
            mainId = parsed[mainkey]
            for item in mainId:
                vals = list()            
                for colkey in subkey:                    
                    if item[colkey]:
                        vals.append(item[colkey])
                    else:
                        vals.append(" ")
                x.add_row(vals)                
            print x.get_string()
        else :            
            print json
        pass
    

    @staticmethod
    def printLevel3(cls):
        """ generated source for method getInstance """

    @staticmethod
    def parseJsontoTopLevelList(cls):
        """ generated source for method getInstance """

    @staticmethod
    def handleQuery(result):
        """ generated source for method handleQuery """
        parsed = json.loads(result)
        objp = Tree(parsed)
        #print OtcConfig.QUERY
        path = objp.execute(OtcConfig.QUERY)
        if isinstance(path, (list, )):
            for object_ in path:
                print object_
        else:
            print path
        

    @staticmethod
    def parseJsontoTopLevelSimple(cls, json):
        """ generated source for method getInstance """
        # TODO: not implemented
        print json 
        raise "NOT Implemented Exception"
        

    
    x = prettytable.PrettyTable({"name","value"})
    x.align = 'l'
    x.sortby = None    

    @staticmethod
    def printJsonTableTransverse(val):
        """ generated source for method getInstance """        
        parsed = json.loads(val)
        
        otcOutputHandler.id_generator(parsed["server"],"")
        print otcOutputHandler.x.get_string()

    
    @staticmethod
    def id_generator(parsed,headkey):
          for k, v in parsed.items():
                if isinstance(v, dict):
                     otcOutputHandler.id_generator(v,headkey+"."+k)                     
                elif isinstance(v, list):
                    for v2 in v:
                        if isinstance(v2, dict):
                            otcOutputHandler.id_generator(v2,headkey+"."+k)
                        else :
                            pass                                     
                else :                    
                    if not v : 
                        v = ""                                          
                    otcOutputHandler.x.add_row(  [headkey+"."+k,v ] )

# f = os.open("detail.txt", os.O_RDONLY)
# t = os.read(f,10000)
# #otcOutputHandler.printJsonTableTransverse(t)
# OtcConfig.QUERY =  "$..server.addresses.7ce62bc1-b232-43f7-a880-97a4ac8371ce['*'].['version']"
# otcOutputHandler.handleQuery(t)
