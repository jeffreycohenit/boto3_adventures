# Adding boto3 to my script
import boto3

ec2_client = boto3.client("ec2")

ec2_resource = boto3.resource("ec2")

response = ec2_resource.create_instances(
    ImageId='ami-08c40ec9ead489470',
    InstanceType='t2.micro',
    MaxCount=6,
    MinCount=6)
    
print(response)