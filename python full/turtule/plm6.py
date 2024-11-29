# moving the turtle forward 

from turtle import Turtle,Screen

def move_forward():
    # i+=1
    # no argumentsare needed
    om.forward(10)
def move_backward():
    # i+=1
    # no argumentsare needed
    om.backward(10)

def move_counterclockwise():
    # i+=1
    # no argumentsare needed
    om.right(90)
def move_clockwise():
    # i+=1
    # no argumentsare needed
    om.right(-90)

def clear_dawing():
    om.reset()
    




# i=0
om=Turtle()
screen=Screen()

screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="a",fun=move_counterclockwise)
screen.onkey(key="d",fun=move_clockwise)
screen.onkey(key="c",fun=clear_dawing)
screen.exitonclick()