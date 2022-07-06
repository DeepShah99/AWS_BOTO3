import boto3
from pprint import pprint
db = boto3.client("dynamodb")

response = db.scan(
    TableName='Article',
    AttributesToGet=[
         'id', 'Name'
    ]
)
pprint(response)
   