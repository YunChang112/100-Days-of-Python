import os
import requests
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/11606c60787b571f8e27b01f2aa26aa9/flightInfoWithAngela/prices"

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.bearer = os.environ["SHEETY_BEARER"]
        self.my_headers = {
    "Authorization": f"Bearer {self.bearer}"
}
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self.my_headers)
        response.raise_for_status()
        data = response.json()

        self.destination_data = data["prices"]

        return self.destination_data
