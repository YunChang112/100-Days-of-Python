import os
from dotenv import load_dotenv
import requests
from pprint import pprint

load_dotenv()

SERPAPI_ENDPOINT = "https://www.searchapi.io/api/v1/search?engine=google_flights"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.Serpapi_key = os.environ["SERPAPI_API_KEY"]

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        params = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time.strftime("%Y-%m-%d"),
            "return_date":  to_time.strftime("%Y-%m-%d"),
            # "type": "1",
            "adults": "1",
            "currency": "CAD",
            "api_key": self.Serpapi_key
        }

        response = requests.get(url=SERPAPI_ENDPOINT, params=params)
        response.raise_for_status()
        data = response.json()
        return data

# 以下，是在flight_search.py里面，直接看结果的方法，必须从“类”就开始调用。
# if __name__ == "__main__":
#     searcher = FlightSearch()
#     test_data = searcher.check_flights("LHR", "NRT", "2026-06-01", "2026-06-10")
#     pprint(test_data)