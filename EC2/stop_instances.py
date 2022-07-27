import boto3
ec2 = boto3.client('ec2')

response = ec2.stop_instances(
    InstanceIds=[
        'i-0ab85e5555ec32e76'
    ]
)
print(response)