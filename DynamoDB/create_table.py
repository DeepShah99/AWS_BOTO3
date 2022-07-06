import boto3
db = boto3.client("dynamodb")
response = db.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'student_id',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'student_name',
            'AttributeType': 'S'
        }
    ],
    TableName='student',
    KeySchema=[
        {
            'AttributeName': 'student_id',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'student_name',
            'KeyType': 'RANGE'
        }
    ],
    BillingMode= 'PAY_PER_REQUEST',
)