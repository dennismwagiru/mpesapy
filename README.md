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
res_json = mpesa.lipa_na_mpesa_online(Password='bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919', Timestamp='20180704203000',
                                      Amount='10', PartyA='254708374149', PartyB='174379', PhoneNumber='254708374149',
                                      CallBackURL='https://putsreq.com/C1HAyC3fEEbl2UaEu6lU', AccountReference='Test', TransactionDesc='Test')
```

##### C2B API
Register urls:

        res_json = mpesa.c2b_register_url(ValidationURL=validation_url, ConfirmationURL=confirmation_url)
Simulate Transaction:

        res_json = mpesa.c2b_simulate(CommandID='CustomerPayBillOnline', Amount=amount, MSISDN=phone_no, BillRefNumber=account_no)

##### B2C Payment Request
    res_json = mpesa.b2c_payment_request(InitiatorName=initiator_name, SecurityCredential=security_credential, CommandID='BusinessPayment', Amount=amount, PartyA=short_code, PartyB=partyB, Remarks=remarks, QueueTimeOutURL=timeout_url, ResultURL=result_url, Occassion=ocassion)

##### B2B Payment Request
    res_json = mpesa.b2b_payment_request(CommandID='BusinessPayBill', Amount=amount, PartyA=partyA, SenderIdentifier=4, PartyB=short_code, RecieverIdentifierType=4, Remarks=remarks, Initiator=initiator, SecurityCredential=security_credential, QueueTimeOutURL=timeout_url, ResultURL=result_url, AccountReference=acc_ref)

##### Account Balance Request
    res_json = mpesa.balance(CommandID='AccountBalance', PartyA=partyA, IdentifierType=4, Remarks=remarks, Initiator=initiator, SecurityCredential=security_credential, QueueTimeOutURL=timeout_url, ResultURL=result_url)

##### Transaction Status Request

##### Reversal Request
