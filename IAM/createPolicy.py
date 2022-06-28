import boto3
import json



def createpolicy():
    iam = boto3.client("iam")
    admin_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "*",
            "Resource": "*"
        }
    ]
}
    response = iam.create_policy(PolicyName = "demopolicy", PolicyDocument = json.dumps(admin_policy))
    print(response)

createpolicy()


