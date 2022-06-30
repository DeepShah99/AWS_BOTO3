import boto3

def createaccesskey(username):
    iam = boto3.client("iam")
    response = iam.create_access_key(
    UserName= username
    )
    print(response)

createaccesskey("ThisUserisAmazing")


