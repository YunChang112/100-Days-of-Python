# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

#TODO 1. Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_list = {row.letter:row.code for (index, row) in data.iterrows()}
print(data_list)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

"""Angela的版本"""
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        letter_list = [data_list[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(letter_list)

generate_phonetic()

# while True:
#     user_word = input("Enter a word:").upper()
# letter_list = []
# for letter in user_word:
#     each_letter = data_list[letter]
#     letter_list.append(each_letter)
# print(letter_list)

"""我们可以把try块想象成一个“手术室”，里面待的时间越长、动的手术越多，发生意外可能性就越高"""

# 第一种
#     try:
#         letter_list = [data_list[each_letter] for each_letter in user_word]
#         break
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
#
# print(letter_list)

"""优点：try块及其精简，只包含了最可能报错的那行代码。
缺点： 逻辑略显断裂。Break之后直接跳到了循环外的print。如果这段代码是在一个很长的函数里，别人可能一眼看不出print(letter_list)是
属于成功后的动作还是无论如何都要执行的动作。"""

# 第二种
#     try:
#         letter_list = [data_list[each_letter] for each_letter in user_word]
#         print(letter_list)
#         break
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")

"""优点：读起来最符合人类直觉。逻辑是：“试着做这件事，成功了就打印并退出”。
缺点：“误伤风险”。如果print语句因为某种极罕见的原因（比如输出流被关闭）报错了，它产生的错误会被except KeyError尝试捕获。虽然这里指定了
KeyError比较安全，但如果携程通用的except Exception， 你就永远不知道到底是“转换”报错了还是“打印”报错了。"""

# 第三种
#     try:
#         letter_list = [data_list[each_letter] for each_letter in user_word]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
#     else:
#         print(letter_list)
#         break

"""优点：完美的职责分离
1、try只负责“可能出错的危险操作”
2、else负责“成功后的奖励操作”
3、它清晰地告诉后来的开发者：转换逻辑已经结束了，现在的打印和退出是确定没问题后才做的。
缺点：代码行数略多，对于初学者来说可能觉得else有点多余。
适用场景：正式项目、需要高度严谨性的代码。"""

