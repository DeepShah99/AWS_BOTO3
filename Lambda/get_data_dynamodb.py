import boto3
import json

def lambda_handler(event, context):
    # TODO implement

    db = boto3.client("dynamodb")
    response = db.get_item(
    TableName='Movies',
    Key={
        'year': {
            
            'N': '2021'
           
        },
        'title': {
            'S' : 'Thor'
            
           
        }
    }
)

    return {
        'statusCode': 200,
        'body': response
    }
