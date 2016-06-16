echo list specific security group groupid, portmin field where name group name contains "default"  string 

FOR /F "tokens=* USEBACKQ" %%F IN (`..\bin\otc ecs describe-volumes --query "$..volumes[?(@.name =~ /.*kurt.*/i)].id` ) DO (
SET var=%%F
)
ECHO %var%

rem ..\bin\otc ecs attach-volume  --instance-ids f344b625-6f73-44f8-ad56-9fcb05a523c4 --volume-id 8c0de9a7-9f61-4613-a68a-21f456cb7298  --device /dev/sdb


