import boto3 


db = boto3.client("dynamodb")
response = db.get_item(
    TableName='Article',
    Key={
        'id': {
            
            'N': '3'
           
        },
        'pub_date': {
            'S' : '2022-01-02'
            
           
        }
    }
)
print(response['Item'])
