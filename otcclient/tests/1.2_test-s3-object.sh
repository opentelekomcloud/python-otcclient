echo "test" > testfile.txt
otc s3 ls 
otc s3 mb functionaltest
otc s3 ls 
otc s3 cp testfile.txt s3://functionaltest/testfile.txt
otc s3 ls s3://functiontest/ 
otc s3 cp s3://functionaltest/testfile.txt testfile2.txt 
otc s3 get_bucket_versioning functionaltest
otc s3 ls 

