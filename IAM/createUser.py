import boto3
iam = boto3.client("iam")

response = iam.create_user(UserName = "ThisUserisAmazing")   #method 1
print(response)


def createUser(user):       #method 2
    response_two = iam.create_user(UserName = user)
    print(response_two)

createUser("ThisUserisAmazingToo")

