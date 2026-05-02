## Logic Design (看最后)

虽然把API成功扒下来了，但成功的喜悦立马被不知道下一步该干什么给浇灭了！于是痛下决心，要把Day 39的整个Flow chart给来个最专业的大包。于是和
Gemini沟通，让他给了我最专业的程序要应该有的思考过程，他还给了我一个彩蛋，即mermaid语法，把一行flowchart内容，GitHub自动渲染成结构图。

## Dictionary Comprehension Nailed Down

```python
# 假设 flight_data 是通过 json.load() 读取的原始数据
clean_dict = {row["iataCode"]: row["lowestPrice (usd)"] for row in flight_data["sheet1"]}

print(clean_dict)
# 预期输出：{'NRT': 500, 'KEF': 500}
```

## 逻辑解析
1、for row in flight_data["sheet1"]: 告诉Python去哪里找原始列表（送料口）
2、row["iataCode"]: row["lowestPrice(usd)"]: 定义了谁是“钥匙”（key）， 谁是“宝藏”（Value）（加工模具）
3、{...}: 这是“生长”的边界，将所有映射关系封装进一个Dictionary

## 今天掌握了从clean_dictionary通过for循环 + items()传参的招数 以及 动态更改不同目的地cache_file的本领。如下：
```Python

for city_code, target_price in iata_and_price.items():

    departure_destination = "YVR"
    arrival_destination = city_code
    Outbound_date = "2026-04-27"
    Return_date = "2026-05-04"
    file_name = f"cache_{city_code}.json"


    url = "https://www.searchapi.io/api/v1/search"
    params = {
        "engine": "google_flights",
        "flight_type": "round_trip",
        "departure_id": departure_destination,
        "arrival_id": arrival_destination,
        "outbound_date": Outbound_date,
        "return_date": Return_date,
        "api_key": API_Key
    }
```

## 今天意识到了for循环的结果与print、以及之后的遍历结果，取决于indnet的对不对！！！

## 2026年5月1号，距离2025年5月31号签下的Python百天学习还有一个月就一年了！终于，在今天写出了第一个联通OOP内部的一个小脚本！但感觉超级棒！
已完成DataManager与FlightSearch的类的封装，实现了main.py的逻辑调度。

```mermaid
graph TD
    A[开始] --> B{是否有本地缓存?}
    B -- 是 --> C[读取 JSON 文件]
    B -- 否 --> D[调用 SerpApi]
    D --> E[保存数据到本地]
    C --> F[解析价格数据]
    E --> F
    F --> G[结束]