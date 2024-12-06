from turtle import Turtle
import random

colors = ("red", "orange", "yellow", "green", "blue", "indigo", "violet")
start_dis=5
move_increment=10


class CarManager():
    def __init__(self):
        self.all_cars=[]
        self.speed=start_dis

    def create_car(self):
        ran_choice=random.randint(1,6)
        if ran_choice == 1:
            car=Turtle("square")
            car.shapesize(1,2)
            car.penup()
            self.xc=240
            self.yc=random.randint(-240,240)
            car.goto(self.xc,self.yc)
            ran_col=random.choices(colors)
            car.color(ran_col)
            self.all_cars.append(car)
        

    def moveC(self):
        for cars in self.all_cars:
            cars.speed('slowest')
            cars.backward(self.speed)
    
    def increase_speed(self):
        self.speed+=move_increment
            