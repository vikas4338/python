import boto3

region = 'us-west-1'
tag_key = 'YourTagKey'
tag_value = 'myTagName' #tag to indentify certain group of instances

ec2 = boto3.client('ec2', region_name=region)

def stop_tagged_instances(event, context):
    # Describe instances to get information about each instance with the specified tag
    response = ec2.describe_instances(
        Filters=[
            {
                'Name': f'tag:{tag_key}',
                'Values': [tag_value]
            },
            {
                'Name': 'instance-state-name',
                'Values': ['running']
            }
        ]
    )

    instance_ids = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])

    if instance_ids:
        print("Stopping instances:", instance_ids)
        ec2.stop_instances(InstanceIds=instance_ids)
        print("Instances stopped")
    else:
        print("No running instances with the specified tag to stop")

# The handler function that AWS Lambda calls in
def lambda_handler(event, context):
    stop_tagged_instances(event, context)
