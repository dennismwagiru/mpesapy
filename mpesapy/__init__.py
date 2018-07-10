import json
import requests
from requests.auth import HTTPBasicAuth
import base64

from .urls import URL

"""
mpesapy

This is a wrapper for Mpesa daraja api

Work in progress

"""
class mpesapy:

    def __init__(self, env, short_code, consumer_key, consumer_secret):
        self.env = env
        self.short_code = short_code
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret

    @staticmethod
    def process_kwargs(expected_keys, kwargs):
        payload = {}

        for key in expected_keys:
            value = kwargs.pop(key)
            if not value:
                raise IndexError("Missing keyword argument: {}.".format(key))
            else:
                payload[key] = value

        return payload

    def get_access_token(self):
        url = URL[self.env]['authentication']
        res = requests.get(url,params=dict(grant_type='client_credentials'),
                           auth=requests.auth.HTTPBasicAuth(self.consumer_key, self.consumer_secret)).text
        res_json = json.loads(res)

        if 'errorMessage' in res_json:
            raise ValueError(res_json['errorMessage'])
        return res_json['access_token']

    def lipa_na_mpesa_online(self, **kwargs):
        expected_keys = ["Password", "Timestamp",
                         "Amount", "PartyA", "PartyB", "PhoneNumber",
                         "CallBackURL", "AccountReference", "TransactionDesc"]
        payload = self.process_kwargs(expected_keys, kwargs)
        string = self.short_code + payload['Password'] + payload['Timestamp']
        key = base64.b64encode((string).encode("utf-8")).decode("ascii").replace('\n', '')
        payload['Password'] = key
        payload['BusinessShortCode'] = self.short_code
        payload['TransactionType'] = 'CustomerPayBillOnline'
        url = URL[self.env]['online_checkout']
        access_token = self.get_access_token()
        headers = {
            'Authorization': 'Bearer ' + access_token
        }
        res = requests.post(url=url, json=payload, headers=headers).text
        return json.loads(res)