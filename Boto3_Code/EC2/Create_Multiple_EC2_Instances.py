# Create multiple EC2 instances 

import boto3

ec2 = boto3.resource('ec2')

instance = ec2.create_instances(ImageId='ami-09d3b3274b6c5d4aa', 
    InstanceType='t2.micro', 
    MaxCount=3, 
    MinCount=3
  )

print(instance)