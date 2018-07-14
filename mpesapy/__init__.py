import json
import requests
from requests.auth import HTTPBasicAuth
import base64

"""
mpesapy

This is a wrapper for Mpesa daraja api

Work in progress

"""
class Mpesa:

    def __init__(self, env, short_code, consumer_key, consumer_secret):
        self.env = env
        self.short_code = short_code
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret

    def reversal(self, **kwargs):
        expected_keys = ['CommandID', 'ReceiverParty', 'ReceiverIdentifierType', 'Remarks', 'Initiator',
                         'SecurityCredential', 'QueueTimeOutURL', 'ResultURL', 'TransactionID', 'Occasion']
        payload = self.process_kwargs(expected_keys, kwargs)
        url = self.get_url('reversal')
        access_token = self.get_access_token()
        headers = {
            'Authorization': 'Bearer ' + access_token
        }
        res = requests.post(url=url, json=payload, headers=headers).text
        return json.loads(res)

    def transaction_status(self, **kwargs):
        expected_keys = ['CommandID', 'PartyA', 'IdentifierType', 'Remarks', 'Initiator', 'SecurityCredential',
                         'QueueTimeOutURL', 'ResultURL', 'TransactionID', 'Occasion']
        payload = self.process_kwargs(expected_keys, kwargs)
        url = self.get_url('transaction_status')
        access_token = self.get_access_token()
        headers = {
            'Authorization': 'Bearer ' + access_token
        }
        res = requests.post(url=url, json=payload, headers=headers).text
        return json.loads(res)

    def balance(self, **kwargs):
        expected_keys = ['CommandID', 'PartyA', 'IdentifierType', 'Remarks', 'Initiator', 'SecurityCredential',
                         'QueueTimeOutURL', 'ResultURL']
        payload = self.process_kwargs(expected_keys, kwargs)
        url = self.get_url('account_balance')
        access_token = self.get_access_token()
        headers = {
            'Authorization': 'Bearer ' + access_token
        }
        res = requests.post(url=url, json=payload, headers=headers).text
        return json.loads(res)

    def b2b_payment_request(self, **kwargs):
        expected_keys = ['CommandID', 'Amount', 'PartyA', 'SenderIdentifier', 'PartyB', 'RecieverIdentifierType',
                         'Remarks', 'Initiator', 'SecurityCredential', 'QueueTimeOutURL', 'ResultURL',
                         'AccountReference']
        payload = self.process_kwargs(expected_keys, kwargs)
        url = self.get_url('b2b_payment_request')
        access_token = self.get_access_token()
        headers = {
            'Authorization': 'Bearer ' + access_token
        }
        res = requests.post(url=url, json=payload, headers=headers).text
        return json.loads(res)

    def b2c_payment_request(self, **kwargs):
        expected_keys = ['InitiatorName', 'SecurityCredential', 'CommandID', 'Amount', 'PartyA', 'PartyB', 'Remarks',
                         'QueueTimeOutURL', 'ResultURL', 'Occassion']
        payload = self.process_kwargs(expected_keys, kwargs)
        url = self.get_url('b2c_payment_request')
        access_token = self.get_access_token()
        headers = {
            'Authorization': 'Bearer ' + access_token
        }
        res = requests.post(url=url, json=payload, headers=headers).text
        return json.loads(res)


    def c2b_simulate(self, **kwargs):
        expected_keys = ['CommandID', 'Amount', 'Msisdn', 'BillRefNumber']
        payload = self.process_kwargs(expected_keys, kwargs)
        payload['ShortCode'] = self.short_code
        url = self.get_url('c2b_simulate')
        access_token = self.get_access_token()
        headers = {
            'Authorization': 'Bearer ' + access_token
        }

        res = requests.post(url=url, json=payload, headers=headers).text
        return json.loads(res)

    def c2b_register_url(self, **kwargs):
        expected_keys = ['ValidationURL', 'ConfirmationURL']
        payload = self.process_kwargs(expected_keys, kwargs)
        payload['ResponseType'] = 'Completed'
        payload['ShortCode'] = self.short_code
        url = self.get_url('register_url')
        access_token = self.get_access_token()
        headers = {
            'Authorization': 'Bearer ' + access_token
        }
        res = requests.post(url=url, json=payload, headers=headers).text
        return json.loads(res)

    def lipa_na_mpesa_online(self, **kwargs):
        expected_keys = ['Password', 'Timestamp', 'Amount', 'PartyA', 'PartyB', 'PhoneNumber', 'CallBackURL',
                         'AccountReference', 'TransactionDesc']
        payload = self.process_kwargs(expected_keys, kwargs)
        string = self.short_code + payload['Password'] + payload['Timestamp']
        key = base64.b64encode((string).encode("utf-8")).decode("ascii").replace('\n', '')
        payload['Password'] = key
        payload['BusinessShortCode'] = self.short_code
        payload['TransactionType'] = 'CustomerPayBillOnline'
        url = self.get_url('online_checkout')
        access_token = self.get_access_token()
        headers = {
            'Authorization': 'Bearer ' + access_token
        }
        res = requests.post(url=url, json=payload, headers=headers).text
        return json.loads(res)

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
        url = self.get_url('authentication')
        res = requests.get(url,params=dict(grant_type='client_credentials'),
                           auth=requests.auth.HTTPBasicAuth(self.consumer_key, self.consumer_secret)).text
        res_json = json.loads(res)

        if 'errorMessage' in res_json:
            raise ValueError(res_json['errorMessage'])
        return res_json['access_token']

    def get_url(self, api):
        urls = {
            'sandbox' : {
                'authentication': 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials',
                'online_checkout': 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest',
                'register_url': 'https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl',
                'c2b_simulate': 'https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate',
                'b2c_payment_request': 'https://sandbox.safaricom.co.ke/mpesa/b2c/v1/paymentrequest',
                'b2b_payment_request': 'https://sandbox.safaricom.co.ke/mpesa/b2b/v1/paymentrequest',
                'account_balance': 'https://sandbox.safaricom.co.ke/mpesa/accountbalance/v1/query',
                'transaction_status': 'https://sandbox.safaricom.co.ke/mpesa/transactionstatus/v1/query',
                'reversal': 'https://sandbox.safaricom.co.ke/mpesa/reversal/v1/request'
            }
        }

        return urls[self.env][api]