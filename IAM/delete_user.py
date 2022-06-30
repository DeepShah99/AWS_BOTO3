import boto3




def createUser(user):  
    iam = boto3.client("iam")  
    response = iam.delete_user(UserName = user)
    print(response)

createUser("ThisUserisAmazingToo")
