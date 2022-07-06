import boto3 
from pprint import pprint

db = boto3.client("dynamodb")
response = db.batch_get_item(
    RequestItems={
        'Article': {
            'Keys': [
                {
                
                   
                        'id':{'N' : '1'},
                        'pub_date':{'S': '2022-06-12'}
                },
                 {
                
                   
                        'id':{'N' : '2'},
                        'pub_date':{'S': '2022-06-11'}
                }
                              
                
            ]

       

        }
    }
)

pprint(response['Responses'])