import json
import boto3

credentials = boto3.Session().get_credentials()

def lambda_handler(event, context):
    # TODO implement
    region_name = event['region']
    return json.dumps(get_vpcs_and_subnets(region_name))

def get_vpcs_and_subnets(region_name):
    ec2 = boto3.client(
        'ec2',
        region_name=region_name,
        aws_access_key_id=credentials.access_key,
        aws_secret_access_key=credentials.secret_key,
        aws_session_token=credentials.token,
    )
    describe_vpc = ec2.describe_vpcs()
    describe_subnets = ec2.describe_subnets()

    response = {
        "results": []
    }

    for vpc in describe_vpc['Vpcs']:
        for subnet in describe_subnets['Subnets']:
            subnets = list()
            if vpc['VpcId'] == subnet['VpcId']:
                subnets.append({
                    "CidrBlock": subnet['CidrBlock'],
                    "SubnetId": subnet['SubnetId']
                })
        response['results'].append({
            "CidrBlock": vpc['CidrBlock'],
            "VpcId": vpc['VpcId'],
            "Subnets": subnets
        })
    
    return response