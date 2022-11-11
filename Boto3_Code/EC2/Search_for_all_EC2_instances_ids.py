# Search for all the EC2 instances ids

import boto3

ec2 = boto3.client('ec2')
instance = ec2.describe_instances()
data=instance["Reservations"][0-4]
data_instance=data["Instances"]

for i in range (len(data_instance)):
    print(f"instance id is {data_instance[i]['InstanceId']}")
