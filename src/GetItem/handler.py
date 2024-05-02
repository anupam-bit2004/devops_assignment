import json
import os
import boto3
def handler(event, context):
    # Log the event argument for debugging and for use in local development.
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['ITEMTABLE_TABLE_NAME']) 
    id = event['pathParameters']['id']
    item = table.get_item(Key={'id': id})

    if 'Item' in item:
        return {
            'statusCode':200,
            'body': json.dumps(item['Item'])
        }
    else:
        return {
            'statusCode': 404
        }
