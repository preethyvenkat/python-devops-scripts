import boto3
import argparse

def check_health(region, target_group):
    client = boto3.client('elbv2', region_name=region)
    response = client.describe_target_health(TargetGroupArn=target_group)
    for target in response['TargetHealthDescriptions']:
        status = target['TargetHealth']['State']
        print(f"Target: {target['Target']['Id']} - Status: {status}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--region", required=True, help="AWS region")
    parser.add_argument("--target-group", required=True, help="Target Group ARN")
    args = parser.parse_args()
    check_health(args.region, args.target_group)
