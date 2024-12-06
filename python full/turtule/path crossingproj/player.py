from turtle import Turtle


start_pos=(0,-250)
move_distance=10
finish_line_y=250

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.go_to_start()
        self.move()
    
    def move(self):
        self.forward(move_distance)

    def go_to_start(self):
        self.goto(start_pos)



