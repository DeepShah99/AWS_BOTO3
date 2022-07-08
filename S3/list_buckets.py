import boto3

'''s3 = boto3.client("s3") #client method

response = s3.list_buckets()

for bucket in response['Buckets']:
    print(bucket['Name']) '''


s3_resource = boto3.resource("s3")   #resource method

s3_bucket = s3_resource.Bucket('awsboto3udemy')

for obj in s3_bucket.objects.all():
    print(obj.key)


