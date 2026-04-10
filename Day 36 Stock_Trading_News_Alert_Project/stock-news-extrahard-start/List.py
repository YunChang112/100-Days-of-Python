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
print(weather_data)

# for item in weather_data["list"]:
#     weather_id = item["weather"][0]["id"]
#     if weather_id == 804:
#         print("rain")
#     else:
#         print(weather_id)