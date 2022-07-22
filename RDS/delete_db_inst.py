
import boto3

rds = boto3.client("rds")

response = rds.delete_db_instance(
    DBInstanceIdentifier='rdsdemoudemy',
    SkipFinalSnapshot=True,
    DeleteAutomatedBackups=True
)
print(response)