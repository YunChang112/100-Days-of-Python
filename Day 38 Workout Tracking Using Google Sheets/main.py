import requests
import os
from dotenv import load_dotenv
print(f"Loading env: {load_dotenv()}")
load_dotenv()
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 80
HEIGHT_CM = 178
AGE = 40

APP_ID = os.getenv("APP_ID")
NUTRITION_API_KEY = os.getenv("NUTRITION_API_KEY")
# BASE_URL = "https://app.100daysofpython.dev"

"""API Document要求的Use this endpoint to verify the API is running before making exercise requests."""
# response = requests.get(url="https://app.100daysofpython.dev/healthz")
# print(response.text)

"""用上面BASE_URL加下面#的Exercise_Input拼接的方法出来的url是错误的，于是报错404"""
# Exercise_Input = "/1/nutrition/natural/exercise"
# url = f"{BASE_URL}{Exercise_Input}"
url = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")
headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": NUTRITION_API_KEY
}

nutrition_data = {
    "query": exercise_text,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
    "gender": GENDER,
}

response_nutrition = requests.post(url, headers=headers, json=nutrition_data)
"""下面这两步，是Gemini建议的好的practice，“职业木工检查木料”"""
# print(response.status_code)
# print(response.text)

result = response_nutrition.json()
# print(result["exercises"][0])


############################################"""Post到Googlesheets"""####################################################

today_Date = datetime.now().strftime("%Y%m%d")
now_Time = datetime.now().strftime("%H:%M:%S")
MY_TOKEN = os.getenv("MY_TOKEN")

bearer_headers = {
"Authorization": f"Bearer {MY_TOKEN}"
}

url = "https://api.sheety.co/11606c60787b571f8e27b01f2aa26aa9/myWorkouts/sheet1"

sheety_data = {
    "sheet1": {
        "date": today_Date,
        "time": now_Time,
        "exercise": result["exercises"][0]["user_input"],
        "duration": result["exercises"][0]["duration_min"],
        "calories": result["exercises"][0]["nf_calories"],
    }
}

response_sheety = requests.post(url, json=sheety_data, headers=bearer_headers)
print(response_sheety)
