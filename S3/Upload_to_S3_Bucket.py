# Upload files to a S3 Bucket

import boto3

s3 = boto3.client('s3')

response = s3.upload_file(
    Filename='/home/ec2-user/environment/boto3_adventures/s3/test.txt',
    Bucket='jeffreylearningboto3'
    Key='/home/ec2-user/environment/boto3_adventures/s3/test.txtt'
)

print (response)