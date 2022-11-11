# Upload files to a S3 Bucket

import boto3

s3 = boto3.client('s3')

response=s3.put_object(
    Body='test.jpg',
    Bucket='jeffreylearningboto3',
    Key='test.jpg')

print (response)