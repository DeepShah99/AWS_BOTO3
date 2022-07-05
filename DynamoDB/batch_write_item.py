import boto3
db = boto3.client("dynamodb")
response = db.batch_write_item(
    RequestItems={
        'Article': [
            {
                'PutRequest': {
                    'Item': {
                        'id': {
                            
                            'N': '10'
                        },
                        "pub_date" : {
                            "S": "2023-01-12"
                        },
                        "Name" : {
                            "S": "Tom"
                        }
                        
                    }
                }
            },
            {
                'PutRequest': {
                    'Item': {
                        'id': {
                            
                            'N': '4'
                        },
                        "pub_date" : {
                            "S": "2023-01-12"
                        },
                        "Name" : {
                            "S": "Tom"
                        }
                        
                    }
                }
            }
        ]
    }
)
print(response)
