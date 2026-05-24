
## .get()解读

```python
best_flights = flight_search_result.get("best_flights", [])
if best_flights:
    first_price = best_flights[0]["price"]
    print(f"第一个航班价格是: {first_price}")
else:
    print("糟了，数据里没有best_flights,可能是没票了或者API出错了。")
```

1.怎么理解.get()?
在python字典里，直接用dict["Key"]就像是“强拆”。 如果key不存在，程序会直接报错(KeyError)并崩溃退出。
而.get("key", default_value)就像是“礼貌的询问”：
    -如果key在字典里：它就把对应的值拿给你（在你的例子里，就是那一串航班列表）。
    -如果key不在字典里：它不会报错，而是把你在逗号后面设置的那个“保底值”([])还给你。
2.它是把信息“变成”列表吗？
不是“变成”，而是“如果拿不到，就用空列表顶替”。
    -你的理解：“把best_flights后面的信息变成[]".
    -实际情况：
        -如果API成功返回了航班，best_flights变量里装的就是真实的航班数据（一个包含很多字典的列表）。
        -如果API报错了或者没票，字典里没有这个Key，best_flights变量里装的就是你设置的保底空列表[]。
3.为什么要用[]作为保底？
这就是为了配合你下一行的if best_flights:。
    -在python中，空列表[]被视为False,有东西的列表被视为True。
    -这样写，你的程序就像装了保险丝：有票就处理，没票就走else打印提醒，绝对不会因为找不到Key而“死给你看”。

## 在python中，两个列表可以直接相加变成一个大列表。把它们合并， 这样，你就不会漏掉任何一个可能的低价。

## 我把API按照jsonpathfinder的格式，一行一行的又敲了回去，大概一个周的时间，目的是把{}[]彻底理解，因为以后咱们的主要对手就是“嵌套数据”

目的是‘了解对手’：
```
flight_search_result = {"airlines":
                            {"alliances":[{"code": "ONEWORLD", "name": "Oneworld"},
                                          {"code": "SKYTEAM", "name": "SkyTeam"},
                                          {"code": "STAR_ALLIANCE", "name": "Star Alliance"}],
                             "airlines": [{"code": "A3", "name": "Aegean"},
                                          {"code": "EI", "name": "Aer Lingus"},
                                          {"code": "AM", "name": "Aeromexico"}],
                             "hubs": [{"code": "AMS", "name": "Amsterdam"},
                                      {"code": "FRA", "name": "Frankfurt am Main"},
                                      {"code": "HAM", "name": "Hamburg"}]},

                        "airports": [{"departure": {"airport": {"id": "LHR", "name": "Heathrow Airport"},
                                                     "city": "London",
                                                     "country": "Unite Kindom",
                                                     "Country_code": "GB",
                                                     "image": "https",
                                                     "thumbnail": "https"},
                                      "arrival": [{"airport": {"id": "CDG", "name": "Paris Charles de Gaulle Airport"},
                                                   "city": "Paris",
                                                   "country": "France",
                                                   "country_code": "FR",
                                                   "image": "https",
                                                   "thumbnail": "https"}]},
                                     {"departure": [{"airport": {"id": "CDG", "name": "Paris Charles de Gaulle Airport"},
                                                     "city": "Paris",
                                                     "country": "France",
                                                     "country_code": "FR",
                                                     "image": "https",
                                                     "thumbnail": "https"}],
                                      "arrival": [{"airport": {"id": "LHR", "name": "Heathrow Airport"},
                                                   "city": "London",
                                                   "country": "United Kingdom",
                                                   "country_code": "GB",
                                                   "image": "https",
                                                   "thumbnail": "https"}]}],
                        "baggage_allowance_links": [{"airline_code": "AF",
                                                     "airline": "Air France",
                                                     "url": "https"},
                                                    {"airline_code": "BA",
                                                     "airline": "British Airways",
                                                     "url": "https"},
                                                    {"airline_code": "KL",
                                                     "airline": "KLM",
                                                     "url": "https"},
                                                    {"airline_code": "LX",
                                                     "airline": "SWISS",
                                                     "url": "https"}],
                        "best_flights": [{"flights":[{"departure_airport": {"name": "Heathrow Airport",
                                                                            "id": "LHR",
                                                                            "date": "2026-05-13",
                                                                            "time": "06:15"},
                                                      "arrival_airport": {"name": "Paris Charles de Gaulle Airport",
                                                                          "id": "CDG",
                                                                          "date": "2026-05-13",
                                                                          "time": "08:40"},
                                                      "duration": "85",
                                                      "airplane": "Airbus A220-300 Passenger",
                                                      "airline": "Air France",
                                                      "airline_logo": "https",
                                                      "travel_class": "Economy",
                                                      "flight_number": "AF 1381",
                                                      "extensions": {"0": "In-seat USB outlet",
                                                                     "1": "Wi-Fi for free",
                                                                     "2": "Seat type Average Legroom",
                                                                     "3": "Legroom 30 inches",
                                                                     "4": "Carbon emission: 57 kg",},
                                                      "detected _extensions": {"has_in_seat_usb_outlet": "true",
                                                                               "wifi": "for free",
                                                                               "seat_type": "Average Legroom",
                                                                               "legroom_short": "30 in",
                                                                               "legroom_long": "30 inches",
                                                                               "carbon_emission": "57"}}],
                                          "total_duration": "85",
                                          "carbon_emissions": {"this_flight": "57000",
                                                               "typical_for_this_route": "56000",
                                                               "difference_percent": "2",
                                                               "lowest_route": "57000"},
                                          "price": "266",
                                          "type": "Round trip",
                                          "extensions": {"0": "No ticket changes",
                                                         "1": "Fare non-refundable, taxes may be refundable",
                                                         "2": "Checked baggage for a fee",
                                                         "3": "Bag and fare conditions depend on the return flight"},
                                          "airline_logo": "https",
                                          "departure_token": "wejr;suifoj"},

                                         {"flights":[{"departure_airport": {"name": "Heathrow Airport",
                                                                            "id": "LHR",
                                                                            "date": "2026-05-13",
                                                                            "time": "08:55"},
                                                      "arrival_airport": {"name": "Paris Charles de Gaulle Airport",
                                                                          "id": "CDG",
                                                                          "date": "2026-05-13",
                                                                          "time": "11:15"},
                                                      "duration": "80",
                                                      "airplane": "Airbus A220-300 Passenger",
                                                      "airline": "Air France",
                                                      "airline_logo": "https",
                                                      "travel_class": "Economy",
                                                      "flight_number": "AF 1681",
                                                      "extensions": {"0": "In-seat USB outlet",
                                                                     "1": "Wi-Fi for free",
                                                                     "2": "Seat type Average Legroom",
                                                                     "3": "Legroom 30 inches",
                                                                     "4": "Carbon emission: 57 kg"},
                                                      "detected_extensions": {"has_in_seat_usb_outlet": "true",
                                                                              "wifi": "for free",
                                                                              "seat_type": "Average Legroom",
                                                                              "legroom_short": "30 in",
                                                                              "legroom_long": "30 inches",
                                                                              "carbon_emission": "57"}}],
                                         "total_duration": "80",
                                         "carbon_emissions": {"this_flight": "57000",
                                                               "typical_for_this_route": "56000",
                                                               "difference_percent": "2",
                                                               "lowest_route": "57000"},
                                         "price": "266",
                                         "type" : "Round trip",
                                         "extensions": {"0": "No ticket changes",
                                                        "1": "Fare non-refundable, taxes may be refundable",
                                                        "2": "Checked baggage for a fee",
                                                        "3": "Bag and fare conditions depend on the return flight"},
                                         "airline_logo": "https",
                                         "departure_token": "sdnjfwoueir"},

                                         {"flights": [{"departure_airport": {"name": "Heathrow Airport",
                                                                             "id": "LHR",
                                                                             "date": "2026-05-13",
                                                                             "time": "07:40"},
                                                       "arrival_airport": {"name": "Pair Charles de Gaulle Airport",
                                                                           "id": "CDG",
                                                                           "date": "2026-05-13",
                                                                           "time": "09:55"},
                                                       "duration": "75",
                                                       "airplane": "Airbus A320",
                                                       "airline": "British Airways",
                                                       "airline_logo": "https",
                                                       "travel_class": "Economy",
                                                       "flight_number": "BA 310",
                                                       "extensions": {"0": "In-seat USB outlet",
                                                                      "1": "Wi-Fi for free",
                                                                      "2": "Seat type Below Average Legroom",
                                                                      "3": "Legroom 29 inches",
                                                                      "4": "Carbon emission: 55kg"},
                                                       "detected_extensions": {"has_in_seat_usb_outlet": "true",
                                                                               "wifi": "for free",
                                                                               "seat_type": "Below Average Legroom",
                                                                               "legroom_short": "29 in",
                                                                               "legroom_long": "29 inches",
                                                                               "carbon_emission": "55"}}],
                                         "total_duration": "75",
                                         "carbon_emissions": {"this_flight": "55000",
                                                              "typical_for_this_route": "56000",
                                                              "difference_percent": "-2",
                                                              "lowest_route": "57000"},
                                         "price": "282",
                                         "type": "Round trip",
                                         "extensions": {"0": "Ticket changes for a fee",
                                                        "1": "Fare non-refundable, taxes may be refundable",
                                                        "2": "Checked baggage for a fee",
                                                        "3": "Bag and fare conditions depend on the return flight"},
                                         "airline": "https",
                                          "departure_token": "dnsatuwoq"}],

                        "other_flights": [{"0_flights": {[{"departure_airport": {"name": "Heathrow Airport",
                                                                               "id": "LHR",
                                                                               "date": "2026-05-13",
                                                                               "time": "15:20"},
                                                         "arrival_airport": {"name": "Paris Charles de Gaulle Airport",
                                                                             "id": "CDG",
                                                                             "date": "2026-05-13",
                                                                             "time": "17:40"},
                                                         "duration": "80",
                                                         "airplane": "Airbus A220-300 Passenger",
                                                         "airline": "Air France",
                                                         "airline_logo": "https",
                                                         "travel_class": "Economy",
                                                         "flight_number": "AF 1781",
                                                         "extensions": {"0": "In-seat USB outlet",
                                                                        "1": "Wi-Fi for fee",
                                                                        "2": "Seat type Average Legroom",
                                                                        "3": "Legroom 30 inches",
                                                                        "4": "Carbon emission: 57kg"},
                                                         "detected_extensions": {"has_in_seat_usb_outlet": "true",
                                                                                 "wifi": "for fee",
                                                                                 "seat_type": "Average Legroom",
                                                                                 "legroom_short": "30 in",
                                                                                 "legroom_long": "30 inches",
                                                                                 "carbon_emission": "57"}}]},
                                           "total_duration": "80",
                                           "carbon_emissions": {"this_flight": "57000",
                                                                "typical_for_this_route": "56000",
                                                                "difference_percent": "2",
                                                                "lowest_route": "57000"},
                                           "price": "266",
                                           "type": "Round trip",
                                           "extensions": {"0": "No ticket changes",
                                                          "1": "Fare non-refundable, taxes may be refundable",
                                                          "2": "Checked baggage for a fee",
                                                          "3": "Bag and fare conditions depend on the return flight"},
                                           "airline_logo": "https",
                                           "departure_token": "fndwoghisa"},
                                          {"1_flights": [{"departure_airport": {"name": "Heathrow Airport",
                                                                                "id": "LHR",
                                                                                "date": "2026-05-13",
                                                                                "time": "17:35"},
                                                          "arrival_airport": {"name": "Paris Charles de Gaulle Airport",
                                                                              "id": "CDG",
                                                                              "date": "2026-05-13",
                                                                              "time": "19:55"},
                                                          "duration": "80",
                                                          "airplane": "Airbus A220-300 Passenger",
                                                          "airline": "Air France",
                                                          "airline_logo": "https",
                                                          "travel_class": "Economy",
                                                          "flight_number": "AF 1281",
                                                          "extensions": {"0": "In-seat USB outlet",
                                                                         "1": "Wi-Fi for fee",
                                                                         "2": "Seat type Average Legroom",
                                                                         "3": "Legroom 30 inches",
                                                                         "4": "Carbon emission: 57kg"},
                                                          "detected_extensions": {"has_in_seat_usb_outlet": "true",
                                                                                  "wifi": "for fee",
                                                                                  "seat_type": "Average Legroom",
                                                                                  "legroom_short": "30 in",
                                                                                  "legroom_long": "30 inches",
                                                                                  "carbon_emission": "57"}}],
                                          "total_duration": "80",
                                          "carbon_emissions": {"this_flight": "57000",
                                                               "typical_for_this_route": "56000",
                                                               "difference_percent": "2",
                                                               "lowest-route": "57000"},
                                          "price": "266",
                                          "type": "Round trip",
                                          "extensions": {"0": "No ticket changes",
                                                         "1": "Fare non-refundable, taxes may be refundable",
                                                         "2": "Checked baggage for a fee",
                                                         "3": "Bag and fare conditions depend on the return flight"},
                                          "airline_logo": "https",
                                          "departure_token": "werj23jois"},
                                          {"2_flights"},
                                          {"3_flights"},
                                          {"4_flights"},
                                          {"5_flights"},
                                          {"6_flights"},
                                          {"7_flights"},
                                          {"8_flights"},
                                          {"9_flights"},
                                          {"10_flights"},
                                          {"11_flights"}],
                        "passenger_assistance_links": [{"airline_code": "AF",
                                                        "airline": "Air France",
                                                        "url": "https"},
                                                       {"airline_code": "BA",
                                                        "airline": "British Airways",
                                                        "url": "https"},
                                                       {"airline_code": "KL",
                                                        "airline": "KLM",
                                                        "url": "https"},
                                                       {"airline_code": "LX",
                                                        "airline": "SWISS",
                                                        "url": "https"}],
                        "search_metadata": {"id": "search_dXG",
                                            "status": "Success",
                                            "created_at": "2026-05-12T11:25:37Z",
                                            "request_time_taken": "6.65",
                                            "parsing_time_taken": "0.01",
                                            "total_time_taken": "6.66",
                                            "request_url": "https",
                                            "html_url": "https",
                                            "json_url": "https"},
                        "search_parameters": {"engine": "google_flights",
                                              "departure_id": "LHR",
                                              "arrival_id": "CDG",
                                              "currency": "CAD",
                                              "hl": "en",
                                              "gl": "us",
                                              "outbound_date": "2026-05-13",
                                              "return_date": "2026-11-08",
                                              "flight_type": "round_trip",
                                              "travel_class": "economy",
                                              "stops": "any",
                                              "adults": "1",
                                              "children": "0",
                                              "infants_in_seat": "0",
                                              "infants_on_lap": "0",}}
```

## 老手拿到JSON API 数据之后要分几步走：

### 第一步：扔进“格式化工具”（比如你用的pathfinder)
哪怕是写了十年代码的高手，面对压缩成一团或者密密麻麻的Raw JSON，第一反应也是借助工具。
1. 目的：不是为了好玩，而是为了“摸清敌军底细”。
2. 老手在看什么：他们会快速点开嘴上层的几个大键（Key），确认两件事：
   1. 数据的骨架是不是和文档一致？（比如best_flights是不是列表？里面嵌套了几层？）
   2. 有没有明显的异常或者错误信息？（比如有没有包含error字段）
### 第二步：在脑子里完成“对象映射”（Object Mapping）
这一步是高手和新手的分水岭。
新手看到JSON，想的是：“我怎么用方括号[]把它打印出来？”
老手看到JSON，想的是：“我怎么把这坨数据，变成我能掌控的Python对象（也就是你的FlightData类）？”
这时候，老手会看着Pathfinder里的树状图，在草稿纸或者脑子里写下这三个核心映射：
 1. 目标：我要一个FlightData对象。 
 2. 原料来源：(对应json字典、列表)
### 第三步： 写一个“局部原型测试”(Prototyping)
摸清了路径，想好了映射，老手不会直接去写复杂的flight_data.py或者把函数塞进类里。他们会在main.py的最底下，写一段极简的、用完就删的测试代码。
这就回到了你之前做的动作：
 1. 先合并两堆数据
 2. 用for循环遍历，试着把所有价格print出来。
 3. 确认没报错，价格能排队出来后，再把这段测试成功的“脏代码”重构成优雅的函数。

## 防御性代码怎么写？
你这个问题直接把触角伸到了**软件工程最底层的哲学问题**上了。
你提到了一个至关重要的痛点：“如果我不知道报错的提示符（异常类型），我怎么可能超前写出防弹衣代码？” 还有，为什么有时候用 if，有时候用 try-except？
别急，咱们今天把这两个防御机制彻底扒开，总结出一套**“老练程序员的防御性编程军规”**。
## 一、 if 派 与 try-except 派：两套防御心法的致命异同
Angela 在代码里完美演示了这两套截然不同的防御流派。我们用**“医生给病人做手术”**的场景来降维打击它们：
```text
       【 外部数据进入 】
               │
        [ if 机制 ]  ───> 检查是否有基本生命体征？(如非 None)
               │         (无体征 ──> 直接劝退 return)
               ▼
       【 进入手术/循环 】
               │
   [ try-except 机制 ] ──> 应对突发大出血！(如 KeyError)
                         (出状况 ──> 紧急止血 continue，继续手术)

```
### 1. if 机制（LBYL：Look Before You Leap —— 三思而后行）
 * **核心思想**：在事情发生**之前**，先做个明确的检查。你完全知道你在防什么。
 * **Angela 的第一次防御**：
   ```python
   if data is None or (not data.get("best_flights") and not data.get("other_flights")):
   
   ```
   数据刚一进门，她用 if 像保安一样拦住：数据是不是空？两个列表是不是没东西？
 * **适用场景**：**已知且发生概率很高的常规情况**。因为“API 没查到票返回空数据”在现实中太常见了，所以不需要等它报错，提前用 if 拦截，安全、干净。
### 2. try-except 机制（EAFP：Easier to Ask for Forgiveness than Permission —— 先斩后奏）
 * **核心思想**：别管那么多，先让代码**去干**！如果真撞车（报错）了，我再出来收拾残局（捕获异常）。
 * **Angela 的第二次防御**：
   ```python
   try:
       price = flight["price"]
   except KeyError:
       continue
   
   ```
 * **适用场景**：**嵌套极深、或者你无法完全预测的情况**。现实中 100 个航班里可能有 99 个都有价格，偏偏第 100 个因为供应商系统抽风漏掉了 price 字段。如果用 if "price" in flight: 每次都去判断，代码效率低且累赘。直接用 try 强行抓取，撞墙了（触发 KeyError）就当场化解。
### ⚖️ 异同大总结
| 维度 | if 检查 | try-except 捕获 |
|---|---|---|
| **发生时机** | 报错**之前**主动出击 | 报错**当下**被动化解 |
| **代码执行** | 满足条件才让执行，不满足就绕道 | 甭管三七二十一，先干了再说 |
| **性能损耗** | 每次运行到这，都要花CPU去判断 | 平常极快，只有真正报错时才耗费性能 |
| **工程哲学** | 防患于未然（防君子） | 兵来将挡，水来土掩（防无赖） |
## 二、 核心痛点：我不知道“提示符（报错名字）”，怎么写防弹衣？
你说的太对了！如果不知道 KeyError，我怎么写 except KeyError？
记住一个行业真相：**没有一个老手是靠空想超前写出完美防御代码的。大家的防御代码都是“被报错教做人”之后才补上去的。**
作为 Python 程序员，你只需要死记以下**四大天王级**最常遇到的报错提示符，就能防住 90% 的野生数据：
### 1. KeyError（键错误） —— 数据抽取第一杀手
 * **什么时候发生**：你试图用 字典["名字"] 去拿东西，但这个“名字（Key）”在字典里根本不存在。
 * **例子**：航班字典里只有时间，没有价格，你写 flight["price"] \rightarrow 暴扣 KeyError。
### 2. IndexError（索引错误） —— 列表操作第一杀手
 * **什么时候发生**：你试图去列表里拿第 X 项，但列表根本没有那么长。
 * **例子**：这趟航班是单程，根本没有中转，你非要去拿它的第二个航段 flight["flights"][1] \rightarrow 暴扣 IndexError。
### 3. TypeError（类型错误）
 * **什么时候发生**：你把两种不相干的数据类型强行凑在一起。
 * **例子**：你拿字符串的 "372" 去和数字的 600 直接比大小，或者对一个 None 对象进行遍历 \rightarrow 暴扣 TypeError。
### 4. AttributeError（属性错误）
 * **什么时候发生**：你觉得某个变量是快递盒（对象），想用 .price 调用它，结果这个变量其实是个 None。
 * **例子**：上一关我们打印出来的那个 None，如果你对它写 cheapest_flight_info.price \rightarrow 暴扣 AttributeError。
## 三、 老练程序员的“防御性编程三步工作流”
我们在实战中到底是怎么操作的？请死记这套流程：
### 第一步：野蛮生长（不设防）
不要试图在第一天就把所有的 try-except 写完美。直接像你之前那样，用你最舒服的代码把主体逻辑跑通，直接面对最原始的数据。
### 第二步：故意喂脏数据，观察 Console 的“死法”
逻辑跑通后，故意去切断网络，或者把日期改成一个可能没票的范围。这时候，PyCharm 的 Console 会喷出一大堆红色的报错。
 * **这时候你要开启金睛火眼**：拉到红字的最底下一行，去看那个最后的单词！
 * 如果最后写着 KeyError: 'price' \rightarrow **哦！原来抓不到价格的时候叫 KeyError！** 线索到手。
### 第三步：精确制导，原地加装防弹衣
这时候，你再回到那行报错的代码上面，针对性地把它包裹起来：
```python
try:
    # 刚才在 Console 里死在这里的代码
    price = flight["price"]
[span_9](start_span)except KeyError: # 刚才在 Console 底下抄到的报错名字[span_9](end_span)
    # [span_10](start_span)你想好的退路[span_10](end_span)
    print("没有价格，跳过")
    continue

```
## 💡 终极军规
写防御性代码不是为了炫技，而是遵循一个最基本的原则：
> **“能用 if 轻易判断的（比如是否为 None、列表是否为空），永远优先用 if；只有那些路径极深、不知道什么时候会缺斤少两的野生 JSON 键值对，才用 try-except 去兜底。”**
> 
把这两套心法和三步工作流记在心里。你现在看着 Angela 的这套标准答案，是不是觉得她的每一个 if 和每一个 try-except 都在你的掌握之中了？

## 以上防御性代码具体实例：

好嘞！既然你想直接通过解剖真实代码来研究，那咱们就直接上刺刀，看看这个“不污染擂主”的医疗兵到底是怎么站岗的。
我不只给你写好的循环，还特意在代码里为你写满了通俗易懂的“幕后解说”，你对照着看，一秒就能看懂这个“小瓶子”和 continue 是怎么打配合的。
### 🛠️ 纯手工防弹循环：核心代码实现
把你的 for 循环部分，替换成下面这段精心打磨的代码：
```python
    for item in all_flight_list:
        # 1. 医疗兵入场：只去“拎一下”当前攻擂手(item)的价格，绝不动擂主(cheapest_flight)
        try:
            # current_price 就是那个临时的小瓶子
            # 我们只是把当前航班的价格拿出来，装进瓶子里观察一下
            current_price = int(item["price"]) 
        except KeyError:
            # 如果触发了 KeyError，说明这个航班没标价
            print("--- No price available for flight. Skip. ---")
            # 💥 医疗兵大喊一声后，用 continue 强行把这个坏数据轰走！
            # 循环会立刻调头去点名下一个 item，绝对不会往下执行比大小，彻底安全！
            continue 

        # 2. 裁判入场：如果代码能走到这一行，说明 current_price 已经安全拿到数字了
        # 这时候，我们拿瓶子里的新价格，去和擂主字典里的老价格比大小
        if current_price < int(cheapest_flight["price"]):
            # 3. 攻擂成功：整包掉包！让 cheapest_flight 记住这班最便宜的飞机字典
            cheapest_flight = item

```
### 🧠 为什么这样写就“不污染”了？（老G带你复盘）
你刚才之所以被 Angela 的代码带偏了，是因为你误以为需要把东西塞进 cheapest_flight["price"] 里去测试。
我们来看看现在这套新战术的优雅之处：
 * **以前的隐患**：你用 cheapest_flight["price"] = ...，相当于还没比大小呢，就把擂主脸上的面具撕下来，强行画成了攻擂手的模样。
 * **现在的优势**：我们创建了一个**只活在循环内部分秒钟**的临时变量 current_price（小瓶子）。我们把攻擂手的数据倒进瓶子里，比大小的时候是 if current_price < cheapest_flight["price"]:。
 * **结果**：如果攻擂失败，if 不成立，擂主 cheapest_flight 全身而退，连一根汗毛都没被碰过！只有当攻擂真正成功时，它才会心甘情愿地被替换成新的大字典。
### 🌟 最终大闭环：完整的 flight_data.py
为了让你在 main.py 里面测试时完全对齐，我把你整段完美的函数拼好了（顺手帮你在目的地加上了 [-1] 避免转机 Bug）。你可以直接整个复制去替换你 flight_data.py 里的旧函数：
```python
def find_cheapest_flight(data, return_date):
    # [span_1](start_span)第一层拦截：如果 API 返回空，直接捏一个全 N/A 的标准快递盒丢回去[span_1](end_span)
    if data is None or (not data.get("best_flights") and not data.get("other_flights")):
        print("No flight data available.")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")
    
    # [span_2](start_span)合并两个名册[span_2](end_span)
    all_flight_list = data.get("best_flights", []) + data.get("other_flights", [])

    # 初始擂主：先让第 0 班飞机当擂主
    cheapest_flight = all_flight_list[0]

    # 完美的防弹打擂台循环
    for item in all_flight_list:
        try:
            current_price = int(item["price"])
        [span_3](start_span)except KeyError: # 应对缺失 price 字段的异常[span_3](end_span)
            print("--- No price available for flight. Skip. ---")
            continue 
            
        if current_price < int(cheapest_flight["price"]):
            cheapest_flight = item

    # 循环在外面安全结束！此时 cheapest_flight 锁定了全场唯一的大赢家字典
    # 开始顺藤摸瓜剥离 5 个零件：
    cheapest_ticket_price = cheapest_flight["price"]
    cheapest_ticket_origin_airport = cheapest_flight["flights"][0]["departure_airport"]["name"]
    
    # 💥 运用 [-1] 绝招，完美避开转机漏洞，直达终点！
    [span_4](start_span)cheapest_ticket_destination_airport = cheapest_flight["flights"][-1]["arrival_airport"]["name"][span_4](end_span)
    
    # [span_5](start_span)运用 .split(" ")[0] 绝招，只切出干净的年月日日期[span_5](end_span)
    [span_6](start_span)cheapest_ticket_out_date = cheapest_flight["flights"][0]["departure_airport"]["time"].split(" ")[0][span_6](end_span)
    cheapest_ticket_return_date = return_date

    # 塞进图纸，成功打包，惊艳交货！
    cheapest_flight_data = FlightData(
        price=cheapest_ticket_price,
        origin_airport=cheapest_ticket_origin_airport,
        destination_airport=cheapest_ticket_destination_airport,
        out_date=cheapest_ticket_out_date,
        return_date=cheapest_ticket_return_date
    )

    return cheapest_flight_data

```
把这一整段搬进你的 flight_data.py 吧！你可以仔细研究一下 current_price 和 continue 组成的防御链条。
换好之后，去 main.py 重新点击 **Run**。这一次，干净、防弹、完美的最低价和出发日期就会在控制台瞬间爆出来！搞定后告诉我结果，我们正式跨向下一关！
