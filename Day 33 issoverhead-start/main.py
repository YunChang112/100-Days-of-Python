import requests
from datetime import datetime
import smtplib
import time
import math

MY_EMAIL = "changyun535@icloud.com"
MY_PASSWORD = "wkofehdctrwjbtis"

# MY_LAT = 49.282730 # Your latitude
# MY_LONG = -123.120735 # Your longitude

# Tokyo
MY_LAT = 35.689487
MY_LONG = 139.691711

observer_list = ["chyywhcg@gmail.com", "chyywhcg@hotmail.com"]

def calculate_distance(lat1, lon1, lat2, lon2):
    deg_to_km_lat = 111
    deg_to_km_lon = 72

    dx = (lat1 - lat2) * deg_to_km_lat
    dy = (lon1 - lon2) * deg_to_km_lon
    return math.sqrt(dx**2 + dy**2)

def get_iss_data():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_lat = float(data["iss_position"]["latitude"])
    iss_lon = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    is_overhead = MY_LAT - 5 < iss_lat < MY_LAT + 5 and MY_LONG - 5 < iss_lon < MY_LONG + 5

    dist = calculate_distance(MY_LAT, MY_LONG, iss_lat, iss_lon)

    return is_overhead, iss_lat, iss_lon, dist

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        "tzid": "America/Vancouver"
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    return time_now.hour < sunrise or time_now.hour > sunset


while True:
    overhead, current_lat, current_lon, distance = get_iss_data()
    current_time = is_night()

    # 计算预计到达时间 （ISS 速度约 7.66 km/s = 460 km/min)
    eta_min = distance / 460

    if overhead and current_time:
        print(f"ISS detected! Coordinates: ({current_lat}, {current_lon}) Dist: {distance:.2f}km. Sending notifications...")
        for recipient in observer_list:
            try:
                with smtplib.SMTP("smtp.mail.me.com", 587) as connection:
                    connection.starttls()
                    connection.login(MY_EMAIL, MY_PASSWORD)
                    connection.sendmail(
                        from_addr=MY_EMAIL,
                        to_addrs=recipient,
                        msg=f"From: {MY_EMAIL}\nTO: {recipient}\nSubject:ISS Tracker Update\n\nThe ISS is at Lat: {current_lat}"
                            f"Lon:{current_lon} and it is above you in the sky. Look Up!"
                    )
            except Exception as e:
                print(f"Error connecting to iCould: {e}")
        time.sleep(300)
    else:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Monitoring... "
              f"ISS Current Location: Lat {current_lat}, Lon {current_lon}"
              f"Dist: {distance:7.2f} km | ETA: {eta_min:4.1f} min")
    time.sleep(60)

