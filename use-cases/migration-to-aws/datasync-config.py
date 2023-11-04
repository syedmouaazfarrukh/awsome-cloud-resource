import boto3
import time
import logging


def transfer_data_to_s3_using_datasync(s3_client, datasync_client, bucket_name, on_premises_location, datasync_task_arn):
  """Transfers data to S3 using AWS DataSync.

  Args:
    s3_client: A Boto3 S3 client.
    datasync_client: A Boto3 DataSync client.
    bucket_name: The name of the S3 bucket to transfer the data to.
    on_premises_location: The location of the on-premises data.
    datasync_task_arn: The ARN of the DataSync task.

  Returns:
    None.
  """

  # Wait for the DataSync task to complete.
  while datasync_client.describe_task(TaskArn=datasync_task_arn)['Status'] != 'SUCCESS':
    time.sleep(60)

  logging.info('Data transferred to S3 successfully.')

if __name__ == '__main__':
    
    # Create S3 and Datasync clients.
    s3_client = boto3.client('s3')
    bucket_name = input('Enter the name of the S3 bucket to transfer the data to: ')
    on_premises_location = input('Enter the location of the on-premises data: ')
    
    datasync_client = boto3.client('datasync')
    response = datasync_client.list_tasks()
    datasync_task_arn = response['TaskList'][0]['TaskArn']

    if datasync_task_arn is None:
        
        # Create a DataSync task.
        response = datasync_client.create_task(
            SourceLocationArn=f'{on_premises_location}',
            DestinationLocationArn=f'arn:aws:s3:::{bucket_name}',
            TaskType='SYNC',
            ScheduleExpression='cron(0 0 * * ? *)',
            Name='op-to-aws-using-datasync'
        )

        # Get the DataSync task ARN.
        datasync_task_arn = response['TaskArn']

    else:
        
        # Get the DataSync task ARN.
        datasync_task_arn = response['TaskArn']    


    # Transfer the data to S3 using Snow
    transfer_data_to_s3_using_datasync(s3_client, datasync_client, bucket_name, on_premises_location, datasync_task_arn)



