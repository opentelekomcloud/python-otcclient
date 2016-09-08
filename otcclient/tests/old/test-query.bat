..\bin\otc ecs describe-instances --query  "servers[].name"
..\bin\otc ecs describe-instances --query  "servers[?name == 'hadoop'].id"
..\bin\otc ecs describe-instances --query  "servers[?name == 'hadoop' || name == 'hadoopdocker'].id"

rem list of all port of specific security groupusing query 
..\bin\otc ecs describe-security-groups --query "security_groups[?contains( name,'testserver')].security_group_rules[*].port_range_min"
rem test command chain 
FOR /F "tokens=*" %%G IN ('..\bin\otc ecs describe-instances --query "servers[].name" ') DO ..\bin\otc ecs describe-instances --instance-name %%G --query "server.[name,key_name,status]"