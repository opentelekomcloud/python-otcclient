#!/bin/bash

echo "test" > testfile.txt
apitest otc s3 ls 
apitest otc s3 mb functionaltest
apitest otc s3 ls 
apitest otc s3 rb functionaltest
apitest otc s3 ls
rm testfile.txt
