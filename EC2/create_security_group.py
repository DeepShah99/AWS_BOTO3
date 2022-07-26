import boto3


ec2 = boto3.client('ec2')

response = ec2.create_security_group(
    Description='udemyDemoSg',
    GroupName='SGudemy'
)
print(response)