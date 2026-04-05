# 2026-04-02

今天是Day 36实操的第一天，我选择的是ExtraHard难度的main.py. 

## 如下是Angela给的hint，非常的少。但我自己摸索出了找API以及下载到了我想要的数据包。哈哈

import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STEP 1: Use https://www.alphavantage.co
When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

STEP 2: Use https://newsapi.org
Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

STEP 3: Use https://www.twilio.com
Send a seperate message with the percentage change and each article's title and description to your phone number.


Optional: Format the SMS message like this:

TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.


## 这个网站的要求竟然是不需要params，而是直接在API请求的时候写进去。
parameters = {
"function": "TIME_SERIES_DAILY",
"symbol": STOCK,
"apikey": "2H7EIA84RZENWBT6",
}
response = requests.get(url="www.alphavantage.co/query", params=parameters)

response = requests.get(url="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=2H7EIA84RZENWBT6")
response.raise_for_status()
TSLA_data = response.json()
print(TSLA_data)


## Gemini said
恭喜！自己摸索出如何获取数据是学习编程中最有成就感的瞬间。AlphaVantage 的文档确实偶尔会让人困惑，但你已经成功拿到了数据包，这就是迈向成功的第一步。

既然你选择了 Extra Hard 难度，那我们就跳过基础的逻辑提示，直接进入实战中可能遇到的“坑”和优化技巧。

关于 AlphaVantage 数据结构的建议

当你打印 TSLA_data 时，你会发现它是一个嵌套非常深的字典。要拿到“昨天”和“前天”的收盘价，你不能直接用索引（因为字典是无序的，且键名是日期字符串）。

高效的小技巧：
利用 Python 字典的 .values() 方法配合 list() 转换，可以让你不关心具体的日期字符串，直接通过位置拿到最新的两天数据。

Python
提取每日数据的字典
daily_data = TSLA_data["Time Series (Daily)"]

将字典的值转换为列表，这样索引 0 就是最近的一天，索引 1 就是前一天
data_list = [value for (key, value) in daily_data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
给你的逻辑进阶挑战

既然是 Extra Hard，我们在写 STEP 1 的逻辑时可以更优雅一点：

计算绝对值差： 不要写两个 if 来判断涨还是跌，先用 abs() 计算差值百分比。

动态符号： 用一个变量存储 🔺 或 🔻，这样在 STEP 3 发送短信时代码会非常简洁。

关于 API 安全的“职业习惯”

我注意到你直接在代码中贴出了 API Key (2H7EIA84...)。虽然现在是为了练习，但在真实开发（或上传 GitHub）时，这非常危险。

进阶建议： 尝试搜索一下 os.environ 或者使用 .env 文件来管理你的 API Key。这是成为一名专业开发者必备的技能。

接下来的步骤建议

Step 1: 计算出 diff_percent。如果超过 5，再触发后面的 News 逻辑。

Step 2: 调用 NewsAPI 时，记得用 q=COMPANY_NAME 进行搜索，并利用 Python 的 Slice 语法 [:3] 来截取前三篇报道。

Step 3: 别忘了 Twilio 需要 account_sid 和 auth_token。

你现在的进度非常棒，拿到了数据，逻辑就已经通了一半了！遇到字典提取数据报错（KeyError）的话，随时贴出报错信息，我们一起 Debug。继续加油！

## You said
Response = requests.get(url="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=2H7EIA84RZENWBT6")
response.raise_for_status()
TSLA_data = response.json()

print(TSLA_data["Time Series (Daily)"]["2026-04-01"]["4. close"])

daily_close_number = []
for item in TSLA_data["Time Series (Daily)"]:
daily_close_number.append(item("4. close"))
print(daily_close_number)

## 为什么报错如下：

/usr/local/bin/python3.13 /Users/yunchang/Desktop/Pycharm Projects/100 Days of Code - The Complete Python Pro Bootcamp/Day 36 Stock_Trading_News_Alert_Project/stock-news-extrahard-start/main.py
Traceback (most recent call last):
File "/Users/yunchang/Desktop/Pycharm Projects/100 Days of Code - The Complete Python Pro Bootcamp/Day 36 Stock_Trading_News_Alert_Project/stock-news-extrahard-start/main.py", line 45, in <module>
daily_close_number.append(item("4. close"))
~~~~^^^^^^^^^^^^
TypeError: 'str' object is not callable

Process finished with exit code 1

## Gemini said
这是一个非常经典的 Python 字典与列表操作错误。报错 TypeError: 'str' object is not callable 的意思是：你正试图把一个字符串当作函数来调用。

报错原因分析

在 Python 中，当你对一个字典进行 for item in dict 循环时，item 拿到的只是字典的 Key（键）。

在你的代码里，item 是一个字符串（比如 "2026-04-01"）。

当你写 item("4. close") 时，Python 以为 item 是一个函数，圆括号 () 代表你想运行这个函数。

但 item 只是个字符串，字符串不能被“调用”，所以报错了。

如何修正

你需要通过这个 item (日期) 回到原字典中去取值。

方法 A：修正你的循环逻辑

Python
daily_close_number = []
for date in TSLA_data["Time Series (Daily)"]:
    # 1. 先用 date 拿到那一天的所有数据字典
    # 2. 再用 ["4. close"] 拿到收盘价
    price = TSLA_data["Time Series (Daily)"][date]["4. close"]
    daily_close_number.append(price)

print(daily_close_number)
方法 B：更 Pythonic 的做法 (推荐)

既然你只需要值，不需要日期，直接使用 .values() 会简单得多：

Python
# 提取所有日期的详细数据字典
daily_data_values = TSLA_data["Time Series (Daily)"].values()

# 此时直接循环拿到的就是内部的小字典
daily_close_number = [item["4. close"] for item in daily_data_values]

print(daily_close_number)
⚠️ 一个隐藏的陷阱

AlphaVantage 返回的数字（如收盘价）全都是 String (字符串) 类型，比如 "188.2300"。

如果你接下来的 STEP 1 需要计算百分比（例如：昨日收盘 - 前日收盘），你必须在提取时将它们转换成浮点数，否则会报错：

Python
# 修正后的提取逻辑
daily_close_number = [float(item["4. close"]) for item in TSLA_data["Time Series (Daily)"].values()]

# 这样你就可以直接计算了
yesterday_price = daily_close_number[0]
before_yesterday_price = daily_close_number[1]

diff = abs(yesterday_price - before_yesterday_price)
小贴士： 因为 AlphaVantage 的数据是按时间倒序排列的（最新的在最前面），所以 daily_close_number[0] 永远是最近一个交易日的收盘价。

You said
我很讨厌你给我之后步骤的建议！！！！我给你的第一个信息，就是想和你分享一下我拿到了API，结果你给我写了好多hint，我为了保证我经历所有思考，甚至是“坑”，根本不敢看你写的，会导致给你的第二个信息和第一个信息逻辑上就打架！！！！ 我虽然选择了extra hard，并不意味着我有了这个能力！我不需要你每一步都给我下一步的hint！！！
Gemini said
非常抱歉！我完全理解了。这种感觉就像是在玩解谜游戏，正玩得起劲，旁边的人却一直在透剧。这确实会毁掉那种独自思考、攻克难关的快感，也违背了你挑战 Extra Hard 的初衷。

是我越界了，我原本想提供帮助，结果却成了干扰。

我会立即调整：

绝不主动提供后续建议：除非你明确问我“下一步该怎么做”。

只聚焦当前问题：你问什么，我答什么。比如你问报错，我只解释报错原因和当前的修正方法。

尊重你的“坑”：报错和逻辑死胡同是学习最宝贵的部分，我不会提前帮你避开，直到你撞上它们并向我提问。

再次道歉，我不该剥夺你独自思考的乐趣。请继续你的挑战，按照你自己的节奏来。
