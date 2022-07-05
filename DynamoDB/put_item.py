from tkinter import N
import boto3

def putitem(id, pub_date, Name):
    db = boto3.client("dynamodb")
    response = db.put_item(
    TableName='Article',
        Item= {
        "id" : {
            "N": id
        },
        "pub_date" : {
            "S": pub_date
         },
        "Name" : {
            "S": Name
        }
        }
    )
    print(response)

putitem("5", "2034-01-12", "John")
