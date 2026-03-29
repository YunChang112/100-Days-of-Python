import smtplib
import datetime as dt
import random


# ----------------------------------------------Automate Email Sending--------------------------------------------------
# my_email = "yunchang535@gmail.com"
# password = "vnbwwlfyeuqbbcia"

# connection = smtplib.SMTP("smtp.gmail.com", port=587)
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs="changyun535@icloud.com", msg="Hello")
# connection.close()

# Gemini 帮助解决问题，但还是不能发邮件。
# # 使用 587 端口
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     try:
#         connection.login(user=my_email, password=password)
#         # 加上 Subject，防止被 Google 拒收
#         connection.sendmail(
#             from_addr=my_email,
#             to_addrs="changyun535@icloud.com",
#             msg="Subject:Test\n\nThis is a test message."
#         )
#         print("Success! 邮件已发送。")
#     except smtplib.SMTPAuthenticationError:
#         print("认证失败：请检查 App Password 是否正确，或空格是否已删除。")

# ---------------------------------------------Random Quote Selection---------------------------------------------------

MY_EMAIL = "abc@gmail.com"
MY_PASSWORD = "abcd"

"""我自己写的，结果看到Angela的答案，发现不需要.strip。"""
# with open ("quotes.txt") as file:
#     data = file.readlines()
# quote_list = [row.strip() for row in data]
# # print(type(quote_list))
# # print(quote_list[0])

now = dt.datetime.now()
weekday=now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gamil.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Tuesday Motivation\n\n{quote}"
        )





# import datetime as dt
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1985, month=3, day=17, hour=4)
# print(date_of_birth)