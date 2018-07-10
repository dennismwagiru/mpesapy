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

        """
        m = mpesapy.mpesapy('sandbox', '603067', 'CltVqUe6GAJVeXCE4VxldKFihjTg7y84', '1WybgBcGaIfBZhe9')
        
        Consumer Key	X2bHLOS1iSXMMNWzoymB3KkMyyjSHEpO
        Consumer Secret	7ZYNkkZyqi9NLEqv
        Shortcode 1	603067
        Initiator Name (Shortcode 1)	api.saf
        Security Credential (Shortcode 1)	11789
        Shortcode 2	600000
        Test MSISDN	254708374149
        ExpiryDate	2018-07-05T16:27:19+03:00
        Lipa Na Mpesa Online Shortcode:	174379
        Lipa Na Mpesa Online PassKey: bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919
        """

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
        # m.lipa_na_mpesa_online(BusinessShortCode='174379', Password='bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919', Timestamp='20180704203000', Amount=10, PartyA='254704149404', PartyB='174379', PhoneNumber='254704149404', CallBackURL='https://putsreq.com/VbOStiHrt6XSkdDeSMFW', AccountReference='1222', TransactionDesc='iii')
        expected_keys = ["Password", "Timestamp",
                         "Amount", "PartyA", "PartyB", "PhoneNumber",
                         "CallBackURL", "AccountReference", "TransactionDesc"]
        payload = self.process_kwargs(expected_keys, kwargs)
        string = self.short_code + payload['Password'] + payload['Timestamp']
        key = base64.b64encode((string).encode("utf-8")).decode("ascii").replace('\n', '')
        payload['Password'] = key
        payload['Business']
        payload['TransactionType'] = 'CustomerPayBillOnline'
        url = URL[self.env]['online_checkout']
        access_token = self.get_access_token()
        headers = {
            'Authorization': 'Bearer ' + access_token
        }
        res = requests.post(url=url, data=payload, headers=headers).text
        res_json = json.loads(res)

        print(res_json)