MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

units = {
    "water": "ml",
    "milk": "ml",
    "coffee": "g",
}


def make_drink(user_choice, menu, resources_needed):
    ingredients = menu[user_choice]["ingredients"]
    for item1, needed in ingredients.items():
        if resources_needed.get(item1, 0) < needed:
            print(f"Sorry there is not enough {item1}.")
            return False

    for item1, needed in ingredients.items():
        resources_needed[item1] -= needed

    # return True


def make_transaction(user_inserted_amount, coffee_cost_required):
    """这个函数是用来比较用户投入的钱数与所选咖啡价格以及当用户输入的钱数大于所选咖啡价格，return差价"""
    if user_inserted_amount < coffee_cost_required:
        print("Sorry that's not enough money. Money refunded.")
        return False

    return user_inserted_amount - coffee_cost_required



coffee_profit = 0

continue_order = True

while continue_order:

    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == "report":
        for item, amount in resources.items():
            unit = units [item]
            print(f"{item.title()}: {amount}{unit}")
        print(f"Money: ${coffee_profit}")
        # break
        # exit()
        continue

    if user_input == "off":
        # exit()
        continue_order = False

    else:
        make_drink(user_input, MENU, resources)

        quarters_inserted = int(input("Please insert coins. \nHow many quarters?: "))
        dimes_inserted = int(input("How many dimes: "))
        nickles_inserted = int(input("How many nickles: "))
        pennies_inserted = int(input("How many pennies "))

        total_coins_inserted = quarters_inserted * 0.25 + dimes_inserted * 0.1 + nickles_inserted * 0.05 + pennies_inserted * 0.01
        coffee_cost = MENU[user_input]["cost"]

        change_to_user = make_transaction(total_coins_inserted, coffee_cost)

        coffee_profit += MENU[user_input]["cost"]

        print(f"Here is ${change_to_user:.2f} in change. ")
        print("Here is your coffee. Enjoy! ")


# 以上问题：
# 1：还没投币，材料已经扣减了





# 以下是原稿，包括思考过程

# def make_drink(user_choice, menu, resources_needed):
#     # 这里面的MENU、resources应该是形参，而不是实参吧？所以我在这里用MENU是不对的？ 确认一下。GPT给的是menu，那它不知道resources被引用了？？？
#     """制作一杯饮品，够料就扣库存并返回True；不够料则不改库存并返回False"""
# # 我现在从GPT抄下了这个函数的样子，它放进去了三个形参，我明白这是把三个变量放进去，要通过这个函数导出一个结论，结论就在下面的“”“ ”“”里面。
# # 但我现在的问题是，就算告诉了我这个过程，但我也是想不出来这中间的流水线如何设计？？？？？？
# # 我觉得我现在的问题就是卡在了，如何从这两个dictionary中同时抽取相同key的方法！！！！！！别急，再让我想想。
# # 函数的职责：返回True/False（让主程序决定怎么做）
#
#     ingredients = menu[user_choice]["ingredients"]
#
#     # for item2 in ingredients:
#     #     if ingredients[item2] >= resources[item2]:
#     #         print(f"Sorry there is not enough {item2}.")
#     #         return False
#
#     for item1, needed in ingredients.items():
#         if resources_needed.get(item1, 0) < needed:
#             print(f"Sorry there is not enough {item1}.")
#             return False
#
#     for item1, needed in ingredients.items():
#         resources_needed[item1] -= needed
#
#     # return True
#
#
# def make_transaction(user_inserted_amount, coffee_cost_required):
#     """这个函数是用来比较用户投入的钱数与所选咖啡价格以及当用户输入的钱数大于所选咖啡价格，return差价"""
#     if user_inserted_amount < coffee_cost_required:
#         print("Sorry that's not enough money. Money refunded.")
#         return False
#
#     return user_inserted_amount - coffee_cost_required
#
#
# # TODO: 1 打印report + Money???
#
# coffee_profit = 0
#
# continue_order = True
#
# while continue_order:
#
#     user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
#
#     if user_input == "report":
#         for item, amount in resources.items():
#             unit = units [item]
#             print(f"{item.title()}: {amount}{unit}")
#         print(f"Money: ${coffee_profit}")
#         # break
#         # exit()
#         continue
#
#     if user_input == "off":
#         # exit()
#         continue_order = False
#         # 为什么这个不能用，因为只是赋值，程序还会继续向下进行。在gpt的不断提示下，我终于明白，这个if语句之后没有其它选项了，所以它必须接着
#     # 往下执行，全部执行结束，才会回到最初来把True改成False。
#
#     # TODO:2 check resources sufficient and return result yes or not 15@Dec
#     # TODO:3 deduct coffee ingredients from resources
#     # 为什么把这两个TODOs 放在一起，是因为它们只是完成一件事情的两个步骤。所以在决定函数要干什么的时候，一定要看的远一些，用哪些步骤来达到这个目标。
#
#     # 思路：把什么放进函数，之后产生什么。所以思路应该是f(a,b)，即把咖啡的ingredients dictionary其中的一组，用a放进去，resources其中的一组
#     # 用b放进去
#     # 不对，这个函数的唯一一个变量应该是user_input吧？？？？？？ 下面这11行，是我自己写的，到最后一行的括号下面有黄色的小波浪线，让我意识到，
#     # 这个函数的唯一变量应该是user_input, 而不是我resource_value。
#
#     # def compare_ingredients_required_and_available(resource_value):
#     #     for resource_value, resource_amount in resources.items():
#     #         ingredients_needed = MENU[user_input]["ingredients"][resource_value]
#     #         ingredients_available = resources[resource_value]
#     #
#     #         if ingredients_needed <  ingredients_available:
#     #             print("ok to proceed")
#     #         else:
#     #             print("not ok to proceed")
#     #
#     # print(compare_ingredients_required_and_available())
#
#     # TODO:2.1 新思路：批量比较所有共同key，注意.get()的使用 16@Dec: 看看能不能用user_input来取所有共同的key。
#     else:
#
#         make_drink(user_input, MENU, resources)
#         # print(resources)
#
#
#
#
#
#         # TODO:4 process coins 19 @ Dec
#         # TODO:5 check transaction successful
#         # 还是需要把这个函数到底要做什么先搞清楚，下面这个函数在思考的过程中就出现了“没有方向”的问题，即“下一步不知道该怎么写了、该做什么了”
#
#         quarters_inserted = int(input("Please insert coins. \nHow many quarters?: "))
#         dimes_inserted = int(input("How many dimes: "))
#         nickles_inserted = int(input("How many nickles: "))
#         pennies_inserted = int(input("How many pennies "))
#
#         total_coins_inserted = quarters_inserted * 0.25 + dimes_inserted * 0.1 + nickles_inserted * 0.05 + pennies_inserted * 0.01
#         # print(f"${total_coins_inserted}")
#         coffee_cost = MENU[user_input]["cost"]
#
#         change_to_user = make_transaction(total_coins_inserted, coffee_cost)
#
#         coffee_profit += MENU[user_input]["cost"]
#
#         print(f"Here is ${change_to_user:.2f} in change. ")
#         print("Here is your coffee. Enjoy! ")
#         # print(resources)
#
#
#
#
#         # TODO:6 make_coffee 25 Dec
#         # 整理！
#         # 今天把两个函数置顶，目的是让主程序看起来简洁
#         # TODO:6.1 make_coffee 26 Dec
#
#
#
#         # 拾遗
#         # 如何用.get(key, 0) 来确保抽取不在dictionary的key的时候不报错，而且显示你想让他显示的值，比如这里是“0”： print(resources.get("iron", 0))
