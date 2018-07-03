
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

