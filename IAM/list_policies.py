import boto3

def listpolicy():
    iam = boto3.client("iam")
    #response = iam.list_policies() #method 1
    #print(response)

    #We should use pagination to get all the values
    count = 1
    for policy in iam.list_policies(Scope = "Local")["Policies"]: #method 2 
        print(count, policy["PolicyName"])
        count += 1

listpolicy()