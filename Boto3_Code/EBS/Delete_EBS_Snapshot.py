import boto3

ec2 = boto3.client('ec2')

response = ec2.delete_snapshot(SnapshotId='snap-08d231b8d76db5284')

print(response)