from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

# class Scoreboard(Turtle):
#
#     def __init__(self):
#         super().__init__()
#         self.goto(-20, 270)
#         self.hideturtle()
#         self.color("white")
#         self.score = 0
#
#     def current_score(self):
#         self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
#
#     def update_score(self):
#         self.clear()
#         self.score += 1


class Scoreboard(Turtle):
    """Angela的版本，比我的在main.py里面少了一行，处于“懒惰”，把计分牌的职责封装在分数变化的那一刻！"""
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align = ALIGNMENT, font = FONT)

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self. update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()