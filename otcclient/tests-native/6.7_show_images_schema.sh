#!/bin/sh

source otcfunc.sh


apitest glance --debug --insecure image-list #  2>/dev/null

