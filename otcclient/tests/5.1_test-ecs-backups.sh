source ./otcclient/tests/otcfunc.sh 

apitest otc ecs describe-snapshots
apitest otc ecs create-snapshot  --volume-id f10d5768-8983-48eb-ac2b-1b1850766d9b
apitest otc ecs describe-snapshots
apitest otc ecs delete-snapshot  --snapshot-id 7b5dfe84-e73f-4800-83ba-9af8871f3d89
apitest otc ecs describe-snapshots
apitest otc ecs restore-snapshot  --snapshot-id 7b5dfe84-e73f-4800-83ba-9af8871f3d89 --volume-id f10d5768-8983-48eb-ac2b-1b1850766d9b
apitest otc ecs describe-snapshots


