source ./otcclient/tests/otcfunc.sh 

# using query 
# column queries 
apitest otc ecs describe-instances --query  "servers[].name"
apitest otc ecs describe-instances --query  "server.[name,key_name,status]"

apitest otc ecs describe-instances --query  "servers[?name == 'doc'].id"
apitest otc ecs describe-instances --query  "servers[?name == 'doc' || name == 'myserver'].id"

# list of all port of any security group 
apitest otc ecs describe-security-groups --query "security_groups[?contains( name,'doc')].security_group_rules[*].port_range_min"
