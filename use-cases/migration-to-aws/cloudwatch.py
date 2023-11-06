import boto3

def create_cloudwatch_alarms(application_name):
    # Create a CloudWatch client
    cloudwatch_client = boto3.client('cloudwatch')

    # Create an alarm for the EFS mount point utilization
    efs_mount_point_utilization_alarm = cloudwatch_client.put_metric_alarm(
        AlarmName=f'{application_name}-EFS-Mount-Point-Utilization-Alarm',
        Namespace='AWS/EFS',
        MetricName='PercentIdle',
        Statistic='Average',
        Period=60,
        EvaluationPeriods=2,
        Threshold=80.0,
        ComparisonOperator='LessThanThreshold',
        AlarmDescription='EFS mount point utilization is too high. Consider scaling up your file system.',
        AlarmActions=['ARN::SNS::us-east-1:123456789012:MySNSTopic']
    )

    # Create an alarm for the S3 storage latency
    s3_storage_latency_alarm = cloudwatch_client.put_metric_alarm(
        AlarmName=f'{application_name}-S3-Storage-Latency-Alarm',
        Namespace='AWS/S3',
        MetricName='Latency',
        Statistic='Average',
        Period=60,
        EvaluationPeriods=2,
        Threshold=100.0,
        ComparisonOperator='GreaterThanThreshold',
        AlarmDescription='S3 storage latency is too high. Consider using a different storage tier or upgrading your network connection.',
        AlarmActions=['ARN::SNS::us-east-1:123456789012:MySNSTopic']
    )

    return efs_mount_point_utilization_alarm, s3_storage_latency_alarm

# Call the function to create the alarms
efs_mount_point_utilization_alarm, s3_storage_latency_alarm = create_cloudwatch_alarms('MyApplication')
