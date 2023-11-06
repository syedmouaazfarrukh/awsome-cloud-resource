import json
import boto3

def lambda_handler(event, context):
    
    # Parse the JSON payload from the webhook or API notification
    payload = json.loads(event['body'])

    # Extract the data uploaded by the user
    uploaded_data = payload['data']

    # Initialize an S3 client
    s3_client = boto3.client('s3')

    # Upload the data to an S3 bucket
    s3_client.put_object(Body=uploaded_data, Bucket='my-s3-bucket', Key='data.txt')

    # Send a response to the on-premises application
    response = {
        'status': 'success',
        'message': 'Data uploaded successfully to S3'
    }

    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
    
    
if __name__ == "__main__":
        
    lambda_handler(event, context)

    # -------- The function is being triggered by a webhook or API notification, so the event will be a JSON object containing the payload of the notification

    #     {
    # "body": "{\"data\": \"This is the uploaded data\"}",
    # "headers": {
    #     "Content-Type": "application/json"
    # },
    # "httpMethod": "POST",
    # "isBase64Encoded": false,
    # "path": "/webhook",
    # "resource": "/webhook",
    # "stage": "prod"
    # }
