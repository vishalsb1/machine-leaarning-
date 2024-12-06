from turtle import Turtle ,Screen 
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

import time

screen=Screen()
screen.setup(600,600)
screen.tracer(0)
screen.listen()
# turtle
tim=Player()
cars=CarManager()
scrbrd=Scoreboard()

# key hoods 
screen.onkeypress(tim.move,"Up")


game_is_on=True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.moveC()
    if tim.ycor()> 240 :
        tim.go_to_start()
        cars.increase_speed()
        scrbrd.write2()
        
    for car in cars.all_cars:
        if tim.distance(car) < 20:
            scrbrd.gameOff()
            game_is_on=False


screen.exitonclick()