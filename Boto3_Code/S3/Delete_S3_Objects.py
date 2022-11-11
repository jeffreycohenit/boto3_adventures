# Deleting objects in a bucket

import boto3

s3 = boto3.client('s3')

response = s3.delete_object(
    Bucket = 'jeffreylearningboto3',
    Key = 'LUIT.png')

print (response)