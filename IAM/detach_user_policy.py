import boto3


def detachpolicy(username, policyARN):
    iam = boto3.client("iam")
    response = iam.detach_user_policy(UserName= username,
    PolicyArn= policyARN)
    print(response)


detachpolicy("ThisUserisAmazing", "arn:aws:iam::476575494177:policy/demopolicy")

