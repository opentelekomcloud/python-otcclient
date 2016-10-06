#!/bin/sh

source otcfunc.sh


apitest glance --insecure image-list 2>/dev/null

