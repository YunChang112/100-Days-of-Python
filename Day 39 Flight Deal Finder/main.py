#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from data_manager import DataManager
from flight_search import FlightSearch

dm = DataManager()
# print(dm.get_destination_data())

fs = FlightSearch()
clean_dictionary = {row["iataCode"]: row["lowestPrice (usd)"] for row in dm.get_destination_data()["sheet1"]}
for city_code, target_price in clean_dictionary.items():
    price = fs.get_price(city_code)
    print(f"{city_code}的当前价格是：{price}")
