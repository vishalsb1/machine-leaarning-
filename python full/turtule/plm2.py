from turtle import Turtle,Screen

timm=Turtle()

for i in range(0,20):
    timm.pendown()
    timm.forward(10)
    timm.penup()
    timm.forward(10)

screen=Screen()
screen.exitonclick()