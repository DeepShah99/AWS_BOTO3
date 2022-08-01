import json
from pyclbr import Function
import boto3
from pprint import pprint
lambda_client = boto3.client('lambda')

response = lambda_client.get_function(
    FunctionName='Lambda_Text_To_Speech'
)

pprint(response)