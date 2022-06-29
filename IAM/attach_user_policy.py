import boto3


def attachpolicy(username, policyARN):
    iam = boto3.client("iam")
    response = iam.attach_user_policy(UserName= username,
    PolicyArn= policyARN)
    print(response)


attachpolicy("ThisUserisAmazing", "arn:aws:iam::476575494177:policy/demopolicy")

