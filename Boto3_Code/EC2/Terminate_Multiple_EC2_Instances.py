# How to terminate multiple EC2 instances

import boto3

ec2 = boto3.client('ec2')

response = ec2.terminate_instances(
    InstanceIds=[
        'i-0f2c02fc3858eac44',
        'i-09e740f3c9516216c',
        'i-0d562c538bf25a1d9',
        'i-02fad88c0e8fc1e1e'
    ],
)

print(response)