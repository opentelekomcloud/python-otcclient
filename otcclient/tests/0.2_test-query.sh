# using query 
# column queries 
otc ecs describe-instances --query  "servers[].name"
otc ecs describe-instances --query  "server.[name,key_name,status]"

otc ecs describe-instances --query  "servers[?name == 'doc'].id"
otc ecs describe-instances --query  "servers[?name == 'doc' || name == 'myserver'].id"

# list of all port of any security group 
otc ecs describe-security-groups --query "security_groups[?contains( name,'doc')].security_group_rules[*].port_range_min"
