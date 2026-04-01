import requests

api_key = "4a53138c12590da7af34543397ba8409"

parameters = {
    "lat": 49.282730,
    "lon": -123.120735,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
# print(weather_data)

for item in weather_data["list"]:
    weather_id = item["weather"][0]["id"]
    if weather_id == 804:
        print("rain")
    else:
        print(weather_id)

# print(data["list"][0]["weather"][0]["id"])
# print(data["list"][0]["weather"][0]["description"])

# """用遍历的方法把id和desc单独以dictionary的方式抽出来"""
# data_collector_with_for_loop = []
# for item in data["list"]:
#     weather_id = item["weather"][0]["id"]
#     weather_desc = item["weather"][0]["description"]
#     data_collector_with_for_loop.append({"id": weather_id, "desc": weather_desc})
# print("data_collector_with_for_loop")
# print(data_collector_with_for_loop)
#
# """list comprehension in list format"""
# data_collector_with_list_comprehension = [(item["weather"][0]["id"], item["weather"][0]["description"]) for item in data["list"]]
# print("list comprehension in list format")
# print(data_collector_with_list_comprehension)
# print(type(data_collector_with_list_comprehension))
#
# """list comprehension in dictionary format"""
# data_collector_with_dictionary_comprehension_in_dictionary_format = [{"id": item["weather"][0]["id"], "desc": item["weather"][0]["description"]} for item in data["list"]]
# print("list comprehension in dictionary format")
# print(data_collector_with_dictionary_comprehension_in_dictionary_format)
# print(type(data_collector_with_dictionary_comprehension_in_dictionary_format))
#
# """dictionary comprehension"""
# data_collector_with_dictionary_comprehension = {item["weather"][0]["id"]: item["weather"][0]["description"] for item in data["list"]}
# print("dictionary comprehension")
# print(type(data_collector_with_dictionary_comprehension))
# print(data_collector_with_dictionary_comprehension)
#
# """class_generator"""
# data_collector_with_generator = ({"id": item["weather"][0]["id"], "desc": item["weather"][0]["description"]} for item in data["list"])
# print("class_generator")
# print(type(data_collector_with_generator))
# print(data_collector_with_generator)
# print("open_generator")
# print(list(data_collector_with_generator))

