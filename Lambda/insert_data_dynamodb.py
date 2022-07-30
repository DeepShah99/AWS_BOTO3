import boto3
import json

def lambda_handler(event, context):
    # TODO implement

    db = boto3.client("dynamodb")
    response = db.put_item(
        TableName='Movies',
        Item= {
        "year" : {
            "N": "2021"
        },
        "title" : {
            "S": "Thor"
         },
        
        }
    
    
)

    return {
        'statusCode': 200,
        'body': json.dumps('data created successfully')
    }
