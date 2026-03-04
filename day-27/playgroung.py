"""
Modify the add function to make an unlimited number of arguments.
Use a loop to sum all the arguments inside the function.
Test it out by calling add() to calculate sum of some arguments
"""

"""
这是我自己手搓的，用最朴素的思路
"""
# def add(*args):
#     arguments_list = []
#     for n in args:
#         arguments_list.append(n)
#     return(sum(arguments_list))
#
#
# try_out = add(4,7,2,6,9,7,9,3,5,7,)
# print(try_out)

"""
这是Gemini给我的建议，一句话，
“其实*args在被接受的那一刻，它在python内部就已经是一个元组(tuple)了，都是可迭代对象(iterable).
"""
# def add(*args):
#     return sum(args)
#
# try_out_2 = add(4,5,3,4,5,6,3,4,)
# print(try_out_2)

"""
这是Angela的题目答案：
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum
"""

# kwargs
def calculate(**kwargs):
    print(type(kwargs))
    # print(kwargs)
    #
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    print(kwargs["add"])

calculate(add=3, multipy=5)


