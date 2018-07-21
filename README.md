# Mpesapy
This wrapper seeks to help python developers implement the various Mpesa APIs without much hustle. It is based on the REST API (daraja) whose documentation is available on http://developer.safaricom.co.ke.

The wrapper implements the following endpoints:
>1. Authentication
>2. Lipa na M-Pesa Online Payment
>3. C2B
>4. B2C
>5. B2B
>6. Account Balance
>7. Transaction Status
>8. Reversal

### Getting Started

####Prerequisites
1. <a href="https://developer.safaricom.co.ke/user/me/apps">Click here </a> and create your app on the Mpesa daraja portal.
2. Once that is done, you will be provided with a `Consumer Key` and a `Consumer Secret`
3. For development and testing environment use `sandbox` for env
4. For live environment use `api` for env
####Installation
>  pip install git+https://github.com/dennismwagiru/mpesapy.git

####Usage
Import Mpesa and create object

`from mpesapy import Mpesa`

`mpesa = Mpesa(env, short_code, Consumer Key, Consumer Secret)`

#####Generate Access Token
`access_token = mpesa.get_access_token()`

#####Lipa Na M-Pesa Online Payment API
``json = mpesa.lipa_na_mpesa_online(BusinessShortCode=short_code, Password=password, Timestamp=timestamp, Amount=amount, PartyA=partyA, PartyB=partyB, PhoneNumber=phone_number, CallBackURL=call_back_url, AccountReference=acc_ref, TransactionDesc=trans_desc)``

