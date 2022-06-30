import boto3

def addUsertoGroup(groupname, username):
    iam = boto3.client("iam")
    response = iam.add_user_to_group(
    GroupName= groupname,
    UserName= username
    )
    print(response)


addUsertoGroup("demo_group", "ThisUserisAmazing")