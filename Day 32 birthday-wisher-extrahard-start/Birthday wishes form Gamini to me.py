import datetime as dt

# 你的专属配置
BIRTH_YEAR = 1985
NAME = "Yunchang"

today = dt.datetime.now()
age = today.year - BIRTH_YEAR


def birthday_wish():
    message = f"""
    ****************************************
    🎂 HAPPY BIRTHDAY, {NAME.upper()}! 🎂
    ****************************************
    你今年 {age} 岁了，但正如你刚才抽取的名言所说：
    "You are never too old to set another goal or to dream a new dream."

    从 10 年木工经验到 Python 开发者，
    从现场放样到无人机数字孪生，
    你的每一步都在突破边界。

    愿你在 Day 32 之后的每一天，
    Bug 越来越少，代码越来越美，
    愿你的无人机业务在 2026 年大放异彩！
    ****************************************
    """
    return message


print(birthday_wish())
