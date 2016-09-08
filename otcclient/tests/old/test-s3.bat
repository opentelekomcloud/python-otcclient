echo "test" > testfile.txt
call ..\bin\otc.bat s3 mb functiontest
call ..\bin\otc.bat s3 cp testfile.txt s3://otcclient/testfile.txt
call ..\bin\otc.bat s3 cp s3://otcclient/testfile.txt testfile2.txt 
call ..\bin\otc.bat s3 get_bucket_versioning otcclient
