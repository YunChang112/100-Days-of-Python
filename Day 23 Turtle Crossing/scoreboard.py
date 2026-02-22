from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.update_level()

    def update_level(self):
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", font= FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_level()

    def game_over(self):
        self.goto(-40,0)
        self.write("GAME OVER", font= FONT)

    # def __init__(self):
    #     super().__init__()
    #     self.level = 1
    #     self.hideturtle()
    #     self.penup()
    #     self.goto(-280, 260)
    #     self.update_scoreboard()
    #
    # def update_scoreboard(self):
    #     self.clear()
    #     self.write(f"Level: {self.level}", align="left", font=FONT)
    #
    # def increase_level(self):
    #     self.level += 1
    #     self.update_scoreboard()
    #
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align="center", font=FONT)
    #

