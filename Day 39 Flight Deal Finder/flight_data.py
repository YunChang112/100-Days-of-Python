class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

    def __repr__(self):
        return f"FlightData(price={self.price}, to={self.destination_airport}, date={self.out_date}"





#########################################这一下，是我刚开始的时候，对flight_data.py的理解###################################
#
# import requests
# import os
# import json
# # from dotenv import load_dotenv
# # load_dotenv()
#
# url = "https://api.sheety.co/11606c60787b571f8e27b01f2aa26aa9/flightInfo/sheet1"
#
# try:
#     with open("flight_info.json", "r") as file:
#         data = json.load(file)
#         print("使用缓存数据...")
# except FileNotFoundError:
#     response = requests.get(url)
#     response.raise_for_status()
#     data = response.json()
#
#     with open("flight_info.json", "w") as file:
#         json.dump(data, file, indent=4)
#         print("API请求成功并已存入缓存")
# print(data)

