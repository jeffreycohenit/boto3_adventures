# Import boto3 library to write code for AWS
import boto3

# Creating the connection to AWS
ec2 = boto3.resource('ec2')

# Creating new EC2 instance
# Editable
instances = ec2.create_instances(
    ImageId='ami-08c40ec9ead489470',
    MinCount=3,
    MaxCount=3,
    InstanceType='t2.micro',
    KeyName='new-aws-key',
)

print("EC2 Launched Successfully")