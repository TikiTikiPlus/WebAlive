import os,sys
import typing
import pydantic
from fastapi import FastAPI
import requests
import configparser
import json

config = configparser.ConfigParser()
config.read('config.ini')
access_token = config['token']['access_token']

order_link = 'https://api.diywebsite.net.au/v2/me/orders'

#create own config

orders = requests.get(order_link, headers={"Authorization":f"Bearer {access_token}"})

if orders.status_code==200:
    data: str = orders.text
    data_json=json.loads(data)
    print(data_json["result"]["orders"])
else:
    print(f"failed to retrieve data from {order_link}: {orders.status_code}")