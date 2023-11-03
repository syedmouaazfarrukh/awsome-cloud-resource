import boto3
import logger



def list_buckets(s3_resource):
    """
    Use the AWS SDK for Python (Boto3) to create an Amazon Simple Storage Service
    (Amazon S3) resource and list the buckets in your account.
    This example uses the default settings specified in your shared credentials
    and config files.
    """
    client = boto3.client('s3')
    # s3_resource = boto3.resource("s3")
    
    print("Hello, Amazon S3! Let's list your buckets:")
    print("Buckets:\n\t", *[b.name for b in s3_resource.buckets.all()], sep="\n\t")
    
    for bucket in s3_resource.buckets.all():
        print(f"\t{bucket.name}")

def create_bucket(s3_resource, bucket_name):
    
    list_buckets(s3_resource)
    
    try:
        print("\nCreating new bucket:", bucket_name)
        bucket = s3_resource.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                "LocationConstraint": s3_resource.meta.client.meta.region_name
            },
        )
    except Exception as e:
        print(
            f"Couldn't create a bucket for the demo. Here's why: "
            f"{e.response['Error']['Message']}"
        )
        raise

    bucket.wait_until_exists()
    print(f"\nBucket: {bucket_name} created")
    
def delete_bucket(s3_resource, bucket_name):
    
    bucket = boto3.resource("s3")
    
    try:
        print("\nDeleting bucket:", bucket_name)
        bucket.delete()
        
    except Exception as e:
        print(
            f"Couldn't delete {bucket_name} bucket. Here's why: "
            f"{e.response['Error']['Message']}"
        )
        raise

    bucket.wait_until_exists()


    # if keep_bucket  == None:
    #     print("\nDeleting bucket:", bucket.name)
    #     bucket.delete()

    #     bucket.wait_until_not_exists()
    #     list_buckets(s3_resource)
        
    # else:
    #     print("\nKeeping bucket:", bucket.name)

def upload_to_s3(bucket_name, file_path, object_name):
    s3_client = boto3.client('s3')
    s3_client.upload_file(file_path, bucket_name, object_name)

def set_lifecycle_policy(bucket_name):
    s3_client = boto3.client('s3')
    lifecycle_config = {
        'Rules': [
            {
                'ID': 'Move old files to IA storage',
                'Prefix': '',
                'Status': 'Enabled',
                'Transitions': [
                    {
                        'Days': 30,
                        'StorageClass': 'STANDARD_IA'
                    }
                ],
                'NoncurrentVersionTransitions': [
                    {
                        'NoncurrentDays': 30,
                        'StorageClass': 'STANDARD_IA'
                    }
                ],
                'Expiration': {
                    'Days': 365
                }
            }
        ]
    }
    s3_client.put_bucket_lifecycle_configuration(Bucket=bucket_name, LifecycleConfiguration=lifecycle_config)




if __name__ == "__main__":
    
    bucket_name = "mouaazodlmigrationtestbucket"
    region_name = "eu-north-1" #Stockholm
    keep_bucket = None
    s3_resource = boto3.resource("s3")
    
    # bucket_name = "mouaazodlmigrationtestbucket"
    # file_path = "path_to_file"  # Replace with your file path
    # object_name = "your_file_name"  # Replace with the name you want to give to the file
    
    # upload_to_s3(bucket_name, file_path, object_name)
    # set_lifecycle_policy(bucket_name)
    
    
    
    list_buckets(s3_resource)
    delete_bucket(s3_resource, bucket_name)
    # create_and_delete_my_bucket(s3_resource, bucket_name, keep_bucket)
    list_buckets(s3_resource)
    
    
