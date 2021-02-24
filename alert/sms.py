from twilio.rest import Client
import os

account_sid = os.environ.get("twilio_account_sid")
auth_token = os.environ.get("twilio_auth_token")
myphone = os.environ.get("myphone")
twilio_number = os.environ.get("my_twillio_number")

def send(contents, reciever=myphone):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to = reciever,
        from_ = twilio_number,
        body = contents
    )