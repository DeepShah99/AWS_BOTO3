import boto3

s3 = boto3.client("s3")

with open('/Users/deepshah/Desktop/AWS_BOTO3/S3/Amazon-DynamoDB.png' , "rb") as f:
    data = f.read()


response = s3.put_object(
    ACL='public-read',
    Body=  data,
    Bucket='awsboto3udemy',
    Key = "DB.png"
)
print(response)