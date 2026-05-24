#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests_cache
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData, find_cheapest_flight
from notification_manager import NotificationManager
from datetime import datetime, timedelta

requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600
    }
)

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
pprint(sheet_data)

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=8)

"""
这里面，是Prototyping, 即“局部原型测试代码”，用了一个例子Paris跑通了，之后就可以遍历所有内容了。
fs = FlightSearch()
flight_search_result = fs.check_flights(
    "LHR",
    "CDG",
    from_time=tomorrow,
    to_time=six_month_from_today,)

cheapest_flight_info = find_cheapest_flight(
    data=flight_search_result,
    return_date=six_month_from_today)

if cheapest_flight_info.price != "N/A" and cheapest_flight_info.price < sheet_data[2]["lowestPrice"]:
    pprint(f"Lower price flight found to {sheet_data[2]["city"]}!")
    dm.update_lowest_price(sheet_data[2]["id"], cheapest_flight_info.price)
"""

flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "YVR"

for destination in sheet_data:
    pprint(f"Getting flights for (destination['city']...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights, return_date=six_month_from_today.strftime("%Y-%m-%d"))
    pprint(f"{destination['city']}: CAD {cheapest_flight.price} on {tomorrow.strftime("%Y-%m-%d")} at {cheapest_flight.price} and return data on {six_month_from_today.strftime("%Y-%m-%d")}")

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        pprint(f"Lower price flight found to {destination['city']}!")
        data_manager.update_lowest_price(destination["id"], cheapest_flight.price)

    message = (f"好消息！ 从{cheapest_flight.origin_airport}去{cheapest_flight.destination_airport}的机票只要 ${cheapest_flight.price}"
               f"出发日期：{tomorrow.strftime("%Y-%m-%d")}, 时间：{cheapest_flight.out_date}")
    notification_manager.send_sms(message)