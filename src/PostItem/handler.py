import json
import boto3
import os
def handler(event, context):
    # Log the event argument for debugging and for use in local development.
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['ITEMTABLE_TABLE_NAME']) 
    item = {
        'id': event['pathParameters']['id'],
        'name': event['queryStringParameters']['name'],
        'price': event['queryStringParameters']['price'],
        'category': event['queryStringParameters']['category']

    }

    table.put_item(Item=item)
    return {
        'statusCode' : 200,
        'body': json.dumps('Item added to table')
    }