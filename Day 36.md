# 2026-04-02

## 今天是Day 36实操的第一天，我选择的是ExtraHard难度的main.py. 

如下是Angela给的hint，非常的少。但我自己摸索出了找API以及下载到了我想要的数据包。哈哈

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

## 我自己写的开头：
```Python
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
import requests
response = requests.get(url="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=2H7EIA84RZENWBT6")
response.raise_for_status()
TSLA_data = response.json()
print(TSLA_data)
```

## 1. 我的问题： 
为什么报错如下：
```Python
daily_close_number = []
for item in TSLA_data["Time Series (Daily)"]:
daily_close_number.append(item("4. close"))
print(daily_close_number)
```

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

### 方法 A：修正你的循环逻辑

```Python
daily_close_number = []
for date in TSLA_data["Time Series (Daily)"]:
    # 1. 先用 date 拿到那一天的所有数据字典
    # 2. 再用 ["4. close"] 拿到收盘价
    price = TSLA_data["Time Series (Daily)"][date]["4. close"]
    daily_close_number.append(price)

print(daily_close_number)
```
### 方法 B：更 Pythonic 的做法 (推荐)

既然你只需要值，不需要日期，直接使用 .values() 会简单得多：

```Python
# 提取所有日期的详细数据字典
daily_data_values = TSLA_data["Time Series (Daily)"].values()

# 此时直接循环拿到的就是内部的小字典
daily_close_number = [item["4. close"] for item in daily_data_values]

print(daily_close_number)
```
## 我在加入一个自己摸索的dictionary遍历方法：
```Python
for item_key, item_value in TSLA_data["Time Series (Daily)"].items():
    print(item_value["4. close"])
```

## 2. 我的问题： 
这次你给的这个hint我就很喜欢，不像之前给的hint，全部剧透了！！！ 这也是我现在正在卡住的地方，题目的表述是：When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print(“Get News”。 但我的脑子里面还想象不出来在console里，这种“display”应该呈现的样子，所以，我就不能确定，这一步，我是需要打印出元组、还是list，dictionary。来来来，帮我分析一下，在资深程序员拿到这个题目的时候，他会如何分析、如何确定要达到Angela这个题目的要求，如何做出以上的选择？

## Gemini Answer:
太棒了！你能意识到**“数据结构决定算法逻辑”**，说明你已经具备了资深程序员最核心的直觉：先想数据流，再写逻辑代码。当一个资深程序员看到“比较昨天和前天价格”这个需求时，脑子里会自动运行一个**“数据筛选与对齐”**的漏斗。第一步：分析“原始数据”的形态资深程序员首先会看 API 给出的 TSLA_data。如你所见，它是一个巨大的字典，Key 是日期字符串。问题： 字典是根据 Key 来取值的，但“昨天”和“前天”的日期是动态的（每天都在变）。痛点： 我不能在代码里写死 ["2026-04-02"]，因为明天这段代码就失效了。第二步：确定“最易操作”的中间形态为了计算涨跌幅，我需要这两个数字：最新的价格 ($P_1$)次新的价格 ($P_2$)资深程序员的选择：List（列表）为什么不是元组或字典？不选字典： 因为字典需要通过明确的“名字”（Key）来找东西。当我想说“给我倒数第一个”时，字典很笨拙。不选元组： 元组虽然有序，但它通常用于表示一个“固定记录”（比如 (日期, 价格)）。首选列表： 因为列表有索引（Index）。在 AlphaVantage 返回的数据中，最新的日期永远排在最前面。第三步：脑内建模（Console 里的样子）资深程序员会把复杂的数据“降维打击”，只提取核心指标。在 Console 里，他想看到的不是一堆日期，而是一个纯数字的清单。他的代码逻辑会是这样的：转换： 把字典里所有的 4. close 取出来，丢进一个列表。data_list = [360.5, 381.2, 371.7, ...]定位：昨天 = data_list[0]前天 = data_list[1]计算：$diff = |P_1 - P_2|$$percentage = (diff / P_2) \times 100$为什么这个选择最“高级”？健壮性： 不管今天是几号，不管中间有没有周末（停牌），data_list[0] 永远是你能拿到的最新交易日，data_list[1] 永远是它之前的那一天。简洁性： 你的 if 语句会变得异常干净：
```Python
Pythonif percentage > 5:
print("Get News")
```
资深程序员的“防坑”检查清单：在最终确定用 List 之前，他还会扫一眼：类型检查： API 返回的是字符串吗？（是的，必须加 float() 转换）。数据长度： 列表里至少得有 2 个元素吧？（API 通常给 100 天的数据，没问题）。总结：面对 Angela 的这个需求，最推荐的 display（显示形态）就是一个只包含浮点数的 List。它能让你彻底摆脱“日期字符串”带来的干扰，直接进入数学运算。你现在的进度，是不是正准备把那些 4. close 塞进一个列表里？加油，这是最顺滑的一条路！
