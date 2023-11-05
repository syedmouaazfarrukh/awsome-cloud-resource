import boto3

# Create an EFS client.
efs_client = boto3.client('efs')

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
