# import colorgram

# colors = colorgram.extract('Day 18/image.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

color_list = [(14, 25, 61), (196, 175, 135), (70, 10, 20), (51, 23, 13), (159, 77, 42), (218, 226, 234), (206, 199, 149), (10, 44, 24), (53, 100, 146), (146, 18, 34), (164, 21, 12), (121, 182, 158), (44, 119, 81), (123, 166, 187), (157, 60, 86), (236, 219, 224), (216, 168, 19), (22, 88, 51), (201, 90, 72), (21, 44, 118), (162, 211, 162), (193, 146, 154), (183, 90, 110), (69, 180, 91), (222, 180, 169), (15, 81, 101), (228, 162, 172), (229, 202, 14)]

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed(0)
tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(250)
tim.setheading(0)
number_of_dots = 101

for dot_count in range(1, number_of_dots):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




screen = turtle_module.Screen()
screen.exitonclick()