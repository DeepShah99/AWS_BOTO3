import json
import boto3
def lambda_handler(event, context):
    # TODO implement
    s3 = boto3.client("s3") #client method
    s3buckets = []

    response = s3.list_buckets()

    for bucket in response['Buckets']:
        s3buckets.append(bucket['Name'])
        
    return {
        'statusCode': 200,
        'body': s3buckets
    }
