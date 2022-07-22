import imp
import boto3
from pprint import pprint
rds = boto3.client("rds")
response = rds.create_db_instance(
    DBName='udemydemo',
    DBInstanceIdentifier='udemydemo',
    AllocatedStorage=20,
    DBInstanceClass='db.t2.micro',
    Engine='MySQL',
    MasterUsername='admin',
    MasterUserPassword='udemydemo',
    Port = 3306,
    PubliclyAccessible=True,
    StorageType = 'gp2'
    )
pprint(response)