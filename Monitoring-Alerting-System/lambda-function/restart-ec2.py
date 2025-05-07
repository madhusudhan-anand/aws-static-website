import json
import boto3

# Initialize EC2 client
ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    instance_id = 'i-001b12546600b5c92'

    print(f"Received event: {json.dumps(event)}")

    try:
        response = ec2.reboot_instances(InstanceIds=[instance_id])
        print(f"Rebooted EC2 instance: {instance_id}")
        return {
            'statusCode': 200,
            'body': f"Rebooted EC2 instance {instance_id}"
        }
    except Exception as e:
        print(f"Error rebooting EC2 instance: {e}")
        return {
            'statusCode': 500,
            'body': str(e)
        }

