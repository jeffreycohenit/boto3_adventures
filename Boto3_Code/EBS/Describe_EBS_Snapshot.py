import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_snapshots(SnapshotIds=[
        'snap-0c0b30d420db08ab8',])

print(response)