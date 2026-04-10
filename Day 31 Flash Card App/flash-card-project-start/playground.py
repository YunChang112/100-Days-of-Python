import random
import pandas

data = pandas.read_csv("data/french_words.csv")
new_data = data.to_dict(orient="records")
print(random.choice(new_data)["French"])


# with open ("data/french_words.csv") as f:
#     raw_data = f.readlines()
#
# data_1 = [row.strip().split(",") for row in raw_data]
# print(data_1)
# # french_word = [word_list[0] for word_list in data]
# # random_french_word = random.choice(french_word)
#
# import csv
# with open ("data/french_words.csv") as f:
#     data = list(csv.reader(f))
# print(data)

# data = pandas.read_csv("data/french_words.csv")
#
# french_column = data["French"]
# french_column_list = data["French"].to_list()
# random_french = random.choice(french_column_list)
# print(random_french)

# french_english = data.dict()
# print(french_english)