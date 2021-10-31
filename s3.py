import boto3
def upload_object():
    s3 = boto3.resource('s3')
    for bucket in s3.buckets.all():
        bucketname = bucket.name
        print(bucketname)
        if bucketname == 'abc':
            data = open('test.txt', 'rb')
            s3.Bucket(bucketname).put_object(Key='test.txt', Body=data)
        bucket = s3.Bucket(bucketname)
        for obj in bucket.objects.all():
            print(obj.key)

def create_instance():
    ec2_client = boto3.client("ec2", region_name="ap-south-1")
    instances = ec2_client.run_instances(
        ImageId="ami-0c1a7f89451184c8b",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="mumbai"
    )
    print(instances["Instances"][0]["InstanceId"])

def terminate_instance():
    ids = ['i-06de476a5520473e5', 'i-01920b5c42ebf83e2', 'i-093501b1421b660b2']
    ec2 = boto3.client("ec2", region_name="ap-south-1")
    filters = [
        {
            'Name': 'instance-state-name', 
            'Values': ['running']
        }
    ]
    response=ec2.describe_instances(Filters=filters)
    RunningInstances = []
    for r in response['Reservations']:
        for i in r['Instances']:
            print(i['InstanceId'])
            RunningInstances.append(i['InstanceId'])
    ec2.terminate_instances(InstanceIds=RunningInstances)
    

#create_instance()
#upload_object()
terminate_instance()
