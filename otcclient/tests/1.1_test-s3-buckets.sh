source ./otcclient/tests/otcfunc.sh 

echo "test" > testfile.txt
apitest otc s3 ls 
apitest otc s3 mb functionaltest
apitest otc s3 ls 
apitest otc s3 rb functionaltest
apitest otc s3 ls 
# TODO: this have to checked
apitest otc s3api create-bucket --bucket mybucket