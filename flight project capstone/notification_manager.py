from twilio.rest import Client

TWILIO_SID = 'ACffa857968df0e436bbc48bcfd2981ea8'
TWILIO_AUTH_TOKEN = 'aa0330f163ebbdfb3f0f66320c316737'
TWILIO_VIRTUAL_NUMBER = '+12184004710'
TWILIO_VERIFIED_NUMBER = '+12184004710'


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
