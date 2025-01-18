from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.x_cor = 0
        self.y_cor = 0
        self.speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        car = Turtle()
        car.penup()
        car.shape("square")
        car.shapesize(stretch_wid=2, stretch_len=1) # Height = 20px (1*20), Width = 40px (2*20)
        car.setheading(180)
        car.color(random.choice(COLORS))
        car.goto(self.x_cor, self.y_cor)
        self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.forward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT