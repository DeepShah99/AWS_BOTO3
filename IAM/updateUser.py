import boto3

iam = boto3.client("iam")

def update_user_name(old_user_name, new_user_name):
    respone = iam.update_user(UserName = old_user_name, NewUserName = new_user_name)
    print(respone)

update_user_name("ThisUserisAmazingToo", "ThisUserisAmazing69")

