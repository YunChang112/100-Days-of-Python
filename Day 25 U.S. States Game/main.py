import turtle
import pandas

"""0.
1. Convert the guess to Title case
2. Check if the guess is among the 50 states
3. Write correct guesses onto the map
4. Use a loop to allow the user to keep guessing
5. Record the correct guesses in a list
6. Keep track of the score"""

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

def write_state_name(state_x_cor, state_y_cor, state_name):
    writer.goto(state_x_cor,state_y_cor)
    writer.write(state_name,font=("Arial",20,"bold"))

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("/Users/yunchang/PycharmProjects/day-25-us-states-game-start/50_states.csv")

all_states = states_data.state.to_list()
correct_states_name = []

"""以下是Gemini写的"""
while len(correct_states_name) < 50:  # 当猜满50个自动结束
    answer_state = screen.textinput(title=f"{len(correct_states_name)}/50 States Correct",
                                        prompt="What's another state's name?").title()
        # 1. 检查退出
    if answer_state == "Exit":
            break

        # 2. 检查是否在 50 个州里，且没被猜过
    if answer_state in all_states and answer_state not in correct_states_name:
        correct_states_name.append(answer_state)
            # 提取数据
        state_info = states_data[states_data.state == answer_state]
            # 你的 .item() 用法非常棒，保留！
        write_state_name(state_info.x.item(), state_info.y.item(), answer_state)

missing_states = []
for state in all_states:
    if state not in correct_states_name:
        missing_states.append(state)
# new_list = [state for state in all_states if state not in missing_states]

"""Gemini建议写法：
new_data = pandas.DataFrame(missing_states, columns = ["State"])
保存时去掉索引
new_data.to_csv("states_to_learn.csv", index = False)"""
states_to_learn = pandas.DataFrame(missing_states,columns=["State"]).to_csv("states_to_learn.csv", index = False)


"""以下是我写的：当时有这么几个疑问：
1、坐标点的找到，当时可以根据answer_state把州那一行找到了，在把x、y找到，但需要.item()最终把它取出来。也给了.ilo[0]的方法：代表永远
“物理位置的第一行”。同时，series里面的标签对应的是整个数据的标签，并不是series里面的位置标签，这个很重要！
2、在检测user输入的名字是否在州名字list里面的时候，我的想法就是直接用not in去series排查，但这个排查的是标签，所以我就去pandas document
查到了.isin(),结果跑通了。Gemini也建议要么在state_data.state后面直接加.values，要么直接把series变成list，.to_list()。这个思路很好！

game_is_on = True
while game_is_on:
all_states = states_data.state.to_list()
correct_states_name = []

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
# if answer_state not in states_data.state:
if not states_data["state"].isin([answer_state]).any():
    print("State not in the list")
    continue
elif answer_state in correct_states_name:
    print("You guessed the state")
state_info = states_data[states_data.state == answer_state]
write_state_name(state_info["x"].item(), state_info["y"].item(), answer_state)
correct_states_name.append(answer_state)
score += 1"""

#     print(correct_states_name)
#     print(score)
#
#
# turtle.mainloop()


"""以下代码是在鼠标点击屏幕的时候，会print这个点的（x，y）坐标"""
# def get_mouse_click_coor(x,y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)


"""看Gemini给的解释，理解series在pandas里的位置、关系。"""
# print(states_info["x"].loc[34])
# print(states_info["x"].iloc[0])
# print(states_info["x"].item())