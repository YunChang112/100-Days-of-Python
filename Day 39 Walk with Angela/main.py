#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests_cache
import json
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6*30))

requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600
    }
)

dm = DataManager()
sheet_data = dm.get_destination_data()
pprint(sheet_data)

fs = FlightSearch()
flight_search_result = fs.check_flights(
    "LHR",
    "CDG",
    from_time=tomorrow,
    to_time=six_month_from_today,)
pprint(flight_search_result)









