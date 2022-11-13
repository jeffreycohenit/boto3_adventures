# Adding boto3 to my script
import boto3

ec2_client = boto3.client("ec2")

response = ec2_client.stop_instances(InstanceIds="")
print(response)