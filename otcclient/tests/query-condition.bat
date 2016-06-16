@rem http://objectpath.org/reference.html
..\bin\otc ecs describe-instances --query  "$..*[name in [hadoop,hadoopdocker]].id" 
--query "$..*[name is hadoop].id"
--query  "$..*[status is active]" 
"$..*[name is hadoop].id"
$.servers.status
