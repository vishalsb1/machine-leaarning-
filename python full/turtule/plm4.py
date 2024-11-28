from turtle import Turtle,Screen
import random
import turtle

turtle.colormode(255)
timm=Turtle()

def colour():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    colour_type=(r,g,b)
    return colour_type


def direction(tim):
    dire=random.choice((84, 65, 45, 3, 95, 26, 69, 14, 80, 83, 78, 56, 57, 15, 46, 68, 72, 1, 25, 50, 51, 60, 5, 28, 34, 39, 29, 37, 13, 81, 91, 38, 53, 7, 89, 66, 99, 61, 76, 71, 20, 77, 100, 33, 4, 64, 86, 40, 93, 42, 18, 11, 87, 17, 47, 24, 92, 49, 19, 55, 6, 9, 32, 8, 12, 36, 82, 59, 94, 21, 67, 62, 30, 22, 16, 35, 79, 52, 48, 41, 2, 63, 97, 43, 54, 31, 85, 23, 44, 96, 27, 73, 74, 75, 70, 58, 98, 88, 10, 90
))
    if(dire>=50):
        timm.right(90)
    else:
        timm.left(90)

# colours_tpl = ("#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#00FFFF", "#FF00FF", "#FFA500", "#800080", "#A52A2A", "#008000",
# "#800000", "#808000", "#000080", "#808080", "#FFC0CB", "#FFD700", "#ADFF2F", "#4B0082", "#FA8072", "#8B4513",
# "#DC143C", "#2E8B57", "#7FFF00", "#FF1493", "#FF4500", "#BA55D3", "#9932CC", "#EE82EE", "#6A5ACD", "#483D8B",
# "#4682B4", "#5F9EA0", "#20B2AA", "#7FFFD4", "#00CED1", "#40E0D0", "#48D1CC", "#1E90FF", "#B0C4DE", "#ADD8E6",
# "#87CEFA", "#6495ED", "#4169E1", "#00008B", "#191970", "#B22222", "#CD5C5C", "#8B0000", "#A52A2A", "#B8860B",
# "#D2691E", "#FF8C00", "#F4A460", "#DEB887", "#D2B48C", "#BC8F8F", "#F5DEB3", "#FFE4B5", "#FFDAB9", "#FFE4C4",
# "#FFEBCD", "#FFEFD5", "#FAEBD7", "#F5F5DC", "#FFF8DC", "#FDF5E6", "#FFFAF0", "#FFFACD", "#FAFAD2", "#FFF5EE",
# "#F8F8FF", "#F0F8FF", "#E6E6FA", "#D8BFD8", "#DDA0DD", "#EE82EE", "#DA70D6", "#FF00FF", "#BA55D3", "#9400D3",
# "#9932CC", "#8A2BE2", "#9370DB", "#8B008B", "#800080", "#4B0082", "#6A5ACD", "#483D8B", "#7B68EE", "#0000CD",
# "#00008B", "#000080", "#191970", "#4682B4", "#5F9EA0", "#6495ED", "#00BFFF", "#1E90FF", "#ADD8E6", "#87CEEB"
# )

timm.hideturtle()
timm.pensize(15)
timm.speed(10)
for i in range(150):
    timm.pencolor(colour())
    timm.forward(30)
    direction(timm)
    
screen=Screen()
screen.exitonclick()