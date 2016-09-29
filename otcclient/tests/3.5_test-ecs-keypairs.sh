source ./otcclient/tests/otcfunc.sh 

apitest otc ecs describe-key-pairs
apitest otc ecs create-key-pair --key-name aaaaa --public-key "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQDx8nkQv/zgGgB4rMYmIf+6A4l6Rr+o/6lHBQdW5aYd44bd8JttDCE/F/pNRr0lRE+PiqSPO8nDPHw0010JeMH9gYgnnFlyY3/OcJ02RhIPyyxYpv9FhY+2YiUkpwFOcLImyrxEsYXpD/0d3ac30bNH6Sw9JD9UZHYcpSxsIbECHw== Generated-by-Nova"
apitest otc ecs describe-key-pairs
apitest otc ecs create-key-pair --key-name aaaaa 
apitest otc ecs describe-key-pairs
apitest otc ecs delete-key-pair --key-name aaaaa