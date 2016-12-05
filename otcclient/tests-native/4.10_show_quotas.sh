#!/bin/sh

source otcfunc.sh
source otcconf.sh


apitest cinder --insecure quota-show a2fe26ba7c4a42a7bca1b481b416d9ad 2>/dev/null
