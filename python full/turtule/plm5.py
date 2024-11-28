from turtle import Turtle,Screen
import random
import turtle

turtle.colormode(255)
def colour():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    colour_type=(r,g,b)
    return colour_type

def sterigram(num):
    for i in range (int(360/num)):
        tim.pencolor(colour())
        tim.circle(100)
        tim.right(5)


tim=Turtle()
tim.speed(15)

# input
sterigram(int(input("tell the input: ")))


screen=Screen()
screen.exitonclick()