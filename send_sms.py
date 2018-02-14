""" my twilio number: +1(843) 508-2536 
	auth: e8c0ce2a158f3e15df02d78cbdd9c9
"""


from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC9adef1e14e327577c5b9462f4c903013"
# Your Auth Token from twilio.com/console
auth_token  = "e8c0ce2a158f3e15df02d78cbdd9c9"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+15558675309", 
    from_="+18435082536",
    body="Hello from Python!")

print(message.sid)

