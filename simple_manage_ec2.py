import boto3

ec2_client = boto3.client('ec2')


# ec2_client = boto3.client(
#     'ec2',
#     aws_access_key_id="xxxxxxxxxxxxxxxxxxxxxxxx",
#     aws_secret_access_key="xxxxxxxxxxxxxxxxxxxxxxxx"
# )

regions = [region['RegionName']
           for region in ec2_client.describe_regions()['Regions']]


def stop_instances():
    for region in regions:
        ec2 = boto3.resource('ec2', region_name=region)
        print("Regions: ", region)
        instances_stopped = ec2.instances.filter(
            Filters=[{'Name': 'instance-state-name',
                      'Values': ['running']}])
        for instance in instances_stopped:
            instance.stop()
            print("Stopped instance: ", instance.id)


def start_instances():
    for region in regions:
        ec2 = boto3.resource('ec2', region_name=region)
        print("Regions: ", region)
        instances_running = ec2.instances.filter(
            Filters=[{'Name': 'instance-state-name',
                      'Values': ['stopped']}])
        for instance in instances_running:
            instance.start()
            print("Start instance: ", instance.id)


def terminate_instances():
    for region in regions:
        ec2 = boto3.resource('ec2', region_name=region)
        print("Regions: ", region)
        instances_running = ec2.instances.filter(
            Filters=[{'Name': 'instance-state-name',
                      'Values': ['stopped', 'running']}])
        for instance in instances_running:
            instance.terminate()
            print("Terminate instance: ", instance.id)
