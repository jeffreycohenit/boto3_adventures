import boto3

ec2 = boto3.client('ec2')

response = ec2.create_volume(
    AvailabilityZone='us-east-1a',
    Encrypted=True,
    Size=12,
    SnapshotId='snap-08d231b8d76db5284',
    VolumeType='gp2',
)

print(response)