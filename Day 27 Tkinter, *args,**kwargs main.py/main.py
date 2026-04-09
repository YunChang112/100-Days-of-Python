from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

def action():
    user_input = float(entry.get())
    result = user_input * 1.609
    label_0.config(text=f"{result}")
    # user_input = entry.get()
    # result = round((int(user_input) * 1.6), 2)
    # label_0.config(text=result)

entry = Entry(width=10)
entry.insert(END, string="0")
entry.focus()
entry.grid(column=1, row=0)

label_Mile = Label(text="Miles", font=("Arial", 24, "bold"))
label_Mile.grid(column=2, row=0)

label_is_equal_to = Label(text="is equql to", font=("Arial", 24, "bold"))
label_is_equal_to.grid(column=0, row=1)

label_0 = Label(text="0", font=("Arial", 24, "bold"))
label_0.grid(column=1, row=1)

label_Km = Label(text="Km", font=("Arial", 24, "bold"))
label_Km.grid(column=2, row=1)

button_Calculate = Button(text="Calculate", command=action)
button_Calculate.grid(column=1, row=2)


"""
以下是课程练习, 上面的代码是这一课的题目以及我的答案
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label["text"] = new_text


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# my_label.pack()
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button
button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

# New Button
new_button = Button(text="Click Me", command=button_clicked)
new_button.grid(column=2, row=0)

#  Entry
input = Entry(width=10)
print(input.get())
# input.pack()
input.grid(column=3, row=2)
"""

window.mainloop()
