from turtle import Turtle
FONT=("Arial",22,"normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.goto(-270,265)
        self.write(f"Level : {self.level}",align='left',font=FONT)

    def write2(self):
        self.level+=1
        self.clear()
        self.write(f"Level : {self.level}",align='left',font=FONT)
        
    def gameOff(self):
        self.clear()
        self.goto(0,0)
        self.write("GameOver",align='left',font=FONT)
