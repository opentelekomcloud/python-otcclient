import json

from otcclient.core.userconfigaction import userconfigaction
from otcclient.core.configloader import configloader
from otcclient.core.OtcConfig import OtcConfig
from otcclient.plugins.ecs import ecs

def test_ecs_get_token():
    OtcConfig.OUTPUT_FORMAT = "noout"
    configloader.readUserValues()
    ecs.getIamToken()
    assert OtcConfig.TOKEN != ""

def test_ecs_describe_instances():
    OtcConfig.OUTPUT_FORMAT = "noout"
    res = json.loads(ecs.describe_instances())
    assert 'servers' in res

def test_ecs_describe_vpcs():
    OtcConfig.OUTPUT_FORMAT = "noout"
    res = json.loads(ecs.describe_vpcs())
    VPCS = res
    assert 'vpcs' in res

def test_ecs_describe_addresses():
    OtcConfig.OUTPUT_FORMAT = "noout"
    res = json.loads(ecs.describe_addresses())
    assert 'publicips' in res

def test_ecs_describe_bandwiths():
    OtcConfig.OUTPUT_FORMAT = "noout"
    res = json.loads(ecs.describe_bandwiths())
    assert 'bandwidths' in res

def test_ecs_describe_security_groups():
    OtcConfig.OUTPUT_FORMAT = "noout"
    res = json.loads(ecs.describe_security_groups())
    assert 'security_groups' in res

def test_ecs_describe_subnets():
    OtcConfig.OUTPUT_FORMAT = "noout"
    res = json.loads(ecs.describe_subnets())
    assert 'subnets' in res

def test_ecs_describe_images():
    OtcConfig.OUTPUT_FORMAT = "noout"
    res = json.loads(ecs.describe_images())
    assert 'images' in res

def test_ecs_describe_flavors():
    OtcConfig.OUTPUT_FORMAT = "noout"
    res = json.loads(ecs.describe_flavors())
    assert 'flavors' in res

def test_ecs_describe_key_pairs():
    OtcConfig.OUTPUT_FORMAT = "noout"
    res = json.loads(ecs.describe_key_pairs())
    assert 'keypairs' in res

def test_ecs_describe_volumes():
    OtcConfig.OUTPUT_FORMAT = "noout"
    res = json.loads(ecs.describe_volumes())
    assert 'volumes' in res

def test_ecs_describe_quotas():
    OtcConfig.OUTPUT_FORMAT = "noout"
    res = json.loads(ecs.describe_quotas())
    assert 'absolute' in res

def test_ecs_describe_snapshots():    
    OtcConfig.OUTPUT_FORMAT = "noout"
    res = json.loads(ecs.describe_snapshots())
    assert 'backups' in res

def test_ecs_describe_private_addresses():
    OtcConfig.OUTPUT_FORMAT = "noout"
    vpcs = [vpc for vpc in json.loads(ecs.describe_vpcs())['vpcs']]
    subnets = [sn for sn in json.loads(ecs.describe_subnets())['subnets']]
    for sn in subnets[0:3]:
        vpc = [v for v in vpcs if sn['vpc_id'] == v['id']]
        if len(vpc) == 0:
            continue
        OtcConfig.SUBNETNAME = sn['name']
        OtcConfig.VPCNAME = vpc[0]['name']
        res = json.loads(ecs.describe_private_addresses())
        assert 'privateips' in res

def test_ecs_describe_network_interfaces(): 
    OtcConfig.OUTPUT_FORMAT = "noout"
    instances = [i for i in json.loads(ecs.describe_instances())['servers']]
    for i in instances[0:3]:
        OtcConfig.INSTANCE_NAME = i['name']
        res = json.loads(ecs.describe_network_interfaces())
        assert 'interfaceAttachments' in res

# vim: sts=4 ts=4 sw=4 et:
