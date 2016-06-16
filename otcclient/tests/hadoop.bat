set VM_NAME=hadoop
FOR /F "tokens=*" %%G IN ('otc ecs describe-instances --query ".[?(@.name =~ /.*%VM_NAME%.*/i)].id" ') DO (
for /f "delims=" %%i in ('otc ecs describe-instances %%G --query ".addr"') do set INTERNAL_IP=%%i
)

for /f "delims=" %%i in ('otc ecs describe-addresses --query ".[?(@.private_ip_address =~ /.*%INTERNAL_IP%.*/i)].public_ip_address"') do set EXTERNAL_IP=%%i
echo %VM_NAME% %INTERNAL_IP%, %EXTERNAL_IP%



