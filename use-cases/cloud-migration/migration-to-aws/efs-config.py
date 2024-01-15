import boto3

if __name__ == "__main__":
    
    bucket_name = "mouaazodlmigrationtestbucket"
    region_name = "eu-north-1" #Stockholm
    efs_client = boto3.client('efs')

    # Get the file system ID.
    file_system_id = response['FileSystemId']
    if file_system_id is None:
        # Create an EFS file system.
        response = efs_client.create_file_system(
            CreationToken='mouaazodlmigration-test',
            PerformanceMode='generalPurpose',
            ThroughputMode='bursting',
            Encrypted=True
        )
        
        file_system_id = response['FileSystemId']
        # Get the mount target IP address.
        ip_address = response['NetworkInterfaceId'] 

        if ip_address is None:
            # Create a mount target.
            response = efs_client.create_mount_target(
                FileSystemId=file_system_id,
                SubnetId='subnet-12345678',
                SecurityGroupId='sg-12345678'
            )
            
            ip_address = response['NetworkInterfaceId'] 

            
# Run the following command on CLI.
# sudo mount -t nfs ${ip_address}:/ /mnt/efs
    
