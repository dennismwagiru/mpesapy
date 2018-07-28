Mpesapy
=======
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

Getting Started
---------------

#### Prerequisites
1. <a href="https://developer.safaricom.co.ke/user/me/apps">Click here </a> and create your app on the Mpesa daraja portal.
2. Once that is done, you will be provided with a `Consumer Key` and a `Consumer Secret`
3. For development and testing environment use `sandbox` for env
4. For live environment use `api` for env

#### Installation:

    pip install git+https://github.com/dennismwagiru/mpesapy.git

#### Usage
Import Mpesa and create object
```python
from mpesapy import Mpesa
mpesa = Mpesa('sandbox', '600462', Consumer Key, Consumer Secret)

```

##### Generate Access Token
```python
access_token = mpesa.get_access_token()
```

##### Lipa Na M-Pesa Online Payment API
```python
res_json = mpesa.lipa_na_mpesa_online(Password='bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919', 
                                      Timestamp='20180704203000', Amount='10', PartyA='254708374149', PartyB='174379', 
                                      PhoneNumber='254708374149', 
                                      CallBackURL='https://putsreq.com/C1HAyC3fEEbl2UaEu6lU', 
                                      AccountReference='Test', TransactionDesc='Test')
```

##### C2B API
Register urls:
```python
res_json = mpesa.c2b_register_url(ValidationURL='https://putsreq.com/C1HAyC3fEEbl2UaEu6lU', 
                                  ConfirmationURL='https://putsreq.com/C1HAyC3fEEbl2UaEu6lU')

```

Simulate Transaction:
```python
res_json = mpesa.c2b_simulate(Amount=amount, MSISDN=phone_no, BillRefNumber=account_no)

```

##### B2C Payment Request
```python
res_json = mpesa.b2c_payment_request(InitiatorName='testapi', Amount=10, PartyB='254708374149', Remarks='Test', 
                                     SecurityCredential='nR47eKS3OWCwOGJofwW4Vze5Y2r9VtiNF+YrxopbnxjRckpZHDp379XscBqPLibV6ZKhQ0OjUFRTR7cVnxLrhF4PDZr8Eg4+euuYL/HB9DQHom0kuDwvxUS+ctQsRZ8gBB8d+QYBqb1hzsBuxl2jNohQpeqVOZ1tb1UzGPnLQfAcQuf/x6q5Ze0orzvC2BmCw75GhJl4quZEG2Pou72PQD2IAiQSUOWYSHcJC/3oyYqtLx6Vl98F9Qjx+6oKZHXqokkWccf2vOyl6ApQ5BKubfUPVSa9ggl87ZdffNueifs60HAIHKtD77NyV4G3vXfKBxbm5Z9AqVLbPp6yXS9AAw==',
                                     QueueTimeOutURL='https://putsreq.com/C1HAyC3fEEbl2UaEu6lU', 
                                     ResultURL='https://putsreq.com/C1HAyC3fEEbl2UaEu6lU', Occassion='Test')
```
##### B2B Payment Request
```python
res_json = mpesa.b2b_payment_request(Amount=10, PartyB='600000', RecieverIdentifierType=4, Remarks='Okay', 
                                     Initiator='testapi',
                                     SecurityCredential='nR47eKS3OWCwOGJofwW4Vze5Y2r9VtiNF+YrxopbnxjRckpZHDp379XscBqPLibV6ZKhQ0OjUFRTR7cVnxLrhF4PDZr8Eg4+euuYL/HB9DQHom0kuDwvxUS+ctQsRZ8gBB8d+QYBqb1hzsBuxl2jNohQpeqVOZ1tb1UzGPnLQfAcQuf/x6q5Ze0orzvC2BmCw75GhJl4quZEG2Pou72PQD2IAiQSUOWYSHcJC/3oyYqtLx6Vl98F9Qjx+6oKZHXqokkWccf2vOyl6ApQ5BKubfUPVSa9ggl87ZdffNueifs60HAIHKtD77NyV4G3vXfKBxbm5Z9AqVLbPp6yXS9AAw==', 
                                     QueueTimeOutURL='https://putsreq.com/C1HAyC3fEEbl2UaEu6lU',
                                     ResultURL='https://putsreq.com/C1HAyC3fEEbl2UaEu6lU', AccountReference='Test')
```
##### Account Balance Request
```python
res_json = mpesa.balance(PartyA='600462', IdentifierType=4, Remarks='Okay', Initiator='testapi', 
                         SecurityCredential='nR47eKS3OWCwOGJofwW4Vze5Y2r9VtiNF+YrxopbnxjRckpZHDp379XscBqPLibV6ZKhQ0OjUFRTR7cVnxLrhF4PDZr8Eg4+euuYL/HB9DQHom0kuDwvxUS+ctQsRZ8gBB8d+QYBqb1hzsBuxl2jNohQpeqVOZ1tb1UzGPnLQfAcQuf/x6q5Ze0orzvC2BmCw75GhJl4quZEG2Pou72PQD2IAiQSUOWYSHcJC/3oyYqtLx6Vl98F9Qjx+6oKZHXqokkWccf2vOyl6ApQ5BKubfUPVSa9ggl87ZdffNueifs60HAIHKtD77NyV4G3vXfKBxbm5Z9AqVLbPp6yXS9AAw==', 
                         QueueTimeOutURL='https://putsreq.com/C1HAyC3fEEbl2UaEu6lU',
                         ResultURL='https://putsreq.com/C1HAyC3fEEbl2UaEu6lU')
```
##### Transaction Status Request

##### Reversal Request
