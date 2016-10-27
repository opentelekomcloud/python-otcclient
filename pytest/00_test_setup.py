from otcclient.core.userconfigaction import userconfigaction
from otcclient.core.configloader import configloader
from otcclient.core.OtcConfig import OtcConfig
from otcclient.plugins.ecs import ecs

def test_uservalues():
    userconfig_org = OtcConfig.OTC_USER_FILE
    OtcConfig.OTC_USER_FILE = "otc_config_mock"
    configloader.readUserValues()
    assert OtcConfig.ak == 'mock_access_key_id'
    assert OtcConfig.sk == 'mock_secret_access_key'
    assert OtcConfig.USERNAME == 'MOCK OTC USER NAME'
    assert OtcConfig.PASSWORD == 'MOCK_API_KEY'

    OtcConfig.OTC_USER_FILE = userconfig_org
    configloader.readUserValues()

# vim: sts=4 ts=4 sw=4 et:
