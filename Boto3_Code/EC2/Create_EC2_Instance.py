# Create an EC2 instance

import boto3

ec2 = boto3.resource('ec2')

instance = ec2.create_instances(ImageId='ami-09d3b3274b6c5d4aa', 
    InstanceType='t2.micro', 
    MaxCount=1, 
    MinCount=1
  )

print(instance)
