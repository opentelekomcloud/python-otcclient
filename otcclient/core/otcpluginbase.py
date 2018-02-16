#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of OTC Tool released under MIT license.
# Copyright (C) 2016 T-systems Kurt Garloff, Zsolt Nagy

from otcclient.core.OtcConfig import OtcConfig
import sys


if sys.version_info >= (3, 0):
    from otcclient.core.otcpluginbase_py3 import otcpluginbase
else:
    from otcclient.core.otcpluginbase_py2 import otcpluginbase


def converter(astr):
    return "https://" + OtcConfig.DEFAULT_HOST
