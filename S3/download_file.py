import boto3

s3_resource = boto3.resource("s3")

s3_object = s3_resource.Object('awsboto3udemy', 'DB.png')

s3_object.download_file('DBDownloaded.png')
