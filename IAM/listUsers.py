import boto3
iam = boto3.client("iam")

def list_users(): 
    #response = iam.list_users() # method 1
    #print(response)
    for user in iam.list_users()["Users"]:  #improved method 2 
       print(user["UserName"])
    

list_users()
