import json
import requests
from requests.auth import HTTPBasicAuth
import base64

name = "mpesapy"

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
        expected_keys = ['PartyA', 'IdentifierType', 'Remarks', 'Initiator', 'SecurityCredential',
                         'QueueTimeOutURL', 'ResultURL']
        payload = self.process_kwargs(expected_keys, kwargs)
        payload['CommandID']='AccountBalance'
        url = self.get_url('account_balance')
        access_token = self.get_access_token()
        headers = {
            'Authorization': 'Bearer ' + access_token
        }
        res = requests.post(url=url, json=payload, headers=headers).text
        return json.loads(res)

    def b2b_payment_request(self, **kwargs):
        expected_keys = ['Amount', 'PartyB', 'RecieverIdentifierType',
                         'Remarks', 'Initiator', 'SecurityCredential', 'QueueTimeOutURL', 'ResultURL',
                         'AccountReference']
        payload = self.process_kwargs(expected_keys, kwargs)
        payload['CommandID'] ='BusinessPayBill'
        payload['SenderIdentifier'] = 4
        payload['PartyA'] = self.short_code
        url = self.get_url('b2b_payment_request')
        access_token = self.get_access_token()
        headers = {
            'Authorization': 'Bearer ' + access_token
        }
        res = requests.post(url=url, json=payload, headers=headers).text
        return json.loads(res)

    def b2c_payment_request(self, **kwargs):
        expected_keys = ['InitiatorName', 'SecurityCredential', 'Amount', 'PartyB', 'Remarks',
                         'QueueTimeOutURL', 'ResultURL', 'Occassion']
        payload = self.process_kwargs(expected_keys, kwargs)
        payload['CommandID'] = 'BusinessPayment'
        payload['PartyA'] = self.short_code
        url = self.get_url('b2c_payment_request')
        access_token = self.get_access_token()
        headers = {
            'Authorization': 'Bearer ' + access_token
        }
        res = requests.post(url=url, json=payload, headers=headers).text
        return json.loads(res)


    def c2b_simulate(self, **kwargs):
        expected_keys = ['Amount', 'MSISDN', 'BillRefNumber']
        payload = self.process_kwargs(expected_keys, kwargs)
        payload['ShortCode'] = self.short_code
        payload['CommandID'] = 'CustomerPayBillOnline'
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
        expected_keys = ['Password', 'Timestamp', 'Amount', 'PartyA', 'PhoneNumber', 'CallBackURL',
                         'AccountReference', 'TransactionDesc']
        payload = self.process_kwargs(expected_keys, kwargs)
        string = self.short_code + payload['Password'] + payload['Timestamp']
        key = base64.b64encode((string).encode("utf-8")).decode("ascii").replace('\n', '')
        payload['Password'] = key
        payload['BusinessShortCode'] = self.short_code
        payload['PartyB'] = self.short_code
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
            'authentication': 'https://{}.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'.format(self.env),
            'online_checkout': 'https://{}.safaricom.co.ke/mpesa/stkpush/v1/processrequest'.format(self.env),
            'register_url': 'https://{}.safaricom.co.ke/mpesa/c2b/v1/registerurl'.format(self.env),
            'c2b_simulate': 'https://{}.safaricom.co.ke/mpesa/c2b/v1/simulate'.format(self.env),
            'b2c_payment_request': 'https://{}.safaricom.co.ke/mpesa/b2c/v1/paymentrequest'.format(self.env),
            'b2b_payment_request': 'https://{}.safaricom.co.ke/mpesa/b2b/v1/paymentrequest'.format(self.env),
            'account_balance': 'https://{}.safaricom.co.ke/mpesa/accountbalance/v1/query'.format(self.env),
            'transaction_status': 'https://{}.safaricom.co.ke/mpesa/transactionstatus/v1/query'.format(self.env),
            'reversal': 'https://{}.safaricom.co.ke/mpesa/reversal/v1/request'.format(self.env)
        }

        return urls[api]