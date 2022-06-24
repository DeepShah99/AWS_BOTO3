import boto3
iam = boto3.client("iam")

def list_users():
    response = iam.list_users()
    print(response)


list_users()
