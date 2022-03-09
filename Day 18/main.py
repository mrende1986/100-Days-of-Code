from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
tim.shape('turtle')
colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r,g,b)
    return color

# colors = ['blue', 'red','spring green','dark cyan']
# directions = [0,90,180,270]
tim.pensize(3)
tim.speed(0)

# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


# def draw_shape(num_sides):
#     angle = 360 / num_sides    
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)


# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)

def draw_spirograph(size_of_gap):    
    for _ in range(int(360 / size_of_gap)):
        tim.circle(100)
        tim.color(random_color())
        tim.setheading(tim.heading() + 10)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()