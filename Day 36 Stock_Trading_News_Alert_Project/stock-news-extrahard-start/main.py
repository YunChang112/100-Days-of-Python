## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

"""
这个网站的要求竟然是不需要params，而是直接在API请求的时候写进去。
# parameters = {
#     "function": "TIME_SERIES_DAILY",
#     "symbol": STOCK,
#     "apikey": "2H7EIA84RZENWBT6",
# }
# response = requests.get(url="www.alphavantage.co/query", params=parameters)
"""
import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

response_stock = requests.get(url="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=2H7EIA84RZENWBT6")
response_stock.raise_for_status()
TSLA_data = response_stock.json()

response_news = requests.get(url="https://newsapi.org/v2/everything?q=tesla&from=2026-03-07&sortBy=publishedAt&apiKey=be68359227634ed7bdfd4ea8390e551b")
response_news.raise_for_status()
TSLA_news = response_news.json()

News_list = []
for item in TSLA_news["articles"]:
    News_list.append(item["description"])

Closing_data = []
for item in TSLA_data["Time Series (Daily)"].values():
    Closing_data.append(float(item["4. close"]))

"""这里是Angela视频中用到的一个List Comprehension，不同的思路。
# Closing_data = [value for (key, value) in TSLA_data["Time Series (Daily)"].items()]
"""

Day_0 = Closing_data[0]
Day_1 = Closing_data[1]

if abs((Day_0 - Day_1)/Day_1) > 0.05:
    print("Yes")
    # print(News_list[:3])
else:
    print("None")



"""以下，是使用for loop遍历最基本的方式， 在dictionary中去到想要的value的方法。下面的第一二行，#的两行，是我第一次按照我自己的想法来遍历的，
我现在已经了解了为什么这样不行，因为这只能便利出key，即item出来的是那些日期。所以，要把item()再带回公式，才能便利出value。
# for time in TSLA_data["Time Series (Daily)"]:
#     print(item["4. close"]

for item in TSLA_data["Time Series (Daily)"]:
    print(TSLA_data["Time Series (Daily)"][item]["4. close"])
"""

"""
以下是直接取value，即我最原始的想法，在上面的“最基本的方式”中添加.value()，来呈现。
for item in TSLA_data["Time Series (Daily)"].values():
    print(item["4. close"])
"""

"""
以下，是把字典也遍历出来，即上面两个只便利出来value，下面的遍历结果是把key：value这个键值对也一并弄出来。
for item_key, item_value in TSLA_data["Time Series (Daily)"].items():
    # daily_closing_data = {item_key: item_value["4. close"]} : 打印出来的是“字典”
    # daily_closing_data = {item_key， item_value["4. close"]} : 打印出来的是“集合”，注意中间没有“冒号：”，用的是哈希表发，所以无序
    # daily_closing_data = item_key, item_value["4. close"] ： 打印出来的是“元组”
    # daily_closing_data = (item_key, item_value["4. close"]) ： 打印出来的是“元组”
    print(daily_closing_data)
"""



