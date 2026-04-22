import requests
import json
import os
from dotenv import load_dotenv
# print(f"Loading env: {load_dotenv()}")
load_dotenv()

API_Key = os.getenv("Serpapi_key")

departure_destination = "YVR"
arrival_destination = "NRT"
Outbound_date = "2026-04-27"
Return_date = "2026-05-04"


url = "https://www.searchapi.io/api/v1/search"
params = {
    "engine": "google_flights",
    "flight_type": "round_trip",
    "departure_id": departure_destination,
    "arrival_id": arrival_destination,
    "outbound_date": Outbound_date,
    "return_date": Return_date,
    "api_key": API_Key
}

try:
    with open("flight_cache.json", "r") as file:
        data = json.load(file)
        print("使用缓存数据...")
except FileNotFoundError:
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    with open("flight_cache.json", "w") as file:
        json.dump(data, file, indent=4)
        print("API请求成功并已存入缓存")
print(data)


class FlightData:
    #This class is responsible for structuring the flight data.
    pass