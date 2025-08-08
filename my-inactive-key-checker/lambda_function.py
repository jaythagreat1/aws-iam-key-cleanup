import boto3
import os

iam = boto3.client('iam')
sns = boto3.client('sns')

def lambda_handler(event, context):
    inactive_keys = []
    users = iam.list_users()['Users']
    for user in users:
        username = user['UserName']
        access_keys = iam.list_access_keys(UserName=username)['AccessKeyMetadata']
        for key in access_keys:
            if key['Status'] == 'Inactive':
                inactive_keys.append(f"User: {username}, Access Key: {key['AccessKeyId']}")

    if inactive_keys:
        sns.publish(
            TopicArn=os.environ['SNS_TOPIC_ARN'],
            Message="Inactive Access Keys:\n" + "\n".join(inactive_keys),
            Subject="Inactive AWS Access Keys Detected"
        )
    return {"statusCode": 200, "body": "Check complete."}