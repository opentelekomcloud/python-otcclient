SERVER_NAME=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 10 | head -n 1)_TEST_SERVER
KEY_NAME=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 10 | head -n 1)_KEY_NAME
TEST_SEC_GROUP=TEST_SEC_GROUP_$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 10 | head -n 1)
RENAME_SERVER=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 10 | head -n 1)_TEST_SERVER
####################################################
NETWORK_NAME=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 10 | head -n 1)_NETWORK
NETWORK_NAME_NEW=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 10 | head -n 1)_NETWORK

PORT_NAME=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 10 | head -n 1)_PORT
PORT_NAME_NEW=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 10 | head -n 1)_PORT

SUBNET_NAME=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 10 | head -n 1)_SUBNET
SUBNET_NAME_NEW=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 10 | head -n 1)_SUBNET
SECURITY_GROUP_NAME=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 10 | head -n 1)_SECNAME

ROUTER_NAME=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 10 | head -n 1)_ROUTER
ROUTER_INTERFACE_NAME=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 10 | head -n 1)_INTERFACE

VOLUME_NAME=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 10 | head -n 1)_VOLUME
VOLUME_NAME_NEW=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 10 | head -n 1)_VOLUME

SNAPSHOT_NAME=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 10 | head -n 1)_SNAPSHOT

IMAGE_NAME=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 10 | head -n 1)_IMAGE
IMAGE_NAME_NEW=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 10 | head -n 1)_IMAGE
####################################################
check_testserver(){
if [ "$TEST_SERVER" = ""  ]; then
        echo "Test Server does not exists.. creating.."
        exit
fi
}
