from turtle import Turtle,Screen
import random

def shape(timm,size,angle):
    i=0
    for i in range(size):

        if i==size:
            timm.right(0)
            timm.forward(100)
        else:
            timm.forward(100)
            timm.right(angle)

timm=Turtle()


for i in range (7):
    colors_typle=("#FF0000", "#00FF00", "#0000FF", "#FFFF00", 
        "#00FFFF", "#FF00FF", "#FFA500", "#800080", 
        "#FFC0CB", "#A52A2A")
    selected_color=random.choice(colors_typle)
    timm.pencolor(selected_color)
    shape(timm,3+i,360/(3+i))

screen=Screen()
screen.exitonclick()