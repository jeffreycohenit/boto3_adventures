# Creating AWS S3 Bucket using Boto3

import boto3
s3 = boto3.resource('s3')
response = s3.create_bucket(Bucket ='jeffreylearningboto3')

print (response)