import json
import boto3
def lambda_handler(event, context):
    # TODO implement
    s3 = boto3.client("s3")

    with open('demoimage.png' , "rb") as f:
        data = f.read()
        response = s3.put_object(
            ACL='public-read',
            Body=  data,
            Bucket='visionvirtualassistant',
            Key = "demoimage.png"
            )

    return {
        'statusCode': 200,
        'body': response
    }
