#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

dm = DataManager()

fs = FlightSearch()
nm = NotificationManager()

"""
以下，用的是我的思路，把clean_dictionary，即data_manager.py传过来的是个城市与价格的dictionary
# for city_code, target_price in dm.get_destination_data().items():
#     price = fs.get_price(city_code)
#     # print(f"{city_code}的当前价格是：{price}")
# 
#     if price <= target_price:
#         print(f"{city_code}的当前价格是：{price}, 符合心理价位{target_price}")
#     else:
#         print(f"价格还没下来，高于咱们的心理价位{target_price},再等等。")
"""

"""
以下，用的是Gemini的思路，在data_manager.py里面，把return的内容用list套dictionary的方式，然后用item[]来取值的方式，更加的灵活、
pythonic.详细背书，请见data_manager.py
"""
# for item in dm.get_destination_data():
#     current_price = fs.get_price(item["city"])
#     if current_price <= item["target_price"]:
#         alert_msg = f"{item["city"]}的当前价格是：{current_price}, 符合心理价位{item["target_price"]}"
#         nm.send_sms(alert_msg)
#     else:
#         print(f"价格还没下来，高于咱们的心理价位{item["target_price"]}")

"""
以下，用的是“脚本小子”和“软件工程师”的分水岭。把机票信息全部打包到flight_data里面，这样传到main.py里面，就可以用“人话”来调取信息。
"""
for item in dm.get_destination_data():
    city_code = item["city"]
    target_price = item["target_price"]

    flight = fs.get_price(city_code)

    if flight.price <= target_price:
        message = (f"好消息！ 从{flight.origin_airport}去{flight.destination_airport}的机票只要 ${flight.price}"
                   f"出发日期：{flight.out_date}")
        nm.send_sms(message)
    else:
        print(f"{flight.destination_airport}的当前价 ${flight.price}还没降到目标价 ${target_price}。")
