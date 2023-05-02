import json
import boto3


dynamodb = boto3.resource('dynamodb')
client = boto3.client('dynamodb')
tablename = dynamodb.Table('cdk-workshop-refreshtable32A794D7F5-1EL8GHMET2DJ0')

def lambda_handler(event, context):
    tablename.update_item(
        #Key={'ID': event['ID']},
        Key={'count': 'ID'},
        UpdateExpression='ADD Visits :incr',
        ExpressionAttributeValues={':incr': 1},
        ReturnValues="UPDATED_NEW"
       
    )

    data = client.get_item(
    TableName='cdk-workshop-refreshtable32A794D7F5-1EL8GHMET2DJ0',
    Key={
        'count': {
          'S': 'ID'

        }

    }
    )
    count = data['Item']
   #return count
    print(count)
    print(data)
   
    return count