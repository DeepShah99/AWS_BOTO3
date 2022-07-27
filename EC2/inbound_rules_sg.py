import boto3

sg = boto3.client('ec2')

response = sg.authorize_security_group_ingress(
    GroupId = 'sg-09bd5bd23c319010e',
    IpPermissions=[
        {
            'FromPort': 22,
            'ToPort': 22,
            'IpProtocol': 'tcp',
            'IpRanges': [
                {
                    'CidrIp': '0.0.0.0/0'
                }
            ]
        }
    ]
)

print(response)