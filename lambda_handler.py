import json, boto3
def lambda_handler(event, context):
    print("hello world")
    ec2_client = boto3.client("ec2", aws_access_key_id='AKIAZ2RIBVPAWAGWMIMI', aws_secret_access_key='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', region_name="ap-south-1")
    instances = ec2_client.run_instances(
        ImageId="ami-0c1a7f89451184c8b",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="mumbai"
    )
    print(instances["Instances"][0]["InstanceId"])
    return {
        'statusCode': 200,
        'body': json.dumps(instances["Instances"][0]["InstanceId"])
    }
