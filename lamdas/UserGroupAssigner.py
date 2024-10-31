import boto3
from botocore.exceptions import BotoCoreError, ClientError


def lambda_handler(event, context):
    userName = event['userName']
    userPoolId = event['userPoolId']

    # Define the group name
    groupName = 'clickers'

    # Create AWS Cognito client
    client = boto3.client('cognito-idp')

    try:
        # Add the user to Cognito group
        response = client.admin_add_user_to_group(
            UserPoolId=userPoolId,
            Username=userName,
            GroupName=groupName
        )

        # Return success
        return event

    except ClientError as e:
        print(e)
        # Return error response
        return {
            'statusCode': 500,
            'body': {
                'message': 'Internal Server Error',
                'error_message': str(e)
            }
        }
