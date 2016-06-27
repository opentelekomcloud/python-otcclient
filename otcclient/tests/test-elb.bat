rem call ..\bin\otc elb describe-load-balancers 
rem call ..\bin\otc elb describe-load-balancers --load-balancer-name nzs
rem call ..\bin\otc elb create-load-balancers --load-balancer-name nzs2 --vpc-name myvpc
rem call ..\bin\otc elb delete-load-balancers --load-balancer-name nzs2

rem call ..\bin\otc elb describe-listeners --load-balancer-name elb-myot
rem call ..\bin\otc elb describe-health-check --load-balancer-name elb-myot
rem call ..\bin\otc elb describe-listeners --load-balancer-name elb-myot
rem call ..\bin\otc elb describe-members --listener-name listener-c67k
call ..\bin\otc elb describe_quotas
