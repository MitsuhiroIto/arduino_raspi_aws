from __future__ import print_function

import json
import boto3
from decimal import Decimal

print('Loading function')

def lambda_handler(event, context):
    client = boto3.client('cloudwatch')
    for record in event['Records']:
        response = client.put_metric_data(
            Namespace='mitsu_raspi_temp',
            MetricData=[
                {
                    'MetricName': 'temperature',
                    'Dimensions': [
                        {
                            'Name': 'mitsu-raspi-temp',
                            'Value': 'mitsu-raspi-temp',
                        },
                    ],
                    'Value': Decimal(record['dynamodb']['NewImage']['payload']['M']['temperature']['S']),
                    'Unit': 'None'
                },
            ]
        )
