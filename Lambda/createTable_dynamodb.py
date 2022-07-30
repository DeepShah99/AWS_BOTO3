import boto3
import json

def lambda_handler(event, context):
    # TODO implement

    db = boto3.client("dynamodb")
    response = db.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'year',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'title',
            'AttributeType': 'S'
        }
    ],
    TableName='Movies',
    KeySchema=[
        {
            'AttributeName': 'year',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'title',
            'KeyType': 'RANGE'
        }
    ],
    BillingMode= 'PAY_PER_REQUEST',
)

    return {
        'statusCode': 200,
        'body': json.dumps('table created successfully')
    }