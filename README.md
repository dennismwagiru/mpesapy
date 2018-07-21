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

    from mpesapy import Mpesa
    mpesa = Mpesa(env, short_code, Consumer Key, Consumer Secret)

##### Generate Access Token
    access_token = mpesa.get_access_token()

##### Lipa Na M-Pesa Online Payment API
    res_json = mpesa.lipa_na_mpesa_online(BusinessShortCode=short_code, Password=password, Timestamp=timestamp, Amount=amount, PartyA=partyA, PartyB=partyB, PhoneNumber=phone_number, CallBackURL=call_back_url, AccountReference=acc_ref, TransactionDesc=trans_desc)

##### C2B API
Register urls:

        m.c2b_register_url(ValidationURL=validation_url, ConfirmationURL=confirmation_url)
Simulate Transaction:

        m.c2b_simulate(CommandID='CustomerPayBillOnline', Amount=amount, MSISDN=phone_no, BillRefNumber=account_no)

##### B2C Payment Request
    m.b2c_payment_request(InitiatorName=initiator_name, SecurityCredential=security_credential, CommandID='BusinessPayment', Amount=amount, PartyA=short_code, PartyB=partyB, Remarks=remarks, QueueTimeOutURL=timeout_url, ResultURL=result_url, Occassion=ocassion)

##### B2B Payment Request
    m.b2b_payment_request(CommandID='BusinessPayBill', Amount=amount, PartyA=partyA, SenderIdentifier=4, PartyB=short_code, RecieverIdentifierType=4, Remarks=remarks, Initiator=initiator, SecurityCredential=security_credential, QueueTimeOutURL=timeout_url, ResultURL=result_url, AccountReference=acc_ref)

##### Account Balance Request
    m.balance(CommandID='AccountBalance', PartyA=partyA, IdentifierType=4, Remarks=remarks, Initiator=initiator, SecurityCredential=security_credential, QueueTimeOutURL=timeout_url, ResultURL=result_url)

##### Transaction Status Request

##### Reversal Request