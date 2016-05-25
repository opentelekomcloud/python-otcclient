echo list specific security group groupid, portmin field where name group name contains "default"  string 
..\bin\otc ecs describe-security-groups --output json --query "$..security_groups[?(@.name =~ /.*default/i)].security_group_rules[*].['security_group_id','port_range_min']"
