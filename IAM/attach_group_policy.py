import boto3


def attachpolicy(groupname, policyARN):
    iam = boto3.client("iam")
    response = iam.attach_group_policy(GroupName= groupname,
    PolicyArn= policyARN)
    print(response)


attachpolicy("demo_group", "arn:aws:iam::476575494177:policy/demopolicy")

