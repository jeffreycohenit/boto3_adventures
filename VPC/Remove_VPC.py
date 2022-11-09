# Deleting a VPC 

import boto3

vpc = boto3.client('ec2')

response = vpc.delete_vpc(
    VpcId='vpc-0adf48b8dc6e65239',
)

print(response)