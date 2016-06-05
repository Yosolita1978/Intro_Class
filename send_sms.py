from security_info import TWILIO_AUTH_TOKEN, TWILIO_ACCOUNT_SID, TWILIO_PHONE
from twilio.rest import TwilioRestClient


def send_SMS(to, message):
    auth_token = TWILIO_AUTH_TOKEN
    account_sid = TWILIO_ACCOUNT_SID
    client = TwilioRestClient(account_sid, auth_token)

    message = client.messages.create(to=to, from_=TWILIO_PHONE, 
    body=message) 
    return message.sid


