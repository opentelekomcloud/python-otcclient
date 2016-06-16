#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of OTC Tool released under MIT license.
# Copyright (C) 2016 T-systems Kurt Garloff, Zsolt Nagy
# NOT used currently (later could change the autentication and plugin tech base on this )

import os
from argparse import ArgumentParser, RawTextHelpFormatter
 
parser = ArgumentParser(prog='otc' ,  formatter_class=RawTextHelpFormatter ) #RawDescriptionHelpFormatter ,description=program_license


def params(*args, **kwargs):
    """Decorator for CLI args.

    Example:

    >>> @arg("name", help="Name of the new entity")
    ... def entity_create(args):
    ...     pass
    """
    def _decorator(func):
        add_arg(func, *args, **kwargs)
        return func
    return _decorator


def env(*args, **kwargs):
    """Returns the first environment variable set.

    If all are empty, defaults to '' or keyword arg `default`.
    """
    for arg in args:
        value = os.environ.get(arg)
        if value:
            return value
    return kwargs.get('default', '')


def add_arg(func, *args, **kwargs):
    """Bind CLI arguments to a shell.py `do_foo` function."""

    if not hasattr(func, 'arguments'):
        func.arguments = []

    # NOTE(sirp): avoid dups that can occur when the module is shared across
    # tests.
    if (args, kwargs) not in func.arguments:
        # Because of the semantics of decorator composition if we just append
        # to the options list positional options will appear to be backwards.
        func.arguments.insert(0, (args, kwargs))
        #print args
        


