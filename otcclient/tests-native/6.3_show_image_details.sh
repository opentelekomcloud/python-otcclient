#!/bin/sh

source otcfunc.sh


apitest glance --insecure image-show Enterprise_OracleLinux_7.2_latest  2>/dev/null
