import boto3
import json



def createpolicy():
    iam = boto3.client("iam")
    lambda_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal":{
                "Service":"lambda.amazonaws.com"
            },
            "Action":"sts:AssumeRole"
        }
    ]
}
    response = iam.create_role(RoleName = "lambdaDemoRole", AssumeRolePolicyDocument = json.dumps(lambda_policy))
    print(response)

createpolicy()


