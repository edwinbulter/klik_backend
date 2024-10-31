import boto3

# initiate DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Clicks')


def lambda_handler(event, context):

    try:
        user_id = event['user_id']
    except:
        user_id = 'Unknown User'

    # get the current item from dynamodb
    response = table.get_item(Key={'USER_ID': user_id})

    if 'Item' in response:
        # increment the counter for existing user
        counter = response['Item']['CLICK_COUNT']
    else:
        # set the counter to 1 for the new user
        counter = 0


    # sum of the counter values for all users
    total_counter = sum([x['CLICK_COUNT'] for x in table.scan()['Items']])
    res = {
        'user_counter': counter,
        'total_counter': total_counter
    }

    return res