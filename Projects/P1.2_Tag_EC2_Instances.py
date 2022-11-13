# Import boto3 library to write code for AWS
import boto3

# Creating the connection to AWS
ec2 = boto3.resource('ec2')

# Adding tags to my instances
# Editable
response = ec2.create_tags(
    Resources=[
        'i-03b063c0208941e2b',
        'i-00751029141316134',
        'i-01278df9bebf02769',
    ],
    Tags=[
        {
            'Key': 'Environment',
            'Value': 'Dev'
        },
    ]
)

print("EC2 instances updated")