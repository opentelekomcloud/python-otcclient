echo "test" > testfile.txt
otc s3 ls 
otc s3 mb functionaltest
otc s3 ls 
otc s3 rb functionaltest
otc s3 ls 
# TODO: this have to checked
otc s3api create-bucket --bucket mybucket