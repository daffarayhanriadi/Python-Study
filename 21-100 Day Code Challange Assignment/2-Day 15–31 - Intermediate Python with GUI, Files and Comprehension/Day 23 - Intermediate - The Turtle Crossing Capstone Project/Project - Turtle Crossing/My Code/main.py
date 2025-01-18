# My TODO
# TODO-1: Create and Move A Player
# TODO-2: Create and Move 6 Cars
# TODO-3: Detect Collision with Car
# TODO-4: Keep the Scoreboard
# TODO-5: Detect Collision with Wall and Increase the Speed

import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
cars_manager = CarManager()
scoreboard = Scoreboard()

for _ in range(0, 6):
    cars_manager.x_cor = random.randint(-280, 280)
    cars_manager.y_cor = random.randint(-240, 240)
    cars_manager.generate_car()

screen.listen()
screen.onkeypress(player.move, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars_manager.move()

    for car in cars_manager.all_cars:
        if abs(car.xcor()) > 320:
            cars_manager.all_cars.remove(car)
            cars_manager.x_cor = 280
            cars_manager.y_cor = random.randint(-240, 240)
            cars_manager.generate_car()

        if car.distance(player) < 30:
            scoreboard.game_over()
            game_is_on = False

        if player.ycor() > 280:
            player.reset_position()
            cars_manager.increase_speed()
            scoreboard.increase_scoreboard()

screen.exitonclick()