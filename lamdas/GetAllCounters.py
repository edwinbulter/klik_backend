import boto3
from datetime import datetime

# initiate DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Clicks')


def lambda_handler(event, context):

    # get the current item from dynamodb
    response = table.scan()

    # items contain all records
    items = response['Items']

    for item in items:
        # Check if 'UPDATED_AT' exists in item and is not None
        if 'UPDATED_AT' in item and item['UPDATED_AT']:
            # Convert 'UPDATED_AT' to datetime object
            datetime_obj = datetime.fromisoformat(item['UPDATED_AT'])

            # Format datetime object into string
            item['UPDATED_AT'] = datetime_obj.strftime("%Y-%m-%d %H:%M:%S")

    return items
