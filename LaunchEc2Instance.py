import boto3
def lambda_handler(event, context):
    region = event.get('region')
    image_id = event.get('image_id')
    instance_type = event.get('instance_type')
    key_name = event.get('key_name')

    ec2_client = boto3.client('ec2', region_name=region)
    numberOfInstances = event.get('numberOfInstances', 1)

    instances = ec2_client.run_instances( 
        ImageId=image_id,
        MinCount=numberOfInstances,
        MaxCount=numberOfInstances,
        InstanceType=instance_type,
        KeyName=key_name
    )

    instance_ids = [instance['InstanceId'] for instance in instances['Instances']]
    print(f'Launched instances: {instance_ids}')
