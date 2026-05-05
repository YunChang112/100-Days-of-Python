import requests
import json
import os
from dotenv import load_dotenv
from flight_data import FlightData
# print(f"Loading env: {load_dotenv()}")
load_dotenv()


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.API_Key = os.getenv("Serpapi_key")

    def get_price(self, city_code):
        departure_destination = "YVR"
        arrival_destination = city_code
        outbound_date = "2026-06-02"
        return_date = "2026-06-09"
        file_name = f"cache_{city_code}.json"

        url = "https://www.searchapi.io/api/v1/search"
        params = {
            "engine": "google_flights",
            "flight_type": "round_trip",
            "departure_id": departure_destination,
            "arrival_id": arrival_destination,
            "outbound_date": outbound_date,
            "return_date": return_date,
            "api_key": self.API_Key
        }

        try:
            with open(file_name, "r") as file:
                data = json.load(file)
                # print("使用缓存数据...")
        except FileNotFoundError:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()

            with open(file_name, "w") as file:
                json.dump(data, file, indent=4)
                # print("API请求成功并已存入缓存")

        """在听了Gemini的structuring the flight data的建议之后，我把之前的return一个数字（如下两行），变成了return一个FlightData的实例。
        real_price = data["best_flights"][0]["price"]
        return real_price
        """
        try:
            real_price = data["best_flights"][0]["price"]
        except (KeyError, IndexError):
            print(f"没有找到去{city_code}的航班数据")
            return None
        """
        下面这些代码，就是与flight_data.py里面的__init__连起来，所以两者必须一一对应。这样，flight_search.py最后return的，就是一个
        实例。
        """
        new_flight = FlightData(
            price=real_price,
            origin_airport=departure_destination,
            destination_airport=arrival_destination,
            out_date=outbound_date,
            return_date=return_date,
        )

        return new_flight






#########################################这一下，是我刚开始的时候，对flight_search.py的理解###################################

# with open("flight_info.json", "r") as file:
#         flight_data = json.load(file)
#         iata_and_price = {row["iataCode"]: row["lowestPrice (usd)"] for row in flight_data["sheet1"]}
#
# for city_code, target_price in iata_and_price.items():
#
#     departure_destination = "YVR"
#     arrival_destination = city_code
#     Outbound_date = "2026-04-27"
#     Return_date = "2026-05-04"
#     file_name = f"cache_{city_code}.json"
#
#
#     url = "https://www.searchapi.io/api/v1/search"
#     params = {
#         "engine": "google_flights",
#         "flight_type": "round_trip",
#         "departure_id": departure_destination,
#         "arrival_id": arrival_destination,
#         "outbound_date": Outbound_date,
#         "return_date": Return_date,
#         "api_key": API_Key
#     }
#
#     try:
#         with open(file_name, "r") as file:
#             data = json.load(file)
#             print("使用缓存数据...")
#     except FileNotFoundError:
#         response = requests.get(url, params=params)
#         response.raise_for_status()
#         data = response.json()
#
#         with open(file_name, "w") as file:
#             json.dump(data, file, indent=4)
#             print("API请求成功并已存入缓存")
#     print(data)



