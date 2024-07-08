import pandas as pd
import numpy as np
import requests
import json
import os
import boto3
import logging
from botocore.exceptions import ClientError


symbol= 'AMZN'
exchange = 'US'
api_token ='demo'
fmt='json'

url = f'https://eodhd.com/api/eod/{symbol}.{exchange}?period=d&api_token={api_token}&from=2021-01-01&fmt={fmt}'

path = os.getcwd()
file_path = f"{path}\\data\\stock_history.json"
# print(file_path)

file_name = file_path
bucket = 's3-datalake-stock-price-darshil0208'
object_name = 'AMZN_stock_price.json'


def create_json_file(url):

    data = requests.get(url).json()

    # print(len(data))
    # print(url)
    for record in data:
        with open(file_path, 'a') as f:
            json.dump(record, f, separators=(',', ':'))
            f.write('\n')
    return

def upload_file_to_s3(file_name,bucket,object_name):
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True