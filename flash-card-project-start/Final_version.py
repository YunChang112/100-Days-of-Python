from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
flip_timer = None

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

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


def is_know():
    global current_card, to_learn
    to_learn.remove(current_card)
    pandas.DataFrame(to_learn).to_csv("data/words_to_learn.csv", index=False)
    next_card()

# -------------------------------------------------UI SETUP---------------------------------------#

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

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
known_button = Button(image=check_image, highlightthickness=0, command = is_know)
known_button.grid(column=1, row=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command = next_card)
unknown_button.grid(column=0, row=2)

next_card()

window.mainloop()