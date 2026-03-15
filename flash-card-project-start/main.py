from tkinter import *
from tkinter import messagebox
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")

# to_learn_words = [] 这个是下面我的版本才需要的list，以下有详尽解释。
try:
    new_data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    to_learn = to_learn
else:
    to_learn = new_data.to_dict(orient="records")

current_card = {}
# used_card = {} 我竟然不记得这个是什么意思？也不记得是我自己写的了。#之后竟然没有对程序起到任何变化。
"""把下面这个timer放在这里，是Gemini建议的，而且增加一个if，来增加程序的鲁棒性。"""
flip_timer = None

# -------------------------------------------------FUNCTION SETUP---------------------------------------#

def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

def next_card():
    global current_card, flip_timer
    if flip_timer:
        window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)


def next_card_know():
    to_learn.remove(current_card)
    pandas.DataFrame(to_learn).to_csv("data/words_to_learn.csv", index=False)
    next_card()


"""跑通了！其实下面这三个def也是保守了，正如我和Gemini讨论的，我在试图用代码逻辑去对抗可能的操作失误。其实是我的大脑，在规划flow chart的时候，
潜意识中没有找到用简单方法来建立正确逻辑的能力，所以，引导我走了如下三个def的路，现在让我来试试，把代码简化，如上。"""
# def flip_card():
#     canvas.itemconfig(canvas_image, image=card_back_img)
#     canvas.itemconfig(card_title, text="English", fill="white")
#     canvas.itemconfig(card_word, text=current_card["English"], fill="white")
#
# def next_card_know():
#     global current_card, flip_timer
#     if flip_timer:
#         window.after_cancel(flip_timer)
#     pandas.DataFrame(to_learn).to_csv('words_to_learn.csv')
#     current_card = random.choice(to_learn)
#     to_learn.remove(current_card)
#     canvas.itemconfig(canvas_image, image=card_front_img)
#     canvas.itemconfig(card_title, text="French", fill="black")
#     canvas.itemconfig(card_word, text=current_card["French"], fill="black")
#     flip_timer = window.after(3000, func=flip_card)
#
# def next_card_unknow():
#     global current_card, flip_timer
#     if flip_timer:
#         window.after_cancel(flip_timer)
#     pandas.DataFrame(to_learn).to_csv('words_to_learn.csv')
#     current_card = random.choice(to_learn)
#     canvas.itemconfig(canvas_image, image=card_front_img)
#     canvas.itemconfig(card_title, text="French", fill="black")
#     canvas.itemconfig(card_word, text=current_card["French"], fill="black")
#     flip_timer = window.after(3000, func=flip_card)

"""下面这个逻辑是把不会的存入到新的.csv里面，但经过和Gemini的沟通，我发现这个逻辑是错误的，比如，第一次打开，做了一半，就关机了，
那么，剩下的，无论会不会，都不会被存入新的列表中了。所以，我把下面这两个def都换了，是因为我刚才意识到，如果要用Gemini对Angela题目的理解，
我只要在next_card()里面，把内存中的list导入words_to_learn.csv即可，而我之前以为的，存入新的csv应该在cross_button才用到的，
现在应该是放在tick_button里面，这个逻辑才对的，要不然，第一个单词如果不会的话，也永远被删除，不会被存入新的.csv里面去。"""
# def next_card():
#     global current_card, flip_timer
#     if flip_timer:
#         window.after_cancel(flip_timer)
#     """下面这个if语句是我想到的最后没有词的话会怎么办，当时忘记写return了， Gemini帮我填了坑。先隐藏起来，看看Angela如何来解决最后没有
#     单词可抽的问题。"""
#     # if len(to_learn) < 1:
#     #     messagebox.showinfo(title="Hello", message="No more words to learn.")
#     #     return
#     current_card = random.choice(to_learn)
#     to_learn.remove(current_card)
#     canvas.itemconfig(canvas_image, image=card_front_img)
#     canvas.itemconfig(card_title, text="French", fill="black")
#     canvas.itemconfig(card_word, text=current_card["French"], fill="black")
#     flip_timer = window.after(3000, func=flip_card)
#     """如下两个if\else语句，是我想的，通过这个方法，来判定用最初的完整单词表，还是被筛检出来不会的单词表。但一眼看出来臃肿，而且这个==0
#     也不对，跑不通，还是直接进的是完整单词表。于是咨询Gemini，它说，无论用哪个单词表，都用to_learn这一个list跑全局"""
#     # if len(words_to_learn) == 0:
    #     current_card = random.choice(to_learn)
    #     to_learn.remove(current_card)
    #     canvas.itemconfig(canvas_image, image=card_front_img)
    #     canvas.itemconfig(card_title, text="French", fill="black")
    #     canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    #     flip_timer = window.after(3000, func=flip_card)
    # else:
    #     current_card = random.choice(words_to_learn)
    #     words_to_learn.remove(current_card)
    #     canvas.itemconfig(canvas_image, image=card_front_img)
    #     canvas.itemconfig(card_title, text="French", fill="black")
    #     canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    #     flip_timer = window.after(3000, func=flip_card)

# def save_and_next_card():
#     global current_card, flip_timer
#     if flip_timer:
#         window.after_cancel(flip_timer)
#     pandas.DataFrame(to_learn).to_csv('words_to_learn.csv')
#     current_card = random.choice(to_learn)
#     to_learn.remove(current_card)
#     canvas.itemconfig(canvas_image, image=card_front_img)
#     canvas.itemconfig(card_title, text="French", fill="black")
#     canvas.itemconfig(card_word, text=current_card["French"], fill="black")
#     flip_timer = window.after(3000, func=flip_card)


"""以下这个思路，是我最初的、原始的、朴素的，简单一句话就是没有经过深思熟虑、仅凭简单意会Angela的题意，而自己脑补的UI程序过程。
在和Gemini仔细沟通之后，我明白了我和它对题意理解的偏差：
我这个的版本的指向：是每次把不认识的单词存进words_to_learn.csv；
而它的版本的过程指向，是把不会的和还没有出现的单词全部存入words_to_learn.csv，之后，会的，从current_card，即内存中的list删掉；
不会的以及剩下的单词，全部覆盖之前的words_to_learn.csv,即一直是“瘦身版”。"""
# def save_and_next_card():
#     global current_card, flip_timer
#     if flip_timer:
#         window.after_cancel(flip_timer)
#     """下面这个if语句是我想到的最后没有词的话会怎么办，当时忘记写return了， Gemini帮我填了坑。先隐藏起来，看看Angela如何来解决最后没有
#     单词可抽的问题。"""
#     # if len(to_learn) < 1:
#     #     messagebox.showinfo(title="Hello", message="No more words to learn.")
#     #     return
#     """在这里把按X键之后的单词存进了words_to_learn这个新的list里面"""
#     to_learn_words.append(current_card)
#     current_card = random.choice(to_learn)
#     to_learn.remove(current_card)
#     """这一步是把每次有新词加进去之后导出.csv文件"""
#     pandas.DataFrame(to_learn_words).to_csv('words_to_learn.csv')
#     canvas.itemconfig(canvas_image, image=card_front_img)
#     canvas.itemconfig(card_title, text="French", fill="black")
#     canvas.itemconfig(card_word, text=current_card["French"], fill="black")
#     flip_timer = window.after(3000, func=flip_card)
#     print(current_card)
#     print(to_learn_words)



# 以下，要表达python中，代码是“从上往下执行”的，如下，func=flip_card下面才是flip_card()，就会报错；就算把它整体搬到func=flip_card
# 上面，又会出现“叫不到”current_word的作用域scope的问题,所以就在如上，加入了global。
# def next_card():
#     current_card = random.choice(to_learn)
#     canvas.itemconfig(card_title, text="French")
#     canvas.itemconfig(card_word, text=current_card["French"])
#     def flip_card():
#         canvas.create_image(400, 263, image=card_back_img)
#         canvas.itemconfig(card_title, text="English", fill="white")
#         canvas.itemconfig(card_word, text=current_card["English"], fill="white")
#     window.after(3000, func=flip_card)


"""以下是三种方法来达到转换数据、随机抽取数据的方法，都是我自己摸索出来,只是把csv转换成list。上面的才是按照Angela的转换成dic来用"""
# def show_french_word():
#     french_column = data["French"]
#     french_column_list = french_column.to_list()
#     random_french_word = random.choice(french_column_list)


# 下面这个import csv，也是python原生自带的功能，但每次使用必须import，但不需要下载，它的结果和readlines()+strip()+split()是一样的。
# import csv
# with open ("data/french_words.csv") as f:
#     data = list(csv.reader(f))


# 下面这个show_french_word()函数，是我用python原生态的readiness()函数搭建的。感觉很爽，硬核碰撞python list性能。
# def show_french_word():
#     with open ("data/french_words.csv") as f:
#         raw_data = f.readlines()
#
#     data = [row.strip().split(",") for row in raw_data]
#     french_word = [word_list[0] for word_list in data]
#     random_french_word = random.choice(french_word)
#

# --------------------------------------------------UI SETUP--------------------------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

"""把flip_timer放在这里，是Angela的方法，而Gemini建议放在最上面，并赋值None，并在下面用if检测，是否存在。"""
# flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)

# Card_text
card_title = canvas.create_text(400, 150, text="title", font=("Ariel", 40, "italic"),fill="black")
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"), fill="black")

canvas.grid(column=0, row=0, columnspan=2)

# Buttons
check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command = next_card_know)
known_button.grid(column=1, row=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command = next_card)
unknown_button.grid(column=0, row=2)

next_card()

window.mainloop()

# 如下是我第一次写的，把两个card都放上去了，所以，后写的会覆盖前面写的。上面的是Gemini建议的，先写一个，稍后在逻辑部分再切换图片。
# card_front_img = PhotoImage(file="/Users/yunchang/Desktop/Pycharm Projects/100 Days of Code - The Complete"
#                                  " Python Pro Bootcamp/Day 31 Flash Card App/flash-card-project-start/images/"
#                                  "card_front.png")
# canvas.create_image(400, 250, image=card_front_img)
# canvas.grid(column=0, row=0, columnspan=2)
#
# card_back_img = PhotoImage(file="/Users/yunchang/Desktop/Pycharm Projects/100 Days of Code - The Complete"
#                                 " Python Pro Bootcamp/Day 31 Flash Card App/flash-card-project-start/images/"
#                                 "card_back.png")
# canvas.create_image(400, 250, image=card_back_img)
# canvas.grid(column=0, row=0, columnspan=2)
