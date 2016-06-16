echo this example demonstrate the loop, fetch instance ids and do additional action with loop 

FOR /F "tokens=*" %%G IN ('..\bin\otc ecs describe-instances --query ".id" ') DO ..\bin\otc ecs describe-instances %%G --output json >> all

FOR /F "tokens=*" %%G IN ('otc ecs describe-instances --query ".id" ') DO otc ecs describe-instances %%G --query ".['name','key_name','status']"
