source ./otcclient/tests/otcfunc.sh 

apitest otc ecs describe-security-groups
apitest otc ecs authorize-security-group-ingress --group-name mytest --vpc-name myvpc --protocol tcp --ethertype IPv4 
apitest otc ecs authorize-security-group-ingress --group-name mytest --vpc-name myvpc --protocol tcp --ethertype IPv4 --portmin 22 --portmax 25
apitest otc ecs authorize-security-group-egress --group-name mytest --vpc-name myvpc --protocol tcp --ethertype IPv4 --portmin 7000 --portmax 7001
apitest otc ecs authorize-security-group-ingress --group-name mytest --vpc-name myvpc  --protocol icmp --ethertype IPv4 --portmin 8 --portmax 0 --cidr 195.228.0.0/16
apitest otc ecs describe-security-groups
