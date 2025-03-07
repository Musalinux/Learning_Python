import boto3
def create_ec2_instance():
    ec2 = boto3.resource('ec2') # Creates an EC2 resource
    instance = ec2.create_instances(
        ImageId = "ami-0123456abcdef1234",
        MinCount = 1,
        MaxCount = 2, 
        InstanceType = 't2.micro',
        KeyName = 'my-key-pair'
    )
    return instance[0].id

instance_id = create_ec2_instance()
print (f"Created instance with ID: {instance_id}")