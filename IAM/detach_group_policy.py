import boto3


def detachpolicy(groupname, policyARN):
    iam = boto3.client("iam")
    response = iam.detach_group_policy(GroupName= groupname,
    PolicyArn= policyARN)
    print(response)


detachpolicy("demo_group", "arn:aws:iam::476575494177:policy/demopolicy")

