#!/bin/sh
source ./otcfunc.sh

KEY_NAME=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 10 | head -n 1)_KEY_NAME


apitest nova --insecure keypair-add $KEY_NAME > MY_KEY.pem 2>/dev/null
apitest nova --insecure keypair-list 2>/dev/null
apitest nova --insecure keypair-show $KEY_NAME 2>/dev/null
apitest nova --insecure keypair-list 2>/dev/null
apitest nova --insecure keypair-delete $KEY_NAME 2>/dev/null
apitest nova --insecure keypair-list 2>/dev/null
