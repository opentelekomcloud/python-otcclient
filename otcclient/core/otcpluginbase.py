#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of OTC Tool released under MIT license.
# Copyright (C) 2016 T-systems Kurt Garloff, Zsolt Nagy

from abc import abstractmethod, ABCMeta

class otcpluginbase:    
    def __init__(self,*args,**kwargs):
        pass
        
    __metaclass__ = ABCMeta

    @abstractmethod
    def otctype(self):
        """
        """   