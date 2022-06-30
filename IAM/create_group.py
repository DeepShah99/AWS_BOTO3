import boto3

def creategroup(groupname):
    iam = boto3.client("iam")
    response = iam.create_group(GroupName = groupname)
    print(response)

creategroup("demo_group")