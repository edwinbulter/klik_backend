import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Clicks')

def lambda_handler(event, context):

    try:
        user_id = event['user_id']
    except:
        user_id = 'Unknown User'

    response = table.get_item(Key={'USER_ID': user_id})

    if 'Item' in response:
        counter = response['Item']['CLICK_COUNT'] + 1
    else:
        counter = 1

    now = datetime.now().isoformat()

    table.put_item(
        Item={
            'USER_ID': user_id,
            'CLICK_COUNT': counter,
            'UPDATED_AT': now})

    # sum of the counter values for all users
    total_counter = sum([x['CLICK_COUNT'] for x in table.scan()['Items']])
    res = {
        'user_counter': counter,
        'total_counter': total_counter
    }

    return res
