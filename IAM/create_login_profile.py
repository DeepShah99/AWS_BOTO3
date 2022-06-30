import boto3

def createloginprofile(username):
    iam = boto3.client("iam")
    response = iam.create_login_profile(
    UserName= username,
    Password='@Haha1234567',
    PasswordResetRequired= False
    )
    print(response)

createloginprofile("ThisUserisAmazing")