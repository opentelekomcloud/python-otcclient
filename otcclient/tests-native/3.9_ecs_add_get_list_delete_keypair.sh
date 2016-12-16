#!/bin/sh
source ./otcfunc.sh
source ./otcconf.sh


apitest nova --insecure keypair-add $KEY_NAME > MY_KEY.pem 2>/dev/null
apitest nova --insecure keypair-list 2>/dev/null
apitest nova --insecure keypair-show $KEY_NAME 2>/dev/null
apitest nova --insecure keypair-list 2>/dev/null
#apitest nova --insecure keypair-delete $KEY_NAME 2>/dev/null
apitest nova --insecure keypair-list 2>/dev/null
