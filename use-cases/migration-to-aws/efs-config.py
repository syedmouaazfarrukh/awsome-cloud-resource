import boto3



# Create an EFS file system.
response = efs_client.create_file_system(
    CreationToken='my-unique-token',
    PerformanceMode='generalPurpose',
    ThroughputMode='bursting',
    Encrypted=True
)

# Get the file system ID.
file_system_id = response['FileSystemId']

# Create a mount target.
response = efs_client.create_mount_target(
    FileSystemId=file_system_id,
    SubnetId='subnet-12345678',
    SecurityGroupId='sg-12345678'
)

# Get the mount target IP address.
ip_address = response['NetworkInterfaceId']

# Mount the file system to an EC2 instance.
# sudo mount -t nfs ${ip_address}:/ /mnt/efs


if __name__ == "__main__":
    
    bucket_name = "mouaazodlmigrationtestbucket"
    region_name = "eu-north-1" #Stockholm
    keep_bucket = None
    s3_resource = boto3.resource("s3")
    
    
    file_path = ""
    object_name = "sample object"
    
    list_buckets(s3_resource)
    create_bucket(s3_resource, bucket_name)
    upload_to_s3(bucket_name, file_path, object_name)
    set_lifecycle_policy(bucket_name)
    
    delete_bucket(s3_resource, bucket_name)
    list_buckets(s3_resource)
