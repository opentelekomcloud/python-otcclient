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

def test_ecs_list_instances():
    OtcConfig.OUTPUT_FORMAT = "noout"
    instances = json.loads(ecs.describe_instances())
    assert 'servers' in instances

# vim: sts=4 ts=4 sw=4 et:
