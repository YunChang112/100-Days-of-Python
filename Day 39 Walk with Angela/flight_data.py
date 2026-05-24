
class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

def find_cheapest_flight(data, return_date):
    '''
    这里面是当时在main.py里面收到flight_search.py里面穿进来的json数据之后，制作的原始数据模型。跑通之后，再放在这里开始组装。
    # pprint(flight_search_result)
    # json_string = json.dumps(flight_search_result, indent=2)
    # print(json_string)

    # price_list = flight_search_result.get("best_flights",[])
    # for item in price_list:
    #     price = item["price"]
    #     print(price)

    下面这个思路是我自己想出来的，但问题是，只能选出最小票价，但不能把最小票价对应的航班其他信息一并揪出来，于是就采取了Gamini最初的建议。
    all_flight_price_list = []

    best_flights_price_list = data.get("best_flights", [])
    for item in best_flights_price_list:
        all_flight_price_list.append(item["price"])

    other_flights_price_list = data.get("other_flights", [])
    for item in other_flights_price_list:
        all_flight_price_list.append(item["price"])

    print(all_flight_price_list)

    '''

    if data is None or (not data.get("best_flights") and not data.get("other_flights")):
        print("No flight data")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A" )

    all_flight_list = data.get("best_flights", []) + data.get("other_flights", [])

    cheapest_flight = all_flight_list[0]

    for item in all_flight_list:
        try:
            current_price = int(item["price"])
        except KeyError:
            print("---No price available for flight. ---")
            continue

        if current_price < int(cheapest_flight["price"]):
            cheapest_flight = item

    cheapest_ticket_price = cheapest_flight["price"]
    cheapest_ticket_origin_airport = cheapest_flight["flights"][0]["departure_airport"]["name"]
    cheapest_ticket_destination_airport = cheapest_flight["flights"][-1]["arrival_airport"]["name"]
    cheapest_ticket_out_date = cheapest_flight["flights"][0]["departure_airport"]["time"].split(" ")[0]
    cheapest_ticket_return_date = return_date

    cheapest_flight_data = FlightData(
        price=cheapest_ticket_price,
        origin_airport=cheapest_ticket_origin_airport,
        destination_airport=cheapest_ticket_destination_airport,
        out_date=cheapest_ticket_out_date,
        return_date=cheapest_ticket_return_date
    )

    return cheapest_flight_data