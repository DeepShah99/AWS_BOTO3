import boto3


ec2 = boto3.client('ec2')

response = ec2.create_key_pair(KeyName = 'udemyDemoKeyPair')

file = open('/Users/deepshah/Desktop/AWS_BOTO3/EC2/mydemokeypair.pem', 'w')
file.write(response['KeyMaterial'])
file.close()
