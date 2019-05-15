import os
from twilio.rest import Client

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]

client = Client(account_sid, auth_token)

client.messages.create(
	to="+15106005512",
	from_="+12028757110",
	body="This is the ship that made awesome work"
	)