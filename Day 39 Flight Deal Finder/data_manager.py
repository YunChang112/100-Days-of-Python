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

        # 下面这两句，当时indent的位置错了，Gemini给的比喻是：你建了一个“木工工具箱（class）“，里面有一个”卷尺（self.destination_data)“。
        # 但是你在量尺寸的时候，居然自己从兜里掏出了另一把尺子，完全没碰工具箱里的那把。
        # 也是第一次写，直接把味清洗的数据传给了main.py，再往下两个，分别是我写的清洗过的和Gemini清洗过的。

        # self.destination_data = data
        # return self.destination_data

        # 下面两行，是我第一次写的，我现在要让这个函数直接return city_code，这样在main.py里面，直接用city_code就行，所以底下的
        # 就写在data_manager.py这里面了，main.py就会瘦身。

        # self.destination_data = {row["iataCode"]: row["lowestPrice (usd)"] for row in data["sheet1"]}
        # print(self.destination_data)
        # return self.destination_data

        # 这下面这两行是Gemini写的，它把city名字和其对应的价格以dictionary的形式放进了list里面，下面是他的理由：
        """
        你的方法：像是在木料上直接用记号笔写价格。简单直接，但如果你还想记录“木料种类”、“进货日期”，木料表面很快就写不下了。
        我的方法：给每块木料挂一个“吊牌”（字典）。吊牌上可以无限增加信息：city, target_price, full_name, currency。不管吊牌上有多少项，
        木料本身依然整齐地排在货架（列表）上。
        为什么“列表套字典”比“纯字典”更pythonic?: 在python的工程实践中，我们倾向于把“一条完整的数据记录”看作一个独立的个体。
        编程思维的进化：从“对应关系”到“对象集合”
        你的思维：是在建立mapping（映射）。A对应B，适合查表。
        pythonic的思维：是在处理collection of objects（对象集合）。每一个item都是一个独立的“包裹”，包裹里装载着关于那个目的地的所有情报。
        
        """
        self.destination_data = [{"city": row["iataCode"], "target_price": row["lowestPrice (usd)"]} for row in data["sheet1"]]
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

