# Describe a VPC 

import boto3

vpc = boto3.client('ec2')

response = vpc.describe_vpcs(
    VpcIds='vpc-052122721a9e57048',

)

print(response)