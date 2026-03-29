##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = "changyun535@icloud.com"
MY_PASSWORD = "wkofehdctrwjbtis"

# --------------------------------------------1. Update the birthdays.csv-------------------------------------------------------------------------------------------
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}

now = dt.datetime.now()
month = now.month
day = now.day
birthday_check = (month,day)
if birthday_check in birthdays_dict:
    birthday_person = birthdays_dict[birthday_check]
    letter_picked = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(letter_picked) as f:
        data = f.read()
        letter_with_name = data.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.mail.me.com", 587) as connection:
        connection.starttls()
        print(f"Logging in as: {MY_EMAIL}")
        print(f"Sending from: {MY_EMAIL}")
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            # to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!!!\n\n{letter_with_name}"
        )
