from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.all_car = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        frequency = random.randint(1,6)
        if frequency == 1:
            new_y = random.randint(-250, 250)
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(280, new_y)
            self.all_car.append(new_car)

    def car_move(self):
        for each_car in self.all_car:
            each_car.backward(self.car_speed)
            # 上面是“向量思维”，下面是我自己写的，当时卡在了如何表达y轴坐标不变上）
            # new_x = each_car.xcor() - STARTING_MOVE_DISTANCE
            # each_car.penup()
            # each_car.goto(new_x, each_car.ycor())

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

