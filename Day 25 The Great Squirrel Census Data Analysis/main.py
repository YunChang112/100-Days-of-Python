# data = []
# with open("weather_data.csv") as f:
#     raw_data = f.readlines()
#     for row in raw_data:
#         new_data = row.strip().split(",")
#         data.append(new_data)
# print(data)
# for row in data:
#     print(row)
import numpy as np
# import csv
# with open("weather_data.csv") as f:
#     data = list(csv.reader(f))
#     # 这里用list，是强制把迭代器里的内容全部“掏出来”存进列表，才能下面的内容顶头写，不然的话窗口关闭，只能缩进写了
# temperature = []
# for row in data[1:]:
#     temperature.append(int(row[1]))
# print(temperature)

# temperature_1 = []
# for row in temperature:
#     new_data = int(row)
#     temperature_1.append(new_data)
# print(temperature_1)

import pandas
data = pandas.read_csv("weather_data.csv")
# print(data)
# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
#
# total_temp = sum(temp_list)
# print(total_temp)
#
# average_temp = total_temp / len(temp_list)
# print(average_temp)

# print(data["temp"].mean())
#
# print(data["temp"].max())

# Get Data in Columns
# print(data["condition"])
# print(data.condition)

# Get Data in Row
# print(data[data.day == "Monday"])

# max_temp = data.temp.max()
# print(data[data.temp == max_temp])

monday = data[data.day == "Monday"]
# print(monday.condition)
# print(monday.temp)
print(type(monday.temp[0]))
# print(type(monday.temp))
# monday_Fahrenheit = monday.temp[0] * 9 / 5 + 32
# print(monday_Fahrenheit)

# Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data_1 = pandas.DataFrame(data_dict)
# print(data_1)
# pandas.DataFrame(data_dict).to_csv("student_scores.csv")

import pandas
primary_data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260215.csv')
# print(type(primary_data))

squirrel_number_colum = primary_data["Primary Fur Color"]
# print(type(squirrel_number_colum))


"""以下是用笨办法把.csv文件生成"""

# gray_colour = primary_data[primary_data["Primary Fur Color"] == "Gray"]
# # print(gray_colour)
# gray_colour_number = (len(gray_colour))
#
# red_colour = primary_data[primary_data["Primary Fur Color"] == "Cinnamon"]
# red_colour_number = (len(red_colour))
#
# black_colour = primary_data[primary_data["Primary Fur Color"] == "Black"]
# black_colour_number = (len(black_colour))
#
# data_dict = {
#     "fur color": ["gray", "red", "black"],
#     "Count": [gray_colour_number, red_colour_number, black_colour_number],
# }
#
# pandas.DataFrame(data_dict).to_csv("squirrel_count.csv")

"""以下，是用Pandas API的series里自带的命令生成"""

index = squirrel_number_colum.value_counts().reset_index()
pandas.DataFrame(index).to_csv('Squirrel_2.csv')

# print(index)