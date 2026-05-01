import requests
import json

url = "https://api.sheety.co/11606c60787b571f8e27b01f2aa26aa9/flightInfo/sheet1"


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        try:
            with open("flight_info.json", "r") as file:
                data = json.load(file)
                print("使用缓存数据...")
        except FileNotFoundError:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            with open("flight_info.json", "w") as file:
                json.dump(data, file, indent=4)
                print("API请求成功并已存入缓存")
            # 下面这一句，就是我第一次没明白、没写出来的地方，Gemini给的比喻是：你建了一个“木工工具箱（class）“，里面有一个”卷尺（self.destination_data)“。
            # 但是你在量尺寸的时候，居然自己从兜里掏出了另一把尺子，完全没碰工具箱里的那把。
        self.destination_data = data
        return self.destination_data









#########################################这一下，是我刚开始的时候，对data_manager.py的理解###################################
# with open("flight_info.json", "r")  as file:
#     flight_data = json.load(file)
#
#     clean_dictionary = {row["iataCode"]: row["lowestPrice (usd)"] for row in flight_data["sheet1"]}
#     for city_name, target_price in clean_dictionary.items():
#
#         cache_city_name = f"cache_{city_name}.json"
#
#         with open(cache_city_name, "r") as file:
#             search_data = json.load(file)
#             current_price = search_data["best_flights"][0]["price"]
#             if current_price < target_price:
#                 print(f"Let's go, {city_name}, Price is {current_price}!")
#             else:
#                 print("Not Yet")

