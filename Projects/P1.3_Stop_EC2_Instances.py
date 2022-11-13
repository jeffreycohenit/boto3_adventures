# Import boto3 library to write code for AWS
import boto3

# Creating the connection to AWS
ec2 = boto3.resource('ec2')

# Filters for instances that have the Environment: Dev tag
instances = ec2.instances.filter(
    Filters = [{'Name': 'instance-state-name', 'Values': ['running']},
        {'Name': 'tag:Environment', 'Values':['Dev']}])


# Only stop instances with the Environment: Dev tag
for instance in instances:
    try:
        instance.stop()
        print(f'{instance} are in the process of shutting')
    except:
        print(f'Error {instance} are not able to shut down')