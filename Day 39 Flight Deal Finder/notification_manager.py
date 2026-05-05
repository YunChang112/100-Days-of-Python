import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = os.getenv("TWILIO_SID")
        self.auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        self.from_number = os.getenv("TWILIO_VIRTUAL_NUMBER")
        self.to_number = os.getenv("MY_PHONE_NUMBER")

        self.client = Client(self.account_sid, self.auth_token)

    def send_sms(self, message_body):
        try:
            message = self.client.messages.create(
                body=message_body,
                from_=self.from_number,
                to=self.to_number
            )
            print(f"短信发送成功！ 消息 ID: {message.sid}")
        except Exception as e:
            print(f"短信发送失败: {e}")


    pass