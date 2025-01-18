# Course TODO
# TODO-1: Move the turtle with keypress
# TODO-2: Create and move the cars
# TODO-3: Detect collision with car
# TODO-4: Detect when turtle reaches the other side
# TODO-5: Create a scoreboard

import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars_manager.create_cars()
    cars_manager.move_cars()

    # Detect collision with car
    for car in cars_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        cars_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()