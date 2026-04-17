import requests
import os
from dotenv import load_dotenv
load_dotenv()
from datetime import datetime

USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv("TOKEN")
GRAPH_ID = "graph1"

"""注册新用户"""
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


"""添加graph"""
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


"""添加每日记录"""
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# today = datetime.now()
# print(today.strftime("%Y%m%d"))

"""用datetime函数添加具体日期"""
today = datetime(year=2026, month=4, day=11)

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today?"),
}

# response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
# print(response.text)


"""修改已填信息，用put"""
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"

pixel_update_date = {
    "quantity": "7",
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_update_date, headers=headers)
# print(response.text)


"""删除已填信息，用delete"""
pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"

# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
#
# print(response.text)