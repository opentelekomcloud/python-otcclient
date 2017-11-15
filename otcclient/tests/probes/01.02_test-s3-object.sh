#!/bin/bash

echo "test" > testfile.txt
apitest otc s3 ls 
apitest otc s3 mb functionaltest
apitest otc s3 ls 
apitest otc s3 cp testfile.txt s3://functionaltest/testfile.txt
apitest otc s3 ls s3://functiontest/ 
apitest otc s3 cp s3://functionaltest/testfile.txt testfile2.txt 
apitest otc s3 get_bucket_versioning functionaltest
apitest otc s3 ls 
rm testfile.txt

